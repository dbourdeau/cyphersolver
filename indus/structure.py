"""Toward a reading: the structural layer of the Indus texts, the step that came before
phonetic values in Linear B (Kober's inflected 'triplets') and proto-cuneiform (its
numeral systems). Meaning classes, not sounds.

S1  Numeral systems. Short strokes (1-5 in one row), tiered strokes (13-19: 3 = 2 over 1,
    6 = 3 over 3 ...) and long strokes (31-36). Do they count the same things? Compare the
    signs that follow each series (Jensen-Shannon divergence, permutation of series labels).
S2  Counted nouns: signs that follow numerals more often than chance, i.e. what is counted.
S3  Endings (Kober). The text-final sign class, and 'stems' (the text minus its final 1-2
    signs) attested with two or more different endings: paradigms like Kober's triplets.
S4  Name + formula on the incised copper tablets: recurring tails shared by tablets with
    different images, and what stands before them.
S5  Word segmentation: cut each line where the pair cohesion (PMI) is low, and list the
    commonest resulting units.

Usage: python structure.py            (ICIT-derived corpus)
Writes results/structure.md.
"""
import math
import os
import random
from collections import Counter, defaultdict

from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(11)
OUT = []

SHORT = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '7': 7}
TIERED = {'13': 3, '14': 4, '15': 5, '16': 6, '17': 7, '18': 8, '19': 8, '55': 12}
LONG = {'31': 1, '32': 2, '33': 3, '34': 4, '35': 5, '36': 6}
NUM = {**SHORT, **TIERED, **LONG}


def say(s=''):
    OUT.append(s)
    print(s)


def lines_of(rows):
    return [ln for r in rows for ln in r['seq']]


def js(p, q):
    keys = set(p) | set(q)
    sp, sq = sum(p.values()), sum(q.values())
    d = 0.0
    for k in keys:
        a, b = p[k] / sp, q[k] / sq
        m = (a + b) / 2
        if a:
            d += 0.5 * a * math.log2(a / m)
        if b:
            d += 0.5 * b * math.log2(b / m)
    return d


def s1_s2(lines):
    say('## S1 Numeral systems: do short, tiered and long strokes count the same things?')
    say()
    follow = {'short': Counter(), 'tiered': Counter(), 'long': Counter()}
    events = []
    for ln in lines:
        for a, b in zip(ln, ln[1:]):
            if a in NUM and b not in NUM:
                s = 'short' if a in SHORT else 'tiered' if a in TIERED else 'long'
                follow[s][b] += 1
                events.append((s, b))
    for s, c in follow.items():
        say('- %s strokes (%d tokens before a non-numeral): %s' % (
            s, sum(c.values()), ', '.join('%s x%d' % kv for kv in c.most_common(10))))
    obs = js(follow['short'], follow['long'])
    labels = [s for s, _ in events]
    ge = 0
    for _ in range(1000):
        random.shuffle(labels)
        a, b = Counter(), Counter()
        for s, (_, g) in zip(labels, events):
            if s == 'short':
                a[g] += 1
            elif s == 'long':
                b[g] += 1
        ge += js(a, b) >= obs
    say('- short vs long: Jensen-Shannon divergence of the following signs %.3f bits; label '
        'permutations as large: %d of 1000.' % (obs, ge))
    top = lambda c: {g for g, _ in c.most_common(8)}
    for lab, A, B in (('values 1, 3, 4, 5 only (both pairs left out)', {'1', '3', '4', '5'}, {'31', '33', '34', '35'}),):
        a, b, ev = Counter(), Counter(), []
        for ln in lines:
            for x, y in zip(ln, ln[1:]):
                if y in NUM:
                    continue
                if x in A:
                    a[y] += 1
                    ev.append(('s', y))
                elif x in B:
                    b[y] += 1
                    ev.append(('l', y))
        o2 = js(a, b)
        lab2 = [e for e, _ in ev]
        g2 = 0
        for _ in range(1000):
            random.shuffle(lab2)
            p, q = Counter(), Counter()
            for e, (_, y) in zip(lab2, ev):
                (p if e == 's' else q)[y] += 1
            g2 += js(p, q) >= o2
        say('- %s: short (%d) before %s; long (%d) before %s; divergence %.3f bits, permutations as '
            'large %d of 1000.' % (lab, sum(a.values()), ', '.join('%s x%d' % kv for kv in a.most_common(6)),
                                   sum(b.values()), ', '.join('%s x%d' % kv for kv in b.most_common(6)), o2, g2))
    say('- among the 8 commonest nouns after each: short only %s; long only %s; both %s.' % (
        sorted(top(follow['short']) - top(follow['long']), key=int),
        sorted(top(follow['long']) - top(follow['short']), key=int),
        sorted(top(follow['short']) & top(follow['long']), key=int)))
    say()
    say('## S2 Counted nouns: signs read after a numeral more often than chance')
    say()
    first, second, nb = Counter(), Counter(), 0
    pair = Counter()
    for ln in lines:
        for a, b in zip(ln, ln[1:]):
            first[a] += 1
            second[b] += 1
            pair[a, b] += 1
            nb += 1
    nfirst = sum(first[a] for a in NUM)
    rows = []
    for b in second:
        if b in NUM:
            continue
        o = sum(pair[a, b] for a in NUM)
        e = nfirst * second[b] / nb
        if o >= 8 and o > 2 * e:
            vals = sorted({NUM[a] for a in NUM if pair[a, b]})
            rows.append((o / e, b, o, e, second[b], vals))
    say('| sign | after a numeral | expected | all occurrences as 2nd of a pair | share | values seen |')
    say('|---|---|---|---|---|---|')
    for ratio, b, o, e, n, vals in sorted(rows, reverse=True):
        say('| %s | %d | %.1f | %d | %.0f%% | %s |' % (b, o, e, n, 100 * o / n, vals))
    say()


