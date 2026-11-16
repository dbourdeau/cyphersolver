"""Compare code W with every French numerical code table of 1755-1760 held in this repository.

W side: key/W_1757_attestations.tsv (318 groups, all 1757 values) plus key/W_sibling_values.tsv (values read from the
period decipherment of the 1756-1759 sibling letters). A W group agrees with another table when any of its values,
normalised (lower case, accents and non-letters dropped), equals the other table's value for the same number.
Lenient also counts one value contained in the other when the shorter has 3 letters or more.
Control: the other table's values are shuffled over its numbers 200 times (random.Random(1757 + k)).

Writes results/known_keys_compare.tsv and prints one line per table.
Run from the repository root:  python targets/montcalm1757w/known_keys_compare.py
"""
import csv, json, pathlib, random, re, statistics, sys

HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
sys.path.insert(0, str(HERE))
from siblings_align import load_index, norm  # noqa: E402


def w_table():
    w = {k: set(v) for k, v in load_index().items()}
    with open(HERE / 'key' / 'W_sibling_values.tsv', encoding='utf-8') as f:
        for row in csv.DictReader([ln for ln in f if not ln.startswith('#')], delimiter='\t'):
            w.setdefault(int(row['group']), set()).add(norm(row['value']))
    return w


def tsv(path, kcol, vcol):
    out = {}
    with open(path, encoding='utf-8') as f:
        for row in csv.DictReader([ln for ln in f if not ln.startswith('#')], delimiter='\t'):
            try:
                k = int(row[kcol])
            except (ValueError, TypeError):
                continue
            v = norm(row[vcol] or '')
            if v:
                out[k] = v
    return out


def jsn(path):
    d = json.load(open(path, encoding='utf-8'))
    return {int(k): norm(v) for k, v in d.items() if re.fullmatch(r'\d+', str(k)) and isinstance(v, str) and norm(v)}


TABLES = [
    ('montcalm1758i: Marine table for Montcalm, 1758, LAC sheet e001295272 (frozen)',
     lambda: {k: v for k, v in tsv(T / 'montcalm1758i/key/table_e001295272.tsv', 'cell', 'reading').items()}),
    ('vaudreuil1760 (and 1759a-c): Vaudreuil table 1757, LAC sheet e001295274 (key274.json)',
     lambda: jsn(T / 'vaudreuil1760/key/key274.json')),
    ('kerlerec1759: Louisiana Marine code, clerks\' values 1759-60 (key_manuscript.tsv)',
     lambda: tsv(T / 'kerlerec1759/key/key_manuscript.tsv', 'code', 'clerk_value')),
    ('orvilliers1759: Guiana Navy code 1757-62, key K3 (dudout/key.tsv)',
     lambda: tsv(T / 'orvilliers1759/dudout/key.tsv', 'group', 'value')),
    ('orvilliers1759: Guiana Navy code, key K4 (dudout/key_K4.tsv)',
     lambda: tsv(T / 'orvilliers1759/dudout/key_K4.tsv', 'group', 'value')),
    ('affry1757: Foreign Affairs code M, 1757-58 (key_M.json)', lambda: jsn(T / 'affry1757/key_M.json')),
    ('affry1757: Foreign Affairs code X (key_X.json)', lambda: jsn(T / 'affry1757/key_X.json')),
    ('affry1757: Foreign Affairs code B (key_B.json)', lambda: jsn(T / 'affry1757/key_B.json')),
    ('affry1757: Foreign Affairs code U (key_U.json)', lambda: jsn(T / 'affry1757/key_U.json')),
]


def score(w, other):
    shared = [k for k in w if k in other]
    ex = sum(1 for k in shared if other[k] in w[k])
    le = sum(1 for k in shared if any(other[k] == v or (min(len(v), len(other[k])) >= 3 and (v in other[k] or other[k] in v))
                                       for v in w[k]))
    return len(shared), ex, le


def main():
    w = w_table()
    rows = []
    for name, load in TABLES:
        other = load()
        n, ex, le = score(w, other)
        keys, vals = list(other), list(other.values())
        sh = []
        for k in range(200):
            v2 = vals[:]
            random.Random(1757 + k).shuffle(v2)
            sh.append(score(w, dict(zip(keys, v2)))[1])
        agree = [k for k in w if k in other and other[k] in w[k]]
        rows.append((name, len(other), n, ex, le, round(statistics.mean(sh), 2), max(sh),
                     ' '.join('%d=%s' % (k, other[k]) for k in sorted(agree))))
        print(rows[-1])
    with open(HERE / 'results' / 'known_keys_compare.tsv', 'w', encoding='utf-8') as f:
        f.write('# Code W (1757 index + sibling values, %d groups) against French code tables of 1755-1760 in this repository.\n' % len(w))
        f.write('table\tentries\tshared_numbers\texact\tlenient\tshuffled_mean_exact\tshuffled_max_exact\texact_agreements\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')


if __name__ == '__main__':
    main()
