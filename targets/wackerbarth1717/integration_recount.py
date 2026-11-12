# wackerbarth1717 - integration recount: ONE counting rule for Relation XXII, the letter of 20 Nov. 1715 and the 24 April key check.
# First version 12 Nov 2026 (integration); rule made strict the same day after the claims review by a second reader.
#
# Read-only: prints to stdout, writes nothing. Run from this folder:  python integration_recount.py [-v]
#
# The contributor's reading files mark each cipher word as certain (plain), {probable}, [restored] or <unresolved>. This
# script aligns every word of the readings on the cipher numbers under it (dynamic programming over the frozen
# transcriptions; one stream per document) and applies one rule to all of them:
#
#   a cipher word is COUNTED only when the contributor read it (certain or probable) AND every letter of the word as read
#   is given by the gloss value of the number under it. A word is NOT counted when any of these holds:
#     off  - a number under it has no value from a gloss of the time (only a value from the sense: key.tsv section B
#            without a gloss, the 1715 deductions 96, 85, 70, 64, 284, 75, 72 ...);
#     mis  - a number under it has a gloss value but the reading gives it other letters (garantir on 4 = x: "xarentir");
#     drop - a number with a gloss value inside the word is passed over by the reading (Poel on "p o e h l");
#     sup  - a letter of the word has no number under it (du from "d" alone; réellement from "r e e l l e m").
#   Gloss values: key c of 1717 (key.tsv section A), K1715 (s15_key.tsv), or one of the GLOSS_BACKED values below (each
#   attested by a gloss of the time, cited). A [restored] word is counted only when its sole defect is such a gloss-backed
#   number. Unresolved words are never counted, except a lone nomenclator number whose value a gloss gives.
#   Letters written in clear inside a cipher line ("{de} 29" = des) are given by the manuscript, not supplied.
#   Spelling equivalences allowed (ORTH; stated once, listed in the output): u = v, i = j = y; a consonant written once in
#   the cipher and doubled in the reading or the reverse (tranquilité / tranquillité, ss = s); "est" of the time read "ét"
#   or "êt" (76 = st in estat, estre, estroite); à + "le roy" = "au Roy". Nothing else.
#   A gloss-valued number passed over BETWEEN two words gives no letter of either word: it is reported, not a defect.
#   The output also gives, as a sensitivity figure only, the count if words whose cipher stops before the end of the
#   word (at least three letters given) were taken as abbreviations of the clerk; that is not the count.
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
    '103': ['le', 'les'],  # key c "les" (view 0088 "V.E. les desire"); "le" by the gloss of view 0080 L03, "deloger les
                           # russes" over "53 2 12 16 7 10 27 103 29 60 6 77 2 51" (103 29 = les, so 103 = le)
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
        if x.startswith('le') and len(x) > 4 and x != 'lempereur': out.add(x[2:])
        if x == 'roidesuede': out.add('leroidesuede')
        if x == 'lempereur': out.add('empereur')
    return out

def parse_groups(text):
    """cipher tokens of one transcription line -> list of (label, [alternatives])"""
    out = []
    # clear words written inside a cipher line ("{de} 29" = des) become a pseudo-group CLEAR:<letters>; the reading
    # usually puts them in « » (then they give nothing), but sometimes runs them into a cipher word
    text = re.sub(r'\{([^}]*)\}', lambda mm: ' CLEAR:%s ' % norm(mm.group(1)) if norm(mm.group(1)) else ' ', text)
    for x in text.split():
        if x.startswith('CLEAR:'):
            out.append((x, [x])); continue
        if x.startswith('~') or x in ('…', '...'): continue
        if '>' in x: x = x.split('>')[1]
        x = x.rstrip('…').rstrip('?').rstrip(':').rstrip('.')      # "2…" = the last number of a line cut at the fold
        alts = [a.rstrip('?') for a in x.split('/') if re.fullmatch(r'\d+\??', a)]
        if alts: out.append((x, alts))
    return out

