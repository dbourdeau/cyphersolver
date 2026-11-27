"""C09 (lead 1561) — single pre-registered measure. Standard library only.

    python3 mesure_c09.py <repo_gonzaga1549_dir> <work_dir>

Inputs (all frozen by SHA-256 in PREREG-C09.md before this script is run on them):
  work_dir/arb/{1546,1553,x}_ARB.txt      arbitrated shape transcriptions (project atlas names, see CONSIGNE-AVEUGLE.md)
  work_dir/CROSSWALK-C09.tsv              atlas name -> WAINUT key name (built from the 14 Nov 1549 alignment + listed extras)
  repo/wainut/key.tsv                     the key (WAINUT's working table, origin/main)
  repo/beling_march1553/spanish_enclosure.txt   reference for 1553 (paragraph split exactly as Beling's calibrate.py)
  1553 paragraphs: fixed by our line ids (PARA_LINES: page blocks and the '/' paragraph ends), see PREREG
Outputs: work_dir/MESURE-C09.json, work_dir/decode_{1546,1553,x}.txt
"""
import hashlib, json, random, re, sys, unicodedata
from pathlib import Path

REPO, WORK = Path(sys.argv[1]), Path(sys.argv[2])
HOLE = '?'
N_CONTROLS = 1000
SEED = 1561
PARAGRAPHS_W = ((1, 15), (16, 21), (22, 40), (41, 47), (48, 55), (56, 64))   # WAINUT B-lines, as Beling
LEXICON_FILES = ['13may1549_reading.txt', '14nov1549_reading.txt', '20nov1549_reading.txt', '23dec1549_reading.txt',
                 '30sep1549_reading.txt', 'wainut/reading_1548_c10r.md', 'wainut/reading_1551_c26r.md',
                 'wainut/reading_1551_c28r.md', 'wainut/reading_ch1549_1114.md', 'wainut/clear_1547_c11.txt',
                 'wainut/clear_1549_c14r.txt', 'wainut/clear_ch1549_c29r.txt', 'beling_march1553/spanish_enclosure.txt']


def norm(text):
    folded = unicodedata.normalize('NFKD', text.lower()).translate(str.maketrans('vj', 'ui'))
    return re.sub('[^a-z]', '', folded)


def load_key():
    key = {}
    for line in (REPO / 'wainut/key.tsv').read_text(encoding='utf8').splitlines():
        if line.strip() and not line.startswith('#'):
            label, value = line.split('\t')[:2]
            key[label] = HOLE if '[' in value else norm(value)
    return key


def load_crosswalk():
    cw = {}
    for line in (WORK / 'CROSSWALK-C09.tsv').read_text(encoding='utf8').splitlines():
        if line.strip() and not line.startswith('#'):
            p = line.split('\t')
            cw[p[0]] = p[1]
    return cw


CODES = {'dide': 'dide', 'mus': 'mus', 'quod': 'quod', 'gien': 'gien', 'em': 'em', 'gaces': 'gaces', 'gacez': 'gaces',
         'pollo': 'Pollo'}


def to_wainut(tok, cw):
    """Atlas token -> WAINUT key name; '' for a cancelled sign (dots below); None for unreadable."""
    t = tok.split('|')[0]
    if t in ('#', '[clair]') or t.startswith('?'):
        return None if t != '[clair]' else 'CLEAR'
    if t.startswith('{'):
        return CODES.get(t.strip('{}').lower())
    if t.endswith('-dots-below'):
        return ''
    return cw.get(t)


def read_arb(name):
    lines = []
    for line in (WORK / 'arb' / f'{name}_ARB.txt').read_text(encoding='utf8').splitlines():
        if line.strip() and not line.startswith('#'):
            p = line.split()
            lines.append((p[0], p[1:]))
    return lines


def labels_of(lines, cw):
    out = []
    for lid, toks in lines:
        for t in toks:
            w = to_wainut(t, cw)
            if w == 'CLEAR':
                continue
            out.append((lid, w))
    return out


