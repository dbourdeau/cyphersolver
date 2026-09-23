"""Lead 3: a published decipherment under the same controls. Yajnadevam's Sanskrit key
(github.com/yajnadevam/lipi, src/assets/data/xlits.csv: sign -> letter; inscriptions.csv:
his readings), on the same ICIT sign numbers as this folder.

K1  The key's shape: how many letter classes for how many signs; the ending slot under it.
K2  The null test. Each text (reading order) becomes a consonant skeleton under the key (his
    letter classes: s = s/sh/s./h, t = t/th/t./t.h, ...; vowels dropped, as the script leaves
    them to the reader). A text 'reads' to the extent its skeleton parses into Monier-Williams
    headword skeletons plus an optional one-consonant ending. Score: the share of consonants
    covered by words of 3+ consonants in the parse that maximises that coverage. The same is
    done for 200 random keys that shuffle his letter values among signs of similar frequency.
    If the real key reads no better than the shuffled ones, its readings are not evidence.
K3  The copper tablets under his readings: do the translations of the tablets name the
    animal on the other side?

Usage: python sanskrit_key_test.py xlits.csv inscriptions.csv mw.txt
Writes results/sanskrit_key_test.md.
"""
import csv
import os
import random
import re
import sys
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(17)
CLS = {'k': 'k', 'K': 'k', 'g': 'g', 'G': 'g', 'c': 'c', 'C': 'c', 'j': 'j', 'J': 'j', 't': 't', 'T': 't',
       'w': 't', 'W': 't', 'd': 'd', 'D': 'd', 'q': 'd', 'Q': 'd', 'n': 'n', 'R': 'n', 'N': 'n', 'Y': 'n',
       'M': 'n', 'p': 'p', 'P': 'p', 'b': 'b', 'B': 'b', 'm': 'm', 'y': 'y', 'r': 'r', 'f': 'r', 'l': 'l',
       'v': 'v', 'S': 's', 'z': 's', 's': 's', 'h': 's', 'H': 's'}
ENDINGS = set('smntyrv')


def say(s=''):
    OUT.append(s)
    print(s)


def skel_slp(w):
    return ''.join(CLS[c] for c in w if c in CLS)


def skel_xlit(x):
    x = x.replace('ṃ', 'n').replace('ś', 's').replace('ṣ', 's').replace('h', 's')
    return ''.join(c for c in x.lower() if c in 'kgcjtdnpbmyrlvs')


