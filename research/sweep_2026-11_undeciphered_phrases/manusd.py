import json,sys,time,urllib.request,re
sys.stdout.reconfigure(encoding='utf-8')
for i in sys.argv[1:]:
    req=urllib.request.Request(f"https://manus.iccu.sbn.it/o/manus-api/title?id={i}",headers={"User-Agent":"Mozilla/5.0","X-Requested-With":"XMLHttpRequest"})
    t=urllib.request.urlopen(req,timeout=60).read().decode('utf8','replace')
    print('##',i,len(t))
    for m in re.finditer(r'indecifra|non decifra|cifrat|cifra\b|crittogr',t,re.I):
        print('   ...',re.sub(r'\s+',' ',t[max(0,m.start()-250):m.end()+250]))
        break
    time.sleep(1.2)
