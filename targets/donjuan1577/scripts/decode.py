"""Mechanical decryption of transcription_1410_135.txt with key_frozen.json (the 1577 Genoa-embassy syllabary, hand of Don John's cipher copies).
Token = number[mark][finals]: mark letters a e i o q give the vowel (q = the long-s mark, o); finals ^ n, _ s, v r, ' l; sup2 = small 2 above (no value);
@word = letter group (nomenclator); n† = code with a cross; '/' = slash in the text. A bare number listed under 'bare' has its own value (6 alone = i).
Usage: python3 scripts/decode.py key_frozen.json transcription_1410_135.txt"""
import json, re, sys
def dec_unit(u, K):
    if u in ('|', '/'): return ' '
    if re.fullmatch(r'\d+', u) and u in K.get('bare', {}): return K['bare'][u]
    if u == 'y': return 'y'
    if u.startswith('@'): return K.get('words', {}).get(u[1:], '<' + u[1:] + '>')
    if re.fullmatch(r'[a-zñ]+', u): return u
    m = re.fullmatch(r"(\d+)(sup2)?([aeioq]?)(sup2)?([\^_'v]?)(sup2)?(†?)", u)
    if not m: return '?'
    n, s2a, mk, s2b, fin, s2c, cross = m.groups()
    if cross: return K.get('codes', {}).get(n + 'x' + mk, '?')
    if n in K.get('numcodes', {}) and not mk and not fin: return K['numcodes'][n]
    if n in K['cons']: out = K['cons'][n] + (K['marks2'].get(mk, '?') if mk else '')
    elif n in K['vowels'] and not mk: out = K['vowels'][n]
    else: return '?'
    if s2a or s2b or s2c: out += '?'
    return out + (K['sup'].get(fin, '') if fin else '')
def units(path):
    return [l.split(':', 1)[1].split() for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#') and ':' in l]
def decode(U, K): return ' '.join(''.join(dec_unit(u, K) for u in line) for line in U)
if __name__ == '__main__':
    K = json.load(open(sys.argv[1], encoding='utf-8'))
    for l in open(sys.argv[2], encoding='utf-8'):
        if l.strip() and not l.startswith('#') and ':' in l:
            n, L = l.split(':', 1); print(n + ': ' + ''.join(dec_unit(u, K) for u in L.split()))
