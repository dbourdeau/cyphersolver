import openpyxl,re,collections,json
d="data/"
wb=openpyxl.load_workbook(d+"Repertoire2_ChiffreNouveau.xlsx",read_only=True,data_only=True)
ws=wb["Répertoire"] if "Répertoire" in wb.sheetnames else wb.worksheets[0]
r2=collections.defaultdict(set)
for r in ws.iter_rows(values_only=True):
    if r[0] is None or r[1] is None: continue
    try: k=int(str(r[0]).strip())
    except: continue
    r2[k].add(str(r[1]).strip())
print("R2 entries",len(r2),"max",max(r2))
wb=openpyxl.load_workbook(d+"Dossiers individuels/701218 - Message Chaudordy_ADECHIFFRER/Texte_Chaudordy.xlsx",read_only=True,data_only=True)
toks=[]
for r in wb.worksheets[0].iter_rows(values_only=True):
    for v in r:
        if v is None: continue
        toks.append(str(v).strip())
print(len(toks),"cells")
nums=[]
for t in toks:
    for p in re.split(r"[/]",t):
        m=re.match(r"^\??(\d+)\??$",p)
        if m: nums.append(int(m.group(1)))
print(len(nums),"numeric groups, distinct",len(set(nums)),"max",max(nums))
hit=[n for n in nums if n in r2]
print("covered by R2:",len(hit),"/",len(nums),"= %.1f%%"%(100*len(hit)/len(nums)))
c=collections.Counter(nums)
for n,k in c.most_common(25): print(n,k,sorted(r2.get(n,[])))
json.dump(nums,open("chaudordy_nums.json","w"))
# decode line stream
out=[ "/".join(sorted(r2[n]))[:14] if n in r2 else "[%d]"%n for n in nums]
print(" ".join(out[:150]))
