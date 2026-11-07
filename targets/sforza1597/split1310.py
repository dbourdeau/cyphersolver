"""Split catalogue 1310 (Sforza cart. 1597, 59 cipher records) into per-sign-family leads, then promote them.
Groups are by sign hand, seen on full-page PDFs (6 Nov 2026); keys not yet matched, so groups may split further."""
import json, copy, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
cat = json.loads((ROOT/'catalogue.json').read_text(encoding='utf-8'))
leads = json.loads((ROOT/'research/leads.json').read_text(encoding='utf-8'))
old = next(e for e in cat['entries'] if e['id'] == 1310)
G = [
 ('A', [5425,5426,5427,5428,5429,5430],
  'dense full-page letters in one cursive Greek-looking hand (signs W, a barred divide, x, a lambda, 7), no word division, 12-20 lines each',
  4, 'whole letters in cipher; R5430 (cart. 130) repeats one 8-sign string four times, a name or title; R5425 and R5426 are the densest',
  'Transcribe R5430 (about 400 signs) and run a homophonic solver; compare with the cart. 1597 key sheets (none of nos. 1-60 uses these signs; nos. 61-114 not yet compared).'),
 ('B', [5420,5434,5438,5441,5450,5454,5455,5458,5466],
  'cursive letter-like signs (Greek capitals and minuscules, ligatured), short slips and full-page letters; several slips carry a "Cifra" note above the text',
  3, 'R5434, R5438, R5454, R5458 are short slips; R5441 and R5466 alternate clear Italian with signs; R5420 is a full page',
  'Group first by sign shapes (the family may hold two or three keys); the clear Italian between signs in R5441 and R5466 gives cribs.'),
 ('C', [5415,5417,5418,5424],
  'small sign hand built on o, oo, 8, 7 and a barred divide, in dense lines; R5415 has a few clear Latin or Italian words among the signs',
  3, 'R5415 has clear words among the signs; R5417, R5418 and R5424 are full pages',
  'Match to a key sheet by shape; if none, transcribe R5415 and use its clear words as cribs.'),
 ('D', [5416,5419,5456],
  'signs like a Gothic tt, 4, x, q and ligatured k (R5416, R5456) and a q/p/4 hand with a barred divide (R5419), full pages with no word division',
  3, 'R5416 and R5456 look like one hand; R5419 may be a second key',
  'Compare R5416/R5456 shapes against the key sheets, then split R5419 off if it does not share the alphabet.'),
 ('E', [5433,5435,5437,5443,5444,5445,5447,5457,5467],
  'geometric bar-and-cross signs (plus, inverted T, circle, pi, infinity, comb, "bus" sign), the style of the geometric cart. 1597 key sheets; short letters and slips, several with clear Italian between runs',
  4, 'R5433 and R5435 are short letters wholly in signs; R5437, R5443-R5445, R5457 and R5467 interleave clear Italian ("me pare", "mantova") with sign runs',
  'Compare with the geometric key sheets in nos. 1-114 (Cosimo, Antonio, Lancelotto, Raphael de Pugnellis and others); the clear words are cribs.'),
 ('F', [5459,5460,5463,5464,5465],
  'dense full-page letters in long bar, cross and infinity signs, no word division (R5463 and R5464 fill a whole sheet)',
  3, 'R5459 and R5460 are one hand; R5463, R5464 and R5465 are whole pages',
  'Compare with the geometric key sheets; transcribe R5460 first (shortest).'),
 ('G', [5422,5436,5440,5442,5446,5451,5452,5461,5472,5473,5474],
  'letters in clear Italian with cipher passages in several sign hands (letters-and-numerals in R5440, R5442; geometric signs in R5451, R5461; letters-and-numerals in R5472-R5474); clear text around the signs gives running cribs, and R5436 carries a clear text marked "da cifra"',
  4, 'R5436 is a clear leaf headed as a decipherment; R5472-R5474 are multi-page (3-4 pp.), the last two bound as register openings',
  'Decide for each passage which sign family it belongs to, then use the clear text as cribs; test R5436 against its cipher twin.'),
 ('H', [5448,5449],
  'abbreviation-like sign hand (ligatured c, a, e, n, m with tildes and bars, a comb), 15-20 lines',
  3, 'R5448 is burnt and torn at the top; R5449 is a complete letter',
  'Possibly a syllabic table; compare with the key sheets that carry bigram columns (Angelus cum cifra Vincentii, no. 14).'),
 ('I', [5453,5462],
  'minim-like letter signs, q, g, n, d, o and bars in R5453; d, o and numerals in R5462',
  3, 'R5453 is a dense page with signs in several lines; R5462 is almost all d and o with numerals',
  'Likely two different keys; confirm and split.'),
 ('J', [5380,5391,5439],
  'sign-and-numeral systems: R5380 is a page of repeated sign groups with numerals (a practice or key-sample sheet); R5391 and R5439 mix signs, digits and a few clear lines',
  3, 'R5380 may be a key or exercise sheet, not a letter; R5391 has a clear opening line and closing lines',
  'Check R5380 against the 114 key sheets as a key sample; R5391 and R5439 need a transcription.'),
]