def words_of(text):
    """reading text -> list of (word, mark); clear text and nulls dropped"""
    # a cipher word whose first letter stands in the clear text just before it ("par raport a" + cipher "ux" = [aux])
    text = re.sub(r'\b[aà]»\s*\[aux\]', '» [~ux]', text)
    # a word begun in clear and finished in cipher (« delo- » + cipher "ogera" = délogera): the clear letters are marked
    # with "=" and are not asked of the numbers
    def clear_head(mm):
        frag, word = norm(mm.group(1)), mm.group(2)
        k = len(frag) if frag and norm(word).startswith(frag) and len(norm(word)) > len(frag) else 0
        return '» %s%s' % ('=' * k, word)
    text = re.sub(r"(\w+)-?[\s,.:;]*»\s*([^\s«]+)", clear_head, text)
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
CONS = 'bcdfglmnprst'
def align(groups, words):
    """DP over (group, letter). Each group either gives its gloss value ('key'), is a null, absorbs an unresolved word,
    is a number without a gloss value ('off'), stands under letters other than its value ('mis'), or is passed over by the
    reading ('drop'). A letter of the reading under which no number stands is 'sup' (supplied by the reader).
    Returns (per, bad): per[word] = list of (label, status, letters); bad[word] = set of defects of that word."""
    letters = []; owner = []; hole_num = {}; clear = set()
    for wi, (w, m) in enumerate(words):
        for k in range(len(w) - len(w.lstrip('='))): clear.add(len(letters) + k)
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
    for i in range(n + 1):
        # letters with no number under them: written in clear ('clr'), or supplied by the reader ('sup'). A run of
        # supplied letters stays inside one word and pays once to open, so that the fewest words carry one.
        exp = int(i * m_ / max(n, 1))
        for j in range(max(0, exp - band), min(m_, exp + band + 1)):
            if j not in cost[i] or L[j] == '#': continue
            c0 = cost[i][j]
            if j in clear:
                if c0 + 0.2 < cost[i].get(j + 1, INF): cost[i][j + 1] = c0 + 0.2; back[i][j + 1] = (i, j, 'clr')
                continue
            # spelling: a consonant the reading doubles and the cipher writes once (tranquilité read tranquillité)
            if j > 0 and L[j] == L[j - 1] and L[j] in CONS and owner[j] == owner[j - 1]:
                if c0 + 0.1 < cost[i].get(j + 1, INF): cost[i][j + 1] = c0 + 0.1; back[i][j + 1] = (i, j, 'orth')
            for k in range(1, 14):
                if j + k > m_ or owner[j + k - 1] != owner[j]: break
                c = 1.0 + 0.6 * k
                if c0 + c < cost[i].get(j + k, INF): cost[i][j + k] = c0 + c; back[i][j + k] = (i, j, 'sup')
        if i == n: break
        lab, alts = groups[i]
        if alts[0].startswith('CLEAR:'):
            v = alts[0][6:]
            for j, c0 in list(cost[i].items()):
                if c0 < cost[i + 1].get(j, INF): cost[i + 1][j] = c0; back[i + 1][j] = (i, j, 'clrgrp')
                if L.startswith(v, j) and c0 < cost[i + 1].get(j + len(v), INF):
                    cost[i + 1][j + len(v)] = c0; back[i + 1][j + len(v)] = (i, j, 'clr')
            continue
        vals = set()
        known = False
        for a in alts:
            v = values(a)
            if a in KC or a in K15 or a in GLOSS_BACKED: known = True
            vals |= v
        is_null_shape = all(len(a) >= 4 and a != '1000' for a in alts)
        for j, c0 in list(cost[i].items()):
            if abs(j - exp) > band: continue
            cands = []
            for v in vals:
                if v == '':
                    cands.append((0, 0.3, 'null'))
                elif L.startswith(v, j):
                    cands.append((len(v), 0.0, 'key'))
                # contraction: "a" / "d" + nomenclator "le roy" = "au Roy" / "du Roy"
                if v.startswith('le') and len(v) > 4 and 0 < j < m_ and L[j] == 'u' and L[j - 1] in 'ad' \
                        and L.startswith(v[2:], j + 1):
                    cands.append((len(v) - 1, 0.1, 'orth'))
                # spelling only (ORTH): "est" of the time read "ét/êt" (estat = état), a doubled consonant read single
                if v == 'st' and 0 < j < m_ and L[j - 1] == 'e' and L[j] == 't' and owner[j] == owner[j - 1]:
                    cands.append((1, 0.1, 'orth'))
                if len(v) == 2 and v[0] == v[1] and v[0] in CONS and j < m_ and L[j] == v[0] and L[j + 1:j + 2] != v[0]:
                    cands.append((1, 0.1, 'orth'))
                if len(v) == 1 and v in CONS and 0 < j < m_ and L[j - 1] == v and owner[j] == owner[j - 1]:
                    cands.append((0, 0.1, 'orth'))
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
                for k in range(1, 8):
                    if j + k <= m_ and '#' not in L[j:j + k]:
                        cands.append((k, 2.0 + 0.15 * k + (1.0 * (k - 2) if k > 2 else 0), 'off'))
            else:
                cands.append((0, 3.0, 'drop'))
                for k in range(1, 3):
                    if j + k <= m_ and '#' not in L[j:j + k]:
                        cands.append((k, 3.2 + 1.0 * k, 'mis'))
            for k, c, st in cands:
                nj = j + k
                if c0 + c < cost[i + 1].get(nj, INF):
                    cost[i + 1][nj] = c0 + c; back[i + 1][nj] = (i, j, st)
    if m_ not in cost[n]:
        return None
    per = collections.defaultdict(list); bad = collections.defaultdict(set)
    i, j = n, m_
    while (i, j) != (0, 0):
        pi, pj, st = back[i][j]
        if st in ('sup', 'clr', 'orth') and pi == i:
            if st == 'sup': bad[owner[pj]].add('sup')
            if st == 'orth': bad[owner[pj]].add('orth')
            per[owner[pj]].append(('+', st, L[pj:j]))
            i, j = pi, pj; continue
        lab = groups[pi][0]
        if j > pj:
            span = owner[pj:j]
            wi = collections.Counter(span).most_common(1)[0][0]
            if st in ('off', 'mis'):
                for o in set(span): bad[o].add(st)      # every word a defective number reaches
            if st == 'orth': bad[wi].add('orth')
        else:
            # a number that gives no letter: inside a word it belongs to that word; between two words to the next one
            wi = owner[pj] if pj < m_ else owner[m_ - 1]
            if st == 'orth': bad[owner[pj - 1]].add('orth'); wi = owner[pj - 1]
            if st in ('off', 'drop'):
                inside = 0 < pj < m_ and owner[pj - 1] == owner[pj]
                bad[wi].add(st if (inside or st == 'off') else 'drop-edge')
        if st == 'unres':
            wi = owner[pj] if (pj < m_ and L[pj] == '#') else owner[pj - 1]
        per[wi].append((lab, st, L[pj:j], (groups[pi][1], L[pj:j])))
        i, j = pi, pj
    for wi in per: per[wi].reverse()
    return per, bad

