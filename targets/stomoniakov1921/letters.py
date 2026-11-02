"""Find runs of 5-letter groups in all M316 OCR (not only figure frames)."""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
C='C:/Users/dbour/cypher/research/nara_reels/cache/'
out=[]
for reel in [604700562,604701877,604703234,604704577,604705830,604707113,604708415,604709981,604711297]:
    T={str(o['objectId']):o.get('extractedText') or '' for o in json.load(open(f'{C}{reel}.txt.json',encoding='utf-8'))}
    for d in json.load(open(f'{C}{reel}.rec.json',encoding='utf-8'))['digitalObjects']:
        t=T.get(str(d['objectId']),'')
        toks=t.split();run=[];start=0
        def flush(i):
            global run,start
            if len(run)>=8:
                out.append({'file':d['objectFilename'],'head':' '.join(toks[max(0,start-14):start]),'tail':' '.join(toks[i:i+8]),'groups':run})
            run=[]
        for i,w in enumerate(toks):
            s=w.strip('.,;:-')
            if re.fullmatch(r'[A-Z]{5}',s):
                if not run: start=i
                run.append(s)
            elif re.fullmatch(r'[A-Z]{1,4}',s) and run: run.append(s)
            else: flush(i)
        flush(len(toks))
json.dump(out,open('letter_runs.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(out),sum(len(r['groups']) for r in out))
for r in out:
    s=''.join(r['groups']);c=collections.Counter(s);n=len(s)
    ic=sum(v*(v-1) for v in c.values())/(n*(n-1))*26
    v=sum(c[x] for x in 'AEIOUY')/n
    print(r['file'][5:-4],len(r['groups']),'ic %.2f vow %.2f'%(ic,v),'|',r['head'][-70:],'|',' '.join(r['groups'][:6]),'|',r['tail'][:40])
