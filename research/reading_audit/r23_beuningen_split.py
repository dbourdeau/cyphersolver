"""R23 (16 Nov 2026): beuningen1676 read share over cipher words only. Run from targets/beuningen1676:
    python ../../research/reading_audit/r23_beuningen_split.py
Each line of reading.txt is aligned to its line in transcription/june1676_tx.txt; reading words matching the ~clear~
segments are clear (lower case), the rest cipher (UPPER CASE); prints the labelled lines and the counts."""
import re, difflib
W=re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?|'[^\W\d_]+|\[\.\.\.\]|\[t218[^\]]*\]|\(\?\)")
tx={l[:7]:l[8:] for l in open('transcription/june1676_tx.txt',encoding='utf-8') if re.match(r'\d{3}[LR]\.\d\d ',l)}
tot=dict(cw=0,ch=0,cd=0,clw=0,clh=0,cld=0)
out=[]
for l in open('reading.txt',encoding='utf-8'):
    m=re.match(r'(\d{3}[LR]\.\d\d)\s+(.*)',l)
    if not m: continue
    lab,r=m.groups()
    r=r.replace('[struck through: ...]',' ').replace('BR[U]GGE','[...]').replace('(en)','en')   # BR[U]GGE: a supplied letter, the word is a hole
    r=re.sub(r'\[ins ([^\]]*)\]',r' \1 ',r)
    t=tx[lab]
    t=t.replace('[struck through: ...]',' ')
    clear=[w.lower() for seg in re.findall(r'~([^~]*)~',t) for w in re.findall(r"[^\W\d_]+",seg)]
    toks=re.findall(r"\[\.\.\.\]|\[t218[^\]]*\]|\(\?\)|[^\W\d_]+",r)
    words=[(i,x.lower()) for i,x in enumerate(toks) if not x.startswith(('[','('))]
    sm=difflib.SequenceMatcher(None,[w for _,w in words],clear,autojunk=False)
    cl=set()
    for a,b,n in sm.get_matching_blocks():
        for j in range(n): cl.add(words[a+j][0])
    lab_out=[]
    for i,x in enumerate(toks):
        if x.startswith('['):
            tot['ch']+=1; lab_out.append('#HOLE')
        elif x=='(?)':
            if i-1 in cl: tot['cld']+=1
            else: tot['cd']+=1
            lab_out.append('(?)')
        elif i in cl: tot['clw']+=1; lab_out.append(x.lower())
        else: tot['cw']+=1; lab_out.append(x.upper())
    out.append(lab+' '+' '.join(lab_out))
print('\n'.join(out))
print(tot)
cw,ch,cd=tot['cw'],tot['ch'],tot['cd']
print('cipher share', round(1-(ch+cd)/(cw+ch),3))
w=cw+tot['clw']; print('whole', round(1-(ch+cd+tot['cld'])/(w+ch),3))
