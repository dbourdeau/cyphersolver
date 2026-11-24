"""Decode the digit passages of c. 48 and c. 49r with the frozen key of system Y held in ../capilupi1546
(dudout/KEY-1555.json, longest code first, the same parse as its measure_1555.py). 14 Nov 2026.
Usage (from this folder): python scripts/decode_digits.py transcription_c48.txt > decryption_c48.txt
? = doubtful digit kept as a hole; # = digit with no code; bracketed clear text and (blot) are passed through."""
import json,re,sys,pathlib
key=json.load(open(pathlib.Path(__file__).resolve().parents[2]/'capilupi1546'/'dudout'/'KEY-1555.json',encoding='utf8')); key.pop('_parse',None)
codes={k:v for k,v in key.items() if not k.startswith('_')}
L=max(len(k) for k in codes)
def dec(seg):
    out='';i=0
    while i<len(seg):
        if seg[i]=='?': out+='?'; i+=1; continue
        for n in range(min(L,len(seg)-i),0,-1):
            if seg[i:i+n] in codes:
                v=codes[seg[i:i+n]]; out+= '' if v.startswith('[') else v; i+=n; break
        else: out+='#'; i+=1
    return out
for f in sys.argv[1:]:
    for l in open(f,encoding='utf8'):
        l=l.rstrip('\n')
        if l.startswith('#') or not l.strip(): continue
        lab,body=l.split(' ',1)
        parts=re.split(r'(\[[^\]]*\]|\(blot\))',body)
        o=''
        for p in parts:
            if p.startswith('[') or p.startswith('('): o+=' '+p+' '
            else: o+=dec(re.sub(r'\s+','',p))
        print(lab,o.strip())
