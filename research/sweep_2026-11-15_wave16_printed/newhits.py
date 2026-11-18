# run ex_note + ex_cal patterns over all raw/*.txt, print only hits not printed before (seen.json). usage: newhits.py [A|B|AB] [max]
import re,os,sys,json,subprocess
kinds=sys.argv[1] if len(sys.argv)>1 else "A"; mx=int(sys.argv[2]) if len(sys.argv)>2 else 60
sys.stdout.reconfigure(errors="replace")
try: seen=set(json.load(open("seen.json")))
except Exception: seen=set()
subprocess.run([sys.executable,"-I","-X","utf8","ex_note.py","^(?!_)","n_note.json"],stdout=subprocess.DEVNULL)
if "B" in kinds or "C" in kinds: subprocess.run([sys.executable,"-I","-X","utf8","ex_cal.py","^(?!_)","n_cal.json"],stdout=subprocess.DEVNULL)
hits=[dict(h,k="A") for h in json.load(open("n_note.json",encoding="utf-8"))["hits"]]+json.load(open("n_cal.json",encoding="utf-8"))["hits"]
n=0; left=0; near=set()
for h in hits:
    key="%s:%d"%(h["id"],h["pos"]//400)
    sig=re.sub(r"\W+","",h["ctx"][250:450])[:80]   # same text in duplicate copies
    if key in seen or h["k"] not in kinds: continue
    if sig in near: seen.add(key); continue
    if n>=mx: left+=1; continue
    near.add(sig); seen.add(key); n+=1
    print("# %s %s @%d\n%s\n"%(h["k"],h["id"],h["pos"],h["ctx"][:1150]))
json.dump(sorted(seen),open("seen.json","w")); print("printed",n,"left",left)
