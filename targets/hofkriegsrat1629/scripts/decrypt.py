"""Mechanical decryption: transcription tokens + key -> letters. Usage: python -I decrypt.py <transcription> <key.tsv>"""
import sys, re
def load_key(p):
    k = {}
    for ln in open(p, encoding='utf8'):
        if ln.startswith('#') or not ln.strip(): continue
        s, v = ln.rstrip('\n').split('\t')[:2]
        k[s] = '' if v == '-' else v
    return k
def dec_word(tokens, k):
    out = ''
    for t in tokens:
        if t in ',.;': out += t; continue
        m = re.fullmatch(r'\[(\w+)\]', t)
        if m:  # small interlinear insertion, decrypt each digit-sign
            out += ''.join(k.get(ch, '?') for ch in m.group(1)); continue
        out += k.get(t, '[' + t + ']')
    return out
def decrypt_lines(tp, kp):
    k = load_key(kp); res = []
    for ln in open(tp, encoding='utf8'):
        if not re.match(r'L\d\d:', ln): continue
        lab, body = ln.split(':', 1)
        words = [w.split() for w in body.split(' / ')]
        res.append((lab, [dec_word(w, k) for w in words]))
    return res
if __name__ == '__main__':
    for lab, ws in decrypt_lines(sys.argv[1], sys.argv[2]):
        print(lab + ': ' + ' '.join(ws))
