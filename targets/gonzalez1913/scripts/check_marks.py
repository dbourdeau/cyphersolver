"""Rebuild the mechanical decryption from transcription + key_frozen.tsv and compare it with the
'Coded runs' section of a reading file, after undoing every mark. Fails on any unmarked departure.
usage: check_marks.py TRANSCRIPTION READING_MD [KEY_TSV]
Marks: {x/y} -> x (mechanical value), {+a} -> nothing, [?w:G1,G2] -> [G1][G2], [...:G] -> [G], [NN] stays.
Accents (not ñ), spaces and case are ignored."""
import sys, re, unicodedata, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import key, segs, dec

def flat(s):
    s = s.replace('ñ', '#').replace('Ñ', '#')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').replace('#', 'ñ').lower()
    return re.sub(r'[^a-zñ0-9\[\]?]', '', s)

def undo(r):
    r = re.sub(r'\{([^/{}+]*)/([^{}]*)\}', lambda m: m.group(1), r)
    r = re.sub(r'\{\+[^{}]*\}', '', r)
    r = re.sub(r'\[\?[^:\]]*:([^\]]*)\]', lambda m: ''.join('[' + g + ']' for g in m.group(1).split(',')), r)
    r = re.sub(r'\[\.\.\.:([^\]]*)\]', lambda m: ''.join('[' + g + ']' for g in m.group(1).split(',')), r)
    return r

k = key(sys.argv[3] if len(sys.argv) > 3 else None); mech = {sid: flat(''.join(dec(gr, k))) for sid, _, gr, _ in segs(sys.argv[1])}
runs = {}
text = open(sys.argv[2], encoding='utf8').read().split('## Coded runs')[1]
for ln in text.splitlines():
    m = re.match(r'^([SFCM]\d\d) \| (.*)$', ln)
    if m: runs[m.group(1)] = m.group(2)
bad = 0; marks = 0
for sid in mech:
    if sid not in runs:
        print('MISSING', sid); bad += 1; continue
    marks += len(re.findall(r'\{[^}]*\}|\[\?[^\]]*\]|\[\.\.\.[^\]]*\]', runs[sid]))
    got = flat(undo(runs[sid]))
    if got != mech[sid]:
        print('FAIL', sid, '\n  mechanical', mech[sid], '\n  reading   ', got); bad += 1
print(f'{len(mech)} runs, {marks} marks, {bad} failures:', 'PASS' if not bad else 'FAIL')
sys.exit(1 if bad else 0)
