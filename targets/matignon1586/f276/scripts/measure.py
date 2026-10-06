"""Coverage of the f.276 reading, after the rule in targets/matignon1586/measure.py: a cipher sign counts as READ only if
it has a value (not '?') and its letters fall inside a run of at least three consecutive lexicon words totalling at
least ten letters. Word signs (=de, =que ...) are words. Lines are segmented with the lexicon Viterbi (segment.py).
Control: the same rule with the letter values permuted (shuffled key).
    python measure.py f276/read1.txt [n_shuffles]
"""
import sys, re, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segment import seg
A = 'abcdefghilmnopqrstuxz'
def load(p):
    """per line: list of tokens; a token is ('w', word) for a word sign, ('l', letter) or ('?', '')"""
    out = []
    for l in open(p):
        m = re.match(r'^\s*(L\d\d):\s*(.+)$', l)
        if not m or m.group(2).startswith('['): continue
        toks = []
        for t in m.group(2).split():
            if t == '###': toks.append(('w', 'et'))
            elif t.startswith('='): toks.append(('w', t[1:].split('/')[0]))
            elif t.startswith('[') or t == '|': continue
            else:
                v = t.split('/')[0].replace('?', '').replace('y', 'i')
                toks.append(('l', v) if v and all(c in A for c in v) else ('?', ''))
        out.append(toks)
    return out
def read_line(toks, tr=None):
    """segment the letter runs between word signs / unknowns; return per-token read flags"""
    # build a stream of units: each letter token one unit; word sign one unit (a whole word); '?' breaks runs
    words = []                                      # (is_lex, n_letters, token_indices)
    i = 0
    while i < len(toks):
        k, v = toks[i]
        if k == 'w': words.append((True, len(v), [i])); i += 1; continue
        if k == '?': words.append((False, 0, [i])); i += 1; continue
        j = i
        while j < len(toks) and toks[j][0] == 'l': j += 1
        s = ''.join(toks[x][1] for x in range(i, j))
        if tr: s = s.translate(tr)
        _, ws = seg(s); pos = i
        for w in ws:
            n = len(w.strip('[]')); idx = list(range(pos, pos + n)); pos += n
            words.append((not w.startswith('[') and (n >= 2 or w in 'ay'), n, idx))
        i = j
    read = [False] * len(toks); run = []
    def flush():
        if len(run) >= 3 and sum(w[1] for w in run) >= 10:
            for w in run:
                for x in w[2]: read[x] = True
    for w in words + [(False, 0, [])]:
        if w[0]: run.append(w)
        else: flush(); run = []
    return read
def measure(lines, tr=None):
    r = n = 0
    for toks in lines:
        f = read_line(toks, tr); r += sum(f); n += len(f)
    return r, n
lines = load(sys.argv[1]); ns = int(sys.argv[2]) if len(sys.argv) > 2 else 20
r, n = measure(lines); print(f'read {r}/{n} signs = {r/n:.1%}')
random.seed(2); sh = []
for _ in range(ns):
    p = list(A); random.shuffle(p); sh.append(measure(lines, str.maketrans(A, ''.join(p)))[0] / n)
sh.sort(); print(f'{ns} shuffled keys: median {sh[ns//2]:.1%}, max {sh[-1]:.1%}')
