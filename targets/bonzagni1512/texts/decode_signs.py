"""Decode a sign transcription in the labels of R1125_transcription.txt with sign_values.tsv (14 Nov 2026). Standard library only.

    python decode_signs.py R1125_transcription.txt > R1125_decryption.txt

A mechanical decode: p is printed n (it stands for d or n), u stands for u or v, a sign marked ? keeps the mark, a sign with no value prints ‹sign›.
"""
import pathlib, re, sys

H = pathlib.Path(__file__).resolve().parent
KEY = {}
for l in (H / 'sign_values.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith('#') or l.startswith('sign\t') or not l.strip(): continue
    s, v = l.split('\t')[:2]
    KEY[s] = 'n' if v == 'd or n' else v


def word(g):
    g = g.strip()
    if not g: return ''
    out, rest = [], g
    for br in re.findall(r'\[[^\]]*\]', g):
        rest = rest.replace(br, ' ')
    for t in rest.split():
        q = t.endswith('?'); t0 = t.rstrip('?')
        if t0 in ('·', ':', '-'): out.append(t0); continue
        if t0 == '': out.append('?'); continue
        v = KEY.get(t0)
        out.append((v if v is not None else ('.31.' if t0 == '.31.' else '‹%s›' % t0)) + ('?' if q else ''))
    br = ' '.join(re.findall(r'\[[^\]]*\]', g))
    return (br + ' ' if br else '') + ''.join(out)


for l in open(sys.argv[1], encoding='utf8'):
    m = re.match(r'(L\d+): (.*)', l)
    if m: print(m.group(1) + ': ' + ' | '.join(w for w in (word(g) for g in m.group(2).split('|')) if w))
