# print a calendar entry by number from a BHO volume file; usage: entry.py <file-substr> <no> [<no>...]
import sys,os,re
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw","bho")
f=[x for x in sorted(os.listdir(S)) if sys.argv[1] in x][0]
t=open(os.path.join(S,f),encoding="utf-8").read()
for n in sys.argv[2:]:
    for m in re.finditer(r"(?<![\d,.])%s\. "%re.escape(n),t):
        a=max(0,m.start()-120); e=t[a:m.start()+int(os.environ.get("W","1800"))]
        u=t.rfind("@@@",0,m.start()); print("==",f,n,t[u:u+90].split("\n")[0]); print(re.sub(r"\s+"," ",e)); print()
