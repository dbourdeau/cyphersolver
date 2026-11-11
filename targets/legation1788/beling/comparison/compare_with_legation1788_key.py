"""Compare key/code16_key_v4.tsv with the Code No. 16 rows of ../key.tsv (Bourdeau, built by make_key.py).

Run from targets/legation1788/beling:   python3 comparison/compare_with_legation1788_key.py
Writes comparison/v4_vs_legation1788_key.tsv and comparison/v4_vs_legation1788_key.json.

Classes, per Code No. 16 group of ../key.tsv:
  agree                 same letters (brackets, '?', '.', '+' ignored)
  ours is a piece       our value is a proper part of his word: the group is a syllable of a word he credited to it
                        (his_marked = y when he already marked the missing letters with [..] himself)
  his is a piece        his value is a proper part of ours (abbreviations: nov., 10th, thot.)
  abbreviation          his abbreviation of our word (g.b., thot., mc)
  not a word            his value is a dash or a stop (Taylor's stroke over the group), so nothing to compare
  differ                neither contains the other
  his_marked = y        he marked the word as spanning several groups: letters in [..] or a group span in (..)
  his_alt = y           his other_readings column already lists our value (e.g. 541 an x1, 1453 sa- x1)
  his only              not in key v4
  ours from his key     key v4 grade B: the value was taken from his key, so it is not an independent check
Our grades D and S1/S2 were built without his Pinckney 1793-94 values; A values came from aligning bare
Pinckney frames of his transcription to the printed editions, with his values in the starting key.
"""
import csv, json, re, collections
from pathlib import Path

B = Path(__file__).resolve().parents[1]
norm = lambda s: ''.join(c for c in s.lower() if c.isalpha())
v4 = {int(r['group']): r for r in csv.DictReader(open(B / 'key' / 'code16_key_v4.tsv'), delimiter='\t')}
vocab = {norm(l.split('\t')[0]) for l in open(B / 'key' / 'weber_1600_family_vocab.txt') if not l.startswith('#')}
ABBR = {('gb', 'greatbritain'), ('thot', 'thought'), ('mc', 'mac')}
rows, tally, by_grade = [], collections.Counter(), collections.Counter()
for r in csv.DictReader(open(B.parent / 'key.tsv'), delimiter='\t'):
    if r['code'] != '16':
        continue
    g = r['group']; d = re.sub(r'\D', '', g)
    hv = norm(re.sub(r'\(.*?\)', '', r['value']))
    marked = 'y' if ('[' in r['value'] or re.search(r'\(\d+-\d+', r['value'])) else ''
    alts = {norm(re.sub(r'\s*x\d+$', '', a)) for a in r['other_readings'].split(';') if a.strip()}
    o = v4.get(int(d)) if d and g.isdigit() else None
    if o is None: c = 'his only'
    elif o['grade'] == 'B': c = 'ours from his key'
    elif not hv: c = 'not a word'
    elif (hv, o['value']) in ABBR: c = 'abbreviation'
    elif o['value'] == hv: c = 'agree'
    elif hv and o['value'] in hv: c = 'ours is a piece'
    elif hv and hv in o['value']: c = 'his is a piece'
    else: c = 'differ'
    tally[c] += 1
    if o is not None: by_grade[f"{o['grade']} {c}"] += 1
    rows.append(dict(group=g, his_value=r['value'], his_n=r['n'], his_source=r['source'], his_marked=marked, his_alt='y' if o and o['value'] in alts else '',
                     ours=o['value'] if o else '', grade=o['grade'] if o else '', our_n=o['n'] if o else '',
                     our_sources=o['sources'] if o else '', his_on_list='y' if hv in vocab else 'n', cls=c))
with open(B / 'comparison' / 'v4_vs_legation1788_key.tsv', 'w') as f:
    f.write('# key/code16_key_v4.tsv against the Code No. 16 rows of targets/legation1788/key.tsv; see the script for the classes\n')
    cols = list(rows[0])
    f.write('\t'.join(cols) + '\n')
    for r in rows: f.write('\t'.join(str(r[k]) for k in cols) + '\n')
pieces = [r for r in rows if r['cls'] == 'ours is a piece']
summary = dict(his_code16_rows=len(rows), v4_groups=len(v4), v4_groups_not_in_his_key=len({g for g in v4} - {int(re.sub(r'\D', '', r['group'])) for r in rows}),
               tally=dict(tally), by_our_grade=dict(sorted(by_grade.items())),
               ours_is_a_piece=dict(total=len(pieces), he_marked_missing_letters=sum(1 for r in pieces if r['his_marked']),
                                    unmarked_whole_words=[(r['group'], r['his_value'], r['ours'], r['grade'], 'his alt lists ours' if r['his_alt'] else '') for r in pieces if not r['his_marked']]),
               differ=[(r['group'], r['his_value'], r['ours'], r['grade'], 'his alt lists ours' if r['his_alt'] else '') for r in rows if r['cls'] == 'differ'],
               his_off_list_not_in_v4=[(r['group'], r['his_value']) for r in rows if r['cls'] == 'his only' and r['his_on_list'] == 'n'])
json.dump(summary, open(B / 'comparison' / 'v4_vs_legation1788_key.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in summary.items() if k not in ('his_off_list_not_in_v4',)}, indent=1, ensure_ascii=False))
