"""pagni444: rebuild the unit ledger, the final transcription, the decryption, the override list, the
dropped-sign tally, the key table and the arithmetic from the stamped work files and the adjudication list.
Standard library only. Run from the target folder:  python3 scripts/build.py
Reads : timestamps/stamped/LEDGER_444.tsv   per-unit ledger of pass 3 (1,521 units), stamped 11 Nov 2026
        timestamps/stamped/KEY_pass3.tsv     the key, stamped
        timestamps/stamped/still_EN.tsv      every unit not read after adjudication, stamped (cross-check)
        timestamps/stamped/reading_adjudicated.txt  the per-line reading after adjudication, stamped (cross-check)
        timestamps/stamped/R3.txt            the blind third transcription, stamped
        adjudication.tsv                     the 138 disputed units with what the image shows (not stamped)
Writes: units.tsv transcription.txt decryption.txt overrides.tsv dropped_signs.tsv key.tsv counts.txt
"""
import collections, difflib, re, pathlib
T = pathlib.Path(__file__).resolve().parent.parent
S = T / 'timestamps' / 'stamped'
def rows(p, skip=('#',)):
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith(skip)]
# ---- key
key = {}
for f in rows(S / 'KEY_pass3.tsv'):
    for sg in f[0].split(): key[sg] = f[1].strip()
def kv(s):
    """literal key value of a sign label: letter, (che)/(in)/(per), ~ repeat, ° null, {X} code, ? none"""
    v = key.get(s)
    if s == '0' or v is None: return '?'
    if v.upper().startswith('NULL'): return '°'
    if v == 'repeat previous letter': return '~'
    if v in ('che', 'in', 'per'): return '(' + v + ')'
    if s in 'ALSGBDQmnd&' : return '{' + s + '}'
    return v
CODES = set('ALSGBDQmnd&')
# ---- ledger and adjudication
LED = [f for f in rows(S / 'LEDGER_444.tsv') if f[0] != 'line']
ADJ = {(r[1], int(r[2])): r for r in rows(T / 'adjudication.tsv') if r[0] != 'n'}
assert len(LED) == 1521 and len(ADJ) == 138
TWIN_DROP = {('R02', 19)}            # the twin of R02 u18: one 5 on the image where pass 3 had two
NEWVAL = {('R13', 16): 'p', ('V04', 18): 't'}   # sabere -> sapere, poser -> poter (image)
units = []; dropped = []
for f in LED:
    ln, u = f[0], int(f[1]); k = (ln, u); a = ADJ.get(k)
    b43 = f[5]; old = f[10]; acc = f[13]
    if (a and a[11] == 'DROP') or k in TWIN_DROP:
        dropped.append((ln, u, b43, f[8], old)); continue
    if a:
        cands = a[8].split('|'); new = a[11]; verdict = a[6] + ' ' + a[7]; obs = a[5]
        sign = b43 if b43 in cands else cands[0]
        if cands == ['?']: sign = b43
        if cands == ['(none)']: sign = b43; cands = [b43]      # R02 u18: the one 5 on the image, kept
    else:
        cands = [b43]; new = old; verdict = ''; obs = ''; sign = b43
    if k in NEWVAL: acc = NEWVAL[k]
    lit = kv(sign)
    # kind of unit by the accepted reading
    if b43 in CODES and 'CODE' in f[8]: kind = 'code'
    elif new == 'N': kind = 'unread'
    elif f[7] == 'REPEAT' or (lit == '~' and acc != ''): kind = 'repeat'   # R21 u1 repeats the l that ends R20 (quel|la)
    elif acc == '': kind = 'null'
    elif acc in ('che', 'in', 'per'): kind = 'word sign'
    else: kind = 'letter'
    # sub-class of the units not read
    if new == 'S': sub = ''
    elif new == 'N': sub = 'unread'
    elif kind == 'code': sub = 'code value from context'
    else:
        vals = [kv(c).strip('()') for c in cands]
        want = '°' if acc == '' else acc.lower()
        hit = [v == want or ('/' in v and want in v.split('/')) for v in vals]
        if kind == 'null': sub = 'null by context: the sign has a letter value in the key' if not any(hit) else 'null, but the image allows a second sign that is a letter'
        else: sub = 'letter by context: the key gives another value' if not any(hit) else 'letter, but the image allows a second sign with another value'
    units.append(dict(line=ln, unit0=u, word=int(f[3]), pass3=b43, sign=sign, cands='|'.join(cands), key=lit,
                      accepted=acc, kind=kind, cls=new, old=old, b43class=f[8], sub=sub, verdict=verdict, obs=obs))
