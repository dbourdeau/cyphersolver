"""A test bench for proposed decipherments of the Indus script.

A key is a table sign -> value (a sound value in the claimed language, in Latin transliteration)
with an optional gloss (what the sign depicts or means), on ICIT glyph ids (keys/*.tsv; the header
comment names the language: sa Sanskrit, dra Dravidian, sux Sumerian). Every key is scored the
same way:

B1  Shape and coverage: signs keyed, share of sign tokens in the corpus with a value, share of the
    50 commonest signs keyed.
B2  Reading against its own shuffles. Decoded texts become consonant skeletons (coarse classes:
    k/g, c/j, t/d with retroflexes, p/b, n with the other nasals, m, y, r, l, v, s with s/sh/h;
    vowels dropped, as the script is taken to leave them). A text reads to the extent its
    skeleton parses into lexicon words (plus one consonant from the language's case endings).
    Score: share of consonants covered by words of 3+ consonants. The same for 200 keys that
    permute the key's values among keyed signs of similar frequency. The key is scored against
    all three lexicons (Monier-Williams; DEDR, all languages; ePSD2 nouns): a key that reads
    its claimed language no better than its shuffles, or reads the other languages as well, is
    not evidence for its language.
B3  The copper-tablet anchors (Parpola 1994 Fig. 7.14, copper.py): four signs whose meaning the
    tablets fix without any language (341 rhinoceros, 749 goat, 753 hare, 777/778 goat and
    archer), and seven texts written on the back of a picture (goat, rhinoceros, hare, archer,
    spotted bull, long-horned bull, elephant). A right key should read an anchor sign as its
    animal, and should put a word for the animal in its reading of the anchor texts more often
    than its shuffles do.
B4  The structure a reading must fit: are the stroke numerals read as number words, and the
    short and long series apart? Are the two endings 740 and 520 read differently, and the three
    openers 817/820/861?
B5  Controls. (a) Power: synthetic texts made of real lexicon words, written with a random sign
    key of the corpus's shape; the true key against its shuffles. (b) The ceiling: a key fitted
    to the corpus by hill-climbing, one consonant class per sign, for each language: how much
    of the real corpus any language can be made to read.

Usage: python bench.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv> [yajnadevam xlits.csv]
Writes results/bench.md.
"""
import csv
import functools
import glob
import os
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict

from equation_rebus import lexicon_mw
from numerals import NUMS
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(61)
ENDINGS = {'sa': set('smntyrv'), 'dra': set('nlrmtk'), 'sux': set('krtsn')}
LANGNAME = {'sa': 'Sanskrit (Monier-Williams)', 'dra': 'Dravidian (DEDR)', 'sux': 'Sumerian (ePSD2)',
            'mu': 'Munda (JAMBU)', 'ta': 'Old Tamil (Sangam-cited Tamil Lexicon)', 'bu': 'Burushaski (Berger, Yoshioka)'}
ENDINGS_V = {'sa': set('SMNTYRV'), 'dra': set('NLRMTK'), 'sux': set('KRTSN'), 'mu': set('NKTR'),
             'ta': set('NLRMTK'), 'bu': set('MNTSK')}
SIGN_ANCHORS = {'341': ['rhinoceros'], '749': ['goat'], '753': ['hare'], '777': ['goat', 'archer'],
                '778': ['goat', 'archer']}
TEXT_ANCHORS = [('806 233 384 740', 'goat'), ('503 615 740', 'rhinoceros'), ('235 705 33 845 407 321 407', 'hare'),
                ('806 845 61 407 850 900 740', 'archer'), ('231 17 585 95 520 32 407', 'goat'),
                ('32 220 176 740', 'bull'), ('744 760 95 595 1 142 615 615', 'bull'), ('706 33 923 740', 'elephant')]
ANIMAL_PAT = {'rhinoceros': r'\brhinoceros', 'goat': r'\b(goat|he-goat|she-goat|markhor|ibex)', 'hare': r'\b(hare|rabbit)',
              'archer': r'\b(archer|bowman|bow)\b', 'bull': r'\b(bull|ox|bullock)\b', 'elephant': r'\belephant'}
