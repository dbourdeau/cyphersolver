"""autotag.py DRAFT SIGNS_TXT KEY_CODES_TSV > READING : mechanical S/P tagging of a reading draft (C04).
DRAFT lines: `ref word word ...` in Spanish as read by sense. Words already marked are kept as written: <w> (I),
[w] (R), {w†} (needs a sign other than the one transcribed), «clear» (not counted). A plain word is matched IN ORDER
against the line's tokens (key unchanged: codes -> key_codes.tsv, letters -> decode_lot3.SIGN with its declared
alternatives), as an exact spelling by a contiguous run of whole tokens (normalised u=v, i=j=y, accents dropped):
  - matched, no multi-valued sign and no '?' code value in the run -> S (plain) ;
  - matched through a multi-valued sign or a '?' code value -> {w} (P) ;
  - not matched -> ?w? flagged on stderr (to be marked by hand as {w†}, [w] or <w>; never left in the reading).
Alignment (C04 R9640 fork): per line, the plain words are placed in order on the tokens by a dynamic programme that
maximises the number of matched words (ties: fewest skipped tokens), so a short word cannot jump ahead of its place. A word ending in '-' is joined to the first word of the next line and matched over both lines (counted there)."""
import sys, re
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from decode_lot3 import SIGN, NULLS
from pass2_check import norm, code_opts
def load(p):
    K, Q = {}, set()
    for line in open(p, encoding='utf-8').read().splitlines()[1:]:
        if '\t' in line:
            c, v = line.split('\t', 1); c = c.rstrip('?'); K[c] = code_opts(v)
            if '?' in re.sub(r'\[.*?\]', '', v): Q.add(c)
    return K, Q
def toks_of(toks, K, Q):
    out = []
    for t in toks:
        t0 = t.rstrip('?').lstrip('^')
        if t0 in NULLS or t0 == '|': continue
        if t0.startswith('=') or t0.startswith('['): out.append(None); continue
        if t0 in SIGN:
            o = [norm(x) for x in SIGN[t0].strip('()').split('|')]; out.append((o, len(o) > 1)); continue
        out.append((K[t0], t0 in Q) if t0 in K else None)
    return out
def rec_at(w, T, i):
    return match(w, T, i, 0)[1:] if match(w, T, i, 0) else None
def match(w, T, start, slack=10**6):
    def rec(j, r, amb):
        if not r: return (j, amb)
        if j >= len(T) or T[j] is None: return None
        opts, a = T[j]
        for o in opts:
            if o and r.startswith(o):
                x = rec(j + 1, r[len(o):], amb or a)
                if x: return x
        return None
    for i in range(start, min(len(T), start + slack + 1)):
        x = rec(i, w, False)
        if x: return i, x[0], x[1]
    return None
def main():
    K, Q = load(sys.argv[3]); P = {}
    for line in open(sys.argv[2], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        f = line.split(); P[f[0]] = f[1:]
    lines = [l.rstrip('\n') for l in open(sys.argv[1], encoding='utf-8')]
    refs = [l.split(' ', 1)[0] for l in lines if l.strip() and not l.startswith('#')]
    carry = None; pend = None; nflag = 0
    for l in lines:
        if l.startswith('#') or not l.strip(): print(l); continue
        ref, txt = (l.split(' ', 1) + [''])[:2]
        T = toks_of(P.get(ref, []), K, Q); off = 0
        if carry is not None: T = carry + T; off = len(carry)   # rest of previous line, for a word split across lines
        parts = re.findall(r'«[^»]*»|\{[^}]*\}|\[[^\]]*\]|<[^>]*>|\S+', txt)
        carry = None; p0 = pend; pend = None
        last = len(parts) - 1
        if parts and parts[last][0] not in '«{[<' and parts[last].endswith('-'): split = last
        else: split = None
        items = []                                  # (index in parts, normalised word, min start)
        for k, w in enumerate(parts):
            if w[0] in '«{[<' or k == split: continue
            if p0 is not None and k == 0: items.append((k, norm(p0 + w), 0, True))
            else: items.append((k, norm(w), off, False))
        cands = []
        for k, w, mn, first in items:
            c = []
            for i in (range(0, off) if first else range(mn, len(T))):
                x = rec_at(w, T, i)
                if x: c.append((i, x[0], x[1]))
            cands.append(c)
        memo = {}
        def best(n, pos):                           # (matched, -gap, choices) over items[n:]
            if n == len(items): return (0, 0, ())
            key = (n, pos)
            if key in memo: return memo[key]
            r = best(n + 1, pos); r = (r[0], r[1], (None,) + r[2])
            for (i, e, amb) in cands[n]:
                if i < pos: continue
                q = best(n + 1, e); q = (q[0] + 1, q[1] - (i - pos), ((i, e, amb),) + q[2])
                if (q[0], q[1]) > (r[0], r[1]): r = q
            memo[key] = r; return r
        res = best(0, 0 if (items and items[0][3]) else off)
        tag = {}; endp = off
        for (k, w, mn, first), ch in zip(items, res[2]):
            tag[k] = ch
            if ch: endp = max(endp, ch[1])
        out = []
        for k, w in enumerate(parts):
            if w[0] in '«{[<': out.append(w); continue
            if k == split:
                out.append(w); pend = w[:-1]; carry = T[endp:]; continue
            ch = tag.get(k)
            if ch: out.append('{%s}' % w if ch[2] else w)
            else: out.append('?%s?' % w); nflag += 1; print('FLAG', ref, w, file=sys.stderr)
        print(ref, ' '.join(out))
    print('# flagged:', nflag, file=sys.stderr)
if __name__ == '__main__': main()
