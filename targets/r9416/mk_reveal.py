"""Write docs/reveal/r9416.json: f.263 recto lines 11-13 sign by sign, from the word-by-word table of
r9416/reading_p3_11-16.txt (written 15 Oct 2026). Each cipher word is split into the v2 codes (io = e and ng = ch are
one sign each) and aligned to its reading with the key printed in that file's header; a sign whose key value does not
give the reading letter is marked 'unc' (none should be, except the code sign g = [Ferd.], marked 'code', and the
three passed-over signs cI), marked null). Run: python targets/r9416/mk_reveal.py"""
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
    if l.startswith('14  '):
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
while toks and toks[-1]['p'] == ' ':
    toks.pop()
out = {
 'slug': 'r9416',
 'anchor': 'f263',
 'title': 'The Pressburg report, f. 263 recto, lines 11–13',
 'caption': 'Lines 11–13 of R9416 f. 263 recto (BayHStA Kurbayern Äußeres Archiv 4591), sign by sign with the key recovered from the ciphertext alone and re-keyed by hand on these lines: “… daraus der Tag zu Bresburg erfolgt ist, dahin auch des [Ferd.] Tail mit grossem Bumbb kummen sint, auch volmechtigen Gwalt anzaigt …”. The faint gloss of the time over lines 11–12 agrees. g is a code sign for a person, read from the gloss; three signs after “Tail” are passed over by the gloss.',
 'unit': 'signs',
 'key_note': 'A homophonic alphabet with word division; some codes stand for two look-alike signs (z = e or s, b = d or l), and io (e) and ng (ch) are single signs. Shown as the codes of r9416/p34_v2.txt.',
 'tokens': toks,
}
json.dump(out, io.open(os.path.join(ROOT, 'docs', 'reveal', 'r9416.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len([t for t in toks if t['g']]), 'signs;', sum(t['cls'] == 'unc' for t in toks), 'unc')
print(''.join(('[' + t['p'] + ']' if t['cls'] == 'unc' else t['p']) if t['cls'] not in ('null',) else '·' for t in toks))
