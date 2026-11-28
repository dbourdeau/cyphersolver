"""Build the write-up files of Penn LJS 51 from the chain records and the by-eye keys.

    python build_texts.py            (run from targets/ljs51corpus/)

Reads chains_all.json (the chain records from the master TIFFs), keys_eye/*.json (the by-eye keys) and the
translation_*.md files; writes
    texts/cipher_<range>.md     the cipher as transcribed, chain by chain: sign counts per line, the sign inventory,
                                and the sign labels line by line where a by-eye key exists
    texts/arabic_<range>.md     the compiler's plaintext (his decipherment), chain by chain, as read on the masters
    keys.tsv                    one row per sign of every keyed chain: chain, sign label, letter(s), count
    validation.tsv              cipher token (chain:sign) TAB letter, from the keyed chains' alignments
    texts/stats.json            counts used by profile.json and the write-up
    texts/record_comparisons.md count and wording differences in the new by-eye waves
and replaces documents, outcome.texts and the measured shares in profile.json.

Corrections that the chain records do not yet carry are applied here and said in the files:
  - 46v.11 and 13r.1 are one cipher split across the misbound quire 3 (keys_eye/46v.11+13r.1.json);
  - 20r.8 is the first half of the 47r.1 riddle cipher (keys_eye/20r.8+47r.1.json): its plaintext is riddle verses
    1-5, not the f. 21r rhymed prose; its last five rows (21r l.1-5) belong to 48r.8;
  - 48r.8 (with 21r l.1-5) has its own page (targets/ljs51f48r) and 106v.6 has its own page (targets/qaysarani1350):
    one key, one entry, so they are not documents here.
"""
import json, glob, os, re, collections, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
RANGES = [(6, 53), (54, 77), (78, 101), (102, 125), (126, 149), (150, 173), (174, 197), (198, 217)]
OWN_PAGE = {'48r.8': 'ljs51f48r', '106v.6': 'qaysarani1350'}
MERGE = {'46v.11': '46v.11+13r.1', '13r.1': '46v.11+13r.1', '20r.8': '20r.8+47r.1', '47r.1': '20r.8+47r.1'}
SITE = 'https://dbourdeau.github.io/cyphersolver/'


def img(r):
    v = r['pages'][0]['image']
    return int(str(v).split('_')[-1])


def rng(i):
    for a, b in RANGES:
        if a <= i <= b: return f'{a:04d}_{b:04d}'
    raise ValueError(i)


