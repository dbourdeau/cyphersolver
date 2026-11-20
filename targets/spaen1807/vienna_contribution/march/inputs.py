"""Serialize the finite candidate segments of No. 23. No held-out French input."""
from pathlib import Path
import csv,re,unicodedata
p=Path(__file__).resolve().parent
def normalize(text):
    s=unicodedata.normalize('NFD',text.lower().replace('œ','oe').replace('æ','ae'))
    return re.findall('[a-z0-9]+',''.join(c for c in s if not unicodedata.combining(c)))
def codes(n):
    return [r['strict'] for r in csv.DictReader((p/f'groups{n}.tsv').open(),delimiter='\t')]
def main():
    groups=codes(23)
    ids={w:i for i,w in enumerate(sorted(set(groups)-{'?'}))}
    words=normalize((p/'train23.txt').read_text())
    letters=''.join(words)
    edges=[];labels=['NULL'];lids={'NULL':0}
    def edge(start,length,tag,base,whole):
        if tag not in lids: lids[tag]=len(labels);labels.append(tag)
        edges.append((start,length,lids[tag],base,whole))
    start=0
    vowels='aeiouy'
    for idx,w in enumerate(words):
        for a in range(len(w)):
            for b in range(a+1,len(w)+1):
                whole=a==0 and b==len(w)
                if b-a>(20 if whole else 10): continue
                role='W' if whole else 'B' if a==0 else 'E' if b==len(w) else 'M'
                seg=w[a:b];length=len(seg)
                # Soft bonuses for syllabic units and likely break points.
                base=1.0 if 2<=length<=4 else 0.48 if length==1 else 0.70**(length-4)
                if any(c in vowels for c in seg): base*=1.4
                if b<len(w) and b>0 and w[b-1] in vowels and w[b] not in vowels:base*=1.35
                if a>0 and w[a-1] in vowels and w[a] not in vowels:base*=1.35
                edge(start+a,length,role+'|'+seg,base,int(whole))
        if idx+1<len(words) and len(w)+len(words[idx+1])<=20:
            edge(start,len(w)+len(words[idx+1]),'P|'+w+'_'+words[idx+1],0.11,0)
        start+=len(w)
    for pos in range(len(letters)+1):edge(pos,0,'NULL',0.018,0)
    (p/'labels.txt').write_text('\n'.join(labels)+'\n')
    with (p/'alignment_input.txt').open('w') as f:
        print(len(groups),len(letters),len(labels),len(ids),len(edges),file=f)
        print(*(ids.get(w,-1) for w in groups),file=f)
        for e in edges:print(*e,file=f)
if __name__=='__main__':main()