# renumber within the line after the drops
n = collections.Counter()
for x in units: n[x['line']] += 1; x['unit'] = n[x['line']]
N = len(units)
C = collections.Counter(x['cls'] for x in units)
assert N == 1514 and (C['S'], C['E'], C['N']) == (1369, 137, 8), (N, C)
# cross-check with the stamped list of units not read
EN = {(r[0], int(r[1])) for r in rows(S / 'still_EN.tsv') if r[0] != 'line'}
assert EN == {(x['line'], x['unit0']) for x in units if x['cls'] != 'S'}, 'E/N set differs from stamped still_EN.tsv'
lines = list(collections.OrderedDict.fromkeys(x['line'] for x in units))
by = {l: [x for x in units if x['line'] == l] for l in lines}
# ---- units.tsv
with open(T / 'units.tsv', 'w', encoding='utf-8') as o:
    o.write('line\tunit\tunit_pass3\tword\tsign_pass3\tsign\timage_allows\tkey_value\taccepted\tkind\tclass\tclass_pass3\twhy_not_read\tadjudication\n')
    for x in units:
        o.write('\t'.join(str(x[c]) for c in ('line', 'unit', 'unit0', 'word', 'pass3', 'sign', 'cands', 'key', 'accepted', 'kind', 'cls', 'old', 'sub', 'verdict')) + '\n')
# ---- transcription.txt and decryption.txt
def show(x):
    a = x['accepted']
    if x['kind'] == 'code': return '{' + x['sign'] + '}'
    if x['cls'] == 'N': return '<' + x['sign'] + '?>'
    if x['kind'] == 'null': return '°' if x['cls'] == 'S' else '[' + x['key'].strip('()') + ']'
    if x['kind'] == 'repeat': return '~' if x['cls'] == 'S' else a.upper()
    if x['kind'] == 'word sign': return '(' + a + ')' if x['cls'] == 'S' else '(' + a.upper() + ')'
    return a if x['cls'] == 'S' else a.upper()
def dec_line(l):
    s = ''; w = None
    for x in by[l]:
        t = show(x)
        if w is not None and x['word'] != w and not s.endswith(' '): s += ' '
        s += t; w = x['word']
    return ' '.join(s.split())
