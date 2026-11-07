import openpyxl,re,collections,json,glob,os
d="data/"
def nums_of(path,sheets=None):
    wb=openpyxl.load_workbook(path,read_only=True,data_only=True)
    out=[]
    for ws in wb.worksheets:
        if sheets and not sheets(ws.title): continue
        for r in ws.iter_rows(values_only=True):
            for v in r:
                if v is None: continue
                if isinstance(v,(int,float)) : out.append(int(v)); continue
                m=re.match(r"^\??0*(\d+)\??$",str(v).strip())
                if m: out.append(int(m.group(1)))
    return out
ch=json.load(open("chaudordy_nums.json"))
r2=nums_of(d+"Repertoire2_ChiffreNouveau.xlsx",lambda t:t.startswith(("DIL","B-part")))
print("R2 letters",len(r2),"distinct",len(set(r2)),"max",max(r2))
cr=collections.Counter(r2); cc=collections.Counter(ch)
def top(c,n=15): return [k for k,_ in c.most_common(n)]
print("R2 top",top(cr,20)); print("Chaudordy top",top(cc,20))
print("overlap of top30:",len(set(top(cr,30))&set(top(cc,30))))
# range distribution
import bisect
for name,c in(("R2",cr),("Chaud",cc)):
    t=sum(c.values())
    print(name,[round(100*sum(v for k,v in c.items() if lo<=k<hi)/t) for lo,hi in((0,100),(100,500),(500,1000),(1000,1500),(1500,2000),(2000,2400))])
# other series with same range: other xlsx with numbers < 2400 in 2emeS dossiers
for f in glob.glob(d+"Dossiers individuels/*/*.xlsx")+glob.glob(d+"Dossiers individuels/*/*/*.xlsx"):
    try: n=nums_of(f)
    except Exception as e: continue
    if len(n)<150: continue
    c=collections.Counter(n)
    print(os.path.basename(f)[:40],len(n),"max",max(n),"top5",top(c,5),"in-top30-with-Chaud",len(set(top(c,30))&set(top(cc,30))))
