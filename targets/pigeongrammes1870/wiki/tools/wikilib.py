"""Shared helpers for the wiki tools: parse pages, list pages, write pages, append to the log."""
import os,re,json,datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS={"source":"sources","entity":"entities","system":"systems","claim":"claims","question":"questions","test":"tests","synthesis":"syntheses"}
def parse(path):
    t=open(path,encoding="utf8").read()
    m=re.match(r"---\n(.*?)\n---\n(.*)",t,re.S)
    if not m: return None,t
    fm={}
    for line in m.group(1).split("\n"):
        if ":" not in line: continue
        k,v=line.split(":",1); k=k.strip(); v=v.strip()
        if v.startswith("[") and v.endswith("]"):
            v=[x.strip() for x in v[1:-1].split(",") if x.strip()]
        fm[k]=v
    return fm,m.group(2)
def pages():
    out={}
    for typ,d in DIRS.items():
        p=os.path.join(ROOT,d)
        if not os.path.isdir(p): continue
        for f in sorted(os.listdir(p)):
            if f.endswith(".md"):
                fm,body=parse(os.path.join(p,f)); out[f[:-3]]=(fm,body,os.path.join(p,f))
    return out
def write_page(typ,pid,fm,body):
    d=os.path.join(ROOT,DIRS[typ]); os.makedirs(d,exist_ok=True)
    lines=["---"]
    for k,v in fm.items(): lines.append("%s: [%s]"%(k,", ".join(v)) if isinstance(v,list) else "%s: %s"%(k,v))
    lines+=["---","",body.strip(),""]
    open(os.path.join(d,pid+".md"),"w",encoding="utf8").write("\n".join(lines))
def log(kind,subject,text):
    p=os.path.join(ROOT,"log.md")
    with open(p,"a",encoding="utf8") as f:
        f.write("\n## [%s] %s | %s\n%s\n"%(datetime.date.today().isoformat() if False else "2026-11-07",kind,subject,text.strip()))
def load_lex(code):
    return json.load(open(os.path.join(ROOT,"lexicon_%s.json"%code),encoding="utf8"))
def save_lex(code,obj):
    json.dump(obj,open(os.path.join(ROOT,"lexicon_%s.json"%code),"w",encoding="utf8"),indent=1,ensure_ascii=False)
def next_id(prefix,start,existing):
    n=start
    while "%s%03d"%(prefix,n) in existing: n+=1
    return "%s%03d"%(prefix,n)
