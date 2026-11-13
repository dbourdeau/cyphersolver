"""decode.py KEY TX : decode every cipher word of a frozen transcription with a frozen key, once.
Standard library only. Cipher letters are lower-cased before lookup (reader 2 wrote capital W, S, O for the
same glyphs); a letter not in the key file decodes as '?' (a hole). '|' (clear text, sign or blot) is kept.
Output: a header with both md5s, then one line per transcription line: cipher (lower-cased)=plain for each word."""
import sys, hashlib
def load_key(kf):
    k = {}
    for l in open(kf, encoding='utf-8'):
        if l.startswith('#'): continue
        for p in l.split():
            a, b = p.split('='); k[a] = b
    return k
def md5(f): return hashlib.md5(open(f, 'rb').read()).hexdigest()
def lines(tf):
    return [l.split() for l in open(tf, encoding='utf-8') if not l.startswith('#') and l.strip()]
def dec_word(w, k): return ''.join(k.get(c, '?') for c in w.lower())
def decode(kf, tf):
    k = load_key(kf)
    out = [f'# key {kf.split("/")[-1]} md5 {md5(kf)} ; transcription {tf.split("/")[-1]} md5 {md5(tf)} ; one decode, no edits']
    for ws in lines(tf):
        out.append(' '.join(w if w == '|' else w.lower() + '=' + dec_word(w, k) for w in ws))
    return '\n'.join(out) + '\n'
if __name__ == '__main__':
    sys.stdout.write(decode(sys.argv[1], sys.argv[2]))
