"""Label every crib pair by its source (written 14 Nov 2026, session 2, after the independent check).
Reads the transcription files directly (all pairs, including those added after the freeze) and writes
../pairs_labeled.tsv with columns: frame, line, pos, group, value, source_class, in_freeze_snapshot, uncertain.
source_class:
  gloss_over_group   - 1791 letters (M43-02), where the clerk glossed group by group, and the gloss sits over this group
  gloss_running      - 1800-01 running decipherments (M31-006-0127, 0130, 0253, 0254, 0271): the clerk's words run over
                       several groups or a line; the split into elements is ours (this includes the pairs marked '!'
                       there, e.g. 296 'bas' and 1538 'minister' on 0127, which pass 1 overstated)
  printed            - value aligned by us to a printed decoded text: Papers of Thomas Jefferson 18:472-75, 497-98
                       (M43-02 pairs without a legible gloss) or Papers of James Madison SS 1:50-53 (M31-006-0284,
                       Wagner's decipherment of the duplicate on 0285)
The '!' marks in the 1791 files are taken at face value as gloss_over_group; the independent check found 26 of 40
sampled pairs directly glossed, 10 running-gloss splits (two of them on 0127 marked '!'), 4 printed-only."""
import re, glob, os, csv
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
snap = set()
for r in csv.DictReader(open(B + '/work/pairs_at_freeze_v1.tsv'), delimiter='\t'):
    snap.add((r['frame'], r['line'], r['pos'], r['group']))
RUN = {'M31-006-0127', 'M31-006-0130', 'M31-006-0253', 'M31-006-0254', 'M31-006-0271'}
out = []
for f in sorted(glob.glob(B + '/transcriptions/M*.txt')):
    fr = os.path.basename(f)[:-4]
    for line in open(f):
        m = re.match(r'([LR]\d+\w*):\s*(.*)', line.strip())
        if not m: continue
        body = re.sub(r'\[(?:cut|struck|1791|Struck)[^\]]*\]', '', m.group(2))
        for k, tok in enumerate(body.split()):
            if '=' not in tok: continue
            g, v = tok.split('=', 1)
            mark = '!' if '!' in v else ''
            unc = 'g' if '?' in g else ('u' if v.endswith('?') else '')
            v = v.replace('!', '').replace('~', '').rstrip('?'); g = g.replace('?', '')
            if fr in RUN: cls = 'gloss_running'
            elif fr == 'M31-006-0284': cls = 'printed'
            else: cls = 'gloss_over_group' if mark else 'printed'
            out.append((fr, m.group(1), k, g, v, cls, 'y' if (fr, m.group(1), str(k), g) in snap else 'n', unc))
with open(B + '/pairs_labeled.tsv', 'w') as o:
    o.write('frame\tline\tpos\tgroup\tvalue\tsource_class\tin_freeze_snapshot\tuncertain\n')
    for r in out: o.write('\t'.join(map(str, r)) + '\n')
import collections
print(len(out), collections.Counter(r[5] for r in out))
