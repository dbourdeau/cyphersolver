"""Reader for the fuller ICIT-derived corpus (the corpus built into indusscript.net; ICIT data, Wells / Fuls; used
locally, not redistributed).

Record fields used: 0 id, 1 CISI number, 3 site, 11 depth ('-3.0 ft', '-125 cm', 'surface', '- -'), 17 condition,
20 object type, 34 text. Text conventions: signs as 3-digit Wells/ICIT numbers joined by '-', '/' between lines,
'000' a missing or illegible sign, ']' at the (visual) left and '[' at the (visual) right mark a broken edge, '+' an
intact edge. Texts are stored in visual order; reading order is the reverse (as build_corpus.py): the visual left
edge is the reading end, the visual right edge the reading start.
"""
import csv
import re

from signs import SPLIT


def records(path):
    for rec in csv.reader(open(path, encoding='utf-8')):
        if len(rec) >= 35 and rec[34] and rec[34][0] in '+[]':
            yield rec


def lines_of(text):
    """Lines in reading order: list of dicts {signs, gap (a 000 inside), broken_start, broken_end}."""
    out = []
    parts = text.split('/')
    for k, part in enumerate(parts):
        left_broken = part.startswith(']') or part.startswith('[')
        right_broken = part.endswith('[') or part.endswith(']')
        toks = [t for t in re.split(r'[-+\[\]]', part) if t]
        rd = list(reversed(toks))
        signs, gap = [], False
        for t in rd:
            if not t.isdigit():
                continue
            if t == '000':
                gap = True
                signs.append(None)
                continue
            g = str(int(t))
            signs.extend(SPLIT.get(g, [g]))
        out.append({'signs': signs, 'broken_start': right_broken, 'broken_end': left_broken,
                    'gap': gap})
    return out


def depth_ft(s):
    s = s.strip()
    if s.startswith('surface'):
        return 0.0
    m = re.match(r'^-?\s*(\d+(?:\.\d+)?)\s*(ft|m|cm)\b', s.replace('- ', '-'))
    if not m:
        return None
    v = float(m.group(1))
    return {'ft': v, 'm': v * 3.281, 'cm': v / 30.48}[m.group(2)]


def objects(path, intact_only=False):
    """Rows in the shape of signs.load(): seq (lines, gaps split out), flat, site, type, depth; plus 'raw' lines."""
    rows = []
    for rec in records(path):
        ls = lines_of(rec[34])
        seq = []
        for ln in ls:
            if intact_only and (ln['broken_start'] or ln['broken_end'] or ln['gap']):
                continue
            cur = []
            for g in ln['signs']:
                if g is None:
                    if cur:
                        seq.append(cur)
                    cur = []
                else:
                    cur.append(g)
            if cur:
                seq.append(cur)
        rows.append({'sealid': rec[0], 'cisi': rec[1], 'site': rec[3], 'type': rec[20], 'depth': depth_ft(rec[11]),
                     'condition': rec[17], 'seq': seq, 'flat': [g for ln in seq for g in ln], 'motif': '',
                     'raw': ls, 'text': rec[34]})
    return rows
