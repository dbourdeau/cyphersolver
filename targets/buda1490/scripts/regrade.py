"""Regrade of every word measure.py counts as read (escalation step "retry", second half, 30 Oct 2026): the
retry pass (scripts/retry.py) re-ran the unread words; this re-runs the read ones, and the doubtful readings among
them (spelling variants, the cipher's own wording, added words, words read only with the extended key), and asks of
each how far its reading rests on the minute.

For each read word the signs are decoded again, sign by sign, with every value a key allows for that sign (nulls may
give nothing), and the test is whether they can give the word as read:
  B    key.json gives it, and so does the blind key key14 (scripts/data/key14.json, recovered from the ciphertext
       alone before the minute was found): the reading does not rest on the minute;
  K    key.json gives it, key14 does not (key14 had a sign wrong, or as a null): the value comes from the alignment
       with the minute, which key14 did not confirm;
  X    only the extended key gives it (qA = i/t, retry pass): a minority value from the alignment;
  C    a code sign gives it (y = 200,000, non, quoniam, quod): the meaning of a code sign rests on the minute alone;
  D    no key gives the word as read: the reading takes an abbreviation or emendation (listed with the reason).
The words are taken in the cipher's own order: where the alignment crossed the minute's word order (P3L04-05
"habere uelit tantum", P2L22 "neque uideat a quibus") the stretch is tested as one group against the cipher's wording.

    python scripts/regrade.py      writes reading/regrade.md and prints the summary
"""
import collections, functools, importlib.util, json, pathlib

H = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('measure', H / 'measure.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
P, WID = M.P, M.WID
K14 = json.load(open(H / 'scripts/data/key14.json'))

# Stretches the alignment crossed, tested as one group in the cipher's order (measure.py WORDING, DISPLAY, EXTRA_ADDED)
GROUPS = {('P3L04', 'tantum'): ('habereuelittantum', [('P3L04', 'tantum'), ('P3L05', 'habere')]),
          # neque in full (P o oH qB w); [u]ieat inside the stretch is the unread uideat, d left out (Remaining gaps)
          ('P2L22', 'imo'): ('nequeuieataquibus', [('P2L22', 'imo'), ('P2L22', 'quod'), ('P2L22', 'ambobus')])}
IN_GROUP = {m: g for g, (_, ms) in GROUPS.items() for m in ms}
EXTRA = {('P3L04', 'tantum'): 1}             # uelit, the word measure.py adds inside that stretch (EXTRA_ADDED)
# Readings that take an abbreviation the key does not spell out (none left after the group test)
ABBREV = {}


def vals(s, which):
    """Letter values sign s may give under key.json ('K'), key.json + extended ('X') or key14 ('B')."""
    if which == 'B':
        v = K14.get(s)
        if v is None or v == '#': return set()
        return set(v.split('/')) if '/' in v else {v}
    k = M.KEY.get(s)
    if not k or k['kind'] == 'code': return set()
    out = {'' if k['kind'] == 'null' else v for v in k['values']} if k['values'] else set()
    if which == 'X': out |= M.EXTENDED.get(s, set())
    return out


def gives(signs, target, which):
    @functools.lru_cache(None)
    def go(i, j):
        if i == len(signs): return j == len(target)
        return any(target.startswith(v, j) and go(i + 1, j + len(v)) for v in vals(signs[i], which))
    return go(0, 0)


def main():
    recs, adds = M.classify()
    units = collections.defaultdict(list)
    for p in P:
        for i in range(p['a'], p['b']):
            if p['type'] != 'skip' and (not units[WID[i]] or units[WID[i]][-1] is not p): units[WID[i]].append(p)
    by_key = {(r['line'], r['clear']): r for r in recs}
    rows, grades, kinds = [], collections.Counter(), collections.defaultdict(collections.Counter)
    done = set()
    for r in recs:
        if r['status'] not in M.SENSE or r['w'] in done: continue
        key = (r['line'], r['clear'])
        if key in IN_GROUP:
            target, members = GROUPS[IN_GROUP[key]]
            ws = [by_key[m]['w'] for m in members]
            done.update(ws)
            span = [P.index(p) for w in ws for p in units[w]]
            us = [p for p in P[min(span):max(span) + 1] if p['type'] != 'skip']   # signs the alignment gave no word too
            shown = ' '.join(by_key[m]['clear'] for m in members)
        else:
            target, us, shown = r['form'], units[r['w']], r['clear']
        target = target.replace('_', '')
        codes = [p for p in us if (M.KEY.get(p['sign']) or {}).get('kind') == 'code'
                 or (p['type'] == 'code' and p['txt'] in M.EXT_CODE.get(p['sign'], ()))]
        signs = tuple(p['sign'] for p in us if p not in codes)
        if codes:
            g, why = 'C', 'code sign ' + '/'.join(p['sign'] for p in codes) + ' = ' + r['form'].strip('{}')
        elif not '{' in target and gives(signs, target, 'K'):
            if gives(signs, target, 'B'): g, why = 'B', 'key.json and the blind key14 give it'
            else:
                miss = [p for p in us if p not in codes and p['txt'] not in vals(p['sign'], 'B')] if key not in IN_GROUP else \
                       [p for p in us if not vals(p['sign'], 'B') & vals(p['sign'], 'K')]
                g, why = 'K', 'key14 differs on ' + ', '.join(dict.fromkeys(
                    f"{p['sign']} = {p['txt'] or 'null'} (key14 {K14.get(p['sign'], 'none') or 'null'})" for p in miss))
        elif gives(signs, target, 'X'):
            g, why = 'X', 'extended key: ' + ', '.join(f'{s} = {"/".join(sorted(M.EXTENDED[s]))}' for s in dict.fromkeys(signs) if s in M.EXTENDED)
        else:
            g, why = 'D', ABBREV.get(key, 'no key gives the form as read')
        kind = 'group' if key in IN_GROUP else r['status']
        n = len(GROUPS[IN_GROUP[key]][1]) + EXTRA.get(IN_GROUP.get(key), 0) if key in IN_GROUP else 1
        grades[g] += n; kinds[kind][g] += n
        if kind != 'exact' or g != 'B':
            rows.append((r['line'], shown, target, kind, ' '.join(signs + tuple(p['sign'] for p in codes)), g, why))
    for a in adds:
        if a['status'] not in M.SENSE: continue
        if not a['signs']: continue                      # uelit: tested inside the P3L04-05 group
        s = a['signs']
        if s == '&':
            g, why = ('B' if 'et' in vals('&', 'B') else 'K'), '& = et in both keys'
        else:
            g, why = 'C', f'code sign {s} = {a["form"]}'
        grades[g] += 1; kinds['added'][g] += 1
        rows.append((a['line'], '(added)', a['form'], 'added', s, g, why))
    total = sum(grades.values())
    order = ('B', 'K', 'X', 'C', 'D')
    L = ['# Regrade of the read words (scripts/regrade.py, 30 Oct 2026)', '',
         'Every word measure.py counts as read, decoded again sign by sign with every value a key allows, and graded by '
         'what the reading rests on. B = key.json and the blind key14 (ciphertext only, before the minute was found) both '
         'give it; K = key.json gives it, key14 does not; X = only the extended key (retry pass) gives it; C = a code '
         'sign, whose meaning rests on the minute alone; D = no key gives the form as read (abbreviation or emendation). '
         'Stretches where the alignment crossed the minute\'s word order are tested as one group in the cipher\'s order.', '',
         f'Read words {total}: ' + ', '.join(f'{g} {grades[g]}' for g in order) +
         f'. Independent of the minute (B): {grades["B"]} ({100 * grades["B"] / 624:.1f}% of the 624 words).', '']
    L.append('| kind | ' + ' | '.join(order) + ' |'); L.append('|---|' + '---|' * len(order))
    for kd in ('exact', 'spelling', 'wording', 'group', 'added'):
        L.append(f'| {kd} | ' + ' | '.join(str(kinds[kd][g]) for g in order) + ' |')
    L += ['', 'Every read word that is not an exact word graded B:', '',
          '| line | minute | read | kind | signs | grade | why |', '|---|---|---|---|---|---|---|']
    for row in rows:
        L.append('| ' + ' | '.join(row) + ' |')
    (H / 'reading/regrade.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L[:14]))
    return grades, kinds


if __name__ == '__main__':
    main()
