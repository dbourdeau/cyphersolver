"""Build the Rossi 1537 unit ledger, decryption files, d/t ledger and counts from the stamped inputs.
Own script (standard library). usage: python3 -I build.py <b56 dir> <b64 dir> <b68 dir> <out dir>
Inputs (all stamped 11 Nov 2026): pass-1 transcriptions, KEY_pass1.tsv, READING.txt (b56); shape_units.tsv (b64,
the non-blind shape verdicts); secret/map.tsv and blind_set_labels_Ponly.tsv (b68, the blind shape classes).
"""
import sys, re, collections, pathlib
B56, B64, B68, OUT = map(pathlib.Path, sys.argv[1:5])
PAGE = {'L': 'c31r', 'V': 'c31v', 'B': 'c33r'}

def tx(f):
    out = []
    for l in open(f, encoding='utf-8'):
        if l[0] == '#' or not l.strip(): continue
        lab, body = l.rstrip('\n').split(':', 1); t = body.split(); o = []; i = 0
        while i < len(t):
            if t[i] == 'I' and i + 1 < len(t) and t[i + 1] == ':': o.append('I:'); i += 2
            else: o.append(t[i]); i += 1
        out.append((lab, o))
    return out
LINES = tx(B56 / 'tx/rossiA_c31_pass1.txt') + tx(B56 / 'tx/rossiB_c33_pass1.txt')
KEY = {}
for l in open(B56 / 'work/KEY_pass1.tsv'):
    if l[0] == '#' or not l.strip(): continue
    a = l.rstrip('\n').split('\t'); KEY[a[0]] = a[1]
READ = {}
for l in open(B56 / 'work/READING.txt'):
    if l[0] == '#' or not l.strip(): continue
    lab, body = l.rstrip('\n').split(':', 1); READ[lab] = (re.findall(r'\(\w+\)|[a-z_\-]', body), body.strip())
SH = {}   # (line, pos without gaps) -> b64 verdict
for l in list(open(B64 / 'work/shape_units.tsv'))[1:]:
    lab, n, j, x, z, v = l.rstrip('\n').split('\t'); SH[lab, int(j)] = v
BL = {}
for l in list(open(B68 / 'blind_set_labels_Ponly.tsv'))[1:]:
    a = l.rstrip('\n').split('\t'); BL[a[0]] = (a[1].strip().upper(), a[2].strip(), a[3].strip() if len(a) > 3 else '')
BM = {}   # (line, pos) -> (id, class, conf, note)
for l in list(open(B68 / 'secret/map.tsv'))[1:]:
    a = l.rstrip('\n').split('\t'); BM[a[1], int(a[3])] = (a[0],) + BL[a[0]]
C2L = {'A': 'd', 'B': 't', 'C': 'l'}

rows = []; dec = collections.defaultdict(list)
for lab, toks in LINES:
    nog = [t for t in toks if t != '/']            # positions as in the b64/b68 ledgers (gaps dropped)
    r, rbody = READ[lab]; u = 0; j = -1
    kline = []; sline = []; bline = []
    for t in toks:
        if t == '/': kline.append(' '); sline.append(' '); bline.append(' '); continue
        j += 1
        if t[0] == '{' or t == 'x':                 # clear writing inside the cipher: not a cipher unit
            kline.append(t); sline.append(t); bline.append(t); continue
        if t == '#': k = KEY['hash_before8'] if j + 1 < len(nog) and nog[j + 1] == '8' else KEY['hash_else']
        else: k = KEY.get(t, '_')
        v = SH.get((lab, j), ''); firm = v in ('d', 't', 'l')
        s = v if firm else k                        # consensus, firm verdicts only
        s2 = v.rstrip('?') if v.rstrip('?') in ('d', 't', 'l') and v != '?' else k   # firm + leanings
        bm = BM.get((lab, j)); b = C2L.get(bm[1]) if bm else None; bl = b or k
        z = r[u]; u += 1
        cls = lambda L: 'N' if z in ('_', '-') else ('S' if L == z else 'E')
        rows.append([lab, PAGE[lab[0]], str(u), t, k, v, s, bm[0] if bm else '', bm[1] if bm else '', bm[2] if bm else '', bl, z, cls(k), cls(s), cls(s2), cls(bl)])
        kline.append(k); sline.append(s); bline.append(bl)
    assert u == len(r), (lab, u, len(r))
    dec[lab[0]].append((lab, toks, ''.join(kline), ''.join(sline), ''.join(bline), rbody))

