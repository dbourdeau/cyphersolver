"""Rebuild the decryption of c. 13r from transcription_c13r.txt and key.tsv.
    python scripts/decode.py      writes decryption_c13r.txt"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
PUNCT = {',', '/', '.', ':'}


def load_key(frozen_only=False):
    key = {}
    for l in (ROOT / 'key.tsv').read_text(encoding='utf8').splitlines():
        if not l or l.startswith('#') or l.startswith('sign\t'):
            continue
        s, v, st = l.split('\t')[:3]
        if frozen_only and st != 'frozen':
            continue
        key.setdefault(s, []).extend(v.split('|'))
    return key


def signs():
    for l in (ROOT / 'transcription_c13r.txt').read_text(encoding='utf8').splitlines():
        if l.startswith('M'):
            ln, _, t = l.partition('\t')
            yield ln, [x for x in t.split() if x not in PUNCT and not x.startswith('[')]


def units(toks, key):
    out = []
    for t in toks:
        d = t.endswith('?'); g = t.rstrip('?')
        out.append((g, key.get(g, ['?' + g]), d))
    return out


def main():
    key = load_key()
    lines = ['# Decryption of c. 13r, rebuilt by scripts/decode.py from transcription_c13r.txt and key.tsv.',
             '# Per line: the signs, then the values (a|b = sign name with two values, null = no letter, ? = doubtful sign).']
    for ln, toks in signs():
        us = units(toks, key)
        lines.append(f'{ln}\tsigns\t' + ' '.join(g for g, _, _ in us))
        lines.append(f'{ln}\tvalues\t' + ' '.join('|'.join(v) + ('?' if d else '') for _, v, d in us))
    (ROOT / 'decryption_c13r.txt').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
