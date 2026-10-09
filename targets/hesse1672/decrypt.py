"""Decipher the two letter-cipher passages of HStAM 4 f Dänemark Nr. 125 f. 4r (1672)
with the letter table of HCPortal key 255 (HStAM 4 d Nr. 1234 ff. 13-16, Lincker 1666/1676)."""
import re, sys, os
COLS = {  # plaintext: five homophones, from the key table (image 13)
 'a':[20,30,40,50,60],'b':[22,32,42,52,62],'c':[24,34,44,54,64],'d':[26,36,46,56,66],
 'e':[28,38,48,58,68],'f':[21,31,41,51,61],'g':[23,33,43,53,63],'h':[25,35,45,55,65],
 'i':[27,37,47,57,67],'k':[29,39,49,59,69],'l':[70,80,90,100,110],'m':[72,82,92,102,112],
 'n':[74,84,94,104,114],'o':[76,86,96,106,116],'p':[78,88,98,108,118],'q':[71,81,91,101,111],
 'r':[73,83,93,103,113],'s':[75,85,95,105,115],'t':[77,87,97,107,117],'u':[79,89,99,109,119],
 'w':[120,130,140,150,160],'x':[122,132,142,152,162],'y':[124,134,144,154,164],'z':[126,136,146,156,166]}
NUM = {n: p for p, ns in COLS.items() for n in ns}
DOUBLE = dict(zip('CC DD EE FF GG HH II KK LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ AA BB'.split(),
                  'a b c d e f g h i k l m n o p q r s t u w x y z'.split()))
SYL = {'[st]': 'st', '[tt]': 'tt'}
NULLS = set(range(1, 20)) | {121,131,141,151,161,171,123,125,127,129,133,135,137,139,143,145,147,149,153,155,157,159,163,165,167,169,173,175,177,178,179}
CODES = {'634': 'Holstein', '768': 'Schweden (Sueco)'}

def dec(tok):
    if tok in SYL: return SYL[tok]
    if tok in DOUBLE: return DOUBLE[tok]
    m = re.fullmatch(r'\[(\d+)\]', tok)
    if m: return '<' + CODES.get(m.group(1), m.group(1)) + '>'
    if tok.isdigit():
        n = int(tok)
        if n in NULLS: return '·'
        return NUM.get(n, '?')
    return '?'

if __name__ == '__main__':
    for line in open(os.path.join(os.path.dirname(__file__), 'ct.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        toks = line.split()
        print(' '.join(f'{t}={dec(t)}' for t in toks))
        print('  ->', ''.join(dec(t) for t in toks))
