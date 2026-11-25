"""Write the two transcriptions of catalogue 2857 in George Lasry's sign names, from the frozen records.

    python make_transcriptions.py

The readers transcribed with neutral sheet ids (K01-K58), each a sign cut from Lasry's key image for BnF Espagnol
318 no. 95 (records/solver/signsheet_K_private_map.json gives the column letter and row of each id). This script
turns the ids into the sign names of Lasry's CTTS key (../esp318no95/lasry2021/ctts/key.txt), checks that every name
carries the same letter in his key as the column it was cut from, and writes:

  transcription_blind.txt    the strict blind transcription: two readers who knew no values, reconciled by script
                             (records/verifier/transcription_reconciled.txt); holes closed only where later fresh
                             blind readers agreed: a third reading (two more readers; a hole closes when three of four
                             readers agree; records/third_reading/transcription_strict_round3_ids.txt) and a fourth
                             (two more readers with a sign sheet cut from the 1496 letters; four of six readers agree;
                             records/fourth_reading/tests/recount1497_stretches.tsv); put in reading order; every
                             position still without agreement is '#'
  transcription_working.txt  the first transcription (records/solver/transcription_reconciled.txt) with the five
                             corrections the image supports, and the dotted h sign written as its own sign
  transcription_differences.md  the edits, and every place where the two transcriptions differ

Standard library only; deterministic.
"""
import difflib, hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
KEY = HERE.parent / 'esp318no95' / 'lasry2021' / 'ctts' / 'key.txt'
KEY_SHA = '5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06'
REC = HERE / 'records'

# Lasry's sign names by column and row of his key image (rows top to bottom, as in key.txt; L3 is his "i... - l",
# R4 his "p - r", added below the table)
ROWS = {'A': ['X_', 'Z'], 'B': ['I-'], 'C': ['4', 'oI'], 'D': ['7', ':-', 'S'], 'E': ['=.', 'C.'], 'F': ['Y'],
        'G': ['-I-'], 'H': ['I-o'], 'I': ['pi0', 'u_'], 'L': ['ee', 'n+', 'i...'], 'M': ['_I_o', 'gt', 'yt'],
        'N': ['7+', 'L'], 'O': ['77', 'pi:', 'pi'], 'P': ['.X.', 'np'], 'Q': ['-o-', 'm'],
        'R': ['T:', 'p++', 'a_', 'p'], 'S': ['7-', '7o'], 'T': ['D-', 'X'], 'U': ['FB', 'ct'], 'Y': ['C', 'of'],
        'Z': ['o', 'b++']}
SPECIAL = {'nine_dot': '9', 'D_null': 'D', 'aunque': 'oN'}

# corrections to the first transcription (0-based position in the whole text, old id, new id, reason)
EDITS = [
    (83, 'K19', 'K16', 'L3 "guela" -> "guera": a top stroke runs over the bowl, as in Lasry\'s R sign a_ '
                       '(both blind readers of the check, and the first blind reader, read it so)'),
    (96, 'K20', 'K04', 'L4 "modtrar" -> "mostrar": a bar crosses the diagonal of the 7 (Lasry\'s S sign 7-)'),
    (116, 'K20', 'K04', 'L4 "led dio" -> "les dio": crossbar on the 7 (7-)'),
    (147, 'K20', 'K04', 'L5 "led hizo" -> "les hizo": crossbar on the 7 (7-)'),
    (148, 'K42', 'N02', 'L5 "hizo": the h is Lasry\'s H sign with two dots before the o; his table has no such sign, '
                        'so it is written as its own sign, with no value (the first transcription gave it H by a class rule)'),
    (164, 'K16', 'K19', 'L6 after [dal]: an upright bowl with no top stroke, Lasry\'s L sign ee, not R (both blind '
                        'readers of the check, and the first blind reader)'),
]


def load_key():
    raw = KEY.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == KEY_SHA, 'Lasry key.txt is not the version these files were made with'
    key = {}
    for line in raw.decode('utf8').splitlines():
        if line.startswith('#') or ' - ' not in line:
            continue
        signs, value = line.rsplit(' - ', 1)
        for s in signs.split('|'):
            key[s] = value
    return key


