#!/usr/bin/env python3
"""Build the partial table of the code ("cipher F") from the hand-corrected alignment."""
import sys, json, csv, collections
tok = json.load(open(sys.argv[1]))['tokens']
_rows = list(csv.DictReader(open(sys.argv[2]), delimiter='\t'))
corr = {int(r['token_index']): (int(r['brackx']), int(r['proposed'])) for r in _rows}
# digit changes that two blind readers did not read on the film (21 Nov 2026): kept as readings of the text,
# but such a use does not count towards "confirmed by repeated use"
EMENDED = {int(r['token_index']) for r in _rows if r.get('second_reading_2026-11-21', '').startswith('not confirmed')}
N_TRAIN = 568
FAMILY = {1078, 172, 174, 826, 663, 1126, 240, 151, 152, 1031, 355, 664, 474, 257}
JOINT = {634, 169, 716, 354, 1098, 470, 730, 216, 148, 714, 649, 593, 1154, 1022, 830, 540, 630, 41, 153, 998, 1186,
         273, 954, 1176, 113, 677, 301, 141, 992, 1156, 651, 1194, 660, 797, 715, 263, 76, 11, 60, 77, 187, 839, 854, 420, 905}
UNSURE = {383: 'd in extraor-d-inaire; "de (la)" before Chambre, where 363/362 = "de la" elsewhere; image reads 383 both times',
          571: 'stands where the draft has (se)rait and where it has general; both read 571 on the image; not resolved',
          1122: 'vr or v in de-vr-ait (twice); stands for "eur" in port-eur-s; not resolved',
          526: 'd in Mozar-d and in soin d(en) faire; stands after consulaire(s) before d economie; not resolved',
          347: 'qu ils; 247 = qu il(s) twice, so 347 may be a slip for 247 (Brackx: 347 or 367)',
          802: 'between "je compte" and "a cet egard": a comma, a null or a word not in the draft',
          411: 'between "delai" and "Il faut": punctuation (the draft has a colon)',
          1126: 'utile or utilite: stands for "utiles" once and once where the corrected draft reads "facilite" over an earlier word; value rests on that reading of the draft',
          251: 'ai in n-ai, n-ay-ez, consul-ai-re, but the NUMBER is a conjecture: Brackx and two blind readers read 257 on the film at all three places (second choice 251); 251 rests on the text and on the run 253 ainsi, 254 ajouter, 257 al',
          469: 'no letters: first group of the despatch and inside m-o-i-(469)-s at the end; a null'}
NOTE = {496: 'port in ap-port-eront, rap-port-s, port-eurs; also stands for "pui" in pui-s-se-nt (not explained)',
        257: 'al: a l(ouverture), prairi-al. The film also reads 257 at three places where the text has "ai" (see 251 and corrections)',
        100: 'sur; a third use (token 233) is an emendation: the film reads 108 or 128 there',
        361: 'del in de l(impatience); a second use (del-ai) is an emendation: the film reads 381, blotted',
        767: 'Adams. First time without a group for "M.", second time 935 = M(onsieur)',
        405: 'en / ent (15 times)', 39: 're (rez in au-rez, ver-rez)',
        175: 'se (session written se-si-on)', 855: 'pre (propres written pro-pre)'}
by = collections.defaultdict(list)
for i, (g, draft, meaning, kind) in enumerate(tok):
    if i in corr:
        assert corr[i][0] == g, (i, g, corr[i])
        g = corr[i][1]
    val = meaning if kind == 'text' else {'null': '(null)', 'stop': '(full stop)', 'unknown': '(unknown)'}[kind]
    by[g].append((i, val))

def common_prefix(a, b):
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]: n += 1
    return n

rows = []
for g in sorted(by):
    occ = by[g]
    cnt = collections.Counter(v for _, v in occ)
    vals = sorted(cnt.items(), key=lambda kv: (-kv[1], len(kv[0]), kv[0]))
    main = vals[0][0]
    shortest = min(cnt, key=len)
    fam = all(common_prefix(shortest, v) >= max(1, len(shortest) - 1) for v in cnt)
    n_film = sum(1 for i, _ in occ if i not in EMENDED)
    if g in UNSURE: cls = 'C'
    elif n_film < 2 and len(occ) >= 2 and len(cnt) == 1: cls = 'B' if n_film == 1 else 'C'
    elif len(occ) >= 2 and (len(cnt) == 1 or fam or g in FAMILY): cls = 'A'
    elif len(occ) >= 2: cls = 'C'
    elif g in JOINT: cls = 'B2'
    else: cls = 'B'
    note = UNSURE.get(g) or NOTE.get(g, '')
    rows.append([g, main, len(occ), len(occ) - n_film, cls, '; '.join('%s x%d' % kv for kv in vals) if len(vals) > 1 else '',
                 sum(1 for i, _ in occ if i < N_TRAIN), sum(1 for i, _ in occ if i >= N_TRAIN), note])
w = csv.writer(open(sys.argv[3], 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['group', 'value', 'occurrences', 'of_which_emended', 'class', 'all_values', 'in_first_568', 'in_last_85', 'note'])
w.writerows(rows)
c = collections.Counter(r[4] for r in rows)
tokc = collections.Counter()
for r in rows: tokc[r[4]] += r[2]
print('groups', len(rows), dict(c), 'tokens by class', dict(tokc))
# consistency of the hand table across the split (not the pre-set test; see TEST_PLAN Test 3 for that)
train = {}
for g in by:
    tv = collections.Counter(v for i, v in by[g] if i < N_TRAIN)
    if tv: train[g] = tv
hit = tot = unseen = 0
miss = []
for g in by:
    for i, v in by[g]:
        if i < N_TRAIN: continue
        if g not in train: unseen += 1; continue
        tot += 1
        if any(common_prefix(v, t) >= max(1, min(len(v), len(t)) - 1) for t in train[g]): hit += 1
        else: miss.append((i, g, v, dict(train[g])))
print('last 85 groups: %d have a value from the first 568; %d agree with the draft there; %d not seen before' % (tot, hit, unseen))
for m in miss: print('  differs:', m)
