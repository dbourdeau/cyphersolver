"""build_reading.py DOC : the reading text of one blind document, built mechanically from DOC/judge.tsv (python3 -I).

The judge's segmented text is used unchanged: for each unit row the judge's reading column, or the decode where
the judge left that column empty (the decode was taken as it stands). Only presentation is applied:
  - a row the judge marked all N with no reading, and the judge's 'symbol/blot, no value', become the hole [...];
    '[S]' and '[blot]' inside a word become [...]; rows 'struck through, not counted' are left out (writer's deletion);
  - a word split across rows is joined as the judge wrote it ('le|gato' + 'legato' -> legato; 'solcher hand-' +
    '-lung' -> solcher handlung; 'memorials|' + '-weise' -> memorialsweise);
  - the judge's annotations in parentheses ('(name)', '(name, unverified)') and '=modern' glosses ('newe=neue') are
    moved to the notes list below the text; the word itself is not changed.
Writes nothing; prints the text, one manuscript line per output line ('image line: text'), then the notes.
"""
import sys, os, re
def rows(doc):
    out = []
    for l in open(os.path.join(doc, 'judge.tsv'), encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if f[0] in ('image', '', 'TOTAL') or f[1] == 'TOTAL': continue
        f += [''] * (8 - len(f)); out.append(f)
    return out
def word(f, notes):
    img, ln, dec, marks, S, E, N, rd = f[:8]
    if rd == 'struck through, not counted' or dec == '<struck>': return None
    if rd == 'symbol/blot, no value': return '[...]'
    if not rd:
        rd = '[...]' if marks and set(marks) == {'N'} else dec
    m = re.search(r'\s*\(([^)]*)\)\s*$', rd)
    if m: notes.append('%s: %s' % (rd[:m.start()], m.group(1))); rd = rd[:m.start()]
    if '=' in rd: a, b = rd.split('=', 1); notes.append('%s = %s (judge)' % (a, b)); rd = a
    return rd.replace('[S]', '[...]').replace('[blot]', '[...]')
def build(doc):
    R = rows(doc); notes = []; lines = []; cur = None; i = 0
    def emit(img, ln, w):
        nonlocal cur
        if cur is None or cur[0] != (img, ln): cur = [(img, ln), []]; lines.append(cur)
        cur[1].append(w)
    while i < len(R):
        f = R[i]; w = word(f, notes); i += 1
        if w is None: continue
        nxt = word(R[i], []) if i < len(R) else None
        if '|' in w or w.endswith('-'):
            if nxt is not None and nxt.startswith('-'):
                w = w.rstrip('|').rstrip('-').replace('|', '') + nxt[1:] if (w.endswith('|') or w.endswith('-')) else w.replace('|', ''); i += 1
            elif '|' in w:
                full = w.replace('|', '')
                if nxt is not None and nxt.replace(' ', '') == full.split(' ')[-1]: i += 1
                w = full
        emit(f[0], f[1], w)
    return lines, notes
if __name__ == '__main__':
    lines, notes = build(sys.argv[1])
    for (img, ln), ws in lines: print('%s %s: %s' % (img.replace('.jpg', ''), ln, ' '.join(ws)))
    if notes: print('\nNotes from the judge: ' + '; '.join(notes) + '.')
