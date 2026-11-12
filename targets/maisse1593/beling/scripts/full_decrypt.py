"""Full construction, step 2 (exploratory, after the round-2 test): decrypt every transcribed cipher line of ff. 406
and 410-411 with the full key (key/key_full.tsv plus key/construction_overrides.tsv), align each letter to its whole
copy text, and list where cipher and copy differ. Also decrypts the short run on f. 406r l. 13.

Run from beling/:  python3 -I scripts/full_decrypt.py
Writes results/full_decryption.txt and results/full_variants.tsv. Standard library only.
"""
import difflib, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE / 'scripts'))
import build_key_v2 as b  # noqa: E402


def load(path, cols=(0, 1)):
    out = {}
    for row in (HERE / path).read_text(encoding='utf-8').splitlines():
        if row.strip() and not row.startswith('#'):
            p = row.split('\t')
            out[p[cols[1]]] = p[cols[0]]
    return out


WAINUT = HERE.parent / 'wainut'  # targets/maisse1593/wainut in the repo
if not WAINUT.exists():  # local working layout
    WAINUT = HERE.parent / 'upstream' / 'targets' / 'maisse1593' / 'wainut'
FULL = {  # letter: [(file, collation letter, folios used, start text, end text or None)]
    '406': [(WAINUT / 'f406_brienne_copy.txt', '8 Feb', ('172r', '172v'), 'Le surplus', None),
            (HERE / 'transcription' / 'brienne_173r_173v.txt', '8 Feb', ('173r', '173v'), None, 'priant Dieu.')],
    '410': [(WAINUT / 'f410_brienne_copy.txt', '28 Apr', ('193v', '194r'), "L'experience", None),
            (HERE / 'transcription' / 'brienne_194v_196r.txt', '28 Apr', ('194v', '195r', '195v', '196r'), None,
             'bien disposees')],
}


def full_copy(L):
    """The whole copy from the cipher's first words, first readings with every settled collation reading applied."""
    coll = [r.split('\t') for r in (HERE / 'transcription' / 'second_reading' / 'collation.tsv')
            .read_text(encoding='utf-8').splitlines()[1:]]
    text, notes = [], []
    for path, letter, folios, start, end in FULL[L]:
        pages, cur = {}, None
        for row in path.read_text(encoding='utf-8').splitlines():
            if row.startswith('## fol. '):
                cur = row[len('## fol. '):].split()[0]
                pages[cur] = []
            elif row.startswith('## '):
                cur = None
            elif cur and row.strip() and not row.startswith('#'):
                pages[cur].append(row)
        for r in coll:
            if len(r) < 7 or r[0] != letter:
                continue
            folio, line, first, settled = r[1].replace('fol. ', ''), r[2], r[3], r[5]
            if folio not in pages or folio not in folios:
                continue
            i = int(line) - 1 if line.isdigit() else -1
            if first != '(nothing)' and 0 <= i < len(pages[folio]) and first in pages[folio][i]:
                pages[folio][i] = pages[folio][i].replace(first, settled.replace('[...]', '').replace('[?]', ''), 1)
            else:
                notes.append(f'{folio} {line} {first!r} -> {settled!r}')
        for folio in folios:
            for row in pages[folio]:
                if start and start in row:
                    row, start = row[row.index(start):], None
                elif start:
                    continue
                if end and end in row:
                    text.append(row[:row.index(end) + len(end)])
                    return b.norm(' '.join(text)), notes
                text.append(row)
    return b.norm(' '.join(text)), notes


def merge_pairs(toks, pairs):
    out, i = [], 0
    while i < len(toks):
        if i + 1 < len(toks) and (toks[i][2], toks[i + 1][2]) in pairs:
            out.append((toks[i][0], toks[i][1], toks[i][2] + ' ' + toks[i + 1][2]))
            i += 2
        else:
            out.append(toks[i])
            i += 1
    return out


def main():
    key = {s: (None if v == '?' else '' if v == 'null' else v) for s, v in load('key/key_full.tsv').items()}
    over = {s: v for v, s in ((r.split('\t')[1], r.split('\t')[0]) for r in
            (HERE / 'key' / 'construction_overrides.tsv').read_text(encoding='utf-8').splitlines()
            if r.strip() and not r.startswith('#'))}
    key.update(over)
    pairs = {tuple(s_.split(' ')) for s_ in over if ' ' in s_}
    copy_notes = []
    out, var = [], ['letter\tafter line\tcipher gives\tcopy has\tkind']
    tot_m = tot_n = 0
    for L in ('406', '410'):
        toks = merge_pairs(b.tokens('r1', L) + b.tokens('r2', L), pairs)
        T, nts = full_copy(L)
        copy_notes += nts
        d, owner = [], []
        for i, (_, ln, s) in enumerate(toks):
            v = key.get(s) if s is not None else None
            for ch in ('?' if v is None else v):
                d.append(ch)
                owner.append(ln)
        D = ''.join(d)
        sm = difflib.SequenceMatcher(None, D.replace('?', '\x00'), T, autojunk=False)
        m = sum(x.size for x in sm.get_matching_blocks())
        tot_m += m
        tot_n += len(D)
        dmap = {}
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            for k in range(i1, i2):
                dmap[k] = j1 + (k - i1 if tag == 'equal' else round((k - i1) * (j2 - j1) / max(1, i2 - i1)))
            if tag != 'equal' and max(i2 - i1, j2 - j1) >= 4:
                ln = owner[i1] if i1 < len(owner) else owner[-1]
                kind = {'replace': 'differs', 'delete': 'cipher only', 'insert': 'copy only'}[tag]
                var.append(f'{L}\t{ln}\t{D[i1:i2] or "-"}\t{T[j1:j2] or "-"}\t{kind}')
        out.append(f'== letter {L}: {len(toks)} signs, {len(D)} letters decrypted, {m} matched the copy '
                   f'({m / len(D):.3f})')
        lines = []
        for k, ln in enumerate(owner):
            if not lines or lines[-1][0] != ln:
                lines.append([ln, k, k])
            lines[-1][2] = k + 1
        for ln, i1, i2 in lines:
            j1, j2 = dmap.get(i1, 0), dmap.get(i2 - 1, 0) + 1
            out.append(f'{ln:>7}  cipher: {D[i1:i2]}')
            out.append(f'{"":>7}  copy:   {T[j1:j2]}')
    out.insert(0, f'# Full decryption with key_full.tsv + construction_overrides.tsv. Both letters: {tot_m}/{tot_n} '
                  f'= {tot_m / tot_n:.3f} of decrypted letters match the copy (exploratory; built on these same lines).')
    out.append('\n# copy: second-reading readings not applied automatically: ' + ('; '.join(copy_notes) or 'none'))
    run = [r for r in b.load_rows('transcription/round1_catalogue/f406r_cipher.tsv') if r[0] == '406r' and r[1] == 13]
    if run:
        s = ''.join('?' if key.get(b.sign_of(x)) is None else key[b.sign_of(x)] for x in run[0][3])
        out.append(f'\n== f. 406r l. 13, short run inside the clear text: {s}')
    (HERE / 'results' / 'full_decryption.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'results' / 'full_variants.tsv').write_text('\n'.join(var) + '\n', encoding='utf-8')
    print(out[0]); print('\n'.join(x for x in out if x.startswith('==')))
    print(len(var) - 1, 'variant stretches of 4+ letters')


if __name__ == '__main__':
    main()
