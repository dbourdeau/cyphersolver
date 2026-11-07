import pickle, re, collections, sys, numpy as np, os
from sklearn.svm import SVC
os.environ['KR_MINW'] = '4'
src = open('keyrefine.py', encoding='utf-8').read().split("toks = [l.split()")[0]
sys.argv = ['x', 'a', 'b', 'c']; exec(src)
recs, lab = pickle.load(open('ctts/p100_0.4.txt.pkl', 'rb')); lab = np.array(lab)
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
tok = np.array([rank[l] for l in lab])
key = {}
for line in open('ctts/kr_real4_key.txt'):
    m = re.match(r'^s(\d+) - ([A-Z])$', line.strip())
    if m: key[int(m.group(1))] = m.group(2).lower()
F = np.array([r['feat'] for r in recs]); y = np.array([key[t] for t in tok])
lines = collections.OrderedDict()
for i, r in enumerate(recs): lines.setdefault((r['page'], r['line']), []).append(i)
keys = list(lines.keys()); fold = {}
for n, k in enumerate(keys):
    for i in lines[k]: fold[i] = n % 2
fold = np.array([fold[i] for i in range(len(recs))])
pred = y.copy()
for f in (0, 1):
    tr = fold != f; te = fold == f
    clf = SVC(kernel='rbf', C=3, gamma='scale').fit(F[tr], y[tr]); pred[te] = clf.predict(F[te])
print('agreement of cross-fitted prediction with key letters', round(float((pred == y).mean()), 3))
def text_of(letters): return [''.join(letters[i] for i in idx) for idx in lines.values()]
def coverage(texts):
    cov = 0; tot = 0
    for s in texts:
        n = len(s); sc = [1e9] * (n + 1); cv = [0] * (n + 1); sc[0] = 0
        for i in range(n):
            if sc[i] >= 1e9: continue
            if sc[i] + UNK < sc[i + 1]: sc[i + 1] = sc[i] + UNK; cv[i + 1] = cv[i]
            for L in range(4, 13):
                if i + L > n: break
                c = cost.get(s[i:i + L])
                if c is not None and sc[i] + c < sc[i + L]: sc[i + L] = sc[i] + c; cv[i + L] = cv[i] + L
        cov += cv[n]; tot += n
    return cov / tot
print('coverage key letters', round(coverage(text_of(y)), 3), '| cross-fitted classifier letters', round(coverage(text_of(pred)), 3))
# control: labels shuffled among glyphs of the same cluster-size (classifier sees no true shape/label link)
rng = np.random.default_rng(0); yp = rng.permutation(y); pc = yp.copy()
for f in (0, 1):
    tr = fold != f; te = fold == f
    pc[te] = SVC(kernel='rbf', C=3, gamma='scale').fit(F[tr], yp[tr]).predict(F[te])
print('control (shuffled labels) coverage', round(coverage(text_of(pc)), 3))
open('ctts/clf_text.txt', 'w').write('\n'.join(text_of(pred)) + '\n')
