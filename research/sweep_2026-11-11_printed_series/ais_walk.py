# walk consecutive AIS detail IDs and print signature/title/dates; usage: ais_walk.py start n
import sys,re,html,time,urllib.request
a=int(sys.argv[1]); n=int(sys.argv[2])
for i in range(a,a+n):
    try:
        s=urllib.request.urlopen(urllib.request.Request("https://www.archivinformationssystem.at/detail.aspx?ID=%d"%i,headers={"User-Agent":"Mozilla/5.0"}),timeout=40).read().decode("utf-8","replace")
    except Exception as e:
        print(i,"ERR",e); time.sleep(3); continue
    t=re.sub(r"[\s|]+"," ",html.unescape(re.sub(r"<[^>]+>","|",re.sub(r"<script.*?</script>","",s,flags=re.S))))
    m=re.search(r"Signatur: (.*?) Titel: (.*?) Entstehungszeitraum: (.*?) Stufe",t)
    print(i,"|",m.groups() if m else t[:80],flush=True)
    time.sleep(2.5)
