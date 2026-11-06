"""Align a hand reading of R91 with the digit stream under key 2, token by token.

Reading file (reading.txt): lines '<folio.line> <text>'; the text runs on across lines (a word may break at a
line end). In the text:
  ordinary words      letters a-z (j=i, v=u; accents and punctuation ignored); must be produced by the key
  word[?]             an uncertain reading: aligned like any word, counted separately
  {d d d}             digits left unread (written as they stand in the stream, '?' for a lost digit)
  |                   optional: where a null 11 stands (ignored by the aligner, which finds nulls itself)
The aligner finds the cheapest derivation: a code (1 or 2 digits) giving its plain or dotted value (a dotted value
on a position the re-read shows undotted, or the reverse, costs 1), a null 11 (cost 0), a skipped uncertain or lost
digit (cost 1), or an emendation (one digit read as another digit's value, cost 4, listed). It reports the first
place where no derivation exists.

  python align91.py [reading.txt] [--key k2b] [--tsv validation.tsv] [--measure]
"""
import argparse, importlib, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import vdot

# Meister p. 177, key no. 2: three-digit code words printed beside N.S. and S.M.ta (added 2026-11-05, third pass)
EXTRA = {'000': ['francia']}

NORM = str.maketrans('jvàáâèéêìíîòóôùúûç', 'iuaaaeeeiiiooouuuc')


def parse_reading(path):
    """Returns list of items: ('w', letters, uncertain, line) or ('u', [digit tokens], line); and line order."""
    items = []
    for raw in open(path, encoding='utf-8'):
        raw = raw.rstrip('\n')
        if not raw.strip() or raw.startswith('#'):
            continue
        lab, _, text = raw.partition(' ')
        for m in re.finditer(r'\{([^}]*)\}|([^\s{}|]+)|\|', text):
            if m.group(1) is not None:
                items.append(('u', m.group(1).split(), lab))
            elif m.group(2):
                w = m.group(2)
                unc = w.endswith('[?]')
                w = w.replace('[?]', '').lower().translate(NORM)
                w = re.sub(r'[^a-z]', '', w)
                if w:
                    items.append(('w', w, unc, lab))
    return items


def build_options(key):
    plain = {c: list(v) for c, v in key.items()}
    for c in vdot.DOTTED:
        if c in plain:
            plain[c] = [v for v in plain[c] if v not in vdot.DOTTED[c]]
    return plain, vdot.DOTTED


def align(items, key, D):
    plain, dotted = build_options(key)
    flat = [t for _, ts, _ in D.S for t in ts]       # (digit or -1, dotted_flag, unsure)
    n = len(flat)
    dotp = D.dotp
    # target sequence: letters with word ids, and unread spans
    tgt = []          # each element: ('c', ch, item_index) or ('U', ndigits, item_index)
    for k, it in enumerate(items):
        if it[0] == 'w':
            for ch in it[1]:
                tgt.append(('c', ch, k))
        else:
            tgt.append(('U', len(it[1]), k))
    m = len(tgt)
    INF = 10 ** 9
    states = [dict() for _ in range(n + 1)]      # states[i][j] = (cost, back)
    states[0][0] = (0, None)

    def relax(i, j, i2, j2, c, info):
        if i2 > n or j2 > m:
            return
        nc = states[i][j][0] + c
        old = states[i2].get(j2)
        if old is None or nc < old[0]:
            states[i2][j2] = (nc, (i, j, info))

    def matches(j, s):
        if j + len(s) > m:
            return False
        for q, ch in enumerate(s):
            t = tgt[j + q]
            if t[0] != 'c' or t[1] != ch:
                return False
        return True

    digs = [t[0] for t in flat]
    for i in range(n + 1):
        if len(states[i]) > 400:                   # prune: keep the cheapest states
            states[i] = dict(sorted(states[i].items(), key=lambda kv: kv[1][0])[:400])
        for j in list(states[i]):
            if i == n:
                continue
            d = digs[i]
            # unread span
            if j < m and tgt[j][0] == 'U':
                L = tgt[j][1]
                relax(i, j, i + L, j + 1, 0, ('U', L, tgt[j][2]))
            # lost or uncertain digit skipped
            if d < 0 or flat[i][2]:
                relax(i, j, i + 1, j, 1, ('skip', 1, None))
            if d < 0:
                continue
            for L in (1, 2):
                if i + L > n:
                    break
                if L == 2 and digs[i + 1] < 0:
                    break
                c = str(d) if L == 1 else f'{d}{digs[i + 1]}'
                for o in plain.get(c, []):
                    pen = 1 if (L == 2 and dotp[i] == 1 and c in dotted) else 0
                    if o == '':
                        relax(i, j, i + L, j, pen, ('code', c, ''))
                    elif matches(j, o):
                        relax(i, j, i + L, j + len(o), pen, ('code', c, o))
                if L == 2 and c in dotted:
                    for o in dotted[c]:
                        pen = 1 if dotp[i] == 0 else 0
                        if matches(j, o):
                            relax(i, j, i + L, j + len(o), pen, ('code', "'" + c, o))
            # three-digit code words (EXTRA), e.g. 000 = Francia
            if i + 3 <= n and min(digs[i:i + 3]) >= 0:
                c3 = ''.join(map(str, digs[i:i + 3]))
                for o in EXTRA.get(c3, []):
                    if matches(j, o):
                        relax(i, j, i + 3, j + len(o), 0, ('code', c3, o))
            # emendation of one digit inside a two-digit code (e.g. 8 7 read as 88): any code differing in one digit
            if i + 1 < n and digs[i + 1] >= 0 and j < m and tgt[j][0] == 'c':
                c0 = f'{d}{digs[i + 1]}'
                for c2 in list(plain) + [x for x in dotted]:
                    if len(c2) != 2 or c2 == c0 or sum(a != b for a, b in zip(c2, c0)) != 1:
                        continue
                    for o in plain.get(c2, []) + dotted.get(c2, []):
                        if o and matches(j, o):
                            relax(i, j, i + 2, j + len(o), 4, ('emend', f'{c0}>{c2}', o))
            # emendation: one digit read as any single-letter value of another digit
            if j < m and tgt[j][0] == 'c':
                for e in '0123456789':
                    if e != str(d) and tgt[j][1] in plain.get(e, []):
                        relax(i, j, i + 1, j + 1, 4, ('emend', f'{d}>{e}', tgt[j][1]))
    if m not in states[n]:
        best_j, best_i = 0, 0
        for i in range(n + 1):
            for j in states[i]:
                if j > best_j:
                    best_j, best_i = j, i
        its = sorted(set(tgt[q][2] for q in range(max(0, best_j - 3), min(m, best_j + 3))))
        ctx = ' '.join(items[k][1] if items[k][0] == 'w' else '{..}' for k in its)
        return None, f'no derivation past target letter {best_j} near "{ctx}" (digit {best_i}, line {line_of(D, best_i)})'
    path = []
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, info = states[i][j][1]
        path.append((pi, i, pj, j, info))
        i, j = pi, pj
    return path[::-1], states[n][m][0]


