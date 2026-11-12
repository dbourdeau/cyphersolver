"""dec.py KEY.tsv TX.txt [UNITS_OUT.tsv]  -- single decoder for PARSER.md P1. python3 -I, stdlib only."""
import re,sys
LINE=re.compile(r'^(\d+[rv]\.L\d+):(.*)$')
UNIT=re.compile(r"^(c?)(x?)(\d+)((?:[_'?]|\^\d)*)$")
def loadkey(p):
    k={}
    for l in open(p,encoding='utf-8'):
        f=l.rstrip('\n').split('\t')
        if len(f)<2 or f[0] in('token','') or f[0].startswith('#'): continue
        k[f[0]]=f[1]
    return k
def parse_piece(p,extra=''):
    """-> dict(raw,canon,cls-pre,flags,marks,x)"""
    u={'raw':p,'flags':set(extra),'canon':None,'acc':'','sup':'','x':False,'ill':False,'struck':False}
    m=re.search(r'\[([^\]]*)\]',p)
    if m:
        if m.group(1).strip()=='struck': u['struck']=True
        else: u['flags'].add('D')
        p=re.sub(r'\[[^\]]*\]','',p)
    if u['struck']: return u
    if '|' in p:
        alts=p.split('|'); subs=[parse_piece(a) for a in alts]
        first=subs[0]; first['raw']=u['raw']; first['flags']|=u['flags']
        if len({s['canon'] for s in subs})>1 or any(s['ill'] for s in subs): first['flags'].add('ALT')
        return first
    m=UNIT.match(p)
    if not m: u['ill']=True; return u
    c,x,d,suf=m.groups()
    if c: u['flags'].add('C')
    if '?' in suf: u['flags'].add('D')
    u['canon']=d+('_' if '_' in suf else ''); u['acc']="'" if "'" in suf else ''
    s=re.search(r'\^(\d)',suf); u['sup']='^'+s.group(1) if s else ''
    u['x']=bool(x); u['digits']=d
    return u
def parse_body(body):
    """yield ('clear',text) or ('unit',u)"""
    for part in re.split(r'(\{[^}]*\})',body):
        if part.startswith('{'): yield ('clear',part[1:-1]); continue
        for ch in part.split():
            if ch=='[struck]': yield ('unit',parse_piece('[struck]')); continue
            extra=''
            m=re.match(r'^\^\((.*)\)([.,:;=]*)$',ch)
            if m: ch=m.group(1); extra='R'
            while True:
                n=ch.rstrip('=').rstrip('.,:;')
                if n==ch: break
                ch=n
            if not ch: continue
            for pc in ch.split('-'):
                if pc in('','?'): continue
                yield ('unit',parse_piece(pc,extra))
def classify(u,key):
    if u['struck']: return 'X','[x]'
    if u['ill']: return 'ILL','#'
    d=u['digits']; c=u['canon']
    if len(d)>=3:
        if u['x']: u['flags'].add('D')
        v=key.get(c) or key.get(d)
        return 'CODE',('{%s=%s}'%(d,v) if v else '{%s}'%d)+u['sup']
    if c in key:
        v=key[c]; 
        if u['x']: v='h'+v
        return ('WORD' if v.isupper() else 'SYL'), v+u['acc']+u['sup']
    return 'UNK','{%s}'%c+u['acc']+u['sup']
def mark(cls,flags):
    if cls=='X': return 'X'
    if cls=='ILL': return 'N'
    if cls in('CODE','UNK') or flags&{'D','C','ALT'}: return 'E'
    return 'S'
def run(keyp,txp):
    key=loadkey(keyp); lines=[]
    for l in open(txp,encoding='utf-8'):
        m=LINE.match(l.rstrip('\n'))
        if not m: continue
        lid,body=m.groups(); items=[]; i=0
        for kind,o in parse_body(body):
            if kind=='clear': items.append(('clear',o)); continue
            i+=1; cls,val=classify(o,key); o.update(cls=cls,val=val,idx=i,line=lid,mark=mark(cls,o['flags']))
            items.append(('unit',o))
        lines.append((lid,items))
    return lines
def literal(items):
    return ' '.join('«%s»'%o if k=='clear' else o['val'] for k,o in items)
if __name__=='__main__':
    lines=run(sys.argv[1],sys.argv[2]); out=open(sys.argv[3],'w',encoding='utf-8') if len(sys.argv)>3 else None
    if out: out.write('line\tidx\traw\tcanon\tclass\tvalue\tflags\tmark\n')
    for lid,items in lines:
        print(lid+': '+literal(items))
        if out:
            for k,o in items:
                if k=='unit': out.write('\t'.join([lid,str(o['idx']),o['raw'],o['canon'] or '',o['cls'],o['val'],''.join(sorted(o['flags'])),o['mark']])+'\n')
