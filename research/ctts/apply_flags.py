"""Apply a first pass's own box flags before the CTTS project is written: split, part, missed.

On a page of single-digit signs (marburg1635: ~580 signs) the candidate boxes need far more surgery than on a
nomenclator page, and doing it all by computer use in CTTS is slow and brittle (Bordeaux report, section 4). The first
pass already says what each flagged box holds, so this does that surgery mechanically:
  - `a b !split`  -> the box is cut into equal-width boxes, one per sign, each with its own label;
  - `x !part` on consecutive boxes with the same label -> one box covering them all;
  - `missed` entries -> a box of the line's median size placed after the box it follows (labelled `?<label>` so it is
    checked in CTTS).
Boxes made this way are listed in `auto_boxes.json` so they can be checked first in CTTS. Output: boxes_applied.json and
labels_applied.json, in the formats to_ctts.py reads (`python to_ctts.py PROJECT labels_applied.json --boxes
boxes_applied.json`).

  python apply_flags.py PROJECT_DIR LABELS_JSON
"""
import json
import statistics
import sys
from pathlib import Path


def main():
    proj = Path(sys.argv[1]); labels = json.load(open(sys.argv[2], encoding='utf-8'))
    boxes = json.load(open(proj / 'boxes.json', encoding='utf-8'))
    missed = labels.get('missed', {})
    out_b, out_l, auto = {}, {}, {}
    for img, bx in boxes.items():
        lab = labels.get(img, {})
        rows = []                                   # (x, y, w, h, label, how)
        i = 0
        while i < len(bx):
            b = bx[i]; l = (lab.get(str(b['n']), '?') or '?').strip()
            if '!part' in l:
                base = l.replace('!part', '').strip()
                grp = [b]
                # the first pass may give the full label on one box and `!part` on its twin: merge with a neighbour
                # that carries the same reading, flagged or not
                if rows and rows[-1][4] == base and not rows[-1][5].startswith('split'):
                    r = rows.pop()
                    grp.insert(0, {'x': r[0], 'y': r[1], 'w': r[2], 'h': r[3], 'n': r[5] or 'prev'})
                while i + 1 < len(bx) and (lab.get(str(bx[i + 1]['n']), '') or '').replace('!part', '').strip() == base:
                    i += 1; grp.append(bx[i])
                x0 = min(g['x'] for g in grp); y0 = min(g['y'] for g in grp)
                x1 = max(g['x'] + g['w'] for g in grp); y1 = max(g['y'] + g['h'] for g in grp)
                rows.append((x0, y0, x1 - x0, y1 - y0, base or '?', 'merged %s' % [g['n'] for g in grp] if len(grp) > 1 else 'part alone %d' % b['n']))
            elif '!split' in l:
                signs = l.replace('!split', '').split()
                k = max(len(signs), 1)
                for j, s in enumerate(signs or ['?']):
                    rows.append((b['x'] + b['w'] * j / k, b['y'], b['w'] / k, b['h'], s, 'split %d' % b['n']))
            else:
                rows.append((b['x'], b['y'], b['w'], b['h'], l, ''))
            # missed signs after this box
            for m in missed.get(img, []):
                if int(m.get('after', -1)) == b['n']:
                    ws = [r[2] for r in rows if not r[4].startswith('_')] or [30]
                    hs = [r[3] for r in rows if not r[4].startswith('_')] or [40]
                    w, h = statistics.median(ws), statistics.median(hs)
                    for s in str(m['label']).split():
                        last = rows[-1]
                        rows.append((last[0] + last[2] + 2, last[1], w, h, '?' + s.lstrip('?'), 'missed after %d' % b['n']))
            i += 1
        for m in missed.get(img, []):
            if int(m.get('after', -1)) == 0:
                rows.insert(0, (5, 40, 30, 50, '?' + str(m['label']).lstrip('?'), 'missed at start'))
        nb, nl, au = [], {}, []
        for n, r in enumerate(rows, 1):
            nb.append({'line': 1, 'x': round(r[0]), 'y': round(r[1]), 'w': max(round(r[2]), 4), 'h': round(r[3]), 'n': n})
            nl[str(n)] = r[4]
            if r[5]:
                au.append({'n': n, 'label': r[4], 'how': r[5]})
        out_b[img], out_l[img], auto[img] = nb, nl, au
    json.dump(out_b, open(proj / 'boxes_applied.json', 'w', encoding='utf-8'), indent=1)
    json.dump(out_l, open(proj / 'labels_applied.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    json.dump(auto, open(proj / 'auto_boxes.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(sum(len(v) for v in out_b.values()), 'boxes;', sum(len(v) for v in auto.values()), 'made or changed by flags')


if __name__ == '__main__':
    main()
