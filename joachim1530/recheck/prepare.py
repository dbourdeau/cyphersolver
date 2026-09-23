"""Regenerate the solver input/model from the repository's shared language engine."""
from pathlib import Path
import json
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from lang import lm
from joachim1530.solve import load
p=Path(__file__).resolve().parent
m=lm.load('it-cinquecento',order=4,spaces=False)
m.lp.astype('float32').tofile(p/'it4.bin')
(p/'input.json').write_text(json.dumps({'alpha':m.alpha,'items':load(str(p.parent/'ciphertext_dotted.txt'))}),encoding='utf-8')
print('Prepared',len(m.lp),'four-gram scores; alpha',m.alpha)