def decode(seq, table):
    return ''.join('' if w == '' else HOLE if w is None else table.get(w, HOLE) for _, w in seq)


class Distance:
    """Myers' bit-vector Levenshtein distance to a fixed target (as in beling_march1553/calibrate.py)."""
    def __init__(self, reference):
        self.length = len(reference)
        self.high_bit = 1 << (self.length - 1)
        self.masks = {}
        for i, char in enumerate(reference):
            self.masks[char] = self.masks.get(char, 0) | (1 << i)

    def __call__(self, sequence):
        positive, negative, score = -1, 0, self.length
        for char in sequence:
            matches = self.masks.get(char, 0)
            xv = matches | negative
            xh = (((matches & positive) + positive) ^ positive) | matches
            ph = negative | ~(xh | positive)
            mh = positive & xh
            score += bool(ph & self.high_bit) - bool(mh & self.high_bit)
            ph = (ph << 1) | 1
            mh <<= 1
            positive = mh | ~(xv | ph)
            negative = ph & xv
        return score


def reference_1553():
    body = (REPO / 'beling_march1553/spanish_enclosure.txt').read_text(encoding='utf8').split('[37r]\n')[1]
    body = body.replace('[37v]', '').replace('[38r]', '')
    chunks = [s.strip() for s in re.split(r'\n\s*\n', body) if s.strip()]
    assert len(chunks) == 8
    return list(map(norm, [chunks[0], chunks[1], chunks[2] + chunks[3], chunks[4] + chunks[5], chunks[6], chunks[7]]))


PARA_LINES = (('P35r', 1, 15), ('P35v', 1, 6), ('P35v', 7, 18, 'P40r', 1, 7), ('P40r', 8, 15), ('P40r', 16, 23), ('P40v', 1, 8))


def para_of(lid):
    """Paragraph (0-5) of a 1553 line, fixed by the page blocks and the '/' paragraph ends of the cipher (PREREG)."""
    page, n = lid.split('-L')[0], int(lid.split('-L')[1])
    for i, spec in enumerate(PARA_LINES):
        for k in range(0, len(spec), 3):
            if page == spec[k] and spec[k + 1] <= n <= spec[k + 2]:
                return i
    raise ValueError(lid)


def lexicon():
    words = set()
    for f in LEXICON_FILES:
        p = REPO / f
        if p.exists():
            for w in re.findall(r"[A-Za-zÀ-ÿ]+", p.read_text(encoding='utf8')):
                n = norm(w)
                if len(n) >= 3:
                    words.add(n)
    return words


def coverage(text, words, maxlen=16, minlen=4):
    """Share of letters covered by lexicon words (>= 4 letters), best non-overlapping cover (DP)."""
    n = len(text)
    best = [0] * (n + 1)
    for i in range(1, n + 1):
        best[i] = best[i - 1]
        for L in range(minlen, min(maxlen, i) + 1):
            if text[i - L:i] in words:
                best[i] = max(best[i], best[i - L] + L)
    return best[n] / n if n else 0.0


def shuffled_tables(key, rng):
    labels = sorted(l for l, v in key.items() if v not in ('', HOLE))
    values = [key[l] for l in labels]
    while True:
        perm = values[:]
        rng.shuffle(perm)
        t = dict(key)
        t.update(zip(labels, perm))
        yield t


