"""French-ness score for a letter string (no spaces): DP segmentation maximising characters covered by
lexicon words of length >= MINLEN (shorter words / unmatched chars cost nothing but score nothing).
Lexicon = modern French wordlist (fr_words.json) + early-modern spellings (EXTRA)."""
import json, unicodedata, re, functools, os
D=os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s=unicodedata.normalize('NFD',s.lower())
    s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    s=s.replace('j','i').replace('v','u').replace('y','i')
    return re.sub(r'[^a-z]','',s)
EXTRA="""doibt faict estre estat estats mesme mesmes nostre vostre noz voz roy royne angleterre espagne villeroy buzanval
bouillon rosny sully monsieur messieurs advis advertir adverty escrit escript escrire aultre aultres faulte cognoistre
cognoissance desja tousiours tesmoigner tesmoignage soubz aussy ainsy ceste cest icy faire faict faicte apres pais pays
destat paix guerre ambassadeur archiducq archiduc mareschal ennemis ennemy secours deniers argent sommes somme villes
places affaires seureté seurete dessein desseins vray vraye veoir doubte doubter peult peut vouloir voulloit
""".split()
@functools.lru_cache(None)
def lex(minlen=4):
    w=json.load(open(f'{D}/fr_words.json'))
    S={norm(x) for x in w if '-' not in x and ' ' not in x}
    S|={norm(x) for x in EXTRA}
    return frozenset(x for x in S if len(x)>=minlen)
def coverage(s,minlen=4,maxw=16):
    s=norm(s); L=lex(minlen); n=len(s)
    best=[0]*(n+1)
    for i in range(n-1,-1,-1):
        b=best[i+1]
        for k in range(minlen,min(maxw,n-i)+1):
            if s[i:i+k] in L: b=max(b,k+best[i+k])
        best[i]=b
    return best[0]/max(n,1)
if __name__=='__main__':
    import sys
    for a in sys.argv[1:]: print(a, round(coverage(a),3))
