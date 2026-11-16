"""ONE measurement (PREREG-AMENDEMENT-1317-K3.md): decode the cipher runs of BnF ital. 1585 f. 71 (texts/f71_signs_portion.txt)
with the frozen key K3 (K3_key.tsv) and compare with the reference words of the period decipherment f. 70 (texts/f70_reference.txt).
Metric identical to measure_f35.py / measure_f353.py: first value of x|y; normalisation (lower case, letters only, v->u, y->i, j->i,
h dropped, doubled letters simplified); score = 1 - sum Levenshtein / sum reference length.
Controls: 200 keys shuffled inside classes (word signs = UPPER-CASE labels; nulls = empty value; letters/syllables = the rest), seed 1449.
Labels absent from K3 (e.g. @Nxx new shapes) decode to nothing.  Run: python3 -I measure_f71.py"""
import os, sys, runpy
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'measure_f353.py'), encoding='utf8').read()
src = src.replace("'texts/f353_signs.txt'", "'texts/f71_signs_portion.txt'").replace("'texts/f352_reference.txt'", "'texts/f70_reference.txt'")
src = src.replace("'K2_key.tsv'", "'K3_key.tsv'").replace('random.Random(1447)', 'random.Random(1449)')
assert "K3_key.tsv" in src and "1449" in src and "f70_reference" in src
exec(compile(src, os.path.join(here, 'measure_f353.py'), 'exec'), {'__name__': '__main__', '__file__': os.path.join(here, 'measure_f353.py')})
