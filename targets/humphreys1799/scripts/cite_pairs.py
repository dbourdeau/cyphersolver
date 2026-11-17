"""Write key/pairs.tsv: every crib pair with its roll, frame, line and source label (packaging step, 14 Nov 2026).
Input: the working file pairs_labeled.tsv made by label_pairs.py from transcriptions/crib/*.txt (copied in here as
key/pairs_labeled_source.tsv). Usage: python scripts/cite_pairs.py"""
import csv, os, collections
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
LABEL = {'gloss_over_group': 'clerk_word_over_one_group',
         'gloss_running': 'clerk_words_over_several_groups_split_by_us',
         'printed': 'printed_edition'}
def edition(frame):
    if frame.startswith('M43-02-004'): return 'Papers of Thomas Jefferson 18:472-75 (No. 10)'
    if frame.startswith('M43-02-005'): return 'Papers of Thomas Jefferson 18:497-98 (No. 11)'
    if frame == 'M31-006-0284': return 'Papers of James Madison, Secretary of State Series 1:50-53 (Wagner decoding of the duplicate, 0285)'
    return ''
rows = list(csv.DictReader(open(B + '/key/pairs_labeled_source.tsv'), delimiter='\t'))
with open(B + '/key/pairs.tsv', 'w') as o:
    o.write('roll\tframe\tline\tpos\tgroup\tvalue\tsource\tedition_aligned_to\tin_table_build\tuncertain\n')
    for r in rows:
        pub, roll, fr = r['frame'].split('-')
        ed = edition(r['frame']) if r['source_class'] == 'printed' else ''
        o.write('\t'.join([f'{pub} roll {int(roll)}', fr, r['line'], r['pos'], r['group'], r['value'],
                           LABEL[r['source_class']], ed, r['in_freeze_snapshot'], r['uncertain']]) + '\n')
c = collections.Counter((LABEL[r['source_class']], r['in_freeze_snapshot']) for r in rows)
for k, v in sorted(c.items()): print(v, *k)
print(len(rows), 'pairs;', sum(v for k, v in c.items() if k[1] == 'y'), 'in the table build')
