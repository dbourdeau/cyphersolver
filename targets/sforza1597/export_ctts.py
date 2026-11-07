"""Write a CTTS project for R5464 (two leaves): images, positions, symbol types, key. usage: python export_ctts.py <outdir> <keyfile>"""
import sys, os, json, pickle, re, shutil, collections, numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from signreader import track_line_j, straighten, segment_strip2
out = sys.argv[1]; keyf = sys.argv[2]
os.makedirs(out + '/positions', exist_ok=True)
colorset = [l.strip() for l in open('ctts/exp/colorset.txt') if l.strip()]
recs_all, lab_all = pickle.load(open('ctts/h64.txt.pkl', 'rb'))
cnt = collections.Counter(lab_all); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
used = {}
def boxes_for(tag, ncount):
    d = f'sr_{tag}'; ink = cv2.imread(d + '/ink.png', 0); lj = json.load(open(d + '/lines.json')); ys = lj['lines']
    pitch = float(np.median(np.diff(ys))); jump = int(max(12, 0.4 * pitch)); half = int(min(70, round(0.55 * pitch)))
    res = []; centers = []
    for li, y in enumerate(ys):
        fl = (centers[-1] + 0.6 * pitch) if centers else None
        c = track_line_j(ink, y, jump, floor=fl)
        if centers and np.mean(np.abs(c - centers[-1])) < 0.35 * pitch: continue
        centers.append(c)
        si = straighten(ink, c, half); comps, lab = segment_strip2(si)
        line = []
        for (x, yy, w, h, a, ids, extra) in comps:
            x0 = min([x] + [e[0] for e in extra]); y0 = min([yy] + [e[1] for e in extra])
            x1 = max([x + w] + [e[0] + e[2] for e in extra]); y1 = max([yy + h] + [e[1] + e[3] for e in extra])
            cx = int(min(max(x0 + (x1 - x0) / 2, 0), len(c) - 1)); off = c[cx] - half
            line.append((x0, y0 + off, x1 - x0, y1 - y0))
        res.append(line)
    return res
pos = 0; names = {}
for tag, imgname in (('R5464_P1_0', 'R5464_P1'), ('R5464_P2_0', 'R5464_P2')):
    n = sum(1 for r in recs_all if r['page'] == tag)
    lines = boxes_for(tag, n)
    flat = [b for l in lines for b in l]
    assert len(flat) == n, (tag, len(flat), n)
    txt = []
    k = 0
    for l in lines:
        for (x, y, w, h) in l:
            cl = rank[lab_all[pos + k]]; used[cl] = True; k += 1
            txt.append(f'{x:f} {y:f} {w:f} {h:f} {cl:3d}')
        txt.append('')
    pos += n
    open(f'{out}/positions/{imgname}_positions.txt', 'w', newline=chr(10)).write('\n'.join(txt) + '\n')
    shutil.copy(f'sr_{tag}/gray.png', f'{out}/{imgname}.png')
# symbol types: colour i <-> cluster i, name "#i"
with open(out + '/colors.txt', 'w', newline=chr(10)) as f:
    for i, c in enumerate(colorset):
        f.write(c + ';' + ('#%d' % i if i in used else '') + ';' + str(i) + chr(10))
# key: from solver output (cluster sNN -> letter)
mp = collections.defaultdict(list)
for line in open(keyf, encoding='utf-8'):
    m = re.match(r'^([s\d|]+) - ([A-Za-z])$', line.strip())
    if m:
        for c in m.group(1).split('|'): mp[m.group(2).upper()].append('#' + str(int(c[1:])))
with open(out + '/key.txt', 'w', newline=chr(10)) as f:
    f.write('#ORIGIN: Claude / CTTS solver (period Italian corpus), R5464 two leaves, 7 Nov 2026\n#STATUS: Partial; machine key, not verified\n#LANGUAGE: Italian\n')
    for L, v in sorted(mp.items()): f.write('|'.join(v) + ' - ' + L + '\n')
print('written', out, 'symbol types', len(used), 'positions', pos)
