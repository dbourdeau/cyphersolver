"""Integration check, 14 Nov 2026: decode transcription.txt with the State Department code WE028 under the
block reversal found for Anthony Morris's copy (this target; the folder was targets/claiborne1806 until it was
folded in here on 14 Nov 2026), and compare each word with Wagner's word.

    python targets/morris1813/claiborne/we028_check.py            # summary per letter
    python targets/morris1813/claiborne/we028_check.py --words    # every word, decoded

Key: ../beling/key/codebook_M97_13_transcription.csv (NARA M97 roll 13 frames 1056-1057, Weber's WE028),
column morris_number_after_reversal (Morris/Claiborne 100*i + r = WE028 100*(15-i) + r). Nothing here was built from
Claiborne's letters: the table is used unchanged. Corrections to the contributor's transcription seen on the NARA
images are applied from transcription_corrections.tsv (they are listed there, with the image).

A word counts as reproduced when the codebook values of its groups, joined (hook = -s, triangle = -ed), give Wagner's
word, allowing the code's syllable overlaps (a value may run one or two letters into the next, e.g. confide + en =
confid-en) and I/J, U/V merged; digits are digits. Everything else is listed as a misfit.
"""
import csv, re, sys, collections, pathlib

HERE = pathlib.Path(__file__).resolve().parent
KEY = HERE.parent / 'beling' / 'key' / 'codebook_M97_13_transcription.csv'

code = {}
for r in csv.reader(open(KEY, encoding='utf-8')):
    if r and r[0].isdigit():
        code[int(r[1])] = r[2]

corr = {}
cp = HERE / 'transcription_corrections.tsv'
if cp.exists():
    for line in open(cp, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        c = line.rstrip('\n').split('\t')
        corr[int(c[0])] = c[3]          # transcription.txt data line number -> corrected groups


def norm(s):
    s = s.lower().replace('i.j.', 'i').replace('uv', 'u')
    return re.sub(r'[^a-z0-9]', '', s.replace('j', 'i').replace('v', 'u'))


def fits(vals, word):
    """True if the values, with overlaps of up to two letters trimmed at each boundary, spell the word."""
    w = norm(word)
    states = {0}
    for v in vals:
        v = norm(v)
        if not v:
            return False
        nxt = set()
        for p in states:
            for back in (0, 1, 2):
                q = p - back
                if q < 0:
                    continue
                if back and w[q:p] != v[:back]:
                    continue
                if w.startswith(v, q):
                    nxt.add(q + len(v))
        states = nxt
        if not states:
            return False
    return len(w) in states


ok, tot, gok, gtot = (collections.Counter() for _ in range(4))
rows = []
n = 0
for line in open(HERE / 'transcription.txt', encoding='utf-8'):
    if line.startswith('#'):
        continue
    c = line.rstrip('\n').split('\t')
    if len(c) < 3:
        continue
    n += 1
    groups = corr.get(n, c[2]).split()
    vals = []
    for g in groups:
        m = re.match(r'(\d+)\??([LD]?)', g)
        v = code.get(int(m.group(1)), '') if m else ''
        vals.append(v + {'L': 's', 'D': 'ed'}.get(m.group(2) if m else '', ''))
    good = fits(vals, c[1])
    tot[c[0]] += 1; ok[c[0]] += good
    gtot[c[0]] += len(groups); gok[c[0]] += len(groups) if good else 0
    rows.append((n, c[0], c[1], ' '.join(groups), ' | '.join(vals), 'ok' if good else 'MISFIT'))

if '--words' in sys.argv:
    for r in rows:
        print('\t'.join(map(str, r)))
names = {'A': '24 Oct 1805', 'B': '13 Jan 1806', 'C': '25 Nov 1806'}
for L in 'ABC':
    print(f'{L} {names[L]}: words {ok[L]}/{tot[L]} ({ok[L]/tot[L]:.3f}); groups in those words {gok[L]}/{gtot[L]} ({gok[L]/gtot[L]:.3f})')
T, O, GT, GO = sum(tot.values()), sum(ok.values()), sum(gtot.values()), sum(gok.values())
print(f'all: words {O}/{T} ({O/T:.3f}); groups {GO}/{GT} ({GO/GT:.3f})')
print('misfits:')
for r in rows:
    if r[-1] != 'ok':
        print('  ', r[0], r[1], r[2], '=', r[3], '->', r[4])
