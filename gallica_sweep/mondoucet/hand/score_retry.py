# Control for the retry: decode the 16 July block (ct_f62 + ct_f62v) with each key and score against the Court's
# verbatim reading (pt_f64.txt). Score = letters of pt_f64 matched by a monotone alignment (difflib, no autojunk)
# of the decoded letter stream (nulls dropped), over the letters of pt_f64. NB key2 was built on this same block,
# so this is a fit check of the key change, not a held-out test (the held-out test is f1573's 79.0 %).
import sys, os, re, difflib, unicodedata
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import decode_retry as D
def norm(t):
    t=unicodedata.normalize('NFD',t); t=''.join(c for c in t if unicodedata.category(c)!='Mn').lower()
    t=t.replace('j','i').replace('v','u').replace('w','u'); return ''.join(c for c in t if c in D.ALPHA)
pt=norm(''.join(l for l in open(os.path.join(D.M,'pt_f64.txt'),encoding='utf-8') if not l.startswith('#')))
H=D.H
for name in sys.argv[1:]:
    out=D.run(name,[os.path.join(H,'ct_f62.txt'),os.path.join(H,'ct_f62v.txt')])
    dec=''.join(s for _,s,_ in out).replace('·','').replace('u','u')
    sm=difflib.SequenceMatcher(None,dec,pt,autojunk=False); m=sum(b.size for b in sm.get_matching_blocks())
    print('%-6s decoded %d letters, pt %d letters, matched %d = %.1f %% of pt'%(name,len(dec),len(pt),m,100*m/len(pt)))
