"""Decrypt a 2358 transcription with key.tsv. Standard library only.

    python decrypt.py <transcription.txt> [key.tsv]  -> 'Lnn<TAB>word word ...'

Transcription lines: 'Lnn<TAB>' + space-separated cipher words; one token per character, except '[?]' (a sign not
made out, value '?'). A '?' directly after a token marks a doubtful shape and is dropped. Letters not in the key stand
for themselves (consonants are written plain). Nulls give nothing; a word of nulls only prints as '-'.
Class tokens S (s or i) and G (g, q, u or v) print as S and G and are resolved in the reading.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding='utf-8')


def load_key(path):
    key = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.rstrip('\n').split('\t')
        key[parts[0]] = parts[1] if len(parts) > 1 else ''
    return key


def tokens(word):
    out, i = [], 0
    while i < len(word):
        if word.startswith('[?]', i):
            out.append('?'); i += 3; continue
        c = word[i]; i += 1
        if c == '?':
            continue  # doubt mark on the previous token
        out.append(c)
    return out


def dec_word(word, key):
    v = ''.join(key.get(t, t) for t in tokens(word))
    return v if v else '-'


def main():
    tr = sys.argv[1]
    key = load_key(sys.argv[2] if len(sys.argv) > 2 else ROOT / 'key.tsv')
    for line in open(tr, encoding='utf-8'):
        m = re.match(r'^(L\d\d)\t(.*)$', line.rstrip('\n'))
        if m:
            print(m.group(1) + '\t' + ' '.join(dec_word(w, key) for w in m.group(2).split()))


if __name__ == '__main__':
    main()