NUMWORDS = {'sa': {1: ['eka'], 2: ['dvi', 'dva'], 3: ['tri'], 4: ['catur'], 5: ['panca'], 6: ['sas'],
                   7: ['sapta'], 8: ['asta'], 12: ['dvadasa']},
            'dra': {1: ['or', 'oru', 'onru'], 2: ['iru', 'irantu'], 3: ['mu', 'munru'], 4: ['nal', 'nanku'],
                    5: ['cay', 'ai', 'aintu'], 6: ['aru'], 7: ['elu'], 8: ['en', 'ettu'], 12: ['panniru', 'pannirantu']},
            'sux': {1: ['dis', 'as'], 2: ['min'], 3: ['es'], 4: ['limmu'], 5: ['ia'], 6: ['as'], 7: ['imin'],
                    8: ['ussu'], 12: ['usmin']}}


def say(s=''):
    OUT.append(s)
    print(s)


CLASS = {}
for cls, chars in (('k', 'kgqx'), ('c', 'cj'), ('t', 'td'), ('p', 'pbf'), ('n', 'n'), ('m', 'm'), ('y', 'y'),
                   ('r', 'r'), ('l', 'lz'), ('v', 'vw'), ('s', 's')):
    for ch in chars:
        CLASS[ch] = cls


@functools.lru_cache(maxsize=None)
def skel(x):
    """Consonant skeleton on coarse classes. Aspiration (a consonant + h) is dropped; a bare h joins s."""
    x = x.lower().replace('ĝ', 'n').replace('ḫ', 'k').replace('ṃ', 'n').replace('ḥ', '').replace('r̤', 'l')
    x = unicodedata.normalize('NFD', x)
    x = ''.join(c for c in x if not unicodedata.combining(c))
    x = re.sub(r'([kgcjtdpb])h', r'\1', x).replace('h', 's')
    s = ''.join(CLASS[c] for c in x if c in CLASS)
    return re.sub(r'(.)\1+', r'\1', s)


VOWEL = {'a': 'a', 'e': 'a', 'i': 'i', 'o': 'u', 'u': 'u'}
for _v, _c in (('ə', 'a'), ('ɛ', 'a'), ('æ', 'a'), ('ɔ', 'u'), ('ɨ', 'i'), ('ʌ', 'a'), ('ɯ', 'u')):
    VOWEL[_v] = _c


@functools.lru_cache(maxsize=None)
def skelv(x):
    """Vowel-aware skeleton: the consonant classes (upper case) with the vowels kept in three classes
    (a/e, i, o/u), as a syllabic script writes them. Used for the B2v test."""
    x = x.lower().replace('ĝ', 'n').replace('ḫ', 'k').replace('ṃ', 'n').replace('ḥ', '').replace('r̤', 'l')
    x = unicodedata.normalize('NFD', x)
    x = ''.join(c for c in x if not unicodedata.combining(c))
    x = re.sub(r'([kgcjtdpb])h', r'\1', x).replace('h', 's')
    s = ''.join(CLASS[c].upper() if c in CLASS else VOWEL.get(c, '') for c in x)
    return re.sub(r'(.)\1+', r'\1', s)


def lexicons(mw, dedr, sux):
    lex, gl = {}, {}
    w = lexicon_mw(mw)
    lex['sa'] = {skel(a) for a, _ in w if len(skel(a)) >= 1}
    gl['sa'] = w
    dw = []
    for r in csv.DictReader(open(dedr, encoding='utf-8')):
        f = r['Form'].strip().strip('-')
        if f:
            dw.append((f, r['Parameter_ID']))
    lex['dra'] = {skel(a) for a, _ in dw if skel(a)}
    sw = [(r['cf'], (r['gw'] + ' ' + r['senses']).lower())
          for r in csv.DictReader(open(sux, encoding='utf-8'), delimiter='\t')]
    lex['sux'] = {skel(a) for a, _ in sw if skel(a)}
    gl['sux'] = sw
    raw = {'sa': [a for a, _ in w], 'dra': [a for a, _ in dw], 'sux': [a for a, _ in sw]}
    return lex, gl, raw


