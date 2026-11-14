"""dubellay: independent decoder for the 16 June 1529 block (fr. 3078 p. 21).
Brice Dudout (Claude Opus 5.5), 14 Nov 2026. Reads only key_p21.tsv and p21_signs.txt (sign part of each token),
not the '=value' labels, then compares (1) with those labels and (2) with the letters of the published decryption
texts/16jun1529_decryption.md. Usage: python3 verify_dudout_20261114.py <path to targets/dubellay>"""
import sys, os, re, unicodedata
root = sys.argv[1] if len(sys.argv) > 1 else '.'
K = {}
for l in open(os.path.join(root, 'key_p21.tsv'), encoding='utf-8'):
    if l.startswith('sign\t') or not l.strip(): continue
    s, v = l.rstrip('\n').split('\t')[:2]; K[s] = v
WORD = {'madame': 'madame', 'madame marguerite': 'madamemarguerite', 'fault/faict': 'faict', 'vous': 'vous', 'roy': 'roy'}
def val(sign):
    v = K.get(sign)
    if v is None: return None
    if v.startswith('null'): return ''
    if v in WORD: return WORD[v]
    if v.startswith('q ('): return 'q'
    return v
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub('[^a-z]', '', s)
lines = [l.split() for l in open(os.path.join(root, 'p21_signs.txt'), encoding='utf-8') if re.match(r'L\d ', l)]
n = agree = 0; out = []; unk = []
for toks in lines:
    lab = toks[0]
    for t in toks[1:]:
        sign, _, lv = t.rpartition('=') if t.count('=') == 1 or not t.startswith('==') else ('=', '', t[2:])
        if t.startswith('=='): sign, lv = '=', t[2:]
        v = val(sign); n += 1
        if v is None: unk.append((lab, sign, lv)); out.append('?'); continue
        alts = v.split('|')
        lvn = norm(lv)
        if (v == '' and lvn.startswith('null')) or any(norm(a) == lvn for a in alts) or (lv.upper() == lv and norm(lv) == norm(alts[0])): agree += 1
        else: print('label differs:', lab, sign, 'key', v, 'label', lv)
        out.append(alts if v else [''])
print(f'{n} sign tokens; {agree} agree with their label; not in key: {unk}')
dec = open(os.path.join(root, 'texts', '16jun1529_decryption.md'), encoding='utf-8').read()
body = re.search(r'\*Monsr, (.*?)\*', dec, re.S).group(1)
D = norm(body)
# u|v and b|f are one sign each in this key: fold v->u and f->b in both streams before comparing
fold = lambda x: x.replace('v', 'u').replace('f', 'b')
D = fold(D); C = fold(norm(''.join(o[0] for o in out if o != '?')))
# alignment of the decoded letter stream with the decryption's letters (difflib)
import difflib
sm = difflib.SequenceMatcher(None, C, D, autojunk=False)
m = sum(b.size for b in sm.get_matching_blocks())
print(f'decoded letters {len(C)}, decryption letters {len(D)}, matching {m} ({m/len(C):.3f} of decoded)')
for op, a0, a1, b0, b1 in sm.get_opcodes():
    if op != 'equal': print(f'   {op:8} cipher "{C[a0:a1]}"  decryption "{D[b0:b1]}"  (decryption context "{D[max(0,b0-12):b1+12]}")')
