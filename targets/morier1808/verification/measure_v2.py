import sys,json,collections; sys.path.insert(0,'/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/morier-1808/work/scripts')
from v2 import *
key=json.load(open(W+'/key.json'))['map']
H=[w for w in load_words(W+'/H2_18_0012-0014.txt') if all(t.isdigit() and int(t)<100 for t in w)]
S,mx,lab,dec=measure(H,key)
c=collections.Counter(lab)
print('H2 counted words',len(H),dict(c))
print('BINDING S2=%.4f max control=%.4f  bar=max(0.85, %.4f)  PASS=%s'%(S,mx,mx+0.30,S>=0.85 and S>=mx+0.30))
print('non-binding strict word share=%.4f'%(c['word']/len(H)))
print(' '.join(d if l=='word' else f'[{d}:{l}]' for d,l in zip(dec,lab)))