READ = {l[:3]: l[3:].split('[b43:')[0].strip() for l in open(S / 'reading_adjudicated.txt', encoding='utf-8') if l[:1] in 'RV'}
HEAD_T = """# ASF, Mediceo del Principato 444, c. 315r-v: final transcription (pass 3 after adjudication against the blind third transcription)
# One row per manuscript line of cipher. R01-R26 recto, V01-V10 verso, as in issue 426. R01 is the second written line of the
# recto: the first line and the start of the second are in clear (given below). 1,514 units.
# Sign labels: digits 1-9 and x as written; ' one dot above; " two dots above (side by side or stacked); 2. a 2 with a dot or colon
# beside it; J the hooked form of 3; b the repeat sign; u a l the three word signs; N the pi-like sign; # the barred sign; 0 a round sign
# (once); capitals and d Q m n & the code signs. A sign followed by ? is one where the image allows a second label (units.tsv, column
# image_allows). The cipher is written without spaces; the spaces here only separate signs.
# Differs from the lines printed in issue 426 at 19 units, where the adjudication found another sign on the image (issue sign > sign here):
# R01 u2 5>5'; R03 u20 5>5'; R04 u18 3'>3"; R04 u25 5'>5"; R05 u1 3'>3"; R05 u26 1'>1"; R05 u37 3>3'; R09 u38 3'>3"; R10 u44 6>6'; R11 u20 1">7"; R11 u26 6>6'; R13 u8 6>6'; R15 u34 5>5'; R16 u12 1'>1"; R22 u22 1'>7"; V02 u25 3>9; V02 u37 1'>1"; V07 u24 3'>B'; V10 u11 5'>5".

[clear, line 1]  scrissi laltro hierj a v.s. raguagliandolo di quel ch(e) passava por
[clear, line 2]  acca. co(n) esta intendra(?) como   [then the cipher of R01 on the same line]
"""
with open(T / 'transcription.txt', 'w', encoding='utf-8') as o:
    o.write(HEAD_T)
    for l in lines:
        o.write(l + ' ' + ' '.join(x['sign'] + ('?' if '|' in x['cands'] else '') for x in by[l]) + '\n')
    o.write('\n[clear, verso, below V10]  el dj xx. m   [a bar over "xx. m"; no further letters in the writing ink; no year, place or signature]\n')
HEAD_D = """# ASF, Mediceo del Principato 444, c. 315r-v: decryption, line by line against transcription.txt
# For each line: the signs, the key value of every unit, then the line as read (words divided by us).
# lower case = the key gives this letter from the sign on the image (class S)   ~ = repeat sign   (che) (in) (per) = word signs
# ° = a sign the key lists as a null (S)      [x] = a sign with key value x that the reading drops as a null (E)
# CAPITAL = letter by context: the key gives another value, or the image leaves two signs open (E)
# [°] = a null sign by one reading of the image, a letter sign by the other (E)
# {X} = code sign, value not fixed (E)        <X?> = unread (N)
# A ~ at the start of R21 repeats the l that ends R20 (quel|la).
"""
with open(T / 'decryption.txt', 'w', encoding='utf-8') as o:
    o.write(HEAD_D)
    for l in lines:
        o.write('\n' + l + '  ' + ' '.join(x['sign'] for x in by[l]) + '\n')
        o.write('  key   ' + dec_line(l) + '\n')
        o.write('  read  ' + READ[l] + '\n')
# the read line must be the decryption with nulls and brackets removed
def strip(s): return re.sub(r'\s+', '', re.sub(r'\[[^\]]*\]|°', '', s).replace('(', '').replace(')', '').replace('~', '')).lower()
for l in lines:
    d = dec_line(l); r = READ[l]
    # expand the repeat sign before comparing
    e = '';
    for ch in re.sub(r'\[[^\]]*\]|°', '', d):
        e += (e[-1] if ch == '~' and e else ch)
    a = re.sub(r'[\s()]', '', e).lower().lstrip('~'); b = re.sub(r'\s', '', r).lower()
    a = re.sub(r'<[^>]*>', '<?>', a); b = re.sub(r'<[^>]*>', '<?>', b)
    assert a == b, (l, a, b)
# ---- overrides.tsv: every unit that is not read
with open(T / 'overrides.tsv', 'w', encoding='utf-8') as o:
    o.write('line\tunit\tsign\timage_allows\tkey_value\tadopted\tclass\twhat\tin_word\n')
    for x in units:
        if x['cls'] != 'S':
            wd = ''.join(y['accepted'] for y in by[x['line']] if y['word'] == x['word']) or '(between words)'
            o.write('\t'.join(str(v) for v in (x['line'], x['unit'], x['sign'], x['cands'], x['key'], x['accepted'] or '(null)', x['cls'], x['sub'], wd)) + '\n')
