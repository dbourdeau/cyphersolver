"""kanawha1863: check the frozen hashes, the route on the crib, the held-out test, and write the decryption grids.

Run from anywhere:  python targets/kanawha1863/verify.py
Writes decryption/*.txt (grids with code words replaced, unvalued code words in [brackets]).
Exits non-zero if a hash, the crib check or the held-out figures do not reproduce.
"""
import hashlib, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(HERE, 'freeze', 'round2')
R1 = os.path.join(HERE, 'freeze', 'round1')
ok = True


def check(cond, msg):
    global ok
    print(('PASS ' if cond else 'FAIL ') + msg)
    ok = ok and cond


# 1. Freeze hashes ------------------------------------------------------------
def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

for folder, listing in ((R1, 'key.sha256'), (R2, 'key_v2.sha256')):
    for line in open(os.path.join(folder, listing)):
        h, name = line.split()
        p = os.path.join(folder, os.path.basename(name))
        check(sha(p) == h, f'hash {os.path.relpath(p, HERE)}')

K = json.load(open(os.path.join(R2, 'key_v2.json')))
ROUTE = [(c, d) for c, d in K['route']['order']]
CODE = K['code_words']
AFTER_TEST = {'plated': 'retreated', 'nile': 'Toland'}  # learned from .185 after the held-out test was scored


# 2. Route --------------------------------------------------------------------
def undo(tokens, rows, route=ROUTE, ncols=6, lengths=None):
    """Write cipher words back into the grid. lengths: words per column in route order (default: all = rows)."""
    grid = [[None] * ncols for _ in range(rows)]
    k = 0
    for i, (col, d) in enumerate(route):
        n = lengths[i] if lengths else rows
        rr = list(range(n - 1, -1, -1)) if d == 'u' else list(range(n))
        for r in rr:
            if k < len(tokens):
                grid[r][col - 1] = tokens[k]
                k += 1
    return grid, tokens[k:]


def encipher(grid, route=ROUTE):
    rows = len(grid)
    out = []
    for col, d in route:
        rr = range(rows - 1, -1, -1) if d == 'u' else range(rows)
        out += [grid[r][col - 1] for r in rr]
    return out


# 3. Crib: .114 grid put through the route against the .341 cipher -------------
G114 = [l.split() for l in """Fayette July second Scammon Charleston Just
reported we from out post Mrs
Miller wife soldier 13th Virginia is
there from head Paint says 40
fifth and 20 second were to
leave Lewisburg yesterday Truly yours White""".splitlines()]
C341 = ("Venus were says va post Rye sycamore reported miller there fifth leave Italy second paint thirteenth ? amazon July we "
        "wife ? and Lewisburg ?ssissipi to forty is ms just second from soldier had twenty yesterday").split()
VARIANT = {('virginia', 'va'), ('13th', 'thirteenth'), ('40', 'forty'), ('20', 'twenty'), ('mrs', 'ms'), ('head', 'had')}
pred = encipher(G114)
same = code = var = hidden = 0
for a, b in zip(pred, C341):
    al, bl = a.lower(), b.lower()
    if al == bl:
        same += 1
    elif b.startswith('?') and b != '?':
        code += 1  # partly hidden code word (Mississippi = White)
    elif b == '?':
        hidden += 1
    elif CODE.get(bl, '').lower().replace("'s", '') == al:
        code += 1
    elif (al, bl) in VARIANT:
        var += 1
print(f'.341 vs .114 through the route: {same} same word, {code} code words with the key value, {var} spelling variants, '
      f'{hidden} hidden under the repair patch (of {len(pred)})')
check((same, code, var, hidden) == (22, 6, 6, 2), '.341 crib: 34 of 36 positions agree, 2 unseen under the patch')


# 4. Held-out test (freeze/round2/TEST_PROTOCOL_v2.md), reproduced -------------
C185 = open(os.path.join(HERE, 'transcription', 'GLC02414.185.txt')).read().split('\n')
C185 = ' '.join(l for l in C185 if l and not l.startswith('#')).split()
TRUTH = [l.split() for l in """after making a thorough search of
army wagon I have to announce
that that powder and fuse are
not here Madden thinks they were
left in staff train we started
at three this morning if the
enemy has retreated and suspect our
plan it will be a close
race they having the shortest road
would like to know positively where
the enemy is going signed Toland""".splitlines()]


def sections(t):
    i = t.index('Turkey')
    return [t[1:i], t[i + 1:]]


def norm(w):
    return (w or '').lower().strip(".,'")


def gloss(w, extra=None):
    d = dict(CODE)
    if extra:
        d.update(extra)
    return d.get(norm(w), w) if w else None


