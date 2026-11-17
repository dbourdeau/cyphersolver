"""The one pre-registered measure for key_c02 on the 20/31 Aug 1764 letter (PREREG-AUG1764.md).
usage: python3 -I measure_aug.py key.json cipher.txt clear.txt [--show]
Decode: every group >= 100 with the first value of the key (no value / unknown group -> nothing).
CA (decision metric) = share of the DECODED letters that lie in difflib matching blocks of >= 4 letters between the decode
   and the normalised clear (a-z, accents stripped; [del:..] dropped, [ins:..] kept, [?] dropped).
M (reported, not decisive) = share of the CLEAR letters covered by the same blocks (the metric of check2.py / measure_june.py).
Controls: 200 random permutations of the non-empty values over the groups that have one; random.seed(17640820)."""
import json,sys,re,random,difflib,unicodedata
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); return re.sub(r'[^a-z]','',s)
def clear_text(path):
    out=[]
    for l in open(path,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        p=l.split(None,1)
        if len(p)<2: continue
        t=re.sub(r'\[del:[^\]]*\]','',p[1]); t=re.sub(r'\[ins:([^\]]*)\]',r'\1',t); t=t.replace('[?]','')
        out.append(t)
    return norm(' '.join(out))
def groups_of(path):
    gs=[]
    for l in open(path,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        p=l.split(None,1)
        if len(p)<2: continue
        for g in re.split(r'[\s.|]+',p[1]):
            v=re.sub(r'[^0-9]','',g.split('/')[0])
            if v and int(v)>=100: gs.append(str(int(v)))
    return gs
def run(keypath,cpath,clpath,show=False):
    K=json.load(open(keypath)); km={k:norm(v[0]) if v and v[0] else '' for k,v in K.items()}
    gs=groups_of(cpath); gl=clear_text(clpath)
    def score(m):
        d=''.join(m.get(g,'') for g in gs)
        sm=difflib.SequenceMatcher(None,d,gl,autojunk=False)
        hit=sum(b.size for b in sm.get_matching_blocks() if b.size>=4)
        return hit/max(len(d),1), hit/max(len(gl),1), d
    ca,M,d=score(km)
    ks=[k for k in km if km[k]]; vals=[km[k] for k in ks]
    random.seed(17640820); cc=[]; cm=[]
    for i in range(200):
        random.shuffle(vals); m=dict(km); m.update(zip(ks,vals)); a,b,_=score(m); cc.append(a); cm.append(b)
    cov=sum(1 for g in gs if km.get(g))/max(len(gs),1)
    mx=max(cc); ok= ca>=0.85 and ca>=mx+0.30
    res={"groups_ge100":len(gs),"key_coverage":round(cov,3),"decoded_letters":len(d),"clear_letters":len(gl),
      "CA":round(ca,4),"CA_ctrl_max":round(mx,4),"CA_ctrl_mean":round(sum(cc)/len(cc),4),
      "M":round(M,4),"M_ctrl_max":round(max(cm),4),
      "threshold":"CA>=0.85 and CA>=CA_ctrl_max+0.30","verdict":"PASS" if ok else "FAIL"}
    print(json.dumps(res,indent=1))
    if show: print(d)
    return res
if __name__=='__main__': run(sys.argv[1],sys.argv[2],sys.argv[3],'--show' in sys.argv)