hdr = ['line', 'page', 'unit', 'sign', 'key', 'shape_nonblind', 'letter_consensus', 'blind_id', 'blind_class', 'blind_conf', 'letter_blind', 'reading', 'class_key', 'class_consensus', 'class_consensus_lean', 'class_blind']
(OUT / 'units.tsv').write_text('# One row per cipher unit (2,368). sign = first-transcription code; key = letter by key.tsv with P printed t; shape_nonblind = the shape verdict of the second look (not blind; d t l, ? undecided, d?/t? leaning, empty = not a tall sign, not_sheeted = not looked at); letter_consensus = key with firm shape verdicts applied; blind_class = the blind shape test (A hook closed on stem = d, B open hat over tick = t, C bowl at foot = l, D unclear; blind for sign P only, C on sign D set from the code); letter_blind = key with blind classes applied; reading = the letter the reading takes (_ unread, - dropped, (tt) one sign for two letters). class: S same, E reading differs, N not read.\n' + '\t'.join(hdr) + '\n' + ''.join('\t'.join(r) + '\n' for r in rows), encoding='utf-8')

for g, name, head in (('LV', 'decryption_A.txt', 'Letter A, San Secondo 4 Nov 1537: c. 31r lines L01-L22, c. 31v lines V01-V14'), ('B', 'decryption_B.txt', 'Letter B, San Secondo 8 Nov 1537: c. 33r lines B01-B17')):
    o = ['# ' + head + '. Line by line against transcription_%s.txt.' % name[-5],
         '# T = first transcription (frozen before decoding; / = gap on the sheet). K = key.tsv applied sign by sign, with P printed t throughout.',
         '# S = the same with P and D recoded by the shape verdicts of the second look (not blind). R = the reading, aligned unit by unit',
         '# (word division added; _ unread; - sign dropped; (tt) one sign for two letters; clear roman numerals and the Latin word fuit left out of R).', '']
    for p in g:
        for lab, toks, k, s, b, r in dec[p]:
            o += [lab + ' T  ' + ' '.join(toks), lab + ' K  ' + k, lab + ' S  ' + s, lab + ' R  ' + r, '']
    (OUT / name).write_text('\n'.join(o), encoding='utf-8')

# d/t ledger: every tall sign (first-transcription P or D)
led = [r for r in rows if r[3] in ('P', 'D')]
(OUT / 'dt_ledger.tsv').write_text('# Every tall sign of the first transcription (codes P and D): 358. shape_nonblind = second look, reader knew the hypothesis; blind_class = blind shape test on crops under random ids (A = d, B = t, C = l, D = unclear); blind for sign P only: for sign D the class C was set from the transcription code, because the classifier put most D signs in class A (raw labels in timestamps/blind_shape_test/stamped/blind_set_labels.tsv). reading = the letter the reading takes. agree = blind class and non-blind verdict give the same letter (only where both gave one).\nline\tpage\tunit\tsign\tshape_nonblind\tblind_id\tblind_class\tblind_conf\treading\tagree\n' + ''.join('\t'.join([r[0], r[1], r[2], r[3], r[5], r[7], r[8], r[9], r[11], ('' if not (C2L.get(r[8]) and r[5].rstrip('?') in ('d', 't', 'l') and r[5] != '?') else 'yes' if C2L[r[8]] == r[5].rstrip('?') else 'no')]) + '\n' for r in led), encoding='utf-8')

# counts
out = []; P = out.append
def tab(col, title):
    P(title)
    tot = collections.Counter()
    for name, pre in (('A recto  (c. 31r, L01-L22)', 'L'), ('A verso  (c. 31v, V01-V14)', 'V'), ('B        (c. 33r, B01-B17)', 'B')):
        c = collections.Counter(r[col] for r in rows if r[0][0] == pre); n = sum(c.values()); tot += c
        P('  %s  S %4d + E %3d + N %2d = %4d   S/total = %d/%d = %.2f%%' % (name, c['S'], c['E'], c['N'], n, c['S'], n, 100 * c['S'] / n))
        if pre == 'V':
            a = collections.Counter(r[col] for r in rows if r[0][0] in 'LV'); n = sum(a.values())
            P('  A whole  (recto + verso)     S %4d + E %3d + N %2d = %4d   S/total = %d/%d = %.2f%%' % (a['S'], a['E'], a['N'], n, a['S'], n, 100 * a['S'] / n))
    n = sum(tot.values()); P('  Both letters                 S %4d + E %3d + N %2d = %4d   S/total = %d/%d = %.2f%%' % (tot['S'], tot['E'], tot['N'], n, tot['S'], n, 100 * tot['S'] / n)); P('')