base = max([e['id'] for e in cat['entries']] + [l['id'] for l in leads['leads']])
v0 = old['vetting']
new = []
for k, (tag, ids, hand, solv, folio, verify) in enumerate(G):
    nid = base + 1 + k
    nos = [i - 5300 for i in ids]
    e = copy.deepcopy(old)
    for f in ('scored', 'repository', 'outcome', 'in_progress'):
        e.pop(f, None)
    e['id'] = nid
    e['title'] = f"Sforza chancery letters in cipher, ASMi Carteggio Sforzesco cart. 1597, sign family {tag} ({len(ids)} records)"
    e['shelfmark'] = f"Archivio di Stato di Milano, Carteggio Visconteo-Sforzesco, cart. 1597 (Chiavi e cifrari), nos. {', '.join(map(str, nos))} (DECODE R{', R'.join(map(str, ids))})"
    e['folio_note'] = f"Sign hand: {hand}. {folio[0].upper() + folio[1:]}."
    e['status'] = ("Split from catalogue 1310 on 6 Nov 2026 (targets/sforza1597/): the 59 cart. 1597 cipher records are not one cipher. "
                   "Grouped here by sign hand on the full-page DECODE PDFs; the groups are a proxy for keys, not proven keys, and may split further once a key sheet is matched. "
                   "DECODE: status N/A, no metadata, no decipherment on the leaves.")
    e['verify'] = verify
    e['decode_ids'] = ids
    e['links'] = [{'label': f'DECODE R{i}', 'href': f'https://de-crypt.org/decrypt-web/RecordsView/{i}'} for i in ids[:4]]
    e['solvability'] = solv
    e['score_note'] = 'Scored from full-page PDFs of every record in the family, viewed 6 Nov 2026 (targets/sforza1597/)'
    e['access'] = 'online'
    v = copy.deepcopy(v0)
    v.update(date='2026-11-06', by='claude, split of catalogue 1310')
    v['seen'] = {'kind': 'scan',
                 'where': f"DECODE R{', R'.join(map(str, ids))}: full-resolution PDFs fetched and viewed 6 Nov 2026 (login cookie)",
                 'extent': f"{len(ids)} records, {sum(1 for _ in ids)} letters or slips of 1-4 pp.; {hand}",
                 'cipher': 'Sign-cipher text on the leaf; no decipherment written on or with it (the clear-text leaves in the box, R5421, R5423, R5468, are letters, not decipherments).'}
    v['key_check'] = ("The 115 key sheets of the same cartella (DECODE R5301-R5414, R5469-R5471) were fetched and the first 60 viewed: they are 18th-century copies headed with correspondent names, "
                      "with geometric signs; none was matched to this family's letters, and no transcription was made.")
    v['key_in_volume'] = 'cart. 1597 nos. 1-114 and 169-171 (DECODE R5301-R5414, R5469-R5471); not yet matched to this family.'
    v['duplicates'] = ("Split from catalogue 1310 (same box); DECODE records R5380-R5474 are not in any other catalogue entry; related Sforza ciphers in BnF ital. 1583 (targets/it1583, visconti1446) use different alphabets.")
    v['verdict'] = 'open'
    e['vetting'] = v
    new.append(e)
print('base', base, [(e['id'], len(e['decode_ids'])) for e in new])
if '--write' in sys.argv:
    cat['entries'] = [e for e in cat['entries'] if e['id'] != 1310]
    leads['leads'].extend(new)
    for path, d in (('catalogue.json', cat), ('research/leads.json', leads)):
        (ROOT / path).write_text(json.dumps(d, ensure_ascii=False, indent=1) + chr(10), encoding='utf-8')
    print('written')
