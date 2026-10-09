"""Measure soria1523: share of cipher units (one sign or one code group) read as sense.

Key-A letters: units come from the transcriptions (keyA_june.txt, keyA_r9492_v2.txt), the reading from
r_june.txt / r_july.txt, aligned line by line (difflib) through the mechanical key-A decrypt (deca.py).
Key-B letters: kb_*.txt list each plaintext word with the cipher units that carry it (hand-aligned
from the re-transcription), one word per line: 'word = unit unit unit'.
A unit counts as read only if every word it carries is (a) not bracketed and (b) passes the sense test:
the word (joined across line breaks) is in a Castilian lexicon (Quijote, Vasto memorias, Danvila's
documents of 1520-21; words seen at least twice) or in the proper-name list below.
Bracketed words ([x]) are unread or context-only guesses and count as unread.
{x} marks are declared openers/closers/nulls and are not counted.
Also prints a per-letter character-LM score of the read text (es-golden-age) with a shuffled control.
"""
import sys, os, re, io, difflib, random, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, ROOT); sys.path.insert(0, HERE)
from lang import lm
from deca import dec, toks, CODES

OPEN_CODES = {'rip', 'qed', 'pur', 'dus', 'cop'}
NAMES = set('''milan uenecia uenecianos caracciolo prospero leon francia ytalia italia prouenca bresa grisones otauiano
campofregoso bergamasco bresano bergamo uerona andrea doria salerno saboya jeronimo antonioto adorno martin centurion
beaurren beurren beurre musiur prantener uionet geneua genoua barcelona carraca lorenco mormino seneses najara costancia gattinara turin geneua darmas'''.split())
# period forms checked by hand (absent from the corpora in this spelling): calar 'come down' (of the Swiss),
# desgravar, aposiento 'billeting', comencarles (començar + les)
NAMES |= {'calaran', 'comencarles', 'desgrauaria', 'aposiento'}


def lexicon():
    words = collections.Counter()
    for f in ['lang/corpora/es-quijote.txt', 'lang/corpora/es-vasto-memorias.txt', 'targets/adrian1521/danvila/mhe37.txt']:
        t = lm.norm(open(os.path.join(ROOT, f), encoding='utf-8', errors='ignore').read(), 'early')
        words.update(t.split())
    return {w for w, c in words.items() if c >= 2} | NAMES


def N(w):
    return lm.norm(w, 'early').replace(' ', '')


def add_word(words, w):
    br = w.startswith('[')
    core = w.strip('[]')
    if core.startswith('-') and words and words[-1][0].endswith('-'):
        words[-1][0] = words[-1][0][:-1] + core[1:]
        words[-1][1] = words[-1][1] or br
        return len(words) - 1, core[1:]
    words.append([core, br])
    return len(words) - 1, core.rstrip('-')


MISMATCH = [0]


def keyA(trans, reading):
    rd = {}
    for l in open(reading, encoding='utf-8'):
        m = re.match(r'(L\d+):\s*(.*)', l)
        if m: rd[m.group(1)] = m.group(2)
    words, units = [], []
    for l in open(trans, encoding='utf-8'):
        m = re.match(r'\s*(L\d+):(.*)', l)
        if not m: continue
        lid = m.group(1); ct = [t for t in toks(m.group(2)) if t != '.']
        rw = rd[lid].split()
        for w in rw:
            if w.startswith('{') and w[1:-1] in ct: ct.remove(w[1:-1])
        us = []
        for t in ct:
            if t in CODES: us.append((t, N(CODES[t])))
            elif t in OPEN_CODES: us.append((t, t))
            else:
                v = t.replace('cT', '\x01').replace('Lo', '\x02')
                for ch in v:
                    if ch == '?': continue
                    s = {'\x01': 'cT', '\x02': 'Lo'}.get(ch, ch); d = dec(s)
                    us.append((s, '' if d.startswith('_') or d == '?' else d))
        rch = []; base = len(words)
        for w in rw:
            if w.startswith('{'): continue
            wi, txt = add_word(words, w)
            for c in N(txt): rch.append((c, wi))
        a = ''.join(u[1] or '#' for u in us); owner = []
        for k, u in enumerate(us): owner += [k] * max(1, len(u[1]))
        b = ''.join(c for c, _ in rch)
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        umap = [set() for _ in us]
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != 'equal': MISMATCH[0] += len({owner[i] for i in range(i1, i2)})
            if tag in ('equal', 'replace') and j2 > j1:
                for k in range(i2 - i1):
                    umap[owner[i1 + k]].add(rch[j1 + min(k, j2 - j1 - 1)][1])
        for k in range(len(us)):
            if not umap[k]:
                order = list(range(k - 1, -1, -1)) + list(range(k + 1, len(us)))
                nb = next((umap[j] for j in order if umap[j]), {base})
                umap[k] = set(nb)
        units += umap
    return words, units


