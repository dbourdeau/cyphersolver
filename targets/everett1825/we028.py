"""everett1825: the six coded parts of the Notes, collated from the three transcriptions in this folder and decoded
with the State Department code sheet (NARA M97 roll 13 frames 1056-1057, Weber's WE028), 24 Nov 2026.

    python targets/everett1825/we028.py collate   # writes everett1825_collated_transcription.txt, prints every place
                                                  # where the witnesses differ in a number or a mark
    python targets/everett1825/we028.py key       # writes key_we028_everett1825.tsv (one row per different group)
    python targets/everett1825/we028.py decode    # writes everett1825_collated_decryption.txt (key output, unedited)
    python targets/everett1825/we028.py count     # counts words and holes in everett1825_collated_reading.md

Witnesses: beling/transcription_six_sections.txt (all six parts; its loci and line division are kept),
dudout/texts/*_transcription.txt (parts 1-4 and 6) and everett1825_transcription.txt (parts 5 and 6).
Where they differ the group is chosen in DECISIONS below, each with its reason; nothing is chosen silently.
The sheet is ../morris1813/beling/key/codebook_M97_13_transcription.csv, used unchanged; four of its rows are
corrected here from the sheet itself or its numerical half (SHEET_FIXES). Python standard library only.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHEET = os.path.join(HERE, '..', 'morris1813', 'beling', 'key', 'codebook_M97_13_transcription.csv')
OUT_T = os.path.join(HERE, 'everett1825_collated_transcription.txt')
OUT_K = os.path.join(HERE, 'key_we028_everett1825.tsv')
OUT_D = os.path.join(HERE, 'everett1825_collated_decryption.txt')
READING = os.path.join(HERE, 'everett1825_collated_reading.md')

PARTS = {'S1': 'P1', 'S2': 'P2', 'S3': 'P3', 'S4': 'P4', 'S5': 'P5', 'S6': 'P6'}

# Places where the witnesses give different numbers: Beling's locus -> (group taken, reason). The film check is
# beling/film_check (two blind AI readers, 22 Nov 2026); "clerk" is the State Department decipherment of the time
# (beling/period_decipherment.txt); "sheet" the code sheet; "seen 24 Nov" the look at the NARA frame recorded in NOTES.
DECISIONS = {
    '112R.04.6': ('628', 'Beling 628, Dudout 623: film check 628; sheet 628 me, 623 mat; clerk "to me"; seen 24 Nov'),
    '112R.05.10': ('458', 'Beling 458, Dudout 433: film check 458; sheet 458 ve, 433 never; clerk "believe"; seen 24 Nov'),
    '112R.06.8': ('845', 'Beling 845, Dudout 843: film check 345 or 845, last digit 5; sheet 845 dis; clerk "dissimulation"; seen 24 Nov'),
    '113L.03.9': ('1081', 'Beling 1081, Dudout 1031: film check 1081 (both readers); sheet 1081 self, 1031 city; clerk "himself"; seen 24 Nov'),
    '113L.04.11': ('184', 'Dudout 184, Beling 124: film check 184; clerk "his patron"'),
    '113R.01.10': ('182', 'Dudout 182, Beling 152: film check 182; clerk "him"'),
    '113R.03.9': ('1203', 'Dudout 1203, Beling 1205: film check 1203; seen 24 Nov. Sheet 1203 gal; the sense wants 1233 great'),
    '113R.05.6': ('1564', 'Beling 1564, Dudout 1364: film check 1564 (one reader); sheet 1564 observe, 1364 tain; clerk "as I observe"; seen 24 Nov'),
    '113R.10.9': ('1380', 'Dudout 1380, Beling 1390: film check 1380; clerk "indicates"'),
    '113R.12.4': ('683', 'Dudout 683, Beling 623: film check 683; clerk "Spaniards"'),
    '114L.01.8': ('634', 'Dudout 634, Beling 684: film check 634; seen 24 Nov. Sheet 634 mem; the sense wants 684 are'),
    '114L.03.3': ('234', 'Dudout 234, Beling 254: film check 234; clerk "singular"'),
    '114L.05.4': ('1385', 'Dudout 1385, Beling 1325: film check 1385; clerk "the expression"'),
    '114R.03.6': ('1385', 'Dudout 1385, Beling 1345: film check split (1385 or 1345), the digit is blotted; sheet 1385 the, 1345 boa; clerk "the correct"'),
    '114R.03.7': ('1046', 'Dudout 1046, Beling 1246: film check 1046; clerk "correct"'),
    '114R.03.8': ('518', 'Dudout 518, Beling 318: film check 518 (both readers); clerk "correct"'),
    '114R.09.4': ('1293', 'Dudout 1293, Beling 1203: film check 1293; clerk "indifferently"'),
    '114R.10.11': ('1197', 'Dudout 1197, Beling 1497: film check 1197; sheet 1197 work'),
    '114R.12.9': ('284', 'Dudout 284, Beling 254: film check 284; clerk "every"'),
    '114R.15.4': ('1086', 'Dudout 1086, Beling 1056: film check 1086 (both readers); clerk "servants"'),
    '114R.17.1': ('1057?', 'Dudout 1057, Beling 1257: film check 1257 with the second digit unsure (neither reader offered 0). Not '
                            'settled on the frame: the second digit is a closed oval with an exit stroke. 1057 is written here with its '
                            'mark because the group carries three ticks and the sheet withdraws one letter a tick: 1057 crisis less '
                            'three letters = cri (des-cri-bing), 1257 hath less three = h; clerk "describing". If it is 1257 it is a '
                            'one-digit slip inside a word, so the word is read either way under the one-digit rule'),
    '115L.01.6': ('1479', 'Dudout 1479, Beling 1179: film check 1479; clerk "rival"'),
    '115L.02.8': ('1098', 'Dudout 1098, Beling 1092: film check 1098; clerk "sink"'),
    '115L.07.7': ('880', 'Beling 880, Dudout 330: film check 380 or 880, second digit 8; sheet 880 li, 330 fi; clerk "inclined"; seen 24 Nov'),
    '121L.07.6': ('1354', 'Dudout and WAINUT 1354, Beling 1384: film check 1354 (both readers); sheet 1354 br'),
    '121L.10.4': ('1383?', 'Dudout 1383, WAINUT 1383?, Beling 1388: film check 1388 (both readers), written over; sheet 1383 than, '
                            '1388 then; clerk "than". Not settled: kept with its mark'),
    '121L.11.8': ('692', 'Dudout and WAINUT 692, Beling 693: film check 692; clerk "as"'),
}
# Three runs where Beling's line has other groups: the film check has Dudout's groups at all three.
RUNS = {'114L.13': 'film check: 1254 1535 37 598 1576 1385', '114L.20': 'film check: 1385 1028 470 1436 864',
        '114R.20': 'film check: 169 627 1310 318'}
# Marks: where the witnesses differ, the mark taken (seen on the frames, 24 Nov 2026).
MARKS = {
    '121L.01.4': ('v', 'tick under 108 (Dudout, WAINUT); Beling a cross: the frame has a tick'),
    '120R.06.5': ('v^', 'a long stroke under the last figure of 850 and a caret after it (Dudout x^, WAINUT ^, Beling caret and "strike?")'),
    '114R.01.4': ('+<>', 'a short upright stroke under 1083 and a lozenge (Dudout +D, Beling b-stroke and d); the cross-bar is not visible'),
    '115L.04.9': ('', 'Dudout has a tick at 569; the frame has a small mark at the upper right of the group, nothing under it'),
}
# Four rows where the sheet transcription (the CSV) is wrong or blank, with what the value rests on.
SHEET_FIXES = {
    233: ('sim', 'the sheet transcription has "sem"; the alphabetical sheet (frame 1056) prints sim 233, between sight 1100 and '
                 'sin 234 (seen 24 Nov 2026); 1082 is sem'),
    234: ('sin', 'the sheet transcription has "sen"; the alphabetical sheet (frame 1056) prints sin 234, before since 235 '
                 '(seen 24 Nov 2026); 1083 is sen; ../jqa/code_table.tsv 234 sin (C, 5x)'),
    1093: ('shal', 'the sheet transcription has "shall" (numerical half); the alphabetical sheet (frame 1056) prints shal 1093 '
                   '(seen 24 Nov 2026), and Everett writes the group with the doubling cross for shall'),
    681: ('are','the sheet transcription leaves it blank because its two halves differ (numerical "are", alphabetical "arc"; '
                 'the entry is too faint on frame 1056 to settle here); the numerical reading is taken; '
                 '../jqa/code_table.tsv 681 are (H, 2x)'),
}


def number(tok):
    m = re.match(r'-?(\d+)', tok)
    return m.group(1) if m else None


def marks(tok, who):
    """Marks of a token in one notation: + cross under, v tick under (one a letter), <> lozenge, ^ caret."""
    rest = re.sub(r'^-?\d+', '', tok)
    out = ''
    if who == 'beling':
        tags = re.findall(r'\{([^}]*)\}', rest)
        for t in tags:
            if t in ('b+', 'below-plus'): out += '+'
            elif t in ('bv', 'below-v'): out += 'v'
            elif t == 'bv2': out += 'vv'
            elif t == 'bv3': out += 'vvv'
        for t in tags:
            if t in ('d', 'diamond'): out += '<>'
            elif t in ('a^', 'above-caret'): out += '^'
        other = [t for t in tags if t not in ('b+', 'below-plus', 'bv', 'below-v', 'bv2', 'bv3', 'd', 'diamond', 'a^', 'above-caret')]
        return out, other
    if who == 'dudout':
        out += '+' * rest.count('+') + 'v' * (rest.count('v') + rest.count('x'))
        if 'D' in rest or '◊' in rest: out += '<>'
        if '^' in rest: out += '^'
        return out, []
    out += '+' * rest.count('_+')
    m = re.search(r'_(v+)', rest)
    if m: out += m.group(1)
    if '<>' in rest: out += '<>'
    if '^' in rest: out += '^'
    return out, (['?'] if '?' in rest else [])


def read_beling():
    lines = []
    for l in open(os.path.join(HERE, 'beling', 'transcription_six_sections.txt'), encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        sec, loc, groups = l.rstrip('\n').split('\t')
        lines.append((sec, loc, groups.split()))
    return lines


def read_dudout(page):
    out = []
    for l in open(os.path.join(HERE, 'dudout', 'texts', page + '_transcription.txt'), encoding='utf-8'):
        if l.startswith('#'):
            continue
        out += [t for t in l.split() if number(t)]
    return out


def read_wainut(passages):
    out = []
    for l in open(os.path.join(HERE, 'everett1825_transcription.txt'), encoding='utf-8'):
        if l[:1] in passages and l[1:2] == ' ':
            out += [t for t in l.split()[1:] if number(t)]
    return out


def collate(report=True):
    """-> [(part, locus, [(number, marks, doubt)])], and the list of differences."""
    bel = read_beling()
    p01, p03 = read_dudout('p01_0112'), read_dudout('p03_0113')
    p18 = read_dudout('p18_0121')
    line3 = ['1440', '1082+D', '569', '1310', '1541', '480', '262', '1599', '1384', '1385']   # not in his p. 18 files
    dud = {'S1': p01[:6], 'S2': p01[6:], 'S3': read_dudout('p02_0113') + p03[:38],
           'S4': p03[38:] + read_dudout('p04_0114') + read_dudout('p05_0114') + read_dudout('p06_0115'),
           'S6': read_dudout('p17_0120') + p18[:22] + line3 + p18[22:]}
    wai = {'S5': read_wainut('A'), 'S6': read_wainut('BC')}
    pos = {s: 0 for s in PARTS}
    out, diffs = [], []
    for sec, loc, toks in bel:
        row = []
        for k, tok in enumerate(toks, 1):
            i = pos[sec]; pos[sec] += 1
            locus = '%s.%d' % (loc, k)
            b = number(tok)
            d = dud[sec][i] if sec in dud else None
            w = wai[sec][i] if sec in wai else None
            nums = {x for x in (b, number(d) if d else None, number(w) if w else None) if x}
            if len(nums) == 1:
                n = b
            elif locus in DECISIONS:
                n = DECISIONS[locus][0]
                diffs.append((locus, 'number', tok, d or '', w or '', n, DECISIONS[locus][1]))
            elif loc in RUNS:
                n = number(d)
                diffs.append((locus, 'run', tok, d or '', w or '', n, RUNS[loc]))
            else:
                raise SystemExit('undecided difference at %s: %s / %s / %s' % (locus, tok, d, w))
            mb, other = marks(tok, 'beling')
            md = marks(d, 'dudout')[0] if d else None
            mw, wq = marks(w, 'wainut') if w else (None, [])
            ms = {x for x in (mb, md, mw) if x is not None}
            if locus in MARKS:
                m = MARKS[locus][0]
                diffs.append((locus, 'mark', tok, d or '', w or '', n + m, MARKS[locus][1]))
            elif len(ms) == 1:
                m = mb
            elif loc in RUNS:
                m = md
            else:
                raise SystemExit('undecided mark at %s: %s / %s / %s' % (locus, tok, d, w))
            if other or wq:
                diffs.append((locus, 'note', tok, d or '', w or '', n + m, 'other signs: ' + ', '.join(other + wq)))
            row.append((n.rstrip('?'), m, n.endswith('?')))
        out.append((PARTS[sec], loc, row))
    for s in dud:
        assert pos[s] == len(dud[s]), (s, pos[s], len(dud[s]))
    for s in wai:
        assert pos[s] == len(wai[s]), (s, pos[s], len(wai[s]))
    if report:
        for d in diffs:
            print('\t'.join(d))
    return out, diffs


def tok(n, m, q):
    return n + m + ('?' if q else '')


def write_transcription():
    rows, diffs = collate(report=True)
    total = sum(len(r[2]) for r in rows)
    head = [
        '# Everett, Notes of a conversation with Mr Zea (Madrid, 25 Sep 1825): the six coded parts, collated.',
        '# NARA RG 59, M31 roll 27, frames 0112-0115 (MS pp. 1-6) and 0119-0121 (MS pp. 14-15, 17-18).',
        '# Written by we028.py (24 Nov 2026) from three transcriptions made independently of one another:',
        '# beling/transcription_six_sections.txt, dudout/texts/*_transcription.txt, everett1825_transcription.txt.',
        '# Where they differ, the group taken and the reason are in DECISIONS, RUNS and MARKS in we028.py, and in NOTES.md.',
        '# One line per line of the manuscript: a label, then the groups. The label is the part (P1-P6, the six parts of',
        '# the State Department decipherment) and the locus (frame, L or R page, line; Andrew Beling\'s numbering).',
        '# Marks, as the code sheet\'s printed instructions name them: + a cross under the group (doubles a letter),',
        '# v a tick under it (withdraws a letter; vv two, vvv three), <> a lozenge after it (plural or genitive of a noun,',
        '# third person of a verb), ^ a caret (participle or past tense). ? after a group = the digits are not settled.',
        '# %d groups.' % total,
    ]
    with open(OUT_T, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(head) + '\n')
        for part, loc, row in rows:
            f.write('%s:%s\t%s\n' % (part, loc, ' '.join(tok(*g) for g in row)))
    print('wrote', os.path.basename(OUT_T), total, 'groups;', len(diffs), 'places listed')


def sheet():
    d = {}
    for r in csv.DictReader(open(SHEET, encoding='utf-8', newline='')):
        d[int(r['code_number'])] = (r['reading'], r['status'])
    return d


def value(n, sh):
    if n in SHEET_FIXES:
        return SHEET_FIXES[n][0], 'sheet, transcription corrected: ' + SHEET_FIXES[n][1]
    if n not in sh:
        return '', 'no such number on the sheet (1-1600)'
    v, st = sh[n]
    return v, 'sheet (' + st + ')'


def read_collated():
    rows = []
    for l in open(OUT_T, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        label, groups = l.rstrip('\n').split('\t')
        part, loc = label.split(':')
        rows.append((part, loc, groups.split()))
    return rows


def write_key():
    sh = sheet()
    seen = {}
    for part, loc, groups in read_collated():
        for g in groups:
            n = int(number(g))
            seen[n] = seen.get(n, 0) + 1
    with open(OUT_K, 'w', encoding='utf-8', newline='\n') as f:
        f.write('# Key for everett1825_collated_transcription.txt: the value of the State Department code sheet (NARA M97 roll 13\n'
                '# frames 1056-1057, Weber WE028) for each different group of the six coded parts, copied by we028.py from\n'
                '# ../morris1813/beling/key/codebook_M97_13_transcription.csv (1,600 numbers). Nothing is added to the sheet.\n'
                '# Four rows where that transcription is wrong or blank (233, 234, 681, 1093) are corrected and say so.\n'
                '# A group written with a slip carries the sheet value as it stands, not the word the reading wants.\n'
                '# The marks under and after a group are not in this file: the sheet\'s printed instructions for them are in NOTES.md.\n'
                '# number\tvalue\ttimes\tsource\n')
        for n in sorted(seen):
            v, src = value(n, sh)
            f.write('%d\t%s\t%d\t%s\n' % (n, v, seen[n], src))
    print('wrote', os.path.basename(OUT_K), len(seen), 'different groups,', sum(seen.values()), 'groups')


def write_decryption():
    key = {}
    for l in open(OUT_K, encoding='utf-8'):
        if l.startswith('#'):
            continue
        p = l.rstrip('\n').split('\t')
        key[p[0]] = p[1]
    n_groups = n_blank = 0
    with open(OUT_D, 'w', encoding='utf-8', newline='\n') as f:
        f.write('# Everett, Notes of a conversation with Mr Zea (25 Sep 1825): the six coded parts, group by group.\n'
                '# Output of: python we028.py decode  (key_we028_everett1825.tsv applied to everett1825_collated_transcription.txt).\n'
                '# Nothing is edited: a group written with a slip gives the wrong word here. The marks stay on the group and\n'
                '# are not applied: + doubles a letter, v withdraws one (vv two, vvv three), <> plural, genitive or third\n'
                '# person, ^ participle or past tense. (?) = no value. group=value, line by line.\n')
        for part, loc, groups in read_collated():
            cells = []
            for g in groups:
                v = key.get(number(g), '')
                n_groups += 1
                if not v:
                    n_blank += 1
                cells.append('%s=%s' % (g, v or '(?)'))
            f.write('%s:%s\t%s\n' % (part, loc, '  '.join(cells)))
        f.write('# %d groups, %d without a value\n' % (n_groups, n_blank))
    print('wrote', os.path.basename(OUT_D), n_groups, 'groups,', n_blank, 'without a value')


def count():
    """Words and holes of the reading, part by part and page by page. A word with a square bracket in it is a hole
    (a word, a letter or an ending the key does not give for the groups as written); {+x} marks a one-digit slip read
    under the one-digit rule and counts as read; (text in round brackets) and lines not starting with '> ' are not counted."""
    part = page = None
    tally = {}
    order = []
    for l in open(READING, encoding='utf-8'):
        m = re.match(r'##\s+(Part \d)', l)
        if m:
            part = m.group(1)
            continue
        m = re.match(r'###\s+(MS p\. [\d-]+)', l)
        if m:
            page = m.group(1)
            continue
        if not l.startswith('> '):
            continue
        text = re.sub(r'\([^)]*\)', ' ', l[2:])
        for w in text.split():
            if not re.search(r'[A-Za-z]', w):
                continue
            hole = '[' in w or ']' in w
            for key in (('part', part), ('page', page), ('all', 'all six parts')):
                if key not in tally:
                    tally[key] = [0, 0, []]; order.append(key)
                tally[key][0] += 1
                if hole:
                    tally[key][1] += 1
                    tally[key][2].append(w.strip('.,;:'))
    for kind in ('part', 'page', 'all'):
        for key in order:
            if key[0] != kind:
                continue
            n, h, ws = tally[key]
            print('%s\t%d words\t%d holes\t%.3f\t%s' % (key[1], n, h, (n - h) / n, ' '.join(ws)))


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'collate':
        write_transcription()
    elif cmd == 'key':
        write_key()
    elif cmd == 'decode':
        write_decryption()
    elif cmd == 'count':
        count()
    else:
        print(__doc__)
