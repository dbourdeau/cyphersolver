"""Sense-based measure of the reading of DL 46150 (catalogue 1235), and the reading files built from it.

What is counted: the words of the cipher letter. They are the words of the clear minute that the cipher enciphers
(scripts/data/alignment.json, the EM alignment of the four cipher pages with the minute; every minute word has a
cipher counterpart) plus the words the cipher adds (code signs and "et" with no counterpart in the minute).

A word counts as read (sense) when its signs, under key.json, give a Latin word that fits the sentence:
  exact      the signs give the minute's word;
  spelling   only letters the writer left out, and the form is the minute's word with a double consonant written
             single or an h dropped (afinitatem, suma, comunem, retraere), or one listed in SPELLING;
  wording    the cipher's wording differs from the minute and the cipher's word fits (WORDING: uigesimam for
             uigesimamquartam, audiitque, euenit, debebit ...), or an added word that fits (ADDED_SENSE).
It does not count when it rests on
  suspect    a sign listed in transcription/suspects.md whose image check is ambiguous (fixed and confirmed rows
             are settled: a fix is in the transcription and alignment.json, a confirmed sign is a writer slip);
  unvalued   a sign with no value in key.json for that place (8C, y, H, 6, a letter sign standing where the minute
             has a title: "medio [x] eius sororis" = Illustrissime Domine Blance, 1 case);
  no sense   the signs give no fitting Latin word (writer slips such as proter, presenis, or a stretch not resolved);
and words with a lost sign are reported apart (damage).
READABLE_SUSPECT lists words that rest on a suspect sign but read as a fitting Latin word as they stand
(extendet, condiciones): they are not counted, and the figure with them is printed for reference.

    python measure.py            writes measure.txt and reading/p1-p4.md, reading/latin.md (prints measure.txt)
"""
import collections, difflib, json, pathlib, re

H = pathlib.Path(__file__).resolve().parent
A = json.load(open(H / 'scripts/data/alignment.json'))
P, WORDS, WID = A['path'], A['words'], A['wid']
KEY = {s: k for s, k in json.load(open(H / 'key.json')).items() if not s.startswith('_')}
DAM = '_'

SPELLING = {('P3L24', 'sanguine'),                              # sangine
            ('P2L10', 'contraxerat'), ('P1L08', 'prefatum')}     # cotraxerat, prefatu: nasal left out (retry, 30 Oct 2026)
# Extended key (retry pass, 30 Oct 2026; scripts/retry.py, reading/retry.md): values key.json's acceptance rule left out.
# qA = i in four words (circa, ipsam, animo, additione) and t in three (affinitatem, inter, debeat), every one of the
# seven checked on the image and confirmed as qA (transcription/suspects.md): qA is polyphonic s/i/t like qB (u/s/f).
# y = the code for 200,000 at both places the minute has "ducenta milia" / "ducentorum milium".
EXTENDED = {'qA': {'i', 't'}}
EXT_CODE = {'y': {'ducentamilia', 'ducentorummilium'}}
WORDING = {('P1L01', 'uigesimamquartam'): 'ad uigesimam diem (the 20th; the minute: 24th)',
           ('P1L12', 'audiuitque'): 'audiitque, the contracted perfect',
           ('P3L08', 'uestitum'): 'in uestitu sponse (ablative)',
           ('P4L05', 'euenerit'): 'sin aliter euenit',
           ('P4L05', 'debebitis'): 'debebit (subject: Dominatio Vestra, as in remittet)',
           ('P3L04', 'tantum'): 'the cipher has "habere uelit tantum cupiat", the minute "tantum habere cupiat"; the '
                                'alignment crossed the two words, so its suspects P3L04 #26 and P3L05 #1 are artefacts',
           ('P3L05', 'habere'): 'see tantum',
           ('P3L02', 'extendit'): 'extendet (future); the w (P3L03 #5) is confirmed on the image (suspects.md)',
           ('P3L20', 'conditiones'): 'condiciones; the mH is confirmed on the image (suspects.md)',
           ('P2L20', 'deberet'): 'debeat (qA = t, extended key); the minute word is itself doubtful ("[?deberet]")',
           ('P3L08', 'necessaria'): 'necessarie, the adverb ("necessarie exponenda esse")',
           # P2L22: the cipher has "neque [u]ideat a quibus haberi possit" (nor does he see from whom it could be had)
           # where the minute has "imo videat quod ambobus haberi possit" (retry, 30 Oct 2026)
           ('P2L22', 'imo'): 'neque (the cipher wording: "neque uideat a quibus haberi possit")',
           ('P2L22', 'quod'): 'a (neque uideat a quibus)', ('P2L22', 'ambobus'): 'quibus (neque uideat a quibus)'}
