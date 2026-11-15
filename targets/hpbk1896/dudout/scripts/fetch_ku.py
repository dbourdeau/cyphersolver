# Fetch Koc HPBK page images (CC BY-NC-ND 3.0) to SPOF_2. Polite: >=6 s between requests, backoff, hard cap.
import subprocess, time, os, sys
OUT='IMGROOT/img'
ids=[int(x) for x in sys.argv[1:]]
cap=int(os.environ.get('CAP','40')); n=0
log=open(OUT+'/fetch.log','a')
for i in ids:
    p=f'{OUT}/HPBK_{i}.jpg'
    if os.path.exists(p) and os.path.getsize(p)>50000: continue
    wait=6
    for t in range(3):
        if n>=cap: print('cap reached'); sys.exit()
        url=f'https://libdigitalcollections.ku.edu.tr/iiif/2/HPBK:{i}/full/full/0/default.jpg'
        r=subprocess.run(['curl','-s','-A','Mozilla/5.0','--max-time','90','-o',p+'.part','-w','%{http_code}',url],capture_output=True,text=True)
        n+=1; code=r.stdout.strip()
        sz=os.path.getsize(p+'.part') if os.path.exists(p+'.part') else 0
        log.write(f'{time.strftime("%H:%M:%S")} {i} try{t} {code} {sz}\n'); log.flush()
        if code=='200' and sz>50000:
            os.replace(p+'.part',p); print(i,'ok',sz,flush=True); break
        time.sleep(wait); wait*=2
    else: print(i,'FAIL',flush=True)
    time.sleep(6)
print('requests',n)
