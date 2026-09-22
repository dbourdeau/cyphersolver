import re,sys
t=open(sys.argv[1],encoding='utf8').read()
t='\n'.join(l for l in t.splitlines() if not l.startswith(('#','Address')))
t=re.sub(r'<[^>]*>',' ',t)
w=re.findall(r"\[[^\]]*\]\??|[\w()]+\??",t)
bad=[x for x in w if x.endswith('?') or x.startswith('[')]
print(f'words {len(w)}  unread/doubtful {len(bad)}  read {100*(len(w)-len(bad))/len(w):.1f}%'); print(bad)
