"""Decrypt the sign transcription with key.tsv, line by line. Standard library only.

    python scripts/decode.py                 print the decryption
    python scripts/decode.py --write         rewrite decryption_15oct_ff34r-35v.txt

Output is letter for letter; nulls are dropped; a code sign prints as [Qn]. Signs marked doubtful in the transcription, and
values the key marks as proposed from context, print in round brackets: (i), or [Q8?] for a code sign.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TR = ROOT / 'transcription_15oct_ff34r-35v.txt'
OUT = ROOT / 'decryption_15oct_ff34r-35v.txt'


def load_key():
    key, proposed = {}, set()
    for l in (ROOT / 'key.tsv').read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        p = l.split('\t')
        key[p[0]] = p[1]
        if len(p) > 2 and p[2] == 'proposed':
            proposed.add(p[0])
    return key, proposed


def signs():
    """Yield (line, sign, doubtful) for every sign of the transcription, nulls included."""
    for l in TR.read_text(encoding='utf8').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        t = l.split()
        for x in t[1:]:
            yield t[0], x.split('{')[0].lstrip('^'), '{?' in x


def decrypt():
    key, proposed = load_key()
    lines = {}
    for ln, s, doubt in signs():
        v = key[s]
        lines.setdefault(ln, [])
        if v == 'null':
            continue
        doubt = doubt or s in proposed
        if v.startswith('['):
            lines[ln].append(v[:-1] + '?]' if doubt else v)
        else:
            lines[ln].append('(' + v + ')' if doubt else v)
    return [f'{ln} {"".join(r)}' for ln, r in lines.items()]


if __name__ == '__main__':
    out = '\n'.join(decrypt()) + '\n'
    if '--write' in sys.argv:
        OUT.write_text(out, encoding='utf8', newline='\n')
    else:
        sys.stdout.write(out)
