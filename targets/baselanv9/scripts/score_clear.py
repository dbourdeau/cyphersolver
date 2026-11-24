"""Score the ONE decode (DECODE.txt) against the clear copy, letter by letter (Levenshtein alignment).
H2 line by line (the clear page f. 167r has the same line breaks); H1 as one passage. '?' in the decode counts as a
wrong letter. Two figures per page: with abbreviations of the clear copy expanded (strict), and with the bracketed
expansions left out (letters the clear scribe actually wrote)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
D = '/home/claude/keyless/round40c/basel_anv9/'

def norm(s, expand=True):
    s = s.lower()
    if not expand:
        s = re.sub(r'\[[^\]]*\]', '', s)
    s = s.replace('[', '').replace(']', '')
    s = s.replace('j', 'i').replace('v', 'u').replace('y', 'i').replace('k', 'c')
    return re.sub('[^a-z? ]', '', s)

def lev(a, b):
    """Edit distance and number of matched letters on one best path (numpy rows, same result as the plain DP)."""
    import numpy as np
    n, m = len(a), len(b)
    if n == 0 or m == 0:
        return max(n, m), 0
    A = np.frombuffer(a.encode('latin-1'), dtype=np.uint8)
    B = np.frombuffer(b.encode('latin-1'), dtype=np.uint8)
    Mx = np.zeros((n + 1, m + 1), dtype=np.int32)
    Mx[0] = np.arange(m + 1)
    jj = np.arange(m + 1)
    for i in range(1, n + 1):
        cost = ((B != A[i - 1]) | (A[i - 1] == ord('?'))).astype(np.int32)
        T = np.empty(m + 1, dtype=np.int32)
        T[0] = i
        T[1:] = np.minimum(Mx[i - 1, 1:] + 1, Mx[i - 1, :-1] + cost)
        Mx[i] = np.minimum.accumulate(T - jj) + jj
    i, j, match = n, m, 0
    while i > 0 and j > 0:
        if a[i-1] == b[j-1] and a[i-1] != '?' and Mx[i, j] == Mx[i-1, j-1]:
            match += 1; i -= 1; j -= 1
        elif Mx[i, j] == Mx[i-1, j-1] + 1:
            i -= 1; j -= 1
        elif Mx[i, j] == Mx[i-1, j] + 1:
            i -= 1
        else:
            j -= 1
    return int(Mx[n, m]), match


def lev_slow(a, b):
    n, m = len(a), len(b)
    d = list(range(m + 1))
    bt = [[0] * (m + 1) for _ in range(n + 1)]
    prev = list(range(m + 1))
    M = [[0] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1): M[0][j] = j
    for i in range(1, n + 1):
        M[i][0] = i
        for j in range(1, m + 1):
            M[i][j] = min(M[i-1][j] + 1, M[i][j-1] + 1, M[i-1][j-1] + (0 if a[i-1] == b[j-1] and a[i-1] != '?' else 1))
    # count matches on a best path
    i, j, match = n, m, 0
    while i > 0 and j > 0:
        if a[i-1] == b[j-1] and a[i-1] != '?' and M[i][j] == M[i-1][j-1]:
            match += 1; i -= 1; j -= 1
        elif M[i][j] == M[i-1][j-1] + 1:
            i -= 1; j -= 1
        elif M[i][j] == M[i-1][j] + 1:
            i -= 1
        else:
            j -= 1
    return M[n][m], match

dec = {}
for ln in open(D + 'DECODE.txt'):
    if ln.startswith('#') or not ln.strip():
        continue
    k, t = ln.rstrip('\n').split('\t')
    dec[k] = t.replace('=', '')

out = []
def letters(s):
    return s.replace(' ', '')

for expand in (True, False):
    tag = 'strict (abbreviations of the clear copy expanded)' if expand else 'letters written in the clear copy (expansions left out)'
    out.append('### ' + tag)
    # H2 line by line
    clear = {}
    for ln in open(D + 'score/CLEAR_H2_f167r.txt'):
        if ln.startswith('#') or not ln.strip(): continue
        k, t = ln.rstrip('\n').split('\t'); clear[k] = t
    T = [0, 0, 0, 0]
    out.append('H2 f. 159r vs clear f. 167r, line by line: line | clear letters | decoded letters | matches | edits | match% of clear')
    for k in sorted(clear):
        r = letters(norm(clear[k], expand)); dd = letters(norm(dec.get('H2 ' + k, ''), True))
        e, mt = lev(dd, r)
        T[0] += len(r); T[1] += len(dd); T[2] += mt; T[3] += e
        out.append('  %s | %d | %d | %d | %d | %.1f%%' % (k, len(r), len(dd), mt, e, 100.0 * mt / max(1, len(r))))
    out.append('H2 TOTAL: clear letters %d, decoded letters %d, matches %d, edits %d -> %.1f%% of clear letters reproduced; precision %.1f%%; CER %.1f%%'
               % (T[0], T[1], T[2], T[3], 100.0 * T[2] / T[0], 100.0 * T[2] / T[1], 100.0 * T[3] / T[0]))
    # H1 as one passage
    r = letters(norm(' '.join(l for l in open(D + 'score/CLEAR_H1_f109v.txt') if not l.startswith('#')), expand))
    dd = letters(norm(' '.join(dec[k] for k in sorted(dec) if k.startswith('H1 ')), True))
    e, mt = lev(dd, r)
    out.append('H1 f. 15r lines 1-12 vs clear f. 109v (one passage): clear letters %d, decoded letters %d, matches %d, edits %d -> %.1f%% of clear letters reproduced; precision %.1f%%; CER %.1f%%'
               % (len(r), len(dd), mt, e, 100.0 * mt / len(r), 100.0 * mt / len(dd), 100.0 * e / len(r)))
    # H3 pentacle rims (clear rims found after the decode, f. 123r)
    T = [0, 0, 0, 0]
    for ln in open(D + 'score/CLEAR_H3_f123r.txt'):
        if ln.startswith('#') or not ln.strip(): continue
        k, t = ln.rstrip('\n').split('\t')
        r = letters(norm(t, expand)); dd = letters(norm(dec.get('H3 ' + k, ''), True))
        e, mt = lev(dd, r)
        T[0] += len(r); T[1] += len(dd); T[2] += mt; T[3] += e
        out.append('  H3 %s | clear %d | decoded %d | matches %d | edits %d | %.1f%%' % (k, len(r), len(dd), mt, e, 100.0 * mt / len(r)))
    out.append('H3 f. 34r pentacles 3-4 vs clear f. 123r: clear letters %d, decoded letters %d, matches %d, edits %d -> %.1f%% of clear letters reproduced; precision %.1f%%; CER %.1f%%'
               % (T[0], T[1], T[2], T[3], 100.0 * T[2] / T[0], 100.0 * T[2] / T[1], 100.0 * T[3] / T[0]))
    out.append('')
print('\n'.join(out))
open(D + 'score/score_clear_out.txt', 'w').write('\n'.join(out) + '\n')
