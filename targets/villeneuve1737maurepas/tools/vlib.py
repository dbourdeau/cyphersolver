"""Villeneuve 1737 tooling: parsing transcriptions, building passages. No key inside."""
import re,json,unicodedata,difflib
T="/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/villeneuve-1737/transcr"
def parse(path):
    pages={};cur=None
    for ln in open(path,encoding='utf-8'):
        ln=ln.rstrip('\n')
        m=re.match(r'#\s*(\d{4}[LRS])\s*$',ln)
        if m: cur=m.group(1); pages[cur]=[]; continue
        if cur is None or ln.startswith('#') or not ln.strip(): continue
        m=re.match(r'L(\d+)(?:-L\d+)?\s+([CGTN]):\s?(.*)$',ln)
        if not m: continue
        no,k,p=int(m.group(1)),m.group(2),m.group(3)
        if k=='C': pages[cur].append((no,'C',re.findall(r'«[^»]*»|\[G\]|\S+',p)))
        else: pages[cur].append((no,k,p))
    return pages
def nz(s):
    s=re.sub(r'‹…›','#',s); s=s.replace('‹','').replace('›','')
    s=re.sub(r'\[\?\]','',s); s=re.sub(r'~[^~]*~','',s)
    s=unicodedata.normalize('NFD',s); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.lower().replace('j','i').replace('v','u')
    return re.sub(r'[^a-z#]','',s)
def cc(t):
    t=t.split('|')[0]; d=re.sub(r'[^0-9]','',t.split('^')[0])
    return d if d else '?'
def rows(pages_list, gloss_file=f"{T}/gloss_careful.txt"):
    """per cipher line: codes (merged), gutter flag, gloss (careful)"""
    M=json.load(open(f"{T}/merged_cipher.json"))
    A=parse(f"{T}/passA_witness.txt"); A.update(parse(f"{T}/passA_targets.txt"))
    G=parse(gloss_file) if gloss_file else {}
    out=[]
    for pg in pages_list:
        gl={no:p for no,k,p in G.get(pg,[]) if k=='G'}
        for no,k,p in A[pg]:
            if k!='C': continue
            codes=[t for (l,t,s) in M[pg] if l==no]
            out.append(dict(pg=pg,no=no,codes=codes,gutter=('[G]' in p),
                            clear=[x for x in p if x.startswith('«')],raw=p,gloss=gl.get(no,'')))
    return out
def passages(rs):
    """page-level concatenation: codes stream with GAP at gutter losses; gloss stream (# = lacuna)"""
    P={}
    for r in rs:
        p=P.setdefault(r['pg'],{'codes':[],'g':''})
        p['g']+=nz(r['gloss'])
        p['codes']+=[cc(t) for t in r['codes']]+(['GAP'] if r['gutter'] else [])
    return P

def chunks(rs, nlines=3):
    """non-overlapping chunks of consecutive cipher lines of a page (a line without gloss is kept
    with the following line); returns list of {'codes','g'}"""
    out=[]; cur=None; cnt=0; pg=None
    for r in rs:
        if cur is None or r['pg']!=pg or (cnt>=nlines and prev_has_gloss):
            if cur and cur['codes']: out.append(cur)
            cur={'codes':[],'g':'','pg':r['pg']}; cnt=0; pg=r['pg']
        cur['g']+=nz(r['gloss'])
        cur['codes']+=[cc(t) for t in r['codes']]+(['GAP'] if r['gutter'] else [])
        cnt+=1; prev_has_gloss=bool(r['gloss'].strip())
    if cur and cur['codes']: out.append(cur)
    return out
