"""Record the terminal-pair and Dutchman-page tests in both profiles and notes. Run from the repository root."""
import json
DAY = '2026-11-02'
steps = [
 {'date': DAY, 'kind': 'statistics', 'what': 'Terminal-pair profile against the 13040 and 18470 families, which survives page renumbering: nothing beyond chance. System A against 13040 reached 0.864 on a mixed reference, then z = 1.9 on the 270 clean group-word pairs, across many comparisons: noise.', 'result': 'failed'},
 {'date': DAY, 'kind': 'sibling key', 'what': 'Quoted 18470 groups converted through the double-numbered page lists Mendelsohn prints for 37000, 29000 and 2500, against shuffled page pairs: every family inside the control range. Only those listed pages can be converted, so this tests a fraction of each code.', 'result': 'ruled out'},
]
for t in ('stockholm1918', 'ludendorff1918'):
    p = f'targets/{t}/profile.json'
    d = json.load(open(p, encoding='utf-8'))
    d['solution'] += [s for s in steps if s not in d['solution']]
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, ensure_ascii=False, indent=1); f.write('\n')
n = open('targets/stockholm1918/NOTES.md', encoding='utf-8').read()
old = '5. **Printed cribs.**'
new = ('5. **Terminal pairs, which survive page renumbering** (`work/terminal.py`, `work/terminal2.py`). A family member should share the\n'
       '   last-two-figure profile of its family. Nothing beyond chance. A against 13040 first reached 0.864 (control maximum 0.868), then\n'
       '   z = 1.9 on the 270 clean group-word pairs, across many comparisons: noise. The Bernstorff text, as a control, gave z = -3.1.\n'
       '6. **The "Dutchman" codes, in part.** Mendelsohn prints only their double-numbered pages. 18470 groups converted through those lists\n'
       '   for 37000, 29000 and 2500, against shuffled pairs: all inside the control range (best: B on 37000, 12 hits, control mean 7.1, maximum\n'
       '   17). This covers only a fraction of each code. 20000 could not be parsed from the OCR.\n'
       '7. **Printed cribs.**')
if '**Terminal pairs' not in n: n = n.replace(old, new)
n = n.replace('Not tested: the "Dutchman" codes 2500, 37000, 29000, 20000, 9700, 5300 (Mendelsohn describes them, but the page tables\nwere never printed).',
              'Not tested beyond the partial lists in step 6: the "Dutchman" codes 2500, 37000, 29000, 20000; not tested at all: 9700, 5300 (Mendelsohn\ndescribes them, but the full page tables were never printed).')
open('targets/stockholm1918/NOTES.md', 'w', encoding='utf-8', newline='\n').write(n)
print('ok')
