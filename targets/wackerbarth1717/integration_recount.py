# wackerbarth1717 - integration recount (12 Nov 2026): ONE counting rule for Relation XXII and the letter of 20 Nov. 1715.
#
# Read-only: prints to stdout, writes nothing. Run from this folder:  python integration_recount.py [-v]
#
# What it does. The contributor's reading files mark each cipher word as certain (plain), {probable}, [restored] or
# <unresolved>, but the two letters were marked by different rules for one kind of word: a word containing a number that
# no key built from the glosses of the time carries. In Relation XXII such a word is [restored] (not counted); in the 1715
# letter it is {probable} (counted). This script aligns every word of both readings on the cipher numbers under it
# (dynamic programming over the frozen transcriptions) and applies one rule to both:
#
#   a cipher word is COUNTED when the contributor read it (certain or probable) AND every number under it has a value
#   in a key built from glosses of the time: key c of 1717 (key.tsv section A) or K1715 (s15_key.tsv), or one of the
#   GLOSS_BACKED values below (each attested by a gloss of the time, cited). A [restored] word is counted only when its
#   sole defect is such a gloss-backed number. A word under which a number has only a value deduced from the sense
#   (key.tsv section B without a gloss, or the 1715 deductions 96, 85, 70, 64, 284, 75 ...) is NOT counted.
#   Unresolved words are never counted.
import re, sys, unicodedata, collections

VERBOSE = '-v' in sys.argv

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = s.replace('œ', 'oe').replace('æ', 'ae')
    s = re.sub(r'[^a-z]', '', s)
    return s.replace('j', 'i').replace('v', 'u').replace('y', 'i')

def load_key(path, section_a_only=False):
    K = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('## B'):
            if section_a_only: break
            continue
        if l.startswith('#') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        K[f[0]] = norm(f[1]) if len(f) > 1 else ''
    return K

KC = load_key('key.tsv', section_a_only=True)     # key c, frozen, glosses of Loc. 00713/01
K15 = load_key('s15_key.tsv')                      # K1715, glosses of Loc. 00712/05 views 0388-0390
# Values attested by a gloss of the time although absent from (or outvoted in) the key of the letter being read.
GLOSS_BACKED = {
    '4': ['x'],          # K1715: 9 glosses (views 0388-0390)
    '76': ['st'],        # K1715: 5 glosses
    '20': ['b'],         # K1715: 1 gloss; key c had "ee" from one alignment
    '306': ['uienne'],   # K1715: gloss "la cour de Vienne", view 0389
    '78': ['le'],        # training view 0057 of 1717: one gloss "le", one "t" (tie, key c kept t)
    '103': ['le', 'les'],  # key c "les" (view 0088); read "le" in "le comte de Sinzendorf"
}

def values(n):
    v = set()
    for K in (KC, K15):
        if n in K: v.add(K[n])
    for x in GLOSS_BACKED.get(n, []): v.add(x)
    # nomenclator spellings: "le roy" / "leroi", "roidesuede" with or without article
    out = set()
    for x in v:
        out.add(x)
        if x.startswith('le') and len(x) > 4: out.add(x[2:])
        if x == 'roidesuede': out.add('leroidesuede')
        if x == 'lempereur': out.add('empereur')
    return out

def parse_groups(text):
    """cipher tokens of one transcription line -> list of (label, [alternatives])"""
    out = []
    text = re.sub(r'\{[^}]*\}', ' ', text)
    for x in text.split():
        if x.startswith('~') or x in ('…', '...'): continue
        if '>' in x: x = x.split('>')[1]
        x = x.rstrip('?').rstrip(':').rstrip('.')
        alts = [a.rstrip('?') for a in x.split('/') if re.fullmatch(r'\d+\??', a)]
        if alts: out.append((x, alts))
    return out

def words_of(text):
    """reading text -> list of (word, mark); clear text and nulls dropped"""
    # a cipher word whose first letter stands in the clear text just before it ("par raport a" + cipher "ux" = [aux])
    text = re.sub(r'\b[aà]»\s*\[aux\]', '» [~ux]', text)
    text = re.sub(r'«[^»]*»', ' ', text)
    text = re.sub(r'∅\d+', ' ', text).replace('|', ' ')
    out = []
    for w in text.split():
        if '‹' in w: m = 'unresolved'
        elif '[' in w: m = 'restored'
        elif '{' in w: m = 'probable'
        else: m = 'certain'
        out.append((w, m))
    return out

