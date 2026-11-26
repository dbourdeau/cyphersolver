"""name_step_o4.py (O4) - logged naming step of PREREG-O4 §4: the guard of measure_o4.py aborted before decoding on
reference-list names that have no row in key.tsv (13, @2, N6o, mx3 = composites of SIGNS.md / SHAPES-KEY-NAMES.md bases
with a raised mark). Each such token is renamed tS-<name> (no letter). Nothing else is changed."""
import re
REN = {'13', '@2', 'N6o', 'mx3'}
src = open('transcription_1548-03-12_P_merged.txt', encoding='utf-8').read().split('\n')
out = []; n = 0
for l in src:
    m = re.match(r'^(\d[rv] L\d\d: )(.*)$', l)
    if not m: out.append(l); continue
    t = m.group(2).split(); n += sum(x in REN for x in t)
    out.append(m.group(1) + ' '.join('tS-' + x if x in REN else x for x in t))
out.insert(3, '# Naming step (PREREG-O4 §4, tools/name_step_o4.py): %d tokens 13/@2/N6o/mx3 (no key row) renamed tS-<name>; nothing else changed.' % n)
open('transcription_1548-03-12_P_merged_named.txt', 'w', encoding='utf-8').write('\n'.join(out))
print(n, 'tokens renamed')
