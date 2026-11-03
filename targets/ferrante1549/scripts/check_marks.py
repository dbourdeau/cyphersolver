#!/usr/bin/env python3
"""Check a reading against its decryption and count its words. Standard library only.

    python scripts/check_marks.py ch1549_1114             counts, unmarked departures
    python scripts/check_marks.py ch1549_1114 --table     also print the repair table (Markdown)

The Spanish of reading_<doc>.md is aligned letter by letter with decryption_<doc>.txt. Word classes:
verbatim = letters as the signs give them; repaired = word with a degree mark; proposal = [?word]; hole = [...].
A departure touching a verbatim word is an error of the reading and the script exits 1. A19 of 14 Nov, a repeated
line struck by the clerk, and passage C of c. 28r, a transcription job, are left out.
"""
import difflib, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP = {'A19', 'C1', 'C2'}       # the repeated line of 14 Nov; passage C of c. 28r, covered by its margin


def fold(w):
    w = unicodedata.normalize('NFKD', w.lower().replace('ç', 'c'))
    return ''.join(c for c in w if c.isalpha())


def spanish(doc):
    t = (ROOT / f'reading_{doc}.md').read_text(encoding='utf8')
    if '## Spanish' in t:
        t = t.split('## Spanish')[1].split('\n## ')[0]
    return ' '.join(l for l in t.splitlines() if l and not l.startswith('#'))


def decryption(doc):
    chars, lines = [], []
    for l in (ROOT / f'decryption_{doc}.txt').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        lab, _, body = l.partition(' ')
        if lab in SKIP:
            continue
        body = re.sub(r'\[\?la Yglesia\]', '\x00laYglesia\x00', body)
        for tag, val in (('[Papa]', 'papa'), ('[?Roma]', 'roma'), ('[?Francia]', 'francia'), ('[?zi]', 'zi'), ('[?gu]', 'gu'),
                         ('[?su]', 'su'), ('Su Magestad', 'sumagestad'), ('Rey de Francia', 'reydefrancia'), ('Embaxador', 'embaxador')):
            body = body.replace(tag, val)
        body = body.replace('\x00', '')
        body = re.sub(r'\[[^\]]*\]', '@', body).replace('.', '').replace('/', '')
        for c in fold_keep(body):
            chars.append(c)
            lines.append(lab)
    return ''.join(chars), lines


def fold_keep(s):
    return ''.join(c.lower() for c in s if c.isalpha() or c == '@')


def main():
    doc = sys.argv[1]
    table = '--table' in sys.argv
    items = re.findall(r'\[\?[^\]]*\]|\[\.\.\.\]|\[Papa\]|[^\s,.;:]+', spanish(doc))
    r, st, wi, words = [], [], [], []
    for it in items:
        if it == '[...]':
            kind, w = 'h', ''
        elif it.startswith('[?'):
            kind, w = 'q', fold(it[2:-1])
        elif it == '[Papa]':
            kind, w = 'f', 'papa'
        elif it.endswith('°'):
            kind, w = 'r', fold(it)
        else:
            kind, w = 'f', fold(it)
        k = len(words)
        words.append((it, kind))
        if kind == 'h':
            r.append('@'); st.append('h'); wi.append(k)
        for c in w:
            r.append(c); st.append(kind); wi.append(k)
    r = ''.join(r)
    d, ln = decryption(doc)
    sm = difflib.SequenceMatcher(None, d, r, autojunk=False)
    gives = {}
    bad = set()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        if j2 > j1:
            ws = sorted(set(wi[j1:j2]))
        else:                                       # signs with nothing in the reading: the neighbours answer for them
            ws = [w for w in {wi[max(j1 - 1, 0)], wi[min(j1, len(wi) - 1)]}]
            if any(words[w][1] != 'f' for w in ws):
                ws = [w for w in ws if words[w][1] != 'f']
            ws = ws[:1] if len(ws) > 1 and wi[max(j1 - 1, 0)] == wi[min(j1, len(wi) - 1)] else ws
        for w in ws:
            gives.setdefault(w, []).append((i1, i2))
            if words[w][1] == 'f':
                bad.add(w)
    tot = len(words)
    nq = sum(k == 'q' for _, k in words)
    nh = sum(k == 'h' for _, k in words)
    nr = sum(k == 'r' for _, k in words)
    nf = sum(k == 'f' for _, k in words)
    print(f'{doc}: words {tot}; verbatim {nf} ({nf / tot:.1%}); repaired {nr}; proposals {nq}; holes {nh}; sense firm {nf + nr} ({(nf + nr) / tot:.1%})')
    unused = [words[i][0] for i, (_, k) in enumerate(words) if k == 'r' and i not in gives]
    if unused:
        print('marked but no departure found:', unused)
    if bad:
        print('UNMARKED departures:', [(words[w][0], d[max(gives[w][0][0] - 6, 0):gives[w][-1][1] + 6]) for w in sorted(bad)])
    if table:
        print('| line | reading | the signs give |\n|---|---|---|')
        for w in sorted(gives):
            if words[w][1] != 'r':
                continue
            a, b = gives[w][0][0], gives[w][-1][1]
            a2, b2 = max(a - 7, 0), min(b + 7, len(d))
            print(f'| {ln[min(a, len(ln) - 1)]} | {words[w][0].rstrip("°")} | `{d[a2:a].lower()}[{d[a:b]}]{d[b:b2].lower()}` |')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
