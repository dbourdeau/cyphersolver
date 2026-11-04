"""Build and check the marked reading of c. 15r. Standard library only.

    python reading.py build   write the marked block of reading_c15r.md: the words of the contemporary decipherment (c. 22r),
                              each departure from the signs marked in place
    python reading.py check   rebuild the decryption from transcription_c15r.txt and key.tsv, walk the marked reading
                              unit by unit against it, count words; exit 1 on any unmarked departure

Marks (inside a word):
    {a/e}   the text reads a, the signs give e          changed
    {+s}    the text has s, no sign gives it            restored from c. 22r
    {-e}    a sign gives e, the text does not have it   dropped
    [V. Ex.] etc.  code group, read
A word with no mark is verbatim from the signs. Code values: see key.tsv.
"""
import difflib
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decrypt
import diff_clear

ROOT = decrypt.ROOT
TR = ROOT / 'transcription_c15r.txt'
OUT = ROOT / 'reading_c15r.md'
A, B = '<!-- marked -->', '<!-- /marked -->'
CODE_TXT = {'{vex}': '[V. Ex.]', '{mag}': '[Mag.]', '{pap}': '[Papa]', '{bol}': '[Bolona]',
            '{duq}': '[Duque de Florencia]', '{car}': '[Cardenal]'}


def clear_words():
    s = ' '.join(l.split('\t', 1)[1].strip() for l in open(ROOT / 'clear_c22r.txt', encoding='utf-8') if l.startswith('P'))
    s = s.replace('ñ', 'n').replace('ç', 'z')
    for a, b in (('V. Ex.', '{vex}'), ('Mag.', '{mag}'), ('Duque de Florencia', '{duq}'), ('Bolona', '{bol}'),
                 ('Cardenal', '{car}'), ('Papa', '{pap}')):
        s = s.replace(a, b)
    words = []
    for w in s.split():
        units = re.findall(r'\{\w+\}|[A-Za-z]', w)
        if units:
            words.append(units)
    return words


def build():
    cu = [x[0] for x in diff_clear.cipher_units(TR, decrypt.load_key())]
    words = clear_words()
    flat = [(wi, u.lower() if len(u) == 1 else u, u) for wi, w in enumerate(words) for u in w]
    marks = [[] for _ in words]  # per word: list of rendered pieces
    sm = difflib.SequenceMatcher(None, cu, [f[1] for f in flat], autojunk=False)
    pending = []  # dropped sign values waiting for the next clear unit's word

    def put(wi, piece):
        marks[wi].extend(pending)
        pending.clear()
        marks[wi].append(piece)

    for op, i1, i2, j1, j2 in sm.get_opcodes():
        cl = flat[j1:j2]
        ci = cu[i1:i2]
        if op == 'equal':
            for wi, lo, orig in cl:
                put(wi, CODE_TXT.get(lo, orig))
            continue
        k = 0
        for wi, lo, orig in cl:
            if k < len(ci) and len(lo) == 1 and len(ci[k]) == 1:
                put(wi, '{%s/%s}' % (orig, ci[k]))
                k += 1
            else:
                put(wi, '{+%s}' % (CODE_TXT.get(lo, orig)))
        for c in ci[k:]:
            pending.append('{-%s}' % c)
    if pending:
        marks[-1].extend(pending)
    text = ' '.join(''.join(m) for m in marks)
    doc = OUT.read_text(encoding='utf-8')
    head, rest = doc.split(A, 1)
    tail = rest.split(B, 1)[1]
    OUT.write_text(head + A + '\n' + text + '\n' + B + tail, encoding='utf-8')
    print('wrote the marked block of', OUT)


def check():
    cu = [x[0] for x in diff_clear.cipher_units(TR, decrypt.load_key())]
    text = OUT.read_text(encoding='utf-8').split(A, 1)[1].split(B, 1)[0]
    rev = {v: k for k, v in CODE_TXT.items()}
    signs_side = []
    words = verbatim = 0
    fails = []
    tokens = re.findall(r'(?:\[[^\]]+\]|\{[^}]*\}|[A-Za-z])+', text.replace('[Duque de Florencia]', '[Duque_de_Florencia]'))
    for w in tokens:
        w = w.replace('_', ' ')
        words += 1
        marked = False
        for u in re.findall(r'\[[^\]]+\]|\{[^}]*\}|[A-Za-z]', w):
            if u.startswith('['):
                signs_side.append(rev[u])
            elif u.startswith('{+'):
                marked = True
            elif u.startswith('{-'):
                marked = True
                signs_side.append(u[2:-1])
            elif u.startswith('{'):
                a, b = u[1:-1].split('/')
                if a.lower() == b:
                    fails.append(f'empty change mark {u} in {w}')
                marked = True
                signs_side.append(b)
            else:
                signs_side.append(u.lower())
        verbatim += not marked
    if signs_side != cu:
        sm = difflib.SequenceMatcher(None, signs_side, cu, autojunk=False)
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op != 'equal':
                fails.append(f'unmarked departure: reading implies {signs_side[i1:i2]}, signs give {cu[j1:j2]}')
    print(f'words {words}; verbatim from the signs {verbatim} ({verbatim / words:.1%}); with marks {words - verbatim}')
    for f in fails:
        print('FAIL', f)
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    {'build': build, 'check': check}[sys.argv[1]]()