def classify(words, aligned, primary):
    """one rule -> counted?  `primary` is the key of the letter being read (KC or K15)."""
    per, bad = aligned
    res = []
    for wi, (w, m) in enumerate(words):
        raw = [x for x in per.get(wi, []) if len(x) == 4]
        gs = [(x[0], x[1], x[2]) for x in per.get(wi, [])]
        d = bad.get(wi, set())
        off = [(l.split(':')[-1], s) for l, st, s in gs if st == 'off']
        # groups read with a gloss-built value that the letter's own key does not carry (other volume, or GLOSS_BACKED)
        other = [(l.split(':')[-1], s) for l, st, s, (alts, _) in raw
                 if st == 'key' and not any(primary.get(a) == s or (a in primary and s in values(a) and
                                            primary[a] in (s, 'le' + s, s[2:])) for a in alts)]
        hole = re.fullmatch(r'‹(\d+)›\W*', w)
        defect = None
        for x in ('off', 'mis', 'drop', 'sup'):      # 'drop-edge' is reported, not a defect of the word
            if x in d: defect = x; break
        if m == 'unresolved' and hole and values(hole.group(1)):
            counted = True; why = 'unresolved, now counted: %s=%s (gloss)' % (hole.group(1), '/'.join(sorted(values(hole.group(1)))))
        elif m == 'unresolved': counted = False; why = 'unresolved'
        elif m == 'restored' and not (other and not defect):
            # a restored word is counted only when its sole defect is a number whose value a gloss of the time gives
            counted = False; why = 'restored'
        elif defect:
            counted = False; why = WHY[defect]
            if off: why += ': ' + ' '.join('%s=%s' % x for x in off)
        elif m == 'restored':
            counted = True; why = 'restored, now counted: ' + ' '.join('%s=%s' % x for x in other)
        else:
            counted = True; why = m
        res.append((w, m, counted, why, gs, defect, 'orth' in d, d))
    return res