def s3(lines):
    say('## S3 Endings and paradigms (Kober)')
    say()
    fin = Counter(ln[-1] for ln in lines if len(ln) >= 2)
    tot = Counter(g for ln in lines for g in ln)
    enders = [(g, c, c / tot[g]) for g, c in fin.items() if tot[g] >= 30 and c / tot[g] >= 0.5]
    say('- signs that end a line in half or more of their occurrences (>= 30 tokens): ' + ', '.join(
        '%s (%d of %d, %.0f%%)' % (g, c, tot[g], 100 * s) for g, c, s in sorted(enders, key=lambda x: -x[1])))
    starters = Counter(ln[0] for ln in lines if len(ln) >= 2)
    st = [(g, c, c / tot[g]) for g, c in starters.items() if tot[g] >= 30 and c / tot[g] >= 0.5]
    say('- signs that begin a line in half or more of their occurrences: ' + ', '.join(
        '%s (%d of %d)' % (g, c, tot[g]) for g, c, s in sorted(st, key=lambda x: -x[1])))
    # endings: final 1 or 2 signs drawn from the ender class (+ the jar-group)
    END = {g for g, _, _ in enders} | {'740', '741', '742', '745'}
    stems = defaultdict(Counter)
    for ln in lines:
        k = len(ln)
        while k > 0 and ln[k - 1] in END and len(ln) - k < 2:
            k -= 1
        if 0 < k < len(ln) and k >= 2:
            stems[' '.join(ln[:k])][' '.join(ln[k:])] += 1
        elif k == len(ln) and k >= 2:
            stems[' '.join(ln)]['(none)'] += 1
    para = [(s, c) for s, c in stems.items() if len(c) >= 2]
    say('- ending class used: %s. Stems (the line minus up to two final ending signs, at least two '
        'signs long) attested with two or more different endings: %d of %d stems.' % (
            ' '.join(sorted(END, key=int)), len(para), len(stems)))
    ends = Counter(e for _, c in para for e in c)
    say('- endings that alternate on the same stem: ' + ', '.join('%s x%d' % kv for kv in ends.most_common(12)))
    say()
    say('| stem (reading order) | endings attested (count) |')
    say('|---|---|')
    for s, c in sorted(para, key=lambda x: (-len(x[1]), -sum(x[1].values())))[:25]:
        say('| %s | %s |' % (s, '; '.join('%s x%d' % kv for kv in c.most_common())))
    say()


