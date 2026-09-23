"""Hard-EM over the word decoder: decode, count which letter each sign label was read as (incl. substitutions),
then give every label the letters it takes >= FRAC of the time. Iterate."""
import sys, json, collections
import wdec
from decode import load
FILES = sys.argv[2].split(','); KEY = json.load(open(sys.argv[1], encoding='utf8'))
FRAC = 0.15; LOCK = {'1','E','K','M','3','Z'}
def run(KEY):
    L = load(FILES); cnt = collections.defaultdict(collections.Counter); texts = {}
    for fname in FILES:
        pre = fname.split('.')[0] + '.'
        stream = [t for name, toks in L if name.startswith(pre) for t in toks] + ['...']
        cur = []
        for t in stream:
            if t == '...':
                if cur:
                    out, sc = wdec.decode_stream(cur, KEY)
                    for i, j, w in out:
                        if w.startswith('?'): continue
                        # re-derive per-sign letters greedily
                        pos = 0
                        for k in range(i, j):
                            vs = wdec.vals(KEY, cur[k])
                            m = next((v for v in sorted(vs, key=len, reverse=True) if v and w.startswith(v, pos)), None)
                            if m is None:
                                if '' in vs: continue
                                m = w[pos:pos+1]
                            cnt[cur[k]][m] += 1; pos += len(m)
                cur = []
            else: cur.append(t)
    return cnt
for it in range(int(sys.argv[3]) if len(sys.argv) > 3 else 3):
    cnt = run(KEY); new = dict(KEY)
    for lab, c in cnt.items():
        if lab in LOCK: continue
        tot = sum(c.values())
        keep = [v for v, k in c.most_common() if k >= FRAC * tot][:3]
        if keep: new[lab] = ','.join(keep)
    ch = {k: (KEY.get(k), new[k]) for k in new if KEY.get(k) != new[k]}
    print('iter', it, ch, flush=True)
    KEY = new
json.dump(KEY, open('key_em.json', 'w'), indent=0)
