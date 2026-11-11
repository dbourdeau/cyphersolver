"""Write ../decryption_1813-02-20.txt: the 1813 decryption line by line against Daniel Bourdeau's transcription
(../../transcription.tsv), group by group.

For each written line (the 41 rows of transcription.tsv for P1-P9, which match the 41 lines of our frozen numerals one
to one), five rows:
  Bourdeau  the group as in transcription.tsv
  frozen    our frozen reading (transcription/numerals_1813_frozen.txt, after the one correction made after the freeze)
  used      the number the reading uses (groups_1813-02-20.tsv); '-' for a hole
  WE025     its WE025 element (key/we025_poinsett.tsv; 668 = fect after the freeze), with the group's mark; for a hole,
            in brackets, the element of our frozen reading, which the reading does not use
  status    D A R I H as in groups_1813-02-20.tsv, X = struck-out group
and, when Bourdeau's number differs from the one used, a sixth row 'WE025(B)' with the element his number would give.

    python3 scripts/make_decryption.py
"""
import csv, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import texts

we = texts.load_key()
dan = texts.load_daniel_1813()
fro = texts.load_1813()
grp = list(csv.DictReader(open(texts.BEL / 'groups_1813-02-20.tsv', encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE))
assert len(dan) == len(fro) == 41, (len(dan), len(fro))


def dnum(t):
    """Bourdeau's number, if all its digits are written: '1436?' -> 1436 (doubtful), '788?°' -> 788, '15?9', '13??',
    '134...' -> None."""
    t = t.strip('[]').rstrip('°^+')
    if t.endswith('?'): t = t[:-1].rstrip('°^+')
    return int(t) if t.isdigit() else None


raw = texts.load_1813(apply_corrections=False)   # for comparing the two transcriptions as made
tr = {'first': 0, 'second': 0, 'differ': [], 'unread': []}
for d, f in zip(dan, raw):
    for b, t in zip(d['groups'], f['toks']):
        if t['raw'] == '[X]': continue
        bn = dnum(b)
        if bn is None or (len(t['alts']) == 1 and '?' in t['alts'][0]): tr['unread'].append(f"{f['label']} {b}/{t['raw']}")
        elif str(bn) == t['alts'][0]: tr['first'] += 1
        elif str(bn) in t['alts']: tr['second'] += 1
        else: tr['differ'].append(f"{f['label']} {b}/{t['raw']}")


same = differ = dunread = 0
diffs = []
out = []
gi = 0
for d, f in zip(dan, fro):
    n = len(f['toks'])
    assert len(d['groups']) == n, (f['label'], d['groups'], [t['raw'] for t in f['toks']])
    g = grp[gi:gi + n]; gi += n
    assert all(r['line'] == f['label'] for r in g)
    cols = []
    for i in range(n):
        r = g[i]
        b = d['groups'][i]
        used = r['used']
        ours = used or (re.match(r'\{?(\d+)', r['frozen']).group(1) if r['status'] == 'H' else '')   # a hole: our frozen first reading
        if r['status'] == 'X':
            el, st = '', 'X'
        elif r['status'] == 'H':
            el, st = f"({we.get(int(ours), '?')})", 'H'
        else:
            el, st = r['element'], r['status']
        bn = dnum(b)
        alt = ''
        if r['status'] != 'X':
            if bn is None: dunread += 1
            elif bn == int(ours): same += 1
            else:
                differ += 1
                alt = we.get(bn, '(none)')
                diffs.append(f"{f['label']}[{i}] {b} -> {ours}{' (hole)' if not used else ''}")
        cols.append([b, r['frozen'], used or '-', el, st, alt or ('' )])
    has_alt = any(c[5] for c in cols)
    names = ['Bourdeau', 'frozen', 'used', 'WE025', 'status'] + (['WE025(B)'] if has_alt else [])
    w = [max(len(c[k]) for k in range(len(names))) for c in cols]
    ctx = f'   clear before: {d["context"]}' if d['context'] else ''
    out.append(f"{f['label']:6} transcription.tsv {d['passage']}, frame {d['frame']}, line {d['line']}{ctx}")
    for k, nm in enumerate(names):
        out.append(f'  {nm:9} ' + '  '.join((c[k] or ('-' if k == 5 else '')).ljust(w[j]) for j, c in enumerate(cols)).rstrip())
    out.append('')

head = f"""# poinsett1813/beling: decryption of Poinsett to Monroe, Santiago, 20 Feb 1813 (NARA M37 roll 2, frames 0093-0094), passages P1-P9,
# with WE025 (Weber 1979, pp. 470-480), line by line against Daniel Bourdeau's transcription.tsv. Written by scripts/make_decryption.py.
# P0 (frame 0092) is not transcribed by either reader and is not here.
# Rows: Bourdeau = transcription.tsv; frozen = our numerals, frozen before decoding ({{a|b}} two readings kept open, ? digit unread,
#   ◇ diamond or ° circle over a group (Bourdeau writes ° for both), + cross, ^ caret: meanings inferred from use only (README);
#   [X] or [1249] struck-out group); used = number the reading uses;
#   WE025 = its element; status: D frozen first reading, A the other frozen reading, R reread on the image after decoding,
#   I assumed digit misread (not confirmed on the image), H hole (no element that makes sense; WE025's element for our frozen
#   reading shown in brackets, not used), X struck out;
#   WE025(B) = the element of Bourdeau's number where it differs from the one used.
# The two transcriptions (437 groups, the struck-out one excluded; ours as frozen, before the one later correction):
#   Bourdeau's number is our first frozen reading at {tr['first']}, our second at {tr['second']}; both read every digit and differ at
#   {len(tr['differ'])} ({', '.join(tr['differ'])});
#   one or both leave a digit unread at {len(tr['unread'])} ({', '.join(tr['unread'])}).
# Bourdeau's number equals the number the reading uses (for a hole, our frozen reading) at {same} groups, differs at {differ}
#   (WE025(B) rows), and has an unread digit at {dunread}. Holes count as groups but are not read.
# The reading as sentences is reading_1813-02-20.md; every group with its note is in groups_1813-02-20.tsv.
"""
pathlib.Path(texts.BEL / 'decryption_1813-02-20.txt').write_text(head + '\n' + '\n'.join(out), encoding='utf-8')
print(f"transcriptions: first {tr['first']}, second {tr['second']}, differ {len(tr['differ'])}, unread {len(tr['unread'])}")
print(f'vs number used: same {same}, differ {differ}, Bourdeau digit unread {dunread}')
print('\n'.join(diffs))
