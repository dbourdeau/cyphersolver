import sys,glob,re,fitz
pat=re.compile(r'(š|s|Š)ifr|zašifr|[Cc]hiffr|rejtjel|cifra|cifr[ao]v|kryptogr|dešifr|decipher|Geheimschr',re.I)
for f in sorted(glob.glob(sys.argv[1]+'/*.pdf')):
    try: d=fitz.open(f)
    except Exception as e: print(f,'ERR');continue
    n=0
    for p in d:
        for line in p.get_text().split('\n'):
            if re.search(r'[šŠsS]ifr|[Cc]hiffr|rejtjel|ifrov|ifrá|kryptogr|Geheimschr',line):
                n+=1;print(f.split('/')[-1],p.number+1,line[:200])
    print(f.split('/')[-1],len(d),'pages',n,'hits')
