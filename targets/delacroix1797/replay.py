"""Adapter for docs/_replay.py: the contributor's partial table applied to Brackx's 653 groups, against the reading.

key            beling2026/key/code_table_F_partial.tsv
transcription  ciphertext.txt (Michael Brackx, digits unchanged)
reading        beling2026/readings/reading_1797-07-13.md

How a group's value is taken (24 Nov 2026):
- a number of class C (unsure) has no value here: it is given as one hole mark (#) per letter the hand alignment
  has at that place, so that the word on it comes out as marked, as in the reading (one # alone lets the aligner
  slide a bracketed letter onto an equal letter beside it, and three words then show as unmarked that are not);
  the unknown signs 411 and 802 and the null 469 carry no letters and are passed over;
- at the eight places where a digit change is proposed, the number keeps the table's main value on Brackx's digit
  (257 al, 327 que, 1024 ap), not the value the draft wants there;
- where the table lists more than one value for a number (column all_values: 39 re and rez, 350 au and aux, 1015
  consul and consuls), the listed value that the hand alignment (beling2026/key/alignment_by_group.txt) has at that
  place is taken; a value the table does not list is never taken. This uses the alignment to choose between the
  table's own values and nothing else.
The code runs on without word division, so words are counted over the reading. The words of the draft that have no
group in the copy (<<not in the groups: ...>>) are left out.
"""
import csv, os, re, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, 'beling2026')
DIVIDED = False
POLYPHONY = {}
SOURCES = {'key': 'beling2026/key/code_table_F_partial.tsv', 'transcription': 'ciphertext.txt',
           'reading': 'beling2026/readings/reading_1797-07-13.md'}
LABEL = 'No. 5'


def norm(s):
    d = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', ''.join(c for c in d if unicodedata.category(c) != 'Mn'))


def mechanical():
    main, allv, cls = {}, {}, {}
    for r in csv.DictReader(open(os.path.join(B, 'key', 'code_table_F_partial.tsv'), encoding='utf-8'), delimiter='\t'):
        g = int(r['group'])
        cls[g] = r['class']
        if r['value'].startswith('('):                       # (full stop), (null), (unknown)
            main[g] = '' if 'full stop' in r['value'] else None
            allv[g] = set()
            continue
        main[g] = norm(r['value'])
        allv[g] = {main[g]}
        for a in (r.get('all_values') or '').split(';'):
            a = re.sub(r'\s*x\d+\s*$', '', a.strip())
            if a:
                allv[g].add(norm(a))
    prop = {int(r['token_index']) for r in csv.DictReader(
        (l for l in open(os.path.join(B, 'proposals', 'transcription_corrections.tsv'), encoding='utf-8')
         if not l.startswith('#')), delimiter='\t')}
    align = []                                               # the draft's letters at each group, by the hand alignment
    for line in open(os.path.join(B, 'key', 'alignment_by_group.txt'), encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        for t in line.split():
            if not t.startswith('~'):
                g, v = t.split('=', 1)
                align.append((int(g), '' if v in ('0', '.', '?') else v.split('!')[0]))
    groups = [int(x) for l in open(os.path.join(HERE, 'ciphertext.txt'), encoding='utf-8')
              if l.strip() and not l.startswith('#') and not l.startswith('frame') for x in l.split()]
    assert [g for g, _ in align] == groups, 'the alignment does not follow ciphertext.txt group for group'
    word = []
    for i, (g, lets) in enumerate(align):
        if g not in main or main[g] is None:
            v = None
        elif cls[g] == 'C':
            v = '#' * len(lets) if lets else None
        elif i in prop:
            v = main[g]
        else:
            v = lets if lets in allv[g] else main[g]
        word.append((str(g), v))
    return [(LABEL, [word])]


def reading():
    txt = open(os.path.join(B, 'readings', 'reading_1797-07-13.md'), encoding='utf-8').read()
    txt = txt[txt.index('Les Consuls de New-yorck'):]
    txt = txt.split('<!--', 1)[0]
    txt = re.sub(r'<<[^>]*>>', ' ', txt)
    return {LABEL: txt}
