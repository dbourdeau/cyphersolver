"""Beling addition to magdeburg1647: decode the *_BEL transcriptions with the envoys' worksheet key (frame 168).

Standard library only, no network. Run from this target folder:  python3 -I scripts/beling_build.py
  - writes decryptions/<name>_BEL.txt for every transcriptions/<name>_BEL.txt
  - prints a count of cipher words per file (clear text, described signs and alternatives' second branch excluded)
  - with --frame278, prints the worksheet-key rescoring of the frame-278 gloss pairs instead
  - with --check, compares each output with the file already filed and exits 1 on any difference

Key: AMPHICTYONES over zxwurqlkgfdb, reciprocal (gloss/worksheet_frame168.txt). Conventions of these transcriptions:
i = j and u = v (cipher j decodes as r, cipher v as h); the W-shaped glyph is cipher w (= plain p).
Markup passes through unchanged: {clear: ...} clear text on the page, [S: ...] a described sign, [blot], [struck],
[gutter] and similar editorial tags; the capital K-form is cipher y (= plain k); <A || B> written as
'⟨A ∥ B⟩' for two readings the image does not settle (both branches are decoded), '?' an unread letter.
"""
import pathlib, re, sys

TOP, BOTTOM = 'amphictyones', 'zxwurqlkgfdb'
KEY = {}
for a, b in zip(TOP, BOTTOM):
    KEY[a] = b; KEY[b] = a
KEY.update({'j': 'r', 'v': 'h', 'W': 'p', 'K': 'y'})
SPAN = re.compile(r'(\{clear:[^}]*\}|\[[^\]]*\])')
HERE = pathlib.Path(__file__).resolve().parent.parent


def decode_text(s):
    out = []
    for part in SPAN.split(s):
        if SPAN.fullmatch(part or ''):
            out.append(part)
        else:
            out.append(''.join(KEY.get(c, c) for c in part))
    return ''.join(out)


def cipher_words(s):
    s = SPAN.sub(' ', s)
    s = re.sub(r'⟨([^∥⟩]*)∥[^⟩]*⟩', r'\1', s)
    return [w for w in s.split() if re.search(r'[A-Za-z]', w)]


def build(check=False):
    bad = 0
    for tx in sorted((HERE / 'transcriptions').glob('*_BEL.txt')):
        rows, words = [], 0
        for line in tx.read_text(encoding='utf-8').splitlines():
            if line.startswith('#') or not line.strip():
                continue
            parts = line.split('\t')
            words += len(cipher_words(parts[-1]))
            rows.append('\t'.join(parts[:-1] + [decode_text(parts[-1])]))
        head = [f'# {tx.name} decoded with the frame-168 worksheet key (AMPHICTYONES over zxwurqlkgfdb) by scripts/beling_build.py.',
                '# Mechanical output only: no letter changed, markup passed through. The readings are in readings/.']
        text = '\n'.join(head + rows) + '\n'
        out = HERE / 'decryptions' / tx.name
        if check:
            same = out.is_file() and out.read_text(encoding='utf-8') == text
            bad += not same
            print(f'{tx.name}: {words} cipher words, decryption {"identical" if same else "DIFFERS"}')
        else:
            out.write_text(text, encoding='utf-8')
            print(f'{tx.name}: {words} cipher words')
    return bad




def frame278():
    """Descriptive rescoring of the 23 frame-278 gloss pairs (gloss/frame278_BEL/) with the worksheet key.
    The pre-registered test (PREREG2_frame0278.md) used the earlier booklet key and is filed as it ran."""
    import csv, difflib
    base = HERE / 'gloss' / 'frame278_BEL'
    norm = lambda s: s.lower().replace('ä', 'a').replace('ö', 'o').replace('ü', 'u').replace('v', 'u').replace('j', 'i').replace(' ', '')
    ci = {r['id']: r['cipher_as_seen'] for r in csv.DictReader(open(base / 'f0278_cipher_as_seen.tsv', encoding='utf-8'), delimiter='\t')}
    gl = {r['id']: norm(r['clear_as_seen']) for r in csv.DictReader(open(base / 'f0278_gloss_as_seen.tsv', encoding='utf-8'), delimiter='\t')}
    m = t = exact = 0
    lines = ['id\tcipher\tworksheet decode\tclear gloss\tmatched/clear']
    for k in sorted(ci):
        d = norm(''.join(KEY.get(c, c) for c in ci[k]))
        g = gl[k]
        mm = sum(b.size for b in difflib.SequenceMatcher(None, d, g, autojunk=False).get_matching_blocks())
        m += mm; t += len(g); exact += d == g
        lines.append(f'{k}\t{ci[k]}\t{d}\t{g}\t{mm}/{len(g)}')
    lines.append(f'# pooled {m}/{t} = {m / t:.4f}; exact words {exact}/{len(ci)}')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    if '--frame278' in sys.argv:
        print(frame278(), end='')
    else:
        sys.exit(1 if build('--check' in sys.argv) else 0)
