import sys,urllib.request,os,time
u,out,total=sys.argv[1],sys.argv[2],int(sys.argv[3])
f=open(out,'ab')
while os.path.getsize(out)<total:
    s=os.path.getsize(out)
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'Range':f'bytes={s}-','User-Agent':'Mozilla/5.0'}),timeout=120)
        if s and r.status!=206: print('no range support',r.status); break
        while True:
            b=r.read(1<<20)
            if not b: break
            f.write(b); f.flush()
    except Exception as e: print('err',e,os.path.getsize(out)); time.sleep(3)
print('done',os.path.getsize(out))
