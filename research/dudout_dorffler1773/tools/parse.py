import re, unicodedata
def norm(s):
    s=s.lower().replace('ä','a').replace('ö','o').replace('ü','u').replace('ß','ss')
    s=''.join(ch for ch in unicodedata.normalize('NFD',s) if not unicodedata.combining(ch))
    s=re.sub('[^a-z]','',s)
    return s.replace('j','i').replace('y','i').replace('v','u')
def load(path):
    blocks=[];cur=None
    for line in open(path,encoding='utf-8'):
        line=line.rstrip('\n')
        if not line or line.startswith('#'): continue
        if line.startswith('@'):
            cur={'id':line[1:].split()[0],'C':[],'G':'','lines':[]}; blocks.append(cur); continue
        tag,rest=line[0],line[2:]
        if tag=='C':
            toks=rest.split(); cur['C']+=toks; cur['lines'].append(('C',toks))
        elif tag=='G':
            cur['G']+=norm(rest); cur['lines'].append(('G',rest))
        elif tag=='X': cur['lines'].append(('X',rest))
    return blocks
