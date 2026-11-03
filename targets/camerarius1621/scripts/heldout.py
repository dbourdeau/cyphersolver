"""Held-out test: values frozen from the n.63 glosses alone (Clm 10398, scans 287-289), applied to the code groups of
n.194 (Clm 10397), compared with the second-hand glosses written in n.194. Also checks that every glossed n.194 value
falls in the alphabetical slot between its n.63 neighbours (one-part code test). Standard library only.

Limits (stated after the independent check of 3 Nov 2026): the N63 dictionary below is typed into this script; nothing
in the folder proves it was written before n.194 was read. It covers 11 distinct groups and tests key values only,
graded against the n.194 glosses as transcribed by the solver. A gloss matches if its letters, with spaces and dots
removed, contain the stem or one of its listed abbreviations."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
# frozen from n.63 before n.194 was read (stems used for matching the glosses)
N63 = {'484': 'cam', '552': 'sachs', '553': 'sachs', '875': 'engl', '1214': 'gesandt', '1439': 'braunschw',
       '1441': 'lüneb', '1687': 'denn', '1814': 'legat', '2095': 'n.s', '1344': 'grosshofm'}
ORDER = [(211, 'Audienz'), (470, 'Calvinische'), (484, 'Camerarius'), (552, 'Chursachsen'), (722, 'Dennemarck'),
         (1214, 'Gesandte'), (1344, 'Grosshofmeister'), (1501, 'Hoe'), (1582, 'Instruction'), (1679, 'Koenig'),
         (1749, 'Land'), (1814, 'Legaten'), (2253, 'periculum'), (2368, 'Proposition'), (2503, 'Resolution'), (3034, 'Unirten')]
ABBR = {'1344': ('grhofm',), '553': ('churs',)}   # abbreviations of the same value seen in the glosses
hit = miss = untested = 0
glossed = {}
for l in (ROOT / 'n194' / 'code_groups_n194.tsv').read_text(encoding='utf8').splitlines():
    if l.startswith(('#', 'seq')): continue
    f = l.split('\t'); g, gl = f[3], f[5].lower()
    if gl not in ('-', '?') and not gl.startswith('?'): glossed[g] = f[5]
    if g in N63:
        if gl in ('-', '?') or gl.startswith('?'): untested += 1; print(f'{g}: n.63 says {N63[g]}; n.194 gloss illegible/absent')
        elif any(s in gl or s in gl.replace(' ', '').replace('.', '') for s in (N63[g],) + ABBR.get(g, ())): hit += 1
        else: miss += 1; print(f'{g}: MISMATCH n.63 {N63[g]} vs n.194 gloss {f[5]}')
print(f'held-out occurrences: agree {hit}, disagree {miss}, untestable {untested}')
bad = 0
for g, gl in sorted(glossed.items(), key=lambda x: int(x[0])):
    n = int(g); lo = max([o for o in ORDER if o[0] <= n], default=(0, 'A')); hi = min([o for o in ORDER if o[0] >= n], default=(9999, 'Z'))
    a = gl.lower().lstrip('[?').replace('v. ', '').replace('k. i', 'koenig').replace('k. in', 'koenig')[:1]
    flag = '' if lo[1][0].lower() <= a <= hi[1][0].lower() else '  OUT OF SLOT'
    bad += bool(flag)
    print(f'{g:>5} {gl:<24} between {lo[0]} {lo[1]} and {hi[0]} {hi[1]}{flag}')
print(f'glossed groups out of their n.63 slot (by first letter of the gloss): {bad}')
