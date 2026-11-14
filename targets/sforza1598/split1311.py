"""Split catalogue 1311 (Sforza cart. 1598/1591, 110 cipher records) into per-sign-family leads, then promote them.
Groups are by sign hand, seen on full-page PDFs (14 Nov 2026, text strips at 110 dpi); keys not yet matched, so groups may split further."""
import json, copy, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
cat = json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'))
leads = json.loads((ROOT/'research/leads.json').read_text(encoding='utf-8'))
old = next(e for e in cat['entries'] if e['id'] == 1311)
G = [
 ('A', [5488,5528,5579,5581], 'geometric bar signs (T, inverted T, triple bar III, infinity, U, barred d, m with bar), word-spaced runs, full pages', 4, 'R5579 and R5581 are full pages in one hand; R5488 and R5528 match sign for sign', 'Transcribe R5579 (one clean page) and solve; compare with the geometric key sheets of cart. 1598.'),
 ('B', [5562,5572,5573,5575,5576,5577,5586], 'letter-like signs x, double-cross, 3, m with bar, pp, k, 7, no word division', 4, 'slips and half pages, several pinned together; R5577 has a clear docket strip', 'Pool the seven slips (one hand) and run a homophonic solver.'),
 ('C', [5502,5503,5504,5505,5506,5514,5515,5517,5518], 'numerals 4, 6, 8 with crossed and inverted-T signs, b, p, f, dense; clear Italian or Latin openings ("Illustrissime princeps ...", "quando", "sempre quella")', 5, 'nine letters of 1-2 pp. in one hand, with clear phrases between runs (cribs)', 'Largest family: transcribe and solve jointly; clear phrases between runs are cribs.'),
 ('D', [5495,5496,5497,5498,5499,5507], 'lambda, 3, bz ligature, L with dot, triple circle ooo, pi, double-bar =, phi', 4, 'short letters and slips; R5498 is three slips', 'Pool and solve; frequent groups (22 ooo, 3 phi L) look like word signs.'),
 ('E', [5520,5523,5535,5537,5541], 'm with divide, infinity, pi, barred P, beta, dotted colon signs', 3, 'short letters (8-12 lines)', 'Pool and solve.'),
 ('F', [5555,5556,5559,5563], 'v, divide, infinity, plus, tilde-o, barred 9, Greek-like H, with some clear text (R5563)', 3, 'R5563 is mostly clear with a cipher run; R5556 has a second slip', 'Pool and solve; use R5563 clear context as crib.'),
 ('G', [5516,5519,5522], 'x, inverted-T with stroke, 4, 3, theta, lambda, slashes; clear Italian between runs in R5516 and R5522', 3, 'full letters with clear passages', 'Clear text gives cribs; pool and solve.'),
 ('H', [5551,5561], 'cursive letter-like signs with m l, z 3 o, double slash //', 3, 'R5551 is damaged; R5561 is short', 'Pool and solve.'),
 ('I', [5500,5553], 'cursive pseudo-Latin letters (a b f, long s, barred o), superscript letters', 3, 'full pages', 'Pool and solve; letters may be a shifted alphabet.'),
 ('J', [5490,5493], 'cursive pseudo-Latin letters with b z, r b, Z', 3, 'R5490 one page with address leaf; R5493 one page in paragraphs', 'Pool and solve.'),
 ('K', [5511,5512,5513], 'numeral-like signs 7, 5, 3, 9, 8 with a z-like sign and dots', 3, 'short letters', 'Pool and solve.'),
 ('L', [5564,5565,5582,5583,5584], 'ta, delta, square, double-cross, A f k, H x, superscript letters', 4, 'short letters; R5582 is two leaves', 'Pool and solve.'),
 ('M', [5486,5487,5530], 'bz ligature, inverted T, infinity, lambda, hash, square bracket signs; R5487 and R5530 have clear openings', 3, 'R5486 and R5487 signed by the same hand', 'Pool and solve; clear openings as cribs.'),
 ('N', [5568,5574], 'hash, 8, inverted T, T, phi, barred d', 3, 'R5568 three slips; R5574 one page', 'Pool and solve.'),
 ('O', [5524,5529], 'V, hash, 8, barred p, inverted T, crossed f', 3, 'full pages', 'Pool and solve.'),
 ('P', [5521,5542], 'to, delta, 3 n, q o, oo in short word-like groups', 3, 'full pages', 'Pool and solve.'),
 ('Q', [5482,5485], 'code: capital letters with superscript numbers (H30, A13, M2, e39) and single signs; R5485 clear Italian with coded runs', 3, 'R5482 one page signed Idem; R5485 two pages, 16th-century hand', 'Codebook needed or rebuilt from repeats and the clear context of R5485.'),
 ('Z', [5297,5298,5476,5480,5501,5532,5533,5484,5489,5492,5508,5509,5510,5526,5527,5531,5534,5536,5538,5539,5540,5543,5544,5545,5546,5547,5548,5549,5550,5554,5558,5560,5567,5570,5571,5580,5585,5587], 'single letters each in a sign hand not matched to another letter of the box (numerals, Greek-like, geometric and pseudo-Latin hands)', 3, 'many interleave clear Italian or Latin with cipher runs (R5297, R5510, R5531, R5534, R5536, R5543, R5567)', 'Split further when a key sheet is matched; start with the clear-context letters as cribs.'),
]