# ---- dropped_signs.tsv: signs dropped as nulls, by label
tab = collections.defaultdict(collections.Counter)
for x in units:
    if x['kind'] == 'code' or x['cls'] == 'N': continue
    lab = x['pass3']
    if x['kind'] == 'null': tab[lab]['null S' if x['b43class'] == 'NULL-KEY' else 'null ctx'] += 1
    else: tab[lab]['read S' if x['old'] == 'S' else 'read E'] += 1
with open(T / 'dropped_signs.tsv', 'w', encoding='utf-8') as o:
    o.write('# by the sign label of pass 3 (the transcription of issue 426), classes of pass 3 before adjudication, 1,514 units\n')
    o.write('sign\tkey_value\tread_by_key\tread_by_context\tnull_by_key\tdropped_as_null_by_context\n')
    for lab in sorted(tab, key=lambda s: (-tab[s]['null ctx'], s)):
        t = tab[lab]; o.write('%s\t%s\t%d\t%d\t%d\t%d\n' % (lab, kv(lab), t['read S'], t['read E'], t['null S'], t['null ctx']))
ctx_total = sum(t['null ctx'] for t in tab.values())
# after adjudication: what the 69 are
after = collections.Counter()
for x in units:
    if x['b43class'] == 'NULL-CTX':
        after['S: the image shows a two-dot null sign' if x['cls'] == 'S' else ('E: image allows a null sign and a letter sign' if 'second' in x['sub'] else 'E: a letter sign on the image, dropped by sense')] += 1
# ---- key.tsv
use = collections.defaultdict(collections.Counter)
for x in units: use[x['sign']][x['cls']] += 1
NOTE = {"2'": 'dot above the 2: 7 of 7 are nulls', '4': 'also stands where h is read (7 units, by context)', "4'": 'expected h; seen once and dropped as a null',
        '6': 'plain 6', "6'": '6 with a separate dot', '9"': 't in some places, dropped in others', 'x"': 'two dots; z by position in the pairs, see NOTES',
        'J': 'hooked form of the 3', 'b': 'repeats the letter before it', 'u': 'word sign', 'a': 'word sign', 'l': 'word sign; also at three clause breaks where it is not read',
        '0': 'once, R07; not in the key of issue 426; dropped as a null by context', '&': 'value open', 'A': 'value from context only', 'L': 'value from context; five uses agree',
        'S': 'value from context only', 'G': 'value from context only', 'B': 'value from context only', 'D': 'value open', 'Q': 'value open', 'm': 'value open', 'n': 'value open', 'd': 'value open',
        "B'": 'V07, once: a heavy B-like sign where f is read by context (franzesi)', 'u"': 'R22, once: unread (temp?)'}
VAL = {'A': '[?Papa]', 'L': '[?Duca]', 'S': '[?Siena]', 'G': '[?Cardinale]', 'B': '[?Imperatore]', '&': '[?et]', 'D': '?', 'Q': '?', 'm': '?', 'n': '?', 'd': '?', '0': '?'}
order = ['1', "1'", '2', '2.', '3', 'J', "3'", '4', "4'", '5', "5'", '6', "6'", '7', "7'", '8', "8'", '9', "9'", '9"', 'x', "x'", 'x"', 'b', 'u', 'a', 'l',
         "2'", '1"', '2"', '3"', '4"', '5"', '6"', '7"', '8"', 'J"', 'N', '#', '0', 'A', 'L', 'S', 'G', 'B', '&', 'D', 'Q', 'm', 'n', 'd']
extra = [s for s in use if s not in order]
with open(T / 'key.tsv', 'w', encoding='utf-8') as o:
    o.write('sign\tvalue\tkind\tunits\tread_S\tnot_read_E\tunread_N\tnote\n')
    for s in order + sorted(extra):
        v = VAL.get(s) or {'°': 'null', '~': 'repeat'}.get(kv(s), kv(s).strip('()'))
        kind = 'code' if s in CODES else 'null' if v == 'null' else 'repeat sign' if v == 'repeat' else 'word sign' if s in 'ual' else 'not in the key' if s in extra or s == '0' else 'letter'
        c = use[s]; o.write('%s\t%s\t%s\t%d\t%d\t%d\t%d\t%s\n' % (s, v, kind, sum(c.values()), c['S'], c['E'], c['N'], NOTE.get(s, '')))
