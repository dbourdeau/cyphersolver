"""Apply George Lasry's key for BnF Espagnol 318 no. 95, unchanged, to the two transcriptions of catalogue 2857.

    python decode.py

The key is read from Lasry's own target (../esp318no95/lasry2021/ctts/key.txt) and checked by its sha256; nothing
is copied, changed, added or refitted. Writes decode_blind.txt and decode_working.txt: per manuscript line, the
letters his key gives, with

  ?            a sign with no value: a hole (#) of the transcription, or [N02] / [N03], signs not in his table
  [dal]        a code group of his table (his label in the header: dal is one of his unidentified names)
  [bnm]        a group not in his table

Standard library only; deterministic.
"""
import hashlib, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
KEY = HERE.parent / 'esp318no95' / 'lasry2021' / 'ctts' / 'key.txt'
KEY_SHA = '5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06'


def load_key():
    raw = KEY.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == KEY_SHA, 'Lasry key.txt is not the version these files were made with'
    key = {}
    for line in raw.decode('utf8').splitlines():
        if line.startswith('#') or ' - ' not in line:
            continue
        signs, value = line.rsplit(' - ', 1)
        for s in signs.split('|'):
            key[s] = value
    return key


def value(t, key):
    if t == '#' or re.fullmatch(r'\[N\d\d\]', t):
        return '?'
    if t.startswith('['):
        return f' {t} '
    v = key[t]
    if v == '[null?]':
        return ''
    if len(v) == 1:
        return v.lower()
    if t.startswith('_'):           # a code group of his table
        return f' [{t[1:]}] '
    return f' {v} '            # Lasry's special signs, e.g. [y?] (none occurs in this letter)


def decode(path, key):
    out, labels = [], {}
    for line in path.read_text(encoding='utf8').splitlines():
        m = re.match(r'(L\d):\s*(.*)', line)
        if not m:
            continue
        toks = m.group(2).split()
        for t in toks:
            if t.startswith('_') and len(key[t]) > 1:
                labels[t[1:]] = key[t]
        out.append(f'{m.group(1)}: ' + re.sub(' +', ' ', ''.join(value(t, key) for t in toks)).strip())
    return out, labels


def main():
    key = load_key()
    for label in ('blind', 'working'):
        lines, labels = decode(HERE / f'transcription_{label}.txt', key)
        head = [f'# Mechanical decode of transcription_{label}.txt with George Lasry\'s key for BnF Espagnol 318 no. 95 '
                f'(../esp318no95/lasry2021/ctts/key.txt, sha256 {KEY_SHA[:8]}...{KEY_SHA[-4:]}), applied unchanged',
                '# ? = sign with no value (hole, or a sign not in his table); word division is not in the cipher',
                '# code groups: ' + ', '.join(f'[{k}] = Lasry {v}' for k, v in sorted(labels.items()))
                + '; [bnm] is not in his table']
        (HERE / f'decode_{label}.txt').write_text('\n'.join(head + lines) + '\n', encoding='utf8')
        print(f'== decode_{label}.txt'); print('\n'.join(lines))


if __name__ == '__main__':
    main()
