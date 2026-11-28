"""Decrypt transcription.txt with key.tsv, line by line, and write decryption.txt (standard library only).
usage: python3 -I targets/vind1647/decrypt.py [--check]   (--check: compare with the filed decryption.txt, write nothing)"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent

def key():
    k = {}
    for line in open(HERE / 'key.tsv', encoding='utf-8'):
        if line.startswith('sign') or not line.strip(): continue
        s, p = line.rstrip('\n').split('\t')[:2]; k[s] = p
    return k

def lines(path):
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        body = line.split('#')[0]
        num, rest = body.split(None, 1)
        yield num, rest.split()

def main():
    k = key(); out = ['# vind1647: transcription.txt decrypted with key.tsv by decrypt.py (letters as the key gives them; = marks a word broken at line end)']
    for num, ws in lines(HERE / 'transcription.txt'):
        out.append('%s %s' % (num, ' '.join(''.join(k[c] for c in w.rstrip('=')) + ('=' if w.endswith('=') else '') for w in ws)))
    text = '\n'.join(out) + '\n'
    if '--check' in sys.argv:
        same = (HERE / 'decryption.txt').read_text(encoding='utf-8') == text
        print('decryption.txt', 'matches' if same else 'DIFFERS'); sys.exit(0 if same else 1)
    with open(HERE / 'decryption.txt', 'w', encoding='utf-8', newline='\n') as f: f.write(text)
    print(text, end='')

if __name__ == '__main__':
    main()
