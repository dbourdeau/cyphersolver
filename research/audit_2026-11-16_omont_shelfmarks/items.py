"""Print given items (by number) of a Français volume: python -I -X utf8 items.py N no[,no...]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import am
N = int(sys.argv[1]); want = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else None
n, d = am.find_fr(N)
print(f'fr. {N} cc{n} {am.url(n)} items on page: {len(d["items"])}')
for no, tx, fol in d['items']:
    if want is None or no in want:
        print(f'  {no} [f. {fol}] {tx[:300]}')
