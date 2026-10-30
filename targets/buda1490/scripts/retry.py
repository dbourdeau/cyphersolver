"""Retry pass (escalation step "retry", 30 Oct 2026): every word measure.py leaves unread, run again under the
extended key and regraded.

The extended key is key.json plus three things key.json's acceptance rule (>= 2 aligned cases and >= 4% of the
sign's occurrences) left out:
  1. minority values: a value the EM alignment gave the sign in >= 2 OTHER places (not counting the word under test);
  2. look-alike labels: the labels split from one shape family on the images (signs.md: q -> qA/qB/4, g -> gA/gB/g,
     oo -> ooA/ooB, h -> hA/hB, 8 -> 8/8A/8B/8C, 6 -> 6/6A/6B, 3 -> 3/3G, j -> j/jB, T -> T/Tx, w -> w/wL, B -> B/Bd,
     a -> a/al/aN, and the free-standing H next to o); a sign whose sister label carries the letter the sentence needs
     is a possible split error;
  3. code signs that meet the rule only once the code reading is counted (y = 200,000 at "ducenta milia").
Each unread word is then graded:
  C+   every failing sign is explained by (1) or (3): the word reads under the extended key; the value rests on the
       alignment with the minute (see "Circularity" in NOTES.md);
  M    a failing sign is explained only by (2): the word reads if the label is wrong, which only the image can say;
       for the signs already checked on the image and confirmed as written (suspects.md) the grade is M-slip: the
       writer wrote the sister sign, so the cipher itself carries the slip;
  -    nothing in the extended key explains the failing sign (writer slip with no homophone link, or a different
       wording).
Damaged words are listed apart (a lost sign cannot be retried).

    python scripts/retry.py        writes reading/retry.md and prints the summary
"""
import collections, importlib.util, json, pathlib, re, sys

H = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('measure', H / 'measure.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
KEY, P, WID = M.KEY, M.P, M.WID
# the retry starts from the pre-retry measure: switch off what the retry added to measure.py
ADOPTED = dict(EXTENDED=M.EXTENDED, EXT_CODE=M.EXT_CODE,
               SPELLING={('P2L10', 'contraxerat'), ('P1L08', 'prefatum')},
               WORDING={('P2L20', 'deberet'), ('P3L08', 'necessaria'), ('P2L22', 'imo'), ('P2L22', 'quod'),
                        ('P2L22', 'ambobus')})
M.EXTENDED, M.EXT_CODE = {}, {}
M.SPELLING = M.SPELLING - ADOPTED['SPELLING']
WORDING_ALL = dict(M.WORDING)
M.WORDING = {k: v for k, v in M.WORDING.items() if k not in ADOPTED['WORDING']}
# sign values counted on the current alignment (key.json's aligned_counts predate the 29 Oct image fixes)
CNT = collections.defaultdict(collections.Counter)
for _p in P:
    if _p['type'] != 'skip': CNT[_p['sign']][_p['txt']] += 1

FAMILIES = [{'qA', 'qB', '4', 'q'}, {'gA', 'gB', 'g'}, {'ooA', 'ooB', 'oo'}, {'hA', 'hB'}, {'8', '8A', '8B', '8C'},
            {'6', '6A', '6B'}, {'3', '3G'}, {'j', 'jB'}, {'T', 'Tx'}, {'w', 'wL'}, {'B', 'Bd'}, {'a', 'al', 'aN'},
            {'H', 'Ho', 'oH'}]
fam = {s: f for f in FAMILIES for s in f}


def confirmed():
    """(line, token #) of suspects whose image check confirmed the sign as written."""
    out = {}
    for l in open(H / 'transcription/suspects.md', encoding='utf-8'):
        m = re.match(r'\| (P\dL\d\d) \| (\d+) \|', l)
        if m and (' confirmed ' in l or ' ambiguous' in l):
            out[(m.group(1), int(m.group(2)))] = 'confirmed' if ' confirmed ' in l else 'ambiguous'
    return out


def main():
    recs, adds = M.classify()
    conf = confirmed()
    pos, cur, n = {}, None, 0
    for p in P:
        if p['type'] == 'skip': continue
        if p['line'] != cur: cur, n = p['line'], 0
        pos[id(p)] = n + 1; n += p['ntok']
    units = collections.defaultdict(list)
    for p in P:
        for i in range(p['a'], p['b']):
            if p['type'] != 'skip' and (not units[WID[i]] or units[WID[i]][-1] is not p): units[WID[i]].append(p)
    rows, grades = [], collections.Counter()
    for r in recs:
        if r['status'] in M.SENSE: continue
        if r['status'] == 'damage':
            rows.append((r, 'damage', 'lost sign: nothing to retry')); grades['damage'] += 1; continue
        bad = [p for p in units[r['w']] if not M.ok(p)]
        why, grade = [], 'C+'
        for p in bad:
            s, t = p['sign'], p['txt']
            k = KEY.get(s) or {}
            key_t = t
            others = CNT[s].get(t, 0) - 1
            sis = sorted(x for x in fam.get(s, ()) if x != s and t in ((KEY.get(x) or {}).get('values') or []))
            c = conf.get((p['line'], pos.get(id(p))))
            if s == 'y' and p['type'] == 'code' and ('ducenta' in t or 'ducentorum' in t):
                why.append(f'{s} = code 200,000 (ducenta milia, 2 aligned cases of 5)')
            elif others >= 2 and key_t:
                why.append(f'{s} = {t or "null"} as a minority value ({others} other aligned cases of {sum(CNT[s].values())})')
            elif sis:
                why.append(f'{s} for {t}: sister label {"/".join(sis)} = {t}' + (f' (image: {c})' if c else ' (image not checked)'))
                grade = 'M-slip' if (c == 'confirmed' and grade != '-') else ('M' if grade == 'C+' else grade)
            else:
                why.append(f'{s} for {t or "(nothing)"}: no value, sister or code explains it' + (f' (image: {c})' if c else ''))
                grade = '-'
        if (r['line'], r['clear']) in ADOPTED['SPELLING']:
            why = ['every sign has its key value; a nasal (n, final m) left out, the usual omitted macron: spelling variant']; grade = 'C+'
        elif (r['line'], r['clear']) in ADOPTED['WORDING']:
            why = (why if grade == 'C+' else []) + ['the cipher word fits the sentence: ' + WORDING_ALL[(r['line'], r['clear'])]]; grade = 'C+'
        elif not bad: why.append('every sign has its key value: the cipher wording differs from the minute'); grade = '-'
        grades[grade] += 1
        rows.append((r, grade, '; '.join(why)))
    for a in adds:
        if a['status'] not in M.SENSE:
            rows.append((a, '-', a['note'])); grades['-'] += 1
    total = len(recs) + len(adds)
    read = sum(1 for r in recs + adds if r['status'] in M.SENSE)
    gain = grades['C+']
    L = ['# Retry pass over the unread words (scripts/retry.py, 30 Oct 2026)', '',
         'Every word measure.py leaves unread, retried under the extended key (key.json + minority values seen in >= 2 '
         'other places + look-alike labels + y = 200,000) and regraded. C+ = reads under the extended key (value from '
         'the alignment with the minute); M = reads only if a look-alike label was mis-split (image not checked, or checked and ambiguous); '
         'M-slip = the image confirmed the sign as written, so the slip is the cipher writer\'s; - = not explained.', '',
         f'Words {total}; read before the retry {read} ({100 * read / total:.1f}%).',
         f'Grades of the {total - read} unread words: ' + ', '.join(f'{g} {grades[g]}' for g in ('C+', 'M', 'M-slip', '-', 'damage')),
         f'Read with the C+ words: {read + gain} ({100 * (read + gain) / total:.1f}%); with C+ and M as well: '
         f'{read + gain + grades["M"]} ({100 * (read + gain + grades["M"]) / total:.1f}%); M-slip words, if a reader '
         f'accepts the emendation: {read + gain + grades["M"] + grades["M-slip"]} '
         f'({100 * (read + gain + grades["M"] + grades["M-slip"]) / total:.1f}%).', '',
         '| line | signs give | minute | was | grade | why |', '|---|---|---|---|---|---|']
    for r, g, why in rows:
        L.append(f"| {r['line']} | {r['form'] or '-'} | {r['clear'] or '(added)'} | {r['status']} | {g} | {why} |")
    out = '\n'.join(L) + '\n'
    (H / 'reading/retry.md').write_text(out, encoding='utf-8')
    print('\n'.join(L[:8]))
    return grades


if __name__ == '__main__':
    main()