def extra_raw(scout):
    """Word lists for Munda (JAMBU: Pinnow 1959, Munda 1968 Proto-Kherwarian, Zide 1982 Sora, Santali
    survey, Kharia), Old Tamil (Tamil Lexicon entries citing Sangam works or Tolkappiyam, romanised
    headword) and Burushaski (Berger via JAMBU, Yoshioka), from the scout folder."""
    raw = {'mu': [], 'ta': [], 'bu': []}
    if not scout or not os.path.isdir(scout):
        return raw
    for fn in glob.glob(os.path.join(scout, 'munda', 'jambu', '2026*.csv')):
        for r in csv.reader(open(fn, encoding='utf-8')):
            if len(r) > 2 and r[2]:
                raw['mu'].append(re.sub(r"[()ˈˌʔ'\-]", '', r[2]))
    p = os.path.join(scout, 'oldtamil', 'mtl_sangam_cited_entries.csv')
    if os.path.exists(p):
        for r in csv.DictReader(open(p, encoding='utf-8')):
            h = r['body'].split('||')[0].strip()
            if h:
                raw['ta'].append(h.replace('-', ''))
    for fn in glob.glob(os.path.join(scout, 'burushaski', 'jambu', '2026*.csv')):
        for r in csv.reader(open(fn, encoding='utf-8')):
            if len(r) > 2 and r[2]:
                raw['bu'].append(re.sub(r"[()ˈˌʔ'\-=]", '', r[2]))
    return raw


def dedr_glosses(dedr_forms):
    """DEDR meanings per form, through the entry csv next to forms.csv."""
    p = os.path.join(os.path.dirname(dedr_forms), 'dedr_entry_v11.csv')
    out = []
    for r in csv.DictReader(open(p, encoding='utf-8')):
        f = r['entry_str'].split('(')[0].split(',')[0].strip().strip('-').strip(')')
        f = f.split()[0] if f.split() else ''
        if f:
            out.append((f, r['entry_meaning'].lower()))
    return out


def coverage(s, words, endings, maxlen=8):
    n = len(s)
    best = [-1] * (n + 1)
    best[0] = 0
    for i in range(n):
        if best[i] < 0:
            continue
        for L in range(1, min(maxlen, n - i) + 1):
            w = s[i:i + L]
            if w in words or (L > 1 and w[:-1] in words and w[-1] in endings):
                v = best[i] + (L if L >= 3 else 0)
                if v > best[i + L]:
                    best[i + L] = v
    return max(best[n], 0)


def runs(t, key, sk=None):
    """Maximal runs of keyed signs, as skeletons."""
    sk = sk or skel
    out, cur = [], ''
    for g in t:
        v = key.get(g)
        if v is None:
            if cur:
                out.append(cur)
            cur = ''
        else:
            cur += sk(v)
    if cur:
        out.append(cur)
    return out


def score(texts, key, words, endings, sk=None, maxlen=8):
    tot = cov = 0
    for t in texts:
        for s in runs(t, key, sk):
            tot += len(s)
            cov += coverage(s, words, endings, maxlen)
    return cov / tot if tot else 0.0


def shuffles(key, freq, n=200, band=10):
    signs = sorted(key, key=lambda g: -freq[g])
    bands = [signs[i:i + band] for i in range(0, len(signs), band)]
    for _ in range(n):
        k2 = {}
        for b in bands:
            vals = [key[g] for g in b]
            random.shuffle(vals)
            k2.update(zip(b, vals))
        yield k2


def load_key(path):
    meta, key, gloss = {}, {}, {}
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#'):
            m = re.search(r'language:\s*(\w+)', ln)
            if m:
                meta['lang'] = m.group(1)
            if 'title' not in meta:
                meta['title'] = ln.lstrip('# ').split(':')[0].strip()
            continue
        c = ln.rstrip('\n').split('\t')
        if len(c) >= 2 and c[0] != 'sign':
            key[c[0]] = c[1]
            if len(c) >= 3:
                gloss[c[0]] = c[2]
    return meta, key, gloss


