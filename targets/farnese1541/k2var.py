"""Compare whole variants of key 2's single-digit layer on R91 (syllable table as printed)."""
import sys
from key1 import beam_decode, lm, lines
from key2 import K2
m = lm.load('it-cinquecento', order=5, spaces=False)
d = ''.join(t[0] for _, _, toks, _ in lines() for t in toks)
SYL = {k: v for k, v in K2.items() if len(k) == 2 and k not in ('01', '11')}
V = {
 'print_et1_11null': {'3':'a','5':'e','7':'i','9':'o','0':'u','8':'bc','01':'dfg','2':'lp','4':'nm','6':'rt','1':['et'],'11':['']},
 'sz1_et11':        {'3':'a','5':'e','7':'i','9':'o','0':'u','8':'bc','01':'dfg','2':'lp','4':'nm','6':'rt','1':'sz','11':['et']},
 'sz1_11null':      {'3':'a','5':'e','7':'i','9':'o','0':'u','8':'bc','01':'dfg','2':'lp','4':'nm','6':'rt','1':'sz','11':['']},
 'sz1_et11_or_null':{'3':'a','5':'e','7':'i','9':'o','0':'u','8':'bc','01':'dfg','2':'lp','4':'nm','6':'rt','1':'sz','11':['et','']},
}
for name, sing in V.items():
    K = {k: list(v) for k, v in SYL.items()}
    for c, outs in sing.items():
        K.setdefault(c, []).extend(list(outs))
    s, path = beam_decode(d, K, m, 32)
    txt = ''.join(o for _, o in path)
    print(f'{name:18} {s:9.1f} skips {txt.count("#")}  {txt[:150]}')
