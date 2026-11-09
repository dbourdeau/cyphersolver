import subprocess,re,sys,time,html
terms=sys.argv[1:]
for k in terms:
    for fld in ["KEYWORDS"]:
        p=subprocess.run(["curl","-s","-m","40","-A","Mozilla/5.0","-b","cj.txt","-c","cj.txt","-L","https://pam.minisisinc.com/scripts/mwimain.dll/225285137/1/0?SEARCH&ERRMSG=%5BPAM%5DdescNo.htm","--data","KEYWORDS=%s&FLD_OP1=AND_WORD&TITLE=&FLD_OP2=AND_WORD&FORMAT=&DATEDSRC=&D_SCHEDULE=&RESP_CENTRE="%k],capture_output=True)
        h=p.stdout.decode("utf8","replace")
        open("r_%s.html"%k.replace(" ","_"),"w",encoding="utf8").write(h)
        t=re.search(r"setPageTitle\('(.*?)'\)",h)
        nf="No records found" in h
        links=re.findall(r'href="([^"]*(?:DESCRIPTION|DESC)[^"]*)"[^>]*>([^<]{5,160})<',h)
        print(k,"NOREC" if nf else "", t.group(1) if t else "", len(links))
        for l in links[:40]: print("   ",html.unescape(l[1]).strip()[:140],l[0][-60:])
    time.sleep(3)
