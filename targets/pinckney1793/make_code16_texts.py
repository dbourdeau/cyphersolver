"""Build the transcription (ct/) and decryption (texts/*_decryption.txt) files of the other Code No. 16 letters from
Andrew Beling's witness files in beling/witnesses/ (PR #399). Run from targets/pinckney1793:

    python make_code16_texts.py

It reads only beling/witnesses/ and writes only ct/<doc>.txt and texts/<doc>_decryption.txt for the six documents
below. The readings (texts/<doc>_reading.txt) are written by hand from these decryptions and are not touched.
A decryption line is "groups=word" in manuscript order: the word is the one written over the groups at the time
(Taylor's, Wagner's, Graham's or the unnamed clerk's interlinear), or, for Eaton's coded copy of the Bey's letter, the
word of the 1802 printed translation that the groups were aligned to. "groups=" with nothing after it means nothing
is written over the group (it belongs to the word before or after). {..} is clear text on the line.
"""
import csv, re
from pathlib import Path

H = Path(__file__).resolve().parent
W = H / 'beling' / 'witnesses'


def rows(path):
    lines = [l for l in open(path, encoding='utf-8') if not l.startswith('#')]
    return list(csv.DictReader(lines, delimiter='\t'))


def write(name, text):
    (H / name).write_text(text, encoding='utf-8', newline='\n')
    print('wrote', name)


def from_spans(doc, title, src, spans, linekey, lines_txt=None, line_filter=None, note=''):
    """Interlined witnesses: spans.tsv has one row per span (groups, interlinear, kind, placement)."""
    rs = rows(spans)
    by = {}
    for r in rs:
        by.setdefault(linekey(r), []).append(r)
    ct = [f'# {title}: code groups as transcribed, one line per manuscript line; ? doubtful digit, _ or * digits lost,',
          f'# + ++ ^ marks written with the group. Clear words on the coded lines are left out here (they are in the decryption).',
          f'# Source: {src}. Transcription: Andrew Beling (beling/witnesses/, PR #399).']
    de = [f'# {title}: groups=word written over them at the time; ~ after a word = its placement over the groups is',
          f'# ambiguous; {{..}} = clear text on the line; "groups=" alone = nothing written over the group. {note}'.rstrip()]
    for k, lr in by.items():
        g = ' '.join(r['groups'].strip() for r in lr if r['groups'].strip() and not r['groups'].strip().startswith('{'))
        if g:
            ct.append(f'{k} {g}')
        toks = []
        for r in lr:
            gr, w = r['groups'].strip(), r['interlinear'].strip()
            amb = '~' if r['placement'].strip() == 'ambiguous' else ''
            if r['kind'].strip() == 'clear-on-line' or gr.startswith('{'):
                toks.append('{' + (w or gr.strip('{}')) + '}')
            else:
                toks.append(f"{gr.replace(' ', '.')}={w}{amb if w else ''}")
        de.append(f'{k} ' + ' '.join(toks))
    write(f'ct/{doc}.txt', '\n'.join(ct) + '\n')
    write(f'texts/{doc}_decryption.txt', '\n'.join(de) + '\n')


def tunis():
    doc = 'eaton_18021009'
    title = "Eaton's coded copy of Hammuda Bey to Jefferson, Tunis, 8 Sep 1802, with Eaton's coded postscript (enclosed in Eaton to Madison, 9 Oct 1802; Code No. 16)"
    body = rows(W / 'tunis_1802-09-08_enclosure' / 'tunis_word_spans.tsv')
    ps = rows(W / 'tunis_1802-09-08_enclosure' / 'tunis_postscript_spans_v2.tsv')
    ct = [f'# {title}: code groups as transcribed; a dash joins the groups of one word (Eaton\'s own dashes), a space',
          '# separates words; ^ caret under a group, + inflection mark, ? doubtful digit. One line per section of the manuscript.',
          '# Source: NARA RG 59, T303 roll 2, frames 0299-0303. Transcription: Andrew Beling (beling/witnesses/, PR #399).']
    de = [f'# {title}: groups=word. The words of the body are those of the 1802 printed English translation (American',
          '# State Papers, Claims, p. 331) that the groups were aligned to by hand; the postscript follows the Madison Papers',
          "# editors' decipherment. Flags from the alignment: (x) the cipher differs from the print or is unresolved,",
          '# (u) uncertain, (d) date line, low confidence.']
    sec = None; cl = []; dl = []
    def flush():
        if cl:
            ct.append(f'[{sec}] ' + ' '.join(cl)); de.append(f'[{sec}] ' + ' '.join(dl))
    for r in body:
        if r['section'] != sec:
            flush(); sec = r['section']; cl = []; dl = []
        cl.append(r['groups']); dl.append(f"{r['groups']}={r['word']}" + (f"({r['flag']})" if r['flag'] else ''))
    flush()
    sec = 'postscript'; cl = [r['groups'] for r in ps]
    dl = [f"{r['groups']}={r['word']}" + (f"({r['flag']})" if r['flag'] else '') for r in ps]
    flush()
    write(f'ct/{doc}.txt', '\n'.join(ct) + '\n')
    write(f'texts/{doc}_decryption.txt', '\n'.join(de) + '\n')


