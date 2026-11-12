"""Build the round-2 copy texts (PREREG_round2 step 4): the first readings with the second reader's settled readings
applied. Run from beling/:  python3 -I scripts/make_copy_round2.py
Writes transcription/copy_round2_406.txt and copy_round2_410.txt, and prints each replacement made or missed.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TR = HERE / 'transcription'
PARTS = {  # letter: (first-reading file, collation letter, first folio/line kept, start text on that line, end text)
    '406': ('brienne_173r_173v.txt', '8 Feb', ('173v', 2), "laq.lle", 'priant Dieu.'),
    '410': ('brienne_194v_196r.txt', '28 Apr', ('194v', 1), None, 'bien disposees'),
}


def read_pages(path):
    pages, cur = {}, None
    for row in path.read_text(encoding='utf-8').splitlines():
        if row.startswith('## fol. '):
            cur = row[len('## fol. '):].strip()
            pages[cur] = []
        elif cur and row.strip() and not row.startswith('#'):
            pages[cur].append(row)
    return pages


def main():
    coll = [r.split('\t') for r in (TR / 'second_reading' / 'collation.tsv').read_text(encoding='utf-8').splitlines()[1:]]
    for L, (fname, letter, (f0, l0), start, end) in PARTS.items():
        pages = read_pages(TR / fname)
        log = []
        for r in coll:
            if len(r) < 7 or r[0] != letter:
                continue
            folio, line, first, settled, how = r[1].replace('fol. ', ''), r[2], r[3], r[5], r[6]
            if folio not in pages or not line.isdigit() or 'open' in how.lower() and '[V]' not in how:
                continue
            i = int(line) - 1
            if i < len(pages[folio]) and first in pages[folio][i]:
                pages[folio][i] = pages[folio][i].replace(first, settled, 1)
                log.append(f'applied  {folio} {line}: {first!r} -> {settled!r}')
            else:
                log.append(f'MISSED   {folio} {line}: {first!r} -> {settled!r}')
        out, keep = [], False
        for folio, rows in pages.items():
            for n, row in enumerate(rows, 1):
                if (folio, n) == (f0, l0):
                    keep = True
                    if start:
                        row = row[row.index(start) + len(start):]
                if keep:
                    if end in row:
                        out.append(row[:row.index(end) + len(end)])
                        keep = None
                        break
                    out.append(row)
            if keep is None:
                break
        hdr = [f'# Copy text T for scripts/test_key_v2.py (PREREG_round2 step 4), letter {L}: {fname} from fol. {f0} '
               f'l. {l0}{" after " + repr(start) if start else ""} to {end!r},',
               '# with the settled readings of second_reading/collation.tsv applied (made by scripts/make_copy_round2.py).']
        (TR / f'copy_round2_{L}.txt').write_text('\n'.join(hdr + out) + '\n', encoding='utf-8')
        print(f'== {L}: {len(out)} lines'); print('\n'.join(log))


if __name__ == '__main__':
    main()