P('Rossi 1537: counts by cipher unit. S = the letter given by the key equals the letter the reading takes; E = the reading takes another letter; N = unit not read.')
P('Units: %d (c. 31r %d, c. 31v %d, c. 33r %d). Clear tokens inside the cipher (roman numerals, fuit) are not units.' % (len(rows), sum(r[0][0] == 'L' for r in rows), sum(r[0][0] == 'V' for r in rows), sum(r[0][0] == 'B' for r in rows))); P('')
tab(12, '1. Key alone, P printed t (first transcription does not split d from t)')
tab(13, '2. Consensus: P and D recoded by the shape verdicts of the second look, firm verdicts only (NOT blind)')
tab(14, '3. Consensus with the leaning verdicts (d?, t?) as well (NOT blind)')
tab(15, '4. Blind: P recoded by the blind shape classes (reader saw only the crops); D stays l as the key has it')
# blind agreement on hat signs
x = collections.Counter((r[3], r[5].rstrip('?') if r[5] not in ('?', 'not_sheeted') else r[5], r[8]) for r in led)
P('5. Blind shape test against the non-blind verdicts, tall signs: %d (P %d, D %d)' % (len(led), sum(r[3] == 'P' for r in led), sum(r[3] == 'D' for r in led)))
for k in sorted(x): P('   sign %s, non-blind %-11s blind %s: %d' % (k[0], k[1] + ',', k[2], x[k]))
firm = [r for r in led if r[3] == 'P' and r[5] in ('d', 't') and r[8] in ('A', 'B')]
ag = sum(C2L[r[8]] == r[5] for r in firm)
dA = sum(r[5] == 'd' and r[8] == 'A' for r in firm); dB = sum(r[5] == 'd' and r[8] == 'B' for r in firm); tA = sum(r[5] == 't' and r[8] == 'A' for r in firm); tB = sum(r[5] == 't' and r[8] == 'B' for r in firm)
P('   Sign P with a firm non-blind d or t and a blind A or B: d&A %d + d&B %d + t&A %d + t&B %d = %d. Agree: %d + %d = %d of %d = %.1f%%.' % (dA, dB, tA, tB, len(firm), dA, tB, ag, len(firm), 100 * ag / len(firm)))
both = [r for r in led if C2L.get(r[8]) and r[5].rstrip('?') in ('d', 't', 'l') and r[5] != '?']
ag2 = sum(C2L[r[8]] == r[5].rstrip('?') for r in both)
firm2 = [r for r in led if r[3] == 'P' and r[5].rstrip('?') in ('d', 't') and r[5] != '?' and r[8] in ('A', 'B')]
ag3 = sum(C2L[r[8]] == r[5].rstrip('?') for r in firm2)
P('   The same with the leaning verdicts (d?, t?) counted: %d of %d = %.1f%%. (This is the 178/215 = 82.8%% of the issue; its words "firm d/t call" should have read "firm or leaning".)' % (ag3, len(firm2), 100 * ag3 / len(firm2)))
P('   All tall signs (P and D) where both gave d, t or l (leanings included): %d of %d = %.2f%%. NOT a blind figure: in the scored labels every sign D was set to class C by its transcription code (see blind_agreement.txt), so only the P rows are blind.' % (ag2, len(both), 100 * ag2 / len(both)))
# where the reading takes d or t from P
pd = [r for r in rows if r[3] == 'P' and r[11] in ('d', 't')]
P(''); P('6. Sign P where the reading takes d or t: %d (d %d, t %d).' % (len(pd), sum(r[11] == 'd' for r in pd), sum(r[11] == 't' for r in pd)))
for nm, col in (('non-blind firm verdict', 6), ('blind class', 10)):
    ok = sum(r[col] == r[11] for r in pd)
    P('   %s gives the reading\'s letter on %d of %d = %.1f%% (d: %d of %d; t: %d of %d).' % (nm, ok, len(pd), 100 * ok / len(pd), sum(r[col] == 'd' for r in pd if r[11] == 'd'), sum(r[11] == 'd' for r in pd), sum(r[col] == 't' for r in pd if r[11] == 't'), sum(r[11] == 't' for r in pd)))
e = collections.Counter((r[3], r[6], r[11]) for r in rows if r[13] == 'E')
P(''); P('7. The E units under the consensus (sign, consensus letter, reading letter): ' + ', '.join('%s %s>%s x%d' % (k + (v,)) for k, v in e.most_common()))
nn = collections.Counter(r[0] for r in rows if r[13] == 'N')
P('8. The N units by line: ' + ', '.join('%s %d' % kv for kv in sorted(nn.items())) + ' = %d' % sum(nn.values()))
(OUT / 'counts.txt').write_text('\n'.join(out) + '\n', encoding='utf-8'); print('\n'.join(out))