def eaton_oct22():
    doc = 'eaton_18021022'
    title = 'Eaton to Madison, Tunis, 22 Oct 1802, the coded passage (Code No. 16)'
    d = W / 'eaton_1802-10-22'
    A = [r for r in rows(d / 'transcription_A.tsv') if r['kind'] == 'code']
    B = [r for r in rows(d / 'transcription_B.tsv') if r['kind'] == 'code']
    il = {}
    for l in open(d / 'interlinear_B_SPOILER.tsv', encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) > 3 and p[1].isdigit():
            il.setdefault(p[1], []).append(f"{p[2].replace('above ', '')}={re.sub(r' *\[.*$', '', p[3])}")
    ct = [f'# {title}: two blind transcriptions of the numerals (A and B), line by line; where they differ both are given.',
          '# ? doubtful digit, * digit hidden, + mark after the group, - Eaton\'s dash inside a word, . his stop after a word.',
          '# Source: NARA RG 59, T303 roll 2, frame 0320. Transcription: Andrew Beling (beling/witnesses/eaton_1802-10-22/, PR #399).']
    de = [f'# {title}: the words a hand of the time wrote over the groups (interlinear as read by transcriber B),',
          '# "groups=word", line by line. The passage repeats the postscript of 9 Oct 1802 (eaton_18021009).']
    for a, b in zip(A, B):
        n = a['line_no']
        ct.append(f'L{n} A: {a["content"]}')
        if a['content'] != b['content']:
            ct.append(f'L{n} B: {b["content"]}')
        de.append(f'L{n} ' + ' '.join(il.get(n, [])))
    write(f'ct/{doc}.txt', '\n'.join(ct) + '\n')
    write(f'texts/{doc}_decryption.txt', '\n'.join(de) + '\n')


if __name__ == '__main__':
    from_spans('eaton_18010525', 'William Eaton to the Secretary of State, Tunis, 25 May 1801 (Code No. 16), copy A',
               'NARA RG 59, T303 roll 2, frame 0049 (copy B, frame 0048, has the same 196 groups)',
               W / 'eaton_1801-05-25' / 'spans.tsv', lambda r: r['line'],
               note="Interlinear: Jacob Wagner's (State Department).")
    from_spans('lear_181301', 'Tobias Lear to James Madison, [January 1813] (Code No. 16)',
               'Library of Congress, James Monroe Papers, reel 5 (mss33217.005), images 981-982',
               W / 'lear_1813-01' / 'lear1813_spans.tsv', lambda r: r['line'],
               note="Interlinear: John Graham's (State Department).")
    from_spans('pinckney_179508', 'Thomas Pinckney, the coded parts of his letters of 21 Jul and 11 Aug 1795 re-enciphered in "Cypher 2d" (enclosed 27 Aug 1795), and of 1 Oct 1795 (Code No. 16)',
               'NARA RG 59, M31 roll 7, frames 0018-0021',
               W / 'pinckney_1795_madrid' / 'spans.tsv', lambda r: f"{r['frame']}-{r['line']}",
               note="Interlinear: George Taylor Jr.'s (State Department).")
    from_spans('pinckney_179510', 'Thomas Pinckney, San Ildefonso 1 Oct, San Lorenzo 28 Oct (with his notes on the treaty) and Paris 18 Dec 1795 (Code No. 16)',
               'NARA RG 59, M31 roll 7, frames 0020, 0111, 0134-0135, 0177',
               W / 'pinckney_1795_oct-dec' / 'spans.tsv', lambda r: f"{r['frame'].replace('M31-007-', '')}-{r['page'][0].upper()}-{r['line']}",
               note="Interlinear: a State Department clerk's; on 0134-0135 the decipherment is in the margin, not aligned to the groups.")
    tunis()
    eaton_oct22()
