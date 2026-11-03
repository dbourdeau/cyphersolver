# blindcheck.py : key-free reads, through key.tsv, against the final transcriptions. n/h confusions counted apart.
import re,json,difflib,collections
ID=json.load(open('scans/work/blind_ids_private.json'))
def final(fn):
    d={}
    for l in open(fn,encoding='utf8'):
        m=re.match(r'c\. (\d+)([rv]) l\. (\d+): (.*)',l)
        if m:
            t=re.sub(r'\{.*?\}','',m[4]).replace('[deleted signs]','')
            d[(f'c{m[1]}{m[2]}',int(m[3]))]=re.sub(r'[\[\]()]','',t).split()
    return d
N={}
for f in ['transcription_cc09_1630-02-15.txt','transcription_cc11r_1630-02-15.txt','transcription_cc16_1630-02-22.txt','transcription_cc20_1630-03-01.txt']: N.update(final(f))
B=collections.OrderedDict()
for f in ['read_c9','read_c20','read_c16']:
    for l in open(f'scans/blind/{f}.txt',encoding='utf8'):
        m=re.match(r'(c\d+[rv]) (\d+)\.(\d+):\s*(.*)',l)
        if m: B.setdefault((m[1],int(m[2])),[]).extend(re.findall(r'\[[^\]]*\]|\{clear\}|\S+',m[4]))
def dec(t):
    if t=='{clear}' or t.startswith('[del'): return None
    m=re.match(r'\[blot:(.*)\]',t)
    if m: t=m[1]
    return ID.get(t.split('/')[0],'?')
tot=collections.Counter();dif=collections.Counter();hn=collections.Counter();unc=collections.Counter()
for k,toks in B.items():
    seq=[x for x in map(dec,toks) if x]; o=N.get(k,[]); p=k[0][:-1]; tot[p]+=len(o)
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,o,seq,autojunk=False).get_opcodes():
        if op=='equal': continue
        a=o[i1:i2];c=seq[j1:j2];w=max(len(a),len(c))
        if set(a)<={'V'} and set(c)<={'v'} and a: hn[p]+=w
        elif '?' in c: unc[p]+=w
        else: dif[p]+=w
for p in tot: print(p,'signs',tot[p],'n read as h',hn[p],'unreadable to the reader',unc[p],'other differences',dif[p],round(dif[p]/tot[p]*100,1),'%')
print('all signs',sum(tot.values()),'n/h',sum(hn.values()),'unreadable',sum(unc.values()),'other',sum(dif.values()),round(sum(dif.values())/sum(tot.values())*100,1),'%')
