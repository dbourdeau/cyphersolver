"""Cut the contributor's two run tables out of his issue text, value for value.

    python extract.py            write transcription_A.txt, transcription_B.txt, decode_A.tsv, decode_B.tsv
    python extract.py --check    compare the files on disk with a fresh extraction, write nothing

Source: prior/issue784_SeldomPhooey_2026-11-18.md (issue #784, unchanged). Each table row is
| run | line | clear text around the run | cipher groups | decryption |. Nothing in a cell is edited: the doubt marks
(49?, ??, ?5, 1?) and the decryption marks ([?k], [?p], [?x], #) are his. The dagger his table puts after a run number
(a run corrected against the image) goes into its own column.
"""
import io, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'prior' / 'issue784_SeldomPhooey_2026-11-18.md'
HEAD = {'A': '### A. Post Scriptum, Tykocin, 1[3] March 1656 (scans 42-43): 112 runs, 673 groups',
        'B': '### B. P. S., Labiau, 3 December 165[6] (scans 39-40): 102 runs, 598 groups'}
DOC = {'A': 'A. "Post Scriptum", Tykocin, 1[3] March 1656: AGAD AR dz. IV 46 (1/354/0/4/46), scans 42-43',
       'B': 'B. "P. S.", Labiau, 3 December 165[6]: AGAD AR dz. IV 46 (1/354/0/4/46), scans 39-40'}


def rows(doc):
    """[(run, corrected, line, context, groups, decryption)] of one table, cells as written."""
    lines = SRC.read_text(encoding='utf-8').split('\n')
    i = lines.index(HEAD[doc])
    out = []
    for l in lines[i + 1:]:
        if l.startswith('### '): break
        if not l.startswith('| ' + doc): continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        assert len(cells) == 5, l
        run = cells[0]
        corrected = run.endswith('†')
        run = run.rstrip('†').strip()
        assert re.fullmatch(doc + r'\d{3}', run), run
        out.append((run, 'corrected' if corrected else '', cells[1], cells[2], cells[3], cells[4]))
    return out


def files(doc):
    r = rows(doc)
    n = sum(len(x[4].split()) for x in r)
    tr = [f'# radziwill1656: transcription of the cipher runs, document {DOC[doc]}',
          '# Transcribed by SeldomPhooey (issue #784, 18 Nov 2026; Claude-family AI agents) from the archive viewer images.',
          '# Cut from his table by extract.py with no value edited; not re-read against the images here.',
          '# One run per line: run number, then the two-digit groups in the order of the page. Marks are his:',
          '# NN? = the group is uncertain on the image; ?? or a ? in place of a digit = unreadable;',
          '# an overline (doubling) is written as the group twice (33 33 = mm).',
          f'# The page line, the clear text around each run and his decryption are in decode_{doc}.tsv.',
          f'# {len(r)} runs, {n} groups.']
    tr += [f'{x[0]} {x[4]}' for x in r]
    de = ['run\tcorrected\tline\tclear text around the run (_ = the run)\tcipher groups\tdecryption']
    de += ['\t'.join(x) for x in r]
    return {f'transcription_{doc}.txt': '\n'.join(tr) + '\n', f'decode_{doc}.tsv': '\n'.join(de) + '\n'}, len(r), n


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    check = '--check' in sys.argv
    bad = 0
    for doc in 'AB':
        out, nr, ng = files(doc)
        for name, text in out.items():
            p = HERE / name
            if check:
                same = p.exists() and p.read_text(encoding='utf-8') == text
                bad += not same
                print(f'{name}: {"same as the issue table" if same else "DIFFERS"}')
            else:
                p.write_text(text, encoding='utf-8', newline='\n')
        print(f'{doc}: {nr} runs, {ng} groups, {sum(1 for x in rows(doc) if x[1])} runs marked corrected')
    sys.exit(1 if bad else 0)
