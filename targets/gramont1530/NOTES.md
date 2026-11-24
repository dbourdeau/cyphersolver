# Gramont, cardinal, Rome, to Montmorency, 21 July 1530 (BnF fr. 3071 no. 7; catalogue item 6, Gramont's cipher 1530)

BnF fr. 3071 no. 7, f. 17 (Gallica btv1b9060315f, canvas 30). Read in the session of 18 Sept 2026 under
`targets/gramont1529/`.

**Split on 14 Oct 2026 from `gramont1529`** under the one-key rule (George Lasry): catalogue item 6 grouped four
letters to Montmorency in four different keys. This entry is the one letter in **"Gramont's cipher (1530)"**. The
others are different ciphers, each with its own page: Gramont 1529 (`gramont1529`), Langeac 1529 (`langeac1529`) and
the Mâcon letter of 1537, now in `rome1536` with the cardinal's other letters in Mascon's cipher.

## Key and result

* Key: Lasry's "Gramont's cipher (1530)" (cryptiana GL.htm, `GL/BnF_fr3071_f17.png`, dated 04/11/2023 on the image;
  copy `img/BnF_fr3071_f17.png`), with Tomokiyo's partial table from the sibling fr. 3019 f. 20
  (`img/francisGramont.png`). Substitution with 2-7 homophones per letter, LL/RR/SS signs, COM/CON signs; Lasry
  lists five signs as unknown. Lasry also decoded the letter in 2023, unpublished (his correction of 21 Sept 2026).
* `fr3071_no7_gramont.md`: about **85 %** of the 14 cipher lines read (an estimate; no alias file was kept). The
  Pope keeps "Francisque" on the mission rather than Gramont, for fear of Imperial suspicion; Rodolfo Pio, bishop
  of Faenza and nephew of Carpi, is to leave in 3-4 days to congratulate the King on the return of the Queen and
  the princes. Dated by that return (Bidassoa, 1 July 1530).
* Three of Lasry's unknown signs identified: 8Δ = PAPE, key-ring sign = ROY, ʃʃ-on-stem = word-initial null. (Superseded by the 14 Nov 2026 block below: two identified, pape and roy; the ʃʃ null is not confirmed.)

Other letters in this key, not read here: fr. 3019 f. 20 and fr. 3040 ff. 12, 18 (the key's siblings), and Gramont to
Villandry, fr. 2980 nos. 21-22 (catalogue 328, open).

## Remaining gaps
- four signs without a value, each once: ʃʃ and Z̄ (line 1, between *le* and *vouloir*), # (line 2, between *iamais* and *ie suis*), ▣ (line 2, *dev[▣] execution*; X in Lasry's table, which does not fit) - blocker: no-key-material; ʃʃ, Z̄ and # are among Lasry's five unknown signs; no gloss, clear copy or decipherment of the letter exists; the other letters in this key are where they could be fixed

Not gaps in the cipher, but open: the transcription is a single AI pass, not checked by a person against the image (three doubtful signs: L09 ñ?, L10 λ?, L11 ß?; the words they stand in read); and the clear close of the letter, in secretary hand after the cipher block, is still transcribed only in fragments (not re-read on 14 Nov).

## Escalation
- [x] siblings: fr. 3019 f. 20 and fr. 3040 ff. 12, 18 are the key's sources (Tomokiyo, Lasry); fr. 2980 nos. 21-22 (catalogue 328) is in this key and still open, a source for the unknown signs
- [x] clear-pages: the clear opening and close of f. 17 read; no decipherment on the leaf
- [x] known-keys: Lasry's Gramont 1530 table and Tomokiyo's fr. 3019 f. 20 table applied
- [x] print: Tomokiyo francis.htm, Lasry GL.htm: keys only, no plaintext
- [x] key-rebuild: 8Δ = pape and key-ring = roy from context (18 Sept); 4t = et, COM sign = con-/com- (14 Nov)
- [x] retry: 14 Nov 2026, sign-by-sign transcription of the leaf and mechanical decode (below); 532 of 536 signs read

## Assumptions for George's review

- His prior-solution credit rests on his note of 21 Sept 2026 that he decoded all four item-6 letters in 2023.
- The key-or-decipherment credit here is for his "Gramont's cipher (1530)" table only.

## 14 Nov 2026, full-texts audit: the cipher transcribed and re-decoded

The audit asked for the cipher as written; the first reading (18 Sept) was made by eye and kept no transcription.

- Looked first for an existing one: none in the folder, none in `targets/gramont1529/` named for this leaf, Lasry's
  2023 decipherment is unpublished. So the leaf was fetched from `openapi.bnf.fr` (IIIF, btv1b9060315f view 30,
  4352 x 6081 px; gallica.bnf.fr itself was not used) and transcribed on native-resolution strips.
- `texts/gramont1530_transcription.txt`: **13 cipher lines** (the earlier files say 14), **536 signs** (552 tokens by
  `_check_profile.py --measure --drop-first`, less 16 separator marks). Shape labels are matched to Lasry's table by
  column and row. A single AI transcription, not checked by a person; the header lists the look-alike pairs.
- `texts/gramont1530_decode.md`: the mechanical decode with Lasry's table. It gives continuous French over the whole
  block; 532 of 536 signs take a value. New from the decode: `4t` reads *et* at its four places (the table has the
  shape under S); the COM sign writes *con-* and *com-*; four signs have no value (ʃʃ, Z̄, #, ▣).
- What it changes in the 18 Sept reading: line 2 was a gap, now *ie suis apres pour le faire mectre a dev[.]e
  execution*; *recepvoir* is *concepvoir*; *pource [...] commancement [le pape] a trouvé bon* is *pource commancement
  [pape] trouve bon* (no gap, no *a*); lines 6-7 were a gap, now *y aille seul pour scavoir quel il y faict, et me
  semble qu'il n'i a que rien* (the sign is the table's R: *bien* is not carried); *d'aultant qu'estant yci*; *se aller
  congratuller*. The 18 Sept note that ʃʃ is a word-initial null is not confirmed: it stands between *le* and Z̄.
- `fr3071_no7_gramont_reading.md` and `fr3071_no7_gramont_en.md`: the cipher block rewritten from the decode.
  Read share 0.961 (245 words, 10 holes; 0.933 before). `fr3071_no7_gramont.md` is left as the record of the first reading.
- profile.json: texts entry gets the transcription, the decode, state **read in part -> read**, a reading review;
  `fraction_read` **0.85 (estimated) -> 0.993 (measured, 532/536 signs)**; length 536 signs; gaps replaced.
  `outcome.class` is left at *read in part*: raising it is the maintainer's call, since no person has checked the
  transcription. "About 85 %" and "14 lines" in the paragraphs above are the 18 Sept state.
