"""barbavara1447: independent check of the f. 135 / f. 143 cipher runs (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).

    python3 verify_dudout_20261114.py targets/barbavara1447

Reads only: the sign-value list at the head of texts/glossed_letters.md ("Sign values used here", read off R1857 P11),
the code and spot-checked signs of key_R1857_codes.tsv, the sign strings of texts/glossed_runs.tsv, and the
"deciphered" column of the run tables in texts/glossed_letters.md. The values the notes say were inferred from the
glosses (t-o = i, h = l, fto = ap, eg = s, n/no) are NOT used, so the result measures the key alone.
For each run a DP aligns the signs with the deciphered letters: a sign "fits" when one of its key values spells the
next letters; a code sign fits its word; other signs are free (unread, null, or valued from the gloss).
"""
import pathlib, re, sys, unicodedata


def letters(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if 'a' <= c <= 'z')


def load_key(folder):
    g = (folder / 'texts' / 'glossed_letters.md').read_text(encoding='utf8')
    block = g.split('Sign values used here', 1)[1].split('## f. 135', 1)[0]
    key = {}
    def add(sign, val):
        sign = sign.strip()
        if not sign or sign.startswith('(') or sign == '': return
        key.setdefault(sign, set()).add(val)
    alpha, syl = block.split('Syllables:', 1)
    for part in alpha.split('|'):
        m = re.search(r'(?:^|\n)\s*([a-z]):\s*(.*)', part.strip(), re.S)
        if not m: continue
        val, signs = m.groups()
        for s in re.split(r',\s*', signs.replace('\n', ' ')):
            s = re.sub(r'\(.*?\)', '', s).strip()
            for t in s.split():
                if t in ('3/h/',): add('3', val); add('h/', val); continue
                add(t, val)
    for chunk in re.split(r'[,;]|\.\n', syl):
        f = chunk.split()
        if len(f) < 2 or not re.fullmatch(r'[a-z]{2}', f[0]): continue
        for s in ' '.join(f[1:]).split('/'):
            s = re.sub(r'\(.*?\)', '', s).strip()
            if s: add(s.split()[0], f[0])
    codes = {}
    for line in (folder / 'key_R1857_codes.tsv').read_text(encoding='utf8').splitlines():
        if line.startswith('#') or line.startswith('sign\t') or '\t' not in line: continue
        f = line.split('\t')
        sign, label, value = f[0], f[1], f[2]
        if value == 'open': continue
        v = letters(value.split('(')[0])
        if len(v) <= 2: add(sign, v)
        else: codes[sign] = v
    return key, codes


def runs_table(folder):
    g = (folder / 'texts' / 'glossed_letters.md').read_text(encoding='utf8')
    out = {}
    for line in g.splitlines():
        m = re.match(r'\| (13[5]\.\d+|143\.\d+) \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|', line)
        if m: out[m.group(1)] = (m.group(5).strip(), m.group(6).strip())
    return out


def signs_of(folder):
    out = {}
    for line in (folder / 'texts' / 'glossed_runs.tsv').read_text(encoding='utf8').splitlines():
        f = line.split('\t')
        if len(f) == 3 and re.fullmatch(r'1\d\d\.\d+', f[0]):
            s = re.sub(r'\([^)]*\)', ' ', f[2]).replace('·', ' ').replace('…', ' ').replace('[blot]', ' ')
            out[f[0]] = [t for t in s.split() if t]
    return out


def align(signs, target, key, codes):
    """max number of signs that fit, with the target consumed in order (free signs may take 0-3 letters)."""
    n, L = len(signs), len(target)
    NEG = -10 ** 9
    best = [[NEG] * (L + 1) for _ in range(n + 1)]
    best[0][0] = 0
    for i in range(n):
        s = signs[i]
        vals = set(key.get(s, ())) | ({codes[s]} if s in codes else set())
        for j in range(L + 1):
            b = best[i][j]
            if b == NEG: continue
            for v in vals:
                if target.startswith(v, j) and best[i + 1][j + len(v)] < b + 1: best[i + 1][j + len(v)] = b + 1
            for k in range(0, 4):
                if j + k <= L and best[i + 1][j + k] < b: best[i + 1][j + k] = b
    # letters left over at the end are allowed (unread tail)
    return max(best[n])


def main(folder):
    folder = pathlib.Path(folder)
    key, codes = load_key(folder)
    table, signs = runs_table(folder), signs_of(folder)
    tot = fit = 0
    unknown = {}
    for run, sg in signs.items():
        dec, note = table.get(run, ('', ''))
        tgt = letters(re.sub(r'\[[^\]]*\?\]|\?', '', dec))
        if not tgt: print(f'{run:7s} (not deciphered) {len(sg)} signs'); continue
        f = align(sg, tgt, key, codes)
        tot += len(sg); fit += f
        for s in sg:
            if s not in key and s not in codes: unknown.setdefault(s, []).append(run)
        tag = note.split(':')[0].split('.')[0][:4] if note else ''
        print(f'{run:7s} {tag:5s} {f:2d}/{len(sg):2d} signs fit the key   {dec}')
    print(f'TOTAL {fit}/{tot} signs of the deciphered runs fit a key value ({fit / tot:.3f})')
    print('signs not in the key list (runs):')
    for s, r in sorted(unknown.items(), key=lambda x: -len(x[1])):
        print(f'  {s:10s} x{len(r):2d}  {" ".join(r[:8])}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
