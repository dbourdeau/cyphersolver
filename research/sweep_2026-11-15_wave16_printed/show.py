# print windows from a notes json; usage: show.py notes.json [start [n]] ; or show.py -c [bho:]<id> <pos> [width]
import json,sys,os,re
if sys.argv[1]=="-c":
    S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw"); i=sys.argv[2]
    if i.startswith("bho:"): S=os.path.join(S,"bho"); i=i[4:]
    t=open(os.path.join(S,i+".txt"),encoding='utf-8',errors='replace').read()
    p=int(sys.argv[3]); w=int(sys.argv[4]) if len(sys.argv)>4 else 2500
    u=t.rfind("@@@",0,p); print(t[u:u+80].split("\n")[0] if u>=0 else ""); print(t[max(0,p-w):p+w]); sys.exit()
d=json.load(open(sys.argv[1],encoding='utf-8'))["hits"]
a=int(sys.argv[2]) if len(sys.argv)>2 else 0; n=int(sys.argv[3]) if len(sys.argv)>3 else 40
for k,h in enumerate(d[a:a+n],a): print("#%d %s %s @%d\n%s\n"%(k,h.get("k",""),h["id"],h["pos"],h["ctx"]))
