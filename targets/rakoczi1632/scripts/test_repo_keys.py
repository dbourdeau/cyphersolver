"""Test Dan's repo Rakoczi key (DECODE R639 Bonac-Groffey table, targets/rakoczi1704 and rakoczi1707) on the glossed
pairs of fol. 491r: how many of our key's gloss-confirmed numeric groups get the same letter from R639?
usage: test_repo_keys.py R639_table.txt  (the table file, saved from git show origin/main:targets/rakoczi1707/DOC_R639_D2752_2752.txt)"""
import sys, re, pathlib
R = pathlib.Path(__file__).resolve().parent.parent
t = {}
for l in open(sys.argv[1], encoding='utf8'):
    m = re.match(r'^([\d|/?]+) - (\S+)', l.strip())
    if m:
        for n in re.findall(r'\d+', m.group(1)): t.setdefault(n, []).append(m.group(2).lower())
ours = {}
for l in (R / 'key.tsv').read_text(encoding='utf8').splitlines():
    f = l.split('\t')
    if len(f) > 3 and f[0].isdigit() and f[2] in ('gloss', 'two'): ours[f[0]] = (f[1].split('/'), int(f[3]))
agree = sum(n for g, (v, n) in ours.items() if any(x in v for x in t.get(g, [])))
tot = sum(n for v, n in ours.values())
print(f'R639 table: {agree} of {tot} glossed occurrences agree ({100*agree/tot:.0f}%); by chance about 1/20')
print('Keresdi Bethlen 1645 key (targets/transylvania1645): a letter-for-letter alphabet, no numbers; not applicable')
