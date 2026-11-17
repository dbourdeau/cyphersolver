"""Write the two follow-up keys from key/clerks_values.tsv and key/key_manuscript.tsv.
Usage: python3 -I make_followup_keys.py <keydir>
  key_clerks_only.tsv      seed (key_manuscript.tsv, 164 codes) + basis a (forced by the tiling of the clerks' text)
  key_clerks_enlarged.tsv  the above + basis b (clerk's piece cut with Pusch's table as dictionary)
Value = the clerk's reading (for b, the most frequent clerk's piece). Columns: code, value, source."""
import os, sys
kd = sys.argv[1]
seed = {}
for l in open(os.path.join(kd, 'key_manuscript.tsv'), encoding='utf-8'):
    if l[0].isdigit():
        f = l.rstrip('\n').split('\t'); seed[int(f[0])] = f[1]
a, b = {}, {}
for l in open(os.path.join(kd, 'clerks_values.tsv'), encoding='utf-8'):
    if not l[0].isdigit():
        continue
    f = l.rstrip('\n').split('\t'); c = int(f[0])
    if f[2] == 'a':
        a[c] = f[1]
    elif f[2] == 'b':
        b[c] = f[1]
head = '# Kerlerec nomenclator from the Marine clerks\' interlinear decipherments only. source: seed = key_manuscript.tsv\n' \
       '# (nos. 194, 228 f. 48r); a = forced by the tiling of the clerks\' text in further glossed despatches\n' \
       '# (scripts/clerks_segment.py); b = clerk\'s piece cut with Pusch 2008 Table 2 as dictionary.\n'
for name, parts in (('key_clerks_only.tsv', (('seed', seed), ('a', a))),
                    ('key_clerks_enlarged.tsv', (('seed', seed), ('a', a), ('b', b)))):
    k = {}
    for src, d in parts:
        for c, v in d.items():
            k.setdefault(c, (v, src))
    with open(os.path.join(kd, name), 'w', encoding='utf-8') as f:
        f.write(head)
        for c in sorted(k):
            f.write('%d\t%s\t%s\n' % (c, k[c][0], k[c][1]))
    print(name, len(k), 'codes')
