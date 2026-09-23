"""Syllabic control: the plaintext of pt_control.txt re-enciphered with CV syllables as two-digit figures (each
syllable one number, split into its two figures as the copy writes them) and single letters as homophonic signs.
Writes ct_control_syl.txt."""
import random
random.seed(7)
SYL = [c + v for c in 'bcdfglmnpqrstu' for v in 'aeiou' if not (c == 'q' and v != 'u')]
nums = random.sample(range(10, 100), len(SYL)); code = dict(zip(SYL, nums))
homs = {'e': 5, 'a': 3, 'i': 3, 'n': 3, 's': 3, 't': 3, 'r': 3, 'u': 3, 'o': 3, 'l': 2, 'd': 2, 'c': 2, 'm': 2,
        'p': 2, 'q': 1, 'b': 1, 'f': 1, 'g': 1, 'h': 1, 'x': 1, 'y': 1, 'z': 1}
signs = [f's{i}' for i in range(60)]; random.shuffle(signs); key = {}; k = 0
for c, h in homs.items(): key[c] = signs[k:k + h]; k += h
out = []
for p in open('pt_control.txt', encoding='utf8').read().split():
    toks = []; i = 0
    while i < len(p):
        if p[i:i + 2] in code and random.random() < 0.7:
            n = code[p[i:i + 2]]; toks += [str(n // 10), str(n % 10)]; i += 2
        else:
            toks.append(random.choice(key[p[i]])); i += 1
    out.append(' '.join(toks))
open('ct_control_syl.txt', 'w', encoding='utf8').write('# syllabic control\n' + '\n'.join(out) + '\n')
print(sum(len(o.split()) for o in out), 'tokens')