def kmap(key):
    priv = json.loads((REC / 'solver' / 'signsheet_K_private_map.json').read_text(encoding='utf8'))
    out = {}
    for k, lab in priv.items():
        m = re.fullmatch(r'([A-Z])(\d)', lab)
        if m:
            name = ROWS[m.group(1)][int(m.group(2)) - 1]
            assert key[name].lower() == m.group(1).lower(), (k, lab, name, key[name])
        else:
            name = SPECIAL.get(lab, '_' + lab)
            assert name in key, (k, lab, name)
        out[k] = name
    assert len(set(out.values())) == len(out) == 58
    return out


def read_lines(path):
    d = {}
    for l in path.read_text(encoding='utf8').splitlines():
        m = re.match(r'(L\d[ab]?):\s*(.*)', l)
        if m and m.group(1) not in d:
            d[m.group(1)] = m.group(2).split()
    return d


def name(t, km):
    if t in ('D', '#', '?'):
        return '#'
    if t.startswith('['):
        return t
    if re.fullmatch(r'N\d\d', t):
        return f'[{t}]'
    return km[t]


HEAD = ('# Catalogue 2857: Juan Manuel to the Catholic Monarchs, Genoa, 14 April 1497 (Archivo Historico Provincial de '
        'Zaragoza, Coleccion Zurita, C_CRAR/000001/0039), the cipher block of the recto\n'
        '# Signs in George Lasry\'s names for BnF Espagnol 318 no. 95 (../esp318no95/lasry2021/ctts/key.txt), separated '
        'by spaces; one line per manuscript line; L7 ends "...no se hazer a-", L8 is "si." before the clear dating\n'
        '# # = no value: a position the readers did not agree on, or damaged. [N03] = u/v-shaped sign with a bar, '
        '[N02] = Lasry\'s H sign I-o with two dots before the o: neither is in his table, and neither has a value. '
        '[bnm] = a group written in Latin letters, not in his table\n')


