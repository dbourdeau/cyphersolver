import re,collections,sys
t=open('wesselenyi1664/img/DOC_R674_D1892_1892.txt',encoding='utf8').read()
body=t.split('#IMAGE NAME: 4003.png')[2]
segs=[]
for part in re.split(r'(<CLEARTEXT[^>]*>)',body):
    if part.startswith('<'): segs.append(('C',part[13:-1])); continue
    s=part.replace('s/5?','5').replace('2 o^','1 0')
    s=s.replace(' ','').replace('\r','').replace('\n','.')
    toks=[x for x in s.split('.') if x]
    m={'i':'1','b':'6','g':'9','o':'0'}
    toks=[''.join(m.get(c,c) for c in x) for x in toks]
    if toks: segs.append(('N',toks))
for k,v in segs: print(k, v if k=='C' else ' '.join(v))
allt=[x for k,v in segs if k=='N' for x in v]
print(len(allt)); print(sorted(collections.Counter(allt).items(),key=lambda x:-x[1]))
