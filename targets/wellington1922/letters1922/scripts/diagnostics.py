"""Diagnostics for the letters that missed (labelled as diagnostics only; no key search): letters used in the
hyphenated number-letter chains, and index of coincidence of the letter-only runs.
python3 -I scripts/diagnostics.py test313_transcription.tsv"""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f313 import load, clean, is_chain
R = load(sys.argv[1])
def ic(s):
    c = collections.Counter(s); n = len(s)
    return sum(v*(v-1) for v in c.values())/(n*(n-1)) if n > 1 else float('nan')
for L in ['L1','L2','L3','L4','L5','L6']:
    runs = [r for r in R if r['id'].startswith(L+'.')]
    ch = [clean(r['run'].replace('/', '-')) for r in runs if is_chain(clean(r['run']))]
    lo = [clean(r['run']).replace(' ','') for r in runs if not is_chain(clean(r['run']))]
    chl = ''.join(re.sub(r'[^A-ZÑ]', '', c) for c in ch); lol = re.sub(r'[^A-ZÑ]', '', ''.join(lo))
    nums = collections.Counter(n for c in ch for n in re.findall(r'\d+', c))
    print(f'{L}: chains {len(ch)} (letters {len(chl)}, distinct letters {"".join(sorted(set(chl)))}; distinct numbers {len(nums)}: {" ".join(sorted(nums, key=lambda x:(len(x),x)))}); letter-only runs {len(lo)} ({len(lol)} letters, IC {ic(lol):.4f})')
print('reference: IC of Spanish plain text about 0.072-0.077; random 27 letters 0.037')
