import re
def norm(g):
    g=g.lower().replace('j','i').replace('v','u')
    g=re.sub(r'[^a-z]','',g)
    return re.sub(r'qu','q',g)
def load_key(path):
    K={}
    for line in open(path,encoding='utf-8'):
        if line.startswith('#') or line.startswith('group\t') or not line.strip(): continue
        f=line.rstrip('\n').split('\t')
        g,v=f[0],f[1]
        if len(g.split('.'))>1 or (g.isdigit() and len(g)==3): continue   # code words
        K[g]=set(v.split('/'))
    return K
