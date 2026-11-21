"""Align the blind first-pass labels of the T-S NS J479 CTTS project with the target's transcription, band by band.

Inputs (project dir): boxes.json, labels_s1.json, labels_s2.json (blind first pass), orders.json (reading order of each
band: 'rev' = the transcription lists signs right to left as photographed, i.e. the band is read right to left; 'fwd' =
the band, turned, reads left to right), and the transcription rows of targets/tsnsj479/tr_side1.md, tr_side2.md.
Box order in boxes.json is left to right. Output: labels_final.json / boxes_final.json (the project to write with
to_ctts.py), align_report.json, alignment.tsv (every band, box by box, how each was settled).

Method per band: clean boxes (drop _junk/_clear, merge consecutive !part boxes with the same base label), compare the
base shapes of the box labels with the transcription tokens (difflib), then:
  equal      -> label from the transcription (identical to the blind label ignoring dots and marks)
  replace n:n-> label from the transcription, marked as disagreeing with the blind pass when the shapes differ
  replace n:m, one box flagged !split, m>n -> that box is cut into equal-width boxes labelled from the transcription
  other      -> boxes keep the blind label with a leading ? and tokens without a box are listed as missing
Nothing is settled from the transcription silently: every disagreement is listed for a person to check in CTTS.
"""
import difflib, json, re, sys
from pathlib import Path

P = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / 'projects' / 'tsnsj479'
TR = Path(__file__).resolve().parents[2] / 'targets' / 'tsnsj479'


def base(s):
    s = s.replace('!split', '').replace('!part', '').strip()
    return re.sub(r'[.?^\s]', '', s)


def load_tr():
    T = {}
    for side in (1, 2):
        for l in open(TR / f'tr_side{side}.md', encoding='utf-8'):
            m = re.match(r'(S\d[LVU]\d\d):\s*(.*)', l)
            if m:
                T[m.group(1)] = [t for t in m.group(2).split() if t != '|' and not t.startswith('[')]
    return T


def main():
    boxes = json.load(open(P / 'boxes.json', encoding='utf-8'))
    orders = json.load(open(P / 'orders.json'))
    lab = {}
    for f in ('labels_s1.json', 'labels_s2.json'):
        d = json.load(open(P / f, encoding='utf-8'))
        lab.update(d['labels'])
    T = load_tr()
    out_b, out_l, report, rows = {}, {}, {}, []
    STAT = {}
    tot = dict(boxes=0, equal=0, disagree=0, split=0, unmatched_box=0, missing_tok=0, dropped=0)
    for img, bx in boxes.items():
        r = img[:-4]; L = lab.get(img, {})
        items = []                       # [x,y,w,h,label,flag]
        i = 0
        while i < len(bx):
            b = bx[i]; l = (L.get(str(b['n']), '?') or '?').strip()
            if l.startswith('_'):
                tot['dropped'] += 1; i += 1; continue
            if '!part' in l:
                bs = base(l); grp = [b]
                while i + 1 < len(bx) and '!part' in (L.get(str(bx[i + 1]['n']), '') or '') and base(L.get(str(bx[i + 1]['n']), '')) == bs:
                    i += 1; grp.append(bx[i])
                x0 = min(g['x'] for g in grp); y0 = min(g['y'] for g in grp)
                x1 = max(g['x'] + g['w'] for g in grp); y1 = max(g['y'] + g['h'] for g in grp)
                items.append([x0, y0, x1 - x0, y1 - y0, bs, 'part']); i += 1; continue
            items.append([b['x'], b['y'], b['w'], b['h'], l.replace('!split', '').strip(), 'split' if '!split' in l else '']); i += 1
        toks = T.get(r, [])
        toks = toks[::-1] if orders.get(r) == 'rev' and False else toks
        # transcription is written right to left for photographed-orientation rows; the bands are cut in that
        # orientation, so box order (left to right) is the reverse of the transcription for 'rev' bands
        if orders.get(r) == 'rev':
            toks = toks[::-1]
        a = [base(x[4]) for x in items]; t = [base(x) for x in toks]
        sm = difflib.SequenceMatcher(None, a, t, autojunk=False)
        final = []; log = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                for k in range(i2 - i1):
                    it = items[i1 + k]; final.append((it[:4], toks[j1 + k], 'agree')); tot['equal'] += 1; log.append((r, 'equal', it[4], toks[j1 + k]))
            elif op == 'replace' and (i2 - i1) == (j2 - j1):
                for k in range(i2 - i1):
                    it = items[i1 + k]; final.append((it[:4], toks[j1 + k], 'disagree')); tot['disagree'] += 1
                    log.append((r, 'DISAGREE blind=%s transcription=%s' % (it[4], toks[j1 + k]), it[4], toks[j1 + k]))
            elif op == 'replace' and any(items[i][5] == 'split' for i in range(i1, i2)) and (j2 - j1) > (i2 - i1):
                extra = (j2 - j1) - (i2 - i1); jj = j1
                for k in range(i1, i2):
                    it = items[k]
                    n = 1 + (extra if it[5] == 'split' and extra > 0 else 0)
                    if it[5] == 'split': extra = 0
                    for q in range(n):
                        final.append(([it[0] + it[2] * q / n, it[1], it[2] / n, it[3]], toks[jj], 'split')); jj += 1
                    tot['split'] += 1 if n > 1 else 0
                    log.append((r, 'split %d' % n, it[4], ' '.join(toks[jj - n:jj])))
            else:
                for k in range(i1, i2):
                    it = items[k]; final.append((it[:4], '?' + it[4], 'unmatched')); tot['unmatched_box'] += 1; log.append((r, 'UNMATCHED box', it[4], ''))
                for k in range(j1, j2):
                    tot['missing_tok'] += 1; log.append((r, 'MISSING token (no box)', '', toks[k]))
        final.sort(key=lambda f: f[0][0]); STAT[img] = final
        tot['boxes'] += len(final)
        out_b[img] = [dict(line=1, x=round(f[0][0]), y=round(f[0][1]), w=max(round(f[0][2]), 4), h=round(f[0][3]), n=n + 1) for n, f in enumerate(final)]
        out_l[img] = {str(n + 1): f[1] for n, f in enumerate(final)}
        report[r] = dict(boxes=len(items), tokens=len(toks), final=len(final))
        rows += log
    json.dump({img: [f[2] for f in fl] for img, fl in STAT.items()}, open(P / 'status_final.json', 'w', encoding='utf-8'))
    json.dump(out_b, open(P / 'boxes_final.json', 'w', encoding='utf-8'), indent=1)
    json.dump(out_l, open(P / 'labels_final.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    json.dump(dict(totals=tot, bands=report), open(P / 'align_report.json', 'w', encoding='utf-8'), indent=1)
    with open(P / 'alignment.tsv', 'w', encoding='utf-8') as fh:
        fh.write('band\thow\tblind\ttranscription\n')
        for r in rows: fh.write('\t'.join(map(str, r)) + '\n')
    print(tot)


if __name__ == '__main__':
    main()
