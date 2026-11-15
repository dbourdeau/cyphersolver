"""Settle, from Casgrain's printed clear text, the cells of the frozen table that his four letters use and that are
doubtful, illegible, off the photograph, or shown to be misread; and measure the decodes before and after.

The frozen table (key/table_e001295272.tsv) is not changed. This script:

1. Aligns, for each letter, the printed figures (letters/<L>.tr) with Casgrain's printed clear text, by dynamic
   programming over (group, position in the clear text). A clear cell costs nothing when its reading matches the
   text and 1.2 per edit when it does not; a doubtful cell may take any 1-10 letter value at a cost of 0.8 + 0.1 per
   letter (or half its edit distance from the frozen reading or an alternative, if smaller); an illegible cell or a
   cell off the photograph may take any 1-10 letter value at 0.8 + 0.1 per letter; skipping a letter of the clear
   text costs 1.0. The value implied for each occurrence of a cell is the stretch of clear text aligned with it.
   Writes results/casgrain_implied_values.tsv (every occurrence of every cell that is doubtful, illegible, off the
   photograph, in key/corrections_post_freeze.tsv, or clear but aligned with a different value).

2. With --measure, reads key/table_settled_from_casgrain.tsv (written by hand after looking at the image) and reports,
   for the frozen table and for the frozen table with the settled values put in:
   - whole words: a word of Casgrain's clear text counts only if every letter of it is matched, in the alignment of
     decode and clear text, by letters that come from cells counted as clear (Daniel Bourdeau's measure on #583);
     "with doubtful" also counts doubtful cells;
   - letter similarity: difflib ratio of decode and clear text, as decode_letters.py computes it.
   Writes results/settled_measures.json.

Run from the repository root:  python targets/montcalm1758i/settle_from_casgrain.py [--measure]
"""
import csv, difflib, json, pathlib, sys
from functools import lru_cache

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from decode_letters import LETTERS, norm, load_table, parse, join_clear  # noqa: E402

MAXLEN = 10


