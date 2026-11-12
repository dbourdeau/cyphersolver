"""Décodage ligne à ligne d'une transcription de Daniel (format 'lab g g | g'). Inconnu -> ‹nnn›."""
import sys, json, re
key=json.load(open(sys.argv[1]))
tot=kn=0
for l in open(sys.argv[2]):
    if l.startswith('#') or not l.strip(): continue
    lab,rest=l.rstrip('\n').split(' ',1)
    rest=re.sub(r'\[del:[^\]]*\]','',rest)
    out=[]
    for t in rest.split():
        if t=='|': out.append('|'); continue
        g=re.sub(r"[?'`]",'',t)
        if not g.isdigit(): continue
        tot+=1
        s=key.get(g)
        if s is None: out.append('‹%s›'%g)
        else: kn+=1; out.append(s if s else '·')
    print(lab,' '.join(out))
print('# groupes',tot,'connus',kn,round(kn/max(tot,1),3),file=sys.stderr)
