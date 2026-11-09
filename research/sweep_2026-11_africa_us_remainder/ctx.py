import sys,re,html,subprocess,time,json
ids=sys.argv[1:]
for u in ids:
    h=subprocess.run(["curl","-s","-L","-m","60","-A","Mozilla/5.0",u],capture_output=True).stdout.decode("utf8","replace")
    t=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)))
    ms=[m.start() for m in re.finditer(r'(?i)cipher|cypher|ciphered|in code|cryptogram|decipher|secret writing',t)]
    print("##",u,len(t),len(ms))
    last=-999
    k=0
    for s in ms:
        if s-last<300: continue
        last=s;k+=1
        if k>6: break
        print("  ..."+t[max(0,s-160):s+200])
    time.sleep(2)
