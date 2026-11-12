"""Mechanical decoding of the open-code telegram GV c 1946.03.09/2.

Reads the text strips (L01..) of the transcription, replaces every word that is a code word of the key with
{CODE=meaning}, turns the telegraph word PT into '.', and marks words that the recipient boxed on the form
(VIVILA) as an unidentified code word |WORD|. Everything else is copied as printed.

    python scripts/decrypt.py [key_frozen.tsv] [transcription] > decryption_goulart1946.txt
"""
import sys, pathlib, unicodedata

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).resolve().parent.parent
KEY = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'key_frozen.tsv'
TR = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / 'transcription_goulart1946.txt'
# words boxed in ink on the form, i.e. marked by the recipient as code; not on the key -> unidentified
BOXED = {'VIVILA'}


def norm(w):
    return ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn').upper()


def load_key(path):
    key = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#') or line.startswith('code\t'):
            continue
        code, meaning = line.split('\t')[:2]
        key[norm(code)] = meaning
    return key


def text_lines(path):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.startswith('L') and line[1:3].isdigit():
            lab, rest = line.split(' ', 1)
            yield lab, rest.split()


def decode(words, key):
    out = []
    for w in words:
        if w == 'PT':
            out.append('.')
        elif w == '=':
            out.append('=')
        elif norm(w) in key:
            out.append('{%s=%s}' % (w, key[norm(w)]))
        elif w in BOXED:
            out.append('|%s|' % w)
        else:
            out.append(w)
    return out


def main():
    key = load_key(KEY)
    print('# decryption of GV c 1946.03.09/2 with %s (mechanical, scripts/decrypt.py)' % KEY.name)
    print('# {CODE=meaning}: code word found in the key; |WORD|: boxed on the form, not in the key (unidentified)')
    hits = 0
    for lab, words in text_lines(TR):
        d = decode(words, key)
        hits += sum(1 for x in d if x.startswith('{'))
        print(lab, ' '.join(d))
    print('# code words found in the key: %d' % hits)


if __name__ == '__main__':
    main()
