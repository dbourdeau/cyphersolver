"""Reproduce the conservative reading and its audit; no language model required.

The observed tokens are retained. Local emendations are explicit, never hidden
in the key. I and M use the repository convention: inferred and uncertain.
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parent


def run():
    key = json.loads((ROOT / 'key.json').read_text(encoding='utf-8'))
    lines = [s.split() for s in (ROOT / 'ciphertext_rechecked.txt').read_text(encoding='utf-8').splitlines()
             if s.strip() and not s.startswith('#')]
    corrections = {(e['line'], e['position']): e for e in key['emendations']}
    uncertain = {(l, p) for l, ps in key['unresolved_context'].items() for p in ps}
    rows = []
    for ln, line in enumerate(lines, 1):
        for pos, sign in enumerate(line, 1):
            raw = key['alphabet'].get(sign)
            correction = corrections.get((ln, pos))
            val = correction['reading'] if correction else raw
            context_open = (str(ln), pos) in uncertain
            coherent = val is not None and not context_open
            rows.append(dict(line=ln, position=pos, sign=sign,
                             key_value=raw or '?', reading=val or f'[{sign}]',
                             grade='I' if coherent else 'M', coherent=int(coherent),
                             emendation=correction['reason'] if correction else ''))
    with (ROOT / 'reading_tokens.tsv').open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=rows[0], delimiter='\t'); w.writeheader(); w.writerows(rows)
    literal = []
    edited = []
    for ln in range(1, len(lines)+1):
        rr = [r for r in rows if r['line'] == ln]
        literal.append(f'{ln:02} ' + ''.join(r['key_value'] if r['key_value'] != '?' else f"[{r['sign']}]" for r in rr))
        edited.append(f'{ln:02} ' + ''.join(r['reading'] for r in rr))
    (ROOT / 'reading_literal.txt').write_text('\n'.join(literal)+'\n', encoding='utf-8')
    (ROOT / 'reading_emended.txt').write_text('\n'.join(edited)+'\n', encoding='utf-8')
    stats = {'tokens': len(rows), 'distinct': len({r['sign'] for r in rows}),
             'assigned': sum(r['key_value'] != '?' for r in rows),
             'coherent': sum(r['coherent'] for r in rows),
             'emended_tokens': sum(bool(r['emendation']) for r in rows),
             'uncertain_tokens': sum(not r['coherent'] for r in rows)}
    stats['fraction_read'] = stats['assigned']/stats['tokens']
    stats['fraction_coherent'] = stats['coherent']/stats['tokens']
    (ROOT / 'coverage.json').write_text(json.dumps(stats, indent=2)+'\n', encoding='utf-8')
    # One continuous passage; local editorial corrections remain marked.
    passage = [r for r in rows if r['line'] in (9, 10, 11)]
    reveal = dict(slug='joachim1530', anchor='reading', title='Jewels, vessels and furnishings',
                  caption='Sign aliases retain dots (d). Amber marks an editorial correction; all values are inferred from this ciphertext.',
                  unit='sign', key_note='Reconstructed here; I (inferred), no surviving historical key.',
                  tokens=[{'g':r['sign'], 'p':r['reading'],
                           'cls':'unk' if r['key_value']=='?' else 'unc' if r['emendation'] or not r['coherent'] else ''}
                          for r in passage])
    dest=ROOT.parent/'docs'/'reveal'/'joachim1530.json'
    if dest.parent.exists(): dest.write_text(json.dumps(reveal, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(stats, indent=2))
    print('\n'.join(edited))


if __name__ == '__main__':
    run()
