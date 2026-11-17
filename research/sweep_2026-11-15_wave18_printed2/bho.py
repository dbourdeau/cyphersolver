# British History Online crawler: bho.py <series-path> <vol> [<vol> ...]   e.g. bho.py cal-state-papers/foreign vol11 vol12
# saves raw/bho/<series>_<vol>.txt : sections joined, each headed "@@@ <url>"
import sys,os,re,time,html,urllib.request
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw","bho")
H={"User-Agent":"Mozilla/5.0"}
def get(u):
    for k in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=90).read().decode("utf-8","replace")
        except Exception as e: err=e; time.sleep(5)
    raise err
def text(h):
    m=re.search(r"<main.*?</main>",h,re.S) or re.search(r"<body.*?</body>",h,re.S)
    h=m.group(0) if m else h
    h=re.sub(r"<(script|style|nav|header|footer).*?</\1>"," ",h,flags=re.S)
    h=re.sub(r"</(p|div|h\d|li|tr|section)>","\n",h); h=re.sub(r"<[^>]+>"," ",h)
    return re.sub(r"[ \t]+"," ",html.unescape(h))
ser=sys.argv[1]
for vol in sys.argv[2:]:
    out=os.path.join(S,ser.replace("/","_")+"_"+vol.replace("/","-")+".txt")
    if os.path.exists(out): continue
    links=[]; pg=0; ok=True
    while True:
        try: idx=get("https://www.british-history.ac.uk/%s/%s?page=%d"%(ser,vol,pg))
        except Exception as e: print("fail idx",ser,vol,pg,e,flush=True); ok=(pg>0); break
        new=[l for l in re.findall(r'href="(/%s/%s/[^"#?]+)"'%(re.escape(ser),re.escape(vol)),idx) if l not in links]
        new=list(dict.fromkeys(new))
        if not new: break
        links+=new; pg+=1; time.sleep(1)
        if "page=%d"%pg not in idx: break
    if not ok or not links: continue
    parts=[];bad=0
    for l in links:
        time.sleep(1)
        try: parts.append("@@@ "+l+"\n"+text(get("https://www.british-history.ac.uk"+l)))
        except Exception as e: bad+=1; print("fail",l,e,flush=True)
    open(out,"w",encoding="utf-8").write("\n".join(parts)); print("ok",ser,vol,len(links),bad,sum(map(len,parts)),flush=True)
    time.sleep(1)
