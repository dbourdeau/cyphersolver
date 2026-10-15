"""Write validation.tsv for docs/_validate.py: f.263 recto lines 11-16 sign by sign (the lines re-keyed by hand on
30 Sept 2026; written 15 Oct 2026 from mk_reveal.py, which shows lines 11-13), from the word-by-word table of
r9416/reading_p3_11-16.txt (written 15 Oct 2026). Each cipher word is split into the v2 codes (io = e and ng = ch are
one sign each) and aligned to its reading with the key printed in that file's header; a sign whose key value does not
give the reading letter is marked 'unc' (none should be, except the code sign g = [Ferd.], marked 'code', and the
three passed-over signs cI), marked null). Run: python targets/r9416/mk_validation.py"""
import io, os, re, json
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(H))
KEY = {'z': ['e', 's'], 'f': ['o'], 'j': ['z'], 'H': ['u', 'v'], 'K': ['k'], 's': ['a'], 'q': ['a'], 'O': ['t'],
       'Q': ['n'], 'b': ['d', 'l'], 'B': ['l'], '>': ['m'], 'A': ['g'], 'D': ['f', 'v'], 'y': ['r'], 'm': ['i'],
       'io': ['e'], 'ng': ['ch'], 'g': ['h'], 'a': ['b', 'p'], 'p': ['b', 'w', 'u'], '4': ['s'], 'c': ['t']}
# the table's own corrections (M grade): the image showed another sign than the v2 code
FIX = {('volmechtigen', 0): ['v'], ('anzaigt', 2): ['z'], ('anzaigt', 5): ['g'], ('grosem', 2): ['o'],
       ('erfolgt', 3): ['o'], }


# the cipher's own spelling where the table's plain column is normalised
PLAIN = {'Pomp': 'bumbb'}


def split(w):
    return re.findall(r'io|ng|.', w)


def align(tokens, word):
    """DP: each token takes one of its key values (cost 0) or, failing that, any one letter (cost 1, marked 'unc');
    returns [(value, ok)] for the cheapest path that spells the word, or None."""
    word = word.lower()
    plain = re.sub(r'(.)\1', r'\1', word)
    best = {0: (0, [])}
    for i, t in enumerate(tokens):
        nxt = {}
        for pos, (cost, ch) in best.items():
            opts = [(v, True) for v in FIX.get((plain, i), KEY.get(t, []))] + [(word[pos:pos + 1], False)]
            for v, ok in opts:
                if v and word.startswith(v, pos):
                    c = cost + (0 if ok else 1)
                    if pos + len(v) not in nxt or nxt[pos + len(v)][0] > c:
                        nxt[pos + len(v)] = (c, ch + [(v, ok)])
        best = nxt
    return best.get(len(word), (99, None))


toks = []
started = False
for l in io.open(os.path.join(H, 'r9416', 'reading_p3_11-16.txt'), encoding='utf8'):
    m = re.match(r'(\d\d)?\s+(\S+(?: \S+)*?)\s{2,}(\[?[A-Za-zäöü.]+\]?(?: [A-Za-zäöü\-]+)*|\(not rendered\))\s', l)
    if l.startswith('11  '):
        started = True
    if not started:
        continue
    if l.startswith('17  ') or l.startswith('## '):
        break
    if not m:
        continue
    cipher, plain = m.group(2), m.group(3)
    if plain.startswith('['):
        toks.append({'g': cipher, 'p': plain.strip('[]'), 'cls': 'code'})
        toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
        continue
    if plain == '(not rendered)':
        for c in cipher:
            toks.append({'g': c, 'p': '', 'cls': 'null'})
        toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
        continue
    groups = [split(g) for g in cipher.replace('?', '').split()]
    t = [x for g in groups for x in g]
    ends = set()
    n = 0
    for g in groups:
        n += len(g); ends.add(n)
    pw = PLAIN.get(plain, plain).replace(' ', '').lower()
    vals = min(align(t, pw), align(t, re.sub(r'(.)\1', r'\1', pw)), key=lambda x: x[0])[1]
    for i, s_ in enumerate(t):
        if vals:
            toks.append({'g': s_, 'p': vals[i][0], 'cls': '' if vals[i][1] else 'unc'})
        else:
            toks.append({'g': s_, 'p': KEY.get(s_, ['?'])[0], 'cls': 'unc'})
        if i + 1 in ends:
            toks.append({'g': '', 'p': ' ', 'cls': 'plain'})
pairs = []
for t in toks:
    if not t['g']:
        continue
    if t['cls'] == 'null':
        pairs.append((t['g'], '-'))
    elif t['cls'] in ('unc', 'unk', 'code'):
        pairs.append((t['g'].replace(' ', '_'), '?'))
    else:
        pairs.append((t['g'], t['p']))
n_sig = 0
for l in io.open(os.path.join(H, 'r9416', 'p34_v2.txt'), encoding='utf8'):
    mm = re.match(r'(\d\d): (.*)', l)
    if mm:
        n_sig += sum(1 for ch in re.sub(r'\[[^\]]*\]', '', mm.group(2)).replace('?', '') if not ch.isspace())
with io.open(os.path.join(H, 'validation.tsv'), 'w', encoding='utf8') as f:
    f.write('# model: de-1500s\n# source: r9416/reading_p3_11-16.txt word table, aligned sign by sign with its key (mk_validation.py)\n')
    f.write('# note: f.263 recto lines 11-16 only (the clean hand re-keying); signs the reading does not give unread\n')
    for g_, v in pairs:
        f.write(f'{g_}\t{v}\n')
read = sum(1 for _, v in pairs if v not in ('?',))
print(len(pairs), 'signs on lines 11-16;', read, 'read;', n_sig, 'signs on f.263;', f'{read / n_sig:.3f} of f.263 read clean')
