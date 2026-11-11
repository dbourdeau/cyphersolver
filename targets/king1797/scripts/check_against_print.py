"""Check a key of King's 769 code against King's printed texts of No. 30 (19 Apr 1797) and the 1801 items.

  python3 scripts/check_against_print.py [--key build/key_v1.tsv] [--shuffles 1000] [--seed 17970419]
                                         [--json checks/check_against_print.json] [--tsv checks/check_against_print_alignment.tsv]

Standard library only; deterministic (fixed seed). Reads, inside this folder:
  checks/bare_items.tsv     the blind transcription of the code groups (items No30, 1801-04-25, 1801-06-08)
  checks/print_italics.tsv  the italic (= in cipher) runs of C. R. King, Life and Correspondence 2:172-75, 3:436-38, 472-73

The measure
  Groups: every code group of the item in manuscript order (text outside {...} in bare_items.tsv). A group with an
    unreadable digit (?) has no value. Covered = groups the key gives a value.
  Truth: the letters a-z of the item's italic runs, joined in order (clear words of the copy are not used).
  Alignment: the groups are laid on the truth in order. Each group takes a stretch of the truth's letters (possibly empty).
    A group "agrees" when it takes exactly its key value; after a group marked ^, v or + the value may also be followed by
    s, es, d, ed, n, en, ing or ly (and a final e may give way to ed, en, es, ing). A group that does not agree, or has no
    value, may take 0 to 14 letters. The alignment may begin and end anywhere in the truth. Among all such alignments
    the one with the most agreeing groups is taken (dynamic programming; ties broken the same way on every run).
  Score: agreeing groups / covered groups.
  Control: the key's values are permuted at random over the key's groups (coverage unchanged), N times with a fixed
    seed, one permuted key scoring all three items; reported as mean and best, and the number of permuted keys that
    scored at least as well as the key.
"""
from pathlib import Path
import argparse, csv, hashlib, json, random, re

HERE = Path(__file__).resolve().parents[1]
ITEMS = ['No30', '1801-04-25', '1801-06-08']
MAXL = 14
SUFF = ['s', 'es', 'd', 'ed', 'n', 'en', 'ing', 'ly']
norm = lambda s: ''.join(c for c in s.lower() if 'a' <= c <= 'z')


def load_groups():
    """item -> list of dict(g=int or None, marked=bool, raw, where)."""
    out = {k: [] for k in ITEMS}
    for r in csv.DictReader((HERE / 'checks/bare_items.tsv').open(encoding='utf-8'), delimiter='\t'):
        if r['item'] not in out: continue
        code = re.sub(r'\{[^}]*\}', ' ', r['content'])
        for t in re.findall(r'[\d?]+[\^v+]*', code):
            d = re.sub(r'[\^v+]', '', t)
            out[r['item']].append(dict(raw=t, g=None if '?' in d else int(d), marked=bool(re.search(r'[\^v+]', t)),
                                       where=f"{r['frame'][4:]} {r['page']}{r['line']}"))
    return out


def load_truth():
    out = {k: [] for k in ITEMS}
    lines = [l for l in (HERE / 'checks/print_italics.tsv').read_text(encoding='utf-8').splitlines() if not l.startswith('#')]
    for r in csv.DictReader(lines, delimiter='\t'):
        out[r['item']].append(r['italic_text'])
    return {k: norm(' '.join(v)) for k, v in out.items()}


def load_key(path):
    return {int(r['group']): norm(r['value']) for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t')
            if norm(r['value'])}


def occurrences(T, v, marked, cache):
    """(start, end) of every place in T where v (with an allowed suffix, if marked) can lie."""
    k = (v, marked)
    if k in cache: return cache[k]
    forms = {v}
    if marked:
        forms |= {v + s for s in SUFF}
        if v.endswith('e'): forms |= {v[:-1] + s for s in ('ed', 'en', 'es', 'ing')}
    occ = []
    for f in sorted(forms):
        p = T.find(f)
        while p != -1:
            occ.append((p, p + len(f))); p = T.find(f, p + 1)
    cache[k] = sorted(set(occ))
    return cache[k]


def shift_max(a, k):
    return a[:k] + list(map(max, a[k:], a[:-k]))


