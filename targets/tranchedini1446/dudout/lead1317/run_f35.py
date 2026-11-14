"""Re-run the f. 35 measurement (measure_f35.py, frozen; sha in HASHES-1317.txt) from this repository's layout.
measure_f35.py reads the key at ../nicodemus-r5318/R5318_crosswalk.tsv (the French original of the R5318 key, sha 04c8ae96...).
In this repository the same key is targets/tranchedini1446/r5318/key_R5318_by_1448_label.tsv (comments translated, values
unchanged); this wrapper only points measure_f35.py at that file.  Run: python3 -I run_f35.py"""
import os
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'measure_f35.py'), encoding='utf8').read()
old = "os.path.join(here, '..', 'nicodemus-r5318', 'R5318_crosswalk.tsv')"
assert old in src
src = src.replace(old, "os.path.join(here, '..', '..', 'r5318', 'key_R5318_by_1448_label.tsv')")
exec(compile(src, os.path.join(here, 'measure_f35.py'), 'exec'), {'__name__': '__main__', '__file__': os.path.join(here, 'measure_f35.py')})