# ---- blind third transcription against pass 3 (the comparison of 11 Nov, re-run here)
def norm(t):
    t = t.rstrip('?')
    if t in ('', '?'): return '?'
    t = t.replace('!', '"')
    if t.startswith('g'): t = '9' + t[1:]
    t = {'H': '#', 'I': 'l'}.get(t, t)
    if t == '2:': return '2.'
    if re.fullmatch(r'[1-9]\.', t) and t != '2.': t = t[0] + "'"
    return t
R3 = {}
for l in open(S / 'R3.txt', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    l = re.sub(r'\^\{[^}]*\}', '', l).replace('_{', '').replace('}_', '')
    p = l.split(); m = re.match(r'R(\d+)', p[0]); ln = 'R%02d' % (int(m.group(1)) - 1) if m else p[0]
    R3[ln] = [norm(t) for t in p[1:] if not t.startswith('[')]
r3_units = sum(len([t for t in re.sub(r'\^\{([^}]*)\}', r'\1', l).replace('_{', '').replace('}_', '').split()[1:] if not t.startswith('[')])
               for l in open(S / 'R3.txt', encoding='utf-8') if l.strip() and not l.startswith('#'))
agree = 0; RC = collections.Counter(); LL = collections.OrderedDict()
for f in LED: LL.setdefault(f[0], []).append(f)
def val3(s):
    v = key.get(s)
    if v is None: return '?' + s
    if v.upper().startswith('NULL'): return '°'
    if v == 'repeat previous letter': return '~'
    return v
for ln, us in LL.items():
    A = [u[5] for u in us]; Bq = R3[ln]; m = [None] * len(A)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, A, Bq, autojunk=False).get_opcodes():
        for x in range(i1, i2):
            if op == 'equal': m[x] = ('eq', Bq[j1 + x - i1])
            elif op == 'replace' and i2 - i1 == j2 - j1: m[x] = ('rep', Bq[j1 + x - i1])
            else: m[x] = ('gap', '')
    for k, u in enumerate(us):
        t, b = m[k]
        if t == 'eq': agree += 1
        if 'CODE' in u[8]: c = 'E'
        elif t == 'gap': c = 'N'
        else:
            v = val3(b).lower(); want = (u[13] if u[13] != '' else '°').lower()
            c = 'S' if (v == want or ('/' in v and want in v.split('/')) or (u[12] == '~' and v == '~')) else 'E'
        RC[c] += 1
assert agree == 1395 and (RC['S'], RC['E'], RC['N']) == (1347, 149, 25), (agree, RC)
# ---- counts.txt
B = collections.Counter(f[8] for f in LED); O = collections.Counter(f[10] for f in LED)
fl = collections.Counter();
for f in LED:
    k = (f[0], int(f[1])); a = ADJ.get(k)
    new = 'DROP' if ((a and a[11] == 'DROP') or k in TWIN_DROP) else (a[11] if a else f[10])
    if new != f[10]: fl[(f[10], new)] += 1
