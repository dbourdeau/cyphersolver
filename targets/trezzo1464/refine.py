"""Choose one value per sign type for a cipher text, from the aligner's candidates, by language-model score.

usage: python3 refine.py <key.json> <cipher.txt> [lambda] [restarts] [seed]

key.json is align.py / fb.run output: {sign: [[value, weight], ...]}. For each sign type the candidates are its key
values with prior weight/total (plus a 0.02 floor); a sign absent from the key, or seen fewer than 3 times there, also
gets the 40 commonest values of the key as candidates at a small prior. The objective is the it-cinquecento order-5
score (no spaces) of the decoded text plus lambda times the sum of log priors over the tokens. Coordinate ascent over
sign types, `restarts` random starts; prints the best decode line by line, the objective, and the choices that differ
from the key's top value.
"""
import collections, json, math, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import align  # noqa: E402
from lang import lm  # noqa: E402


def candidates(key, types):
    tot_by = collections.Counter()
    for v in key.values():
        for val, w in v:
            tot_by['' if val == '_' else val] += w
    common = [v for v, _ in tot_by.most_common(40)]
    cand = {}
    for t in types:
        base = key.get(t, [])
        tot = sum(w for _, w in base) or 1.0
        c = {('' if v == '_' else v): math.log(w / tot + 0.02) for v, w in base}
        if tot < 3:
            for v in common:
                c.setdefault(v, math.log(0.01))
        cand[t] = c
    return cand


def main():
    key = json.load(open(sys.argv[1], encoding='utf-8'))
    lines = []
    for line in open(sys.argv[2], encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        lab = line.split()[0]
        toks = [t.rstrip('?') for t in line.split()[1:] if t not in align.DROP]
        lines.append((lab, toks))
    lam = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    restarts = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    rnd = random.Random(int(sys.argv[5]) if len(sys.argv) > 5 else 1)
    model = lm.load('it-cinquecento', order=5, spaces=False)
    toks = [t for _, ts in lines for t in ts]
    types = sorted(set(toks))
    cnt = collections.Counter(toks)
    cand = candidates(key, types)

    def objective(ch):
        text = ''.join(ch[t] for t in toks)
        return model.score(text) + lam * sum(cand[t][ch[t]] * cnt[t] for t in types) / 1.0

    best = None
    for r in range(restarts):
        ch = {t: (max(cand[t], key=cand[t].get) if r == 0 else rnd.choice(list(cand[t]))) for t in types}
        cur = objective(ch)
        improved = True
        while improved:
            improved = False
            for t in sorted(types, key=lambda x: -cnt[x]):
                for v in cand[t]:
                    if v == ch[t]:
                        continue
                    old = ch[t]; ch[t] = v
                    s = objective(ch)
                    if s > cur + 1e-9:
                        cur = s; improved = True
                    else:
                        ch[t] = old
        print('restart', r, 'objective', round(cur, 1), flush=True)
        if best is None or cur > best[0]:
            best = (cur, dict(ch))
    cur, ch = best
    n = sum(len(ch[t]) for t in toks)
    print('best objective', round(cur, 1), 'letters', n, 'lm/letter', round(model.score(''.join(ch[t] for t in toks)) / max(1, n), 3))
    for lab, ts in lines:
        print(lab, ' '.join((ch[t] or '·') for t in ts))
    print('changed from key top:')
    for t in sorted(types, key=lambda x: -cnt[x]):
        top = max(cand[t], key=cand[t].get)
        if ch[t] != top:
            print(' ', t, cnt[t], repr(top), '->', repr(ch[t]))
    json.dump({t: ch[t] for t in types}, open(os.path.join(HERE, 'refine_choice_l%g.json' % lam), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=0)


if __name__ == '__main__':
    main()
