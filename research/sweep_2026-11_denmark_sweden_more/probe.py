import sys,requests
from rik_common import H
def ok(man,i):
    r=requests.get(f'https://lbiiif.riksarkivet.se/arkis!{man}_{i:05d}/info.json',headers=H,timeout=60);return r.status_code==200
def n(man):
    lo,hi=1,1
    while ok(man,hi): lo=hi;hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if ok(man,m):lo=m
        else:hi=m
    return lo
for m in sys.argv[1:]: print(m,n(m),flush=True)
