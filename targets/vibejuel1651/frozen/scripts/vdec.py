"""Déchiffre la transcription Vibe/Juel (système établi sur img 78, 11/11) :
mot = ouvreur (fixe le décalage k) + corps ; corps : n = rang(lettre) + k sur l'alphabet de 23
a b c d e f g h i k l m n o p q r s t u x y z ; valeurs 32/33/34 dans le corps = 1/2/3 (+31).
Table des ouvreurs (provisoire, à figer) : 24-29 -> k0 ; 30-34 -> k1 ; 35-39 -> k2 ; 1-3 -> k3."""
import sys, re
A = 'abcdefghiklmnopqrstuxyz'
def kof(o):
    if 24 <= o <= 29: return 0
    if 30 <= o <= 34: return 1
    if 35 <= o <= 39: return 2
    if 1 <= o <= 3: return 3
    return None
def body(n, k):
    if n >= 32 and n <= 34: n -= 31
    i = n - 1 - k
    return A[i] if 0 <= i < 23 else '?%d' % n
def word(nums, k=None):
    o = nums[0]; kk = kof(o) if k is None else k
    if kk is None: return '<%s>' % '.'.join(map(str, nums))
    return ''.join(body(n, kk) for n in nums[1:])
def decode_text(txt):
    out = []; carry = None
    for line in txt.splitlines():
        if line.startswith('#') or not line.strip(): continue
        res = []
        for tok in re.findall(r'\[[^\]]*\]|\S+', line):
            if tok.startswith('['): res.append(tok); continue
            if tok.startswith('C'): res.append('{%s}' % tok[1:]); continue
            hy = tok.endswith('='); t = tok.rstrip('=')
            nums = [int(x) for x in t.split('.') if x]
            if carry is not None:
                nums = carry + nums; carry = None
            if hy: carry = nums; continue
            res.append(word(nums).upper())
        out.append(' '.join(res))
    return '\n'.join(out)
if __name__ == '__main__':
    for f in sys.argv[1:]:
        print('==', f); print(decode_text(open(f).read()))