INF = 1e9
def align(groups, words):
    """DP: each group emits a slice of the letter stream. Returns per word the list of (label, status, letters)."""
    letters = []; owner = []; hole_num = {}
    for wi, (w, m) in enumerate(words):
        if m == 'unresolved':
            s = '#'          # one placeholder; a numeric <NNN> is absorbed only by the group NNN
            d = re.sub(r'\D', '', w)
            hole_num[len(letters)] = d if re.fullmatch(r'‹\d+›\W*', w) else None
        else:
            s = norm(w)
        for c in s: letters.append(c); owner.append(wi)
    L = ''.join(letters); n = len(groups); m_ = len(L)
    cost = [dict() for _ in range(n + 1)]; back = [dict() for _ in range(n + 1)]
    cost[0][0] = 0.0
    band = 220
    for i in range(n):
        lab, alts = groups[i]
        vals = set()
        known = False
        for a in alts:
            v = values(a)
            if a in KC or a in K15 or a in GLOSS_BACKED: known = True
            vals |= v
        is_null_shape = all(len(a) >= 4 and a != '1000' for a in alts)
        exp = int(i * m_ / max(n, 1))
        for j, c0 in list(cost[i].items()):
            if abs(j - exp) > band: continue
            cands = []
            for v in vals:
                if v == '':
                    cands.append((0, 0.3, 'null'))
                elif L.startswith(v, j):
                    cands.append((len(v), 0.0, 'key'))
            # placeholder of an unresolved word absorbs the group
            if j < m_ and L[j] == '#':
                hn = hole_num.get(j)
                if hn is None: cands.append((1, 0.6, 'unres')); cands.append((0, 0.6, 'unres'))
                elif hn in alts: cands.append((1, 0.0, 'unres'))
            if j > 0 and L[j - 1] == '#' and hole_num.get(j - 1) is None:
                cands.append((0, 0.6, 'unres'))
            if not known and is_null_shape:
                cands.append((0, 0.5, 'null'))
            elif not known:
                cands.append((0, 2.5, 'off'))
                for k in range(1, 15):
                    if j + k <= m_ and '#' not in L[j:j + k]:
                        cands.append((k, 2.0 + 0.15 * k, 'off'))
            else:
                for k in range(0, 4):
                    if j + k <= m_ and '#' not in L[j:j + k]:
                        cands.append((k, 4.0 + 0.5 * k, 'mis'))
            for k, c, st in cands:
                nj = j + k
                if c0 + c < cost[i + 1].get(nj, INF):
                    cost[i + 1][nj] = c0 + c; back[i + 1][nj] = (j, st)
    if m_ not in cost[n]:
        return None
    per = collections.defaultdict(list)
    j = m_
    for i in range(n, 0, -1):
        pj, st = back[i][j]
        lab = groups[i - 1][0]
        if j > pj:
            span = owner[pj:j]
            wi = collections.Counter(span).most_common(1)[0][0]
            if st == 'off':      # a number without a value falls to the word the contributor marked probable, if any
                pr = collections.Counter(o for o in span if words[o][1] == 'probable')
                if pr: wi = pr.most_common(1)[0][0]
        elif pj < m_: wi = owner[pj]
        else: wi = owner[m_ - 1]
        if st == 'unres':
            wi = owner[pj] if (pj < m_ and L[pj] == '#') else owner[pj - 1]
        per[wi].append((lab, st, L[pj:j], (groups[i - 1][1], L[pj:j])))
        j = pj
    for wi in per: per[wi].reverse()
    return per

def classify(words, per, primary):
    """one rule -> counted?  `primary` is the key of the letter being read (KC or K15)."""
    res = []
    for wi, (w, m) in enumerate(words):
        gs = [(l, st, s) for l, st, s, _ in per.get(wi, [])]
        raw = per.get(wi, [])
        off = [(l.split(':')[-1], s) for l, st, s in gs if st == 'off']
        mis = [(l, s) for l, st, s in gs if st == 'mis']
        # groups read with a gloss-built value that the letter's own key does not carry (other volume, or GLOSS_BACKED)
        other = [(l.split(':')[-1], s) for l, st, s, (alts, _) in raw
                 if st == 'key' and not any(primary.get(a) == s or (a in primary and s in values(a) and
                                            primary[a] in (s, 'le' + s, s[2:])) for a in alts)]
        hole = re.fullmatch(r'‹(\d+)›\W*', w)
        if m == 'unresolved' and hole and values(hole.group(1)):
            counted = True; why = 'unresolved, now counted: %s=%s (gloss)' % (hole.group(1), '/'.join(sorted(values(hole.group(1)))))
        elif m == 'unresolved': counted = False; why = 'unresolved'
        elif m == 'restored':
            # counted only when the sole defect is a number whose value a gloss of the time gives
            counted = bool(other) and not off and not mis
            why = ('restored, now counted: ' + ' '.join('%s=%s' % x for x in other)) if counted else 'restored'
        elif off:
            counted = False; why = 'number without a gloss-built value: ' + ' '.join('%s=%s' % x for x in off)
        else:
            counted = True; why = m
        res.append((w, m, counted, why, gs))
    return res

def run_r22():
    groups = []
    files = ['B-REL22.txt', 'R22-0090-fin.txt'] + ['R22-%04d.txt' % v for v in range(91, 100)]
    for f in files:
        for line in open('frozen/releves/' + f, encoding='utf-8'):
            mm = re.match(r'\s*([A-Z]+\d+) C: ?(.*)', line)
            if mm: groups += [('%s:%s' % (mm.group(1), g), a) for g, a in parse_groups(mm.group(2))]
    text = ' '.join(l.split(':', 1)[1].strip() for l in open('frozen/lecture/R22-lecture.txt', encoding='utf-8') if l.startswith('@'))
    return groups, words_of(text)

