"""Decrypt the transcription of catalogue 2533 (Johan van Ewsum, Groninger Archieven 696 inv. 595) with a key.
Standard library only.

    python decrypt.py <transcription.txt> [key.tsv]   -> prints 'Lnn: decryption' / 'Rnn: decryption' per line

Transcription rules (SIGN_CONVENTIONS.md): one character per cipher sign, words separated by spaces.
'//' at the start of a line is the writer's carry-over mark (dropped); '/' at the end is printed '='.
'?' = illegible sign (printed '?'). '[del:...]' = a group struck out by the writer (printed '<struck>').
'[sup:...]' = a group written above the line (decrypted like any other word). ':' ',' '-' are copied.
The null sign (value empty in the key) is dropped; the number dropped is printed with --nulls.
"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
PUNCT = set(':,-')


def load_key(path):
    key = {}
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#') or line.startswith('token\t'):
            continue
        parts = line.rstrip('\n').split('\t')
        key[parts[0]] = parts[1] if len(parts) > 1 else ''
    return key


def decrypt_word(w, key, stats):
    out = ''
    for ch in w:
        if ch == '?':
            out += '?'
        elif ch in PUNCT:
            out += ch
        elif ch in key:
            if key[ch] == '':
                stats['nulls'] += 1
            out += key[ch]
        else:
            out += '[?' + ch + ']'
    return out


def decrypt_line(body, key, stats):
    body = body.strip()
    if body.startswith('//'):
        body = body[2:]
    cont = body.endswith('/')
    if cont:
        body = body[:-1]
    words = []
    for tok in re.findall(r'\[[^\]]*\]|\S+', body):
        if tok.startswith('[del:'):
            words.append('<struck>')
        elif tok.startswith('[sup:'):
            words.append(decrypt_word(tok[5:-1], key, stats))
        else:
            words.append(decrypt_word(tok, key, stats))
    s = ' '.join(words)
    return s + ('=' if cont else '')


def decrypt_file(tpath, kpath):
    key = load_key(kpath)
    stats = {'nulls': 0}
    lines = []
    for line in open(tpath, encoding='utf-8'):
        m = re.match(r'([LR]\d+)\s+(.*)$', line.rstrip('\n'))
        if m:
            lines.append(f'{m.group(1)}: {decrypt_line(m.group(2), key, stats)}')
    return lines, stats


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    t = args[0] if args else str(ROOT / 'transcription_ewsum.txt')
    k = args[1] if len(args) > 1 else str(ROOT / 'key_frozen.tsv')
    lines, stats = decrypt_file(t, k)
    print('\n'.join(lines))
    if '--nulls' in sys.argv:
        print(f'# null signs dropped: {stats["nulls"]}', file=sys.stderr)
