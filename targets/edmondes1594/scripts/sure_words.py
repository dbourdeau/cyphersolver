"""Count the sure words of the reading by a stated rule and write reading/sure_words.tsv (15 Nov 2026).

Rule: a word is SURE when every letter is read and comes from the tested key, the shift set (7, 8, 10) frozen before
the held-out test (keys/frozen_key.json), with no value chosen by sense: the printed letter takes its commonest value
in this reading, and that value covers at least 70% of its uses (the same test as the ° mark of make_reading.py),
and the word is not weak (†, or "he will" across the printed roman "to").
Other statuses: "key, by sense" (every letter allowed by the tested key, at least one chosen by sense);
"outside key" (at least one letter needs shift 20, shift 11 or a value added by hand); "weak"; "unread" (a run of
printed letters not read); "sign" (a person sign or figure, not deciphered; 12 occurrences, listed in NOTES.md).
Also counts the read letters that lie outside the tested key.
Needs no language model. Usage: python3 -I scripts/sure_words.py
"""
import os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
A = 'abcdefghiklmnopqrstuwxyz'
TESTED = (7, 8, 10)
PREF = (7, 8, 10, 11, 20)
SIGNS = ['55', '55', 'm-sign', 'm-sign', 'ho-sign', 'oo-sign', '4s', '300', '300', '26', '26', '26']
WEAK = {('A9.0', 'by'), ('A9.0', 'gouuernor'), ('A10.1', 'relligion'), ('A7.0', 'some'), ('A10.0', 'h'), ('A10.1', 'ill')}

def read_ct(path):           # as scripts/poly.py
    segs, labels = [], []
    for l in open(path):
        if l[:1] not in 'AB' or ' ' not in l: continue
        lab, body = l.split(' ', 1)
        body = re.sub(r'\[[^\]]*\]', ' | ', body)
        for k, part in enumerate(body.split('|')):
            t = re.sub('[^a-z]', '', part)
            if len(t) >= 3: segs.append(t); labels.append(f'{lab}.{k}')
    return segs, labels

def cipher_of(c): return {'u': 'n', 'v': 'u'}.get(c, c)
def shift(c, p):             # as scripts/make_reading.py
    cands = [(A.index(p) - A.index(cc)) % 24 for cc in ({'u': ['n', 'u']}.get(c) or [cipher_of(c)])]
    return sorted(cands, key=lambda k: (k not in PREF, k))[0]

segs, labels = read_ct(os.path.join(ROOT, 'transcription', 'pass1.txt'))
words = dict(l.split('\t') for l in open(os.path.join(ROOT, 'reading', 'reading_words.tsv')).read().splitlines()[1:])
vals = collections.defaultdict(collections.Counter)
for lab, s in zip(labels, segs):
    for c, p in zip(s, words[lab].replace(' ', '')):
        if p != '?': vals[c][p] += 1
def by_sense(c, p):
    v = vals[c]
    if len(v) < 2: return False
    top, n = v.most_common(1)[0]
    return p != top or n < 0.7 * sum(v.values())

rows, cnt, letters, outside = [], collections.Counter(), 0, collections.Counter()
for lab, s in zip(labels, segs):
    i = 0
    for w in words[lab].split():
        cs = s[i:i + len(w)]; i += len(w)
        if '?' in w: rows.append((lab, w, 'unread', '')); cnt['unread'] += 1; continue
        sh = [shift(c, p) for c, p in zip(cs, w)]
        letters += len(sh)
        for k in sh:
            if k not in TESTED: outside[k if k in (11, 20) else 'hand'] += 1
        if (lab, w) in WEAK: st = 'weak'
        elif any(k not in TESTED for k in sh): st = 'outside key'
        elif any(by_sense(c, p) for c, p in zip(cs, w)): st = 'key, by sense'
        else: st = 'sure'
        cnt[st] += 1
        rows.append((lab, w, st, ' '.join(f'{c}{p}{k}' for c, p, k in zip(cs, w, sh))))
for g in SIGNS: rows.append(('sign', g, 'sign', '')); cnt['sign'] += 1
tot = sum(cnt.values()); sure = cnt['sure']; inkey = sure + cnt['key, by sense']
nout = sum(outside.values())
summary = (f'# words {tot}: sure {sure} of {tot} ({sure / tot:.1%}); every letter allowed by the tested key {inkey} of {tot}; '
           f'outside key {cnt["outside key"]}, weak {cnt["weak"]}, unread runs {cnt["unread"]}, signs {cnt["sign"]}\n'
           f'# read letters {letters}; outside the tested key {nout} (shift 20: {outside[20]}, shift 11: {outside[11]}, '
           f'other values added by hand: {outside["hand"]})\n')
with open(os.path.join(ROOT, 'reading', 'sure_words.tsv'), 'w') as f:
    f.write('# Written by scripts/sure_words.py; the rule is in its docstring.\n' + summary +
            '# letters: printed letter, plain letter, shift on the 24-letter alphabet\n'
            'segment\tword\tstatus\tletters\n')
    for r in rows: f.write('\t'.join(r) + '\n')
print(summary, end='')