def run_a24():
    groups = []
    for f in ('A24-0037.txt', 'A24-0038.txt', 'A24-0039.txt'):
        for line in open('frozen/releves/' + f, encoding='utf-8'):
            mm = re.match(r'\s*([A-Z]+\d+) C: ?(.*)', line)
            if mm: groups += [('%s:%s' % (mm.group(1), g), a) for g, a in parse_groups(mm.group(2))]
    words = []
    for l in open('frozen/lecture/A24-lecture.txt', encoding='utf-8'):
        if l.startswith('@'): words += words_of(l.split(':', 1)[1])
    return groups, words

def run_s15():
    pages = collections.OrderedDict(); cur = None
    for line in open('s15_transcription.txt', encoding='utf-8'):
        mm = re.match(r'===== CIBLE-(\d{4}-[gd])', line)
        if mm: cur = mm.group(1); pages[cur] = []; continue
        if line.startswith('# CORRECTIONS'): cur = None
        mm = re.match(r'\s*(L\d+) C: ?(.*)', line)
        if mm and cur: pages[cur] += [('%s %s:%s' % (cur, mm.group(1), g), a) for g, a in parse_groups(mm.group(2))]
    # blind plate W1: three corrected digits (frozen lines unchanged), applied here as the reading v2 does
    fix = {('0384-g', 'L11', '28/25'): ['25'], ('0385-g', 'L22', '28'): ['25', '28'], ('0383-d', 'L14', '16/26'): ['66']}
    for p in pages:
        for k, (lab, alts) in enumerate(pages[p]):
            for (fp, fl, fg), new in fix.items():
                if p == fp and lab.startswith('%s %s:%s' % (fp, fl, fg)): pages[p][k] = (lab, new)
    rp = collections.OrderedDict(); cur = None
    for line in open('s15_reading.md', encoding='utf-8'):
        mm = re.match(r'== (\d{4}-[gd])', line)
        if mm: cur = mm.group(1); rp[cur] = []; continue
        if cur and (re.match(r'L\d+', line) or line.startswith('«')):
            rp[cur] += words_of(re.sub(r'^L\d+(-\d+)?\s', '', line))
    return pages, rp

def report(name, results):
    C = collections.Counter(m for w, m, c, why, gs in results)
    n = len(results); cnt = sum(1 for r in results if r[2])
    print('\n== %s: %d cipher words' % (name, n))
    print('contributor marks:', dict(C), ' certain+probable = %d = %.2f%%' % (C['certain'] + C['probable'], 100.0 * (C['certain'] + C['probable']) / n))
    print('ONE RULE (gloss-built values only): counted %d of %d = %.2f%%' % (cnt, n, 100.0 * cnt / n))
    moved_in = [r for r in results if r[2] and r[1] in ('restored', 'unresolved')]
    moved_out = [r for r in results if not r[2] and r[1] in ('certain', 'probable')]
    print('  restored or unresolved words now counted (a gloss of the time gives the number): %d' % len(moved_in))
    for r in moved_in: print('    %-18s %s' % (r[0], r[3]))
    print('  certain/probable words not counted (a number with a deduced value only): %d' % len(moved_out))
    for r in moved_out: print('    %-18s %s' % (r[0], r[3]))
    offs = collections.Counter(); offv = collections.defaultdict(collections.Counter)
    for w, m, c, why, gs in results:
        for lab, st, s in gs:
            if st == 'off':
                num = lab.split(':')[-1]; offs[num] += 1; offv[num][s] += 1
    print('  numbers with no gloss-built value, and the letters the reading gives them:')
    for num, k in offs.most_common(): print('    %-8s %2d  %s' % (num, k, dict(offv[num])))
    if VERBOSE:
        for w, m, c, why, gs in results:
            print('   %s %-22s %-10s %s' % ('+' if c else '-', w, m, ' '.join('%s[%s:%s]' % (l.split(':')[-1], st, s) for l, st, s in gs)))
    return cnt, n

if __name__ == '__main__':
    g, w = run_r22()
    per = align(g, w)
    assert per is not None, 'Relation XXII: no alignment'
    report('Relation XXII (14-16 June 1717)', classify(w, per, KC))
    g, w = run_a24()
    per = align(g, w)
    assert per is not None, '24 April: no alignment'
    report('Letter of 24 April 1717, views 0037-0039 (key check against the sheet of the time)', classify(w, per, KC))
    pages, rp = run_s15()
    allres = []
    for p in pages:
        per = align(pages[p], rp[p])
        assert per is not None, 's15 page %s: no alignment' % p
        allres += classify(rp[p], per, K15)
    report('Letter of 20 November 1715', allres)