base = max([e['id'] for e in cat['entries']] + [l['id'] for l in leads['leads']])
v0 = old['vetting']
new = []
for k, (tag, ids, hand, solv, folio, verify) in enumerate(G):
    nid = base + 1 + k
    nos = [('1591 no. %d'%(i-5234)) if i<5400 else str(i-5474) for i in ids]
    e = copy.deepcopy(old)
    for f in ('scored', 'repository', 'outcome', 'in_progress'):
        e.pop(f, None)
    e['id'] = nid
    e['title'] = f"Sforza chancery letters in cipher, ASMi Carteggio Sforzesco cart. 1598, sign family {tag} ({len(ids)} records)"
    e['shelfmark'] = f"Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, cart. 1598 (cart. 1591 where marked), nos. {', '.join(map(str, nos))} (DECODE R{', R'.join(map(str, ids))})"
    e['folio_note'] = f"Sign hand: {hand}. {folio[0].upper() + folio[1:]}."
    e['status'] = ("Split from catalogue 1311 on 14 Nov 2026 (targets/sforza1598/): the 110 cart. 1598/1591 cipher records are not one cipher. "
                   "Grouped here by sign hand on 110-dpi text strips of the DECODE PDFs; R5481, R5483, R5494, R5525, R5552, R5557, R5566, R5569, R5578 are clear or nearly clear leaves and are left out; the groups are a proxy for keys, not proven keys, and may split further once a key sheet is matched. "
                   "DECODE: status N/A, no metadata, no decipherment on the leaves.")
    e['verify'] = verify
    e['decode_ids'] = ids
    e['links'] = [{'label': f'DECODE R{i}', 'href': f'https://de-crypt.org/decrypt-web/RecordsView/{i}'} for i in ids[:4]]
    e['solvability'] = solv
    e['score_note'] = 'Scored from full-page PDFs of every record in the family, viewed 14 Nov 2026 (targets/sforza1598/)'
    e['access'] = 'online'
    v = copy.deepcopy(v0)
    v.update(date='2026-11-14', by='claude, split of catalogue 1311')
    v['seen'] = {'kind': 'scan',
                 'where': f"DECODE R{', R'.join(map(str, ids))}: full-resolution PDFs fetched and viewed 14 Nov 2026 (login cookie)",
                 'extent': f"{len(ids)} records, {sum(1 for _ in ids)} letters or slips of 1-4 pp.; {hand}",
                 'cipher': 'Sign-cipher text on the leaf; no decipherment written on or with it (the clear leaves in the box are letters, not decipherments; the Da cifra reading of the vetting note was not confirmed).'}
    v['key_check'] = ('The 93 key sheets of cart. 1598 (DECODE R5235-R5611, record_type 2) and the 115 of cart. 1597 were fetched; none has yet been compared with this family, and no transcription was made.')
    v['key_in_volume'] = 'cart. 1598 key sheets (93 DECODE key records, list in targets/sforza1598/list1598.json); not yet matched to this family.'
    v['duplicates'] = ('Split from catalogue 1311 (same box); sibling box cart. 1597 is catalogue 1310, split into ids 2399-2408 (targets/sforza1597); no shared DECODE records.')
    v['verdict'] = 'open'
    e['vetting'] = v
    new.append(e)
print('base', base, [(e['id'], len(e['decode_ids'])) for e in new])
if '--write' in sys.argv:
    cat['entries'] = [e for e in cat['entries'] if e['id'] != 1311]
    leads['leads'].extend(new)
    for path, d in (('catalogue.json', cat), ('research/leads.json', leads)):
        (ROOT / path).write_text(json.dumps(d, ensure_ascii=False, indent=1) + chr(10), encoding='utf-8')
    print('written')
