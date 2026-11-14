"""Décodage brut d'une transcription avec key_c01.json (sans regarder aucun clair). <100 = nul (·) ; inconnu = ‹nnn›."""
import json,sys,re
key=json.load(open(sys.argv[1]))
for l in open(sys.argv[2]):
    if not l.startswith('L'): continue
    lab,body=l.split(' ',1); out=[]
    for seg in body.strip().split('|'):
        w=[]
        for t in [x for x in seg.split('.') if x]:
            u=t.replace('?','')
            if '[' in t: w.append('‹?›')
            elif u in key: w.append(key[u][0] + ('?' if '?' in t else ''))
            elif u.isdigit() and int(u)<100: w.append('·')
            else: w.append('‹%s›'%u)
        out.append(''.join(x if x!='·' else '' for x in w))
    print(lab,' | '.join(out))
