"""Turn the cipher part of Kervyn IX no. 3359 (local Internet Archive OCR file, read by path, not copied into
our files) into plaintext units: single letters, {word} for words Kervyn prints in brackets, {GAP} for his dots.
Normalisation: lower case, accents stripped, v->u, j->i, w->u, n-tilde->n, c-cedilla->c; other characters dropped."""
import re, unicodedata
import os
# Internet Archive OCR of Kervyn vol. IX: https://archive.org/download/relationspolitiq09nethuoft/relationspolitiq09nethuoft_djvu.txt
# (SHA-256 fc0a16f0fd7011eef8b45d777d8444a0956e795f132e8e0730960d38af7c74e3); not in git. Run scripts/fetch_kervyn.py first.
KV = os.environ.get('KERVYN9', 'kervyn9_djvu.txt')
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('v', 'u').replace('j', 'i').replace('w', 'u')
def units():
    L = open(KV, encoding='utf-8').read().split('\n')[10764:10849]
    t = ' '.join(L); a = t.index('Es  increyble'); b = t.index('Nuestro-Sc')
    s = re.sub(r'DES\s+PAYS-BAS\s+ET\s+DE\s+L.ANGLETERRE\.\s+201', ' ', t[a:b])
    s = re.sub(r"\s\S*m\s+DES", ' DES', s)
    s = s.replace('•', ' ').replace("'", ' ')
    # the OCR lost the rows of dots after 'fue preso' and 'puesto en' (seen on the printed page, p. 201)
    s = s.replace('fue  preso El', 'fue  preso ..... El').replace('puesto  en y', 'puesto  en ..... y')
    out = []
    for m in re.finditer(r'\[([^\]]*)\]|(\.\s*){3,}|\.\s*\.\.\s*\.|([A-Za-zÀ-ÿ])', s):
        if m.group(1) is not None: out.append('{' + re.sub(r'[^a-z]', '', norm(m.group(1))) + '}')
        elif m.group(3): 
            c = re.sub(r'[^a-z]', '', norm(m.group(3)))
            if c: out.append(c)
        else: out.append('{GAP}')
    return out
if __name__ == '__main__':
    u = units(); print(len(u), sum(len(x) == 1 for x in u), [x for x in u if len(x) > 1])
    print(''.join(x if len(x) == 1 else ' ' + x + ' ' for x in u)[:400])
