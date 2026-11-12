"""build.py: makes key.tsv, aliases.tsv, overrides.tsv, units.tsv, decryption.txt, emendation rows and counts.txt
for targets/augustoni1612 from the files stamped on 11 Nov 2026 (timestamps/repair/stamped/) and the image review of
12 Nov 2026 (review.tsv), and checks transcription.txt against the stamped words. Standard library only.
usage: python3 scripts/build.py [target dir]      (default: the folder above this script)
"""
import sys, re, pathlib, collections
T = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
ST = T / 'timestamps' / 'repair' / 'stamped'
def tsv(p):
    L = [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return [dict(zip(L[0], r + [''] * (len(L[0]) - len(r)))) for r in L[1:]]
KEY = tsv(ST / 'KEY.tsv'); ALI = tsv(ST / 'ALIASES.tsv'); OVR = tsv(ST / 'OVERRIDES.tsv'); WORDS = tsv(ST / 'WORDS.tsv')
LED = tsv(ST / 'LEDGER_units.tsv'); REV = tsv(T / 'review.tsv')
CODES = {'I.', 'PP.', '25.'}
out = []
def P(s=''): out.append(s)
pct = lambda a, b: f'{a}/{b} = {100 * a / b:.2f}%'
# ---------------- check 1: transcription.txt braces == stamped consensus words
tx = {}
for l in open(T / 'transcription.txt', encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    name, body = l.split('|', 1); tx[name.strip()] = body.strip()
bywl = collections.defaultdict(list)
for w in WORDS:
    if w['consword'] != '-': bywl[w['line']].append(w['consword'])
bad = [(k, re.findall(r'\{([^}]*)\}', tx.get(k, '')), v) for k, v in bywl.items() if re.findall(r'\{([^}]*)\}', tx.get(k, '')) != v]
extra = [k for k in tx if k not in bywl and '{' in tx[k]]
P('== CHECK 1: cipher words in transcription.txt equal the stamped consensus words (WORDS.tsv), line by line')
P(f'   lines with cipher {len(bywl)}; cipher words {sum(len(v) for v in bywl.values())}; lines that differ {len(bad)}; cipher in an unknown line {len(extra)}  -> ' + ('PASS' if not bad and not extra else 'FAIL ' + str(bad[:3])))
# ---------------- units
units = [u for u in LED if u['label'] != '-']          # rows with label '-' are signs only the blind reader wrote (2)
spur = [u for u in LED if u['label'] == '-']
key = lambda u: (u['line'], u['widx'], u['tidx'])
rev = {(r['line'], r['widx'], r['tidx']): r for r in REV}
DAN_WORDS = {('L04', '1'): 'COSI', ('L14', '1'): 'CONSCESSO', ('L14', '2'): 'AV'}       # the reviewer's three words
REREAD = {('L16', '0'): 'INGANO', ('L17', '5'): 'SCR[I]TURA', ('L18', '0'): 'SCR[I]TURA', ('L19', '0'): 'ASTUTIA'}
ALIAS8 = [u for u in units if u['label'] == 'υ']
def tally(rows, f, name, show=True):
    c = collections.Counter(f(u) for u in rows); s, e, n = c['S'], c['E'], c['N']; t = s + e + n
    if show: P(f'   {name}: S {s} + E {e} + N {n} = {t}; strict S/T = {pct(s, t)}; S+E = {pct(s + e, t)}')
    return s, e, n, t
cip = [u for u in units if u['cat'] == 'CIPHER']; clr = [u for u in units if u['cat'] == 'CLEAR']
b587 = cip + clr
def dan(u):      # the reviewer's rule: the issue's conservative rule, and COSI, CONSCESSO, AV wholly emended
    if u['st_c'] == 'N': return 'N'
    return 'E' if (u['line'], u['widx']) in DAN_WORDS else u['st_c']
def dan_floor(u):
    return 'E' if (dan(u) == 'S' and u['label'] == 'υ') else dan(u)
P(); P('== TALLIES ON THE LEDGER AS STAMPED 11 NOV 2026 (S = key and label aliases give the letter read; E = emended or supplied; N = unread)')
P(f'   unit classes: cipher signs {len(cip)} (of which "?" placeholders {sum(u["label"] == "?" for u in cip)}), clear-script letters inside cipher words {len(clr)}, abbreviation sign & {sum(u["cat"] == "ABBR" for u in units)}, codes {sum(u["cat"] == "CODE" for u in units)}; all {len(units)}')
A = tally(cip, lambda u: u['st'], 'A. issue, unit rule, cipher signs only            ')
B = tally(cip, lambda u: u['st_c'], 'B. issue, "conservative", cipher signs only (94.0%)')
C = tally(b587, dan, 'C. reviewer\'s rule on his 587 units, our count     ')
P('   D. reviewer\'s own count                            : S 537 + E 35 + N 15 = 587; ' + pct(537, 587))
F = tally(b587, dan_floor, 'E. as C, the 8 rounded-u alias units also emended  ')
P(); P('== RECONCILIATION B -> C -> D, unit by unit')
P(f'   denominator: {B[3]} cipher units + {len(clr)} clear-script letters inside cipher words (L04 6osp: o, s; L14 4v: 4, v) = {B[3] + len(clr)}  [reviewer: 584 signs + 3 "?" = 587; ours: {len(cip) - 3} + {len(clr)} = {len(cip) - 3 + len(clr)} signs, + 3 "?"]')
moved = [u for u in cip if u['st_c'] == 'S' and dan(u) == 'E']
bw = collections.Counter(DAN_WORDS[(u['line'], u['widx'])] for u in moved)
P(f'   S: {B[0]} - {len(moved)} units of the three words that were still counted S ({", ".join(f"{k} {v}" for k, v in bw.items())}) = {B[0] - len(moved)}')
P(f'   E: {B[1]} + {len(moved)} (those units) + {len(clr)} (the clear-script letters, not in the 583 at all) = {B[1] + len(moved) + len(clr)}')
P(f'   N: {B[2]} (L10 1, L16 5, L17-18 7, L19 2), unchanged')
P(f'   ours C = {C[0]} + {C[1]} + {C[2]} = {C[3]}; reviewer D = 537 + 35 + 15 = 587. Difference: 1 unit, S {C[0]} against 537.')
P('   Probable source of the 1 unit [derived, not confirmed by the reviewer]: CONSCESSO has 9 units, of which the blot sign')
P('   (L14 word 1 sign 6) was already one of the 20 emended units of B. Taking all 9 off the 548 gives 548 - 2 - 9 = 537;')
P('   taking the 8 that were still S gives 538. We adopt the reviewer\'s 537/587 = 91.5% as the stated figure; our own count is 538/587 = 91.65%.')
# blind transcription under the same rule
r2 = [u for u in LED if u['cat'] in ('CIPHER', 'CLEAR') and u['r2st_c'] != 'OMIT']
def r2dan(u):
    if u['r2st_c'] == 'N': return 'N'
    return 'E' if (u['line'], u['widx']) in DAN_WORDS else u['r2st_c']
P(); P('== BLIND SECOND TRANSCRIPTION (transcription_blind.txt), same ledger')
tally([u for u in LED if u['cat'] == 'CIPHER' and u['r2st_c'] != 'OMIT'], lambda u: u['r2st_c'], 'G. issue, "conservative", cipher signs only (90.2%)')
G = tally(r2, r2dan, 'H. reviewer\'s rule, clear-script letters included  ')
P(f'   (the blind reader wrote 2 signs that are not on the sheet, counted N, and left out 2, not in the total; with those 2 as unread the base is {G[3] + 2}: {pct(G[0], G[3] + 2)})')
# ---------------- after the image review of 12 Nov
P(); P('== AFTER THE IMAGE REVIEW OF 12 NOV 2026 (review.tsv). Not blind: every change was made with the proposed word known.')
v2 = []
for u in b587:
    r = rev.get(key(u)); d = dict(u); d['label_v2'] = r['label_v2'] if r else u['label']; d['st_v2'] = r['st_v2'] if r else u['st']
    d['val_v2'] = r['value_v2'] if r else u['val']; d['rev'] = r['note'] if r else ''; v2.append(d)
new = [r for r in REV if r['tidx'] == '-1']
for r in new: v2.append({'line': r['line'], 'widx': r['widx'], 'tidx': '-1', 'cat': 'CIPHER', 'label': '', 'lit': '', 'val': '', 'acc': '', 'ins': '', 'st': '', 'st_c': '', 'why': 'not in the stamped ledger', 'label_v2': r['label_v2'], 'val_v2': r['value_v2'], 'st_v2': r['st_v2'], 'rev': r['note'], 'r2lab': '', 'r2lit': '', 'r2st': '', 'r2st_c': '', 'r2why': ''})
def v2cons(d):
    if d['st_v2'] == 'N': return 'N'
    if (d['line'], d['widx']) in DAN_WORDS or (d['line'], d['widx']) in REREAD or d.get('ins'): return 'E'
    return d['st_v2']
I = tally(v2, lambda d: d['st_v2'], 'I. unit rule (only the changed or supplied unit is E)       ')
J = tally(v2, v2cons, 'J. whole-word rule (every word with any emendation wholly E)')
P(f'   base: 587 + {len(new)} sign added on L16 = {I[3]}. Unread after review: {I[2]} unit (L10, the sign in the gutter).')
ch = collections.Counter((d['st'] or 'new', d['st_v2']) for d in v2 if d['rev'])
P('   units changed by the review (stamped status -> status now): ' + ', '.join(f'{a}->{b} {n}' for (a, b), n in sorted(ch.items())))
P('   J is lower than C although more is read: three more words (INGANO, SCR[I]TURA, ASTUTIA) are now read with an emendation, and J counts')
P('   every unit of such a word as emended (ASTUTIA had 4 units counted S). No unit entered S on the strength of a relabelled sign.')
# ---------------- words
wv = collections.defaultdict(list)
for d in v2: wv[(d['line'], d['widx'])].append(d)
ACC0 = {('L16', '0'): 'ul4oc (unread)', ('L17', '5'): 'n6y (unread)', ('L18', '0'): 'gq74 (unread)'}
P(); P('== CIPHER WORDS (codes and the & sign apart)')
words = [w for w in WORDS if w['consword'] not in CODES and w['consword'] not in ('&', '-')]
wu = collections.defaultdict(list)
for u in b587: wu[(u['line'], u['widx'])].append(u)
for k in wu: wu[k].sort(key=lambda u: int(u['tidx']))
lit = sum(1 for w in words if all(u['st'] == 'S' for u in wu[(w['line'], w['widx'])]) and not re.search(r'[{]', w['accepted']))
P(f'   word rows written in cipher signs: {len(words)} (SCR-TURA, split over L17-L18, is two rows). The reviewer has 99 cipher words, 83 literal.')
torn = sum(1 for w in words if '<' in w['accepted'])
P(f'   rows whose every unit is S and that need no supplied letter, ledger as stamped: {lit} of {len(words)} = {100 * lit / len(words):.1f}%')
P(f'   of those, rows that end at the torn edge and are completed in the reading (PREVOST<O>, PREVOS<TO>): {torn}; without them {lit - torn} of {len(words)} = {100 * (lit - torn) / len(words):.1f}%, the reviewer\'s 83')
P(f'   not literal: {len(words) - lit} rows = ' + ', '.join(w['line'] + ' ' + ACC0.get((w['line'], w['widx']), w['accepted']) for w in words if not (all(u['st'] == 'S' for u in wu[(w['line'], w['widx'])]) and not re.search(r'[{]', w['accepted']))))
P('   after the review the same 14 rows are not literal: the three re-read words are read, each with an emendation.')
# ---------------- key values that do not come from the key table
P(); P('== WHAT RESTS ON THE KEY TABLE, WHAT ON ALIASES, WHAT ON OVERRIDES (ledger as stamped, 600 units)')
kc = collections.Counter(u['label'] for u in cip if u['st'] == 'S')
ren = sum(kc[x] for x in ('R', 'D')); al8 = kc['υ']
P(f'   S units {A[0]}: by a key sign under its own label {A[0] - ren - al8}; by a renamed label of the same sign (R = K, D = z) {ren}; by the rounded-u split (υ = the n sign o) {al8}')
P(f'   coordinate overrides {len(OVR)}: ' + ', '.join(f'{k} {v}' for k, v in sorted(collections.Counter(o["category"] + " " + o["status"] for o in OVR).items())))
P('   no key value at all: the & sign (6 units), the codes I. x5, PP., 25. (7 units), the Z form (1 unit, q from context)')
# ---------------- files
ACC2 = {('L14', '1'): 'conscenso', ('L16', '0'): 'ingano', ('L17', '5'): 'scr', ('L18', '0'): '{i}tura', ('L19', '0'): 'astutia', ('L10', '0'): '?e'}
with open(T / 'units.tsv', 'w', encoding='utf-8') as f:
    f.write('# One row per unit. Columns line..r2why are the ledger stamped on 11 Nov 2026 (timestamps/repair/stamped/LEDGER_units.tsv), unchanged.\n')
    f.write('# st = unit rule; st_c = the issue\'s "conservative" rule; st_rev = the reviewer\'s rule (COSI, CONSCESSO, AV wholly E). label_v2, val_v2, st_v2, st_v2_word, review = state after the image review of 12 Nov 2026 (review.tsv); st_v2_word counts every unit of an emended word E.\n')
    f.write('# cat: CIPHER a cipher sign; CLEAR a clear-script letter inside a cipher word; ABBR the & sign; CODE I. PP. 25. Row tidx -1 = the sign added on L16. Rows with label "-" = signs only the blind reader wrote.\n')
    cols = ['line', 'widx', 'tidx', 'cat', 'label', 'lit', 'val', 'acc', 'ins', 'st', 'st_c', 'why', 'r2lab', 'r2lit', 'r2st', 'r2st_c', 'r2why']
    f.write('\t'.join(cols + ['st_rev', 'label_v2', 'val_v2', 'st_v2', 'st_v2_word', 'review']) + '\n')
    v2k = {key(d): d for d in v2}
    order = []
    for u in LED:
        if u['line'] == 'L16' and u['widx'] == '0' and u['tidx'] == '0': order.append(v2k[('L16', '0', '-1')])
        order.append(u)
    for u in order:
        d = v2k.get(key(u)) if u.get('label') != '-' else None
        if u.get('tidx') == '-1': d = u
        extra = [dan(u) if (d and u['cat'] in ('CIPHER', 'CLEAR') and u['tidx'] != '-1') else '', d['label_v2'] if d else '', d['val_v2'] if d else '', d['st_v2'] if d else '', v2cons(d) if d else '', d['rev'] if d else '']
        if u['cat'] in ('ABBR', 'CODE'): extra = ['', u['label'], u['val'], u['st'], u['st'], '']
        f.write('\t'.join([u.get(c, '') for c in cols] + extra) + '\n')
keyc = collections.Counter(); 
for u in cip:
    lab = {'R': 'K', 'D': 'z', 'υ': 'o*'}.get(u['label'], u['label']); keyc[lab] += 1
NOTE = {'4': 'open bowl, short descender, bar to the right', 'a': 'closed a-form. Three times a; twice it stands where f is needed (L21, L24: overrides)', 'i': 'dotted i-form', '6': 'tall ascender with a closed bowl', 'b': 'b-form; in the frozen key from the first pass, no instance in the consensus transcription', 't': 't-form', '3': '3-form with a kink', 'z': 'tailed e: one smooth reversed c with a tail (label D in the transcription)', 'u': 'plain u: two angular minims', 'l': 'tall curved ascender', 'L': 'capital L-form, word-initial', 'h': 'h-form', 'p': 'p-form with a long stem', 'm': 'm-form', 'f': 'f-form', 'o': 'small closed circle; the rounded u-form (label υ) is read as the same letter: see aliases.tsv', 'c': 'c-form', 'v': 'pointed v-form with a flourish', 'K': 'capital K-like p-form (label R in the transcription)', 'H': 'capital H-form', '7': 'bar and diagonal', 'n': 'n-form', 'g': 'bowl with a looped descender', 'y': 'open fork with a descender', 'q': 'closed round bowl, long straight descender'}
with open(T / 'key.tsv', 'w', encoding='utf-8') as f:
    f.write('# sign\tplain\tcount\tnote. Augustoni, 9 Oct 1612. Signs are named by the labels of the consensus transcription (ours, by look). Values as frozen 11 Nov 2026 (timestamps/first/stamped/KEY_aug1612.tsv = timestamps/repair/stamped/KEY.tsv).\n')
    f.write('# Simple substitution, letter-like signs: 25 signs for 19 letters; homophones a 2, c 2, e 2, g 2, p 3, u 2; u and v are one letter; no q, z or x sign in the table. Count = cipher units carrying the label in the stamped ledger (583 cipher units, 3 of them "?").\n')
    f.write('# Not in this table, on purpose: label aliases (aliases.tsv) and the 13 coordinate overrides (overrides.tsv). The & sign and the codes I., PP., 25. (and .50. in the clear text) have no key value.\n')
    for k in KEY:
        s = k['sign']; n = keyc[s] + (keyc['o*'] if s == 'o' else 0)
        f.write(f"{s}\t{k['plain']}\t{n}\t{NOTE[s]}" + (f" ({keyc['o']} as o, {keyc['o*']} as υ)" if s == 'o' else '') + '\n')
    f.write(f"Z\t(q)\t{keyc['Z']}\tNOT A KEY VALUE. One instance (L12). 7-form with a foot to the right; q from the word quassi. Override, see overrides.tsv\n")
    f.write(f"&\t(per)\t6\tNOT A KEY VALUE. Abbreviation compound, one unit. per from context at L03 L08 L09 L22; not read at L13 L16\n")
crop = lambda s: ';'.join(x.split('/')[-1] for x in s.split(';'))
with open(T / 'aliases.tsv', 'w', encoding='utf-8') as f:
    f.write('# Label aliases, as stamped 11 Nov 2026 (timestamps/repair/stamped/ALIASES.tsv; crop names only, the crops are not in the repository). An alias says that a label in one transcription is the same written sign as a key label.\n')
    f.write('# kind: rename = the same sign under another name, no reading decision. split = ONE label of the blind transcription divided in two AFTER decoding (a reading decision; see NOTES.md).\n')
    f.write('transcript\tlabel\tkey_label\tkind\tunits\tscope\tvisual_basis\tcrop\n')
    for a in ALI:
        kind = 'split, made after decoding' if a['label'] == 'υ' else ('no alias: decodes literally' if a['label'] == 'u' else ('namespace fix, no key value' if a['key_label'] == 'Z' else 'rename'))
        lab = 'r2lab' if a['transcript'] == 'R2' else 'label'
        n = sum(1 for u in LED if u.get(lab) == a['label'] and u['cat'] == 'CIPHER')
        f.write('\t'.join([a['transcript'], a['label'], a['key_label'], kind, str(n), a['scope'], a['visual_basis'], crop(a['crop'])]) + '\n')
with open(T / 'overrides.tsv', 'w', encoding='utf-8') as f:
    f.write('# All 13 coordinate overrides, as stamped 11 Nov 2026 (timestamps/repair/stamped/OVERRIDES.tsv), with the word and the state after the review of 12 Nov 2026. widx, tidx count from 0 within the line and the word. Every override is scored E or N, never S.\n')
    f.write('line\twidx\ttidx\tword\tlabel\tkey_output\tvalue\tstatus\tcategory\treason\tcrop\tafter_review_12_Nov\n')
    wd = {(w['line'], w['widx']): w for w in WORDS}; led = {key(u): u for u in LED}
    for o in OVR:
        k = (o['line'], o['widx'], o['tidx']); r = rev.get(k)
        f.write('\t'.join([o['line'], o['widx'], o['tidx'], wd[k[:2]]['consword'], o['label'], led[k]['lit'] or '(none)', o['value'], o['status'], o['category'], o['reason'], crop(o['crop']), (f"value {r['value_v2']}, status {r['st_v2']}: {r['note']}" if r else 'unchanged')]) + '\n')
# decryption
lit_of = lambda d: (d['lit'] or '?').upper()
with open(T / 'decryption.txt', 'w', encoding='utf-8') as f:
    f.write('# Decryption, line by line against transcription.txt. For each line with cipher:\n#   T  the line as transcribed (cipher in braces)\n#   K  each cipher word under the key and the label aliases alone, no overrides (? = no key value; & and the codes pass through)\n#   R  the reading adopted after the review of 12 Nov 2026: {x} a letter supplied, <x> lost at the torn edge, ? no value, (x) a value from an override or an emendation, & the abbreviation sign where it is not read (L13, L16; elsewhere PER, from context). CAPITALS = from cipher; lower case = clear text.\n#   Lines without cipher (C30-C41) are given once.\n')
    wl = collections.defaultdict(list)
    for w in WORDS:
        if w['consword'] != '-': wl[w['line']].append(w)
    for name, body in tx.items():
        if name not in wl: f.write(f'{name} T  {body}\n\n'); continue
        ws = iter(wl[name]); kline = body; rline = body
        def K(m):
            w = next(ws); kk = (w['line'], w['widx'])
            if w['consword'] in CODES or w['consword'] == '&': K.r.append(('PER' if w['accepted'] == 'per' else '&') if w['consword'] == '&' else w['consword']); return w['consword']
            us = wu[kk]; K.r.append(None)
            acc = ACC2.get(kk, w['accepted']); ds = sorted(wv[kk], key=lambda d: int(d['tidx']))
            bare = re.sub(r'<[^>]*>|\{[^}]*\}', '', acc); o = []
            for d, ch in zip(ds, bare):
                o.append(ch.upper() if d['st_v2'] == 'S' else ('?' if d['st_v2'] == 'N' else '(' + ch.upper() + ')'))
            s = ''.join(o)
            m2 = re.search(r'\{[^}]*\}', acc)
            if m2:
                pos = len(re.sub(r'<[^>]*>', '', acc[:m2.start()])); cut = sum(len(x) for x in o[:pos]); s = s[:cut] + m2.group(0).upper() + s[cut:]
            m3 = re.search(r'<[^>]*>$', acc)
            if m3: s += m3.group(0).upper()
            K.r[-1] = s
            return ''.join(lit_of(u) for u in us)
        K.r = []
        kline = re.sub(r'\{[^}]*\}', K, body); it = iter(K.r)
        rline = re.sub(r'\{[^}]*\}', lambda m: next(it), body)
        f.write(f'{name} T  {body}\n{name} K  {kline}\n{name} R  {rline}\n\n')
(T / 'counts.txt').write_text('# counts.txt: made by scripts/build.py from timestamps/repair/stamped/ and review.tsv. Every figure is a full count over units.tsv, shown with its parts.\n' + '\n'.join(out) + '\n', encoding='utf-8')
print('\n'.join(out))
