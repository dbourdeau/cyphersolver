"""Write read/<doc>_decryption.txt: the key (key_bouille.tsv, first value) applied to each transcription;
context readings from tentative.tsv in {braces}, groups with no value as [n]. Syllables are separated by spaces."""
import os, re
H = os.path.dirname(os.path.abspath(__file__))
key, tent = {}, {}
for l in open(os.path.join(H, 'key_bouille.tsv'), encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if len(p) > 1 and p[0].isdigit(): key[p[0]] = p[1].split('/')[0]
for l in open(os.path.join(H, 'tentative.tsv'), encoding='utf8'):
    p = l.rstrip('\n').split('\t')
    if l[:1].isdigit() and len(p) > 1: tent[p[0]] = p[1]
DOCS = {'f88': 'groups1778_f88.txt', 'f101_letter': 'groups1778_f101.txt', 'f19': 'cipher_f19_groups.txt',
        'f70': 'cipher_f70_groups.txt', 'f114': 'cipher_f114_groups.txt'}
def dec(g):
    g = g.rstrip('?')
    if g == '|': return ''
    if g in key: return key[g]
    if g in tent: return '{' + tent[g] + '}'
    return '[' + g + ']'
os.makedirs(os.path.join(H, 'read'), exist_ok=True)
for name, fn in DOCS.items():
    n = v = 0; out = []
    for i, l in enumerate(open(os.path.join(H, fn), encoding='utf8')):
        l = l.rstrip('\n')
        if l[:1] == '#' or not l.strip(): continue
        if ':' in l: lab, body = l.split(':', 1)
        else: lab, body = 'L%d' % i, l
        toks = body.split()
        n += sum(1 for t in toks if t != '|'); v += sum(1 for t in toks if t != '|' and t.rstrip('?') in key)
        out.append('%s: %s' % (lab.strip(), ' '.join(x for x in (dec(t) for t in toks) if x)))
    open(os.path.join(H, 'read', name + '_decryption.txt'), 'w', encoding='utf8').write(
        '# %s: %d groups, %d valued from interlinear pairs (%.1f%%)\n' % (fn, n, v, 100 * v / n) + '\n'.join(out) + '\n')
    print(name, n, v, '%.1f%%' % (100 * v / n))