def load_yajnadevam(path):
    key = {}
    for r in csv.DictReader(open(path, encoding='utf-8')):
        g = str(int(r['sign']))
        if r['xlit'].strip() and r['xlit'] not in ('.', ' '):
            key[g] = r['xlit']
    return {'lang': 'sa', 'title': 'Yajnadevam 2024 (github.com/yajnadevam/lipi, xlits.csv)'}, key, {}


def animal_words(lang, gl, animal):
    pat = re.compile(ANIMAL_PAT[animal])
    return {skel(w) for w, g in gl[lang] if pat.search(g) and len(skel(w)) >= 2}


def bench_key(name, meta, key, gloss, texts, freq, lex, gl, lines_all, lexv=None):
    lang = meta['lang']
    say('## %s' % meta['title'])
    say()
    tok = sum(freq.values())
    kt = sum(freq[g] for g in key)
    top = [g for g, _ in freq.most_common(50)]
    say('**B1 shape.** %d signs keyed; %.0f%% of sign tokens have a value; %d of the 50 commonest signs keyed; '
        '%d distinct consonant skeletons among the values.' % (
            len(key), 100 * kt / tok, sum(1 for g in top if g in key), len({skel(v) for v in key.values()})))
    say()
    b2 = {}
    if len(key) < 20:
        say('**B2 reading against shuffled keys:** not applicable; %d signs are too few for a reading test (the '
            'keyed signs rarely stand next to each other).' % len(key))
    else:
        say('**B2 reading against shuffled keys** (share of consonants covered by words of 3+ consonants; 200 '
            'shuffles):')
        say()
        say('| lexicon | real key | shuffles median (range) | shuffles as good | ')
        say('|---|---|---|---|')
    for L in (('sa', 'dra', 'sux') if len(key) >= 20 else ()):
        real = score(texts, key, lex[L], ENDINGS[L])
        sims = sorted(score(texts, k2, lex[L], ENDINGS[L]) for k2 in shuffles(key, freq, band=10 if len(key) > 60 else 3))
        ge = sum(1 for s in sims if s >= real)
        b2[L] = (real, sims[100], ge)
        say('| %s%s | %.1f%% | %.1f%% (%.1f-%.1f) | %d of 200 |' % (
            LANGNAME[L], ' (claimed)' if L == lang else '', 100 * real, 100 * sims[100], 100 * sims[0],
            100 * sims[-1], ge))
    say()
    if lexv and len(key) >= 20:
        say('**B2v the same, vowels kept** (three vowel classes; the version that passes the Linear Elamite '
            'control, B5c; 100 shuffles):')
        say()
        say('| lexicon | real key | shuffles median (range) | shuffles as good |')
        say('|---|---|---|---|')
        b2['v'] = {}
        for L in lexv:
            real = score(texts, key, lexv[L], ENDINGS_V[L], skelv, 12)
            sims = sorted(score(texts, k2, lexv[L], ENDINGS_V[L], skelv, 12)
                          for k2 in shuffles(key, freq, n=100, band=10 if len(key) > 60 else 3))
            ge = sum(1 for s in sims if s >= real)
            b2['v'][L] = (real, sims[50], ge)
            say('| %s%s | %.1f%% | %.1f%% (%.1f-%.1f) | %d of 100 |' % (
                LANGNAME[L], ' (claimed)' if L == lang else '', 100 * real, 100 * sims[50], 100 * sims[0],
                100 * sims[-1], ge))
        say()
    say('**B3 the copper-tablet anchors.**')
    say()
    sa = []
    for g, anim in SIGN_ANCHORS.items():
        if g not in key and g not in gloss:
            sa.append('%s (%s): no value' % (g, '/'.join(anim)))
            continue
        v = key.get(g, '')
        hit = 'the gloss' if any(re.search(ANIMAL_PAT[a], gloss.get(g, '').lower()) for a in anim) else ''
        if not hit and lang in gl and v and len(skel(v)) >= 2:
            m = sorted('%s "%s"' % (w, gg[:40]) for a in anim for w, gg in gl[lang]
                       if re.search(ANIMAL_PAT[a], gg) and skel(w) == skel(v))
            hit = ('the sound, = ' + '; '.join(m[:3])) if m else ''
        sa.append('%s (%s) = %s%s: %s' % (g, '/'.join(anim), v, ' "%s"' % gloss[g] if g in gloss else '',
                                         'names it by ' + hit if hit else 'no'))
    say('- anchor signs: ' + '; '.join(sa) + '.')
    if lang in gl:
        aw = {a: animal_words(lang, gl, a) for a in ANIMAL_PAT}

        def hits(k):
            h = off = 0
            for t, a in TEXT_ANCHORS:
                s = ''.join(runs(t.split(), k))
                h += any(len(w) >= 2 and w in s for w in aw[a])
                off += sum(any(len(w) >= 2 and w in s for w in aw[b]) for b in aw if b != a) / (len(aw) - 1)
            return h, off
        h, off = hits(key)
        sims = [hits(k2)[0] for k2 in shuffles(key, freq, band=10 if len(key) > 60 else 3)]
        say('- anchor texts naming their own animal (a %s word for it, 2+ consonants, inside the reading): %d of %d; '
            'naming another tablet animal: %.1f on average; shuffled keys: mean %.2f, as many or more in %d of 200.' % (
                lang, h, len(TEXT_ANCHORS), off, sum(sims) / len(sims), sum(1 for s in sims if s >= h)))
    say()
    say('**B4 structure.**')
    say()
    nums = NUMWORDS[lang]
    rd, keyed = [], 0
    for g, (val, kind, _) in sorted(NUMS.items(), key=lambda x: (x[1][1], x[1][0])):
        if g in key:
            keyed += 1
            kv = skel(key[g])
            words = [skel(w) for w in nums.get(val, [])]
            eng = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
            if (len(kv) >= 2 and kv in words) or (val <= 12 and re.search(r'\b%s\b' % eng[val], gloss.get(g, ''))):
                ok = 'full'
            elif kv and any(w.startswith(kv) for w in words):
                ok = 'initial'
            else:
                ok = ''
            rd.append((g, val, kind, key[g], ok))
    say('- stroke numerals keyed: %d of %d; value = the number word: %d; value = only its first consonant: %d '
        '(one-letter values match some number by chance: %s). %s.' % (
        keyed, len(NUMS), sum(1 for x in rd if x[4] == 'full'), sum(1 for x in rd if x[4] == 'initial'),
        'the chance a one-consonant value starts the right number word is about 1 in 8',
        ', '.join('%s=%d %s "%s"%s' % (g, v, k, x, ' (%s)' % o if o else '') for g, v, k, x, o in rd)))
    same = [(s, l) for s, l in (('3', '33'), ('4', '34'), ('5', '35'), ('6', '36'), ('1', '31'), ('2', '32'))
            if s in key and l in key]
    say('- short and long strokes of one number: %s.' % ('; '.join('%s/%s = %s/%s' % (s, l, key[s], key[l]) for s, l in same)
                                                         or 'not both keyed'))
    say('- endings 740 / 520 = %s / %s; second slot 400 / 90 / 151 = %s / %s / %s; openers 817 / 820 / 861 = %s / %s / %s.' % tuple(
        repr(key.get(g)) for g in ('740', '520', '400', '90', '151', '817', '820', '861')))
    say()
    return b2