K = collections.Counter((x['kind'], x['cls']) for x in units)
SUB = collections.Counter(x['sub'] for x in units if x['cls'] != 'S')
P = lambda a, b: '%d/%d = %.2f%%' % (a, b, 100 * a / b)
ctxl = B['CTX-LETTER'] + B['CTX-UNC'] + B['CTX-MN'] + B['CTX-GH'] + B['CTX-P1']
inword = B['KEY'] + B['KEY-P2ONLY'] + ctxl
out = []
w = out.append
w('pagni444: the arithmetic, every figure of issue 426 and the final count. Made by scripts/build.py from the stamped ledger.')
w('')
w('A. Pass 3 (11 Nov 2026), 1,521 units, classes of the stamped ledger (timestamps/stamped/LEDGER_444.tsv):')
for k in ('KEY', 'KEY-P2ONLY', 'NULL-KEY', 'CODE', 'NULL-CTX', 'CTX-LETTER', 'CTX-UNC', 'CTX-MN', 'CTX-GH', 'CTX-P1', 'UNREAD'): w('   %-11s %5d' % (k, B[k]))
w('   sum         %5d' % sum(B.values()))
w('')
w('B. The figures given at one time or another, all on those 1,521 units unless said:')
w('   89.7%   first reading (the 20:4x note of 11 Nov; pass 2 consensus): units inside a read word, context letters included, nulls and codes')
w('           left out of the numerator: 1,364/1,521 = 89.68%%. On the pass-3 classes the same measure is KEY %d + KEY-P2ONLY %d + context letters %d = %s.' % (B['KEY'], B['KEY-P2ONLY'], ctxl, P(inword, 1521)))
w('           It counts letters we supplied as read and does not count key nulls. Withdrawn as a measure.')
s915 = B['KEY'] + B['KEY-P2ONLY'] + B['NULL-KEY'] + B['CODE']
w('   91.5%%   pass 3 "strict": KEY %d + KEY-P2ONLY %d + NULL-KEY %d + CODE %d = %s. It counts the %d code signs as read.' % (B['KEY'], B['KEY-P2ONLY'], B['NULL-KEY'], B['CODE'], P(s915, 1521), B['CODE']))
w('           Withdrawn: no code value is fixed.')
s8994 = s915 - B['CODE']
w('   89.94%%  the same with the codes not read: %d - %d = %s. Not read: context letters %d + context nulls %d + codes %d = %d; unread %d.' % (s915, B['CODE'], P(s8994, 1521), ctxl, B['NULL-CTX'], B['CODE'], ctxl + B['NULL-CTX'] + B['CODE'], B['UNREAD']))
w('           Check %d + %d + %d = %d.' % (s8994, ctxl + B['NULL-CTX'] + B['CODE'], B['UNREAD'], s8994 + ctxl + B['NULL-CTX'] + B['CODE'] + B['UNREAD']))
w('   91.72%%  NOT a share read. The blind third transcription (%d sign tokens by our parser; 1,516 by its own note) has the same sign as pass 3 at %s of the pass-3 units.' % (r3_units, P(agree, 1521)))
w('   88.56%%  the blind third transcription under the same key and rule: S %d + E %d + N %d = %d; %s.' % (RC['S'], RC['E'], RC['N'], sum(RC.values()), P(RC['S'], 1521)))
w('           The two differ in sign, or one has no partner, at 1,521 - 1,395 = %d units. With %d more where the sign is the same but the' % (1521 - agree, 138 - (1521 - agree)))
w('           class under the comparison differs, 138 units were adjudicated on the image (adjudication.tsv).')
w('   90.42%%  after that adjudication (C below): %s.' % P(C['S'], N))
w('   95.7%   letters only, before adjudication: 1,224/1,279 = 95.70% (single-letter signs; nulls, codes, word signs and the repeat sign left out).')
w('           Not a headline figure: it leaves out the classes where the reading is weakest.')
w('')
w('C. Adjudication of the 138 disputed units (adjudication.tsv), rule: a unit is read (S) only if every sign the image allows gives')
w('   the accepted value by the key. Changes of class:')
for (a, b), v in sorted(fl.items()): w('   %s -> %-4s %3d' % (a, b, v))
drp = fl[('S', 'DROP')] + fl[('E', 'DROP')]
w('   units: 1,521 - %d with no sign on the image = %d' % (drp, 1521 - drp))
w('   S: %d - %d dropped - %d (S to E) + %d (E to S) = %d' % (O['S'], fl[('S', 'DROP')], fl[('S', 'E')], fl[('E', 'S')], O['S'] - fl[('S', 'DROP')] - fl[('S', 'E')] + fl[('E', 'S')]))
w('   E: %d - %d dropped - %d + %d = %d' % (O['E'], fl[('E', 'DROP')], fl[('E', 'S')], fl[('S', 'E')], O['E'] - fl[('E', 'DROP')] - fl[('E', 'S')] + fl[('S', 'E')]))
w('   N: %d' % O['N'])
w('   dropped units (pass-3 line, unit, sign): ' + '; '.join('%s u%d %s' % d[:3] for d in dropped))
w('')
w('D. FINAL COUNT. Rule of the project: a code is not read unless its value is fixed by a clear duplicate. None is: no code value')
w('   is spelled out anywhere in cipher or in clear. Units %d.' % N)
w('   kind         S      E      N    all')
tot = collections.Counter()
for kind in ('letter', 'repeat', 'word sign', 'null', 'code', 'unread'):
    r = [K[(kind, c)] for c in 'SEN']; w('   %-10s %4d   %4d   %4d   %4d' % (kind, r[0], r[1], r[2], sum(r)))
