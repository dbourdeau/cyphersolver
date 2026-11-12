"""decrypt.py <transcription.txt> <system>  -> mechanical decryption to stdout.
system 'juel' : 8-64 table in key_frozen.tsv (nulls dropped, codes >64 kept as [n], open numbers as [?n]).
system 'vibeold' : Peder Vibe's old cipher as published by Brice Dudout (PR #410, targets/vibejuel1651/key.tsv, section G):
   word = opener (24-39) + body; k = -(opener mod 3); body n -> letter of rank (n - k) mod 23 in a..z without j, v, w;
   in the body 32/33/34 stand for 1/2/3. Numbers >= 100 are codes [n].
A doubtful group written "50|56" in the reconciled transcription is decrypted with its first reading."""
import sys, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
def load_key():
    K = {}
    for l in open(os.path.join(HERE, '..', 'key_frozen.tsv'), encoding='utf8'):
        if l.startswith('#') or l.startswith('number'): continue
        f = l.rstrip('\n').split('\t'); K[int(f[0])] = f[1]
    return K
G = 'abcdefghiklmnopqrstuxyz'
def tokens(line):
    line = re.sub(r'\{[^}]*\}', ' | ', line)
    return [t for t in re.split(r'[\s/]+', line) if t]
def juel(line, K):
    out = []
    for t in tokens(line):
        if t == '|' or t.startswith('#'): out.append(' '); continue
        n = int(t.split('|')[0]); v = K.get(n)
        if n > 64: out.append('[%d]' % n)
        elif v == '(null)': out.append('.')
        elif v is None or v == '?': out.append('[?%d]' % n)
        else: out.append(v)
    return ''.join(out)
def vibeold(line):
    out = []; k = None
    for t in tokens(line):
        if t == '|' or t.startswith('#'): out.append(' '); k = None; continue
        n = int(t.split('|')[0])
        if n >= 100: out.append(' [%d] ' % n); k = None; continue
        if 24 <= n <= 39 and not (k is not None and n in (32, 33, 34)):
            k = -(n % 3); out.append(' '); continue
        if k is None: out.append('[?%d]' % n); continue
        b = {32: 1, 33: 2, 34: 3}.get(n, n)
        out.append(G[(b - k - 1) % 23])
    return ''.join(out)
if __name__ == '__main__':
    src, system = sys.argv[1], sys.argv[2]
    K = load_key()
    for l in open(src, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        print(juel(l, K) if system == 'juel' else vibeold(l))
