"""pass2_check.py READING PASS2_SIGNS KEY_CODES_TSV : PREREG_lot3 §3, second pass on the image for the † words of a reading.
For each {word†} of READING (line ref L), the independent blind re-transcription PASS2_SIGNS is decoded with the key unchanged
(code groups -> key_codes.tsv values; letter signs -> decode_lot3.SIGN with its declared alternatives) over the window of
lines L-1, L, L+1 (same page). The word is CONFIRMED iff it has >= 3 letters and can be spelled exactly by a contiguous run
of whole tokens of that window (one option per token). Normalisation: lower case, accents dropped, n~ -> n, u=v, i=j=y,
spaces dropped. Control: the same test against the window centred 7 lines further on (cyclic over all pass-2 refs); the
confirmations are applied only if the control rate <= 10 %. Output one line per † word, then the totals. No key change."""
import sys, re, unicodedata
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from decode_lot3 import SIGN, NULLS
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.sub('[^a-z]', '', s.replace('ñ', 'n').replace('u', 'v').replace('j', 'i').replace('y', 'i'))
def code_opts(v):
    v = re.sub(r'\[.*?\]', '', v).replace('?', ''); out = set()
    for p in v.split('/'):
        out.add(norm(re.sub(r'\(.*?\)', '', p))); out.add(norm(p.replace('(', '').replace(')', '')))
    return sorted(o for o in out if o)
def load(p):
    K = {}
    for line in open(p, encoding='utf-8').read().splitlines()[1:]:
        if '\t' in line: c, v = line.split('\t', 1); K[c.rstrip('?')] = code_opts(v)
    return K
def sign_opts(t):
    v = SIGN[t]; return [norm(x) for x in v.strip('()').split('|')]
def line_opts(toks, K):
    out = []
    for t in toks:
        t0 = t.rstrip('?').lstrip('^')
        if t0 in NULLS or t0 == '|': continue
        if t0.startswith('=') or t0.startswith('['): out.append(None); continue
        if t0 in SIGN: out.append(sign_opts(t0)); continue
        out.append(K.get(t0))                         # None for unknown groups: breaks a run
    return out
def spell(w, opts):
    def rec(j, r):
        if not r: return True
        if j >= len(opts) or opts[j] is None: return False
        return any(r.startswith(o) and rec(j + 1, r[len(o):]) for o in opts[j])
    return any(rec(i, w) for i in range(len(opts)))
def main():
    K = load(sys.argv[3]); P = {}
    for line in open(sys.argv[2], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        f = line.split(); P[f[0]] = f[1:]
    refs = list(P); conf = tot = short = cconf = 0
    for line in open(sys.argv[1], encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        ref, txt = line.split(' ', 1); pg, n = ref.split('.')
        win = []
        for k in (int(n) - 1, int(n), int(n) + 1):
            win += line_opts(P.get('%s.%02d' % (pg, k), []), K) + [None]
        for m in re.finditer(r'\{([^}]*)†\}', txt):
            w = norm(m.group(1)); tot += 1
            if len(w) < 3: short += 1; print(ref, m.group(1), 'SHORT (stays †)'); continue
            ok = spell(w, win); conf += ok
            if ref in P:
                j = (refs.index(ref) + 7) % len(refs); cw = []
                for k in (j - 1, j, j + 1): cw += line_opts(P[refs[k % len(refs)]], K) + [None]
                cconf += spell(w, cw)
            print(ref, m.group(1), 'CONFIRMED' if ok else 'not confirmed')
    print('# † words %d : confirmed %d, not confirmed %d, short %d' % (tot, conf, tot - conf - short, short))
    n = tot - short; rate = cconf / n if n else 0
    print('# control (window +7 lines): %d/%d = %.1f %%  -> %s' % (cconf, n, 100*rate, 'APPLY' if rate <= 0.10 else 'DO NOT APPLY'))
if __name__ == '__main__': main()
