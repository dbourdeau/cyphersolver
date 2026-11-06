"""Mechanical decryption with key.tsv (or another key). Standard library only.

    python decrypt.py <transcription.txt> [key.tsv]

Transcription lines: 'Lnn<TAB>tokens'. A token is a code number, '.' (word stop written in the cipher),
'|' (clear text between runs), or a number with '?' for a doubtful reading. Clear words in the transcription
are written in angle brackets <...> and are passed through unchanged.
Output: 'Lnn<TAB>' + decrypted letters; unknown codes print as [nn]; '.' prints as a space, '|' as ' | '.
"""
import pathlib, re, sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_key(path=ROOT / 'key.tsv'):
    k = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'):
            continue
        code, val = line.rstrip('\n').split('\t')[:2]
        if val not in ('?',):
            k[code] = val.rstrip('?')
    return k

def dec_tokens(toks, key):
    out = []
    for t in toks:
        if t == '.':
            out.append(' ')
        elif t == '|':
            out.append(' | ')
        elif t.startswith('<'):
            out.append(' ' + t + ' ')
        elif t == '[gutter]':
            out.append('[gutter]')
        else:
            c = t.rstrip('?')
            out.append(key.get(c, f'[{c}]'))
    return re.sub(r' +', ' ', ''.join(out)).strip()

def lines(path):
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^(L\d+)\t(.*)$', line.rstrip('\n'))
        if m:
            yield m.group(1), re.findall(r'<[^>]*>|\S+', m.group(2))

def main():
    key = load_key(sys.argv[2]) if len(sys.argv) > 2 else load_key()
    for lab, toks in lines(sys.argv[1]):
        print(lab + '\t' + dec_tokens(toks, key))

if __name__ == '__main__':
    main()
