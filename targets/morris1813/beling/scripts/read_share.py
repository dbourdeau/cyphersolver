#!/usr/bin/env python3
"""Read share of the five catalogue 650 letters: coded groups (heading, body, signature) minus the groups left
unread or read only by inference, over all coded groups. Run from any folder: python3 read_share.py

The lists of unread and inferred groups are taken by hand from each letter's reading.txt; they are the only judgment
in this count. Unread: [370], the sign after full stops, and [575.1060] in No. 19. Inferred ([?word], or a value
that misfits its key entry): 145 and 131 in No. 18 ("relative", "re"), 1457, 1040; 572, 1101, 1150 in No. 19;
593.813 and 1569 in No. 24. Python standard library only."""
import pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import decode650 as D

L = HERE.parent / 'letters'
LET = {
 'No. 18 (20 Sep 1814)': (L / '1814-09-20_No18' / 'transcription.txt',
     {'unread': [('112.08', 370), ('112.11', 370), ('113.04', 370), ('113.09', 370)],
      'inferred': [('112.02', 145), ('113.05', 145), ('112.07', 131), ('112.10', 1457), ('112.13', 1040)]}),
 'No. 19 (27 Oct 1814)': (L / '1814-10-27_No19' / 'transcription.txt',
     {'unread': [('139.04', 370), ('139.08', 370), ('139.08', 575), ('139.08', 1060)],
      'inferred': [('139.06', 572), ('139.06', 1101), ('139.05', 1150)]}),
 'No. 24 (30 Dec 1814)': (L / '1814-12-30_No24' / 'transcription.txt',
     {'unread': [('220.04', 370)], 'inferred': [('220.01', 593), ('220.01', 813), ('220.03', 1569)]}),
 'No. 25 (6 Jan 1815)': (L / '1815-01-06_No25' / 'transcription.txt', {'unread': [], 'inferred': []}),
 'No. 28 (12 May 1815)': (L / '1815-05-12_No28' / 'transcription.txt', {'unread': [], 'inferred': []}),
}
for name, (f, fl) in LET.items():
    toks = [(lab, t[1]) for lab, ts in D.load(f) for t in ts if t[0] == 'code']
    for lab, g in fl['unread'] + fl['inferred']:     # every flagged group must be where the list says
        assert (lab, g) in toks, (name, lab, g)
    n = len(toks)
    u, i = len(fl['unread']), len(fl['inferred'])
    print(f"{name}: groups {n}, distinct {len({g for _, g in toks})}, unread {u}, inferred {i}, read {n-u-i} = {(n-u-i)/n:.3f}")