recs = json.load(open('chains_all.json', encoding='utf-8'))
byid = {r['chain_id']: r for r in recs}
keys = {}
for f in sorted(glob.glob('keys_eye/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    keys[os.path.basename(f)[:-5]] = d


def keystate(cid):
    """'letter' (a by-eye key, letter-level), 'class' (tashifi), 'tree' (63v), 'partial', or None."""
    d = keys.get(cid)
    if not d or not d.get('key'): return None
    v = str(d.get('verdict') or '').lower().removeprefix('key ')
    if cid == '14v.7': return 'class'
    if cid == '63v.trees': return 'tree'
    if v.startswith('inconsistent') or v.startswith('not keyed') or v.startswith('no plaintext'): return None
    if v.startswith('partly'): return 'partial'
    if v.startswith('consistent'): return 'letter'
    raise ValueError(f'{cid}: key table has no recognized verdict: {v}')


# documents: one per cipher (merged records count once), without the two ciphers that have their own pages
docs = []
seen = set()
for r in recs:
    cid = r['chain_id']
    if cid in OWN_PAGE: continue
    did = MERGE.get(cid, cid)
    if did in seen: continue
    seen.add(did)
    parts = [x for x in (did.split('+') if '+' in did else [did])]
    rr = [byid[p] for p in parts]
    kd = keys.get(did) or (keys.get(cid) if did == cid else None)
    ks = keystate(did)
    if kd and kd.get('signs') and did not in ('14v.7', '102v.11'):
        signs, how = int(kd['signs']), f'by-eye record keys_eye/{did}.json'
    else:
        signs, how = sum(int(x['signs_total']) for x in rr), 'chain record (by-eye count on the master)'
    if did == '30v.7': signs, how = 81, 'by-eye recount in recheck_unanswered.jsonl (the record total 95 was the segmenter count)'
    if did == '20r.8+47r.1': how += ' (the record of 20r.8 counted 21r l.1-5, which belong to 48r.8)'
    ans = rr[0]['answered']
    if did == '46v.11+13r.1': ans = 'yes'
    if did == '20r.8+47r.1': ans = 'yes'
    state = {'yes': 'read', 'partial': 'read in part', 'no': 'not read'}[ans.split()[0]]
    # a by-eye key that aligns the cipher with the plaintext (at least 95% of the signs) shows the plaintext answers it
    # in full, whatever the record's first fit check said (2r.4, 7r.5, 7v.12, 10v.1, 12r.8 ...)
    meas = (kd or {}).get('measures') or {}
    upgraded = False
    if (state == 'read in part' and ks in ('letter', 'partial') and not kd.get('unresolved_positions')
            and isinstance(meas.get('aligned_pairs'), int) and meas['aligned_pairs'] >= 0.95 * signs):
        state, upgraded = 'read', True
    folios = []
    for x in rr:
        for p in x['pages']:
            if p['folio'] not in folios: folios.append(p['folio'])
    docs.append(dict(id=did, recs=rr, parts=parts, signs=signs, count_how=how, state=state, key=ks,
                     folios=folios, image=img(rr[0]), range=rng(img(rr[0])), red=any(x['red_gloss'] for x in rr), upgraded=upgraded))

# plaintexts (the compiler's decipherment as read on the masters), with the corrections above
def plaintext(d):
    did = d['id']
    if did in ('20r.8+47r.1', '46v.11+13r.1'):
        return keys[did]['plaintext'], 'as enciphered (keys_eye/%s.json); the clear copy differs in a few words, see that file' % did
    r = d['recs'][0]
    kd = keys.get(did)
    if d['key'] in ('letter', 'partial', 'tree') and kd:
        kt = kd.get('plaintext_cipher_form') or kd.get('plaintext_used') or kd.get('plaintext')
        if not isinstance(kt, str):
            kt = None
        if not kt and isinstance(kd.get('plaintext_words'), list): kt = ' '.join(kd['plaintext_words'])
        if kt and '!' in kt:
            # These alignments prefix an omitted plaintext letter with !.
            marked = re.findall(r'!([\u0621-\u064a])', kt)
            if marked != [row[0] for row in kd['dropped_letters']]:
                raise ValueError(f'{did}: check omitted-letter notation')
            kt = re.sub(r'![\u0621-\u064a]', '', kt)
        if kt:
            method = 'tree-script rule' if d['key'] == 'tree' else 'by-eye key'
            return kt, f"as enciphered, from the {method} in keys_eye/{did}.json; written copy {r['plaintext'].get('folio_lines') or ''}"
    t = r['plaintext'].get('text') or ''
    if t in ('not read', 'not found') or not t.strip(): return None, r['plaintext'].get('folio_lines') or ''
    return t, '%s; certainty %s' % (r['plaintext'].get('folio_lines') or '', r['plaintext'].get('certainty') or '')


def gl(v):
    return '; '.join(f'{k}: {w}' for k, w in v.items()) if isinstance(v, dict) else str(v)


def lines_of(kd):
    cl = kd.get('cipher_lines')
    out = []
    if isinstance(cl, dict):
        for k, v in cl.items():
            out.append((k, v if isinstance(v, str) else ' '.join(map(str, v))))
    elif kd.get('alignment'):
        by = collections.OrderedDict()
        for row in kd['alignment']:
            by.setdefault(row[0], []).append(str(row[2]))
        out = [(k, ' '.join(v)) for k, v in by.items()]
    return out


os.makedirs('texts', exist_ok=True)
def comparison_words(text):
    text = unicodedata.normalize('NFKC', text).translate(str.maketrans('أإآٱةى', 'ااااهي'))
    text = ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn' and ch != 'ـ')
    return re.findall(r'[ء-ي]+', text)


comparison = ['# Penn LJS 51, differences between chain records and by-eye keys from f. 37r onwards', '',
              'The record gives the earlier transcription. The key form follows the signs where they could be aligned. '
              'The cipher sometimes covers only part of a verse. Elsewhere a difference can reflect the spelling in the cipher, '
              'an omitted letter, or a correction to the earlier reading. '
              'Each linked key gives its evidence and uncertainties. The comparison ignores vowels, verse separators, '
              'uncertainty marks, alif variants, final ta marbuta versus ha, and alif maqsura versus ya. Word breaks are retained.', '']
for d in docs:
    if d['image'] < 78 or d['key'] not in ('letter', 'partial') or len(d['recs']) != 1:
        continue
    r = d['recs'][0]
    pt, _ = plaintext(d)
    original = r['plaintext'].get('text') or ''
    count_changed = int(r['signs_total']) != d['signs']
    text_changed = bool(original and pt and comparison_words(original) != comparison_words(pt))
    if not count_changed and not text_changed:
        continue
    cid = d['id']
    comparison.extend([f"## [{cid}](../keys_eye/{cid}.json)", ''])
    if count_changed:
        comparison.append(f"Sign count in the record: {r['signs_total']}. By-eye recount: {d['signs']}.")
    if text_changed:
        if count_changed:
            comparison.append('')
        comparison.extend(['Record: ' + original, '', 'Key form: ' + pt])
    recheck = keys[cid].get('shape_recheck') or {}
    if isinstance(recheck.get('alternative'), str):
        comparison.extend(['', 'Alternative reading: ' + recheck['alternative']])
    elif recheck.get('interpretation'):
        comparison.extend(['', recheck['interpretation']])
    comparison.append('')
with open('texts/record_comparisons.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(comparison))

tr_files = {f'{a:04d}_{b:04d}': f'translation_{a:04d}_{b:04d}.md' for a, b in RANGES}
groups = collections.OrderedDict((f'{a:04d}_{b:04d}', []) for a, b in RANGES)
for d in docs: groups[d['range']].append(d)

for g, ds in groups.items():
    a, b = g.split('_')
    C = [f'# Penn LJS 51, images {a}-{b}: the ciphers as transcribed', '',
         'Model transcription from the OPenn master TIFFs (2339 x 2959 px), checked by eye; no human has checked it.',
         'Per cipher: where it stands, the sign count per line (by eye), the word groups, the sign inventory as described,',
         'and, where a by-eye key was built (keys_eye/), the signs line by line in reading order (usually right to left; | = word divider).',
         'Labels are names for shapes within one cipher only: S3 in one cipher is not S3 in another.', '']
    A = [f'# Penn LJS 51, images {a}-{b}: the compiler\'s decipherments', '',
         'The plaintext the compiler writes after each cipher (his own solution, or the solution of the patron or the',
         'correspondent that he copies), read on the OPenn master TIFFs by a model and not checked by a human Arabist.',
         '[?] marks a doubtful word. English translation: ' + tr_files[g] + (' and translation_supplement.md' if g in ('0006_0053', '0078_0101', '0102_0125', '0126_0149') else '') + '.', '']
    for d in ds:
        r0 = d['recs'][0]
        where = '; '.join(f"f. {p['folio']} l.{p['lines'][0]}-{p['lines'][1]} (image {img({'pages': [p]}):04d})" for x in d['recs'] for p in x['pages'] if p.get('lines'))
        C.append(f"## {d['id']}")
        C.append('')
        C.append(f"- Where: {where}")
        C.append(f"- Signs: {d['signs']} ({d['count_how']})" + ('' if len(d['recs']) == 1 else '; records ' + ', '.join(d['parts'])))
        kd = keys.get(d['id'])
        by_line = collections.Counter(row[0] for row in (kd or {}).get('alignment', [])
                                      if row[0] is not None and row[2] not in (None, '-', '+', ''))
        has_recount = bool(by_line) and sum(by_line.values()) == d['signs']
        if has_recount:
            C.append('- Signs per line in the by-eye record: ' + ', '.join(f'{line}: {n}' for line, n in by_line.items()))
            groups_seen = kd.get('measures', {}).get('groups')
            if isinstance(groups_seen, int):
                C.append(f'- Word groups in the by-eye record: {groups_seen}')
        for x in d['recs']:
            spl = x.get('signs_per_line')
            if spl and not has_recount:
                C.append(f"- Earlier chain record, signs per line ({x['chain_id']}): {', '.join(map(str, spl))}" + (f"; word groups {x['word_groups']}" if x.get('word_groups') else ''))
            elif has_recount and x.get('word_groups') and not isinstance(groups_seen, int):
                C.append(f"- Word groups reported in the earlier record ({x['chain_id']}): {x['word_groups']}")
            C.append(f"- Sign inventory ({x['chain_id']}): {x.get('style') or 'not described'}")
            if x.get('rule') and x.get('cipher_text'):
                C.extend(['- Cipher as written: ' + x['cipher_text'], '- Rule: ' + x['rule'],
                          '- Comparison with the clear copy: ' + x['fit_check']])
            if x.get('red_gloss'): C.append(f"- Red gloss ({x['chain_id']}): yes" + (f" - {gl(x['gloss_letters'])}" if x.get('gloss_letters') else ''))
        if d['id'] == '63v.trees' and kd:
            C.append('- Trees (row.position: left/right branch counts = letter by the rule):')
            C.append('')
            C.append('    ' + ' '.join(f"{t['row']}.{t['index_in_row']}:{t['left_branches']}/{t['right_branches']}={t['rule_letter']}" for t in kd['trees']))
        elif kd and lines_of(kd):
            C.append(f"- Sign labels by line (keys_eye/{d['id']}.json):")
            C.append('')
            for k, v in lines_of(kd): C.append(f'    {k}: {v}')
        C.append('')
        pt, src = plaintext(d)
        A.append(f"## {d['id']}")
        A.append('')
        if pt:
            A.append(pt)
            A.append('')
            fit = (kd or {}).get('verdict') or r0.get('fit_check') or ''
            A.append(f"({src}; " + {'read': 'answered in full', 'read in part': 'answered in part: ' + fit[:300], 'not read': ''}[d['state']] + ')')
        else:
            A.append('[no plaintext: ' + (r0.get('fit_check') or r0.get('notes') or '')[:300] + ']')
        A.append('')
    open(f'texts/cipher_{g}.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(C))
    open(f'texts/arabic_{g}.md', 'w', encoding='utf-8', newline='\n').write('\n'.join(A))

# keys.tsv and validation.tsv
K = ['# Penn LJS 51: by-eye keys from the compiler\'s plaintext, not independently confirmed (keys_eye/<chain>.json)',
     '# chain\tsign\tletters (count)\tkey state']
V = ['# model: ar-mamluk', '# source: keys_eye/*.json alignments of the chains keyed letter by letter (consistent or partly consistent)',
     '# note: tokens are chain:sign, so every cipher keeps its own alphabet; a ? line separates the ciphers']
keyed = [d for d in docs if d['key']]
for d in keyed:
    kd = keys[d['id']]
    if d['key'] == 'tree':
        for letter, v in kd['key'].items():
            K.append(f"{d['id']}\tL{v['left']}/R{v['right']}\t{letter} ({v.get('attested', '')})\ttree rule")
        continue
    if d['key'] == 'class':
        for s, v in kd['key'].items():
            K.append(f"{d['id']}\t{s}\t{v}\ttashifi class")
        continue
    for s, v in kd['key'].items():
        if isinstance(v, dict):
            values = ', '.join(f'{l} ({n})' for l, n in v.items()) or 'unassigned'
            K.append(f"{d['id']}\t{s}\t{values}\t{d['key']}")
    if kd.get('alignment'):
        V.append('?\t?')
        for row in kd['alignment']:
            s, letter = row[2:4]
            if s in (None, '-', '?', '+', ''):
                continue  # A letter dropped from the cipher has no sign to score.
            if s not in kd['key'] or letter not in kd['key'][s] or letter in (None, '-', '+', '?', ''):
                V.append('?\t?')
            else:
                V.append(f"{d['id']}:{s}\t{letter}")
open('keys.tsv', 'w', encoding='utf-8', newline='\n').write('\n'.join(K) + '\n')
open('validation.tsv', 'w', encoding='utf-8', newline='\n').write('\n'.join(V) + '\n')

# stats
tot = sum(d['signs'] for d in docs)
read = sum(d['signs'] for d in docs if d['state'] == 'read')
red = [(k, v.get('red_check')) for k, v in keys.items() if isinstance(v.get('red_check'), dict)]
agree = glossed = 0
red_agree_chains = []
for k, rc in red:
    n = rc.get('compared', rc.get('red_read', rc.get('glossed_signs')))
    matches = rc.get('agree_letter', rc.get('agree'))
    if isinstance(n, int) and isinstance(matches, int):
        if not 0 <= matches <= n:
            raise ValueError(f'{k}: invalid red-letter agreement {matches}/{n}')
        glossed += n
        agree += matches
        red_agree_chains.append(k)
st = dict(documents=len(docs), signs=tot, signs_read=read, fraction=round(read / tot, 4),
          by_state=dict(collections.Counter(d['state'] for d in docs)),
          signs_by_state={s: sum(d['signs'] for d in docs if d['state'] == s) for s in ('read', 'read in part', 'not read')},
          keyed=len(keyed), keyed_by_kind=dict(collections.Counter(d['key'] for d in keyed)),
          keyed_ids=[d['id'] for d in keyed], key_files=len(keys),
          not_keyed_files=[k for k in keys if k not in {d['id'] for d in keyed}],
          red_gloss_docs=sum(1 for d in docs if d['red']), red_agree=agree, red_glossed=glossed,
          red_agree_chains=red_agree_chains,
          groups={g: dict(docs=len(ds), signs=sum(d['signs'] for d in ds), read=sum(d['signs'] for d in ds if d['state'] == 'read'))
                  for g, ds in groups.items()},
          open=[(d['id'], d['state'], d['signs']) for d in docs if d['state'] != 'read'])
json.dump(st, open('texts/stats.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# profile.json: documents, texts, shares
P = json.load(open('profile.json', encoding='utf-8'))
PD = []
for d in docs:
    r0 = d['recs'][0]
    pl = ['separate paragraph'] + (['interlinear'] if d['red'] else [])
    if d['state'] == 'not read': pl = ['interlinear'] if d['red'] else ['none']
    pt, src = plaintext(d)
    PD.append({
        'id': d['id'], 'read': d['state'],
        'shelfmark': 'University of Pennsylvania, Kislak Center, LJS 51, ' + ', '.join('f. ' + f for f in d['folios']) + f" (OPenn image 0084_{d['image']:04d})",
        'date': 'text c. 1330-1361 (this project: f. 62r is after Safar 760/1359; the compiler died in 762/1361); copy 15th century (Penn: "14--")',
        'year': 1350, 'country': 'Egypt or Syria (Mamluk sultanate)', 'language': 'Arabic', 'pages': len(d['folios']),
        'cleartext_in_document': 'separate passages',
        'plaintext': {'location': pl, 'partial': d['state'] != 'read',
                      'source': ("The compiler's plaintext after the cipher: " + src[:240]) if pt else ('No plaintext in the volume' + (' (a red gloss survives, mostly unread)' if d['red'] else '') + '.')},
        'length': {'tokens': d['signs'], 'unit': 'symbols', 'measured': False},
        'transcription': {'by': 'llm from images', 'source': 'OPenn master TIFF, 2339 x 2959 px; texts/cipher_%s.md' % d['range'],
                          'image_quality': 'poor' if d['id'] == '1r.2' else 'good',
                          'notes': ('Count from ' + d['count_how'] + '. ' + (r0.get('count_method') or '')[:200]).strip()},
    })
P['documents'] = PD
o = P['outcome']
o['fraction_read'] = st['fraction']
texts = []
summ = json.load(open('texts/summaries.json', encoding='utf-8'))
for g, ds in groups.items():
    gs = st['groups'][g]
    share = round(gs['read'] / gs['signs'], 4)
    allread = all(d['state'] == 'read' for d in ds)
    t = {'doc': [d['id'] for d in ds], 'label': f"Images {g.replace('_', '-')} (ff. {ds[0]['folios'][0]}-{ds[-1]['folios'][-1]}), {len(ds)} ciphers",
         'transcription': f'texts/cipher_{g}.md', 'decryption': f'texts/arabic_{g}.md',
         'translation': [tr_files[g]] + (['translation_supplement.md'] if g in ('0006_0053', '0078_0101', '0102_0125', '0126_0149') else []),
         'language': 'ar', 'state': 'read' if allread else 'read in part', 'read_share': share,
         'reading_review': {'grade': 'B', 'by': 'Claude (model), translation pass over every chain', 'date': '2026-11-27',
                            'reader_kind': 'model', 'independent': False,
                            'note': 'Every plaintext was read as sentences and translated into English; readings are model readings checked on the master TIFFs; no human Arabist has checked them; doubtful words are marked [?].'},
         'summary': summ[g]}
    texts.append(t)
o['texts'] = texts
o['key_file'] = ['keys.tsv']
json.dump(P, open('profile.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open('profile.json', 'a', encoding='utf-8').write('\n')
print(json.dumps({k: v for k, v in st.items() if k not in ('groups', 'keyed_ids', 'open')}, ensure_ascii=False))
print('open:', st['open'])