def main():
    key = load_key()
    km = kmap(key)
    # strict blind text, in reading order (the right-hand part of line 8 continues line 7)
    v = read_lines(REC / 'verifier' / 'transcription_reconciled.txt')
    vso = read_lines(REC / 'verifier' / 'transcription_reconciled_solverorder.txt')
    first = {f'L{i}': v[f'L{i}'] for i in range(1, 7)}
    first['L7'] = v['L7'] + v['L8b']
    first['L8'] = v['L8a']
    assert first == {k: vso[k] for k in first} and len(vso) == 8
    # the third and fourth blind readings close holes of that text (manuscript line order, L8a / L8b apart)
    strict = read_lines(REC / 'third_reading' / 'transcription_strict_round3_ids.txt')
    strict = {L: [t for t in (('#' if x == '#' else km[x]) for x in toks) if t != 'D'] for L, toks in strict.items()}
    closed = 0
    stretches = (REC / 'fourth_reading' / 'tests' / 'recount1497_stretches.tsv').read_text(encoding='utf8').splitlines()[1:]
    for row in sorted((r.split('\t') for r in stretches), key=lambda r: (r[0], -int(r[1]))):
        L, a, b, result = row[0], int(row[1]), int(row[2]), row[9].split()
        if row[10] != 'open':
            strict[L][a - 1:b] = result
            closed += sum(t != '#' for t in result)
    assert closed == 5, closed
    # the frozen strict text of the fourth reading, for comparison: identical except one position, L4 22, where its
    # conversion of the readers' sheet id K50 (Lasry's i..., the letter l) gave a hole; here the sheet map gives i...
    frozen = {L.strip(): [('_dal' if t == '§dal' else '#' if t in ('#', '?') else t) for t in rest.split()]
              for L, rest in (l.split(':', 1) for l in (REC / 'fourth_reading' / 'tests' / 'strict_round5_names.txt')
                              .read_text(encoding='utf8').splitlines() if ':' in l)}
    diffs = [(L, i + 1, a, b) for L in strict for i, (a, b) in enumerate(zip(strict[L], frozen[L])) if a != b]
    assert [len(strict[L]) for L in strict] == [len(frozen[L]) for L in frozen] and diffs == [('L4', 21, 'i...', '#')], diffs
    blind = {f'L{i}': strict[f'L{i}'] for i in range(1, 7)}
    blind['L7'] = strict['L7'] + strict['L8b']
    blind['L8'] = strict['L8a']
    # first transcription with the edits
    s = read_lines(REC / 'solver' / 'transcription_reconciled.txt')
    order = [f'L{i}' for i in range(1, 9)]
    flat = [(L, t) for L in order for t in s[L]]
    for pos, old, new, _ in EDITS:
        assert flat[pos][1] == old, (pos, flat[pos], old)
        flat[pos] = (flat[pos][0], new)
    work = {L: [t for LL, t in flat if LL == L] for L in order}
    out = {}
    for label, d, what in (('blind', blind, 'Strict blind transcription: two readers who knew no sign values, '
                            'reconciled mechanically, with holes closed only where later fresh blind readers agreed '
                            '(three of four, then four of six readers); every position without agreement is a hole (#)'),
                           ('working', work, 'Working transcription: the first transcription with the five '
                            'corrections the image supports, and the dotted h written as its own sign '
                            '(transcription_differences.md)')):
        rows = {L: (list(d[L]) if label == 'blind' else [name(t, km) for t in d[L]]) for L in order}   # blind: names already
        out[label] = rows
        txt = f'# {what}\n' + HEAD + ''.join(f'{L}: ' + ' '.join(rows[L]) + '\n' for L in order)
        (HERE / f'transcription_{label}.txt').write_text(txt, encoding='utf8')
    # differences
    md = ['# Transcription differences, catalogue 2857', '',
          'Both texts are in George Lasry\'s sign names. Positions count from 1 over the whole cipher block, in the '
          'working text.', '', '## Edits to the first transcription', '',
          '| position | line | first transcription | working | why |', '|---|---|---|---|---|']
    for pos, old, new, why in EDITS:
        md.append(f'| {pos + 1} | {flat[pos][0]} | `{name(old, km)}` | `{name(new, km)}` | {why} |')
    wseq = [(L, t) for L in order for t in out['working'][L]]
    bseq = [(L, t) for L in order for t in out['blind'][L]]
    sm = difflib.SequenceMatcher(a=[t for _, t in wseq], b=[t for _, t in bseq], autojunk=False)
    rows, eq, diff, only_b, only_w = [], 0, 0, 0, 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            eq += i2 - i1
            continue
        n = max(i2 - i1, j2 - j1)
        for k in range(n):
            a = wseq[i1 + k] if i1 + k < i2 else None
            b = bseq[j1 + k] if j1 + k < j2 else None
            if a and b:
                diff += 1
            elif b:
                only_b += 1
            else:
                only_w += 1
            rows.append(f'| {(i1 + k + 1) if a else "-"} | {(a or b)[0]} | `{a[1] if a else "-"}` | `{b[1] if b else "-"}` |')
    md += ['', '## Working text against the strict blind text', '',
           f'Aligned by minimum edit (difflib): {eq} positions equal, {diff} different, {only_b} only in the blind '
           f'text, {only_w} only in the working text. In the blind text # marks a place where its readers '
           'did not agree (or one of them wrote nothing); most differences are of that kind, not a different sign. '
           'One position of the strict text, L4 22 (the l of "les", Lasry\'s i...), is a hole in the frozen record '
           'records/fourth_reading/tests/strict_round5_names.txt only because that record\'s conversion of the readers\' '
           'sheet id K50 failed; the sheet map (records/solver/signsheet_K_private_map.json, K50 = L3, his i...) and '
           'the earlier blind texts give i... there.', '',
           '| working position | line | working | blind |', '|---|---|---|---|'] + rows
    (HERE / 'transcription_differences.md').write_text('\n'.join(md) + '\n', encoding='utf8')
    print('blind', sum(len(r) for r in out['blind'].values()), 'positions;',
          'working', sum(len(r) for r in out['working'].values()), 'positions;',
          f'equal {eq}, different {diff}, only blind {only_b}, only working {only_w}')


if __name__ == '__main__':
    main()
