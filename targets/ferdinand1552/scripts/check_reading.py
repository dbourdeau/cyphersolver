"""Compare a reading (reading_<letter>.txt) with the machine decryption (work/beam_<letter>.tsv).

    python scripts/check_reading.py 13oct [--lines]

Per line, the reading's letters are aligned with the decryption's letters (edit distance; a code sign counts as
one symbol). A word of the reading is 'as decrypted' when every one of its letters is matched to the same letter
in the decryption, with nothing inserted inside it. Prints the per-letter agreement, the word counts, and with
--lines every line that differs."""
import sys, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
L = sys.argv[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from transcribe import load_lines, decrypt
_lines, _ = load_lines(L)
dec = {k: decrypt(v[3]).replace('(', '').replace(')', '') for k, v in _lines.items()}
def toks(s):
    s = s.replace('v', 'u').replace('V', 'U').replace('j', 'i')
    return re.findall(r'\[[A-Z0-9?]+\]|[a-z]', s.lower().replace('[q', '[Q').replace('[h', '[H'))
def toks_dec(s):
    return re.findall(r'\[[A-Za-z0-9:#.+=<~*?]+\]|[a-z]', s)
rd = []
for l in open(ROOT / f'reading_{L}.txt', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, t = l.rstrip('\n').split('\t'); rd.append((k, t))
def align(a, b):
    n, m = len(a), len(b); D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    ok = [False] * n; i, j = n, m; ins = set()
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            ok[i-1] = a[i-1] == b[j-1]; i -= 1; j -= 1
        elif i > 0 and D[i][j] == D[i-1][j] + 1:
            i -= 1
        else:
            ins.add(i); j -= 1      # decryption symbol with no reading letter, before reading index i
    return ok, ins, D[n][m]
tot = good = 0; words = []; cur = []; show = '--lines' in sys.argv
for k, t in rd:
    t2 = '' if t == "''" else t
    a = toks(t2); b = toks_dec(dec.get(k, ''))
    b = ['[' + x[1:-1] + ']' if x.startswith('[') else x for x in b]
    ok, ins, d = align(a, b)
    tot += len(a); good += sum(ok)
    if show and d: print(f'{k:7} {t2:40} | {dec.get(k,"")}')
    # words: walk t2 by characters
    i = 0
    for w in re.findall(r'\[[^\]]+\]|[A-Za-z]+-?|\S', t2):
        n = len(toks(w))
        if n == 0: continue
        flags = ok[i:i + n]; inside = any(x in ins for x in range(i + 1, i + n))
        cur.append(all(flags) and not inside)
        i += n
        if not w.endswith('-'):
            words.append(all(cur)); cur = []
print(f'{L}: reading letters {tot}, matched to the decryption {good} ({100*good/max(1,tot):.1f}%)')
print(f'words {len(words)}, as decrypted {sum(words)} ({100*sum(words)/max(1,len(words)):.1f}%)')
