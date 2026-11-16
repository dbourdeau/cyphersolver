"""Decode the glossed Bue 702 word lists with key.tsv (K3) beside the gloss of the time (14 Nov 2026). Standard library only.

    python decode_k3.py            writes bu702_decryption.txt and bu702_gloss.txt

Sources: frozen/train_k3_b702_16_v2.tsv (Bild 16, the 30 words that trained K3) and the held-out block of transcription.txt
(Bild 17 and the end of Bild 16, 24 words). Normalisation as fixed in frozen/PROTOCOLE-v3.md: the 1799 secretary's looped 8 is σ (token o),
and 8d is 0d (82 = 02, 81 = 01 ...). Doubled letters are not collapsed here; ‹x› = a token with no value in key.tsv.
"""
import pathlib, re

H = pathlib.Path(__file__).resolve().parent
KEY = {}
for l in (H / 'key.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith('#') or not l.strip(): continue
    kind, tok, val = l.split('\t')[:3]
    KEY[tok] = '' if kind == 'null' else val


def norm(t):
    t = t.rstrip('?')
    if t == '8': return 'o'
    if re.fullmatch(r'8\d', t): return '0' + t[1]
    return t


def dec(tokens):
    if tokens.strip() == '90': return 'und'   # key.tsv: 90 alone = und
    out = []
    for t in tokens.split():
        n = norm(t)
        out.append(KEY[n] if n in KEY else '‹%s›' % t)
    return ''.join(out)


rows = []
for l in (H / 'frozen' / 'train_k3_b702_16_v2.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith('#') or not l.strip(): continue
    rows.append(('train',) + tuple(l.split('\t')[:3]))
block = False
for l in (H / 'transcription.txt').read_text(encoding='utf8').splitlines():
    if l.startswith('## Held-out'): block = True; continue
    if l.startswith('## '): block = False
    if block and l.strip() and not l.startswith('#'):
        rows.append(('held out',) + tuple(l.split('\t')[:3]))
d = ['# Bue 702 (1799), Bild 16 and 17: the ciphered words of the glossed passages decoded with key.tsv (K3), beside the gloss of the time.',
     '# Written by decode_k3.py, 14 Nov 2026. These are the ciphered words only, one per row, in the order transcribed; the reports are otherwise in clear and are not transcribed here.',
     '# set = train (the 30 words of Bild 16 that K3 was built on) or held out (Bild 17 and the end of Bild 16, the validation set). ‹x› = no value in key.tsv.',
     'set\tBild\ttokens\tK3 decode\tgloss of the time\tagree']
g = ['# Bue 702 (1799), Bild 16 and 17: the glosses of the time over the ciphered words, as transcribed by the contributor (the third column of',
     '# frozen/train_k3_b702_16_v2.tsv and of the held-out block of transcription.txt). Extracted 14 Nov 2026 without change, one word per ciphered word.']
ok = 0
for s, b, t, gl in rows:
    x = dec(t)
    a = re.sub(r'(.)\1', r'\1', x.lower()) == re.sub(r'(.)\1', r'\1', gl.lower())
    ok += a
    d.append('\t'.join((s, b, t, x, gl, 'yes' if a else 'no')))
    g.append('Bild %s (%s): %s' % (b, s, gl))
d.insert(3, '# %d of %d words agree with the gloss letter for letter once doubles are collapsed (no other normalisation; ü/u, y/i and similar count as differences).' % (ok, len(rows)))
(H / 'bu702_decryption.txt').write_text('\n'.join(d) + '\n', encoding='utf8', newline='')
(H / 'bu702_gloss.txt').write_text('\n'.join(g) + '\n', encoding='utf8', newline='')
print(ok, len(rows))
