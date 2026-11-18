import json,re,time,html,urllib.request
d=json.load(open('_tmp/penn_raw.json',encoding='utf8'))
sel={'cipher','cypher','ciphers','ciphered','cryptogram','"secret writing"','"in cipher"','decipher','deciphered','deciphering','cryptograph*','"key to the cipher"','cryptographic','"code book"','"numerical code"','"secret code"','"code letter"','encrypted'}
RX=re.compile(r'cipher|cypher|cryptogra|decipher|decrypt|secret writing|in code\b|code book|codebook|numerical code|secret code|encod|key to the',re.I)
out={}
for r in d.values():
    if not set(r['terms'])&sel: continue
    m=re.match(r'(\d{4})',r['date'])
    if m and int(m.group(1))>=1920: continue
    u='https://findingaids.library.upenn.edu/inventory/'+r['href'].split('/records/')[1]+'/details'
    try: t=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf8','replace')
    except Exception as e: print('ERR',r['id'],e); continue
    x=html.unescape(re.sub(r'<[^>]+>',' ',t));x=re.sub(r'\s+',' ',x)
    ctx=[x[max(0,m.start()-160):m.end()+200] for m in RX.finditer(x)]
    out[r['id']]={'title':r['title'],'date':r['date'],'repo':r['repo'],'href':r['href'],'n':len(ctx),'ctx':ctx[:8]}
    time.sleep(1.5)
json.dump(out,open('_tmp/penn_ead.json','w',encoding='utf8'),ensure_ascii=False,indent=0)
print(len(out))
