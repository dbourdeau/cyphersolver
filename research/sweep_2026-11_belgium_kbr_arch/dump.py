"""python dump.py <eadid> <unitid> [ancestor levels]: print a component's own text and its ancestors' titles"""
import re,sys,os
import xml.etree.ElementTree as ET
CT=re.compile(r'c(0\d|1[0-2])?')
t=lambda e: re.sub(r'\s+',' ',''.join(e.itertext())).strip() if e is not None else ''
root=ET.parse(os.path.join(r'C:\Users\dbour\cypher\research\belgium_lux\ead',sys.argv[1]+'.xml')).getroot()
uid=sys.argv[2]
def walk(c,anc):
    did=c.find('did'); u=t(did.find('unitid')) if did is not None else ''
    if u==uid:
        for a in anc[-4:]: print('^',a[:250])
        print('>>',re.sub(r'\s+',' ',' '.join(t(k) for k in c if not CT.fullmatch(k.tag)))[:1500])
        for k in [k for k in c if CT.fullmatch(k.tag)][:6]: print('   -',t(k)[:300])
        print()
    for k in c:
        if CT.fullmatch(k.tag): walk(k,anc+[u+' '+(t(did.find('unittitle')) if did is not None else '')])
for d in root.iter('dsc'):
    for k in d:
        if CT.fullmatch(k.tag): walk(k,[])
