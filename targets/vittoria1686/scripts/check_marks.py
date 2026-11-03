#!/usr/bin/env python3
"""Build a reading from its marked source, check it against the decryption and count the words. Standard library only.

    python scripts/check_marks.py <doc>            check; counts; exit 1 on any unmarked departure
    python scripts/check_marks.py <doc> --write    also write reading_, translation_ and repairs_<doc>.md

edit_<doc>.txt holds the Italian with the cipher between << and >>. Inside, each token is one word of the reading, and
printed=raw when what is printed differs from what the signs give:

    word              verbatim: the letters are the signs' letters (u/v and i/j not told apart)
    fa[t]to=fato      repaired: square brackets show restored or changed letters
    word°=raw         repaired: surplus signs dropped
    [?word]=raw       proposal, doubtful
    {IMA}             code word, value by context
    [che]             code group with a resolved value
    [...]=raw         not read; [...]=raw#3 counts as 3 words
    [109]             code group not identified
    <null>=raw        ordered null string, left out of the count
    [di]=             word supplied by the editor, no sign behind it, left out of the count

The script joins the raw values and requires them to equal the cipher stream of decryption_<doc>.txt, letter for letter.
A verbatim token whose letters differ from its raw value stops it, so no repair can go unmarked. The clear text between
the cipher passages is compared too, when the source says so (first line: "# clear: check").
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESOLVED = {'[che]'}
HOLES = {'[109]', '[182]'}


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i')
    return ''.join(c for c in s if c.isalpha())


def stream(doc):
    """Cipher letters of the decryption table, and its clear text, each as one string."""
    ci, cl = [], []
    for l in (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        body = l.split(' ', 1)[1]
        for p in re.split(r'(\[[^\]]*\])', body):
            if p.startswith('[') and p not in ('[che]', '[?per]', '[109]', '[182]'):
                cl.append(p[1:-1])
            else:
                ci.append(p.replace(' ', ''))
    return ''.join(ci), fold(' '.join(cl))


def classify(tok):
    pr, eq, raw = tok.rpartition('=') if '=' in tok else (tok, '', None)
    n = 1
    if raw and re.search(r'#\d+$', raw):
        raw, n = raw.rsplit('#', 1)[0], int(raw.rsplit('#', 1)[1])
    if pr == '<null>':
        return pr, raw, 'N', 0
    if pr.startswith('[...]') or pr in HOLES:
        return pr, raw if raw is not None else pr, 'H', n
    if pr.startswith('{'):
        return pr, pr, 'C', 1
    if pr.rstrip('.,;:') in RESOLVED:
        return pr, pr.rstrip('.,;:'), 'K', 1
    if raw == '':
        return pr, '', 'E', 0
    if '[?' in pr:
        return pr, raw if raw is not None else pr, 'D', 1
    if '[' in pr or '°' in pr:
        return pr, raw, 'R', 1
    if raw is not None and fold(pr) != fold(raw):
        sys.exit(f'UNMARKED departure: {tok}')
    return pr, raw if raw is not None else fold(pr), 'V', 1


def load(doc):
    t = (ROOT / f'edit_{doc}.txt').read_text(encoding='utf8')
    check_clear = t.startswith('# clear: check')
    t = '\n'.join(l for l in t.splitlines() if not l.startswith('# '))
    it, en = t.split('## English')
    return it.replace('## Italian', '').strip(), en.strip(), check_clear


def run(doc, write):
    it, en, check_clear = load(doc)
    ci, cl = stream(doc)
    raws, clear, paras, rows, sect = [], [], [], [], ''
    cnt = {}
    for para in it.split('\n'):
        if not para.strip():
            paras.append('')
            continue
        if para.startswith('###'):
            sect = para.lstrip('# ').strip()
            paras.append(para)
            continue
        out = []
        for p in re.split(r'(<<.*?>>)', para):
            if p.startswith('<<'):
                for tok in p[2:-2].split():
                    pr, raw, kl, n = classify(tok)
                    raws.append(raw or '')
                    out.append(pr)
                    c = cnt.setdefault(sect, dict(V=0, R=0, D=0, C=0, K=0, H=0))
                    if kl in c:
                        c[kl] += n
                    if kl == 'R' or (kl == 'D' and fold(pr) != fold(raw)):
                        rows.append((pr, raw, 'repair' if kl == 'R' else 'proposal'))
            elif p.strip():
                clear.append(p)
                out.append(p.strip())
        paras.append(re.sub(r' (\.[ae])\b', r'\1', ' '.join(out)))
    got = ''.join(raws).replace('{', '{')
    want = ci
    if got.lower() != want.lower():
        i = next((k for k, (a, b) in enumerate(zip(got.lower(), want.lower())) if a != b), min(len(got), len(want)))
        sys.exit(f'cipher stream differs at {i}: reading ...{got[max(0, i - 25):i + 15]}... decryption ...{want[max(0, i - 25):i + 15]}...')
    if check_clear:
        c2 = fold(re.sub(r'\[[^\]?]\]', '', ' '.join(clear)))
        if c2 != cl:
            i = next((k for k, (a, b) in enumerate(zip(c2, cl)) if a != b), min(len(c2), len(cl)))
            sys.exit(f'clear text differs at {i}: reading ...{c2[max(0, i - 25):i + 15]}... decryption ...{cl[max(0, i - 25):i + 15]}...')
    tot = {k: sum(c[k] for c in cnt.values()) for k in 'VRDCKH'}
    return paras, en, rows, cnt, tot


def counts_table(cnt, tot):
    head = '| Part | Number or cipher words | As sense (A) | No restored or changed letter (C) | Marked repairs | Doubtful | Code words by context | Not read |\n|---|---|---|---|---|---|---|---|'
    def row(name, c):
        n = sum(c.values())
        a = c['V'] + c['R'] + c['K']
        v = c['V'] + c['K']
        return f"| {name} | {n} | {a} ({a / n:.1%}) | {v} ({v / n:.1%}) | {c['R']} | {c['D']} | {c['C']} | {c['H']} |"
    rows = [row(k or 'whole', c) for k, c in cnt.items()]
    if len(cnt) > 1:
        rows.append(row('all', tot))
    return head + '\n' + '\n'.join(rows)


if __name__ == '__main__':
    doc = sys.argv[1]
    paras, en, rows, cnt, tot = run(doc, '--write' in sys.argv)
    n = sum(tot.values())
    print(f"{doc}: words {n}; as sense {tot['V'] + tot['R'] + tot['K']} ({(tot['V'] + tot['R'] + tot['K']) / n:.1%}); no restored or changed letter {tot['V'] + tot['K']} ({(tot['V'] + tot['K']) / n:.1%}); repaired {tot['R']}; doubtful {tot['D']}; code {tot['C']}; not read {tot['H']}")
    if '--write' in sys.argv:
        header = (ROOT / f'header_{doc}.md').read_text(encoding='utf8').strip()
        title = header.split('\n')[0]
        (ROOT / f'reading_{doc}.md').write_text(title + '\n\n' + '\n'.join(paras).strip() + '\n', encoding='utf8', newline='\n')
        (ROOT / f'translation_{doc}.md').write_text(title + ', English\n\n' + en + '\n', encoding='utf8', newline='\n')
        body = header + '\n\n## Words, generated by scripts/check_marks.py\n\n' + counts_table(cnt, tot) + '\n'
        body += '\n## Repairs and proposals where the printed word differs from the signs\n\n| Printed | The signs give | Kind |\n|---|---|---|\n'
        body += ''.join(f'| {a.replace("|", "/")} | `{b}` | {c} |\n' for a, b, c in rows)
        (ROOT / f'repairs_{doc}.md').write_text(body, encoding='utf8', newline='\n')