DISPLAY = {('P3L04', 'tantum'): 'habere', ('P3L05', 'habere'): 'tantum',   # the cipher's word order
           ('P2L22', 'imo'): 'neque'}
EXTRA_ADDED = [dict(line='P3L04', form='uelit', after=('P3L04', 'tantum'), note='uelit (habere uelit tantum)')]
READABLE_SUSPECT = {('P3L03', 'extendit'): 'extendet (future)', ('P3L20', 'conditiones'): 'condiciones'}
ADDED_SENSE = {('P1L25', 'Gp'): 'non (amabat non mediocriter)', ('P3L02', '&'): 'et', ('P3L12', '&'): 'et',
               ('P4L04', '&'): 'et', ('P3L24', 'K'): 'quoniam, where the minute has an illegible word before ipsa',
               ('P4L01', 'dt'): 'quod (operabitur quod), the minute\'s quod; the minute word aligned to it is lost'}
ADDED_FORM = {('P4L01', 'dt'): 'quod'}
UNVALUED_SIGNS = {'8C', 'y', 'H', '6'}


def ok(p):
    k = KEY.get(p['sign'])
    if p['sign'] == DAM or not k: return False
    if p['type'] == 'code' and p['txt'] in EXT_CODE.get(p['sign'], ()): return True
    if p['type'] == 'code': return k['kind'] == 'code' and p['txt'] in k['values']
    if p['txt'] in EXTENDED.get(p['sign'], ()): return True
    if k['kind'] == 'code': return False
    return p['txt'] in k['values'] or (k['kind'] == 'null' and p['txt'] == '')


def emit(p):
    """What the signs of a unit give under the key (a polyphonic sign takes the value of its set the alignment chose)."""
    s, k = p['sign'], KEY.get(p['sign'])
    if s == DAM: return '_'
    if not k: return '#'
    if k['kind'] == 'null': return ''
    if p['type'] == 'code' and p['txt'] in EXT_CODE.get(s, ()): return '{' + p['txt'] + '}'
    if k['kind'] == 'code': return '{' + (p['txt'] if p['type'] == 'code' else k['values'][0]) + '}'
    if p['txt'] in k['values'] or p['txt'] in EXTENDED.get(s, ()): return p['txt']
    return k['values'][0] if k['values'] else '#'


def suspects():
    out = set()
    for l in open(H / 'transcription/suspects.md', encoding='utf-8'):
        m = re.match(r'\| (P\dL\d\d) \| (\d+) \|', l)
        if m and ' FIXED ' not in l and ' confirmed ' not in l:     # image verdicts: fixed or confirmed rows are settled
            out.add((m.group(1), int(m.group(2))))
    return out


degem = lambda w: re.sub(r'(.)\1', r'\1', w).replace('h', '')


