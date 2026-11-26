"""Build final.txt from pass2.txt: apply the resolutions of the pass 1 / pass 2 disagreements (checked on the image at 3.2x)
and the class refinements decided from the contact sheets. Every change is listed in CHANGES so it can be audited.
Usage: python build_final.py"""
import os
import tok

HERE = os.path.dirname(os.path.abspath(__file__))
rows = tok.parse(os.path.join(HERE, 'pass2.txt'))

# (line, x) -> (new code, new grade or None, reason)
CHANGES = {
    # resolutions of disagreements, 3.2x tiles res1.png / res2.png
    ('L1', 1825): ('I', 'doubtful', 'resolved: rubbed stem with black blobs at top and foot (pass 2 only)'),
    ('L1', 1905): ('.', 'likely', 'resolved: firm small black dot with a trail to the left'),
    ('L1', 2380): ('b', 'doubtful', 'resolved: rising bar of blobs, dotted head at right (pass 1 read ?)'),
    ('L1', 4225): ('?', 'doubtful', 'resolved: only a faint grey vertical smear, no ink; stem possible (pass 2 read I)'),
    ('L2', 3903): ('I', 'doubtful', 'resolved: thin beaded vertical stroke, thinner than the other stems'),
    ('L4', 2305): ('E', 'likely', 'resolved: two stacked black ovals with rubbed bars below, as in the stacked-bar sign of L5 and L8'),
    ('L4', 1692): ('I', 'likely', 'resolved: short thick black block with a notch'),
    ('L6', 3857): ('U', 'likely', 'resolved: slanting black left arm curving into a faint bottom, tall right arm (pass 1 read B)'),
    ('L8', 3683): ('W', 'likely', 'resolved: V cup whose right arm carries a thin top arm to 3779 (pass 1 read v plus a dash)'),
    # refinements from the contact sheets
    ('L6', 1758): ('o', None, 'merged e into o: solid leaf blob with a notch, same as L6@3448 and L7@3731'),
    ('L7', 3731): ('o', None, 'merged e into o'),
}
# solid rounded black blobs of about 40 px and more (contact sheet of c): o; small ovals, dots, rubbed blobs stay c
O = [('L3', 3318), ('L5', 4167), ('L6', 3448), ('L7', 4620), ('L8', 3097), ('L8', 3455), ('L8', 3992), ('L8', 4698),
     ('L4', 2025), ('L4', 4132), ('L4', 3300)]
for k in O:
    CHANGES[k] = ('o', None, 'contact sheet: solid black rounded blob (o), not a small oval or dot (c)')
# short thick bars (under about 70 px, no long tail): d; long bars with a head at the right stay b
D = [('L1', 2227), ('L1', 4150), ('L2', 3085), ('L2', 3357), ('L4', 1980), ('L4', 1743), ('L6', 1618), ('L6', 4545), ('L8', 3190)]
for k in D:
    CHANGES[k] = ('d', None, 'contact sheet of b: short thick bar (d), apart from the long rising bar with a head at the right (b)')
CHANGES[('L1', 4940)] = ('bb', None, 'contact sheet of b: heavy blob bar with a flag, one example')
CHANGES[('L3', 4262)] = ('Ds', None, 'contact sheet of V: thin short diagonal stroke, not a wedge')
CHANGES[('L3', 4627)] = ('Ds', None, 'contact sheet of V: thin short diagonal stroke, not a wedge')

out = []
log = []
for ln, x, code, grade, note in rows:
    k = (ln, x)
    if k in CHANGES and code not in ('|',):
        nc, ng, why = CHANGES[k]
        if nc != code or (ng and ng != grade):
            log.append('%s@%d %s(%s) -> %s(%s): %s' % (ln, x, code, grade, nc, ng or grade, why))
        code = nc
        grade = ng or grade
    out.append((ln, x, code, grade, note))

with open(os.path.join(HERE, 'final.txt'), 'w', encoding='utf-8') as f:
    f.write('# final positioned transcription of T-S K24.37 recto: pass 2 plus the resolutions and refinements in build_final.py\n')
    for ln, x, code, grade, note in out:
        f.write('%s|%d|%s|%s|%s\n' % (ln, x, code, grade, note))
with open(os.path.join(HERE, 'changes_from_pass2.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(log) + '\n')
print(len(log), 'changes written to changes_from_pass2.txt')
