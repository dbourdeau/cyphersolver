"""How many of the basis (a) values in key/clerks_values.tsv equal Pusch 2008's entry for the same code.

Usage (from the repository root or anywhere):
  python3 -I targets/kerlerec1759/scripts/compare_a_with_pusch.py [--pusch <local copy of Pusch 2008 Table 2, tsv>]

Basis (a) values were cut from the clerks' glosses without Pusch's table (scripts/clerks_segment.py run without
--pusch). This script checks them against Pusch afterwards. Matching is the one clerks_segment.py uses
(kcommon.load_table and norm: lower case, accents and punctuation dropped; code 208 read as cu, his prose p. 469).

1. Always: against the Pusch values that are in this folder, key/pusch_values_used.tsv (124 codes, the ones used in
   nos. 206, 207 and 215 with no clerk's pair in the first round).
2. With --pusch: against his whole Table 2 (Louisiana History 49:4, Fall 2008, pp. 477-480;
   https://www.jstor.org/stable/25478601; see NOTES.md, "Using Pusch's table"). That table is not in this folder and is not reproduced here; the figure
   in NOTES.md (213 of 257) was computed this way from our local copy, an OCR extraction in which accented letters
   print as '?' (load_table expands '?' to e, c or a).
"""
import csv, os, sys

here = os.path.dirname(os.path.abspath(__file__))
td = os.path.dirname(here)
sys.path.insert(0, here)
from kcommon import norm, load_table  # noqa: E402


def compare(A, table, label):
    have = [r for r in A if int(r['code']) in table]
    eq = [r for r in have if norm(r['value']) in table[int(r['code'])]]
    print(f'== against {label}')
    print(f'basis (a) codes: {len(A)}; with an entry there: {len(have)}; value equal to it: {len(eq)}')
    diff = [r for r in have if r not in eq]
    for r in diff:
        print(f"   differs  {r['code']:>4}  clerk {r['value']!r:<18} Pusch {table[int(r['code'])]}")
    return len(eq)


def main(argv):
    A = [r for r in csv.DictReader(open(os.path.join(td, 'key/clerks_values.tsv'), encoding='utf-8'), delimiter='\t')
         if r['basis'] == 'a']
    used = {}
    for line in open(os.path.join(td, 'key/pusch_values_used.tsv'), encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if line.startswith('#') or not p[0].isdigit():
            continue
        used[int(p[0])] = [norm(p[1])]
    compare(A, used, 'key/pusch_values_used.tsv (in this folder)')
    if len(argv) > 1 and argv[0] == '--pusch':
        full = load_table(argv[1])
        full[208] = ['cu']   # OCR slip in our extraction of his table; his prose gives cu (p. 469)
        compare(A, full, f'Pusch 2008 Table 2, local copy {os.path.basename(argv[1])}')


if __name__ == '__main__':
    main(sys.argv[1:])