def planted(lex, freq, texts, L):
    """B5a: synthetic corpus of real lexicon words under a random sign key of the corpus's shape."""
    words = [w for w in lex[L] if 2 <= len(w) <= 5]
    signs = [g for g, _ in freq.most_common(200)]
    classes = sorted(set(CLASS.values()))
    truth = {g: random.choice(classes) for g in signs}
    bycls = defaultdict(list)
    for g, c in truth.items():
        bycls[c].append(g)
    syn = []
    for t in texts[:800]:
        s = ''
        while len(s) < len(t):
            s += random.choice(words)
        syn.append([random.choice(bycls[c]) if bycls[c] else signs[0] for c in s[:len(t)]])
    f2 = Counter(g for t in syn for g in t)
    for g in truth:
        f2[g] += 0
    real = score(syn, truth, lex[L], ENDINGS[L])
    sims = sorted(score(syn, k2, lex[L], ENDINGS[L]) for k2 in shuffles(truth, f2, n=50))
    return real, sims[25], sims[-1]


def fitted(lex, freq, texts, L, iters=3000):
    """B5b: hill-climb a one-consonant-per-sign key to the corpus for language L."""
    signs = [g for g, _ in freq.most_common(250)]
    classes = sorted(set(CLASS.values()))
    key = {g: random.choice(classes) for g in signs}
    idx = defaultdict(set)
    for i, t in enumerate(texts):
        for g in t:
            idx[g].add(i)
    per = [None] * len(texts)

    def tscore(i, k):
        c = tot = 0
        for s in runs(texts[i], k):
            tot += len(s)
            c += coverage(s, lex[L], ENDINGS[L])
        return c, tot
    for i in range(len(texts)):
        per[i] = tscore(i, key)
    cur = sum(c for c, _ in per)
    for _ in range(iters):
        g = random.choice(signs)
        old = key[g]
        key[g] = random.choice(classes)
        aff = idx[g]
        new = {i: tscore(i, key) for i in aff}
        delta = sum(new[i][0] - per[i][0] for i in aff)
        if delta >= 0:
            for i in aff:
                per[i] = new[i]
            cur += delta
        else:
            key[g] = old
    tot = sum(t for _, t in per)
    return cur / tot, key


