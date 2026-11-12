# goulart1946: João Goulart to Ladislau Abreu, São Borja to Rio, March 1946 (catalogue 1488)

WAINUT, 12 Nov 2026. Work done with AI language-model agents viewing the images; no human reader has checked the
text. An independent AI language-model agent that took no part in the solve reviewed the folder blind (see
"Independent review" below).

Written up (integration, 12 Nov 2026) as docs/goulart1946.html. Read in part, 12 Nov 2026: 17 of 18 words read as sense; the one hole is
the boxed code word VIVILA, which is not on the filed code list.

## Document

- CPDOC/FGV, Arquivo Getúlio Vargas, **GV c 1946.03.09/2**: one telegram form of the Departamento dos Correios e
  Telégrafos, text on teleprinter strips. To LADISLAU ABREU, AVDA PRESIDENTE WILSON 113 9º ANDAR, RIO DF; from
  S. Borja by telephone (preamble `R 255 DE SBORJA ( TELEFONICA ) RS 20/29-30-9º-21H`); signed `JANGO`. Station
  stamp 1?.III.46, pencil receipt note 11/3/46; catalogue date 9 Mar 1946.
- Image: CPDOC DocReader, collection `CorrespGV3`, physical page 521:
  https://www.docvirt.com/docreader.net/docreader.aspx?bib=CorrespGV3&pasta=GV%20c%201946.03.09/2
- Text (20 words, matching the word count 20 in the preamble):
  `RESPEITO NOSSO NEGOCIO AVISE BARTOLOMEU PODE TRATAR / ASSUNTO SEM ASSUMIR COMPROMISSO PT ESTE DEPENDERA /
  NOVO ENTENDIMENTO VIVILA PT SAUDS = JANGO`. VIVILA is boxed in ink, with a pencil scribble under it inside the
  box; `Código` (?) is pencilled up the left margin.
- Preamble figures (a suggestion from the independent review, not checked further): the form's own legend gives the
  order "kind, station of origin, number, number of words, date and time of presentation". So `20/29` is probably
  20 text words and 29 chargeable words with the address, and `9º-21H` may be "the 9th, 21h", which would fit the
  catalogue date of 9 Mar 1946. `30` is unexplained.

## System

