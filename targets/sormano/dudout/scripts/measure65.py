"""PREREG measure for no. 65 (see PREREG65.md), run once. Same scoring as measure63.py.
Portion = every cipher sign of no65_signs_reread.txt (foot of f. 119r L32-36, f. 119v L23 end-L37, f. 120r L01-L11,
L13-L20, L22-L23). Tokens: one per cipher sign; null (!) dropped; code signs (P W R I D) and unidentified signs (?) =
context tokens; doubtful signs -> first option; looped Z = z. Clear-hand text closes a run.
Statistic M = share of cipher-sign tokens READ by Daniel's rule (run of >= 3 lexicon words totalling >= 10 letters),
lexicon it-cinquecento, mincount 20. Controls: 200 permuted letter keys (seeds 1..200) + 200 shuffles of the token order
(seeds 1001..1200).
Comparison: Daniel's n65_transcription.md, same lines. Inside *...*: [..] notes removed, (?) removed, null markers
(ɦ) (ﬀ) (ﬀɦ) (ɦﬀ) removed, other parentheses and braces removed with their letters kept, accents stripped, a-z letters
one token each (v->u, y->i, j->i), · and any other glyph = context token; text outside italics = clear (separator).
usage: measure65.py <cyphersolver worktree> <no65_signs_reread.txt> <n65_transcription.md>"""
import sys, re, random, os, unicodedata
wt, mine, old = sys.argv[1:4]
sys.path.insert(0, wt); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import measure_daniel as M
from decode65 import M as KEY
SEP = ('w', '#sep#')
SEL = {'119r': set(range(32, 37)), '119v': set(range(23, 38)),
       '120r': set(range(1, 12)) | set(range(13, 21)) | {22, 23}}
def mine_tokens(p):
    toks = []
    for l in open(p, encoding='utf-8'):
        l = l.rstrip('\n')
        if not l or l.startswith('#'): continue
        sig = l.partition('\t')[2]
        for part in re.split(r'(\[[^\]]*\])', sig):
            if part.startswith('['): toks.append(SEP); continue
            part = re.sub(r'\(([^|)]*)(\|[^)]*)?\)', r'\1', part)
            for ch in part:
                if ch in ' !': continue
                if ch in 'PWRID?': toks.append(('?', '')); continue
                v = KEY[ch].replace('v', 'u').replace('y', 'i')
                toks.append(('l', v))
    return toks
def deacc(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
def old_tokens(p):
    sel = []; side = None
    for l in open(p, encoding='utf-8').read().split('\n'):
        m = re.match(r'^## f\. (\d+[rv])', l)
        if m: side = m.group(1); continue
        m = re.match(r'^L(\d\d)\s?(.*)$', l)
        if not m or side not in SEL or int(m.group(1)) not in SEL[side]: continue
        sel.append(m.group(2))
    toks = []
    for s in sel:
        s = re.sub(r'\[[^\]]*\]', '', s)
        for k, part in enumerate(re.split(r'\*', s)):
            if k % 2 == 0: toks.append(SEP); continue
            part = part.replace('(?)', '')
            part = re.sub(r'\((ɦ|ﬀ|ﬀɦ|ɦﬀ)\)', '', part)
            part = re.sub(r'[(){}]', '', deacc(part))
            for ch in part:
                if ch.isspace(): continue
                c = ch.lower().replace('v', 'u').replace('y', 'i').replace('j', 'i')
                toks.append(('l', c) if c in M.A else ('?', ''))
    return toks
LEX, scheme = M.lexicon('it-cinquecento', 20)
def score(toks, tr=None):
    f = M.read_flags(toks, LEX, tr)
    idx = [i for i, t in enumerate(toks) if t != SEP]
    return sum(f[i] for i in idx), len(idx)
A_ = mine_tokens(mine); O_ = old_tokens(old)
r, n = score(A_); ro, no = score(O_)
print(f'portion: {n} cipher-sign tokens, {sum(1 for t in A_ if t[0]=="l")} with a letter value')
print(f'M re-read = {r}/{n} = {r/n:.3f}')
print(f'M old     = {ro}/{no} = {ro/no:.3f}  (n65_transcription.md, same lines)')
ctl = []
for s in range(1, 201):
    random.seed(s); p = list(M.A); random.shuffle(p)
    ctl.append(('key', score(A_, str.maketrans(M.A, ''.join(p)))[0] / n))
flat = [t for t in A_ if t != SEP]
for s in range(1, 201):
    random.seed(1000 + s); f = flat[:]; random.shuffle(f); ctl.append(('shuf', score(f)[0] / n))
for kind in ('key', 'shuf'):
    v = sorted(x for k, x in ctl if k == kind)
    print(f'{kind}: n={len(v)} median {v[len(v)//2]:.3f} p99 {v[int(.99*len(v))-1]:.3f} max {v[-1]:.3f}')
ge = sum(1 for _, x in ctl if x >= r / n); print(f'controls >= M re-read: {ge}/400 ; p = {(ge+1)/401:.4f}')
