"""Decode the cipher runs of both postscripts from key.tsv and compare with the contributor's decryption column.

    python decode.py             per document: runs whose decryption equals his column, group and mark counts
    python decode.py --print     also print every run with its decryption
    python decode.py --words     the decrypted letters of each run, one line per run (run TAB letters)
    python decode.py --write     also write decryption_A.txt and decryption_B.txt: this decoder's output, run by run,
                                 set in the clear words his table gives around each run
    python decode.py --validation  write validation.tsv, the token and letter pairs for docs/_validate.py

Written here from the key in issue #784, not from his scripts (which were not sent). A group is two digits, with an
optional ? after it for "uncertain on the image" (decoded all the same, as he does). A group with a ? in place of a
digit (??, ?5, 1?) is unreadable and gives #. A proposed value prints as [?k], [?p] or [?x].
Exit code 1 when any run differs.
"""
import io, re, sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent


def load_key():
    key = {}
    for l in (HERE / 'key.tsv').read_text(encoding='utf-8').splitlines():
        if not l.strip() or l.startswith('#') or l.startswith('value'): continue
        value, letter, grade = l.split('\t')[:3]
        key[value] = (letter.split('/')[0], grade)
    return key


def decode_group(g, key, seen):
    m = re.fullmatch(r'(\d\d)(\?)?', g)
    if not m:
        seen['unreadable'] += 1
        return '#'
    if m.group(2): seen['uncertain'] += 1
    letter, grade = key[m.group(1)]
    seen['values'].add(m.group(1))
    if grade == 'proposed':
        seen['proposed'] += 1
        return f'[?{letter}]'
    if grade == 'not seen':
        raise SystemExit(f'group {g}: the key marks this value as not seen')
    return letter


def runs(doc):
    out = []
    for l in (HERE / f'transcription_{doc}.txt').read_text(encoding='utf-8').splitlines():
        if not l.strip() or l.startswith('#'): continue
        run, *groups = l.split()
        out.append((run, groups))
    return out


def his(doc):
    rows = [l.split('\t') for l in (HERE / f'decode_{doc}.tsv').read_text(encoding='utf-8').splitlines()[1:] if l.strip()]
    return {r[0]: r for r in rows}


def validation(key):
    """validation.tsv: one group per line, doubt marks dropped from the token; a gap line between runs, because the
    runs stand among clear words and are not continuous text."""
    out = ['# model: de-1640s',
           '# source: transcription_A.txt and transcription_B.txt decoded with key.tsv (python decode.py --validation)',
           '# note: one two-digit group per line, the doubt mark dropped from the token; an unreadable group and the break '
           'between two runs are ? (no n-gram spans them); the proposed values of 29, 39 and 53 are given as k, p, x']
    for doc in 'AB':
        for run, groups in runs(doc):
            for g in groups:
                m = re.fullmatch(r'(\d\d)\??', g)
                out.append(f'{m.group(1)}\t{key[m.group(1)][0]}' if m else f'{g}\t?')
            out.append('/\t?')
    (HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
    print(f'validation.tsv: {len(out) - 3} lines')


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    key = load_key()
    if '--validation' in sys.argv:
        validation(key); sys.exit(0)
    bad = total_runs = total_groups = 0
    for doc in 'AB':
        table = his(doc)
        seen = collections.Counter(); seen['values'] = set()
        same = n = 0
        lines = [f'# radziwill1656: decryption of document {doc}, the unedited output of key.tsv on transcription_{doc}.txt '
                 '(python decode.py --write).',
                 '# One run per line: run, page line, then the clear words his table gives around the run with the decryption '
                 'between ** ** in place of the run.',
                 '# [?k] [?p] [?x] = the proposed values of 29, 39 and 53; # = a group that could not be read. Nothing is '
                 'corrected: a word the key gets wrong stays wrong.',
                 f'# Equal, run for run, to the decryption column of the contributor\'s table (decode_{doc}.tsv).']
        for run, groups in runs(doc):
            mine = ''.join(decode_group(g, key, seen) for g in groups)
            row = table[run]
            assert row[4].split() == groups, f'{run}: transcription and decode table differ'
            assert row[3].count('_') <= 1, f'{run}: more than one place for the run in the context'
            ctx = row[3] if '_' in row[3] else row[3] + ' _'      # B016: his cell has no _; the run follows the cell
            lines.append(f'{run}\t{row[2]}\t{ctx.replace("_", "**" + mine + "**")}')
            n += len(groups)
            ok = mine == row[5]
            same += ok
            if '--words' in sys.argv: print(f'{run}\t{mine}')
            elif '--print' in sys.argv or not ok:
                print(f'{run}\t{row[2]}\t{" ".join(groups)}\t{mine}' + ('' if ok else f'\tDIFFERS from his: {row[5]}'))
        r = len(runs(doc))
        bad += r - same; total_runs += r; total_groups += n
        if '--write' in sys.argv:
            (HERE / f'decryption_{doc}.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
        if '--words' not in sys.argv:
            print(f'{doc}: {same} of {r} runs decode to his decryption; {n} groups, {len(seen["values"])} distinct values; '
                  f'{seen["uncertain"]} groups marked uncertain (NN?), {seen["unreadable"]} unreadable (#), '
                  f'{seen["proposed"]} with a proposed value (29, 39, 53)')
    if '--words' not in sys.argv:
        print(f'total: {total_runs - bad} of {total_runs} runs match, {total_groups} groups')
    sys.exit(1 if bad else 0)