def keyB(path):
    words, units = [], []
    for l in open(path, encoding='utf-8'):
        l = re.split(r'\s#\s|^#', l)[0].strip()   # comments: '#' at line start or ' # '; m#, t#, 9# are signs
        if not l or '=' not in l: continue
        w, _, u = l.partition('=')
        w = w.strip(); n = len(u.split())
        if w.startswith('{'): continue
        wi, _ = add_word(words, w)
        units += [{wi}] * n
    return words, units


def sense(s, LEX, M):
    """lexicon word; or an enclitic/inflected form whose stem is in the lexicon; or (length >= 6) a word the
    character LM scores as Castilian (>= -1.9/char; gibberish of the same letters scores below -4)."""
    if s in LEX or s.isdigit(): return True
    # spelling variants of the period: c/z (comencar), u/b (iuntauan), f/h (fasta)
    for i, ch in enumerate(s):
        for a, b in (('c', 'z'), ('u', 'b'), ('f', 'h')):
            if ch == a and s[:i] + b + s[i + 1:] in LEX: return True
    for e in ('selas', 'selos', 'sela', 'selo', 'les', 'los', 'las', 'se', 'la', 'le', 'lo'):
        if s.endswith(e) and s[:-len(e)] in LEX: return True
        if s.endswith(e) and s[:-len(e)] + 'r' in LEX: return True
    return len(s) >= 6 and M.per_char(' ' + s + ' ') >= -1.9


LETTERS = [('June 1523 (R9488-90, key A)', 'A', '../keyA_june.txt', 'r_june.txt'),
           ('July 1523 body (R9492-93, key A)', 'A', '../keyA_r9492_v2.txt', 'r_july.txt'),
           ('July 1523 post data (R9492-93, key B)', 'B', 'kb_r9492.txt', None),
           ('20 July 1523 to Gattinara (R9491, key B)', 'B', 'kb_r9491.txt', None),
           ('26 July 1523 (R9494-96, key B)', 'B', 'kb_r9494.txt', None),
           ('13 Aug 1523 (R9497-98, key B)', 'B', 'kb_r9497.txt', None)]

if __name__ == '__main__':
    os.chdir(HERE); LEX = lexicon(); M = lm.load('es-golden-age')
    tot_r = tot = 0; verbose = '-v' in sys.argv
    for name, kind, a, b in LETTERS:
        if not os.path.exists(a): print(f'{name}: (no file {a})'); continue
        words, units = keyA(a, b) if kind == 'A' else keyB(a)
        ok, bad = [], []
        for w, br in words:
            s = N(w.rstrip('-'))
            good = (not br) and sense(s, LEX, M)
            ok.append(good)
            if not br and not good: bad.append(w)
        if kind == 'A':
            print(f'   key-A units whose mechanical decrypt differs from the reading (homophone variants, slips): {MISMATCH[0]}'); MISMATCH[0] = 0
        r = sum(1 for u in units if all(ok[i] for i in u)); n = len(units)
        tot_r += r; tot += n
        txt = ' '.join(N(w) for (w, br), g in zip(words, ok) if g)
        sc = M.per_char(txt); L = list(txt); random.seed(1); random.shuffle(L)
        print(f'{name}: {r}/{n} units read = {r / n:.3f}; words {sum(ok)}/{len(words)}; '
              f'LM {sc:.2f}/char (shuffled control {M.per_char("".join(L)):.2f})')
        if bad: print('   unbracketed words failing the lexicon:', ' '.join(bad))
        if verbose: print('   unread:', ' '.join(w for (w, br), g in zip(words, ok) if not g))
    print(f'OVERALL: {tot_r}/{tot} = {tot_r / tot:.3f}')
