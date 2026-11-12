import re
MARKV={"'":"a", ",":"e", '"':"a", "^":""}
def load_trans(path):
    lines={}
    for ln in open(path,encoding='utf-8'):
        if ln.startswith('#') or ':' not in ln: continue
        k,v=ln.split(':',1); lines[k.strip()]=v.strip()
    return lines
def words(line):
    out=[]
    for w in line.split('|'):
        t=[x for x in w.split() if x not in ('+','/','//')]
        if t: out.append(t)
    return out
def load_key(path):
    key={}
    for ln in open(path,encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        p=ln.rstrip('\n').split('\t')
        key[p[0]]=p[1] if len(p)>1 else ''
    return key
def dec_tok(t,key):
    if t in key: return key[t]
    m=re.match(r"^(.+?)([',\"^]+)$",t)
    if m and m.group(1) in key:
        return key[m.group(1)]+''.join(MARKV[c] for c in m.group(2))
    return '?'
def dec_line(line,key):
    return ' '.join(''.join(dec_tok(t,key) for t in w) for w in words(line))
