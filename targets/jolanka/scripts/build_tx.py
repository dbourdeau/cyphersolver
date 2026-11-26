# Converts the working shorthand files in tx_short/ to TRANSCRIPTION.tsv with neutral shape labels. python3 -I tools/build_tx.py
import glob,re,os
B='/home/claude/keyless/postcards/jolanka'
M={'-':'H1','=':'H2','E':'H3','1':'V1','2':'V2','3':'V3','G':'GAM','F':'EFF','C':'RC','c':'LC','Z':'ZIG','y':'YOG','N':'TIL','X':'EX','K':'EXS','T':'TEE','S':'ESS','A':'ONE','D':'LOOP','6':'SIX','8':'EIGHT','O':'OVAL','+':'CROSS'}
out=['record\tseries\timage\tside\tline\theldout\ttokens']
for f in sorted(glob.glob(B+'/tx_short/R*.txt')):
    L=open(f,encoding='utf-8').read().split('\n'); h=L[0]
    rid=re.search(r'R(\d+)',h).group(1); ser=re.search(r'jolanka-(\d+)',h).group(1); img=re.search(r'(IMG_\S+)',h).group(1)
    ho='1' if 'HELD OUT' in h else '0'
    for l in L[1:]:
        if not l or l.startswith('#'): continue
        n,t=l.split('\t'); toks=[]
        for w in re.findall(r'\{[^}]*\}|\[[^\]]*\]|\S+',t):
            if w[0] in '{[' or w in ',.': toks.append(w); continue
            q=w.endswith('?'); w=w.rstrip('?'); acc=''
            if w.endswith('"'): acc='+aa'; w=w[:-1]
            elif w.endswith("'"): acc='+a'; w=w[:-1]
            toks.append(M[w]+acc+('?' if q else ''))
        out.append('\t'.join([rid,ser,img,'address side, main block',n,ho,' '.join(toks)]))
open(B+'/TRANSCRIPTION.tsv','w',encoding='utf-8').write('\n'.join(out)+'\n'); print(len(out)-1,'lines')
