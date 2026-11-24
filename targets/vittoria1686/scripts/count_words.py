#!/usr/bin/env python3
"""Count cipher words, sure words and holes in the five Vittoria Gonzaga letters by the README sure-word rule.

    python scripts/count_words.py

Cipher words come from the transcription files (words split at ' / ', [clear text] left out, a word carried
over a line end with '=' counted once, the two clear numerals 1000 and 50 left out). Holes come from the reading
files: in the cipher text (the parts not in *italics*), a word is a hole when it holds a supplied or changed
letter ([x]), a probable word ([?word]), a code group with no value ([200]) or a bracketed code whose value is not
graded sure. The cipher words found in each reading must equal those of its transcription.

Two adjustments to Letter 4 come from the image check of 24 Nov 2026 (NOTES.md): danno is written in full with
its doubling stroke (the reading file prints dan[n]o), and the word before ho on c. 21r is under a blot (the
reading file prints e). One adjustment to Letter 1 comes from the second reader of 24 Nov 2026: anni on c. 4r
(L1_4r_20) has the same doubling stroke over its 55 (Kennedy's note: "ink macron over 55"; the reading file
prints an[n]i), so it is counted sure like danno. The contributors' files are not edited.

Two gradings are printed: before the fifth letter (only 104 che sure, as on 24 Nov 2026) and after it
(key_additions_2026-11-24.tsv: 104, 159, 13, 182 and 109 sure).
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
K = ROOT / 'kennedy_2026'
LETTERS = [
    ('Letter 1, 2 Apr 1686, cc. 3v-4r', K / 'transcription_cc03r-04v_1686-04-02.txt', K / 'reading_cc03r-04v_1686-04-02.md'),
    ('Letter 2, 13 Apr 1688, c. 11r', K / 'transcription_cc11r-12v_1688-04-13.txt', K / 'reading_cc11r-12v_1688-04-13.md'),
    ('Letter 3, 4 Sept 1691, cc. 22r-23r', K / 'transcription_cc22r-23v_1691-09-04.txt', K / 'reading_cc22r-23v_1691-09-04.md'),
    ('Letter 4, 16 Oct 1691, cc. 20r, 21r', K / 'transcription_cc20r-21v_1691-10-16.txt', K / 'reading_cc20r-21v_1691-10-16.md'),
    ('Letter 5, 18 Sept 1691, cc. 24v-25r', ROOT / 'transcription_cc24v-25r.txt', ROOT / 'reading_cc24v-25r.md'),
]
CLEAR_NUMERALS = {('L2_11r_01', '1000'), ('L4_21r_03', '50')}
GRADINGS = {
    'before the fifth letter (only 104 che sure)': {'[che]'},
    'after the fifth letter (104, 159, 13, 182, 109 sure)': {'[che]', '[per]', '[et]', '[V.E.]', '[Duca]'},
}


def strip_clear(body):
    """Replace each [clear text] (brackets may nest, as in [5 p[er] 100]) by a word break."""
    out, depth = [], 0
    for ch in body:
        if ch == '[':
            if depth == 0:
                out.append(' / ')
            depth += 1
        elif ch == ']' and depth:
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return ''.join(out)


def transcription_words(path):
    words = []
    for ln in path.read_text(encoding='utf-8').splitlines():
        if ln.startswith('#') or not ln.strip():
            continue
        lab, body = ln.split(' ', 1)
        body = strip_clear(body)
        for w in body.split('/'):
            gs = w.split()
            if not gs:
                continue
            if (lab, ' '.join(gs)) in CLEAR_NUMERALS:
                continue
            if gs[0] == '=':                      # second half of a word carried over a line end
                continue
            words.append((lab, ' '.join(gs)))
    return words


def reading_words(path):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<!--.*?-->', ' ', text, flags=re.S)
    m = re.search(r'^## Italian\s*$', text, flags=re.M)
    if m:
        text = text[m.end():]
    out = []
    for ln in text.splitlines():
        if ln.startswith('#'):
            continue
        ln = re.sub(r'\*[^*]*\*', ' ', ln)            # clear text in italics
        ln = ln.replace('[dittogr. di]', '[dittogr_di]')
        for tok in ln.split():
            tok = tok.strip(',;:!?"()“”')
            if tok.endswith('.') and not tok.endswith('.]') and tok not in ('S.', 'D.'):
                tok = tok[:-1]
            for part in re.split(r"['’]", tok):
                if re.search(r'\w', part):
                    out.append(part)
    return out


def is_hole(tok, sure):
    if tok in sure:
        return False
    return '[' in tok


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    rows = []
    for name, tr, rd in LETTERS:
        tw = transcription_words(tr)
        rw = reading_words(rd)
        if name.startswith('Letter 1'):                   # doubling stroke over the 55 of anni, as for danno
            rw = ['anni' if t == 'an[n]i' else t for t in rw]
        if name.startswith('Letter 4'):
            rw = ['danno' if t == 'dan[n]o' else t for t in rw]
            i = next(k for k in range(len(rw) - 1) if rw[k] == 'e' and rw[k + 1] == 'ho')
            rw[i] = '[blot]'
        if name.startswith('Letter 5'):                   # the ink writes sene as one word; the reading prints se ne
            merged, k = [], 0
            while k < len(rw):
                if rw[k] == 'se' and k + 1 < len(rw) and rw[k + 1] == 'ne':
                    merged.append('sene'); k += 2
                else:
                    merged.append(rw[k]); k += 1
            rw = merged
        rows.append((name, tw, rw))
        flag = 'ok' if len(tw) == len(rw) else 'MISMATCH'
        print(f'{name}: {len(tw)} cipher words in the transcription, {len(rw)} in the reading ({flag})')
    for gname, sure in GRADINGS.items():
        print(f'\nCodes graded {gname}:')
        tot_w = tot_h = tot_w4 = tot_h4 = 0
        for name, tw, rw in rows:
            holes = [t for t in rw if is_hole(t, sure)]
            n, h = len(tw), len(holes)
            print(f'  {name}: {n - h} of {n} sure, {h} holes, {100 * (n - h) / n:.1f}%')
            print(f'    holes: {", ".join(holes)}')
            tot_w += n; tot_h += h
            if not name.startswith('Letter 5'):
                tot_w4 += n; tot_h4 += h
        print(f'  Letters 1-4: {tot_w4 - tot_h4} of {tot_w4}, {tot_h4} holes, {100 * (tot_w4 - tot_h4) / tot_w4:.1f}%')
        print(f'  Letters 1-5: {tot_w - tot_h} of {tot_w}, {tot_h} holes, {100 * (tot_w - tot_h) / tot_w:.1f}%')


if __name__ == '__main__':
    main()
