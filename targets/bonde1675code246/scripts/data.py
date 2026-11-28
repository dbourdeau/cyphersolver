import re
D='.'  # the work folder (local path removed)
def clean(g):
    g=g.split('|')[0].strip()
    g=re.sub(r'\[\?\]','',g)
    if '/' in g or not re.fullmatch(r'\d+',g): return None
    return g
def load(p,cols=2):
    rows=[]
    for l in open(p,encoding='utf-8'):
        f=l.rstrip('\n').split('\t')
        if len(f)<2: continue
        gs=[clean(x) for x in f[1].split('.') if x.strip()]
        rows.append((f[0],[g for g in gs if g],f[2] if len(f)>2 else '', f[3] if len(f)>3 else ''))
    return rows
def learning():
    L=load(D+'/transcriptions/113R_L01-L18_pass1.tsv'); G=load(D+'/transcriptions/114L_G01-G32_pass1.tsv')
    return L,G
