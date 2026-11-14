"""Decode Casgrain's four code I letters with the frozen sheet e001295272 table alone, and compare with his clear text.

Inputs (this folder):
  key/table_e001295272.tsv   the frozen table (sha256 in key/FREEZE.txt); readings used exactly as transcribed
  letters/I1.tr ... I4.tr    Casgrain III (1890): printed figure lines (F) and printed clear lines (C), checked on the page images

Outputs:
  letters/<L>_groups.txt     the printed cipher figures, one paragraph per line ({...} = words printed in clear among the figures)
  letters/<L>_casgrain_fr.txt  Casgrain's printed clear text, one paragraph per line
  letters/<L>_decode.txt     the table-only decode, one paragraph per line: reading? = doubtful cell, [N?] = group not on
                             the photograph (cells 1-20) or illegible, {...} = clear word printed among the figures
  validation.tsv             cipher group TAB table reading, for docs/_validate.py
  results/letters_test.json  similarity of decode and clear text, against 200 shuffled tables

Similarity: both strings lower-cased, accents removed, everything but a-z dropped; difflib.SequenceMatcher ratio
(autojunk off), whole letter. Clear words printed among the figures are kept on both sides. This measure was chosen
after the test plan (TEST_PLAN.md) was frozen; the shuffle control is the one the plan describes (readings of cells
21-700 permuted over the cell numbers, random.Random(1758 + k), k = 0..199).

Run from the repository root:  python targets/montcalm1758i/decode_letters.py
"""
import csv, difflib, json, pathlib, random, re, statistics, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
LETTERS = ['I1', 'I2', 'I3', 'I4']


def norm(s):
    s = s.replace('(sic)', '').replace('œ', 'oe').replace('Œ', 'oe')
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z]', '', s)


def load_table():
    t = {}
    with open(HERE / 'key' / 'table_e001295272.tsv', encoding='utf-8') as f:
        for row in csv.DictReader(f, delimiter='\t'):
            t[int(row['cell'])] = (row['reading'], row['status'])
    return t


def parse(path):
    """Paragraphs of (kind, token) and the printed clear text of each paragraph."""
    paras, cur = [], None
    for ln in open(path, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if ln.startswith('#para') or (cur is None and ln[:2] in ('F ', 'C ')):
            cur = {'groups': [], 'clear': []}
            paras.append(cur)
            if ln.startswith('#para'):
                continue
        if ln.startswith('#'):
            continue
        if ln.startswith('F '):
            for m in re.finditer(r'\{([^}]*)\}|(\d+)', ln[2:]):
                cur['groups'].append(('w', m.group(1)) if m.group(1) is not None else ('g', int(m.group(2))))
        elif ln.startswith('C '):
            cur['clear'].append(ln[2:])
    return [p for p in paras if p['groups'] or p['clear']]


def join_clear(lines):
    out = ''
    for x in lines:
        x = x.strip()
        if out.endswith('-'):
            out = out[:-1] + x
        else:
            out = (out + ' ' + x).strip()
    return out


def decode_tokens(groups, table, readings=None):
    out = []
    for kind, tok in groups:
        if kind == 'w':
            out.append(('w', tok))
            continue
        r, st = table.get(tok, ('?', 'illegible'))
        if readings is not None and 21 <= tok <= 700 and st != 'illegible':
            r = readings[tok]
        out.append(('g', tok, r, st))
    return out


def as_text(dec):
    parts = []
    for d in dec:
        if d[0] == 'w':
            parts.append('{' + d[1] + '}')
        elif d[3] == 'illegible' or not (21 <= d[1] <= 700):
            parts.append('[%d?]' % d[1])
        elif d[3] == 'doubtful':
            parts.append(d[2] + '?')
        else:
            parts.append(d[2])
    return ' '.join(parts)


def as_norm(dec):
    s = ''
    for d in dec:
        if d[0] == 'w':
            s += norm(d[1])
        elif d[3] != 'illegible' and 21 <= d[1] <= 700:
            s += norm(d[2])
    return s


def main():
    table = load_table()
    legible = [c for c in range(21, 701) if table[c][1] != 'illegible']
    letters = {L: parse(HERE / 'letters' / (L + '.tr')) for L in LETTERS}
    result = {}
    val = ['# model: fr-1750-nospace',
           '# source: decode_letters.py, frozen table key/table_e001295272.tsv applied to letters/I1-I4.tr',
           '# note: cipher group TAB reading of that cell on sheet e001295272 as transcribed (no post-freeze corrections);'
           ' ? = cell off the photograph or illegible; clear words printed among the figures are left out']
    for L, paras in letters.items():
        dec = [decode_tokens(p['groups'], table) for p in paras]
        (HERE / 'letters' / (L + '_groups.txt')).write_text(
            '\n'.join(' '.join(('{%s}' % t) if k == 'w' else str(t) for k, t in p['groups']) for p in paras) + '\n', encoding='utf-8')
        (HERE / 'letters' / (L + '_casgrain_fr.txt')).write_text('\n'.join(join_clear(p['clear']) for p in paras) + '\n', encoding='utf-8')
        (HERE / 'letters' / (L + '_decode.txt')).write_text('\n'.join(as_text(d) for d in dec) + '\n', encoding='utf-8')
        for d in dec:
            for x in d:
                if x[0] == 'g':
                    ok = x[3] != 'illegible' and 21 <= x[1] <= 700
                    val.append('%d\t%s' % (x[1], x[2].lower() if ok else '?'))
        ref = ''.join(norm(join_clear(p['clear'])) for p in paras)
        real = difflib.SequenceMatcher(None, as_norm([x for d in dec for x in d]), ref, autojunk=False).ratio()
        groups = [g for p in paras for g in p['groups']]
        n_g = sum(1 for k, _ in groups if k == 'g')
        off = sum(1 for k, t in groups if k == 'g' and (not 21 <= t <= 700 or table[t][1] == 'illegible'))
        dbt = sum(1 for k, t in groups if k == 'g' and 21 <= t <= 700 and table[t][1] == 'doubtful')
        shuf = []
        for k in range(200):
            rng = random.Random(1758 + k)
            vals = [table[c][0] for c in legible]
            rng.shuffle(vals)
            readings = dict(zip(legible, vals))
            sd = [x for p in paras for x in decode_tokens(p['groups'], table, readings)]
            shuf.append(difflib.SequenceMatcher(None, as_norm(sd), ref, autojunk=False).ratio())
        result[L] = {'groups': n_g, 'groups_not_on_sheet': off, 'groups_doubtful_cell': dbt,
                     'clear_letters': len(ref), 'similarity': round(real, 3),
                     'shuffled_mean': round(statistics.mean(shuf), 3), 'shuffled_max': round(max(shuf), 3),
                     'shuffles_at_or_above': sum(1 for s in shuf if s >= real)}
        print(L, result[L])
    (HERE / 'validation.tsv').write_text('\n'.join(val) + '\n', encoding='utf-8')
    (HERE / 'results' / 'letters_test.json').write_text(json.dumps(result, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