def mw_skeletons(path):
    sk = set()
    with open(path, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('<L>'):
                m = re.search(r'<k1>([^<]*)', ln)
                if m:
                    s = skel_slp(m.group(1))
                    if s:
                        sk.add(s)
    return sk


def coverage(s, words, maxlen=8):
    """Best parse of skeleton s into words (+ optional ending consonant); returns
    (parsable, consonants covered by words of 3+ consonants)."""
    n = len(s)
    best = [-1] * (n + 1)
    best[0] = 0
    for i in range(n):
        if best[i] < 0:
            continue
        for L in range(1, min(maxlen, n - i) + 1):
            w = s[i:i + L]
            ok = w in words or (L > 1 and w[:-1] in words and w[-1] in ENDINGS)
            if ok:
                v = best[i] + (L if L >= 3 else 0)
                if v > best[i + L]:
                    best[i + L] = v
    return best[n] >= 0, max(best[n], 0)


def score(texts, key, words):
    tot = long_ = parsed = 0
    for t in texts:
        s = ''.join(skel_xlit(key.get(g, '')) for g in t)
        if not s:
            continue
        ok, cov = coverage(s, words)
        parsed += ok
        long_ += cov
        tot += len(s)
    return parsed, long_ / tot if tot else 0


def main(xl, ins, mw):
    key = {}
    for r in csv.DictReader(open(xl, encoding='utf-8')):
        key[str(int(r['sign']))] = r['xlit']
    words = mw_skeletons(mw)
    rows = [r for r in load() if r['flat']]
    texts = [ln for r in rows for ln in r['seq'] if len(ln) >= 3]
    freq = Counter(g for t in texts for g in t)
    say('# A published Sanskrit key under the same controls (Yajnadevam)')
    say()
    say('## K1 The key')
    say()
    letters = Counter(skel_xlit(v) or '(vowel only)' for v in key.values())
    say('- %d signs keyed; %d distinct consonant skeletons among their values; the commonest: %s.' % (
        len(key), len(letters), ', '.join('%s x%d' % kv for kv in letters.most_common(10))))
    say('- The ending slot under the key: 740 = %r, 520 = %r; second slot 400 = %r, 90 = %r, 151 = %r; '
        'openers 817/820/861 = %r/%r/%r; the fish 220 = %r, the marked fish 235/240/233 = %r/%r/%r.' % tuple(
            key.get(g) for g in ('740', '520', '400', '90', '151', '817', '820', '861', '220', '235', '240', '233')))
    say()
    say('## K2 Does the key read better than a shuffled key?')
    say()
    real = score(texts, key, words)
    signs = sorted(freq, key=lambda g: -freq[g])
    bands = [signs[i:i + 10] for i in range(0, len(signs), 10)]
    sims = []
    for _ in range(200):
        k2 = dict(key)
        for b in bands:
            vals = [key.get(g, '') for g in b]
            random.shuffle(vals)
            for g, v in zip(b, vals):
                k2[g] = v
        sims.append(score(texts, k2, words))
    sims_cov = sorted(s[1] for s in sims)
    sims_par = sorted(s[0] for s in sims)
    ge = sum(1 for s in sims if s[1] >= real[1])
    say('- %d lines of 3+ signs; MW headword skeletons: %d.' % (len(texts), len(words)))
    say('- Real key: %d lines parse fully (%.0f%%); consonants covered by words of 3+ consonants: %.1f%%.' % (
        real[0], 100 * real[0] / len(texts), 100 * real[1]))
    say('- 200 shuffled keys (letter values permuted among signs of similar frequency): lines parsing fully '
        'median %d (range %d-%d); long-word coverage median %.1f%% (range %.1f-%.1f%%); shuffled keys as good '
        'as the real one: %d of 200.' % (sims_par[100], sims_par[0], sims_par[-1], 100 * sims_cov[100],
                                          100 * sims_cov[0], 100 * sims_cov[-1], ge))
    say()
    say('## K3 The copper tablets under his readings')
    say()
    tab, byid = {}, {}
    for r in csv.DictReader(open(ins, encoding='utf-8-sig')):
        tab.setdefault(r['cisi'], r)
        byid[r['id']] = r
    anim = {'Hare': r'\b(hare|rabbit|sasa|śaśa)', 'Elep': r'\b(elephant|gaja|hastin|nāga|naga|ibha)',
            'Anth': r'\b(archer|bow|arrow|hunter|dhanu|rudra|śiva)', 'Goat:8': r'\b(goat|aja|chāga|markhor)',
            'Rhin': r'\b(rhinoceros|khaḍga|gaṇḍa)', 'Tigr': r'\b(tiger|vyāghra|śārdūla)', 'Loop': r'\b(knot|loop)'}
    seen = set()
    for r in rows:
        if r['type'] != 'TAB:C' or r['motif'] not in anim:
            continue
        t = ' '.join(r['flat'])
        if (t, r['motif']) in seen:
            continue
        seen.add((t, r['motif']))
        y = tab.get(r['cisi'])
        tr = (y.get('translation') or '') if y else ''
        sk = (y.get('sanskrit') or '') if y else ''
        if tr.startswith('ref:') or sk.startswith('ref:'):
            ref = (sk if sk.startswith('ref:') else tr)[4:]
            z = byid.get(ref)
            if z:
                sk, tr = z.get('sanskrit') or '', z.get('translation') or ''
        hit = bool(re.search(anim[r['motif']], (sk + ' ' + tr).lower()))
        say('- %s (%s, %s): "%s" = "%s" -> names the picture: %s' % (
            r['cisi'], r['motif'], t, sk, tr[:90], 'yes' if hit else 'no'))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'sanskrit_key_test.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:4])
