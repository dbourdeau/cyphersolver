"""Mechanical decryption for 2393 (Pandolfini 1515), standard library only.
    python scripts/decrypt.py <transcription.txt> [key.tsv]
Transcription lines: label: tokens (base[^superscript], .n. codes, '.', 'd', '{INS}' marks).
Rules (as Dudout's decode_v6): a whole token in the token table wins; else base value + one vowel per superscript
digit (n, m kept as letters); unknown base or digit -> '?'; .n. -> code value or [n]; V^0, the block-end formula (END = the closing marks such as 'Θ . d .'), the slash and {INS} -> nothing.
Context rules of v6: O before bare r = c; 2^5 before 'y 3..' = ba; .4. = maesta after a decode ending in 'a' or after
S^4 6 8(^5), else cristianissimo. Output: label<TAB>one decoded piece per token, joined by '|'."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_key(p):
    K = {'vowel': {}, 'base': {}, 'token': {}, 'code': {}, 'alias': {}, 'null': {}}
    for line in open(p, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        kind, sign, val = line.rstrip('\n').split('\t')[:3]
        K[kind][sign] = val
    return K

def norm(t, K):
    t = t.rstrip('?') or t
    b, sep, e = t.partition('^')
    return K['alias'].get(b, b) + sep + e

def dec(t, K):
    if t in K['null'] or t in ('.', 'END', '{INS}', '/'): return ''
    m = re.fullmatch(r'\.(\w+)\.', t)
    if m: return K['code'].get(m.group(1), '[%s]' % m.group(1))
    if t in K['token']: return K['token'][t]
    b, _, e = t.partition('^')
    if b not in K['base']: return '?'
    out = K['base'][b]
    for ch in e:
        out += K['vowel'].get(ch, ch if ch in 'nm' else '?')
    return out

def decode(toks, K):
    raw = [x.rstrip('?') or x for x in toks]
    N = [norm(x, K) for x in toks]
    outs = []
    for i, t in enumerate(N):
        nx = N[i + 1] if i + 1 < len(N) else ''
        nx2 = N[i + 2] if i + 2 < len(N) else ''
        if t == '.4.':
            prev = re.sub(r'[^a-z]', '', ''.join(outs))
            q = N[max(0, i - 3):i] in (['S^4', '6', '8'], ['S^4', '6', '8^5'])
            d = 'maesta' if (prev.endswith('a') or q) else K['code']['4']
        elif t == 'O' and nx == 'r': d = 'c'
        elif t == '2^5' and nx == 'y' and nx2.startswith('3'): d = 'ba'
        else: d = dec(t, K)
        outs.append(d)
    return outs

def lines(path):
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.lstrip().startswith('#'): continue
        lab, _, rest = line.partition(':')
        yield lab.strip(), rest.split()

def main():
    K = load_key(sys.argv[2] if len(sys.argv) > 2 else ROOT / 'key.tsv')
    for lab, toks in lines(sys.argv[1]):
        print(lab + '\t' + '|'.join(decode(toks, K)))

if __name__ == '__main__':
    main()
