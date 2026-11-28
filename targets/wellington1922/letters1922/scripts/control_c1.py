"""C1: the decoder must reproduce Narvaez's printed decipherment of the four runs of paragraph 2, folio 2, of the
Wellington letter DCXXI.6.588.1 (Narvaez, Documenta & Instrumenta 13, 2015, pp. 123-126; cipher strings as printed
there; his printed plain text, spaces removed, his '(sic)' letters kept). Variant A (continuous).
python3 -I scripts/control_c1.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f313 import decode
CASES = [
 ('FPPWJPJFPWFVGFSDSWLEDDUJRVULHNH', 'CONTINGENTESDEPARTIDAARIOSTIEMEUSTED'),
 ('UFSXCÑLDD', 'REPUBLICA'),
 ('PPVHÑYLFVXTXÑULOBVSBUDFXWSDUEHÑMHPPBFPPHMHOFPWPVDVPDMFIDWBPWSDVDHPEHPUDÑ',
  'NOSENVIESUSULTIMASPARAEUTRARDELLENOYCONELEMENTOSAUNALVCHATANTRASCENDENTAL'),
 ('VPEUFWRERIBÑWBVGFHÑFOHÑWRT', 'SOBRETODOFALTASDEELEMENTOS'),
]
ok = True
for c, p in CASES:
    d = decode(c, 'A')
    good = d == p
    ok &= good
    print(('PASS' if good else 'FAIL'), c, '->', d, '' if good else f'(printed {p})')
print('C1', 'PASS' if ok else 'FAIL')