def s4(rows):
    say('## S4 Name + formula on the copper tablets')
    say()
    tabs = [r for r in rows if r['type'] == 'TAB:C']
    texts = Counter(' '.join(r['flat']) for r in tabs)
    motif = defaultdict(Counter)
    for r in tabs:
        motif[' '.join(r['flat'])][r['motif'] or '-'] += 1
    tails = Counter()
    for t in texts:
        s = t.split()
        for k in range(2, 5):
            for i in range(len(s) - k + 1):
                tails[' '.join(s[i:i + k])] += 1
    shared = [(k, n) for k, n in tails.items() if n >= 3]
    say('Copper tablets: %d objects, %d distinct texts. Sign sequences (2-4 signs) found in 3 or '
        'more distinct texts, with what stands before them and the images of those tablets:' % (
            len(tabs), len(texts)))
    say()
    for k, n in sorted(shared, key=lambda x: (-x[1], -len(x[0]))):
        if any(k != k2 and k in k2 and tails[k2] == n for k2, _ in shared):
            continue            # report only the longest form of each shared sequence
        say('- **%s** in %d texts:' % (k, n))
        for t, c in texts.most_common():
            if (' ' + k + ' ') in (' ' + t + ' '):
                pre = t[:(' ' + t + ' ').index(' ' + k + ' ')].strip() or '(nothing)'
                say('    - %s  [ %s ] %s  (x%d; images %s)' % (pre, k, t[len(pre):].replace(k, '', 1).strip()
                                                           if pre != '(nothing)' else t[len(k):].strip(),
                                                           c, dict(motif[t])))
    say()


def s4b(rows):
    say('## S4b The formula 845 (61) 407 and what precedes it')
    say()
    distinct = {}
    for r in rows:
        s = r['flat']
        for i in range(len(s) - 1):
            j = i + 1 if s[i + 1] == '407' else (i + 2 if i + 2 < len(s) and s[i + 2] == '407' else None)
            if s[i] == '845' and j is not None:
                distinct.setdefault(' '.join(s), []).append((r['cisi'] or r['sealid'], r['type'], r['motif']))
                break
    mark = FISH | {'806'}
    hits = 0
    for t, objs in distinct.items():
        pre = t.split(' 845 ')[0].split()
        has = any(g in mark for g in pre)
        hits += has
        say('- %s   | before the formula: %s | %d object(s): %s' % (
            t, 'fish-series or 806 sign' if has else 'none', len(objs),
            ', '.join('%s %s %s' % o for o in objs[:4])))
    # baseline: in texts of the corpus, how often does a random prefix of the same length hold such a sign
    pre_lens = [len(t.split(' 845 ')[0].split()) for t in distinct]
    texts = [r['flat'] for r in rows if len(r['flat']) >= 3]
    base = []
    for _ in range(4000):
        L = random.choice(pre_lens)
        s = random.choice(texts)
        if len(s) <= L:
            continue
        i = random.randrange(0, len(s) - L)
        base.append(any(g in mark for g in s[i:i + L]))
    p0 = sum(base) / len(base)
    pr = sum(math.comb(len(distinct), k) * p0 ** k * (1 - p0) ** (len(distinct) - k)
             for k in range(hits, len(distinct) + 1))
    say()
    say('- distinct texts with the formula: %d; the phrase before it holds a fish-series sign or the '
        'leaf-in-oval 806 in %d. A random stretch of the same length from the corpus holds one with '
        'probability %.2f; binomial p of %d or more: %.1e.' % (len(distinct), hits, p0, hits, pr))
    say()


def s5(lines):
    say('## S5 Word segmentation by pair cohesion')
    say()
    uni = Counter(g for ln in lines for g in ln)
    pair = Counter((a, b) for ln in lines for a, b in zip(ln, ln[1:]))
    N = sum(uni.values())
    NP = sum(pair.values())

    def pmi(a, b):
        return math.log2((pair[a, b] / NP) / ((uni[a] / N) * (uni[b] / N))) if pair[a, b] else -9

    units = Counter()
    cuts = 0
    for ln in lines:
        cur = [ln[0]]
        for a, b in zip(ln, ln[1:]):
            if pmi(a, b) < 2.0 or pair[a, b] < 3:
                units[' '.join(cur)] += 1
                cur = [b]
                cuts += 1
            else:
                cur.append(b)
        units[' '.join(cur)] += 1
    multi = [(u, c) for u, c in units.items() if ' ' in u and c >= 6]
    say('Rule: cut between two signs unless the pair occurs 3+ times with PMI >= 2 bits (at least '
        'four times its chance rate). %d lines, %d cuts, %d distinct units; units of 2+ signs '
        'occurring 6+ times: %d.' % (len(lines), cuts, len(units), len(multi)))
    say()
    say('| unit (reading order) | occurrences |')
    say('|---|---|')
    for u, c in sorted(multi, key=lambda x: -x[1])[:60]:
        say('| %s | %d |' % (u, c))
    say()


def main():
    rows = [r for r in load() if r['flat']]
    lines = lines_of(rows)
    say('# Structure of the Indus texts (ICIT-derived corpus)')
    say()
    s1_s2(lines)
    s3(lines)
    s4(rows)
    s4b(rows)
    s5(lines)
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'structure.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
