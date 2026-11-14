"""Write key/key_entries.tsv: every number, the majority unit, all votes, and the page and context of each source pair."""
import collections, os, sys
D = sys.argv[1]
src = collections.defaultdict(list); votes = collections.defaultdict(collections.Counter)
def rows(fn):
    for l in open(os.path.join(D, fn), encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        yield l.rstrip('\n').split('\t')
for f in rows('key/key_source_pairs_pp600-603_609.tsv'):
    votes[int(f[0])][f[1]] += 1; src[int(f[0])].append(f'(a) p.{f[2]} "{f[3]}"')
for f in rows('transcriptions/p604-606_cipher_with_p599_draft.tsv'):
    if len(f) >= 3 and not f[0].endswith('s') and f[2] != '?':
        votes[int(f[1])][f[2]] += 1; src[int(f[1])].append(f'(a) p.604-605 line {f[0]} = p.599 draft')
for f in rows('key/heldout_p608_truth.tsv'):
    votes[int(f[0])][f[1]] += 1; src[int(f[0])].append(f'(a) p.608 "{f[2]}"')
for f in rows('key/key_additions_round2.tsv'):
    cls = '(b)' if f[2] == '579' else '(a)'
    votes[int(f[0])][f[1]] += 1; src[int(f[0])].append(f'{cls} p.{f[2]} "{f[3]}"')
for f in rows('key/key_pairs_classB_glosses.tsv'):
    votes[int(f[0])][f[1]] += 1; src[int(f[0])].append(f'(b) p.{f[2]} gloss "{f[3]}"')
with open(os.path.join(D, 'key/key_entries.tsv'), 'w', encoding='utf-8') as o:
    o.write('# number\tunit (majority)\tvotes\tsources ((a) de Neufville draft, (b) recipient gloss on a Baudouin letter; pages are Fold3/NARA image numbers of file unit 464816476)\n')
    for n in sorted(votes):
        c = votes[n]
        o.write(f"{n}\t{c.most_common(1)[0][0]}\t{'; '.join(f'{u}x{k}' for u, k in c.most_common())}\t{' | '.join(dict.fromkeys(src[n]))}\n")
print(len(votes), 'numbers')
