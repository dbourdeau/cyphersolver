"""Mechanical decryption of a letter-substitution telegram. Standard library only.

    python scripts/decrypt.py <transcription.txt> [key.tsv]

Transcription lines: label<TAB>tokens. A token =word= is clear text and a bare = is the telegraph sign; in the telegram and is copied as is.
Any other token is a cipher group; each letter is replaced by its key value. A key value a|b means the one
cipher letter stands for two plain letters in this key; it prints as (a|b). A letter missing from the key prints [x?].
Output: label<TAB>decrypted tokens, separated as the groups are on the page.
"""
import pathlib, sys
sys.stdout.reconfigure(encoding='utf-8', newline='\n')
ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_key(path):
    k = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        c, v = line.rstrip('\n').split('\t')[:2]
        k[c] = v
    return k

def dec_token(tok, key):
    if set(tok) == {'='}:
        return '='
    if tok.startswith('=') and tok.endswith('=') and len(tok) > 1:
        return tok.strip('=')
    out = []
    for ch in tok:
        v = key.get(ch)
        out.append(f'[{ch}?]' if v is None else (f'({v})' if '|' in v else v))
    return ''.join(out)

def decrypt_line(text, key):
    return ' '.join(dec_token(t, key) for t in text.split())

def main():
    key = load_key(sys.argv[2] if len(sys.argv) > 2 else ROOT / 'key.tsv')
    for line in open(sys.argv[1], encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        lab, t = line.rstrip('\n').split('\t')[:2]
        print(f'{lab}\t{decrypt_line(t, key)}')

if __name__ == '__main__':
    main()
