import json
P='https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/'
common=dict(language='Spanish',region='Spain',access_note='images online on PARES (free reuse, cite Ministerio de Cultura/PARES URL)',needs_archive_scan='no',seen='scan')
rows=[
dict(year=1811,date='2 Jun 1811 (file 16 May-2 Jun 1811)',title='Cipher dispatches and symbol-cipher key from a confidant in Seville on the French occupation (Soult, Napoleon, Joseph, Mazona/Massena, Victor, Mortier named in the key)',
 correspondents='anonymous Spanish confidant in French-occupied Seville -> Spanish authorities (Cadiz Regency / Junta), unknown',place='Seville',
 period='1801-1900',shelfmark='AHN, ESTADO,3010,Exp.10',folio_note='9 images; key sheet on image 1, symbol-cipher pages images 2-6+ (marginal "Soult" notes only)',cls='A',
 status='PARES catalogue: "Criptograma y mensajes cifrados remitidos por un confidente en Sevilla, sobre la ocupacion de la ciudad por las tropas francesas". Viewed images 1-6 on 9 Nov 2026: image 1 is a key sheet (alphabet with symbol equivalents, 15 nomenclator symbols for Napoleon, King Jose, Marshals Massena, Victor, Mortier, Soult etc.), images 2-6 are pages of solid symbol-cipher text with a few plain marginal names; no interlinear plaintext. Not in known.py. Two web searches (Spanish/English) found no edition or decipherment.',
 why='A 1811 Peninsular War intelligence cipher in invented symbols with the key in the same file: a key-known read with a nomenclator, a rare case for the Spanish side of the war.',
 importance=3,solvability=5,difficulty=2,score_note='Seen on PARES images 9 Nov 2026; key sheet in the file',
 verify='Transcribe key sheet (image 1) and decode pages 2-6; check the rest of the 9 images and ESTADO,3010 neighbours (Joseph Bonaparte government papers).',
 links=[{'href':P+'5040064','label':'PARES 5040064 (ESTADO,3010,Exp.10)'}],
 source='PARES diversos 19th c sweep, 9 Nov 2026 (research/sweep_2026-11_pares_diversos_19c)',
 prior_art='open as far as checked (9 Nov 2026): known.py on ESTADO,3010 finds nothing; 2 web searches found nothing; not in Scovell/Oman lists (French ciphers) since this is a Spanish confidant cipher.'),
dict(year=1812,date='14-25 Feb 1812',title='Anonymous numeric cipher letter (about 2 pages) enclosed with a letter on the reward for drawing up accounts, Cadiz 1812 (Baena papers)',
 correspondents='unnamed correspondent at Cadiz -> duke of Baena (letter mentions the ambassador and General Antonio Bayon)',place='Cadiz',
 period='1801-1900',shelfmark='AHNOB, BAENA,C.38,D.267-268',folio_note='6 images: plain letter images 1-3, numeric cipher on images 4-6 (2-digit numbers 1-28 joined by dots, no spaces)',cls='A',
 status='PARES: "Acompana una carta cifrada" (2 documents). Viewed images 1-5 on 9 Nov 2026: plain letter dated Cadiz 14 Feb 1812, then a "No 2" sheet and a second page of dotted numbers between 1 and 28 (alphabet-sized range, one value 1 or 14 very frequent, probably a simple substitution with nulls), no plaintext above or below. known.py finds nothing for BAENA,C.38 or the record id. Two web searches found nothing.',
 why='A short simple-looking numeric substitution from Cadiz during the Cortes, a good ciphertext-only target; frequency of the repeated "14"/"28"/"22" groups suggests a monoalphabetic cipher over about 28 values.',
 importance=2,solvability=4,difficulty=2,score_note='Seen on PARES images 9 Nov 2026',
 verify='Transcribe images 4-6 and attempt a monoalphabetic solve (Spanish, 28 symbols).',
 links=[{'href':P+'6354614','label':'PARES 6354614 (BAENA,C.38,D.267-268)'}],
 source='PARES diversos 19th c sweep, 9 Nov 2026 (research/sweep_2026-11_pares_diversos_19c)',
 prior_art='open as far as checked (9 Nov 2026): known.py nothing; 2 web searches nothing.'),
dict(year=1866,date='Jan-Feb 1866',title='Copybook of orders and reports to colonel Taulet during the January 1866 rising, with short numeric cipher passages in his reports',
 correspondents='Lieutenant colonel Bernardo Taulet (Catalonia/Maestrazgo columns) -> captain general of Catalonia / chiefs of columns',place='Barcelona / Tarragona province',
 period='1801-1900',shelfmark='AHN, DIVERSOS-COLECCIONES,193,N.99',folio_note='53 pages; hyphenated 2-digit number groups seen in the reports on images 25-26 (also earlier)',cls='A',
 status='PARES: "Hay algunos documentos cifrados". Viewed images 1-6, 13-18, 25-30 on 9 Nov 2026: plain order-book copies and daily reports (Jalet/Abella/Villarroya) with short passages of hyphenated 2-digit groups (e.g. 61-64-22-...) set into the plaintext; no interlinear decipherment. Not in known.py (Taulet nothing). Web search: nothing on Taulet or this unit.',
 why='19th-century Catalan military cipher in numbers, in an otherwise clear context, so cribs are available; no Carlist-war pair among those already read.',
 importance=2,solvability=3,difficulty=3,score_note='Seen on PARES images 9 Nov 2026; cipher passages are short',
 verify='Transcribe the numeric passages (images 25-30 and others), compare with the plain context of each day report.',
 links=[{'href':P+'5928106','label':'PARES 5928106 (DIVERSOS-COLECCIONES,193,N.99)'}],
 source='PARES diversos 19th c sweep, 9 Nov 2026 (research/sweep_2026-11_pares_diversos_19c)',
 prior_art='open as far as checked (9 Nov 2026): known.py nothing; 1 web search nothing.'),
]
for r in rows: r.update({k:v for k,v in common.items() if k not in r})
json.dump(rows,open('candidates.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(rows))
