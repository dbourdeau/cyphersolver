# printed-ciphertext detector: runs of consecutive rare tokens (letters) or long runs of number groups.
# usage: ex_gib.py <id-regex> out.json
import re,os,sys,json,collections
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr"
idre=re.compile(sys.argv[1]); files=[f for f in sorted(os.listdir(S)) if idre.search(f[:-4])]
vocab=collections.Counter()
texts={}
for f in files:
    t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read(); texts[f[:-4]]=t
    vocab.update(w.lower() for w in re.findall(r"[A-Za-z]{2,}",t))
out=[]
tok=re.compile(r"[A-Za-z]{2,}|\d+")
for i,t in texts.items():
    run=[];start=None;last_end=0
    def flush():
        global run,start
        if len(run)>=5 and re.search(r"c[iy]pher|in code|key-?word",t[max(0,start-900):last_end+400],re.I): out.append({"id":i,"pos":start,"n":len(run),"kind":"letters","ctx":re.sub(r"\s+"," ",t[max(0,start-500):last_end+300])})
        run=[];start=None
    for m in tok.finditer(t):
        w=m.group(0)
        if w.isdigit(): 
            continue
        rare = vocab[w.lower()]<=2 and len(w)>=3
        if rare:
            if not run: start=m.start()
            run.append(w); last_end=m.end()
        else:
            if run and len(run)>=3 and len(w)<=3 and m.start()-last_end<6:  # tolerate one short common token inside cipher
                last_end=m.end(); continue
            flush()
    flush()
    # number runs: >=12 number groups separated by space/comma/period/dash only, with a cipher word within 600 chars before
    for m in re.finditer(r"(?:\b\d{1,4}\b[\s,.;\-]{1,3}){12,}",t):
        pre=t[max(0,m.start()-700):m.start()]
        if re.search(r"c[iy]pher|chiffr|cifra|Ziffer",pre,re.I):
            out.append({"id":i,"pos":m.start(),"n":len(re.findall(r"\d+",m.group(0))),"kind":"numbers","ctx":re.sub(r"\s+"," ",t[max(0,m.start()-500):m.end()+300])})
print(len(out),collections.Counter(x['kind'] for x in out))
json.dump(out,open(sys.argv[2],"w"),indent=0)