WHY = {
    'off': 'a number without a gloss-built value',
    'mis': 'a number read as a letter other than its gloss value',
    'drop': 'a number with a gloss value passed over inside the word',
    'drop-edge': 'a number with a gloss value passed over just before the word (reported, not a defect)',
    'sup': 'a letter supplied with no number under it',
}

def run_r22():
    groups = []
    files = ['B-REL22.txt', 'R22-0090-fin.txt'] + ['R22-%04d.txt' % v for v in range(91, 100)]
    for f in files:
        view = '0089-90'
        for line in open('frozen/releves/' + f, encoding='utf-8'):
            mm = re.match(r'# SCAN (\d{4})', line)
            if mm: view = mm.group(1)
            if view == '0089-90' and f.startswith('R22-'): view = f[4:8]
            mm = re.match(r'\s*([A-Z]+\d+) C: ?(.*)', line)
            if mm: groups += [('%s %s:%s' % (view, mm.group(1), g), a) for g, a in parse_groups(mm.group(2))]
    text = ' '.join(l.split(':', 1)[1].strip() for l in open('frozen/lecture/R22-lecture.txt', encoding='utf-8') if l.startswith('@'))
    return groups, words_of(text)

def run_a24():
    groups = []
    for f in ('A24-0037.txt', 'A24-0038.txt', 'A24-0039.txt'):
        view = f[4:8]
        for line in open('frozen/releves/' + f, encoding='utf-8'):
            mm = re.match(r'\s*([A-Z]+\d+) C: ?(.*)', line)
            if mm: groups += [('%s %s:%s' % (view, mm.group(1), g), a) for g, a in parse_groups(mm.group(2))]
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
    # a catchword at the foot of a page that the transcriber took as a last line (0384-g L26 "6 2 12" = the first three
    # numbers of 0384-d) is not counted twice
    names = list(pages)
    for a, b in zip(names, names[1:]):
        if not pages[a] or not pages[b]: continue
        last = pages[a][-1][0].rsplit(':', 1)[0]
        tail = [x for x in pages[a] if x[0].rsplit(':', 1)[0] == last]
        if 2 <= len(tail) <= 4 and [x[1] for x in tail] == [x[1] for x in pages[b][:len(tail)]]:
            print('catchword not counted twice: %s = %s' % (last, ' '.join(x[1][0] for x in tail)))
            pages[a] = pages[a][:-len(tail)]
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

