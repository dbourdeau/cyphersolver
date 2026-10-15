import json
idx=json.load(open('qwork/index.json'))
ch={1,3,4,7,9,10,12,13,16,18,20,21,23,26,27,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,53,54,55,57,59,60,62,63,64,65,67,68,69,70,71,72,74,76,78,86,88,102,104,105,106,108,114,118,120,141,144,146,147,150}
senseA={3,12,18,23,27,32,34,35,37,39,40,41,42,43,50,51,54,57,59,60,62,63,64,65,68,74,86,102,105,146}
senseM={6,11,15,17,19,22,24,25,28,33,48,52,66,77,85,93,97,99,103,109,110,113,115,116,119,121,123,124,127,128,130,131,132,136,143,148}
note={0:'q not clearly located (plut/T cluster); kept',2:'bare q, no bar visible; sense weakly a; kept',5:'bare q, no bar; kept',8:'bare q, no bar; kept',14:'bare q, no bar; kept',73:'bare q, no bar; kept',94:'image shows ah here, no q; kept',95:'image shows mt here (culpa); kept',111:'bare q, no bar; kept',126:'bare q, no bar; kept',137:'bare q, no bar; kept',58:'image has q1 before this q, missing from transcription (sigamos)',61:'image has q1 before this q, missing from transcription (fagamos)',18:'bar faint; sense espana'}
rows=['file\tline\ttoken\told\tnew\tbasis\tnote']
edits={}
for k,(f,tag,i) in enumerate(idx):
    new='q1' if k in ch else 'q'
    b='both' if (k in senseA or k in senseM) else 'image'
    if k in note and k not in ch and k not in senseM: b='doubtful'
    rows.append(f"{f}\t{tag}\t{i}\tq\t{new}\t{b}\t{note.get(k,'')}")
    if new=='q1': edits.setdefault(f,set()).add((tag,i))
open('qwork/q_decisions.tsv','w',encoding='utf-8').write('\n'.join(rows)+'\n')
for f in ['n45_pp03-09.txt','n45_pp10-15.txt','n57_transcription.txt']:
    out=[];hdr=False;n=0
    for l in open(f,encoding='utf-8'):
        if l.startswith('L'):
            tag,body=l.rstrip('\n').split(':',1);t=body.split()
            for (tg,i) in edits.get(f,()):
                if tg==tag: assert t[i]=='q'; t[i]='q1'; n+=1
            l=tag+': '+' '.join(t)+'\n'
        elif not hdr and not l.startswith('#'): pass
        out.append(l)
    # header after first comment block line
    out.insert(1,'# v2 (5 Oct 2026): q/q1 pass - every q checked on the image; single-bar q relabelled q1 (=a); see qwork/q_decisions.tsv\n')
    g=f.replace('.txt','_v2.txt'); open(g,'w',encoding='utf-8').write(''.join(out))
    tot=sum(1 for x in idx if x[0]==f); print(f,'total',tot,'changed',n,'kept',tot-n)
