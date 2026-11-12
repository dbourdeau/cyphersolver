"""Round-2 check (PREREG_round2.md, section 1): the code table, rebuilt without any mssBLA 194 gloss, against the
full transcription of mssBLA 194 (transcription/sib194_*.txt). Consistency of code and transcription only.

    python3 -I scripts/check_194.py [--target ..]
Writes results/check_194_result.json and results/check_194_output.txt.
"""
import argparse
import json
import os
import random
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_4aug import TOKEN, norm, sib_files, ALIAS  # noqa: E402
import collections  # noqa: E402

SEED = 1729
NSHUF = 200
DROP_LINE = 'L194h60893'


def build_table_without_194(paths):
    seen = collections.defaultdict(list)
    for path in paths:
        for line in open(path, encoding='utf-8'):
            if not line.startswith('L') or line.split(None, 1)[0] == DROP_LINE:
                continue
            rest = re.sub(r'\{[^}]*\}(=\S+)?', ' ', line.split(None, 1)[1])
            for m in TOKEN.finditer(rest):
                value = m.group(3)
                doubtful = bool(m.group(2)) or '?' in value
                seen[int(m.group(1))].append((value.strip('[]').lstrip('?'), doubtful))
    table = {}
    for g, occ in seen.items():
        firm = [v for v, d in occ if not d] or [v for v, _ in occ]
        table[g] = collections.Counter(ALIAS.get(v, v) for v in firm).most_common(1)[0][0]
    return table


def tokens_194(folder):
    out = []
    for name in sorted(os.listdir(folder)):
        if not (name.startswith('sib194_') and name.endswith('.txt')):
            continue
        for line in open(os.path.join(folder, name), encoding='utf-8'):
            if not line.startswith('L'):
                continue
            label, rest = line.split(None, 1)
            rest = re.sub(r'\{[^}]*\}', ' ', rest)
            for m in TOKEN.finditer(rest):
                gloss = m.group(3)
                if m.group(2) or '?' in gloss or gloss == '_':
                    continue
                out.append((f'{name[:-4]}:{label}', int(m.group(1)), gloss))
    return out


def same(gloss, value):
    a, b = norm(gloss), norm(ALIAS.get(value, value))
    if not a or not b:
        return False
    if a == b:
        return True
    short, long_ = sorted((a, b), key=len)
    return len(short) >= 3 and long_.startswith(short)


def score(toks, table):
    usable = [(w, g, gl) for w, g, gl in toks if table.get(g) not in (None, '_')]
    hits = [same(gl, table[g]) for _, g, gl in usable]
    return sum(hits), len(usable), usable, hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', default='..')
    ap.add_argument('--out', default='results')
    args = ap.parse_args()
    table = build_table_without_194(sib_files(args.target, lambda n: True))
    toks = tokens_194('transcription')
    m, n, usable, hits = score(toks, table)
    rng = random.Random(SEED)
    groups = [g for g, v in table.items() if v != '_']
    values = [table[g] for g in groups]
    shuf = []
    for _ in range(NSHUF):
        perm = values[:]
        rng.shuffle(perm)
        t = dict(table)
        t.update(zip(groups, perm))
        sm, sn, _, _ = score(toks, t)
        shuf.append(sm / sn if sn else 0.0)
    s = m / n if n else 0.0
    best, mean = max(shuf), sum(shuf) / len(shuf)
    res = {'firm_tokens_194': len(toks), 'tokens_with_table_value': n, 'matched': m, 'score': round(s, 4),
           'best_shuffled': round(best, 4), 'mean_shuffled': round(mean, 4), 'margin': round(s - best, 4),
           'pass': n >= 30 and s >= 0.80 and s - best >= 0.30, 'too_small': n < 30,
           'not_in_table': sorted({g for _, g, _ in toks if table.get(g) in (None, '_')}),
           'seed': SEED, 'n_shuffles': NSHUF}
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, 'check_194_result.json'), 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(args.out, 'check_194_output.txt'), 'w', encoding='utf-8') as f:
        f.write('# check_194.py: mssBLA 194 firm glosses against the table rebuilt without any 194 gloss.\n')
        f.write('# where group gloss(194) table-value match\n')
        for (w, g, gl), h in zip(usable, hits):
            f.write(f'{w}\t{g}\t{gl}\t{table[g]}\t{"+" if h else "MISS"}\n')
    print({k: res[k] for k in ('tokens_with_table_value', 'matched', 'score', 'best_shuffled', 'mean_shuffled',
                               'margin', 'pass', 'too_small')})
    print('not in table:', res['not_in_table'])


if __name__ == '__main__':
    main()
