"""Write legend.txt (shape classes with counts per grade) and doubts.txt (every likely and doubtful sign) from final.txt."""
import os
import collections
import tok

HERE = os.path.dirname(os.path.abspath(__file__))
rows = tok.parse(os.path.join(HERE, 'final.txt'))

DESC = {
    'J': 'upright stem with a foot running to the LEFT (flat, hooked or long thin; one continuum, not split); top often a blotchy cap',
    'Jd': 'J whose foot is a thick diagonal approaching from the upper left',
    'L': 'upright stem with a foot running to the RIGHT (often ending in a ball or an upturn)',
    'I': 'plain upright stem with no foot, thick and blotchy (four rubbed or thin examples are doubtful)',
    'R': "bracket ']' : top bar and bottom bar running left from a right-hand stem, open on the left",
    'r': 'small bracket (about half height): top bar, left stem, bottom bar pointing right; one example',
    'B': 'closed rectangular box, usually with a flag or a stem rising from the top right corner',
    'U': 'cup: two arms joined by a bottom curve (left arm short or tall, right arm tall)',
    'u': 'small black cup or bowl with a tick at an upper corner (about half height)',
    'Uc': 'thin cup with a black oval blob standing in its mouth (two examples)',
    'C': 'large open ring, opening to the right, with an inner curl',
    'O': 'bowl carrying a Y or cross of two strokes inside (the ring with cross); one example',
    'S': 'wave bar: ball at the left, arching bar, tail running down to the right',
    'G': 'stem at the left with a top bar rising to the right and ending in a hook',
    'A': 'slanted stem, curved foot to the right, arm at the upper right; one example',
    'H': 'stem with a rising top arm and a small mid bar (G or H); one doubtful example',
    'K': 'slanting stem with a flag at the top left and a diagonal arm to the lower right ending in a ball (three identical examples)',
    'W': 'stem or V cup with a diagonal from the upper left into its foot and a top arm running right',
    'X': 'two crossed diagonals, often dotted, with a blob at one end',
    'Y': 'fork: dotted diagonal from the upper left and twigs from the upper right meeting in a black blob; one example',
    'Z': 'angular zigzag: top bars, a thick diagonal, a bottom bar running left',
    'M': 'down-stroke, thick diagonal, a branch to the upper right and a tail down to the right; one example',
    'P': 'stem ending in a bowl that curves right and curls up (a 6); one example',
    'N': 'arch open at the bottom, heavy left leg; one example',
    'T': 'top bar of two joined blobs with a tall oval blob below at the right (c + I?); one doubtful example',
    'E': 'two or three stacked short bars (an equals sign)',
    'V': 'small black pointed wedge (pointing down or down-left)',
    'Ds': 'thin short diagonal stroke (backslash)',
    'D': 'long diagonal or curved diagonal stroke, 120-150 px, often with a side arm or ticks at the right',
    'wd': 'black wedge: thin top bar bending down into a blob at the right; one example',
    'o': 'solid black rounded blob of about 40-55 px (leaf, bean or oval), sometimes with a notch',
    'c': 'small oval, dot-like blob or rubbed blot (under about 35 px)',
    'b': 'long bar (90 px and more), usually rising to the right, with a heavy head or ring at the right and a thin tail at the left',
    'd': 'short thick bar (under about 70 px), ball at the left or none',
    'bb': 'heavy blob bar with a flag at the top right; one example',
    'b^': 'bar floating 30-50 px above the line (over a U in line 1, high in lines 4 and 8)',
    '-': 'dash divider (thin bar at mid height, often dotted, 50-140 px)',
    '.': 'dot divider or isolated dot',
    '?': 'sign present but not classifiable (rubbed, blotted or torn)',
    '|': 'hole, tear or rubbed zone where signs are lost (extent in final.txt notes)',
}
cnt = collections.defaultdict(collections.Counter)
for ln, x, c, g, n in rows:
    cnt[c][g] += 1
with open(os.path.join(HERE, 'legend.txt'), 'w', encoding='utf-8') as f:
    f.write('Shape classes of transcription.txt (T-S K24.37 recto, second reading, 24 Nov 2026). Descriptions of the printed shape,\n')
    f.write('not claims of identity. Counts: total (firm / likely / doubtful). Class letters are arbitrary labels, not letters of a script.\n')
    f.write('Merge and split decisions: build_final.py (CHANGES) and the contact sheets; the J class was kept whole after comparing 31 examples.\n\n')
    order = sorted([c for c in cnt if c not in ('-', '.', '?', '|')], key=lambda c: -sum(cnt[c].values()))
    for c in order + ['-', '.', '?', '|']:
        if c not in cnt:
            continue
        v = cnt[c]
        tot = sum(v.values())
        if c in ('|',):
            f.write('%-3s %3d              %s\n' % (c, tot, DESC[c]))
        else:
            f.write('%-3s %3d (%d / %d / %d)  %s\n' % (c, tot, v['firm'], v['likely'], v['doubtful'], DESC[c]))
with open(os.path.join(HERE, 'doubts.txt'), 'w', encoding='utf-8') as f:
    f.write('Doubt list for final.txt: every sign graded likely or doubtful, with the reason. firm = shape and class seen clearly on both\n')
    f.write('readings; likely = class seen but part of the shape faint, rubbed or on a damage; doubtful = class or even presence uncertain.\n\n')
    for g in ('doubtful', 'likely'):
        f.write('== %s ==\n' % g)
        for ln, x, c, gr, n in rows:
            if gr == g and c != '|':
                f.write('%s@%d %s  %s\n' % (ln, x, c, n))
        f.write('\n')
print('legend.txt, doubts.txt written')
