#!/usr/bin/env python3
"""Mesure unique pré-déclarée (PREREG.md). Usage: python3 -I score.py <transcription_arbitree.json>"""
import json, sys, random, unicodedata, re, os
D=os.path.dirname(os.path.abspath(__file__))
MAP1655={"none":"","acute":"′","diaeresis":"¨","caron":"ˇ","macron":"¯","dot":"·","tilde":"^","grave":"`"}
def norm(s):
    s=unicodedata.normalize("NFD",s.lower()); s="".join(c for c in s if c.isalpha() and ord(c)<128)
    return s.replace("j","i").replace("v","u").replace("y","i")
def lev(a,b):
    p=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        c=[i]
        for j,cb in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(ca!=cb)))
        p=c
    return p[-1]
def sim(h,r): return 1-lev(h,r)/max(len(h),len(r),1)
def heldout_tokens(tr):
    runs=tr["runs"]; idx_clear=[i for i,r in enumerate(runs) if r["type"]=="clear"]
    ciph=[i for i,r in enumerate(runs) if r["type"]=="cipher"]
    first_clear=idx_clear[0]; last_c=ciph[-1]
    toks=[]
    for i in ciph:
        if first_clear<i<last_c: toks+=runs[i]["tokens"]
    return toks
def lookup_k2(K,t): return K.get(t)
def lookup_k1(K,t):
    if t.startswith("SYM:"): return None
    n,m=t.split("|"); return K.get(n+MAP1655.get(m,"?"))
def decode(toks,K,look):
    out=[]
    for t in toks:
        if t.endswith("|macron"): continue
        v=look(K,t)
        if v: out.append(v[0])
    return norm("".join(out))
def main():
    tr=json.load(open(sys.argv[1])); toks=heldout_tokens(tr)
    ref=norm("".join(l for l in open(D+"/reference_brianson_688.txt") if not l.startswith("#")))
    k2={k:v for k,v in json.load(open(D+"/K2_brianson.json"))["table"].items()}
    k1={k:v["valeurs"] for k,v in json.load(open(D+"/K1_key1655.json"))["table"].items() if v.get("valeurs")}
    res={"n_signes_heldout":len(toks),"n_signes_mesures":sum(1 for t in toks if not t.endswith("|macron")),"len_ref":len(ref)}
    rng=random.Random(20261123)
    for name,K,look in (("K1_1655",k1,lookup_k1),("K2_brianson",k2,lookup_k2)):
        h=decode(toks,K,look); s=sim(h,ref)
        keys=list(K); vals=[K[k] for k in keys]; ctr=[]
        for _ in range(200):
            v=vals[:]; rng.shuffle(v); ctr.append(sim(decode(toks,dict(zip(keys,v)),look),ref))
        best=max(ctr); cov=sum(1 for t in toks if not t.endswith("|macron") and look(K,t))/max(res["n_signes_mesures"],1)
        res[name]={"accord_caracteres":round(s,4),"meilleur_temoin":round(best,4),"moyenne_temoins":round(sum(ctr)/200,4),
          "couverture_signes":round(cov,4),"VALIDE":bool(s>=0.85 and s>=best+0.30),"decodage":h}
    res["reference"]=ref
    print(json.dumps(res,ensure_ascii=False,indent=1))
main()
