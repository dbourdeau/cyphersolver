# count.py [FOLDER]  (run from anywhere; FOLDER defaults to the folder above this script)
# Writes counts.txt, units/units_from_seg.tsv and units/petkum_1665-11-30_R2.units.tsv. Standard library only; run with python3 -I.
#
# COUNTING RULE (one rule for every letter in this folder; the rule of our issues #443 and #444):
#   unit = one word of the plaintext as divided by the reader (a word may span several cipher tokens; a code word is one unit).
#   S = every token of the word has a spelled value in the key (letter or syllable, tier A or B) and the word reads as French as written.
#   E = the word is (or contains) a code word (a value longer than three letters, or 'et'), even when the chancery glossed it.
#   N = any token not in the key, any token marked unsure (~), any tier C (one-anchor row) value, or a spelling that does not read (!N).
#   strict share = S / (S + E + N).  S+E is given for information only and is not a share read.
# Three sources of labels, all in units/:
#   *.seg         segmentation 'tokens unit [!N note]'; labels are computed here from key.tsv (logic of the contributor's units_seg.py, b96)
#                 and the flattened tokens are asserted equal to the frozen transcription, token for token.
#   *.units.tsv   labels given by the reader per unit when the letter was first decoded (30 Nov 1665 R1, Paulmyer); counted as they stand.
#   R2 of 30 Nov  the R1 labels with the 23 explicit changes of the contributor's units_R2.py (b96), applied and asserted here.
import sys, os, re, collections

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(HERE)
def P(*a): return os.path.join(F, *a)

