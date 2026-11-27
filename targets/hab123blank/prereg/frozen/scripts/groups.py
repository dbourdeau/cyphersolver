"""Extraction des groupes chiffrés éligibles d'une passe (aucun déchiffrement ici)."""
import re
EXCL_EXACT={'fh','f','kt','p9','p9ca','p9pa','pk','B','t','p~','lp~k','zp~k','p~k','k~i','k~c','p~k6','6'}
def norm(g):
    g=re.sub(r'\[([^|\]]*)\|[^\]]*\]',r'\1',g)      # alternative -> 1re lecture
    return g
def eligible(raw,line):
    if '~' in raw or "'" in raw or '^' in raw: return False
    if any(ch.isupper() for ch in raw): return False
    g=norm(raw).replace('?','').replace('_','')
    if g in EXCL_EXACT or len(g)<2: return False
    return True
def groups(path):
    """renvoie [(ligne:int, groupe_normalisé)] pour le corps L01-L46 ; exclut barrés {..} et 'clair?'"""
    out=[]
    for line in open(path,encoding='utf-8'):
        m=re.match(r'L(\d\d)\s',line)
        if not m: continue
        n=int(m.group(1))
        body=re.sub(r'\{[^}]*\}','',line[m.end():])
        for mm in re.finditer(r'<([^>]*)>(\S*)(\s*\(clair\?\))?',body):
            raw=mm.group(1)+('~' if mm.group(2).startswith('~') else '')
            if mm.group(3): continue
            if eligible(raw,n):
                out.append((n,norm(raw).replace('?','').replace('_','')))
    return out
