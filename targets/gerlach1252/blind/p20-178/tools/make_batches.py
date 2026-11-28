import os,hashlib,shutil,subprocess,datetime,sys
D="/home/claude/gerlach_next"
scans=[f"{i:04d}" for i in range(23,117)]+[f"{i:04d}" for i in range(164,186)]
names="DEFGHIJKLMNOP"
batches=[]
for k in range(0,94,10): batches.append(scans[k:min(k+10,94)])
rest=scans[94:]
for k in range(0,len(rest),10): batches.append(rest[k:k+10])
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
tmpl=open(f"{D}/A/packet/PROMPT.txt").read()
with open(f"{D}/MAPPING.tsv","a") as mp:
  for b,ss in zip(names,batches):
    bd=f"{D}/{b}"
    if os.path.exists(bd): print("exists",b); continue
    os.makedirs(f"{bd}/packet"); os.makedirs(f"{bd}/img",exist_ok=True); os.makedirs(f"{bd}/judge")
    for s in ss:
        subprocess.run(["bash",f"{D}/tools/fetch.sh",b,s],check=True)
        shutil.move(f"{bd}/img/scan{s}.jpg",f"{bd}/packet/scan{s}.jpg")
        mp.write(f"{b}\t{s}\t?\tpage number to be read by blind reader\n")
    os.rmdir(f"{bd}/img")
    for f in ("key_frozen.tsv","decode_once.py","shuffle.py"): shutil.copy(f"{D}/A/{f}",f"{bd}/{f}")
    shutil.copy(f"{D}/A/packet/SHEET.md",f"{bd}/packet/SHEET.md")
    imgs=", ".join(f"scan{s}.jpg" for s in ss)
    p=tmpl.replace("9 pages (batch A)",f"{len(ss)} pages (batch {b})").replace("/gerlach_next/A/",f"/gerlach_next/{b}/").replace("blind_A_scratch",f"blind_{b}_scratch")
    i=p.index("You are given "); j=p.index(" and SHEET.md")
    p=p[:i]+f"You are given {len(ss)} page images ({imgs})"+p[j:]
    p=p.replace("141\tL01","20\tL01")
    open(f"{bd}/packet/PROMPT.txt","w").write(p)
    now=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files=["key_frozen.tsv","decode_once.py","shuffle.py","packet/SHEET.md","packet/PROMPT.txt"]+[f"packet/scan{s}.jpg" for s in ss]
    with open(f"{bd}/FREEZE.txt","w") as F:
        F.write(f"batch {b}: scans {ss[0]}-{ss[-1]}; key_frozen.tsv = A/key_frozen.tsv (key_v2); frozen {now}, before any blind transcription or decode\n\n")
        for f in files: F.write(f"{sha(f'{bd}/{f}')}  {f}\n")
        F.write(f"{sha(D+'/tools/after_blind.py')}  ../tools/after_blind.py\n")
    print(b,ss[0],ss[-1],len(ss))
