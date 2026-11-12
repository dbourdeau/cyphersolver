import sys,re,json,hashlib
sys.path.insert(0,'/home/claude/en/trackB/b116_biermann_glyph/scripts')
import count_b105 as cb
B73='/home/claude/en/trackB/b73_biermann_v4_heldout/'
TX={'0628':'kl_0628_tx.txt','07B':'kl_07B_tx.txt','07C':'kl_07C_tx.txt'}
cls={r.split('\t')[0]:r.rstrip('\n').split('\t') for r in open('frozen/glyph_classes_FROZEN.tsv') if r.startswith('C')}
mp=[l.split() for l in open('work/map_cands_to_b73.tsv')]
mode=sys.argv[1]  # 'b73' | 'glyph' | 'glyph_unclearH'
table=json.load(open(B73+'frozen/table_M3.json')); table={k:v for k,v in table.items() if not k.startswith('_')}
words=json.load(open(B73+'frozen/words_FROZEN_v4.json')); words={k:v for k,v in words.items() if not k.startswith('_')}
tot=[0,0,0]; res={}
for tag,f in TX.items():
    L=open(B73+'tx/'+f).read().split('\n')
    changes=0
    for t,ln,ix,cid in mp:
        if t!=tag: continue
        ln=int(ln); ix=int(ix); c=cls[cid][7]
        new = 'H' if (c=='H' or (c=='?' and mode=='glyph_unclearH')) else '#'
        if mode=='b73': new='#'
        line=L[ln-1]; parts=re.split(r'(\{[^}]*\})',line); k=0; done=False
        for pi,p in enumerate(parts):
            if p.startswith('{'): continue
            toks=re.split(r'(\s+)',p)
            for ti,tk in enumerate(toks):
                if not tk.strip(): continue
                if k==ix:
                    assert tk.rstrip('?"')=='#',(tag,ln,ix,tk)
                    toks[ti]=tk.replace('#',new,1); done=True
                k+=1
            parts[pi]=''.join(toks)
        assert done,(tag,ln,ix)
        L[ln-1]=''.join(parts); changes+= new=='H'
    out='work/kl_%s_tx_%s.txt'%(tag,mode); open(out,'w').write('\n'.join(L))
    r=cb.score(out,B73+'work/gloss_%s_v4.tsv'%tag,table,words)
    res[tag]=(r['strict'],r['N'],r['lenient'],changes)
    tot[0]+=r['strict'];tot[1]+=r['N'];tot[2]+=r['lenient']
    print(f"{mode}\t{tag}\tH-tokens set {changes}\tstrict {r['strict']}/{r['N']} = {100*r['strict']/r['N']:.2f}%\tlenient {r['lenient']}/{r['N']}\t{hashlib.md5(open(out,'rb').read()).hexdigest()[:8]}")
print(f"{mode}\tPOOLED\tstrict {' + '.join(str(res[t][0]) for t in TX)} = {tot[0]} ; {' + '.join(str(res[t][1]) for t in TX)} = {tot[1]} ; {tot[0]}/{tot[1]} = {100*tot[0]/tot[1]:.2f}%\tlenient {tot[2]}/{tot[1]} = {100*tot[2]/tot[1]:.2f}%")
