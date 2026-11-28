import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigparse import parse_lines
from solve import solve
lam,R,IT=float(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
lines=[' '.join(l.split()[1:]) for l in open(sys.argv[1],encoding='utf8') if l.startswith(('48r','48v'))]
toks,K,_=parse_lines(lines)
d,o,l,dec,_=solve(toks,K,True,lam,R,IT,2811)
print(len([t for t in toks if t>=0]),'signes',K,'classes dir',d,'lm/sym',round(l,3)); print(dec)
