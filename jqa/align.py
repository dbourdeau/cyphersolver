"""Align a transcribed run of JQA code groups with the plaintext Ford printed from the decyphered copy.

python align.py CODEFILE [--table pairs_jqa.txt] [--extra clerk_*.tsv ...]

CODEFILE blocks:
    @ <ref>                 e.g. @ 0010 block 2 (Ford 4:15-16)
    = <plaintext as printed by Ford>
    <code lines>            numbers; a trailing ^ = the superscript o (plural s), + = the mark under a group;
                            words = clear text written in the line; ? after a number = uncertain reading
The DP segments the plaintext letters over the groups: known groups must match one of their table values
(a mismatch is allowed at a cost and reported), unknown groups take 1-8 letters. Output per block: the
alignment, then 'NEW n value' lines for groups not in the table and 'CONFLICT n table-values ford-letters'.
"""
import sys, re, glob

def norm(s):
    return re.sub(r'[^a-z]', '', s.lower())

def load_table(files):
    tab = {}
    for f in files:
        for l in open(f, encoding='utf8'):
            if l.startswith('#') or not l.strip():
                continue
            p = l.rstrip('\n').split('\t')
            if len(p) < 3 or not p[0].strip().isdigit():
                continue
            gcol = 2 if f.endswith('code_table.tsv') else 3
            if len(p) <= gcol:
                continue
            n, r, g = int(p[0]), p[1], p[gcol].strip()[:1]
            vals = set()
            for alt in r.split('/'):
                alt = alt.replace('U.S.', 'unitedstates').replace('[', '').replace(']', '')
                full = norm(alt)
                short = norm(re.sub(r'\(.*?\)', '', alt))
                for v in (full, short):
                    if v:
                        vals.add(v)
            tab.setdefault(n, {})
            for v in vals:
                # keep the best grade per value
                old = tab[n].get(v)
                if old is None or 'HCMI'.index(g if g in 'HCMI' else 'I') < 'HCMI'.index(old):
                    tab[n][v] = g if g in 'HCMI' else 'I'
    return tab

def parse(codefile):
    blocks = []
    cur = None
    for l in open(codefile, encoding='utf8'):
        l = l.rstrip('\n')
        if l.startswith('@'):
            cur = {'ref': l[1:].strip(), 'plain': '', 'toks': []}
            blocks.append(cur)
        elif l.startswith('='):
            cur['plain'] += ' ' + l[1:]
        elif l.strip() and not l.startswith('#'):
            cur['toks'] += l.split()
    return blocks

def align(toks, plain, tab):
    P = norm(plain)
    n, m = len(toks), len(P)
    INF = 1e9
    # token specs
    specs = []
    for t in toks:
        mt = re.fullmatch(r'(\d+)([\^+]*)(\??)', t)
        if mt:
            specs.append(('num', int(mt.group(1)), mt.group(2), mt.group(3)))
        else:
            specs.append(('word', norm(t), '', ''))
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for j in range(1, m + 1):  # leading plaintext not in this run
        D[0][j] = 0.2 * j; B[0][j] = ('skipP', 0, j - 1)
    for i in range(n):
        kind, val, mark, unc = specs[i]
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF:
                continue
            # skip plaintext letter (Ford wording differs)
            if j < m and d + 1.0 < D[i][j + 1]:
                D[i][j + 1] = d + 1.0; B[i][j + 1] = ('skipP', i, j)
            # drop token (misread / null)
            if d + 4.0 < D[i + 1][j]:
                D[i + 1][j] = d + 4.0; B[i + 1][j] = ('drop', i, j)
            opts = []
            if kind == 'word':
                if val and P.startswith(val, j):
                    opts.append((len(val), 0.0, 'word'))
            else:
                known = tab.get(val, {})
                extra = [0, 1, 2] if mark else [0]
                for v, g in known.items():
                    if P.startswith(v, j):
                        for e in extra:
                            if j + len(v) + e <= m:
                                opts.append((len(v) + e, 0.0 + 0.3 * e + (0.2 if g in 'MI' else 0), 'known'))
                maxL = 14 if val <= 100 else 8
                for L in range(1, maxL + 1):
                    if j + L <= m:
                        if val <= 100:
                            c = 1.2
                        else:
                            c = 1.5 + 0.5 * max(0, L - 4) + 0.6 * max(0, 2 - L)
                        opts.append((L, c + (3.5 if known else 0), 'mis' if known else 'new'))
            for L, c, how in opts:
                if d + c < D[i + 1][j + L]:
                    D[i + 1][j + L] = d + c; B[i + 1][j + L] = (how, i, j)
    # trailing plaintext allowed
    best = min(range(m + 1), key=lambda j: D[n][j] + 0.2 * (m - j))
    out = []
    i, j = n, best
    while i > 0 or j > 0:
        how, pi, pj = B[i][j]
        if how == 'skipP':
            out.append(('skip', None, P[pj:j]))
        elif how == 'drop':
            out.append(('drop', toks[pi], ''))
        else:
            out.append((how, toks[pi], P[pj:j]))
        i, j = pi, pj
        if i == 0 and how == 'skipP':
            # consume leading
            while j > 0 and B[0][j] and B[0][j][0] == 'skipP':
                j -= 1
            break
    out.reverse()
    return out, D[n][best]

def main():
    args = sys.argv[1:]
    code = args[0]
    tabfiles = ['pairs_jqa.txt'] + [a for a in args[1:] if a.endswith('.tsv')]
    tab = load_table(tabfiles)
    for b in parse(code):
        out, cost = align(b['toks'], b['plain'], tab)
        print('@', b['ref'], ' cost %.1f' % cost)
        print(' '.join(f'{t}={s}' if how != 'skip' else f'<{s}>' for how, t, s in out))
        for how, t, s in out:
            if how == 'new':
                print('NEW', re.sub(r'\D', '', t), s)
            elif how == 'mis':
                n = int(re.sub(r'\D', '', t))
                print('CONFLICT', n, '/'.join(sorted(tab[n])), s)
            elif how == 'drop':
                print('DROP', t)
        print()

if __name__ == '__main__':
    main()