def classify():
    sus = suspects()
    # token position of every unit in its line (as in transcription/suspects.md)
    pos, cur, n = {}, None, 0
    for p in P:
        if p['type'] == 'skip': continue
        if p['line'] != cur: cur, n = p['line'], 0
        pos[id(p)] = n + 1; n += p['ntok']
    wu, wskip, first = collections.defaultdict(list), collections.Counter(), {}
    for p in P:
        for i in range(p['a'], p['b']):
            if p['type'] == 'skip': wskip[WID[i]] += 1
            elif not wu[WID[i]] or wu[WID[i]][-1] is not p: wu[WID[i]].append(p)
            if p['type'] != 'skip': first.setdefault(WID[i], p['line'])
    last = 'P1L01'
    for w in range(len(WORDS)):
        last = first.setdefault(w, last)
    recs = []
    for w, clear in enumerate(WORDS):
        us, ln = wu.get(w, []), first[w]
        form = ''.join(emit(p) for p in us)
        bad = [p for p in us if not ok(p)]
        r = dict(line=ln, clear=clear, form=form, signs=' '.join(p['sign'] for p in us), note='')
        if any(p['sign'] == DAM for p in us): r['status'] = 'damage'
        elif not bad and not wskip[w]: r['status'] = 'exact'
        elif (ln, clear) in WORDING: r['status'] = 'wording'; r['note'] = WORDING[(ln, clear)]
        elif any(pos.get(id(p)) and (ln if p['line'] == ln else p['line'], pos[id(p)]) in sus for p in bad) or \
                any((p['line'], pos.get(id(p))) in sus for p in bad):
            r['status'] = 'suspect'
            if (ln, clear) in READABLE_SUSPECT: r['note'] = 'readable as ' + READABLE_SUSPECT[(ln, clear)]
        elif (ln, clear) in WORDING: r['status'] = 'wording'; r['note'] = WORDING[(ln, clear)]
        elif not bad and ((ln, clear) in SPELLING or degem(form) == degem(clear)): r['status'] = 'spelling'
        elif any(p['sign'] in UNVALUED_SIGNS or not KEY.get(p['sign']) or not KEY[p['sign']]['values'] and KEY[p['sign']]['kind'] != 'null'
                 or (len(p['txt']) > 2 and KEY[p['sign']]['kind'] != 'code') for p in bad):
            r['status'] = 'unvalued'
        else: r['status'] = 'no sense'
        r['w'] = w
        recs.append(r)
    adds = []                                              # words the cipher adds
    for p in P:
        if p['type'] == 'skip' or p['a'] != p['b']: continue
        k = KEY.get(p['sign']) or {}
        if k.get('kind') == 'code' or p['sign'] == '&':
            key = (p['line'], p['sign'])
            word = (k['values'][0] if k.get('values') else '?') if p['sign'] != '&' else 'et'
            word = ADDED_FORM.get(key, word)
            adds.append(dict(line=p['line'], clear='', form=word, signs=p['sign'], at=p['a'],
                             status='added' if key in ADDED_SENSE else 'no sense',
                             note=ADDED_SENSE.get(key, 'code sign with no counterpart in the minute')))
    for e in EXTRA_ADDED:
        w = next(r['w'] for r in recs if (r['line'], r['clear']) == e['after'])
        adds.append(dict(line=e['line'], clear='', form=e['form'], signs='', at=None, after_w=w, status='added', note=e['note']))
    return recs, adds


SENSE = ('exact', 'spelling', 'wording', 'added')


