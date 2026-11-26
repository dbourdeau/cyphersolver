#!/usr/bin/env python3
"""Build the partial table of the code ("cipher F") from the hand-corrected alignment.

usage: build_table.py TOKENS.json PROPOSALS.tsv OUT.tsv [--brackx]
  TOKENS.json   written by check_manual.py (the 653 groups, Brackx's digits, with the draft letters of each)
  PROPOSALS.tsv proposals/transcription_corrections.tsv (comment lines start with #), read only to find the
                eight places where a digit change is proposed
  OUT.tsv       key/code_table_F_partial.tsv
The table is built on Brackx's digits as transcribed. No proposed digit change is applied: the proposals stay
unapplied until a person has looked at the film. --brackx (the earlier way to ask for this) is accepted and ignored."""
import sys, json, csv, collections
BRACKX = True   # Brackx's digits only; the mode that applied the proposals was removed on 23 Nov 2026
args = [a for a in sys.argv[1:] if a != '--brackx']
tok = json.load(open(args[0]))['tokens']
_rows = list(csv.DictReader((l for l in open(args[1], encoding='utf-8') if not l.startswith('#')), delimiter='\t'))
EMENDED = set()
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
          469: 'no letters: first group of the despatch and inside m-o-i-(469)-s at the end; a null'}
NOTE = {496: 'port in ap-port-eront, rap-port-s, port-eurs; also stands for "pui" in pui-s-se-nt (not explained)',
        257: 'al: a l(ouverture), prairi-al. The film also reads 257 at three places where the text has "ai" (see 251 and corrections)',
        100: 'sur; a third use (token 233) is an emendation: the film reads 108 or 128 there',
        361: 'del in de l(impatience); a second use (del-ai) is an emendation: the film reads 381, blotted',
        767: 'Adams. First time without a group for "M.", second time 935 = M(onsieur)',
        405: 'en / ent (15 times)', 39: 're (rez in au-rez, ver-rez)',
        175: 'se (session written se-si-on)', 855: 'pre (propres written pro-pre)'}
if BRACKX:
    NOTE.update({
        257: 'al: a l(ouverture), prairi-al; also stands three times where the text has "ai" (n-ai, n-ay-ez, consul-ai-re): proposed 251, see proposals/',
        100: 'sur (two uses); a third place where the text has "sur" reads 108 or 128 on the film (see 108)',
        361: 'del in de l(impatience); a second place where the text has "del" reads 381 on the film (see 381)',
        108: 'sur here only; proposed 100 (= sur twice); blotted; no blind reader read 100',
        381: 'del here only; proposed 361; blotted; no blind reader read 361',
        808: 'con here only (le-con); proposed 898 (= con four times); the film shows 898 with "80" written above (3 of 3 blind readers)',
        1024: 'ap in m-ap-porte-ront; also where the text has "e" (pri-e): proposed 1034 there (1033, 1035 = e; 2 of 3 blind readers)',
        327: 'que (6 uses); also once where the text has "d" (d-envoyer): proposed 527 there (527 = d; 2 of 3 blind readers)'})
    # 108, 381 and 808 occur only at a proposal place: their value is unsure until the digit is settled
    for g in (108, 381, 808):
        UNSURE[g] = NOTE.pop(g)
PROP = {int(r['token_index']) for r in _rows} if BRACKX else set()   # the eight places where a change is proposed
by = collections.defaultdict(list)
for i, (g, draft, meaning, kind) in enumerate(tok):
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
    if BRACKX:   # class from the uses away from the eight proposal places (those places are marked in the reading)
        cnt = collections.Counter(v for i, v in occ if i not in PROP) or cnt
        n_film = sum(1 for i, _ in occ if i not in PROP)
        fam = all(common_prefix(min(cnt, key=len), v) >= max(1, len(min(cnt, key=len)) - 1) for v in cnt)
        main = sorted(cnt.items(), key=lambda kv: (-kv[1], len(kv[0]), kv[0]))[0][0]
    if g in UNSURE: cls = 'C'
    elif n_film < 2 and len(occ) >= 2 and len(cnt) == 1: cls = 'B' if n_film == 1 else 'C'
    elif len(occ) >= 2 and (len(cnt) == 1 or fam or g in FAMILY): cls = 'A'
    elif len(occ) >= 2: cls = 'C'
    elif g in JOINT: cls = 'B2'
    else: cls = 'B'
    note = UNSURE.get(g) or NOTE.get(g, '')
    rows.append([g, main, len(occ), len(occ) - n_film, cls, '; '.join('%s x%d' % kv for kv in vals) if len(vals) > 1 else '',
                 sum(1 for i, _ in occ if i < N_TRAIN), sum(1 for i, _ in occ if i >= N_TRAIN), note])
w = csv.writer(open(args[2], 'w'), delimiter='\t', lineterminator='\n')
w.writerow(['group', 'value', 'occurrences', 'at_proposal_places' if BRACKX else 'of_which_emended', 'class', 'all_values', 'in_first_568', 'in_last_85', 'note'])
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
