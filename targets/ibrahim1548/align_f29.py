"""Decode the f. 29 transcription with the R367 values recorded in the READ lines and align the result on the Latin exemplar.

Reads transcription/f29_lines_*.txt (pairs of 'Lnn SIGNS:' / 'Lnn READ :' lines, see TRANSCRIPTION_BRIEF.md).
READ tokens: a letter, [code], '.' null, '?' unknown, 'a/b' alternatives, trailing '*' = value taken from the exemplar
(counted as crib-dependent, never as a match). Prints the match rate of the key-derived tokens against the exemplar
after a global alignment, and writes transcription/f29_alignment.txt.
"""
import glob, pathlib, re, sys

HERE = pathlib.Path(__file__).parent
EX = (HERE / 'texts' / 'exemplar_7-4-4_A.txt').read_text(encoding='utf8')


def exemplar_letters():
    body = EX.split('\n\n', 1)[1]
    s = body.lower().replace('[', '').replace(']', '').replace('..', '')
    s = s.replace('æ', 'e').replace('à', 'a').replace('ae', 'e').replace('oe', 'e')
    s = s.replace('j', 'i').replace('v', 'u').replace('&', 'et')
    return re.sub(r'[^a-z]', '', s)


def read_tokens():
    toks = []
    for f in sorted(glob.glob(str(HERE / 'transcription' / 'f29_lines_*.txt'))):
        for ln in open(f, encoding='utf8'):
            m = re.match(r'(L\d\d) READ\s*:\s*(.*)', ln)
            if not m:
                continue
            for t in m.group(2).split():
                toks.append((m.group(1), t))
    return toks


def to_set(t):
    crib = t.endswith('*')
    t = t.rstrip('*')
    if t == '.' or t == '':
        return None, False
    if t == '?':
        return set(), crib
    if t.startswith('['):
        return {t.strip('[]')}, crib
    return set(a.strip('*') for a in t.split('/')), crib


def main():
    ex = exemplar_letters()
    toks = []
    for line, t in read_tokens():
        s, crib = to_set(t)
        if s is None:
            continue
        # normalise like the exemplar: v->u, j->i, ae->e, doubled letters and [et] take two exemplar letters
        s = {('u' if x == 'v' else 'i' if x == 'j' else 'e' if x == 'ae' else x) for x in s}
        if len(s) == 1 and (list(s)[0] in ('ll', 'ss', 'tt', 'cc', 'dd', 'ff', 'gg', 'mm', 'nn', 'pp', 'rr', 'et')):
            v = list(s)[0]
            toks.append((line, t, {v[0]}, crib)); toks.append((line, t, {v[1]}, crib)); continue
        toks.append((line, t, s, crib))
    n, m = len(toks), len(ex)
    # global alignment, tokens (rows) against exemplar letters (columns)
    M, MM, G = 2, -1, -1
    sc = [[0] * (m + 1) for _ in range(n + 1)]
    bk = [[None] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        sc[i][0] = i * G; bk[i][0] = 'u'
    for j in range(1, m + 1):
        sc[0][j] = j * G; bk[0][j] = 'l'
    for i in range(1, n + 1):
        _, _, s, crib = toks[i - 1]
        for j in range(1, m + 1):
            c = ex[j - 1]
            if crib or not s:
                d = 0
            else:
                d = M if any(c.startswith(x) or x == c for x in s) else MM
            opts = [(sc[i - 1][j - 1] + d, 'd'), (sc[i - 1][j] + G, 'u'), (sc[i][j - 1] + G, 'l')]
            sc[i][j], bk[i][j] = max(opts)
    i, j, rows = n, m, []
    while i > 0 or j > 0:
        b = bk[i][j]
        if b == 'd':
            rows.append((toks[i - 1], ex[j - 1])); i -= 1; j -= 1
        elif b == 'u':
            rows.append((toks[i - 1], '-')); i -= 1
        else:
            rows.append((None, ex[j - 1])); j -= 1
    rows.reverse()
    hit = miss = unk = cribn = gap = 0
    out = []
    for tok, c in rows:
        if tok is None:
            gap += 1; out.append(f'  -    {c}'); continue
        line, t, s, crib = tok
        if c == '-':
            gap += 1; out.append(f'{line} {t:8} -')
            continue
        if crib:
            cribn += 1; tag = 'crib'
        elif not s:
            unk += 1; tag = 'unk'
        elif any(c.startswith(x) or x == c for x in s):
            hit += 1; tag = 'ok'
        else:
            miss += 1; tag = 'MISS'
        out.append(f'{line} {t:8} {c} {tag}')
    scored = hit + miss
    summ = (f'tokens {n}, exemplar letters {m}; key-derived tokens matched {hit}/{scored}'
            f' ({100 * hit / max(scored, 1):.1f}%); crib-dependent {cribn}; unknown {unk}; unmatched/gaps {gap}')
    (HERE / 'transcription' / 'f29_alignment.txt').write_text(summ + '\n' + '\n'.join(out) + '\n', encoding='utf8')
    print(summ)


if __name__ == '__main__':
    main()
