"""Cohérence signe->lettre (définition de Daniel, keys_eye/REPORT.md) :
part des occurrences de formes vues >=2 fois (paires alignées) qui prennent la lettre majoritaire de la forme."""
import json, sys, collections
def load_pairs(path):
    d = json.load(open(path))
    pairs = []
    for row in d['alignment']:
        line, pos, shape, letter = row[0], row[1], row[2], row[3]
        if shape and letter:
            pairs.append((line, pos, shape, letter))
    return d, pairs
def consistency(pairs):
    by = collections.defaultdict(collections.Counter)
    for _, _, s, l in pairs: by[s][l] += 1
    rep = {s: c for s, c in by.items() if sum(c.values()) >= 2}
    occ = sum(sum(c.values()) for c in rep.values())
    ok = sum(c.most_common(1)[0][1] for c in rep.values())
    breaks = {s: dict(c) for s, c in rep.items() if len(c) > 1}
    return ok, occ, (ok / occ if occ else None), breaks, {s: dict(c) for s, c in by.items()}
if __name__ == '__main__':
    for p in sys.argv[1:]:
        d, pairs = load_pairs(p)
        ok, occ, r, br, _ = consistency(pairs)
        print(d['chain_id'], f'{ok}/{occ} = {r:.3f}', 'ruptures:', json.dumps(br, ensure_ascii=False))
