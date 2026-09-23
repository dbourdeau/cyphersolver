"""Build the DECODE upload package from decode_updates/queue.json.

For every queued record not yet sent, writes decode_updates/out/R<id>/:
  additional_information.txt  the line to append to the record's Additional Information
  fields.txt                  status and descriptive-field changes
  key.txt                     DECODE key format, only when the key was rebuilt here (not when it is already in DECODE)
  decryption.txt              DECODE header + our reading

Usage: python decode_updates/build.py [target ...]     (run from the repo root)
       python decode_updates/build.py --check          list records with no reading or no key file
"""
import html
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = os.path.join(ROOT, 'decode_updates', 'queue.json')
OUT = os.path.join(ROOT, 'decode_updates', 'out')
LANG = {'IT': 'Italian', 'ES': 'Spanish', 'FR': 'French', 'DE': 'German', 'NL': 'Dutch', 'HU': 'Hungarian'}
BY = 'Dan Bourdeau'
DATE = 'September 2026'


def read(path):
    return open(os.path.join(ROOT, path), encoding='utf-8').read()


def key_lines(path):
    """Convert a key file (json dict, tsv, markdown table or ready DECODE lines) to 'code - value' lines."""
    text = read(path)
    if path.endswith('.json'):
        d = json.loads(text)
        out = []
        for k, v in d.items():
            if isinstance(v, list):
                v = '|'.join(v)
            out.append(f'{k} - {v if v else "<unknown>"}')
        return out
    if path.endswith('.tsv'):
        rows = [l.split('\t') for l in text.splitlines() if l.strip()]
        head = [h.lower() for h in rows[0]]
        out = []
        for r in rows[1:]:
            if len(r) < 2:
                continue
            line = f'{r[0]} - {r[1]}'
            if 'confidence' in head and len(r) > head.index('confidence') and r[head.index('confidence')] != 'confirmed':
                line += f'   <NOTE ED {r[head.index("confidence")]}>'
            out.append(line)
        return out
    if path.endswith('.md'):
        rows = [[c.strip() for c in l.strip().strip('|').split('|')]
                for l in text.splitlines() if l.lstrip().startswith('|')]
        rows = [r for r in rows if not set(''.join(r)) <= set('-: ')]
        head = [h.lower() for h in rows[0]]
        # a table is either sign -> value or value -> signs
        if head[0] in ('plain', 'clear', 'value'):
            out = []
            for r in rows[1:]:
                for s in re.split(r',\s*', r[1]):
                    if s:
                        out.append(f'{s} - {r[0]}')
            return out
        return [f'{r[0]} - {r[1]}' for r in rows[1:] if len(r) > 1]
    return [l for l in text.splitlines()]


def key_file(rec, t, q):
    k = q['key']
    lang = k.get('lang', '')
    head = ['#KEY: reconstructed', f'#CATALOG NAME: DECODE {rec} ({t})', f'#LANGUAGE: {lang}',
            f'#TRANSCRIBER NAME: {BY}', f'#DATE OF TRANSCRIPTION: {DATE}', '#STATUS: reconstructed',
            f'#COMMENT: {k.get("how", "")}. Write-up: {q["writeup"]}', '']
    body = []
    for f in [k.get('file'), k.get('file2')]:
        if f:
            if len(body):
                body += ['', f'<NOTE ED second key, from {os.path.basename(f)}>']
            body += key_lines(f)
    return '\n'.join(head + body) + '\n'


def extract(src):
    text = read(src['file'])
    if 'section' in src and src['file'].endswith('.html'):
        m = re.search(r'<h2 id="%s".*?</h2>(.*?)(?=<h2 |</main>|$)' % re.escape(src['section']), text, re.S)
        if not m:
            raise SystemExit(f"{src['file']}: no <h2 id=\"{src['section']}\">")
        body = re.sub(r'</(p|li|div|tr|h3)>|<br\s*/?>', '\n', m.group(1))
        body = html.unescape(re.sub(r'<[^>]+>', '', body))
        return '\n'.join(l.strip() for l in body.splitlines() if l.strip())
    if 'section' in src:
        lines = text.splitlines()
        start = next((i for i, l in enumerate(lines) if l.startswith('#') and src['section'] in l), None)
        if start is None:
            raise SystemExit(f"{src['file']}: no heading containing {src['section']!r}")
        level = len(lines[start]) - len(lines[start].lstrip('#'))
        end = next((i for i in range(start + 1, len(lines))
                    if lines[i].startswith('#') and len(lines[i]) - len(lines[i].lstrip('#')) <= level), len(lines))
        return '\n'.join(lines[start:end]).strip()
    if 'block' in src:
        parts = re.split(r'(?m)^(?===)', text)
        p = next((p for p in parts if p.startswith(src['block'])), None)
        if p is None:
            raise SystemExit(f"{src['file']}: no block starting {src['block']!r}")
        return p.strip()
    return text.strip()


