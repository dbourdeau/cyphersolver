# Cipher-letter table of key NA 1.10.29 inv. 1209, scans 3 & 5 ("Dit dient om te ontcijfferen"), checked against
# the encipher tables scans 4 & 6. 2..98 -> letter; vowel-substitute letters -> vowel.
NUM = dict(zip(range(2,99), (
 "a u o i e i e u o a d f m s y b i e a u o e i h "   # 2-25
 "q x r l g t n w k e z p u a i o m t d z u a h r "   # 26-49
 "q w c o s n a u y f e o i g l p x k b s x b h q "   # 50-73
 "u a y n o k z i l r e f w t m c d p g a o u i e c" # 74-98
).split()))
# 'w' at 33,51,86 = w ; 'i' = i/j ; 'u' = u/v
VOWEL_LETTER = {'m':'a','q':'a','t':'a','x':'a','z':'a',
                'a':'e','k':'e','o':'e','r':'e','w':'e',
                'b':'i','d':'i','f':'i','g':'i','n':'i',
                'e':'o','s':'o','v':'o','y':'o','&':'o',
                'c':'u','h':'u','i':'u','l':'u','p':'u'}
assert len(NUM)==97
if __name__=='__main__':
    from collections import defaultdict
    inv=defaultdict(list)
    for k,v in NUM.items(): inv[v].append(k)
    for l in sorted(inv): print(l, inv[l])
