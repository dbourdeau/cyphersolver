"""Build profile.json for visconti1446 from the per-slip files in texts/. Counts are measured from texts/f<n>_tokens.tsv
(nulls = {null}/{null?}; unread = any [..]) and texts/f<n>_signs.txt (docs/_check_profile.py --measure). Rerun after
any change to a slip:  python targets/visconti1446/make_profile.py   (from the repository root)
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
T = os.path.join(HERE, 'texts')
G = 'https://gallica.bnf.fr/ark:/12148/btv1b100373864'

# folio, date, year, place written, canvas/DECODE, clear text (location, source) or None, independent?, summary
SLIPS = [
 (110, '1 Nov 1446', 1446, 'Milan', 'DECODE R7902 (recto, verso)', ('separate collection', 'BnF ital. 1597 (Gallica btv1b10037396j) f. 123r-v, canvases 126-127: 19th-c. copy made by deciphering this slip'), False,
  'After the rout of his army the Duke gives up his grudge: Sforza’s kind brief has changed his mind, he will never act against Sforza’s state, offers to pay his provision if Venice stops it and to send horse at his own cost, except against the Church and the King of Aragon, and asks for a quick conclusion.'),
 (130, '25 Nov 1446', 1446, 'Milan', 'DECODE R7904', None, True,
  'Sforza\'s brief of 14 November came by Perino da Cotignola; Cosimo de\' Medici has always been well disposed; the Duke begs Sforza to come at once and dispose of the men-at-arms and of his own person, and to say whether he will stay in the Marche or come to Lombardy. The contemporary translation f. 131 exists but was not reached.'),
 (136, '29 Nov 1446', 1446, 'Milan', 'DECODE R7907', ('separate collection', 'BnF ital. 1597 (Gallica btv1b10037396j) f. 154, canvas 157: 19th-c. copy made by deciphering this slip'), False,
  'The Duke sent Giovanni del Maino to Sforza with full powers the day after his letter of the 15th, but Sforza\'s men-at-arms in Cremona and the Cremonese have gone over to the enemy camp; it is more honourable to win than to sit in winter quarters.'),
 (154, '12 Dec 1446', 1446, 'Milan', 'DECODE R7914 (recto, verso)', None, True,
  'Donino has come from Sforza; the Duke is sending Pietro da Pusterla and Antonio da Trezzo to him secretly, awaits answers from the Pope and King Alfonso, and begs Sforza to conclude at once and in secret; letters are to go secretly through Cotignola.'),
 (158, '31 Dec 1446', 1446, 'Cusago', 'DECODE R7915', None, True,
  'After the rout of his men-at-arms the Duke sent Thomase to France for help: nothing but words from the Duke of Savoy, but the Dauphin is willing, and Asti has been offered to him in return; the Duke asks Sforza\'s opinion.'),
 (5, '10 Jan 1447', 1447, 'Abbiategrasso', 'Gallica canvas 9', ('separate folio', 'f. 6, "Traduzione" of the time on the same mount; f. 7 later copy'), False,
  'Reply to Sforza\'s letters and Pietro da Pusterla\'s: the Duke has worked to keep the Marquis of Mantua from Venice; if Rolando Pallavicino comes to terms with Venice he only does his duty; the Duke will follow Sforza\'s advice.'),
 (8, '11 Jan 1447', 1447, 'Abbiategrasso', 'Gallica canvas 11', ('separate folio', 'f. 9, "Traduzione" of the time on the same mount; f. 10 later copy'), False,
  'The Duke asks Sforza to send one of his most trusted men, seemingly as if he had left Sforza\'s service, through whom Sforza will know everything done at court, since nothing is to be done without his consent; even the Duke\'s worst enemy will do.'),
 (24, '5 Feb 1447', 1447, 'Milan', 'Gallica canvas 24 (lower slip)', ('separate folio', 'f. 25, contemporary decipherment; f. 26 later copy (found after the reading)'), True,
  'Answer to Sforza\'s brief brought by Fra Benedetto da Valenza: the report from Cremona of a proclamation sparing Cremona is untrue and malicious; the Duke approves Sforza\'s writing to Cremona; on Foschino\'s request through Pietro Visconti at Pizzighettone.'),
 (23, '5 Feb 1447, duplicate of 24 Feb', 1447, 'Milan', 'Gallica canvas 24 (upper slip)', ('separate folio', 'f. 25, contemporary decipherment; f. 26 later copy (found after the reading)'), True,
  'The same letter as f. 24, enciphered afresh with other homophones and re-sent on 24 February ("duplicata die vigesimo quarto eiusdem").'),
 (30, '9 Feb 1447', 1447, 'Milan', 'Gallica canvas 30', ('separate folio', 'f. 29, later clear copy (made from f. 31)'), False,
  'Ser Battista, chancellor of the castellan of Castel Sant\'Angelo, has come to Sforza for the Cardinal Camerlengo; the Duke is delighted and urges Sforza to deal with men trusted by the "Signori", since the Camerlengo can do everything with the Pope.'),
 (31, '9 Feb 1447, duplicate of 24 Feb', 1447, 'Milan', 'Gallica canvas 30', ('separate folio', 'f. 29, later clear copy made from this slip'), False,
  'The duplicate of f. 30, re-sent on 24 February.'),
 (36, '12 Feb 1447', 1447, 'Milan', 'Gallica canvas 34', ('separate folio', 'f. 38, contemporary decipherment; ff. 35r-v, later copy'), False,
  'Asti is to be given to the Dauphin; Rolando Pallavicino; the missions of Gasparo degli Ubaldini and Giovanni del Maino; Cosimo de\' Medici to urge Sforza to an agreement; a rumour that Sforza has renewed his pact with Venice hampers the raising of money.'),
 (37, '12 Feb 1447, duplicate of 25 Feb', 1447, 'Milan', 'Gallica canvas 34', ('separate folio', 'f. 38, contemporary decipherment; ff. 35r-v, later copy'), False,
  'The duplicate of f. 36, re-sent on 25 February.'),
 (64, '6 Mar 1447', 1447, 'Milan', 'Gallica canvas 62', ('separate folio', 'f. 63, later clear copy'), False,
  'Venetian troops have crossed the Oglio into the Cremonese to take Cremona; the Duke has sent Carlo Gonzaga, Alberto Pio and Conte Carlo with their men and the river fleet, and ordered Pietro Visconti at Pizzighettone to help save the town.'),
 (65, '6 Mar 1447, duplicate of the same day', 1447, 'Milan', 'Gallica canvas 62', ('separate folio', 'f. 63, later clear copy'), False,
  'The duplicate of f. 64, sent the same day.'),
 (72, '7 Mar 1447', 1447, 'Milan', 'Gallica canvas 69', ('separate folio', 'f. 73, later clear copy (found after the reading)'), True,
  'Answer to four briefs of Sforza and a letter of Marcolino Barbavara: on binding himself to the Church and the King of Aragon Sforza should do as seems best and tell Marcolino; Pietro da Pusterla has gone to Ferrara; a request brought by Angelo Simonetta.'),
 (83, '11 Mar 1447', 1447, 'Milan', 'Gallica canvas 80', ('separate folio', 'f. 84, contemporary decipherment; ff. 82r-v and 85r, later copy'), False,
  'The Dauphin and Asti through Tommaso da Bologna; Rome and the Cardinal Camerlengo; Padua or Verona offered to the Duke of Ferrara; the Malatesta condotte; the Count of Urbino\'s planned raid; discontent in Milan with the agreement.'),
 (94, '18 Mar 1447', 1447, 'Milan', 'Gallica canvas 91', ('separate folio', 'f. 95, contemporary decipherment; f. 92 (pencil 93), later copy'), False,
  'The Duke is glad Sforza sent Messer Nicola Maffeo; praises his letters to the College of Cardinals and the governor of the March and the truce with the Malatesta; asks how he should write from now on.'),
 (102, '23 Mar 1447 (duplicate)', 1447, 'Milan', 'Gallica canvas 98 (upper slip)', ('separate folio', 'f. 103, contemporary decipherment; f. 101 later copy (found after the reading)'), True,
  'The new pope, Nicholas V, will not do what he ought; Sforza should come to an understanding with the King of Aragon and act before the pope sets his feet more firmly.'),
]


# word agreement of the readings made before the clear text was found (texts/compare_clear.py): exact / with spelling variants
AGREE = {23: '65.4% / 83.2%', 24: '64.4% / 84.1%', 72: '72.8% / 88.3%', 102: '70.2% / 87.5%'}


def counts(n):
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, f'f{n}_tokens.tsv'), encoding='utf-8')]
    rows = [r for r in rows if len(r) >= 3 and r[0] != 'line']
    tot = len(rows); nul = sum(1 for r in rows if r[2] in ('{null}', '{null?}'))
    unr = sum(1 for r in rows if '[..]' in r[2])
    return tot, nul, unr


def measure(n):
    out = subprocess.run([sys.executable, os.path.join(ROOT, 'docs', '_check_profile.py'), '--measure',
                          os.path.join(T, f'f{n}_signs.txt')], capture_output=True, text=True, encoding='utf-8').stdout
    return json.loads(out)


docs, texts, gaps = [], [], []
T_all = N_all = U_all = 0
for f, date, year, place, img, clear, indep, summ in SLIPS:
    tot, nul, unr = counts(f); T_all += tot; N_all += nul; U_all += unr
    share = (tot - nul - unr) / (tot - nul)
    m = measure(f)
    sampled = f in (83, 94)
    state = 'read' if (share >= 0.95 or (clear and not indep and (share >= 0.9 or f in (83, 94)))) else 'read in part'
    docs.append({
        'id': f'f{f}', 'shelfmark': f'BnF italien {1583 if year == 1446 else 1584} f. {f} ({img})', 'date': date, 'year': year,
        'country': 'Duchy of Milan', 'route': f'Filippo Maria Visconti, Duke of Milan ({place}) -> Francesco Sforza',
        'places': {'from': place, 'to': 'Pesaro'},
        'language': 'Italian', 'pages': 2 if f in (110, 154) else 1, 'cleartext_in_document': 'none',
        'plaintext': ({'location': [clear[0]], 'source': clear[1], 'partial': False} if clear else
                      {'location': ['none'], 'source': 'no decipherment or clear text reached; deciphered here with key R5323', 'partial': True}),
        'length': {'tokens': m['tokens'], 'distinct': m['distinct'], 'unit': 'symbols', 'measured': True, 'file': f'texts/f{f}_signs.txt'},
        'transcription': {'by': 'llm from images',
                          'source': ('DECODE image (low resolution)' if year == 1446 else 'Gallica IIIF full-size canvas'),
                          'image_quality': 'fair' if year == 1446 else 'good',
                          'notes': (f'sample only ({m["tokens"]} tokens): the rest of the text is the later clear copy, checked on the sample'
                                    if sampled else f'{tot} tokens, {nul} nulls, {unr} unread; {share:.1%} of non-null tokens read')},
        'read': 'read in part' if state == 'decoded, not read' else state})
    t = {'doc': f'f{f}', 'label': f'f. {f}, {place}, {date}', 'transcription': f'texts/f{f}.md',
         'decryption': (f'texts/f{f}_clear.md' if sampled else f'texts/f{f}_reading.md'),
         'translation': f'texts/f{f}_en.md', 'state': state, 'summary': summ,
         **({} if state == 'decoded, not read' else {'reading_review': {'grade': 'A' if state == 'read' else 'B', 'by': 'claude-opus-5-5', 'date': '2026-10-29',
                            'note': (f'made before the clear text was found; words agree with it {AGREE[f]} (exact / with spelling variants)' if f in AGREE else 'coherent; checked against the clear text' if clear else
                                     'coherent with scattered holes' if state == 'read' else 'sentences hold where read; holes in several sentences')}})}
    texts.append(t)

fr = (T_all - N_all - U_all) / T_all
profile = {
 'schema_version': 1, 'target': 'visconti1446',
 'title': 'Filippo Maria Visconti to Francesco Sforza, cipher slips of Nov 1446 - Mar 1447 (BnF italien 1583, 1584; key DECODE R5323)',
 'documents': docs,
 'system': {
  'types': ['homophonic', 'syllabic', 'nomenclator'],
  'summary': 'Homophonic substitution (up to six signs a letter) with a full table of vowel+consonant syllable signs, twelve word signs, about fourteen name signs and twelve nulls; no word division; each slip ends with the date, the ducal title in cipher and an alphabet-run padding.',
  'symbol_kind': 'letters and symbols', 'distinct_symbols': max(d['length']['distinct'] for d in docs),
  'diacritics': {'used': True}, 'homophones': {'used': True},
  'nomenclator': {'present': True, 'kinds': ['syllables', 'common words', 'names', 'titles']},
  'nulls': {'present': True, 'count': 12}, 'key_order': 'partly alphabetical', 'word_division': 'none',
  'sibling_key': "The Duke's second key, ASMi cart. 1597 no. 24 (DECODE R5324), reads one slip of the same series (f. 15, targets/visconti1447)."},
 'conditions': {
  'prior_solution': {'exists': 'partial', 'where': 'contemporary decipherments on the next leaf of eight of the eleven ital. 1584 letters (ff. 6, 9, 25, 38, 84, 95, 103) and of ital. 1583 f. 130 (f. 131, not digitised); later fair copies of every ital. 1584 letter (ff. 7, 10, 26, 29, 35, 63, 73, 82/85, 92, 101); 19th-c. copies of ital. 1583 ff. 110, 136 and 145 in BnF ital. 1597, made by deciphering the slips. None known for ff. 154 and 158.', 'found': 'during attempt', 'used': True},
  'inputs': ['images', 'key from archive', 'cleartext context'], 'attack': 'key from archive',
  'human_role': 'The project chose the target from the Oct 2026 Venice/Milan sweep and asked for the slips to be read; the model found the key, mapped the volumes, and transcribed and deciphered the slips through worker subagents, checked by the main session.',
  'tools': ['Gallica IIIF image API', 'BnF Archives et manuscrits records (arks)', 'DECODE authenticated record and image download', 'PIL tiling, deskew and baseline tracking', 'show-through removal by registered mirror division (f. 110 verso)', 'lang/ Italian word search'],
  'models': ['claude-opus-5-5'], 'sessions': 2, 'first_date': '2026-10-28', 'last_date': '2026-10-29'},
 'solution': [
  {'date': '2026-10-28', 'kind': 'literature search', 'what': "Mazzatinti's inventory of BnF ital. 1583-1593 marks 21 of the Duke's letters 'In cifre: membran.', three with a translation after them.", 'result': 'worked'},
  {'date': '2026-10-28', 'kind': 'access', 'what': "Gallica blocks scripts; the openapi.bnf.fr IIIF image API serves ital. 1584 full size. The ark recorded for ital. 1583 is a 1456 volume, so its six slips were taken from DECODE R7902-R7915.", 'result': 'partial'},
  {'date': '2026-10-28', 'kind': 'key from source', 'technique': ['key matching'], 'what': "Re-fetched the 15th-c. key records of ASMi Carteggio Sforzesco cart. 1597 (R5301-R5340) and read the headings; no. 23 (R5323) is headed 'Filippo Maria Duca di Milano'. f. 8 line 1 deciphers sign for sign to its translation f. 9.", 'result': 'worked'},
  {'date': '2026-10-28', 'kind': 'verification', 'technique': ['plaintext matching'], 'what': 'ff. 8 and 5 deciphered and compared token by token with the translations ff. 9 and 6: 96.9% and 96.5% agreement; differences are the translator normalising Lombard spelling.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'reading', 'technique': ['contextual inference'], 'what': 'ff. 30/31, 36/37, 64/65 deciphered (95.5-98.9%); each pair is one letter sent twice. Their later clear copies (ff. 29, 35, 63) were found first and were in view.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'reading', 'technique': ['contextual inference'], 'what': 'ff. 23/24, 72 and 102 deciphered with no clear text; the two encipherments of ff. 23/24 fill each other; padding identified at the end of each slip.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'verification', 'technique': ['plaintext matching'], 'what': 'Samples of ff. 83 and 94 deciphered first, then compared with their later clear copies: 99.2% and 98.5%; Mazzatinti\'s "copia moderna" f. 92 is the text of f. 94.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'reading', 'technique': ['contextual inference', 'language-model scoring'], 'what': 'ital. 1583 ff. 130, 136, 158 deciphered from the DECODE images (88-92%); ff. 154 and 110 read in part after baseline-tracked re-transcription and, for the f. 110 verso, removal of the recto show-through.', 'result': 'partial'},
  {'date': '2026-10-29', 'kind': 'literature search', 'what': 'Web search for an edition or decipherment of the slips or of the Duke\'s keys: none found; Cerioni 1970 covers the later Sforza period.', 'result': 'failed'},
  {'date': '2026-10-29', 'kind': 'key from source', 'technique': ['key matching'], 'what': 'A parallel session found the same key a second time on DECODE R1857 image 17 (ASMi Potenze Sovrane cart. 1592, "Filippo Maria Duca di Milano") and calibrated it on ff. 5/8 against ff. 6/9 (96.7% / 97.8%); its corrections are in peer/working_key.md. Tomokiyo had tied R1857 (image 11) to ital. 1584 f. 69 only.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'access', 'what': 'The BnF Archives et manuscrits record for ital. 1583 gives only microfilm MF 16151: the volume is not digitised (the ark btv1b10033686w is ital. 1587). The "Copie moderne di documenti" volumes are: ital. 1597 btv1b10037396j, 1598 btv1b10037380f.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'access', 'what': 'ital. 1597 canvases 116-182 hold 19th-c. copies numbered with the ital. 1583 document numbers: f. 110 (canvases 126-127), f. 112, f. 136 (canvas 157), f. 145 (canvas 160); none of ff. 130, 154, 158. The f. 110 copy writes gi for the cipher group II+3 and leaves the blank name sign blank: it was made by deciphering the slip.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'reading', 'technique': ['plaintext matching'], 'what': 'f. 110 re-transcribed line by line at 3.5-8x and aligned with the ital. 1597 copy: recto 96.5%, verso 69.6% of non-null signs (this folder\'s blind pass had read 32%). f. 136 likewise: 95.7%; the blind pass (91.5% by sense) matches the copy on only 68% of words.', 'result': 'worked'},
  {'date': '2026-10-29', 'kind': 'control', 'technique': ['language-model scoring'], 'what': 'lattice.py: beam search over candidate values for the glyph classes the binarized DECODE scans do not separate, scored with it-cinquecento order 5, tried on f. 136 where the copy fixes every value: 70 of 126 ambiguous signs right (55.6%). Not applied.', 'result': 'failed'},
  {'date': '2026-10-29', 'kind': 'verification', 'technique': ['plaintext matching'], 'what': 'The survey of ital. 1584 by the parallel session showed that ff. 23/24, 72 and 102, read here as having no clear text, have one: f. 25 and f. 103 are contemporary decipherments, f. 73 a later copy (f. 103 had been taken for a parallel letter and used as a guide to sense in the f. 102 retry). Transcribed and compared: word agreement 83-88% with spelling variants, 64-73% exact.', 'result': 'partial'},
  {'date': '2026-10-29', 'kind': 'literature search', 'what': 'Osio, Documenti diplomatici tratti dagli archivj milanesi III (1872) prints agents\' reports, Sforza to the Duke of 12 Dec and the Pusterla procuration of 22 Dec 1446, none of the Duke\'s cipher letters.', 'result': 'failed'}],
 'outcome': {
  'class': 'read in part',
  'method': 'read after matching with key from external sources',
  'method_basis': "The key is an unlabelled DECODE key record (ASMi cart. 1597 no. 23, R5323) matched to the slips and checked against two contemporary translations.",
  'parts': [
   {'label': 'ital. 1583 ff. 130, 154, 158 (no clear text reached)', 'method': 'read after matching with key from external sources', 'extent': 'partial'},
   {'label': 'ital. 1584 ff. 5, 8, 23/24, 36/37, 83, 94, 102 (contemporary decipherments), 30/31, 64/65, 72 (later copies); ital. 1583 ff. 110, 136 (19th-c. copies in ital. 1597)', 'method': 'read from existing decipherment', 'extent': 'complete'}],
  'contribution': ['transcription', 'catalogue correction', 'sender or date identified'],
  'key': 'not applicable',
  'fraction_read': round(fr, 3), 'fraction_read_method': 'measured',
  'fraction_read_source': 'texts/f*_tokens.tsv, all cipher tokens of the 19 slips (nulls counted as not read; ff. 83 and 94 sampled)',
  'verification': ['contemporary decipherment', 'independent clear copy', 'key confirms', 'historical consistency'],
  'first_break': False, 'provenance': 'project',
  'notes': f'{T_all} tokens transcribed, {N_all} nulls, {U_all} unread. Sixteen of the nineteen slips have a decipherment of the time or a later copy (ital. 1584 next to each slip; ital. 1583 ff. 110 and 136 in ital. 1597); only ff. 130, 154 and 158 are deciphered here with no clear text reached. ff. 110 and 136 were merged from a parallel session. f. 15 (key R5324) is written up as visconti1447.',
  'credits': [
   {'who': 'contemporary', 'role': 'prior solution', 'note': 'decipherments ff. 6, 9, 25, 38, 84, 95, 103 (and f. 131, not digitised); later copies ff. 7, 10, 26, 29, 35, 63, 73, 82/85, 92, 101 and, in ital. 1597, of ff. 110, 136, 145', 'date': '1447'},
   {'who': 'decode', 'role': 'key or decipherment used', 'note': 'key record R5323 (ASMi cart. 1597 no. 23), uploaded 2023; slip images R7902-R7915', 'date': '2023-07', 'source': 'https://de-crypt.org/decrypt-web/RecordsView/5323'},
   {'who': 'mazzatinti', 'role': 'identification', 'note': 'inventory entries for the 21 slips', 'date': '1883', 'source': 'Mazzatinti, Inventario delle carte dell\'archivio sforzesco, Archivio storico lombardo 1883'}],
  'gaps': [
   {'item': 'f. 110 verso (1 Nov 1446): 231 signs run together on the binarized DECODE image (the 1597 copy gives the sense)', 'blocker': 'illegible'},
   {'item': 'f. 154 (12 Dec 1446): parts of 14 lines', 'blocker': 'illegible'},
   {'item': 'ff. 130, 158: scattered stretches', 'blocker': 'illegible'},
   {'item': 'f. 72: the name signs < and est (the later copy f. 73 leaves < blank too)', 'blocker': 'open-codes'},
   {'item': 'ital. 1583 f. 145 (1 Dec 1446; its 19th-c. copy is ital. 1597 canvas 160) and the translation f. 131: ital. 1583 is not digitised (microfilm MF 16151)', 'blocker': 'needs-physical-access'}],
  'texts': texts, 'key_file': 'key.md'}}

json.dump(profile, open(os.path.join(HERE, 'profile.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{len(docs)} documents; {T_all} tokens, {N_all} nulls, {U_all} unread; fraction_read {fr:.3f}')
