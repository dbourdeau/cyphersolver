"""POST HOC, NOT COUNTED. Rule (written after the reviewer's observation, 23 Nov 2026): where a run stops giving
words, the 3-1-3 cycle may be resumed one or two places on (phase 1 or 2) from one stated letter to the end of the
run, once per run; an unreadable sign ("?") may instead be dropped (the typist's struck sign), which is the same as a
one-place shift. The point is marked <+1> or <+2> (or <drop>) in the output. The letters after the point are the
unedited output of that phase. Nothing here enters the counts in NOTES.md or profile.json.
python scripts/posthoc_shift.py > posthoc_shift.txt"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import runs, A
def dec(s, phase=0):
    return ''.join(A[(A.index(c) - [3, 1, 3][(i + phase) % 3]) % 27] for i, c in enumerate(s))
# run id: (letter index where the shift starts, 0-based in the run's letters with "/" removed; phase or 'drop')
SHIFTS = {'f2.19': (19, 'drop'), 'f3.10': (10, 2), 'f3.13': (0, 1), 'f3.20': (20, 1)}
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {rid: s.replace('/', '') for rid, _, _, s in runs(os.path.join(here, 'transcription_DCXXI.6.588.1.txt'))}
print('# POST HOC, NOT COUNTED: one shift of the 3-1-3 cycle per run (rule in scripts/posthoc_shift.py)')
for rid, (at, ph) in SHIFTS.items():
    s = T[rid]; head = dec(s[:at]) if at else ''
    if ph == 'drop':
        head = dec(s[:at]); tail = s[at + 1:]; out = head + '<drop>' + dec(tail, at % 3)
    else:
        out = head + f'<+{ph}>' + dec(s[at:], (at + ph) % 3)
    print(f'{rid}\t{out}')
