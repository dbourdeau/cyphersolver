"""Apply George Lasry's key for BnF Espagnol 318 no. 95, unchanged, to the transcriptions of Juan Manuel's two letters
from Genoa of 10 November and 18 December 1496 (Biblioteca Nacional de España, MSS/20212/61/1 and /2).

    python decode.py

The key is read from Lasry's own target (../esp318no95/lasry2021/ctts/key.txt) and checked by its sha256; nothing is
copied, changed, added or refitted. The transcriptions are in his sign names. Writes, per letter:

  decode_<letter>.txt          the main decode: the sign written S here has no value (see below)
  decode_<letter>_with_S.txt   the same with that sign given Lasry's value for his S (d), reported separately

Marks in the decodes:
  ?          a sign with no value: a hole (_) of the transcription; a sign with no counterpart in his key (<W26>, <W27>,
             <W48>, <W49>); his 9 (his own value is "[y?]"); in the main decode, S
  |[grp]|    a group written in Latin letters (a code group); no value is given to any
  |<clear>|  ordinary handwriting follows
His null D is dropped. The sign written S was matched to his S by its shape only after decodes had been seen, so the
main decode and every count give it no value; the _with_S files show what it adds.

Standard library only; deterministic.
"""
import hashlib, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
KEY = HERE.parent / 'esp318no95' / 'lasry2021' / 'ctts' / 'key.txt'
KEY_SHA = '5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06'
LETTERS = {
    '10nov1496': 'Juan Manuel, Genoa, 10 November 1496 (BNE MSS/20212/61/1; lines L = f. 2v, R = f. 3r)',
    '18dec1496': 'Juan Manuel, Genoa, 18 December 1496 (BNE MSS/20212/61/2; lines A = f. 6r, B = f. 6v, C = f. 7r)',
}


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


def value(t, key, with_s):
    if t == '_' or re.fullmatch(r'<W\d\d>', t):
        return '?'
    if t == '<clear>':
        return ' |<clear>| '
    if t.startswith('{'):
        return f' |[{t[1:-1]}]| '
    if t == 'S' and not with_s:
        return '?'
    v = key[t]
    if v == '[null?]':
        return ''
    return v.lower() if len(v) == 1 else '?'


def decode(path, key, with_s):
    out = []
    for line in path.read_text(encoding='utf8').splitlines():
        m = re.match(r'([A-Z]\d\d):\s*(.*)', line)
        if m:
            s = ''.join(value(t, key, with_s) for t in m.group(2).split())
            out.append(f'{m.group(1)}: ' + re.sub(' +', ' ', s).strip())
    return out


def main():
    key = load_key()
    for name, label in LETTERS.items():
        for with_s in (False, True):
            lines = decode(HERE / f'transcription_{name}.txt', key, with_s)
            head = [f'# Mechanical decode of transcription_{name}.txt: {label}',
                    f"# George Lasry's key for BnF Espagnol 318 no. 95 (../esp318no95/lasry2021/ctts/key.txt, sha256 "
                    f'{KEY_SHA[:8]}...{KEY_SHA[-4:]}), applied unchanged; no word division (it is not in the cipher)',
                    '# ? = sign with no value (hole, a sign with no counterpart in the key, his 9'
                    + (')' if with_s else ', or S') + '; |[grp]| = code group in Latin letters, no value given',
                    ('# VARIANT: the sign written S is given the value of Lasry\'s S (d); this mapping was made after '
                     'decodes had been seen and is not used in any count' if with_s else
                     '# main decode: the sign written S has no value (its match to Lasry\'s S was made after decodes '
                     'had been seen)')]
            suffix = '_with_S' if with_s else ''
            (HERE / f'decode_{name}{suffix}.txt').write_text('\n'.join(head + lines) + '\n', encoding='utf8')
            print(f'decode_{name}{suffix}.txt: {len(lines)} lines')


if __name__ == '__main__':
    main()