def predict(route):
    rows = []
    for sec in sections(C185):
        rows += undo(sec, len(sec) // 6, route)[0]
    return rows


def score(rows):
    hit = tot = 0
    for pr, tr in zip(rows, TRUTH):
        for p, t in zip(pr, tr):
            tot += 1
            hit += norm(gloss(p)).replace("'s", '') == norm(t).replace("'s", '')
    return hit, tot


h, n = score(predict(ROUTE))
rng = random.Random(1863)
ctrl = []
for _ in range(200):
    p = list(range(1, 7))
    rng.shuffle(p)
    ctrl.append(score(predict([(c, rng.choice('ud')) for c in p]))[0])
res = dict(agree=h, cells=n, control_max=max(ctrl), control_median=sorted(ctrl)[100],
           controls_at_or_above=sum(c >= h for c in ctrl))
print('held-out .185:', res)
frozen = json.load(open(os.path.join(R2, 'heldout_result.json')))
check(all(res[k] == frozen[k] for k in res), 'held-out result equals freeze/round2/heldout_result.json (60 of 66; best control 40)')


# 5. Decryption grids -----------------------------------------------------------
def render(grid, extra, inferred=None):
    lines = []
    for r, row in enumerate(grid):
        cells = []
        for c, w in enumerate(row):
            if w is None:
                cells.append('[ ]')
                continue
            if inferred and (r, c) in inferred:
                cells.append(inferred[(r, c)])
                continue
            v = gloss(w, extra)
            cells.append(v if v != w or w.lower() not in UNVALUED else f'[{w}]')
        lines.append(' | '.join(cells))
    return '\n'.join(lines)


UNVALUED = {'virginia', 'missouri', 'gaol', 'bent', 'away', 'amore', 'sherry'}
T229 = ("gild they we Vermillion twenty beacon and for soak rye sycamore Jacks open fortifying front fifth Reported heard not us "
        "to soon of Coat ferry forks piney not ffine amazon July found for at in at Gilding to attack the "
        "with would did officer Second forty are apricots road we second path apple ford the packs to say them expect").split()
T229b = "doubtful and six the very sycamore thousand valley Mississippi clear take this".split()
T344 = ("lookout by still o'clock ordered to my post whistle sycamore came night cedar whistle to the road we the seen cotton two "
        "vermillion front all out amazon July within have to currants attack morning currants air mississippi citizens laying in these "
        "rain apricot last apricot third sight sent the into at whistle only on").split()
T341 = ("Venus were says va post Rye sycamore reported miller there fifth leave Italy second paint thirteenth [patch] amazon July we "
        "wife [patch] and Lewisburg Mississippi to forty is ms just second from soldier had twenty yesterday").split()
# .339, arrangement A (round 2): interlined "when not" counted, "&" not counted; second-route column one short, one empty cell.
T339A = ("signed with start important united might rye sherry I answering if direct nile proposed away interfere shall is our last "
         "amazon July saw the when not amore nile the bent please opinion before Virginia first missouri gaol movement at this on").split()
# .339, arrangement B (packaging, 13 Nov): the darker-ink "&" also counted; 42 words fill the 7 x 6 grid exactly.
T339B = T339A[:23] + ['&'] + T339A[23:]

out = {}
g, rest = undo(T341, 6)
out['GLC02414.341'] = ('6 rows (Florida); cipher words 2-37; [patch] = word hidden under the repair patch, given by .114', g, rest, {})
g, rest = undo(T229, 10)
g2, rest2 = undo(T229b, 2)
out['GLC02414.229'] = ('10 rows (Ocean) + 2 rows (turkey)', g + [[None] * 6] + g2, rest + rest2, {})
g, rest = undo(T344, 9)
out['GLC02414.344'] = ('9 rows (Wilderness)', g, rest, {})
gA, restA = undo(T339A, 7, lengths=[7, 7, 7, 6, 7, 7])
gB, restB = undo(T339B, 7)
check(len(T339B) == 42 and not restB and all(all(w for w in row) for row in gB), '.339 arrangement B fills 7 x 6 exactly')
for name, (note, grid, rest, _) in out.items():
    check(not rest, f'{name}: no words left over ({note})')

os.makedirs(os.path.join(HERE, 'decryption'), exist_ok=True)
HDR = ('# Grid rows read left to right. Code words replaced by key_v2 values; [word] = code word with no value; '
       '[ ] = empty cell.\n# Written by verify.py.\n')
for name, (note, grid, rest, _) in out.items():
    body = render([r for r in grid if any(r)], AFTER_TEST)
    if name == 'GLC02414.229':
        rows = render(grid[:10], AFTER_TEST) + '\n-- second section, commencement word "turkey" --\n' + render(grid[11:], AFTER_TEST)
        body = rows
    open(os.path.join(HERE, 'decryption', name + '.txt'), 'w').write(HDR + f'# {name}: {note}\n' + body + '\n')
inf = {(0, 0): '{Camp Piatt}', (5, 0): '[nile]'}  # the first nile does not read as Toland: left as a hole
txt = (HDR + '# GLC02414.339: 7 rows (Dacotah). {Camp Piatt} = "sherry", inferred from the heading slot and the printed form, '
       'not from a pair. nile = Toland in the signature cell comes from .185, learned after the test; the first nile (row 6) is left a hole.\n'
       '# Arrangement B (adopted at packaging, 13 Nov 2026): every written word counted, including the darker-ink "&" and the '
       'margin "when not"; 42 words, no empty cell.\n'
       + render(gB, AFTER_TEST, inf) +
       '\n\n# Arrangement A (round 2): "&" not counted; column 2 one short, so row 7 column 2 is empty.\n'
       + render(gA, AFTER_TEST, inf) + '\n')
open(os.path.join(HERE, 'decryption', 'GLC02414.339.txt'), 'w').write(txt)
g185 = predict(ROUTE)
open(os.path.join(HERE, 'decryption', 'GLC02414.185.txt'), 'w').write(
    HDR + '# GLC02414.185: 9 rows (Wilderness) + 2 rows (Turkey), frozen key only (the held-out prediction); '
    'plated and nile shown raw.\n' + '\n'.join(' | '.join(gloss(w) or '[ ]' for w in r) for r in g185) + '\n')

# 6. Share of .339 cells with a value ---------------------------------------------
for lab, g in (('A', gA), ('B', gB)):
    cells = [c for line in render(g, AFTER_TEST, inf).split('\n') for c in line.split(' | ')]
    holes = sum(c.startswith('[') for c in cells)
    print(f'.339 arrangement {lab}: {len(cells)} cells, {holes} holes (empty or unvalued); '
          f'{len(cells) - holes} with a value, of which 1 (Camp Piatt) is inferred from the heading slot')

print('result:', 'pass' if ok else 'FAIL')
sys.exit(0 if ok else 1)