def main(mw, dedr, sux, yaj=None, scout=None):
    rows = [r for r in load() if r['flat']]
    texts = [ln for r in rows for ln in r['seq'] if len(ln) >= 3]
    freq = Counter(g for t in texts for g in t)
    lex, gl, raw = lexicons(mw, dedr, sux)
    gl['dra'] = dedr_glosses(dedr)
    raw.update({L: v for L, v in extra_raw(scout).items() if v})
    lexv = {L: {skelv(w) for w in ws if skelv(w)} for L, ws in raw.items()}
    say('# A test bench for Indus decipherments')
    say()
    say('%d lines of 3+ signs (ICIT-derived corpus). Lexicon skeletons: %s.' % (
        len(texts), ', '.join('%s %d' % (LANGNAME[L], len(lex[L])) for L in lex)))
    say()
    say('## Key-independent: the endings as gender classes')
    say()
    say('Mahadevan (1998) reads 740 and 520 as the masculine and non-masculine singular suffixes. Gender is a '
        'property of the noun, so a name should take one of them, not both.')
    say()
    def split_end(t):
        if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
            return tuple(t[:-2]), t[-2]
        if len(t) >= 2 and t[-1] in ('740', '520'):
            return tuple(t[:-1]), t[-1]
        return None, None
    ends = [split_end(t) for t in texts]
    ends = [(st, e) for st, e in ends if st]
    stems = defaultdict(Counter)
    for st, e in ends:
        stems[st[-1]][e] += 1
    big = {a: c for a, c in stems.items() if sum(c.values()) >= 10}
    mixed = {a: c for a, c in big.items() if min(c['740'], c['520']) / sum(c.values()) >= 0.2}
    say('- last sign of the name before the ending (740 or 520, with or without 400/90/151 after it), signs with '
        '10+ lines: %d; taking the minority ending in 20%%+ of lines: %d (%s).' % (
            len(big), len(mixed), ', '.join('%s %d/%d' % (a, c['740'], c['520']) for a, c in
                                            sorted(mixed.items(), key=lambda x: -sum(x[1].values())))))

    def both_count(pairs):
        w = defaultdict(set)
        for st, e in pairs:
            w[st].add(e)
        return sum(1 for v in w.values() if len(v) == 2), len(w)
    real, nst = both_count(ends)
    es = [e for _, e in ends]
    sims = []
    for _ in range(200):
        random.shuffle(es)
        sims.append(both_count([(st, e) for (st, _), e in zip(ends, es)])[0])
    sims.sort()
    say('- whole names (the text before the ending) seen with both endings: %d of %d; with the endings shuffled '
        'among the lines: median %d (range %d-%d). %s' % (
            real, nst, sims[100], sims[0], sims[-1],
            'The endings are fixed per name, as a gender (or any lexical class) would be.' if real < sims[0]
            else 'Not more fixed than chance.'))
    say()
    keys = []
    if yaj:
        keys.append(('yajnadevam',) + load_yajnadevam(yaj))
    for p in sorted(p for p in glob.glob(os.path.join(HERE, 'keys', '*.tsv')) if not p.endswith('_raw.tsv')):
        keys.append((os.path.basename(p)[:-4],) + load_key(p))
    summary = []
    for name, meta, key, gloss in keys:
        b2 = bench_key(name, meta, key, gloss, texts, freq, lex, gl, rows, lexv)
        summary.append((meta['title'], meta['lang'], b2 if len(key) >= 20 else None))
    say('## B5 Controls')
    say()
    for L in ('sa', 'dra', 'sux'):
        r, med, mx = planted(lex, freq, texts, L)
        say('- (a) power, %s: planted key reads %.1f%% of its synthetic corpus; its shuffles median %.1f%%, best %.1f%%.' % (
            LANGNAME[L], 100 * r, 100 * med, 100 * mx))
    fit_texts = texts[:1000]
    for L in ('sa', 'dra', 'sux'):
        c, _ = fitted(lex, freq, fit_texts, L)
        say('- (b) ceiling, %s: a key fitted by hill-climbing (one consonant class per sign, 250 commonest signs, '
            '3,000 steps, 1,000 lines) reads %.1f%% of those lines.' % (LANGNAME[L], 100 * c))
    if scout:
        import elamite_control as ec
        le = os.path.join(scout, 'linear_elamite')
        tx = os.path.join(le, 'elamicon_linear_elamite_texts.csv')
        if os.path.exists(tx):
            ekey, etexts = ec.load_le(tx, os.path.join(le, 'elamicon_signvalues.csv'))
            ef = Counter(g for t in etexts for g in t)
            hall = os.path.join(scout, 'elamite', 'hallock1969_glossary_ocr.txt')
            for lab, sk, lx, en, ml in (('consonants only', skel, ec.hallock(hall, skel), set('rkpnmt'), 8),
                                        ('vowels kept', skelv, ec.hallock(hall, skelv), set('RKPNMT'), 12)):
                real = score(etexts, ekey, lx, en, sk, ml)
                sims = sorted(score(etexts, k2, lx, en, sk, ml) for k2 in shuffles(ekey, ef, n=100, band=10))
                say('- (c) a real decipherment, Linear Elamite (Desset 2022 values, Elamicon corpus, Hallock 1969 '
                    'Elamite lexicon), %s: %.1f%% against shuffles %.1f%% (%.1f-%.1f), %d of 100 as good.' % (
                        lab, 100 * real, 100 * sims[50], 100 * sims[0], 100 * sims[-1], sum(1 for x in sims if x >= real)))
    say()
    say('## Summary')
    say()
    say('| key | claimed | consonants only: key / shuffles / as good | vowels kept: key / shuffles / as good | '
        'best other language, vowels kept |')
    say('|---|---|---|---|---|')
    for title, lang, b2 in summary:
        if b2 is None:
            say('| %s | %s | too few signs for a reading test | | |' % (title, lang))
            continue
        v = b2.get('v', {})
        cv = '%.1f%% / %.1f%% / %d of 100' % (100 * v[lang][0], 100 * v[lang][1], v[lang][2]) if lang in v else ''
        others = [L for L in v if L != lang]
        ot = ''
        if others:
            o = max(others, key=lambda L: v[L][0] - v[L][1])
            ot = '%s %.1f%% / %.1f%% / %d of 100' % (o, 100 * v[o][0], 100 * v[o][1], v[o][2])
        say('| %s | %s | %.1f%% / %.1f%% / %d of 200 | %s | %s |' % (
            title, lang, 100 * b2[lang][0], 100 * b2[lang][1], b2[lang][2], cv, ot))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'bench.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:6])
