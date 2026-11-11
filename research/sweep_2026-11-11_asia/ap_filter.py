"""Filter harvested Abhilekh title hits for ciphertext-bearing files (intercepts, seized, foreign, undeciphered); drop code administration."""
import json, re, glob, sys
KEEP=re.compile(r'(?i)intercept|seiz|captur|found|conceal|undecipher|unable to deci|could not be deci|cannot be deci|not be decyph|German|Russian|Chinese|Afghan|Amir|Persian|Turk|Tibet|Japan|Bolshev|Soviet|enemy|suspicious|suspect|spy|secret society|Ghadr|revolution|native state|Maharaja|Nawab|Nizam|Sindia|Holkar|Mutiny|rebel|letter in cyph|in cipher|written in|wireless messages|decypher of|decipher|cryptogra|unknown code|unintelligible|mutilat')
DROP=re.compile(r'(?i)^(supply|issue|withdrawal|safe custody|return|receipt|distribution|destruction)\b')
seen={}
for fn in glob.glob('hits/*.jsonl'):
    for l in open(fn):
        r=json.loads(l); seen.setdefault(r.get('Identifier') or r['itemId'],r)
maxy=int(sys.argv[1]) if len(sys.argv)>1 else 1950
out=[]
for r in seen.values():
    y=re.match(r'\d{4}',r.get('Year','') or ''); y=int(y.group()) if y else 0
    if y>maxy: continue
    if KEEP.search(r['title']): out.append((y,r))
out.sort(key=lambda t:t[0])
for y,r in out: print(y,r.get('Identifier'),r.get('No of Pages'),r['title'][:230])
print(len(seen),len(out),file=sys.stderr)
