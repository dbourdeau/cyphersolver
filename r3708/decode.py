"""Check the reading of BnF fr. 3976 ff. 133-134 (R3708) sign by sign against the key.

The key is nevers1588/key.md (ff. 62 and 131) plus the values this letter added (Q = y, Z = z,
[ and J = n, J = f, r = g, curly 8 = p). Signs are polyphonic, so the decoder does not choose a letter: for each run it aligns
the reading in reading.tsv with the signs and checks every letter against the sign's candidate
values. A letter outside the candidates is reported as NEW (a value this letter alone supports).

    python r3708/decode.py            # per-run check
    python r3708/decode.py --reveal   # write docs/reveal/r3708.json
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# sign -> candidate plaintext letters (u/v and i/j merged)
KEY = {
    '2': 'ah', 'z': 'a', '9': 'ahr', '8': 'buv', 'y': 'b', 'd': 'buv', '7': 'c', 'X': 'c', 'x': 'c',
    '1s': 'cq', '6': 'd', 'v': 'd', 't': 'e', 's': 'e', '5': 'e', '4': 'f', 'f': 'fs', '3': 'gj',
    'g': 'gr', '1r': 'g', 'p': 'i', '1n': 'i', '1e': 'i', 'n': 'l', 'o': 'lu', '19': 'm', 'm': 'm',
    '1d': 'n', 'l': 'n', 'J': 'p', '17': 'o', 'k': 'o', '16': 'p', '1b': 'p', 'h': 'q',
    'q': 'hry', '14': 'r', '13': 's', '12': 't', 'E': 't', '11': 'uv', 'c': 'x',
}
# values first attested in this letter (added to nevers1588/key.md)
ADDED = {'Q': 'y', 'Z': 'z', '[': 'n', 'J': 'nf', 'r': 'g', 'd': 'p'}
# signs seen only once, read from context (reading.tsv, Remaining gaps); R08 '2 t' = 'et'
CONTEXT = {'+': 'e', '1o': 'i'}
CONTEXT_PAIRS = {('R08', 10), ('R08', 11)}


def norm(ch):
    return {'v': 'u', 'j': 'i'}.get(ch, ch)


def runs():
    ct = {}
    for line in open(os.path.join(HERE, 'ciphertext.txt'), encoding='utf8'):
        if line.startswith('#') or not line.strip():
            continue
        rid, signs = line.rstrip('\n').split('\t')
        ct[rid] = [s for s in signs.split() if s != 'S^t']
    rd = {}
    for line in open(os.path.join(HERE, 'reading.tsv'), encoding='utf8'):
        f = line.rstrip('\n').split('\t')
        rd[f[0]] = (f[2], f[3])
    return ct, rd


def align(signs, plain, rid=''):
    """Pair each non-code sign with one letter of plain (letters only, '?' kept)."""
    letters = [c for c in plain if c.isalpha() or c == '?']
    out, i = [], 0
    for s in signs:
        if s.startswith('<'):
            out.append((s, s.strip('<>'), 'code'))
            continue
        # R08: the pair '2 t' carries 'et' after 'andr' + '+'
        p = letters[i] if i < len(letters) else '?'
        i += 1
        if s in CONTEXT or (rid, i - 1) in CONTEXT_PAIRS:
            out.append((s, p, 'unc'))
        elif norm(p) in {norm(c) for c in ADDED.get(s, '')}:
            out.append((s, p, 'added'))
        elif norm(p) in {norm(c) for c in KEY.get(s, '')}:
            out.append((s, p, ''))
        else:
            out.append((s, p, 'NEW'))
    return out, len(letters) - i


def main():
    ct, rd = runs()
    total = ok = 0
    for rid, signs in ct.items():
        plain = rd[rid][0].replace(' ', '')
        pairs, left = align(signs, plain, rid)
        bad = [(s, p) for s, p, c in pairs if c == 'NEW']
        unc = [(s, p) for s, p, c in pairs if c == 'unc']
        add = [(s, p) for s, p, c in pairs if c == 'added']
        n = sum(1 for _, _, c in pairs if c != 'code')
        total += n
        ok += n - len(bad) - len(unc)
        print(f'{rid}: {n:3d} signs  {"".join(p for _, p, c in pairs if c != "code")}'
              + (f'  NEW {bad}' if bad else '') + (f'  context {unc}' if unc else '') + (f'  added {add}' if add else '')
              + (f'  LEFTOVER {left}' if left else ''))
    print(f'total {total} signs, {ok} read by the key or its additions, {total - ok} NEW or context-only')


def reveal():
    ct, rd = runs()
    passage = [
        ('', 'de sorte que '), ('R11', None),
        ('', ' on leur faict tousjours passer quelque carriere, car si tost que quelque chose a esté resolu en l\'hostel de ville, '),
        ('R12', None), ('', ' ne fault de rapporter le tout au '), ('R13', None),
        ('', ' pour adviser les moyens de rompre les deliberations qui ne leur plaisent, ou assistent tousjours '),
        ('R14', None), ('', '. L\'on m\'a asseuré neantmoings que ces jours passez 9 voullant faire sortir '),
        ('R15', None), ('', ' pour aller a '), ('R16', None), ('', ', l\'un des eschevins '), ('R17', None),
        ('', ' qu\'il ne consentiroit jamais que cela se feist sans permission du Roy.'),
    ]
    toks = []
    for rid, text in passage:
        if not rid:
            toks.append({'g': '', 'p': text, 'cls': 'plain'})
            continue
        pairs, _ = align(ct[rid], rd[rid][0].replace(' ', ''), rid)
        for s, p, c in pairs:
            g = {'Q': 'ϙ', 'Z': 'ꝗ', 'E': 'ε', 'd': 'δ'}.get(s, s)
            cls = {'code': 'code', 'unc': 'unc', 'NEW': 'unc'}.get(c, '')
            toks.append({'g': g, 'p': p, 'cls': cls})
    out = {
        'slug': 'r3708', 'anchor': 'reading',
        'title': 'The Hôtel de Ville and Guise\'s council',
        'caption': "BnF fr. 3976 f. 133v, the runs from 'par ruses et faulx bruictz' to 'nommé Cotteblanche dist', "
                   "checked sign by sign against the key of ff. 62 and 131 (r3708/decode.py). Clear text between the runs is as written.",
        'unit': 'signs (one character, or 1 + character)',
        'key_note': 'Homophonic, some signs polyphonic: 9 = a, h or r; the curly 8 = b, u or v; n and o = l. '
                    'Underlined numbers inside a run are code numbers (9 = Guise).',
        'tokens': toks,
    }
    path = os.path.join(HERE, '..', 'docs', 'reveal', 'r3708.json')
    with open(path, 'w', encoding='utf8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote', path, len(toks), 'tokens')


if __name__ == '__main__':
    reveal() if '--reveal' in sys.argv else main()
