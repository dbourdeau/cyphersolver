"""Build reading.tsv for the two letters (Short, Carmichael) and print the measure.
Grades: T = TJ's interlinear over the group (Short); E = the PTJ editors' reading, not attested elsewhere; C = editors' or
context conjecture; O = open. Until 11 Nov 2026 this also took in Pinckney's 28 Aug 1793 passage (grade H = attested in
another letter of the same code); that letter is now in targets/pinckney1793/ (reading_pinckney_17930828.tsv)."""
import csv, collections
OPEN_SHORT = {'401', '1083', '359', '199', '34', '724'}
out = []
for r in csv.DictReader(open('transcription/short_17920726_full.tsv', encoding='utf-8'), delimiter='\t'):
    if (r.get('note') or '').strip() == 'struck':  # Short's own struck group
        continue
    g = r['group'].strip()
    il = (r.get('interlinear') or '').strip()
    grade = 'O' if g in OPEN_SHORT else ('T' if il else 'E')
    out.append(('short_17920726', r['frame'], r['line'], r['pos'], g, il, grade))
carm = [('009_0224', '108', 'Maryland', 'C'), ('009_0230', '108', 'Maryland', 'C'), ('009_0230', '223', 'Massachusetts', 'C'),
        ('009_0230', '273', 'majority', 'C'), ('009_0230', '597', '—', 'O')]
for i, (f, g, w, gr) in enumerate(carm, 1):
    out.append(('carmichael_17880414', f, '', str(i), g, w, gr))
with open('reading.tsv', 'w', encoding='utf-8', newline='') as fh:
    fh.write('letter\tframe\tline\tpos\tgroup\treading\tgrade\n')
    for o in out:
        fh.write('\t'.join(o) + '\n')
by = collections.defaultdict(collections.Counter)
for o in out:
    by[o[0]][o[6]] += 1
tot = collections.Counter()
for k, c in by.items():
    n = sum(c.values()); tot += c
    print(k, n, dict(c), 'read incl. C %.1f%%' % (100 * (n - c['O']) / n), 'excl. C %.1f%%' % (100 * (n - c['O'] - c['C']) / n))
n = sum(tot.values())
print('ALL', n, dict(tot), 'read incl. C %.2f%%' % (100 * (n - tot['O']) / n), 'excl. C %.2f%%' % (100 * (n - tot['O'] - tot['C']) / n))
