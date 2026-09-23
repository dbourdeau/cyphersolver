"""Decrypt the transcription line by line with key.txt and write decrypt_lines.txt (cipher line / plaintext line).

key.txt: one "sign<TAB>letter" per line; multi-sign units (zo, pp, io, ...) are listed like single signs and are
matched longest-first. A letter value of "-" is a null. "=W<TAB>word" is a whole-word code (printed upper-case).
"""
import os, re, glob, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load_key():
    key = {}
    for line in open(os.path.join(HERE, 'key.txt'), encoding='utf8'):
        line = line.split('#')[0].rstrip('\n')
        if '\t' in line:
            s, v = line.split('\t')[:2]
            key[s.strip()] = v.strip()
    return key


def dec_word(w, key, units):
    if '=' + w in key:                       # whole-word code
        return key['=' + w].upper()
    out, i = [], 0
    while i < len(w):
        for u in units:
            if w.startswith(u, i):
                v = key[u]
                out.append('' if v == '-' else v)
                i += len(u)
                break
        else:
            out.append('?' if w[i] != '?' else '?')
            i += 1
    return ''.join(out)


def lines():
    for fn in sorted(glob.glob(os.path.join(HERE, 'transcription', '1*.txt'))):
        fol = os.path.basename(fn)[:-4]
        n = 0
        for line in open(fn, encoding='utf8'):
            line = line.rstrip('\n')
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            n += 1
            yield fol, n, line.split('#')[0].strip()


def main():
    key = load_key()
    units = sorted((k for k in key if not k.startswith('=')), key=len, reverse=True)
    out = []
    for fol, n, line in lines():
        clean = re.sub(r'\[[^\]]*\]', ' ', line).replace('=', '')
        pt = ' '.join(dec_word(w, key, units) for w in clean.split())
        out.append(f'{fol}.{n:02d}  {line}\n{fol}.{n:02d}  {pt}\n')
    open(os.path.join(HERE, 'decrypt_lines.txt'), 'w', encoding='utf8').write('\n'.join(out))
    print(len(out), 'lines')


if __name__ == '__main__':
    main()
