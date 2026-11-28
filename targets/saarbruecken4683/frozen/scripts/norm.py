import re, unicodedata
def norm(s):
    s=s.lower().replace('ß','ss')
    s=s.replace('ä','a').replace('ö','o').replace('ü','u').replace('ÿ','y')
    s=''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn')
    s=re.sub(r'[^a-z]','',s)
    return s.replace('v','u').replace('j','i').replace('y','i')
