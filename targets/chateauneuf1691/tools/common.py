import re, unicodedata
def norm(s, y2i=False):
    s=unicodedata.normalize('NFD',s.lower())
    s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    s=re.sub(r'\[[^\]]*\]', lambda m: m.group(0)[1:-1] if '/' not in m.group(0) else '', s) if False else s
    s=s.replace('[','').replace(']','')
    s=re.sub('[^a-z]','',s).replace('j','i').replace('v','u')
    if y2i: s=s.replace('y','i')
    return s
def tok_numbers(nline):
    """returns list of tokens: int, or None (illegible/cut), ignoring clear text in braces; also returns flags of brace breaks"""
    out=[]
    parts=re.split(r'(\{[^}]*\})',nline)
    for p in parts:
        if p.startswith('{'):
            out.append('BRK'); continue
        for t in p.split():
            t=t.strip('.,')
            if not t: continue
            m=re.match(r'^\[(\d+)/(\d+)\]',t)
            if m: out.append(int(m.group(1))); continue
            if '[...]' in t or '###' in t or t=='?[...]' : out.append(None); continue
            m=re.match(r'^(\d+)\??\^?\??$',t)
            if m: out.append(int(m.group(1))); continue
            out.append(None)
    return out
def read_gloss(path):
    rows=[]
    for l in open(path,encoding='utf-8'):
        l=l.rstrip('\n')
        if not re.match(r'^\d{4}\|',l): continue
        p=l.split('|',4)
        if len(p)<5: continue
        rows.append((p[0],p[1],int(p[2]),p[3],p[4]))
    return rows