def measure(recs, adds):
    pages = ['P1', 'P2', 'P3', 'P4']
    out = ['Sense-based measure of DL 46150 (measure.py; key.json; scripts/data/alignment.json).',
           'Unit: words of the cipher letter (minute words the cipher enciphers + words the cipher adds). Read = '
           'the signs give a Latin word that fits the sentence (exact, spelling variant, different wording, added '
           'word). Not read = rests on an unchecked suspect sign, an unvalued sign, or gives no fitting word. '
           'Damage (a lost sign) apart.', '']
    tot = {}
    for pg in pages + ['ALL']:
        R = [r for r in recs + adds if pg == 'ALL' or r['line'].startswith(pg)]
        c = collections.Counter(r['status'] for r in R)
        n, d = len(R), c['damage']; s = sum(c[x] for x in SENSE)
        rs = sum(1 for r in R if r['status'] == 'suspect' and r['note'])
        tot[pg] = (s, n, d)
        out.append(f"{pg}: words {n}  read {s} ({100 * s / n:.1f}%; of undamaged {100 * s / (n - d):.1f}%)  "
                   f"[exact {c['exact']}, spelling {c['spelling']}, wording {c['wording']}, added {c['added']}]  "
                   f"not read: suspect {c['suspect']} (readable as they stand {rs}), unvalued {c['unvalued']}, "
                   f"no sense {c['no sense']}  |  damage {d} ({100 * d / n:.1f}%)")
    s, n, d = tot['ALL']
    rs = sum(1 for r in recs if r['status'] == 'suspect' and r['note'])
    out += ['', f'Read share (fraction_read): {s}/{n} = {s / n:.3f}; of undamaged words {s / (n - d):.3f}; '
                f'with the {rs} readable suspect words: {(s + rs) / n:.3f}.',
            'README read bar: 95% of words read as sense -> ' + ('read' if s / n >= 0.95 else 'read in part') + '.', '',
            'Strict agreement with the clear minute (reading/measure_external.txt, scripts/ext/report.py): tokens '
            '3047/3199 = 95.2% (95.7% of undamaged), minute words 503/616 = 81.7% (83.3% of undamaged).',
            'Blind reading (ciphertext-only key14, before the minute was found): 396 of 424 words read = 93.4% '
            'exactly right.', '', '## Words not read, by cause', '']
    for st in ('suspect', 'unvalued', 'no sense', 'damage'):
        R = [r for r in recs + adds if r['status'] == st]
        out.append(f'{st} ({len(R)}): ' + '; '.join(f"{r['line']} {r['form'] or '-'}"
                   + (f"({r['clear']})" if r['clear'] else '+') + (f" [{r['note']}]" if r['note'] else '') for r in R))
        out.append('')
    out.append('## Read words that differ from the minute')
    out.append('')
    for st in ('spelling', 'wording', 'added'):
        R = [r for r in recs + adds if r['status'] == st]
        out.append(f'{st} ({len(R)}): ' + '; '.join(f"{r['line']} {r['form']}" + (f"({r['clear']})" if r['clear'] else '')
                                                   for r in R))
    return '\n'.join(out) + '\n', tot


# ---------------------------------------------------------------- reading files
def clear_tokens():
    """Capitalisation and punctuation of each minute word, from reading/clear_minute_running.txt."""
    t = (H / 'reading/clear_minute_running.txt').read_text(encoding='utf-8').split('\n', 1)[1].split()
    n = lambda w: re.sub('[^a-z]', '', w.lower().replace('v', 'u').replace('j', 'i'))
    toks = [x for x in t if n(x)]
    assert [n(x) for x in toks] == WORDS
    return toks


def shown(r, tok):
    """The word as printed in the reading."""
    m = re.match(r'^[\[(?]*(.*?)([.,;:!?\]]*)$', tok)
    cap = re.sub(r'^\[\?', '', tok)[:1].isupper()
    punct = re.sub(r'[\]?]', '', m.group(2)) if m else ''
    w = r['clear']
    if r['status'] == 'damage': return '⟨' + w + '⟩' + punct
    if r['status'] in ('spelling', 'wording'): w = DISPLAY.get((r['line'], r['clear']), r['form'])
    if r['status'] in ('suspect', 'unvalued', 'no sense'):
        sim = difflib.SequenceMatcher(None, re.sub('[{}_#]', '', r['form']), r['clear']).ratio()
        return ('[?' + (w.capitalize() if cap else w) + ']' if sim >= 0.5 else '[...]') + punct
    w = w.capitalize() if cap else w
    return ('V' + w[1:] if w[:1] == 'U' else w) + punct


def tidy(text):
    """An added word after a sentence end takes the capital."""
    return re.sub(r'([.;:] )(et|non|quod|uelit) ([A-Z])', lambda m: m.group(1) + m.group(2).capitalize() + ' ' + m.group(3).lower(), text)


