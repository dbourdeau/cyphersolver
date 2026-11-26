"""Test the open numbers of barlow1812 against the order of the surviving State Department code sheet (WE028).

    python we028_structure.py            # prints the control and the nine open numbers, writes we028_structure.tsv

Plan and rule: we028_structure_plan.md (written before the first run). Reads key.tsv and proposals.tsv of this folder
and ../morris1813/beling/key/codebook_M97_13_transcription.csv (NARA M97 roll 13 frames 1056-1057, Andrew Beling's
transcription); writes only we028_structure.tsv. Standard library only. By an AI agent for the maintainers, 24 Nov 2026.
"""
import csv, pathlib, re, collections

HERE = pathlib.Path(__file__).resolve().parent
SHEET = HERE.parent / 'morris1813' / 'beling' / 'key' / 'codebook_M97_13_transcription.csv'
OPEN = [815, 1567, 1404, 624, 706, 103, 163, 531, 537]
REACH = 8


def norm(s):
    return re.sub(r'[^a-z0-9.,;]', '', s.lower())


sheet = {}
with open(SHEET, encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f):
        sheet[int(r['code_number'])] = r['reading'].strip()
by_value = collections.defaultdict(list)
for m, v in sheet.items():
    by_value[norm(v)].append(m)

key = {}
with open(HERE / 'key.tsv', encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        if r['value']:
            key[int(r['number'])] = (r['value'], r['grade'])
proposals = {}
with open(HERE / 'proposals.tsv', encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        proposals[int(r['number'])] = r['value']

anchors = {n: by_value[norm(v)][0] - n for n, (v, g) in key.items()
           if g in 'PCDW' and len(by_value.get(norm(v), [])) == 1}


def predict(n, anchors):
    below = max((a for a in anchors if n - REACH <= a < n), default=None)
    above = min((a for a in anchors if n < a <= n + REACH), default=None)
    cands = []
    for a in (below, above):
        cands.append(None if a is None else (a, anchors[a], sheet.get(n + anchors[a], '(off the sheet)')))
    if below is not None and above is not None and anchors[below] == anchors[above]:
        return 'interpolated', cands
    if below is None and above is None:
        return 'no anchor', cands
    if below is None or above is None:
        return 'one side', cands
    return 'offsets differ', cands


# control: leave each anchor out
tally = collections.Counter()
misses = []
for n in sorted(anchors):
    rest = {a: o for a, o in anchors.items() if a != n}
    kind, cands = predict(n, rest)
    if kind == 'interpolated':
        ok = norm(cands[0][2]) == norm(key[n][0])
        tally['interpolated', ok] += 1
        if not ok:
            misses.append((n, key[n][0], cands[0][2]))
    else:
        tally[kind, None] += 1
        if kind == 'offsets differ':
            ok = any(norm(c[2]) == norm(key[n][0]) for c in cands)
            tally['offsets differ: one of the two is right', ok] += 1
        if kind == 'one side':
            c = [c for c in cands if c][0]
            tally['one side: right', norm(c[2]) == norm(key[n][0])] += 1

lines = ['# barlow1812: open numbers against the order of the State Department sheet (WE028). Output of we028_structure.py; rule in we028_structure_plan.md',
         '# values in key.tsv: %d; found on the sheet: %d; anchors (grade P/C/D/W, one sheet entry): %d'
         % (len(key), sum(1 for v, g in key.values() if norm(v) in by_value), len(anchors))]
hit, miss = tally['interpolated', True], tally['interpolated', False]
lines.append('# control, each anchor left out: interpolated %d, right %d (%.3f); offsets differ %d (one of the two candidates right in %d); one side %d (right in %d); no anchor %d'
             % (hit + miss, hit, hit / max(1, hit + miss), tally['offsets differ', None],
                tally['offsets differ: one of the two is right', True], tally['one side', None],
                tally['one side: right', True], tally['no anchor', None]))
for n, v, p in misses:
    lines.append('# control miss: %d key "%s", sheet order gives "%s"' % (n, v, p))
lines.append('number\tkind\tanchor_below\tanchor_above\tsheet_entry_from_below\tsheet_entry_from_above\tproposal_from_sense\tverdict')
for n in OPEN:
    kind, cands = predict(n, anchors)
    desc = ['%d=%s (sheet %d)' % (c[0], key[c[0]][0], c[0] + c[1]) if c else '' for c in cands]
    vals = ['%s (sheet %d)' % (c[2], n + c[1]) if c else '' for c in cands]
    prop = proposals.get(n, '')
    got = {norm(c[2]) for c in cands if c}
    if kind == 'interpolated':
        verdict = 'agrees' if prop and norm(prop) in got else ('differs' if prop else 'no proposal; value from position')
    else:
        verdict = 'no prediction' + ('; one candidate agrees' if prop and norm(prop) in got else '')
    lines.append('\t'.join([str(n), kind, desc[0], desc[1], vals[0], vals[1], prop, verdict]))

# Added after the first run (not in the plan, so descriptive only): the numbers key.tsv lists as seen "in the word"
# (no value was ever given to them, so they were not used above). For each, the sheet entries the nearest anchors give;
# a hit when one of them (two letters or more) is contained in the word, with i/j and u/v folded.
fold = lambda s: norm(s).replace('j', 'i').replace('v', 'u')
inword = collections.defaultdict(set)
with open(HERE / 'key_evidence.tsv', encoding='utf-8', newline='') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        if r['grade'].startswith('in the word:'):
            inword[int(r['number'])].add(r['grade'].split(':', 1)[1].strip())
lines.append('# after the plan (descriptive): numbers seen only inside a word, against the sheet entries their nearest anchors give')
lines.append('number\tword\tkind\tsheet_entry_from_below\tsheet_entry_from_above\tin_the_word')
n_in = n_hit = n_interp = n_interp_hit = 0
for n in sorted(inword):
    if n in key:
        continue                                           # has a value from another occurrence: already in the control
    kind, cands = predict(n, anchors)
    ents = [c[2] if c else '' for c in cands]
    words = sorted(inword[n])
    hit = any(len(fold(e)) >= 2 and fold(e) in fold(w) for e in ents if e for w in words)
    n_in += 1
    n_hit += hit
    if kind == 'interpolated':
        n_interp += 1
        n_interp_hit += hit
    lines.append('\t'.join([str(n), '; '.join(words), kind, ents[0], ents[1], 'yes' if hit else 'no']))
lines.append('# in-word numbers: %d; a candidate entry stands in the word for %d; interpolated %d, of which in the word %d'
             % (n_in, n_hit, n_interp, n_interp_hit))
(HERE / 'we028_structure.tsv').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
print('\n'.join(lines))
