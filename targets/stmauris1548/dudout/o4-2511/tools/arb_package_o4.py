"""arb_package_o4.py (O4) - builds ARBITRAGE/CANDIDATS-DESCRIPTIONS.md for blind arbitrator C: the shape descriptions of
SIGNS.md and SHAPES-KEY-NAMES.md (as given, no values) + each pass's own t-shape descriptions and naming conventions
(copied from the pass headers, renamed tA-/tB-). Never reads the key. disputes.json is written by compare_o4.py write."""
import re
out = ['# Candidate names and shape descriptions for arbitration (shapes only, NO values)\n',
       '## Reference list 1 — input/SIGNS.md (WAINUT)\n', open('input/SIGNS.md').read().split('\n', 2)[2],
       '\n## Reference list 2 — input/SHAPES-KEY-NAMES.md (WAINUT)\n', open('input/SHAPES-KEY-NAMES.md').read().split('\n', 2)[2]]
for X in 'AB':
    h = [l for l in open('passe-%s/transcription_pass%s.txt' % (X, X)) if l.startswith('#')]
    out.append('\n## Pass %s — its own t-shapes (renamed t%s-...) and naming conventions, as written in its header\n' % (X, X))
    for l in h:
        if re.search(r'\bt\d+\s', l) or 'onvention' in l or re.search(r'`?(\+o|@2|12|phi|b|N15)`? ?=', l) or l.startswith('#   ') :
            out.append(re.sub(r'\bt(\d+)\b', r't%s-t\1' % X, l.lstrip('#').rstrip()) + '\n')
open('ARBITRAGE/CANDIDATS-DESCRIPTIONS.md', 'w').write(''.join(out))