@lru_cache(maxsize=None)
def ed(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def load_alts():
    alts = {}
    with open(HERE / 'key' / 'table_e001295272.tsv', encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            alts[int(row['cell'])] = [norm(a) for a in row['alternatives'].split('|') if a.strip()]
    return alts


def tokens_of(paras):
    """Flat token list: ('g', cell) or ('w', clear word printed among the figures)."""
    return [t for p in paras for t in p['groups']]


def cost_fn(tok, table, alts):
    kind, t = tok
    if kind == 'w':
        v = norm(t)
        return lambda s: 1.0 * ed(v, s) if s else 0.5 * len(v)
    if not 21 <= t <= 700 or table[t][1] == 'illegible':
        return lambda s: (0.8 + 0.1 * len(s)) if s else 1.5
    v, st = norm(table[t][0]), table[t][1]
    if st == 'clear':
        return lambda s: 1.2 * ed(v, s) if s else 1.2 * len(v)
    cands = [v] + alts.get(t, [])
    return lambda s: min([0.8 + 0.1 * len(s)] + [0.5 * ed(c, s) for c in cands]) if s else 1.5


def align(toks, ref, table, alts):
    """Return list of (token, start, end) spans of ref aligned with each token."""
    n, m = len(toks), len(ref)
    INF = float('inf')
    fns = [cost_fn(t, table, alts) for t in toks]
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0.0
    for j in range(1, m + 1):
        D[0][j] = D[0][j - 1] + 1.0
        B[0][j] = ('skip',)
    for i in range(1, n + 1):
        f = fns[i - 1]
        Di, Dp, Bi = D[i], D[i - 1], B[i]
        for j in range(0, m + 1):
            best, bk = INF, None
            if j > 0 and Di[j - 1] + 1.0 < best:
                best, bk = Di[j - 1] + 1.0, ('skip',)
            for k in range(0, min(MAXLEN, j) + 1):
                c = Dp[j - k]
                if c == INF or c >= best:
                    continue
                c += f(ref[j - k:j])
                if c < best:
                    best, bk = c, ('tok', k)
            Di[j], Bi[j] = best, bk
    spans, i, j = [], n, m
    while i > 0 or j > 0:
        b = B[i][j]
        if b[0] == 'skip':
            j -= 1
        else:
            k = b[1]
            spans.append((toks[i - 1], j - k, j))
            i -= 1
            j -= k
    return spans[::-1]


def letter_ref(paras):
    return ''.join(norm(join_clear(p['clear'])) for p in paras)


def load_corrections():
    out = {}
    with open(HERE / 'key' / 'corrections_post_freeze.tsv', encoding='utf-8') as f:
        rows = [ln for ln in f if not ln.startswith('#')]
    for row in csv.DictReader(rows, delimiter='\t'):
        out[int(row['cell'])] = row['context_value']
    return out


def implied():
    table, alts, corr = load_table(), load_alts(), load_corrections()
    rows = []
    for L in LETTERS:
        paras = parse(HERE / 'letters' / (L + '.tr'))
        ref = letter_ref(paras)
        spans = align(tokens_of(paras), ref, table, alts)
        gi = 0
        for (kind, t), a, b in spans:
            if kind != 'g':
                continue
            gi += 1
            on = 21 <= t <= 700
            st = table[t][1] if on else 'off-photograph'
            if not on and table.get(t, ('', ''))[1] == 'illegible':
                st = 'off-photograph'
            fr = table[t][0] if t in table else '?'
            val = ref[a:b]
            ctx = ref[max(0, a - 12):a] + '[' + val + ']' + ref[b:b + 12]
            interesting = st != 'clear' or t in corr or (val != norm(fr))
            if interesting:
                rows.append((t, fr, st, L, gi, val, ctx))
    rows.sort(key=lambda r: (r[0], r[3], r[4]))
    with open(HERE / 'results' / 'casgrain_implied_values.tsv', 'w', encoding='utf-8') as f:
        f.write('# Every occurrence, in Casgrain\'s four letters, of a cell that is doubtful, illegible, off the photograph,\n'
                '# listed in key/corrections_post_freeze.tsv, or clear but aligned with different clear text.\n'
                '# group = position of the group in the letter (1-based, figures only). implied = normalised clear text\n'
                '# aligned with the group by settle_from_casgrain.py; context = 12 letters either side.\n')
        f.write('cell\tfrozen_reading\tfrozen_status\tletter\tgroup\timplied\tcontext\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')
    print(len(rows), 'occurrences written')


def word_measure(dec_chars, ref_text_words, ok_status):
    """dec_chars: list of (char, status). ref words: list of normalised words, concatenated = reference."""
    dec = ''.join(c for c, _ in dec_chars)
    ref = ''.join(ref_text_words)
    good = [False] * len(ref)
    sm = difflib.SequenceMatcher(None, dec, ref, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            for k in range(i2 - i1):
                if dec_chars[i1 + k][1] in ok_status:
                    good[j1 + k] = True
    n_ok, pos = 0, 0
    for w in ref_text_words:
        if w and all(good[pos:pos + len(w)]):
            n_ok += 1
        pos += len(w)
    return n_ok, sum(1 for w in ref_text_words if w), difflib.SequenceMatcher(None, dec, ref, autojunk=False).ratio()


def decode_chars(paras, table, settled):
    out = []
    for p in paras:
        for kind, t in p['groups']:
            if kind == 'w':
                out += [(c, 'clear') for c in norm(t)]
                continue
            if t in settled:
                v, st = settled[t]
            elif 21 <= t <= 700 and table[t][1] != 'illegible':
                v, st = table[t]
            else:
                continue
            out += [(c, st) for c in norm(v)]
    return out


def measure():
    table = load_table()
    settled = {}
    with open(HERE / 'key' / 'table_settled_from_casgrain.tsv', encoding='utf-8') as f:
        rows = [ln for ln in f if not ln.startswith('#')]
    for row in csv.DictReader(rows, delimiter='\t'):
        settled[int(row['cell'])] = (row['casgrain_value'], row['status'])
    good_settled = {c: (v, 'clear') for c, (v, st) in settled.items()
                    if st in ('confirmed on image', 'image permits')}
    all_settled = {c: (v, 'clear') for c, (v, st) in settled.items()}
    res = {}
    for L in LETTERS:
        paras = parse(HERE / 'letters' / (L + '.tr'))
        # words split on white space only (as in Daniel's count: 122, 31, 233, 371 words)
        words = [norm(w) for p in paras for w in join_clear(p['clear']).split()]
        words = [w for w in words if w]
        r = {}
        for name, s in (('frozen', {}), ('settled_image_ok', good_settled), ('settled_all', all_settled)):
            dc = decode_chars(paras, table, s)
            a, n, sim = word_measure(dc, words, {'clear'})
            b, _, _ = word_measure(dc, words, {'clear', 'doubtful'})
            r[name] = {'words': n, 'whole_words_clear_cells': a, 'pct_clear': round(100 * a / n, 1),
                       'whole_words_with_doubtful': b, 'pct_with_doubtful': round(100 * b / n, 1),
                       'letter_similarity': round(sim, 3)}
        res[L] = r
        print(L, json.dumps(r))
    (HERE / 'results' / 'settled_measures.json').write_text(json.dumps(res, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    if '--measure' in sys.argv:
        measure()
    else:
        implied()
