# local model 'it-1540s-local': it-gutenberg (lang source, cached copy) + Serristori legations (1537-68 despatches) x3.
# Built here because gutenberg.org answered 503 to the registry fetch for it-cinquecento (24 Nov 2026).
import sys, numpy as np
sys.path.insert(0,'/home/claude/keyless/_cs')
from lang import lm
g=open('/home/claude/moonshots2/r2_s2/data/lang/corpora/it-gutenberg.txt',encoding='utf-8',errors='replace').read()
s=open('/home/claude/leads_15nov/dl/serristori_legazioni.txt',encoding='utf-8',errors='replace').read()
import re
s=re.sub(r'-\s*\n\s*','',s)
text=lm.norm(g+'\n'+(s+'\n')*3,'early',False)
alpha=lm.alphabet('early',False)
print(len(text),alpha)
for o in (5,):
    m=lm.DenseLM.build(text,o,alpha,dict(model='it-1540s-local',chars=len(text),norm='early'))
    m.save('/home/claude/keyless/ercole1547/work/it1540.o%d.ns'%o)
    for t in ['chelamaestasuahauendointesoquantomiscriuetedelleterre','xqzkwuipllmnrtbbcdfghaaeeiioouu','nonsipuosapereancorasesuamaestaandarainitalia','etfralealtrecoseuederetedintenderequelloche']:
        print(o,round(m.per_char(t),3),t)
