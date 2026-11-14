"""greenhow1861: independent check (Brice Dudout, Claude Opus 5.5, 14 Nov 2026).
Reads only transcription_side1.txt (its label legend, which gives each shape label its key letter as in
key_1864.md), decryption_side1.txt and ciphertext_side2.txt. Run from targets/greenhow1861/. Standard library."""
import re

src = open('transcription_side1.txt', encoding='utf-8').read().splitlines()
legend = ' '.join(l[1:] for l in src if l.startswith('#'))
key = dict((lab, let) for lab, let in re.findall(r'\b([a-z0-9]{2,3}) = [^,()]*?\(([A-Z])[,)]', legend))
print('1. legend: %d labels ->' % len(key), ' '.join(f'{k}={v}' for k, v in sorted(key.items(), key=lambda x: x[1])))

lines = [l[3:] for l in src if l[:2].isdigit() and l[2:3] == ' ']
mine = []
for l in lines:
    out = []
    for t in l.replace('+', '').split():
        if t == '|': out.append('|')
        elif t == '~': out.append('_')
        elif t.startswith('='): out.append('(%s)' % t[1:])
        else:
            lab, unc = t.rstrip('?'), t.endswith('?')
            v = key[lab]
            out.append(v.lower() if unc else v)
    mine.append(' '.join(out))

# published decode: decryption_side1.txt, column 2 (before "->"), and the decode lines at the foot of the transcription
pub = {}
for l in open('decryption_side1.txt', encoding='utf-8'):
    m = re.match(r'(\d\d)  (.*?)\s+->', l)
    if m: pub[m.group(1)] = m.group(2)
def squash(s):  # letters, losses and clear words only, word gaps ignored
    s = re.sub(r'\(([^)]*)\)', lambda m: '(' + m.group(1).lower() + ')', s)
    return re.sub(r'[\s|+]', '', s)
print('2. side 1, key applied to the labels, against decryption_side1.txt')
ok = 0
for i, m in enumerate(mine, 1):
    p = pub.get('%02d' % i, '')
    same = squash(m) == squash(p)
    ok += same
    if not same: print('   line %02d differs: mine %s | published %s' % (i, m, p))
nsig = sum(1 for l in lines for t in l.split() if t.rstrip('?+') in key)
print(f'   {ok}/{len(lines)} lines agree; {nsig} signs')

print('3. side 2, line 2: ciphertext_side2.txt (GANIZING before 14 Nov 2026) and the re-read on the image')
pub2 = [l.split() for l in open('ciphertext_side2.txt', encoding='utf-8') if not l.startswith('#')]
print('   file      :', ' '.join(pub2[1]))
reread = 'I G A N I S I N G'.split()  # 4ll = one I-sign (as the I of MORNING, side 1 l. 16); torn box = S
print('   re-read   :', ' '.join(reread), '-> [or]ganising')
print('   signs on side 2: file %d, re-read %d; distinct file %d, re-read %d' % (
    sum(map(len, pub2)), len(pub2[0]) + len(reread), len(set(sum(pub2, []))), len(set(pub2[0] + reread))))
