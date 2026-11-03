"""List where the decryption departs from the clear text of c. 22r (letters, in order).

    python diff_clear.py <transcription> [key.tsv]
Prints each departure with its line and the sign(s) involved, then the counts.
"""
import difflib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decrypt


def clear_letters():
    s = ' '.join(l.split('\t', 1)[1] for l in open(decrypt.ROOT / 'clear_c22r.txt', encoding='utf-8') if l.startswith('P'))
    s = s.lower().replace('ñ', 'n').replace('ç', 'z')
    for a, b in (('v. ex.', '{vex}'), ('mag.', '{mag}'), ('duque de florencia', '{duq}'), ('bolona', '{bol}'),
                 ('cardenal', '{car}'), ('papa', '{pap}')):
        s = s.replace(a, b)
    return re.findall(r'\{\w+\}|[a-z]', s)


CODES = {'[V. Ex.]': ['{vex}'], '[su Mag.]': list('su') + ['{mag}'], '[Papa]': ['{pap}'], '[Bolona]': ['{bol}'],
         '[Duque de Florencia]': ['{duq}'], '[Cardenal]': ['{car}']}


def cipher_units(tr, key):
    u = []
    lines = {}
    for ln, s, d in decrypt.signs(tr):
        lines.setdefault(ln, []).append((s, d))
    seq = [(ln, s, v) for ln, items in lines.items() for (s, _), v in zip(items, decrypt.line_values(items, key))]
    for ln, s, v in seq:
        if v in CODES:
            u += [(x, ln, s) for x in CODES[v]]
        elif v.startswith('[?'):
            u.append(('?', ln, s))
        else:
            u += [(c, ln, s) for c in re.sub(r'[^a-z]', '', v)]
    return u


def main():
    tr = sys.argv[1]
    key = decrypt.load_key(sys.argv[2]) if len(sys.argv) > 2 else decrypt.load_key()
    cu = cipher_units(tr, key)
    cl = clear_letters()
    sm = difflib.SequenceMatcher(None, [x[0] for x in cu], cl, autojunk=False)
    n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        n += 1
        ctx = ''.join(x if len(x) == 1 else x for x in cl[max(0, j1 - 6):j2 + 6])
        ln = cu[i1][1] if i1 < len(cu) else cu[-1][1]
        print(f'L{ln:02d}\t{op}\tsigns {" ".join(x[2] for x in cu[i1:i2]) or "-"} give "{"".join(x[0] for x in cu[i1:i2])}"'
              f'\tclear "{"".join(cl[j1:j2])}"\tin "{ctx}"')
    m = sum(b.size for b in sm.get_matching_blocks())
    print(f'# {n} departures; {m} of {len(cl)} clear units matched in order ({m / len(cl):.3f})')


if __name__ == '__main__':
    main()
