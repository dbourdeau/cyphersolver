"""Relative size of Linear A fraction signs from their written order.

Uses sign identities only. The transliteratedWords field of the working corpus
already carries editorial fraction values (e.g. 1/2, 1/4); it is never read here.
A cluster is the run of fraction signs written after one entry's integer, inside
one editorial entry (newline = entry boundary); clusters with damage are dropped.

Assumption under test: compound fractions are written largest first, as in the
Linear B and later Aegean metrological tradition. The script finds the ranking
of signs that violates the fewest observed adjacent pairs (exact, by DP over
subsets), then asks how firmly each pairwise order is fixed.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
import unicodedata as ud

ROOT = Path(__file__).resolve().parent
ROWS = json.loads((ROOT / 'data/corpus.json').read_text(encoding='utf-8'))
DAMAGE = '\U0001076b'
NAMES = Counter(r['name'] for r in ROWS)


def is_fraction(ch):
    return 0x10740 <= ord(ch) <= 0x1075f


def sign(ch):
    return ud.name(ch).split()[-1]


def clusters():
    """Yield (record, [signs]) for every undamaged cluster of >= 1 fraction sign."""
    for r in ROWS:
        if NAMES[r['name']] != 1:
            continue
        buf = []
        entries = [[]]
        for w in r['words']:
            if w == '\n':
                entries.append([])
            elif not w.isspace():
                entries[-1].append(w)
        for entry in entries:
            run = []
            for w in entry + [None]:
                quantity = w is not None and all(
                    ud.name(ch, '').startswith('AEGEAN NUMBER') or is_fraction(ch) or ch == DAMAGE for ch in w)
                if quantity:
                    run.append(w)
                    continue
                s = ''.join(run)
                run = []
                f = [sign(ch) for ch in s if is_fraction(ch)]
                if f and DAMAGE not in s:
                    buf.append((r['name'], r['site'], f))
        yield from buf


def best_orders(signs, pairs):
    """Exact minimum-violation linear orders (largest first) by DP over subsets."""
    idx = {s: i for i, s in enumerate(signs)}
    n = len(signs)
    # cost of placing s after every sign already in mask: pairs (s before t) with t in mask are violated
    before = [[0] * n for _ in range(n)]
    for (a, b), k in pairs.items():
        if a in idx and b in idx and a != b:
            before[idx[a]][idx[b]] += k
    INF = float('inf')
    dp = [INF] * (1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        if dp[mask] == INF:
            continue
        for s in range(n):
            if mask >> s & 1:
                continue
            cost = sum(before[s][t] for t in range(n) if mask >> t & 1)
            nm = mask | 1 << s
            if dp[mask] + cost < dp[nm]:
                dp[nm] = dp[mask] + cost
    # count optimal orders and, per pair, in how many optimal orders a precedes b
    from functools import lru_cache
    full = (1 << n) - 1

    @lru_cache(None)
    def ways(mask):  # number of optimal completions from mask
        if mask == full:
            return 1
        tot = 0
        for s in range(n):
            if mask >> s & 1:
                continue
            cost = sum(before[s][t] for t in range(n) if mask >> t & 1)
            nm = mask | 1 << s
            if dp[mask] + cost == dp[nm] and dp[nm] + rest(nm) == dp[full]:
                tot += ways(nm)
        return tot

    @lru_cache(None)
    def rest(mask):  # minimal remaining cost from mask to full
        if mask == full:
            return 0
        return min(sum(before[s][t] for t in range(n) if mask >> t & 1) + rest(mask | 1 << s)
                   for s in range(n) if not mask >> s & 1)

    # enumerate optimal orders (few signs, so feasible)
    orders = []

    def walk(mask, seq):
        if len(orders) > 5000:
            return
        if mask == full:
            orders.append(seq)
            return
        for s in range(n):
            if mask >> s & 1:
                continue
            cost = sum(before[s][t] for t in range(n) if mask >> t & 1)
            nm = mask | 1 << s
            if dp[mask] + cost == dp[nm] and dp[nm] + rest(nm) == dp[full]:
                walk(nm, seq + [signs[s]])
    walk(0, [])
    return dp[full], orders


def main():
    data = list(clusters())
    singles = Counter(s for _, _, f in data for s in f)
    pairs = Counter()
    where = defaultdict(list)
    repeats = Counter()
    for name, site, f in data:
        for a, b in zip(f, f[1:]):
            if a == b:
                repeats[a] += 1
                where[(a, a)].append(name)
            else:
                pairs[(a, b)] += 1
                where[(a, b)].append(name)
    ordered = sorted({s for p in pairs for s in p})
    violations, orders = best_orders(ordered, pairs)
    # For each pair of signs that co-occur, fraction of optimal orders putting a first
    agreement = {}
    for a, b in combinations(ordered, 2):
        k = sum(o.index(a) < o.index(b) for o in orders)
        agreement[f'{a}>{b}'] = round(k / len(orders), 3)
    # Pairs attested in both directions
    both = {f'{a}/{b}': [pairs[(a, b)], pairs[(b, a)]] for a, b in combinations(ordered, 2)
            if pairs[(a, b)] and pairs[(b, a)]}
    # Chain of direct attested precedences with no contrary evidence
    firm = sorted(f'{a}>{b} ({k})' for (a, b), k in pairs.items() if not pairs[(b, a)])
    result = {
        'method': __doc__.strip(),
        'clusters': len(data), 'multi_sign_clusters': sum(len(f) > 1 for _, _, f in data),
        'sign_frequency_in_clusters': dict(singles.most_common()),
        'adjacent_pairs': {f'{a} {b}': {'count': k, 'records': where[(a, b)]} for (a, b), k in pairs.most_common()},
        'repeated_sign_pairs': {f'{a} {a}': {'count': k, 'records': where[(a, a)]} for a, k in repeats.most_common()},
        'pairs_attested_both_ways': both,
        'unopposed_precedences': firm,
        'min_violations': violations,
        'total_pair_tokens': sum(pairs.values()),
        'optimal_orders_count': len(orders),
        'optimal_orders_sample': [' > '.join(o) for o in orders[:12]],
        'pairwise_share_of_optimal_orders': agreement,
    }
    (ROOT / 'fraction_order_results.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('clusters', result['clusters'], 'multi-sign', result['multi_sign_clusters'])
    print('pairs', dict(pairs.most_common()))
    print('repeats', dict(repeats))
    print('both ways', both)
    print('min violations', violations, 'of', sum(pairs.values()), '; optimal orders', len(orders))
    for o in orders[:12]:
        print('  ', ' > '.join(o))
    print('firm pairwise (share of optimal orders = 1.0):',
          [k for k, v in agreement.items() if v == 1.0])
    print('reversed-firm (share 0.0):', [k for k, v in agreement.items() if v == 0.0])


if __name__ == '__main__':
    main()