def decryption_file(rec, t, q, r):
    k = q['key']
    lang = LANG.get(k.get('lang', ''), q['fields'].get('plaintext_lang', ''))
    keysrc = k.get('decode') or 'reconstructed, see the attached key file'
    head = [f'#DECRYPTION: {rec}', f'#LANGUAGE: {lang}', f'#DECRYPTED BY: {BY}', f'#DATE: {DATE}',
            f'#KEY: {keysrc}', f'#COMMENT: {r["note"]} Write-up: {q["writeup"]}',
            '#CONVENTIONS: <nnn> = code group not read; [...] = illegible or unread; {word} = value inferred from context;'
            ' word? = uncertain; [clear: ...] = written in clear on the document; [p. N] / [f. N] = page or folio', '']
    clean = os.path.join(ROOT, 'decode_updates', 'decryptions', f'{rec}.txt')
    if os.path.exists(clean):
        body = open(clean, encoding='utf-8').read().strip()
    else:
        body = '\n\n'.join(extract(s) for s in r['reading'])
    return '\n'.join(head) + body + '\n'


def transcription_file(rec, t, q, r):
    # Ciphertext transcription for a record that is not read: attached so the next attempt starts from it.
    head = [f'#TRANSCRIPTION: {rec}', f'#TRANSCRIBER NAME: {BY}', f'#DATE OF TRANSCRIPTION: {DATE}',
            f'#COMMENT: {r["note"]} Write-up: {q["writeup"]}', '']
    body = []
    for f in r['transcription']:
        body += [l.rstrip() for l in open(os.path.join(ROOT, f), encoding='utf-8')] + ['']
    return '\n'.join(head + body)


def info_line(t, q, r):
    k = q['key']
    if 'none' in k:
        key = f'Key: none known ({k["none"]}).'
    else:
        key = f'Key: DECODE {k["decode"]}.' if 'decode' in k else f'Key: reconstructed ({k.get("how")}), see the attached key file.'
    cite = f' Sources: {q["cite"]}.' if q.get('cite') else ''
    return f'Updated by {BY}, {DATE}: {r["note"]} {key}{cite} Write-up: {q["writeup"]}'


def main(argv):
    data = json.load(open(Q, encoding='utf-8'))
    check = '--check' in argv
    only = [a for a in argv if not a.startswith('--')]
    gaps, n = [], 0
    for t, q in data['targets'].items():
        if (only and t not in only) or q.get('skip'):
            continue
        if not isinstance(q.get('key'), dict):  # "key": null = queued without a key (unread target)
            q['key'] = {'none': 'no key'}
        for rec, r in q['records'].items():
            if r.get('sent'):
                continue
            if 'TODO' in json.dumps([r, q['key']]):
                gaps.append(f'{t} {rec}: TODO fields left (python decode_updates/queue.py status {t})')
                continue
            needs_key = 'decode' not in q['key'] and 'none' not in q['key']
            if not r.get('reading') and not r.get('reading_not_needed'):
                gaps.append(f'{t} {rec}: no reading file')
            if needs_key and not q['key'].get('file'):
                gaps.append(f'{t} {rec}: no key file')
            if not os.path.exists(os.path.join(ROOT, 'decode_updates', 'decryptions', f'{rec}.txt')) and r.get('reading'):
                gaps.append(f'{t} {rec}: reading not yet cleaned (decode_updates/decryptions/{rec}.txt)')
            if check:
                continue
            d = os.path.join(OUT, rec)
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, 'additional_information.txt'), 'w', encoding='utf-8').write(info_line(t, q, r) + '\n')
            f = [f'status: {r["decode_status"]} -> {r["proposed"]}'] + [f'{a}: -> {b}' for a, b in {**q.get('fields', {}), **r.get('fields', {})}.items()]
            open(os.path.join(d, 'fields.txt'), 'w', encoding='utf-8').write('\n'.join(f) + '\n')
            if needs_key and q['key'].get('file'):
                open(os.path.join(d, 'key.txt'), 'w', encoding='utf-8').write(key_file(rec, t, q))
            if r.get('transcription'):
                open(os.path.join(d, 'transcription.txt'), 'w', encoding='utf-8').write(transcription_file(rec, t, q, r))
            if r.get('reading'):
                open(os.path.join(d, 'decryption.txt'), 'w', encoding='utf-8').write(decryption_file(rec, t, q, r))
            n += 1
    for g in gaps:
        print('gap:', g)
    print(f'{"checked" if check else "built"} {n if not check else ""} records; {len(gaps)} gaps')


if __name__ == '__main__':
    main(sys.argv[1:])