Open code (jargon), not a letter or figure cipher. The words are plain Portuguese; cover words stand for parties,
people and offices. Key: the typed list **GV c 1946/1950.00.00/5** in the same fonds, headed
'Cifra (Ladislau para João Goulart)' (CorrespGV3 pagfis 1852,
https://www.docvirt.com/docreader.net/docreader.aspx?bib=CorrespGV3&pasta=GV%20c%201946/1950.00.00/5). It has 25 typed
pairs written 'meaning -code' (P.T.B. -Sociedade, P.S.D. -Companhia, U.D.N. -Firma, P.C.B. -Empreza,
partidarios -socios, H.Borghi -Bartolomeu, ... Dutra -Manoel, Getulio Vargas -Varela, ...), ink additions on the
right (16 lines, direction not fixed), faint pencil at top right (read in part), and a pencil name after
Bartolomeu ('Ferreira' or 'Teixeira', perhaps a later replacement). Below the list is a set of stock phrases for
weekly telegrams from S. Borja to Alzira signed Maneco. Full transcription in `key.tsv`; the typed pairs only are
frozen in `key_frozen.tsv`.

The second key named in the catalogue, **GV c 1950.02.00/1** (3 pages, CorrespGV3 pagfis 4665-4667, Senado Federal
paper, 1950), is another code: first names for politicians (João = Dutra, Antonio = Góes, Ladislau = Jobim,
Fernando = Amaral, Raul = Brigadeiro, ...), car makes (Ford, Mercury, Chevrolet, Jeep) with assessments, and notes on
the 1950 succession. Transcribed in part in `key_1950.tsv`. It matches 0 of the telegram's 20 words
(`decryption_goulart1946_key1950.txt`).

## Key source and held-out test

The key is the filed list; it was not built from the telegram, so the whole telegram is held out. Result:

- Of the two words that stand out as code (BARTOLOMEU; VIVILA, boxed in ink by the recipient), **1 of 2 (50%)** is on
  the list. BARTOLOMEU = H. Borghi fits the date and the sense (Hugo Borghi, a PTB leader in São Paulo in early
  1946; 'tell him he may handle the matter without making any commitment').
- The 1950 list: 0 of 20 words.
- Search for a second text in the code (DocReader full-text OCR search of CorrespGV3, 12 Nov 2026):
  BARTOLOMEU 10 hits: this telegram (521), the code list (1852), and 8 personal names in newspapers and PTB lists
  (711, 1013, 1014, 2023, 2173, 2193, 2197, 2205; all 8 viewed). VARELA 6 hits: the code list (1852) and the real
  surname (946 list of Constituent Assembly members, 1070 newspaper, 4486 'Governador José Varela'; 2227 and 2242 not
  viewed). VIVILA 0 hits. No second text using the code was found, so there is no further test. OCR misses are
  possible (the search only finds what the OCR read).

## Reading

`reading_goulart1946.md`, `translation_goulart1946.md`:

> Respeito nosso negócio, avise {BARTOLOMEU=H. Borghi} pode tratar assunto sem assumir compromisso. Este dependerá
> novo entendimento |VIVILA|. {SAUDS/Saudações}. Jango.
>
> Regarding our business: tell H. Borghi he can deal with the matter without making any commitment. This will depend
> on a new understanding |VIVILA|. Regards. Jango.

Words (18, the two PT not counted): 15 verbatim from the strips, 1 code word resolved with the filed list, 1 marked
repair (SAUDS written out), 0 from a gloss, 1 hole (VIVILA). Sense 17/18 = 94.4%. Proposed state: **read in part**.
`scripts/check_marks.py` rebuilds the decryption from transcription and frozen key and passes; a tamper test
(BARTOLOMEU replaced without a mark) fails as it should.

Dan's reading checker (`docs/_check_reading.py`, origin/main 54c4ecc65, run in a throwaway worktree): on the
folder, clean share 0.353 (reading file, scored as English because of its English header), decryption 0/3 sentences
('not a reading', scored as French). On the text lines only, as Portuguese: 0/2 clean sentences, hole rate 0.375.
The holes it counts are VIVILA plus Portuguese words absent from its period word list (negócio, avise, assunto,
assumir, compromisso, dependerá, novo, saudações) and the name Jango; the list of missing words was checked word by
word in the independent review. The English translation scores 3/3 clean. So the checker does not confirm the
reading; the sentences are ordinary 1946 Portuguese telegraph style.

## Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solve read the full image and 2x crops of the strips before it
opened the transcription. It agrees on 20 of 20 text words, and on the preamble, address and service line. It re-ran
`scripts/decrypt.py` (same output, apart from BOM and line ends) and `scripts/check_marks.py` (pass), and its own
tamper test (BORGHI to BORGES, PODE to PODEM, unmarked) fails as it should. It read the text as sentences against the
translation: 3 of 3 clean (the second sentence has the one hole), and agreed on **read in part**, grade A. It found
no transcription error and asked for no change to the texts. Its points: complete the list of words missing from the
checker's word list (done above), give the preamble reading as a suggestion (done above), and keep the held-out claim
worded as resting on a single code word. It reads the faint pencil name after Bartolomeu on the code list as
'Ferreira', 'Ferraz' or 'Teixeira', unclear; none of the ink or pencil additions looks like VIVILA or NEGOCIO.

## Integration check (12 Nov 2026)

Checked before the write-up, by a reader who did not take part. Everything below was reproduced or looked at again; the
contributor's figures stand.

- **Image.** The telegram (CorrespGV3 pagfis 521) fetched again with `scripts/fetch_docreader.py` (no login, no captcha): the 20 text
  words, the address, the preamble and the service line agree with `transcription_goulart1946.txt`, as do the
  boxed VIVILA and the pencil notes. The typed list (pagfis 1852) fetched too: 25 typed pairs, spellings agree with
  `key_frozen.tsv`. The ink and pencil additions were not re-read (they are not used in the decryption).
- **Scripts.** `scripts/decrypt.py` and `scripts/check_marks.py` re-run: same decryption, PASS (18 words, 1 marked
  repair). With one code word the decoder is a one-line lookup; the integration did not write a second one.
- **Count.** 17 of 18 words = 94.4% by the read bar (BARTOLOMEU is on the list, so it counts as read; SAUDS is an
  abbreviation written out, not a supplied word; VIVILA is a hole). Under 95%: read in part. The same count holds if NEGOCIO
  is read as plain.
- **Key and test.** The list is headed 'Cifra (Ladislau para João Goulart)', the two correspondents of the
  telegram, in the other direction; its date is only known as 1946-1950. The key was not built from the telegram, so the
  whole telegram is held out, but the only test is one code-looking word of two (50%); the match of a common first name to
  a list entry rests on the sense. The page says so.
- **Catalogue.** Entry 1488 gave the telegram as 'Goulart -> Getulio Vargas'. The form is addressed to Ladislau Abreu (Rio,
  Av. Presidente Wilson 113); the entry leaves the catalogue with the correction (CATALOGUE.md). It carries no
  `decode_ids`, so there is no DECODE record to correct.
- **Not done here.** The ink and pencil additions of the list, the OCR searches of CorrespGV3 (taken from the notes), and a
  reading by a person who reads Portuguese.

## Remaining gaps

- VIVILA - blocker: no-key-material; boxed as code on the form, not on the typed list, not among the ink or pencil
  additions as read, not on the 1950 list, no OCR hit in the collection. Open. The scribble under it inside the box is
  not legible.
- NEGOCIO - blocker: no-key-material; read as the plain word ('our business'); it may itself be agreed jargon not on
  the list.
- Faint pencil on the code list - blocker: illegible; the four lines at the top right and the pencil name after
  Bartolomeu are read only in part (the name 'Ferreira', 'Ferraz' or 'Teixeira'; the independent review could not
  settle it either).
- Direction of the ink additions on the code list - blocker: too-short; 'leader = representante' against
  'crise = revolução' is not fixed, and no text in the code uses them.
- Held-out test and key coverage - blocker: too-short; no second text in this code was found, so both rest on one
  telegram and on a single code word (BARTOLOMEU).

Other open points, outside the coded text:

The preamble figures `20/29` and `9º-21H` have a suggested reading (see Document), not checked; `30` is unexplained.
The addressee Ladislau Abreu is not identified further here. Dan's reading checker does not pass the Portuguese text:
its period word list lacks negócio, avise, assunto, assumir, compromisso, dependerá, novo and saudações (and the name
Jango). A human reader of Portuguese would settle it.

## Escalation

- [x] siblings: the two code lists named in the catalogue (GV c 1946/1950.00.00/5 and GV c 1950.02.00/1) opened and
  transcribed; DocReader full-text search of CorrespGV3 for BARTOLOMEU, VARELA and VIVILA, every BARTOLOMEU hit viewed
- [x] clear-pages: no decipherment or gloss on the telegram form; the code list sheet read with its ink and pencil
  additions
- [x] known-keys: both keys tried: GV c 1946/1950.00.00/5 resolves 1 of the 2 code words, GV c 1950.02.00/1 none
- [x] print: web searches only (3 and 12 Nov 2026, see Prior art); no edition or decoding of the telegram found; the
  published Vargas letters of 1946-50 ('Volta ao Poder') are another series and were not searched for VIVILA
- [n/a] key-rebuild: open code; a cover word cannot be rebuilt from letters, VIVILA occurs once, and no second text
  in the code was found
- [x] retry: VIVILA checked again against the typed list, the ink and pencil additions and the 1950 list, by the solver
  and in the independent review

## Prior art (checked 12 Nov 2026)

- Catalogue vetting of 3 Nov 2026: not in DECODE, Tomokiyo or Lasry; no edition of the telegram; three Portuguese web
  searches found only biographies and PTB histories.
- One web search, 12 Nov 2026: "Vivila" with Vargas, Jango, Goulart, 1946: nothing on the term.
- Collision check, 12 Nov 2026: no target folder, open PR or issue for Goulart, Vargas 1946 or this shelfmark in
  dbourdeau/cyphersolver (origin/main log, `targets/`, `research/`, open PRs, issues searched for Goulart and Vargas).

## Method and access

Images fetched from the CPDOC DocReader by replaying the viewer's own image-load request (`scripts/fetch_docreader.py`),
searches by the viewer's own search and next-hit requests (`search_docreader.py`, `walk_hits.py`); one request at a
time, 2 s apart; no login and no captcha met. Sign conventions were written before the key was applied; the telegram
was transcribed twice (full image; fresh 2x crops), with no disagreement. Work by AI language-model agents for WAINUT;
no human reader checked the text. Scans are kept locally, not in git.
