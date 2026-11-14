"""clair357: independent decoder (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

    python3 verify_dudout_20261114.py targets/clair357

Key: Tomokiyo's table as printed in henryiii_Anonymous.png, typed in below, plus the additions listed in
texts/key.md (87 = e, 71 = a, 22 and 66 nulls). It does not use research/reading_audit/b26_clair_dec.py.
Groups not in that key are shown as <nn>.

1. texts/f167r_l23-29_figures_dudout.txt: the seven cipher lines before the cross on f. 167r, read on the Gallica image.
   Each FIG line is decoded and compared, letter by letter, with the f. 168r clear copy of the same words (COPY).
2. texts/f167_interlinear_transcription.txt (Daniel's FIG lines after the cross): decoded with the same key and
   compared with the DEC lines written there.
"""
import difflib, pathlib, re, sys, unicodedata

TABLE = {  # Tomokiyo, henryiii_Anonymous.png
    'a': '14 20', 'b': '16', 'c': '18', 'd': '25 73', 'e': '28 72', 'f': '17 35', 'g': '12 74', 'h': '86',
    'i': '34 67 98', 'l': '13 51 70', 'm': '42 64', 'n': '19 29', 'o': '23 37', 'p': '40 68', 'q': '85',
    'r': '43 88', 's': '27 36 82', 't': '26 47', 'u': '24 63', 'x': '77', 'z': '41'}
KEY = {g: l for l, gs in TABLE.items() for g in gs.split()}
KEY.update({'78': 'vous', '81': 'que', '83': 'il', '92': 'et'})
KEY.update({'87': 'e', '71': 'a'})                       # texts/key.md additions
NULLS = {'45', '31', '66', '22'}                         # Tomokiyo's nulls + key.md (22, 66)
SIGNS = {'#': 'roydenavarre', '#CATH': '<CATH>', '#HUG': '<HUG>'}


def dec(groups):
    out = []
    for g in groups:
        g = g.strip('?')
        if g in NULLS: continue
        if g in SIGNS: out.append(SIGNS[g])
        elif g.startswith('(') or g == '|': continue
        elif g.startswith('['): out.append(g.strip('[]'))
        elif g in KEY: out.append(KEY[g])
        else: out.append(f'<{g}>')
    return ''.join(out)


def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha() or c in '<>')
    return s.replace('v', 'u').replace('j', 'i').replace('y', 'i')


def main(folder):
    t = pathlib.Path(folder) / 'texts'
    lines = [l.rstrip('\n') for l in open(t / 'f167r_l23-29_figures_dudout.txt', encoding='utf8') if not l.startswith('#')]
    figs = [l[5:].split() for l in lines if l.startswith('FIG')]
    copies = [l[5:] for l in lines if l.startswith('COPY')]
    tot = same = 0
    print('== f. 167r, seven lines before the cross: decode vs the f. 168r copy')
    for n, (f, c) in enumerate(zip(figs, copies), 23):
        d = dec(f)
        a = re.sub(r'<[^>]*>', '#', norm(d))
        b = norm(re.sub(r'\[[^\]]*\]', '', c.replace('Catholiques', '<CATH>').replace('Huguenotz', '<HUG>')))
        b = re.sub(r'<[^>]*>', '#', b)
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        m = sum(x.size for x in sm.get_matching_blocks())
        tot += len(a); same += m
        print(f'l.{n}  {d}\n      copy: {c}\n      letters {m}/{len(a)}')
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal': print(f'      {op}: cipher "{a[i1:i2]}" / copy "{b[j1:j2]}"')
    print(f'TOTAL letters matching the copy: {same}/{tot} = {same / tot:.3f}')
    unk = sorted({g.strip('?') for f in figs for g in f if g.strip('?').isdigit() and g.strip('?') not in KEY and g.strip('?') not in NULLS})
    print('groups outside the key in these lines:', ' '.join(unk))

    print('\n== f. 167r-v after the cross: Daniel\'s FIG lines decoded, compared with his DEC lines')
    rows = open(t / 'f167_interlinear_transcription.txt', encoding='utf8').read().split('\n')
    ok = n = 0
    for i, r in enumerate(rows):
        if not r.startswith('FIG'): continue
        nxt = [x for x in rows[i + 1:i + 3] if x.startswith('DEC')]
        if not nxt: continue
        f = [g for g in re.split(r'\s+', r[3:].split('GLOSS')[0].strip()) if g and g != '/']
        mine = re.sub(r'<[^>]*>', '', norm(dec([g for g in f if re.fullmatch(r'\d\d\??', g)])))
        his = re.sub(r'<[^>]*>|\[[^\]]*\]', '', nxt[0][3:])
        his = norm(his)
        sm = difflib.SequenceMatcher(None, mine, his, autojunk=False)
        m = sum(x.size for x in sm.get_matching_blocks())
        n += max(len(mine), len(his)); ok += m
        print(f'  line {i + 1}: {m}/{max(len(mine), len(his))}')
    print(f'TOTAL {ok}/{n} = {ok / n:.3f}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