def build(recs, adds):
    toks = clear_tokens()
    wend = {}
    for i, x in enumerate(WID): wend[x] = i + 1
    lines = collections.OrderedDict()
    for p in P:
        if p['type'] != 'skip': lines.setdefault(p['line'], [])
    for r in recs:
        lines[r['line']].append(shown(r, toks[r['w']]))
        for a in adds:
            if a['at'] == wend[r['w']] or a.get('after_w') == r['w']:
                lines[a['line']].append(a['form'] if a['status'] == 'added' else '[...]')
    # code words: mark the words one code sign stands for
    signs = {}
    for i in range(1, 5):
        for l in open(H / f'transcription/p{i}.txt', encoding='utf-8'):
            if l.strip():
                ln, rest = l.split(':', 1)
                signs[f'P{i}{ln.strip()}'] = rest.strip()
    units = collections.defaultdict(list)
    for p in P:
        if p['type'] != 'skip': units[p['line']].append(emit(p) or '·')
    pages = collections.OrderedDict()
    for ln, ws in lines.items(): pages.setdefault(ln[:2], []).append((ln, ws))
    head = ('Decryption of DL 46150 under key.json, line by line against transcription/p{n}.txt. signs = the '
            'transcription; decrypt = what each unit gives (· null, {{...}} code sign, _ lost sign, # no value; '
            'a polyphonic sign shows the value of its set that fits); Latin = the words whose first sign stands on '
            'the line. [?word] = rests on a suspect or unvalued sign (the word the context and the minute call '
            'for); [...] = not read; ⟨word⟩ = lost to damage, filled from the clear minute (ASMi Sforzesco 642).')
    for pg, rows in pages.items():
        n = pg[1]
        L = [f'# DL 46150, page {n}: line-by-line decryption', '', head.format(n=n), '']
        for ln, ws in rows:
            L += [f'## {ln}', '', '```', 'signs:   ' + signs.get(ln, ''), 'decrypt: ' + ' '.join(units[ln]), '```',
                  '', 'Latin: ' + tidy(' '.join(ws)), '']
        (H / f'reading/p{n}.md').write_text('\n'.join(L), encoding='utf-8')
    L = ['# DL 46150: the Latin reading', '',
         'Maffeo da Treviglio to Tamás Bakócz, Milan, 30 November 1490. The cipher text under key.json, with word '
         'division and punctuation (taken from the minute where the cipher has the same words). [?word] = rests on a '
         'suspect or unvalued sign; [...] = not read; ⟨word⟩ = lost to damage, filled from the clear minute. Spelling '
         'and wording are the cipher\'s where they differ from the minute (afinitatem, suma, uigesimam). Line '
         'numbers: reading/p1-p4.md.', '', 'In christo pater et domine pater honorande.', '']
    for pg, rows in pages.items():
        L += [f'## Page {pg[1]}', '', tidy(' '.join(w for _, ws in rows for w in ws)), '']
    L += ['In clear below the cipher (transcription/p4_clear.txt): R(everendissi)me D(ominationi) V(estre) me ex animo '
          'commendo. Mediolani in festo S(ancti) Andree apostoli ult(im)a [?] decembris [?] 1490. E(iusdem) R(everendissi)me '
          'D(ominationis) V(estre) Filius Mapheus Triuliensis.', '',
          'Address, in clear: R(everendissi)mo in christo patri et D(omi)no [?] patri honor(ando) D(omino) Thome '
          'ep(iscop)o Jaurien(si), Ser(enissi)mi D(omini) Regis Ungarie Cancellario &c.', '']
    (H / 'reading/latin.md').write_text('\n'.join(L), encoding='utf-8')


if __name__ == '__main__':
    recs, adds = classify()
    txt, tot = measure(recs, adds)
    (H / 'measure.txt').write_text(txt, encoding='utf-8')
    build(recs, adds)
    print(txt)
