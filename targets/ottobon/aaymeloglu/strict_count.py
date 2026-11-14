"""Strict read-share count (integration of issue #552, 14 Nov 2026): words of the editorial reading in transcription.json;
words with a supplied or restored part, a ? or a [sic] form are holes.  python3 strict_count.py transcription.json"""
import json,re,sys
tr=json.load(open(sys.argv[1]))
tot=[0,0]
for piece,fols in (('first',['35r','35v','36r','36v']),('second',['37r','37v','38r'])):
  n=h=0;holes=[]
  for f in tr['folios']:
    if f['folio'] not in fols: continue
    for r in f['rows']:
      s=r['reading']
      # editorial notes following a word: [sic], [sic; x?], [ricevemmo?] after literal word -> mark previous word hole
      s=re.sub(r'(\S+)\s+\[(sic[^\]]*|ricevemmo\?)\]',lambda m:'#'+m.group(1),s)
      s=s.replace('[unresolved ending]','[...]').replace('[null]','')
      for w in re.findall(r'\S+',s):
        if not re.search(r'[\w.]',w): continue
        n+=1
        if w.startswith('#') or '[' in w or ']' in w or '?' in w: h+=1;holes.append(w)
  print(piece,'words',n,'holes',h,'strict',round(1-h/n,4)); tot[0]+=n;tot[1]+=h
  print(' ',holes)
print('all',tot,round(1-tot[1]/tot[0],4))