def trailing_only(r):
    gs = r[4]
    k = len(gs)
    while k and gs[k - 1][1] == 'sup': k -= 1
    head = gs[:k]
    return (k < len(gs) and not any(st in ('sup', 'mis', 'off', 'drop') for l, st, s in head)
            and sum(len(s) for l, st, s in head) >= 3)

def show(r):
    loc = next((l.split(':')[0] for l, st, s in r[4] if ':' in l and st != 'clrgrp'), '')
    return '%-13s %-20s %-9s %s' % (loc, r[0].lstrip('='), r[1], ' '.join('%s[%s:%s]' % (l.split(':')[-1], st, s)
                                                                       for l, st, s in r[4] if st != 'clrgrp'))

def report(name, results):
    C = collections.Counter(r[1] for r in results)
    n = len(results); cnt = sum(1 for r in results if r[2])
    print('\n== %s: %d cipher words' % (name, n))
    print('contributor marks:', dict(C), ' certain+probable = %d = %.2f%%' % (C['certain'] + C['probable'], 100.0 * (C['certain'] + C['probable']) / n))
    print('ONE RULE (every letter of the word given by the gloss value of the number under it): counted %d of %d = %.2f%%' % (cnt, n, 100.0 * cnt / n))
    moved_in = [r for r in results if r[2] and r[1] in ('restored', 'unresolved')]
    print('  restored or unresolved words counted (a gloss of the time gives the number): %d' % len(moved_in))
    for r in moved_in: print('    %-18s %s' % (r[0], r[3]))
    out = [r for r in results if not r[2] and r[1] in ('certain', 'probable')]
    print('  certain/probable words NOT counted: %d' % len(out))
    for d in ('off', 'mis', 'drop', 'sup'):
        sub = [r for r in out if r[5] == d]
        print('   %s: %d' % (WHY[d], len(sub)))
        for r in sub: print('      ' + show(r))
    tr = [r for r in out if r[5] == 'sup' and trailing_only(r)]
    print('     of which the supplied letters are only the end of a word whose cipher gives at least its first three letters'
          ' (a possible abbreviation of the clerk, as "allem:" in the 1715 training glosses): %d -> with these %d of %d = %.2f%%'
          ' (sensitivity figure only, NOT the count)' % (len(tr), cnt + len(tr), n, 100.0 * (cnt + len(tr)) / n))
    edge = [r for r in results if 'drop-edge' in r[7]]
    print('  gloss-valued numbers passed over between two words (reported; they give no letter of the next word): %d' % len(edge))
    for r in edge: print('      ' + show(r))
    orth = [r for r in results if r[2] and r[6]]
    print('  counted words that use a spelling equivalence (ORTH): %d' % len(orth))
    for r in orth: print('      ' + show(r))
    rest = [r for r in results if not r[2] and r[1] == 'restored']
    print('  restored words not counted: %d;  unresolved not counted: %d' % (len(rest), sum(1 for r in results if not r[2] and r[1] == 'unresolved')))
    offs = collections.Counter(); offv = collections.defaultdict(collections.Counter)
    for r in results:
        for lab, st, s in r[4]:
            if st == 'off':
                num = lab.split(':')[-1]; offs[num] += 1; offv[num][s] += 1
    print('  numbers with no gloss-built value, and the letters the reading gives them:')
    for num, k in offs.most_common(): print('    %-8s %2d  %s' % (num, k, dict(offv[num])))
    if VERBOSE:
        for r in results: print('   %s %s' % ('+' if r[2] else '-', show(r)))
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
    # one stream for the whole letter: words run over from one page to the next (puisse = "pu" | "isse", l'ex | périence)
    g = [x for p in pages for x in pages[p]]; w = [x for p in pages for x in rp[p]]
    per = align(g, w)
    assert per is not None, '1715 letter: no alignment'
    report('Letter of 20 November 1715', classify(w, per, K15))
