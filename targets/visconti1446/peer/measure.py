"""Count cipher tokens, nulls, tokens that give sense and unread tokens per slip, from the transcription TSVs.

How "gives sense" is read from each file (the reading agents tagged them differently):
- f. 110 (r and v): the note says `copy X (agree ...)`, `(variant ...)` or `(differ ...)` against the 1597 copy, or
  `(unread ...)`; sense = agree + one-letter variant.
- f. 130: the note carries `sense`, `read-no-sense`, `unread` or `null`; sense = `sense`.
- ff. 136, 154, 158: the note carries `unread` for every unread token; sense = tokens - nulls - unread.
- ff. 5, 8 (ital. 1584, calibration against the contemporary translations ff. 6, 9): sense = tokens - nulls - `?`.
usage: python measure.py            (prints the table; percentages are of non-null tokens)
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))


def rows(f):
    return list(csv.DictReader(open(os.path.join(HERE, 'texts', f'f{f}_transcription.tsv'), encoding='utf8'),
                               delimiter='\t'))


def count(name, rs, how):
    tot = len(rs)
    null = sum(1 for r in rs if r['label'].split('#')[0] == 'NULL')
    if how == 'copy':
        sense = sum(1 for r in rs if re.search(r'\((agree|variant)', r['note'] or ''))
    elif how == 'tags':
        sense = sum(1 for r in rs if re.split(r'[;|]', r['note'] or '')[-1].strip() == 'sense'
                    or (r['note'] or '').strip() == 'sense')
    elif how == 'unread':
        sense = tot - null - sum(1 for r in rs if re.search(r'\bunread\b', r['note'] or ''))
    else:
        sense = tot - null - sum(1 for r in rs if r['label'].startswith('?'))
    nn = tot - null
    return name, tot, null, sense, nn - sense, sense / nn if nn else 0


def main():
    out = []
    r110 = rows('110')
    out.append(count('f. 110r', [r for r in r110 if not r['folio'].endswith('v')], 'copy'))
    out.append(count('f. 110v', [r for r in r110 if r['folio'].endswith('v')], 'copy'))
    out.append(count('f. 130', rows('130'), 'tags'))
    for f in ('136', '154', '158'):
        out.append(count(f'f. {f}', rows(f), 'unread'))
    tot = [sum(x[i] for x in out) for i in (1, 2, 3, 4)]
    out.append(('1446 slips', *tot, tot[2] / (tot[0] - tot[1])))
    for f in ('005', '008'):
        out.append(count(f'f. {int(f)} (1584)', rows(f), 'q'))
    print(f'{"slip":<16}{"tokens":>8}{"nulls":>7}{"sense":>8}{"unread":>8}{"sense %":>9}')
    for n, t, nu, s, u, p in out:
        print(f'{n:<16}{t:>8}{nu:>7}{s:>8}{u:>8}{p:>9.1%}')


if __name__ == '__main__':
    main()