def best_alignment(T, groups, key, cache, trace=False):
    """Most agreeing groups over all in-order alignments (see the module docstring)."""
    n = len(T) + 1
    best = [0] * n                         # free start: any position, nothing agreed yet
    back = []
    for it in groups:
        w = shift_max(shift_max(shift_max(shift_max(best, 1), 2), 4), 7)   # w[p] = max(best[p-14 .. p])
        new = w[:]
        v = key.get(it['g']) if it['g'] is not None else None
        hits = {}
        if v:
            for s, e in occurrences(T, v, it['marked'], cache):
                if best[s] + 1 > new[e] or (best[s] + 1 == new[e] and e in hits and s > hits[e]):
                    new[e] = best[s] + 1; hits[e] = s
            hits = {e: s for e, s in hits.items() if new[e] == best[s] + 1}
        if trace: back.append((best, hits))
        best = new
    m = max(best)
    if not trace: return m, None
    # backtrace from the first end position with the maximum: an agreement where one gives the value, else the
    # nearest earlier position (0-14 letters back) that gives it
    p = best.index(m); path = []
    for i in range(len(groups) - 1, -1, -1):
        prev, hits = back[i]; want = best[p]
        if p in hits and prev[hits[p]] + 1 == want:
            s = hits[p]; path.append((s, p, True))
        else:
            s = next(q for q in range(p, max(-1, p - MAXL - 1), -1) if prev[q] == want); path.append((s, p, False))
        p, best = s, prev
    path.reverse()
    return m, path


def score_items(key, groups, truth, caches, trace=False):
    res, paths = {}, {}
    for k in ITEMS:
        gs = groups[k]; covered = sum(1 for it in gs if it['g'] is not None and it['g'] in key)
        m, path = best_alignment(truth[k], gs, key, caches[k], trace)
        res[k] = dict(groups=len(gs), covered=covered, coverage=round(covered / len(gs), 3), agree=m,
                      score=round(m / covered, 3) if covered else None)
        paths[k] = path
    return res, paths


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--key', default=str(HERE / 'build/key_v1.tsv'))
    ap.add_argument('--shuffles', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=17970419)
    ap.add_argument('--json'); ap.add_argument('--tsv')
    a = ap.parse_args()
    groups, truth, key = load_groups(), load_truth(), load_key(a.key)
    caches = {k: {} for k in ITEMS}
    res, paths = score_items(key, groups, truth, caches, trace=True)
    rng = random.Random(a.seed); gl = sorted(key); vl = [key[g] for g in gl]
    base = {k: [] for k in ITEMS}
    for _ in range(a.shuffles):
        sh = vl[:]; rng.shuffle(sh)
        r2, _ = score_items(dict(zip(gl, sh)), groups, truth, caches)
        for k in ITEMS: base[k].append(r2[k]['agree'] / r2[k]['covered'] if r2[k]['covered'] else 0.0)
    for k in ITEMS:
        b = base[k]; s = res[k]['agree'] / res[k]['covered']
        res[k].update(truth_letters=len(truth[k]), shuffled_mean=round(sum(b) / len(b), 3), shuffled_best=round(max(b), 3),
                      shuffled_at_least_score=sum(1 for x in b if x >= s - 1e-12))
    sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    out = dict(script='scripts/check_against_print.py', key=Path(a.key).resolve().relative_to(HERE).as_posix(),
               key_sha256=sha(a.key), key_groups=len(key),
               inputs={p: sha(HERE / p) for p in ('checks/bare_items.tsv', 'checks/print_italics.tsv')},
               shuffles=a.shuffles, seed=a.seed, max_letters_unmatched_group=MAXL, results=res)
    text = json.dumps(out, indent=1) + '\n'
    print(text, end='')
    if a.json: Path(a.json).write_text(text, encoding='utf-8')
    if a.tsv:
        with open(a.tsv, 'w', encoding='utf-8') as f:
            f.write('item\tn\twhere\tgroup\tvalue\tprint_letters\tagrees\n')
            for k in ITEMS:
                T = truth[k]
                for i, (it, (s, e, ok)) in enumerate(zip(groups[k], paths[k]), 1):
                    v = key.get(it['g'], '') if it['g'] is not None else ''
                    f.write(f"{k}\t{i}\t{it['where']}\t{it['raw']}\t{v}\t{T[s:e]}\t{'y' if ok else ('n' if v else '-')}\n")


if __name__ == '__main__':
    main()
