"""The Vedic substrate words: do the words Witzel (1999) calls Southern Indus ('Meluhhan') look Dravidian or Munda?

Witzel, 'Substrate languages in Old Indo-Aryan' (EJVS 5, 1999), sorts non-Indo-European words of the Vedic texts by
proposed source: Dravidian loans (his 1.6), Para-Munda (1.2, many chosen for Munda-like prefixes ka- / ki- / ku-),
and the 'Southern Indus language: Meluhhan' (1.9), which he takes to be neither Dravidian nor Munda. The 93 words
of his tables were extracted to CSV (scratchpad; checked by hand only for the groups used here).

S1  Sound-pattern models: character trigram models (add-0.1 smoothing) of Dravidian (DEDR forms), Munda (JAMBU),
    Burushaski and Sanskrit (Monier-Williams headwords), on words reduced to plain letters (diacritics dropped,
    aspirates kept as consonant + h). Each word gets the mean log-probability per character under each model.
S2  Dravidian-ness = log P(Dravidian) - log P(Munda), per character, minus the same for 500 random Sanskrit
    headwords (the control: all these words come to us in Sanskrit spelling). Groups: Witzel's Dravidian loans
    (positive control for Dravidian), his Para-Munda words (positive control for Munda, and circular, since they
    were chosen for their prefixes), and the Meluhhan words.

Usage: python substrate.py <mw.txt> <dedr forms.csv> <sux_gloss.tsv> <scout folder> <witzel1999_words.csv>
Writes results/substrate.md.
"""
import csv
import math
import os
import random
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict

import bench

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def plain(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if not unicodedata.combining(c))
    return ''.join(c for c in w if 'a' <= c <= 'z')


class LM:
    def __init__(self, words):
        self.c3, self.c2 = Counter(), Counter()
        self.V = set()
        for w in words:
            s = '^^' + plain(w) + '$'
            if len(s) < 4:
                continue
            for i in range(2, len(s)):
                self.c3[s[i - 2:i + 1]] += 1
                self.c2[s[i - 2:i]] += 1
                self.V.add(s[i])

    def lp(self, w):
        s = '^^' + plain(w) + '$'
        V = len(self.V) or 27
        tot = 0.0
        for i in range(2, len(s)):
            tot += math.log((self.c3[s[i - 2:i + 1]] + 0.1) / (self.c2[s[i - 2:i]] + 0.1 * V))
        return tot / (len(s) - 2)


def main(mw, dedr, sux, scout, words_csv):
    rng = random.Random(149)
    _, _, raw = bench.lexicons(mw, dedr, sux)
    raw.update({L: v for L, v in bench.extra_raw(scout).items() if v})
    lms = {L: LM(raw[L]) for L in ('dra', 'mu', 'bu', 'sa')}
    ws = list(csv.DictReader(open(words_csv, encoding='utf-8')))
    groups = defaultdict(list)
    for r in ws:
        src = r['proposed_source']
        k = ('Witzel: Dravidian loans (1.6)' if src == 'Dravidian' else
             'Witzel: Para-Munda (1.2, 1.4, 2.3)' if 'Munda' in src else
             None)
        if k:
            groups[k].append(r['word'].split('-')[0] if r['word'] else r['word'])
    groups['Witzel 1.9, Southern Indus / Meluhhan (his forms, by hand)'] = ['sinda', 'ili', 'ellu', 'nankal', 'godi',
                                                                            'kangu', 'meluhha']
    ctrl = rng.sample([w for w in raw['sa'] if 4 <= len(plain(w)) <= 10], 500)

    def dm(w):
        return lms['dra'].lp(w) - lms['mu'].lp(w)
    base = statistics.mean(dm(w) for w in ctrl)
    say('# Witzel\'s substrate words: Dravidian-looking or Munda-looking?')
    say()
    say('Dravidian-ness = mean log-probability per character under a Dravidian model minus a Munda model, relative to '
        '500 random Sanskrit headwords (%.3f). Positive = more Dravidian-like than ordinary Sanskrit words.' % base)
    say()
    say('| group | words | Dravidian-ness, mean (range) | words more Dravidian-like than Munda-like |')
    say('|---|---|---|---|')
    for k in ('Witzel: Dravidian loans (1.6)', 'Witzel: Para-Munda (1.2, 1.4, 2.3)',
              'Witzel 1.9, Southern Indus / Meluhhan (his forms, by hand)'):
        v = [dm(w) - base for w in groups[k] if plain(w)]
        if not v:
            continue
        say('| %s | %d | %+.3f (%+.2f to %+.2f) | %d of %d |' % (k, len(v), statistics.mean(v), min(v), max(v),
                                                               sum(1 for x in v if x > 0), len(v)))
    say()
    say('- Meluhhan forms and their scores: %s.' % ', '.join(
        '%s %+.2f' % (w, dm(w) - base) for w in groups['Witzel 1.9, Southern Indus / Meluhhan (his forms, by hand)']))
    say()
    say('Reading: the positive control fails - the Dravidian loans of Witzel are no more Dravidian-like than ordinary '
        'Sanskrit words (mean near zero), while the Para-Munda words look Munda-like only because they were chosen '
        'for their Munda-like prefixes. The sound-pattern model cannot tell the families apart in Sanskrit spelling, '
        'and the Southern Indus language of Witzel is a handful of reconstructed forms (several reconstructed from '
        'Dravidian cognates). No test is possible here; the case of Witzel rests on etymology, not on anything this '
        'script can check. His position (Northern Indus = Para-Munda, prefixing; Southern Indus = Meluhhan, neither '
        'Dravidian nor Munda) is the main alternative to the Dravidian reading and is recorded as such.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'substrate.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:6])
