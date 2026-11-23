"""POST HOC, NOT COUNTED. Where a run stops giving words, the 3-1-3 cycle is resumed at a stated letter.
First noticed by the independent reviewer (one shift of the cycle per run); restated on 23 Nov 2026 after a third,
blind transcription confirmed every sign of these runs: in each case the cycle restarts (shift 3) at the first letter
of a word ("restart"), as the Sanchez letter (targets/sanchez1922) does at every word, or a run continues the cycle
of the run before it across a colon ("continue"). f3.20 needs a second, one-place skip inside PROPIA ("<+1>"), which
the restart rule does not cover. The letters after each point are the unedited output of that phase.
Nothing here enters the counts in NOTES.md or profile.json.
python scripts/posthoc_shift.py > posthoc_shift.txt"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import runs, A
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {rid: s.replace('/', '') for rid, _, _, s in runs(os.path.join(here, 'transcription_DCXXI.6.588.1.txt'))}
# run id: list of (letter index, 0-based in the run's letters with "/" removed, where the key position changes; new key position)
# key position 0 = shift 3 (a restart); for "continue", the key position the previous run would reach.
POINTS = {
    'f2.19': [(16, 0, 'restart')],                                   # PAULATINAS
    'f3.10': [(10, 0, 'restart')],                                   # DE LAS PERSONAS ...
    'f3.13': [(0, len(T['f3.12']) % 3, 'continue f3.12')],           # f3.12 has 130 letters: 130 mod 3 = 1
    'f3.20': [(20, 0, 'restart'), (57, (57 - 20 + 1) % 3, '+1')],         # BONILLA ...; PROP<+1>IA
}
def dec_from(s, pos):
    return ''.join(A[(A.index(c) - [3, 1, 3][(pos + i) % 3]) % 27] if c in A else c for i, c in enumerate(s))
print('# POST HOC, NOT COUNTED: restarts of the 3-1-3 cycle (rule and reasons in scripts/posthoc_shift.py and NOTES.md)')
for rid, pts in POINTS.items():
    s = T[rid].replace('?', 'Ñ')   # f2.19 sign 20: Ñ typed over B (blind passes 2 and 3); as a letter of PAULATINAS it gives L
    out, prev, pos = '', 0, 0
    for at, newpos, label in pts:
        out += dec_from(s[prev:at], pos) + f'<{label}>'
        prev, pos = at, newpos
    out += dec_from(s[prev:], pos)
    print(f'{rid}\t{out}')