def line_of(D, idx):
    pos = 0
    for name, ts, _ in D.S:
        if idx < pos + len(ts):
            return f'{name} pos {idx - pos + 1}'
        pos += len(ts)
    return 'end'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('reading', nargs='?', default=os.path.join(HERE, 'reading.txt'))
    ap.add_argument('--key', default='k2d')
    ap.add_argument('--tsv', default=None)
    a = ap.parse_args()
    key = {k: list(v) for k, v in importlib.import_module(a.key).KEY.items()}
    items = parse_reading(a.reading)
    D = vdot.Dec(only=set(it[-1] for it in items))
    path, info = align(items, key, D)
    if path is None:
        print('FAIL:', info); sys.exit(1)
    flat = [t for _, ts, _ in D.S for t in ts]
    n = len(flat)
    # per-token status: read (word certain), uncertain, unread, null, skipped
    status = [''] * n
    emends = []
    tok_item = [None] * n
    for pi, i, pj, j, inf in path:
        kind = inf[0]
        for q in range(pi, i):
            if kind == 'U':
                status[q] = 'unread'
            elif kind == 'skip':
                status[q] = 'lost' if flat[q][0] < 0 else 'skipped'
            elif kind == 'emend':
                status[q] = 'emend'; emends.append((q, inf[1], inf[2]))
            elif inf[2] == '':
                status[q] = 'null'
            else:
                status[q] = 'word'
        if kind in ('code', 'emend') and inf[2]:
            # item of first letter
            k = None
    # map word tokens to uncertain items
    # recompute: the item for each consumed letter
    tgt_item = []
    for k, it in enumerate(items):
        if it[0] == 'w':
            tgt_item += [k] * len(it[1])
        else:
            tgt_item.append(k)
    unc_tokens = 0
    for pi, i, pj, j, inf in path:
        if inf[0] in ('code', 'emend') and inf[2] and pj < len(tgt_item):
            it = items[tgt_item[pj]]
            if it[0] == 'w' and it[2]:
                for q in range(pi, i):
                    status[q] = 'uncertain'
    c = Counter(status)
    digits = sum(1 for t in flat if t[0] >= 0)
    lost = sum(1 for t in flat if t[0] < 0)
    read = c['word'] + c['null']
    print(f'tokens (digits) {digits}, lost holes {lost}')
    print('status:', dict(c))
    sense = c['word'] + c['null'] + c['uncertain'] + c['emend']
    print(f'read as sense (certain words + nulls): {read}/{digits} = {read / digits:.3f}')
    print(f'incl. uncertain words and emended digits: {sense}/{digits} = {sense / digits:.3f}')
    print(f'alignment cost {info}; emendations {len(emends)}:', ' '.join(f'{q}:{e}={v}' for q, e, v in emends[:40]))
    if a.tsv:
        with open(a.tsv, 'w', encoding='utf-8') as f:
            f.write('# model: it-cinquecento\n# source: reading.txt aligned by align91.py\n')
            for pi, i, pj, j, inf in path:
                if inf[0] == 'code':
                    f.write(f"{inf[1].lstrip(chr(39))}\t{inf[2] if inf[2] else '-'}\n")
                elif inf[0] == 'U':
                    for q in range(pi, i):
                        f.write(f'{flat[q][0]}\t?\n')
                elif inf[0] == 'emend':
                    f.write(f"{inf[1].split('>')[0]}\t?\n")


if __name__ == '__main__':
    main()
