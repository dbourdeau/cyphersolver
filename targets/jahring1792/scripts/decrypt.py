"""Mechanical decryption of the runs with key.tsv (Porta table, keyword constantinopolitanus).
python -I scripts/decrypt.py [--frozen]   writes decryption_119.txt and decryption_120.txt (with --frozen: prints only)."""
import json, re, string, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent.parent
A = string.ascii_lowercase

def load_key(frozen=False):
    f = HERE / ('key_frozen.tsv' if frozen else 'key.tsv')
    kw, signs = None, {}
    for line in open(f, encoding='utf8'):
        if line.startswith('#') or not line.strip(): continue
        p = line.rstrip('\n').split('\t')
        if p[0] == 'keyword': kw = p[1]
        if p[0] == 'sign': signs[p[1]] = p[2]
    return kw, signs

def porta(c, k):
    k = A.index(k) // 2; c = A.index(c)
    return A[13 + (c + k) % 13] if c < 13 else A[(c - 13 - k) % 13]

def cipher_letters(signs, sv):
    s = re.sub(r'\[[^\]]*\]', '', signs)
    out = []
    for ch in s:
        if ch in A: out.append(ch)
        elif ch in sv: out.append(sv[ch])
        # an unmapped sign (frozen key) is dropped
    return ''.join(out)

def decrypt(signs, kw, sv):
    ct = cipher_letters(signs, sv)
    return ''.join(porta(c, kw[i % len(kw)]) for i, c in enumerate(ct))

if __name__ == '__main__':
    frozen = '--frozen' in sys.argv
    kw, sv = load_key(frozen)
    rows = json.load(open(HERE / 'runs.json', encoding='utf8'))
    docs = {}
    for doc, run, signs, *_ in rows:
        docs.setdefault(doc, []).append(f'{run}\t{decrypt(signs, kw, sv)}')
    for doc, lines in docs.items():
        txt = '# mechanical decryption, Porta table, keyword constantinopolitanus, key restarted per run (scripts/decrypt.py)\n' + '\n'.join(lines) + '\n'
        if frozen: print(txt)
        else: open(HERE / f'decryption_{doc}.txt', 'w', encoding='utf8').write(txt)
