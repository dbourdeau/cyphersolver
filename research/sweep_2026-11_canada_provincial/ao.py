import subprocess,re,sys,time,html
act=open("ao_action.txt").read().strip()
def q(k):
    p=subprocess.run(["curl","-g","-s","-m","40","-A","Mozilla/5.0","-b","cj2.txt","-c","cj2.txt","-L",act,"--data-urlencode","KEYWORD_CLUSTER="+k,"-d","$RANKING=Y&MULTISEARCH=M-S"],capture_output=True)
    return p.stdout.decode("utf8","replace")
def txt(h):
    t=re.sub(r"<script.*?</script>","",h,flags=re.S);t=re.sub(r"<[^>]+>"," ",t);return html.unescape(re.sub(r"\s+"," ",t))
for k in sys.argv[1:]:
    h=q(k);t=txt(h)
    open("ao_%s.html"%re.sub(r"\W","_",k),"w",encoding="utf8").write(h)
    m=re.search(r"(\d+) results for",t) or re.search(r"of (\d+)\s+results",t)
    print("##",k,m.group(0) if m else ("DETAIL" if "Reference Code" in t else "?"), "NOREC" if "No records" in t or "no record" in t.lower() else "")
    time.sleep(3)
