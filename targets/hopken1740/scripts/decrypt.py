"""Mechanical decryption: python decrypt.py <key.tsv> <transcription.txt> [out]
Each group -> its key value; unknown -> [group]; trailing ' (stroke = elision) -> value + "'"; ? kept on the group.
Clear text in [clear: ...] is copied as {clear text}."""
import sys, re
def load_key(p):
    k = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        if len(f) > 4 and f[4] == 'unresolved': continue
        k[f[0]] = f[1]
    return k
def tokens(line):
    out = []
    for m in re.finditer(r"\[clear: ([^\]]*)\]|(\d{4})(\?)?(')?|([.,;:])", line):
        if m.group(1) is not None: out.append(('clear', m.group(1)))
        elif m.group(2): out.append(('g', m.group(2), bool(m.group(3)), bool(m.group(4))))
        else: out.append(('p', m.group(5)))
    return out
def decrypt_line(key, rest):
    o = []
    for t in tokens(rest):
        if t[0] == 'clear': o.append('{' + t[1] + '}')
        elif t[0] == 'p': o.append(t[1])
        else:
            v = key.get(t[1], '[%s]' % t[1]); o.append(v + ("'" if t[3] else ''))
    return ' '.join(o)
if __name__ == '__main__':
    key = load_key(sys.argv[1]); res = []
    for l in open(sys.argv[2], encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lab, rest = l.split(' ', 1); res.append(lab + ' ' + decrypt_line(key, rest.strip()))
    s = '\n'.join(res) + '\n'
    if len(sys.argv) > 3: open(sys.argv[3], 'w', encoding='utf-8').write('# mechanical decryption, key %s\n' % sys.argv[1] + s)
    print(s)
