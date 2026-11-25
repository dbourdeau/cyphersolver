import sys,re,csv
# KEY: letter index n (A=1..Z=26) -> 60 + (n+16) mod 26 ; i.e. A=77 ... I=85, J=60 ... Z=76
key={60+((i+16)%26):chr(64+i) for i in range(1,27)}
rows=list(csv.reader(open(sys.argv[1]),delimiter='\t'))[1:]
tot=0
for r in rows:
    toks=re.findall(r'\^?\d\??\d|——|—|-|,|\.|/|\^r\?',r[2])
    out=[]
    for t in toks:
        if t.startswith('^r'): out.append('[r]')
        elif re.fullmatch(r'\^?\d\??\d',t):
            d=t.lstrip('^'); tot+=1
            out.append(key.get(int(d),'#') if '?' not in d else '('+'/'.join(key.get(int(x+d[-1]),'#') for x in '47')+')')
        else: out.append(t if t!='/' else ' ')
    print(r[0],r[1],'|',r[2],'|',''.join(out),sep='\t')
print('pairs decoded:',tot)
