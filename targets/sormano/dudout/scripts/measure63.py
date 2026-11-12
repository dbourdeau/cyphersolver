"""PREREG measure (see PREREG.md), run once. Portion = every cipher sign of no63_signs_reread.txt (no. 63 f. 115r from
"-solverse" to the foot of f. 116v). Tokens: one per cipher sign; null (!) dropped; code signs (P W R I) and unidentified
signs (?) = context tokens ('?'); doubtful signs -> first option. Clear-hand text closes a run (a non-lexical separator).
Statistic M = share of cipher-sign tokens READ by Daniel's rule (targets/matignon1586c3/f276/scripts/measure.py: run of
>= 3 lexicon words totalling >= 10 letters), lexicon it-cinquecento, mincount 20.
Controls: 200 permuted letter keys (seeds 1..200) + 200 shuffles of the token order (seeds 1001..1200).
Comparison: Daniel's n63_transcription.md, same stretch (old L23-L35 of f. 115r, all of ff. 115v, 116r, 116v),
letters inside *...* one token each, {x} kept, (?) dropped, ellipses as context tokens, text outside italics = clear.
usage: measure63.py <cyphersolver worktree> <no63_signs_reread.txt> <n63_transcription.md>"""
import sys, re, random, os
wt, mine, old = sys.argv[1:4]
sys.path.insert(0, wt); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import measure_daniel as M
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decode63 import M as KEY
SEP = ('w', '#sep#')
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
                if ch in 'PWRI?': toks.append(('?', '')); continue
                v = KEY[ch].replace('v', 'u').replace('y', 'i')
                toks.append(('l', v))
    return toks
def old_tokens(p):
    lines = open(p, encoding='utf-8').read().split('\n'); sel = []; side = None
    for l in lines:
        m = re.match(r'^## f\. (\d+[rv])', l)
        if m: side = m.group(1); continue
        m = re.match(r'^L(\d\d)\s?(.*)$', l)
        if not m or side is None: continue
        if side == '115r' and int(m.group(1)) < 23: continue
        sel.append(m.group(2))
    toks = []
    for s in sel:
        s = re.sub(r'\[[^\]]*\]\s*$', '', s)
        for k, part in enumerate(re.split(r'\*', s)):
            if k % 2 == 0: toks.append(SEP); continue
            part = part.replace('(?)', '').replace('{', '').replace('}', '')
            for ch in part:
                if ch in '…': toks.append(('?', ''))
                elif ch.isalpha():
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
print(f'M old     = {ro}/{no} = {ro/no:.3f}  (n63_transcription.md, same stretch)')
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