w('   %-10s %4d   %4d   %4d   %4d' % ('all', C['S'], C['E'], C['N'], N))
w('   READ (S)      %s' % P(C['S'], N))
w('   NOT READ (E)  %s' % P(C['E'], N))
w('   UNREAD (N)    %s' % P(C['N'], N))
w('   check %d + %d + %d = %d' % (C['S'], C['E'], C['N'], C['S'] + C['E'] + C['N']))
w('   The %d E units by reason:' % C['E'])
for k, v in sorted(SUB.items(), key=lambda x: -x[1]):
    if k != 'unread': w('   %4d  %s' % (v, k))
w('   %4d  sum' % sum(v for k, v in SUB.items() if k != 'unread'))
w('')
w('E. Sensitivities on the final count:')
Lc = sum(1 for x in units if x['sign'] == 'L')
w('   L counted as read (five uses, all fitting "Duca"; the reviewer accepts it): %d + %d = %s. Not claimed: no clear duplicate.' % (C['S'], Lc, P(C['S'] + Lc, N)))
p2 = sum(1 for x in units if x['b43class'] == 'KEY-P2ONLY' and x['cls'] == 'S')
w('   the %d units read by the key that only the second pass of the first reader had (no aligned sign in pass 1) taken out: %d - %d = %s.' % (p2, C['S'], p2, P(C['S'] - p2, N)))
w('   the sign 0 (R07, once) is E in this ledger and is not among the %d. The reviewer found 1,368 or 1,369 depending on that sign;' % C['S'])
w('   we cannot say from here which unit makes the difference of one.')
w('')
w('F. Signs dropped as nulls by context (dropped_signs.tsv), pass-3 labels, %d units: %d.' % (N, ctx_total))
for lab in ("9'", "5'", "1'", "4'"):
    t = tab[lab]; w('   %-3s dropped %2d; read by the key %2d, read by context %d' % (lab, t['null ctx'], t['read S'], t['read E']))
rest = [(lab, tab[lab]['null ctx']) for lab in sorted(tab, key=lambda s: (-tab[s]['null ctx'], s)) if tab[lab]['null ctx'] and lab not in ("9'", "5'", "1'", "4'")]
w('   the other %d: ' % sum(v for _, v in rest) + ', '.join('%s %d' % r for r in rest))
w('   check %d + %d = %d' % (sum(tab[l]['null ctx'] for l in ("9'", "5'", "1'", "4'")), sum(v for _, v in rest), ctx_total))
w('   After adjudication those %d are:' % ctx_total)
for k, v in sorted(after.items()): w('   %4d  %s' % (v, k))
w('   %4d  sum' % sum(after.values()))
(T / 'counts.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\n'.join(out))
print('OK: units %d, lines %d, S %d E %d N %d; transcription, decryption, units, overrides, dropped_signs, key, counts written' % (N, len(lines), C['S'], C['E'], C['N']))
