import openpyxl,re,json,collections,glob,os
D="data/Dossiers individuels/"
SRC={ # label: (path, sheet predicate) ; only pure-number rows (cipher rows)
 "chaudordy":(D+"701218 - Message Chaudordy_ADECHIFFRER/Texte_Chaudordy.xlsx",None),
 "fav711019":(D+"2emeS_44_ADECHIFFRER/AJulesFavre_711019.xlsx",None),
 "fav710126":(D+"2emeS_45_ADECHIFFRER/AJulesFavre_710126.xlsx",None),
 "fav701218g":(D+"701218_2emeS-34_ADECHIFFRER/701218_2emeS-34_AJFavre.xlsx",lambda t:"Gauche" in t),
 "s15":(D+"2emeS-15_ADECHIFFRER/2emeS_15.xlsx",None),
 "s23g":(D+"2emeS-23_ADECHIFFRER/2emeS-23_Gauche_ADECHIFFRER.xlsx",None),
 "s35":(D+"2emeS-35_ADECHIFFRER/2emeS-35.xlsx",None),
 "fav701024":(D+"7010_23-24_ADECHIFFRER/701024_A_JulesFavre.xlsx",None),
}
def rows(path,pred):
    wb=openpyxl.load_workbook(path,read_only=True,data_only=True)
    for ws in wb.worksheets:
        if pred and not pred(ws.title): continue
        for r in ws.iter_rows(values_only=True):
            cells=[v for v in r if v is not None]
            if not cells: continue
            toks=[]
            for v in cells:
                s=str(v).strip()
                m=re.match(r"^\??0*(\d+)\??$",s)
                toks.append(int(m.group(1)) if m else None)
            if sum(t is not None for t in toks)>=0.8*len(toks) and len(toks)>=3:
                yield ws.title,[t if t is not None else 0 for t in toks]
pool={}
for k,(p,pr) in SRC.items():
    seq=[]
    sheets=collections.Counter()
    for t,r in rows(p,pr):
        seq+=r; sheets[t]+=1
    pool[k]=seq
    print(k,len(seq),"groups, max",max(seq),dict(sheets))
json.dump(pool,open("pool.json","w"))
# shared n-grams across different letters
def grams(s,n): return {tuple(s[i:i+n]) for i in range(len(s)-n+1)}
for n in (4,3):
    idx=collections.defaultdict(set)
    for k,s in pool.items():
        for g in grams(s,n): idx[g].add(k)
    sh=[(g,v) for g,v in idx.items() if len(v)>1 and 0 not in g]
    print("n=%d shared across letters: %d"%(n,len(sh)))
    for g,v in sorted(sh,key=lambda x:-len(x[1]))[:25]: print(g,sorted(v))