def main():
    key, cw = load_key(), load_crosswalk()
    res = {'key_sha256': hashlib.sha256((REPO / 'wainut/key.tsv').read_bytes()).hexdigest(), 'controls': N_CONTROLS, 'seed': SEED}
    seqs = {n: labels_of(read_arb(n), cw) for n in ('1546', '1553', 'x')}
    for n, s in seqs.items():
        (WORK / f'decode_{n}.txt').write_text(decode(s, key) + '\n', encoding='utf8')
        res[f'{n}_tokens'] = len(s)
        res[f'{n}_unmapped'] = sum(1 for _, w in s if w is None)
    # --- 1553: held-out paragraphs 4-6 against the Spanish enclosure (primary) ---
    plain = reference_1553()
    seq = seqs['1553']
    segs = [[x for x in seq if para_of(x[0]) == i] for i in range(6)]
    res['1553_paragraph_tokens'] = [len(x) for x in segs]
    metrics = [Distance(p) for p in plain]
    held = [3, 4, 5]
    def edits(table, idx):
        return sum(metrics[i](decode(segs[i], table).replace(HOLE, '')) for i in idx)
    real = edits(key, held)
    letters = sum(len(plain[i]) for i in held)
    rng = random.Random(SEED)
    gen = shuffled_tables(key, rng)
    ctrl = [edits(next(gen), held) for _ in range(N_CONTROLS)]
    # second control family: the same tokens in shuffled order inside each paragraph, real key (keeps sign frequencies)
    rng2 = random.Random(SEED + 10)
    ctrl2 = []
    for _ in range(N_CONTROLS):
        tot = 0
        for i in held:
            sh = segs[i][:]
            rng2.shuffle(sh)
            tot += metrics[i](decode(sh, key).replace(HOLE, ''))
        ctrl2.append(tot)
    res['1553_heldout'] = {'letters': letters, 'edits': real, 'CER': round(real / letters, 4),
                           'keyshuffle_best_edits': min(ctrl), 'keyshuffle_median_edits': sorted(ctrl)[N_CONTROLS // 2],
                           'keyshuffle_ties_or_wins': sum(c <= real for c in ctrl),
                           'ordershuffle_best_edits': min(ctrl2), 'ordershuffle_median_edits': sorted(ctrl2)[N_CONTROLS // 2],
                           'ordershuffle_ties_or_wins': sum(c <= real for c in ctrl2),
                           'wainut_baseline_edits_beling': 621,
                           'pass_key': sum(c <= real for c in ctrl) == 0 and sum(c <= real for c in ctrl2) == 0,
                           'beats_wainut_baseline': real < 621}
    res['1553_fitpart_secondary'] = {'letters': sum(len(plain[i]) for i in (0, 1, 2)), 'edits': edits(key, (0, 1, 2))}
    # --- 1546 and x: lexicon coverage against shuffled keys ---
    words = lexicon()
    res['lexicon_words'] = len(words)
    for n in ('1546', 'x'):
        txt = decode(seqs[n], key).replace(HOLE, '')
        real = coverage(txt, words)
        rng = random.Random(SEED + (1 if n == '1546' else 2))
        gen = shuffled_tables(key, rng)
        ctrl = [coverage(decode(seqs[n], next(gen)).replace(HOLE, ''), words) for _ in range(N_CONTROLS)]
        rng2 = random.Random(SEED + (11 if n == '1546' else 12))
        ctrl2 = []
        for _ in range(N_CONTROLS):
            sh = seqs[n][:]
            rng2.shuffle(sh)
            ctrl2.append(coverage(decode(sh, key).replace(HOLE, ''), words))
        res[f'{n}_coverage'] = {'real': round(real, 4), 'keyshuffle_max': round(max(ctrl), 4),
                                'keyshuffle_median': round(sorted(ctrl)[N_CONTROLS // 2], 4),
                                'keyshuffle_ties_or_wins': sum(c >= real for c in ctrl),
                                'ordershuffle_max': round(max(ctrl2), 4), 'ordershuffle_median': round(sorted(ctrl2)[N_CONTROLS // 2], 4),
                                'ordershuffle_ties_or_wins': sum(c >= real for c in ctrl2),
                                'pass_key': sum(c >= real for c in ctrl) == 0 and sum(c >= real for c in ctrl2) == 0}
    (WORK / 'MESURE-C09.json').write_text(json.dumps(res, indent=1) + '\n', encoding='utf8')
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