def load_key(path):
    key = {}
    for l in open(path, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        p = l.rstrip('\n').split('\t'); key[p[0]] = (p[1], p[2])
    return key

KEY = load_key(P('key.tsv'))

def frozen_tokens(tx):
    return [t.strip() for l in open(tx, encoding='utf8') if not l.startswith('#') and '|' in l
            for r in re.findall(r'<([^>]*)>', l) for t in r.split('.') if t.strip()]

def label_seg(seg, tx, face_value=False):
    """units_seg.py logic. face_value=True strips the unsure mark ~ before the key lookup (reported separately, never the count of record)."""
    rows = []; flat = []; c = collections.Counter()
    for l in open(seg, encoding='utf8'):
        if not l.strip(): continue
        p = l.rstrip('\n').split(' ', 2); toks = p[0].split('.'); flat += toks
        look = [t.rstrip('~') for t in toks] if face_value else toks
        note = ''
        if any(t not in KEY for t in look): lab = 'N'; note = 'unknown/unsure token: ' + ','.join(t for t in look if t not in KEY)
        elif any(KEY[t][1] == 'C' for t in look): lab = 'N'; note = 'tier C (one-anchor row)'
        elif len(p) > 2 and p[2].startswith('!N'): lab = 'N'; note = p[2][2:].strip()
        elif any(len(KEY[t][0]) > 3 or KEY[t][0] == 'et' for t in look): lab = 'E'; note = 'code word'
        else: lab = 'S'
        c[lab] += 1; rows.append((p[0], p[1], lab, note))
    fz = frozen_tokens(tx)
    assert flat == fz, 'token mismatch %s at %d' % (seg, next(i for i, (a, b) in enumerate(zip(flat + ['END'], fz + ['END'])) if a != b))
    return c, rows, len(flat)

def label_tsv(path):
    rows = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf8') if l.strip() and not l.startswith('#')]
    ncol = min(len(r) for r in rows)
    col = next(i for i in range(ncol) if all(r[i] in ('S', 'E', 'N') for r in rows))
    return collections.Counter(r[col] for r in rows), rows, col

# --- the 23 relabels of units_R2.py (b96), copied verbatim ---
CHG573 = {('L01','[165]urs'):('{Ambassade}urs','E','165 glossed (574R), v3'),('L02','pfos'):('plus','S','R2+crop: 270'),('L02','dou[U4]'):('doux','S','U4=x glossed 574R'),
('L10','[116]'):('{la France}','E','v3'),('L15','[350]'):('{Royaume}','E','v3'),('L29','[165]urs'):('{Ambassade}urs','E','v3'),('L29','[61]'):('{le Roy T.C.}','E','v3'),
('R01','[61]'):('{le Roy T.C.}','E','v3'),('R02','[165]urs'):('{Ambassade}urs','E','v3'),('R02','persuade[HB]'):('persuadez','S','HB=z glossed 574R'),('R07',"l'[165]ur"):("l'{Ambassade}ur",'E','v3'),
('R09','[74]'):("{l'Empereur}",'E','v3'),('R09','[88]'):("{l'Espagne}",'E','v3'),('R13','[116]'):('{la France}','E','v3'),('R13','pfos'):('plus','S','R2+crop: 270'),
('R16','[153]'):('{Anglois}','E','v3'),('R19','[209]'):('{estre}','E','v3'),('R22','au[U4]'):('aux','S','U4=x'),('R22','[153]'):('{Anglois}','E','v3'),('R24','eu[U4]'):('eux','S','U4=x'),('R33','yeu[U4]'):('yeux','S','U4=x')}
CHGH = {('A08','opliger'):('o[Q]liger','N','crop: sign is plain Q (unknown in v3), not G'),('D01','avic'):('avec','S','R2+crop: 381')}

def relabel_R2():
    out = []; per = {}
    for f, chg, name in ((P('units', 'petkum_1665-11-30_p2-3_R1.units.tsv'), CHG573, 'p2-3 (573)'),
                         (P('units', 'petkum_1665-11-30_p1-p4_R1_heldout.units.tsv'), CHGH, 'p1+p4 (572R+574L)')):
        c = collections.Counter(); used = set()
        for l in open(f, encoding='utf8'):
            if l.startswith('#') or not l.strip(): continue
            p = l.rstrip('\n').split('\t'); k = (p[0], p[1])
            if k in chg:
                used.add(k); u, lab, note = chg[k]; p = [p[0], u, lab, note + ' (was %s %s)' % (p[1], p[2])]
            c[p[2]] += 1; out.append([name] + (p[:4] if len(p) > 3 else p + ['']))
        assert used == set(chg), set(chg) - used
        per[name] = (c, len(used))
    with open(P('units', 'petkum_1665-11-30_R2.units.tsv'), 'w', encoding='utf8') as w:
        w.write('# written by scripts/count.py: R1 units of 30 Nov 1665 with the 23 relabels of units_R2.py (blind R2 adjudicated, KEY_v3 unchanged)\n# part\tline\tunit\tlabel\tnote\n')
        for r in out: w.write('\t'.join(r) + '\n')
    return per

def pct(a, b): return '%d/%d = %.2f%%' % (a, b, 100.0 * a / b)
def line(name, c, extra=''):
    n = c['S'] + c['E'] + c['N']
    return '%-34s S %3d + E %3d + N %3d = %3d units; strict %s; S+E %s%s' % (name, c['S'], c['E'], c['N'], n, pct(c['S'], n), pct(c['S'] + c['E'], n), extra)
def pool(name, parts):
    t = collections.Counter()
    for _, c in parts: t += c
    s = ' + '.join(str(c['S']) for _, c in parts); e = ' + '.join(str(c['E']) for _, c in parts); nn = ' + '.join(str(c['N']) for _, c in parts)
    u = ' + '.join(str(c['S'] + c['E'] + c['N']) for _, c in parts)
    n = t['S'] + t['E'] + t['N']
    return ['POOL %s (%s)' % (name, ', '.join(k for k, _ in parts)),
            '  S = %s = %d' % (s, t['S']), '  E = %s = %d' % (e, t['E']), '  N = %s = %d' % (nn, t['N']),
            '  units = %s = %d; strict %s; S+E %s' % (u, n, pct(t['S'], n), pct(t['S'] + t['E'], n))], t

L = ['counts.txt: written by scripts/count.py (python3 -I). Do not edit by hand.',
     'Rule: strict = S/(S+E+N) per word unit; code words count E (not read) even when glossed; unknown, unsure (~), tier C or non-reading spellings count N. Full rule in the head of scripts/count.py.',
     'key.tsv md5 must be ddc02e4a9408e8ead7d51b5135a1ae82 (KEY_v3); checked below.', '']
import hashlib
km = hashlib.md5(open(P('key.tsv'), 'rb').read()).hexdigest(); assert km == 'ddc02e4a9408e8ead7d51b5135a1ae82', km
L.append('key.tsv md5 %s OK' % km); L.append('')

# A. #443, 30 Nov 1665
L.append('A. Petkum to Biermann, Oxford 30 Nov 1665 (issue #443)')
L.append('A1. First transcription R1, labels as made at the first decode (p2-3 under key v1, p1+p4 under key v2; gloss/), as filed in #443:')
cA = label_tsv(P('units', 'petkum_1665-11-30_p2-3_R1.units.tsv'))[0]; cB = label_tsv(P('units', 'petkum_1665-11-30_p1-p4_R1_heldout.units.tsv'))[0]
L.append(line('  p2-3 (image 573)', cA)); L.append(line('  p1+p4 (572R+574L, held out)', cB))
pl, tR1 = pool('R1', [('p2-3', cA), ('p1+p4', cB)]); L += ['  ' + x for x in pl]
L.append('A2. Blind second transcription R2 adjudicated, KEY_v3 unchanged (23 relabels of R1, units/petkum_1665-11-30_R2.units.tsv), as commented on #443:')
per = relabel_R2()
for k, (c, nchg) in per.items(): L.append(line('  ' + k, c, '; relabels applied %d' % nchg))
pl, tR2 = pool('R2', [(k, v[0]) for k, v in per.items()]); L += ['  ' + x for x in pl]
L.append('')

# B. seg letters
SEGS = [('B', 'Petkum, four letters (issue #444)', ['1665-03-24', '1665-11-23', '1665-12-10', '1666-04-13'], ''),
        ('C', 'Petkum, five letters, first reader (comment on #444)', ['1665-04-28', '1665-06-23', '1665-09-17', '1666-01-18', '1666-04-06'], ''),
        ('D', 'Petkum, the same five, blind second reader (comment on #444)', ['1665-04-28', '1665-06-23', '1665-09-17', '1666-01-18', '1666-04-06'], '_blind')]
segrows = []; pools = {}
for tag, title, ids, suf in SEGS:
    L.append('%s. %s' % (tag, title)); parts = []; fparts = []
    for d in ids:
        c, rows, nt = label_seg(P('units', 'petkum_%s%s.seg' % (d, suf)), P('transcriptions', 'petkum_%s%s.txt' % (d, suf)))
        parts.append((d, c)); L.append(line('  %s%s (%d tokens)' % (d, suf, nt), c))
        segrows += [('petkum_%s%s' % (d, suf),) + r for r in rows]
        if suf:
            fc, _, _ = label_seg(P('units', 'petkum_%s%s.seg' % (d, suf)), P('transcriptions', 'petkum_%s%s.txt' % (d, suf)), face_value=True)
            fparts.append((d, fc))
    pl, t = pool(tag, parts); L += ['  ' + x for x in pl]; pools[tag] = t
    if fparts:
        L.append('  D-face. Same blind units with the unsure mark ~ ignored (face value; information only, not a count of record):')
        for d, fc in fparts: L.append(line('    %s_blind face value' % d, fc))
        pl, t = pool('D-face', fparts); L += ['    ' + x for x in pl]
    L.append('')
with open(P('units', 'units_from_seg.tsv'), 'w', encoding='utf8') as w:
    w.write('# written by scripts/count.py from units/*.seg and key.tsv\n# letter\ttokens\tunit\tlabel\tnote\n')
    for r in segrows: w.write('\t'.join(r) + '\n')

# E. Paulmyer
L.append('E. Jean de Paulmyer to Hannibal Sehested, Paris 1664 (comment on #444; same key, unchanged)')
pp = []
for d in ['1664-04-25', '1664-05-02', '1664-05-16', '1664-06-19']:
    c, rows, col = label_tsv(P('units', 'paulmyer_%s.units.tsv' % d)); pp.append((d, c)); L.append(line('  ' + d, c))
pl, _ = pool('E3 (the three sister letters)', pp[1:]); L += ['  ' + x for x in pl]
pl, _ = pool('E4 (all four Paulmyer letters)', [pp[1], pp[2], pp[3], pp[0]]); L += ['  ' + x for x in pl]
L.append('  (E3 and E4 are below 65% and are offered as support for the key only, as in the comment on #444. The post-hoc pair 25 Apr + 2 May is not a pre-set pool and is not given.)')
L.append('')
pl, _ = pool('H (headline: the eleven letters filed as read in part, each at its count of record: 30 Nov R2, the four of #444, the five by the first reader, Paulmyer 25 Apr)',
              [('30 Nov R2', tR2), ('four', pools['B']), ('five, first reader', pools['C']), ('Paulmyer 25 Apr', pp[0][1])])
L += pl
pl, _ = pool("H' (the same with the five by the blind reader, ~ as N)", [('30 Nov R2', tR2), ('four', pools['B']), ('five, blind', pools['D']), ('Paulmyer 25 Apr', pp[0][1])])
L += pl
L.append('')
L.append('F. Not counted here: the twelve further bare Petkum letters decoded on 12 Nov 2026 (pooled 121/190 = 63.68% in our log), not filed and not in this folder.')
open(P('counts.txt'), 'w', encoding='utf8').write('\n'.join(L) + '\n')
print('\n'.join(L))
