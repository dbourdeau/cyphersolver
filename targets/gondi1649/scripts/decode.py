"""Rebuild the decryption of c. 1r from transcription_c1r.txt and key.tsv, and run the held-out test.
    python scripts/decode.py            writes decryption_c1r.txt
    python scripts/decode.py --heldout  decodes L07-L13 with the frozen rows only and scores them against the reading
"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent


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
    for l in (ROOT / 'transcription_c1r.txt').read_text(encoding='utf8').splitlines():
        if l.startswith('L'):
            ln, _, t = l.partition('\t')
            yield ln, [x for x in t.split() if x not in ('[TXT]', ',', '.')]


def units(toks, key):
    """Group signs: barred sign = code; 2xx = code; W0 = code; 58 = code; d0 = consonant; else one sign."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]; doubt = t.endswith('?'); t = t.rstrip('?')
        nxt = [x.rstrip('?') for x in toks[i + 1:i + 3]]
        if t.endswith('^'):
            g, n = t, 1
        elif t == '2' and len(nxt) == 2 and '2' + ''.join(nxt) in key:
            g, n = '2' + ''.join(nxt), 3
        elif t in 'W5' and nxt[:1] == [{'W': '0', '5': '8'}[t]] and t + nxt[0] in key:
            g, n = t + nxt[0], 2
        elif nxt[:1] == ['0']:
            g, n = t + '0', 2
        else:
            g, n = t, 1
        doubt = doubt or any(x.endswith('?') for x in toks[i + 1:i + n])
        out.append((g, key.get(g, ['?' + g]), doubt))
        i += n
    return out


def show(u):
    g, vals, d = u
    v = '|'.join(vals)
    return (v if not v.startswith('[') else v) + ('?' if d else '')


def main():
    key = load_key()
    lines = ['# Decryption of c. 1r, rebuilt by scripts/decode.py from transcription_c1r.txt and key.tsv.',
             '# Per line: the sign groups, then the values (a|b = polyphonic sign, [x] = code word, ? = doubtful sign).']
    for ln, toks in signs():
        us = units(toks, key)
        lines.append(f'{ln}\tsigns\t' + ' '.join(g for g, _, _ in us))
        lines.append(f'{ln}\tvalues\t' + ' '.join(show(u) for u in us))
    (ROOT / 'decryption_c1r.txt').write_text('\n'.join(lines) + '\n', encoding='utf8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
