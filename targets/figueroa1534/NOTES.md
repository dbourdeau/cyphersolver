# Gómez Suárez de Figueroa, Genoa: cipher letters 1534-1557 (catalogue 744)

Status: in progress

AGS Estado, legajos 1367-1386 (Génova), 20 PARES records listed in catalogue entry 744. Not on DECODE.

## Result of the first session (11 Nov 2026): prior art found, no ciphertext in hand

Catalogue 744 was entered as class C ("no key and no deciphered sibling is known"), and its vetting block says no
Tomokiyo page covers Figueroa's Genoa ciphers. That is wrong. Satoshi Tomokiyo's article *Spanish Ciphers during
the Reign of Emperor Charles V* (http://cryptiana.web.fc2.com/code/spanish2.htm) lists **18 of the 20 records by
their PARES number**, sorts them under four ciphers, and shows a reconstructed key for each (as images on his page):

| Cipher (Tomokiyo's name) | Items of 744 | Key state on Tomokiyo's page |
|---|---|---|
| Suárez de Figueroa's Simple Cipher (1529-1538), simple substitution, about 43 letters | 1367,56-57; 1367,149-150; 1369,232-233 | partly reconstructed (image `CharlesV1534.jpg`) |
| Figueroa-Philip Cipher (1543), vowel indicators | 1376,16-17 | reconstructed by Tomokiyo on this very letter, from the plaintext of the letter of 17 Nov 1543 (PARES 3561997) (`CharlesV1543.jpg`) |
| Imperial Cipher of 1544-1554, two series of syllables with vowel indicators | 1379,14-18; 1380,7-8; 1382,23; 1383,20-22; 1383,242; 1383,265-266; 1383,296; 1383,308-311; 1383,312; 1383,351-353; 1383,364 | reconstructed (Meister 1906; Bertomeu Masiá 2009; reorganised by Tomokiyo; `CharlesV2.jpg`, `CharlesV3.gif`) |
| Doria-Figueroa-Philip Cipher (1548), vowel indicators with heavy superscripts | 1380,9; 1380,10-11; 1380,37-38 | reconstructed from deciphered letters, two of them these items (`CharlesV1548.jpg`) |
| not in Tomokiyo's lists | 1386,1; 1386,92 (1557) | Tomokiyo says Figueroa wrote to the regent Juana in the Imperial Cipher of 1555 (Meister pp. 218-219, 283-284) and in Cg.1 of 1556 (his `spanish3.htm`); neither tested |

The item-by-item table, with Tomokiyo's dates and his notes ("undeciphered", "duplicate", "used in
reconstruction"), is `prior_art.tsv`.

What this means for the entry:

- The keys are in print. None of the 18 items needs a ciphertext-only attack; the method would be "read with known
  key" (1376,16-17; 1380,9; 1380,37-38, for which the key was published) or "read after matching with key from
  external sources".
- Tomokiyo publishes keys, not readings. He marks 1367,149-150, 1369,232-233, 1376,16-17, 1379,14-18 and 1380,10-11
  as undeciphered on the leaf; 1380,9 and 1380,37-38 carry or have a decipherment. For the rest he gives no note. No
  printed text of any of the 20 letters was found (search below). So the texts are, as far as found, still unread
  in print for most items, and the work left is transcription and applying the published keys.
- Catalogue 840 (EST,LEG,1380,151-154, PARES 3567239, memorandum to Eraso, 21 Jan 1549) is in Tomokiyo's list for
  the Imperial Cipher of 1544-1554 too.
- Tomokiyo dates 1367,56-57 to 2 Jul 1534; the frame check of 2 Nov 2026 read "Genoa 1535" on the leaf. Not settled.

Caveat as first written: Tomokiyo's page was read through WebFetch (a page-to-text reader), not as raw HTML.
That check has since been made (next section).

## Integration check (11 Nov 2026, review of PR #392)

- **`prior_art.tsv` checked against the raw HTML** of `spanish2.htm` (plain `curl` with a browser user agent
  answers 200; 121,365 bytes). All 18 PARES numbers are on the page, each under the cipher heading the table gives,
  with the date and recipient the table gives. The two 1557 records (3566204, 3568297) are not on the page.
  Catalogue 840's record 3567239 is there under the 1544-1554 cipher, dated 21 January 1549, to Francisco de Eraso.
  The "duplicate" notes on 1382,23 and 1383,265-266 were not re-derived (the page lists a second record of the same
  date next to 1382,23).
- **The five key images do download** when the request carries a browser user agent and the article as referer:
  `CharlesV1534.jpg`, `CharlesV1543.jpg`, `CharlesV2.jpg`, `CharlesV3.gif`, `CharlesV1548.jpg` under
  `https://cryptiana.web.fc2.com/code/`. They were fetched to confirm the route and not transcribed; writing them
  out as `key_*.tsv` is step 2 of the escalation and no longer blocked.
- **Tomokiyo's page source carries his own working notes** as HTML comments (`<!--Signatura: EST,LEG,... -->`):
  short syllable-by-syllable trial decipherments for eleven of the items here and for 840 (1380,7-8 about 70
  syllables; 1383,20-22; 1383,351-353; 1383,364; 1383,265-266; 1383,242; 1383,308-311; 1383,312; 1383,296;
  1382,23 "cinque ci ? mil escudos"; 1380,151-154). They are unpublished drafts, not readings, and are not copied
  here; they show the published keys do give Spanish on these letters, and they are prior work to credit and to
  compare against once the images are in hand.

## Prior-art search (11 Nov 2026)

- Tomokiyo, `spanish2.htm` and `spanish2A.htm` (the 1529 Figueroa-Charles V cipher, EST,LEG,1362): above.
- Tomokiyo's blog, 2 Oct 2020 ("Deciphered Letter to Emperor Charles V"): the 1529 letter only.
- *Documenti ispano-genovesi dell'Archivio di Simancas* (Genoa 1868): lists Figueroa despatches, some "in cifra"
  (one of April 1547); web search found no printed text for the 20 items. The volume itself was not opened.
- M. J. Levin, "A Failure of Intelligence: Gómez Suárez de Figueroa and the Fieschi Conspiracy, 1547": on the
  embassy, not the ciphers.
- M. J. Bertomeu Masiá, *La guerra secreta de Carlos V contra el Papa* (2009): source of the 1544-1554 key
  according to Tomokiyo; not opened.
- Estudios Románicos 34 (2025), Luo (2021), CODOIN: not searched this session.

## Remaining gaps

- **All 20 letters: no image, no transcription.** Blocker: access. PARES refused this session's machine on
  11 Nov 2026 (connection reset on `catalogo/description/<id>` and `catalogo/show/<id>`, HTTP 429 on the home page;
  four requests in all, then stopped). Earlier sessions reached PARES only through a Spanish exit
  (`research/vetting_2026-10/BRIEF.md`). Claude in Chrome was not available in this session.
- **Tomokiyo's five key images not transcribed.** No blocker since 11 Nov 2026 (they download with a browser user
  agent and referer, see the integration check); not done because no ciphertext is in hand to test them on.
- **1386,1 and 1386,92 (1557): cipher not identified.** Candidates named above, untested.

## Escalation

Not started: nothing was in hand. Next steps, in order:

1. From a machine PARES answers (Spanish exit, or Chrome): fetch the images of the 20 records (recipe in
   `targets/toledo1565/NOTES.md`), and the deciphered siblings Tomokiyo names (3561997 for 1543; the decipherments
   of 1380,9 and 1380,37-38).
2. Save Tomokiyo's key images and write each key out as a `key_*.tsv`; check each against a deciphered sibling.
3. Transcribe and decipher, starting with the items he marks undeciphered (1367,149-150; 1369,232-233; 1376,16-17;
   1379,14-18; 1380,10-11), then the eleven Imperial Cipher letters of 1547-1553.
4. Test the Imperial Cipher of 1555 and Cg.1 on the two 1557 letters.
5. Split entry 744 by cipher (one key per entry) once the images confirm Tomokiyo's assignment.

## Key validated on a held-out page (14 Nov 2026, Brice Dudout with Claude)

Images: the PARES records were fetched on Brice Dudout's machine (Spanish exit in earlier sessions). No AGS image is
in this folder ("Prohibida la reproducción"); the transcriptions here are of the cipher signs only.

**Key.** Imperial Cipher of 1544-1554 as published by Tomokiyo (after Bertomeu Masiá), completed for study only by
the period table AGS MPD D/00203 no. 243 ("Es del año de 1545", pointed out by Tomokiyo; issue #618). The table's
image is not reproduced here; the key as frozen, with the source of each value, is `validation/K4.tsv`. Values never changed after the key was frozen by SHA-256.

**Shape atlas.** Figueroa's secretary writes at about 1000 px on PARES, and the vowel marks (dot, two dots, bar,
small o) and several look-alike bases (X-bar = pre, x-stroke-o = de, sideloop = do, x-curl = no; eight / g / ring /
open j) were confused in our earlier passes. We built an atlas of 76 sign families, 337 crops, from the Biblioteca
Estense copy of Charles V to Ferrante Gonzaga, 14 Nov 1549 (Campori, Lettera K, Karl V sfasc. IV c. 60r/60v, IIIF,
CC BY-NC-SA), aligned on the sign names of `targets/gonzaga1549` (Daniel Bourdeau's names and recipe). The atlas
classes shapes only; it sets no values.

**Validation (pre-registered, one measurement).** Reference: AGS Estado 1379,14-18 (PARES 3615615), Figueroa to
Charles V, Genoa 8 Sep 1547. The unit holds the cipher (images 01-07) and a full clear copy of the time (images
11-17), so the letter itself is "existing"; it serves as the test. Held-out portion: cipher image 06, never looked
at before the freeze. Transcription by shape only, by three separate Claude sub-agents: pass A, pass B without
access to A (their own crops), arbitration on the image without values or clear text (passes agreed on 78 % of
signs; 492 tokens after arbitration). The clear copy (image 15) was read after the transcription was frozen.

| measure (character precision, LCS, scorer of earlier sessions) | value |
|---|---|
| decode vs clear copy of the time | **0.873** |
| 200 within-class shuffles (values permuted inside letters / syllables / codes / nulls), max | 0.477 |
| 200 whole-key shuffles, max | 0.449 |
| signs outside the key | 4.1 % |

Threshold set before: ≥ 0.85 and ≥ best within-class shuffle + 0.30 and ≤ 20 % outside the key: passed. The
within-class control is the harder one (whole-key shuffles move long code values onto frequent signs). Earlier
measurements with the same key family on other portions, without the atlas: 0.740 (1554), 0.783 and 0.795 (1547).

**Re-running it (15 Nov 2026, for the review of PR #621).** `validation/` holds the frozen files: the PREREG
(French, as frozen), the shape labels, the key table `K4.tsv`, the scorer `score_atlas.py` (and the earlier
`score_k4.py`), the arbitrated transcription of image 06, our transcription of the clear copy of the time, the
recorded output and the SHA-256 values. `sh validation/rerun.sh` checks the hashes and regenerates the recorded
output byte for byte (checked here, Python 3.9.6). No AGS image or crop is included (see `validation/README.md`).

**Second held-out measurement (15 Nov 2026), cipher image 04**, the last intact 1547 portion, now spent: same frozen rule and three blind sub-agents; with K4 unchanged **0.887** (best within-class control 0.554, margin +0.333; 13.8 % outside the key). A shape-split candidate K5 scores 0.879, but only one of its 8 new labels (po) occurs often enough to be tested. Since the ARB8e recount (last section) the readings use its labels where Brice Dudout's shape answers put them, and a word that needs one is probable at best. Files and `rerun.sh` (both measures, byte for byte): `validation/img04/`.

**1553 letters: decoded, not read.** See the next section.

## Five 1553 letters transcribed and decoded (14 Nov 2026, Brice Dudout with Claude)

Letters: 1383,242 (28 May, to Juan Vázquez de Molina, 1 p.), 1383,296 (29 Aug, 4 pp.), 1383,364 (30 Aug, 3 pp.),
1383,312 (20 Sep, 2 pp.), 1383,351-353 (27 Oct, 10 pp.), all from Figueroa in Genoa, the last four to Prince Philip.
20 pages, 12,741 signs (`transcriptions/`). Each page: pass A and pass B by two separate Claude sub-agents, blind to
each other and to all values; arbitration on the image by a third sub-agent, shape only (passes agreed on 44-80 % of
signs; the low figures come from line-numbering shifts, realigned on the image). The arbitrated transcriptions were
frozen by SHA-256 before decoding. Decode: the key frozen before the validation, unchanged (`readings/*_decode.txt`).

**Reading count (Daniel Bourdeau's rule: sure / probable / supplied / unread words; 95 % = read).** Holes are
counted by words (README, 14 Nov 2026): each unread passage in `readings/*_reading.txt` carries its size, `[... n]`,
estimated from the decode by the reading sheets' rule (max(1, round(decoded characters / 5)), an unlabelled sign or a
multiple value counting one character; a bare `[...]` is one word). Recounted on 15 Nov 2026 with the sized holes.
The strict figure is "sure only"; "sure + probable" is given for comparison, since the probable words rest on shape
pairs or post-validation conjectures.

| letter | sure only | sure + probable | unread words (sized) | `_check_reading.py` clean share (15 Nov) | state |
|---|---|---|---|---|---|
| 1383,242 (28 May) | 54 % (88 / 163) | 66 % | 53 | 0.133 | decoded, not read |
| 1383,296 (29 Aug) | 40 % (343 / 860) | 72 % | 230 | 0.329 | decoded, not read |
| 1383,364 (30 Aug) | 46 % (268 / 585) | 75 % | 139 | 0.229 | decoded, not read |
| 1383,312 (20 Sep) | 44 % (191 / 436) | 60 % | 173 | 0.366 | decoded, not read |
| 1383,351-353 (27 Oct) | 37 % (1,037 / 2,777) | 70 % | 824 | 0.285 | decoded, not read |

Under the schema's bar (coherent sentences, about 0.60 clean sentences), none is "read in part" yet: holes remain in
most sentences. "Probable" words need either a shape pair this hand merges at PARES resolution (r-series vs c-series,
`L-bar` me vs the closed "4" que, y-series s vs 7-series b/v, dot counts, triangle vs sideloop) or a post-validation
conjecture: a value given after the measurement to one of about 30 recurrent signs that the label table does not
name, kept only when it gives a clean word at least three times. Examples: a 6 joined to a small l-stroke = "al"
(alteza, al principe); an o with a long cross before `mo` = "ge" (Magestad); a dotted omega = "qua" (qual, quales);
`+` = "ne"/"ze" (manera, hazer); the u-shape before an h-series sign = "ch" (dicho, hecho). None of these is applied
to the key; they are listed so that high-resolution images can test them.

**What the letters say, as far as read** (words in square brackets are holes or supplied, not read). 29-30 Aug:
the French and Turkish fleets in Corsica (San Fiorenzo taken; the French fleet at Calvi, the Turkish one at
Bonifacio, "más de cien [...] de distancia"); the Genoese would not accept "su embaxador", and if they accepted him
"el rrey les [... 2] la Corcega" (the verb unread); whether the city has the forces to resist France ("esta ciudad
[...] tiene fuerças para rresistir", the word before tiene unread); dispatches go "por la via de Leon con cartas de
mercaderes" because of corsairs. 20 Sep: the Prince comes with 26 galleys and 2000 Germans (figures in clear); a
place surrenders on terms; the Genoese will bear half the cost of the enterprise of the island, "assi para la
seguridad de [...] tierra como para lo de [... 2] de Secilia y Cerdenia". 27 Oct: Bonifacio lost; the French mean to
arm up to 40 galleys and to call the galleys of Algiers (12 galleys, 18 galiots); the galleys of Naples and Sicily
sent for, after a report "del virrey [...] de Vega" (the first name is supplied, not read); a ceremony in the
cathedral ("yglesia mayor") to give the Prince a standard ("el estandarte de San [...]": the saint's name is a hole);
the Prince's office in the enterprise rests on holes and on a conjecture, so it is not claimed; money to be taken a
cambio. 28 May: changes, asientos, the Spinola, what remains owed. The contemporary Relaciones (1383,80-81, 89-91,
404) agree where they overlap.

**Prior work and collation.** Satoshi Tomokiyo's short drafts in the HTML comments of spanish2.htm agree with our
openings of all five ("lo que le puedo escrebir en esta", "por esta via de", "con cartas de mercaderes por las
qua[les]", "del presente", "mercaderes burgaleses"). 296 and 364 share the passage on the French ambassador; 242 and
351-353 share "a cambio". The duplicate 1383,308-311 (16 Sep) and 1383,265-266 (16 May) are not transcribed yet.

**Shape work since 14 Nov.** The 7 / y and 8 / ȣ shape pairs of this hand were separated on the images (atlas v4, v5), and the split classes were settled on shape sheets; the figures above are the first state. The recount on the ARB8e transcription is in the last section.

**Next.** AGS high-resolution reproductions (requested in Brice Dudout's archive register, 28 Oct 2026) would settle
the dots and the merged shapes; then test the conjectures on 1547 image 04, which is still untouched.

## Shape sheet 312e and the ARB8e recount (15 Nov 2026, Brice Dudout with Claude)

**Sheet.** Shape sheet 312e asked Brice Dudout, by shape only (one framed sign per question, option thumbnails without labels or values, dot count and a remark for each), for the 20 signs of the 1553 letters where a split shape class decides a word, plus 3 controls from the 1547 clear copy. The PREREG (decision rules for every answer, written before the answers) and the answer key were frozen by SHA-256 before the sheet was built. Controls: **3 / 3 shapes and 3 / 3 dot counts**, so the answers were applied as pre-registered. Answers, read literally (no remarks were written):

| targets | answer | effect |
|---|---|---|
| 5 ɏ-like signs in mañana, señores, campaña, España, enseñoreada | the closed "4" form (?Z4, 3 earlier supports for ñ: daño ×2, Señoría) | these words probable; with ≥ 3 such answers, ñ on this form counts as supported, and the other ñ words (señor …) become probable |
| 3 ɏ-like signs in Su Majestad ×2, sustentar | the "yr" form (su, K5 candidate) | words stay probable; blind re-label of all ɏ (below) |
| 4 X-bar signs (te / pre) | 2 × the barred triangle (te, K4), 2 × the te-form of X (K5) | "entendía" replaces "emprendía" (312); ternemos (364) sure; parte, tener probable; the re-label of all 82 X-bar was not triggered (1 of 3 needed) |
| 2 ꞓ signs | the 1545 table's cre sign (K4) | escrebí, escrebir sure (they agree with Tomokiyo's draft) |
| 2 dotted n | the n-with-dot (fa) | faltan, infantes probable; blind re-label (below); one of them was answered with 0 dots, noted |
| bo, ce, ne, po (4) | as expected | Bonifacio (312) probable; hazer, manera, propósito kept as probable |

**Blind re-labels.** Seven Claude sub-agents re-read, on the images, by shape only and with no values, every sign of the two classes that reached their pre-registered threshold (378 signs; reference rows of confirmed shapes, targets masked in the transcription). ɏ: the "yr" form on 16 of 281 (closed "4" on 20, not applied: that re-label was not pre-registered). Dotted n / caret: the n-with-dot on 33 of 97; all 32 earlier "dotted n" came back as n-with-dot and all earlier carets as carets except one. The new transcription ARB8e (the answers plus these re-labels) was frozen by SHA-256 before decoding. Key K4 unchanged; no measurement (no intact 1547 portion is left).

**Recount** (same strict rule; the readings were redone from the ARB8e decode and the holes sized again):

| letter | sure only | sure + probable | unread words (sized) | clean share | state |
|---|---|---|---|---|---|
| 1383,242 | 58 % (94 / 162) | 68 % | 50 | 0.333 | decoded, not read |
| 1383,296 | 47 % (384 / 812) | 80 % | 147 | 0.382 | decoded, not read |
| 1383,364 | 49 % (286 / 586) | 77 % | 129 | 0.407 | decoded, not read |
| 1383,312 | 53 % (236 / 445) | 70 % | 127 | 0.244 | decoded, not read |
| 1383,351-353 | 42 % (1,248 / 2,949) | 74 % | 703 | 0.346 | decoded, not read |

Against the first state: unread words 1,156 of 4,954 (1,419 of 4,821); sure only 42-58 % (37-54 %). Most of the gain comes from the 7 / y and 8 / ȣ separation; sheet 312e and the re-labels themselves add 14 read words net and remove 19 unread words (escrebí, escrebir, entendía, ternemos, mañana, señor, señores, campaña, España, Bonifacio, faltan, infantes, parte, tener …). The `_check_reading.py` clean share rises for four letters and falls for 312 (0.366 to 0.244) although its hole rate falls (0.321 to 0.254): the holes are fewer but spread over more sentences. No letter reaches 95 % or the sentence bar, so the states do not change.

Doubts kept: 351-353 img05 l. 1 "asentarse" (sure) has the "yr" form on its second sign by one sub-agent ("probable"); the reading is kept, not counted as changed. Same letter img05 l. 32, "se" became the "yr" form: the word is now an unread passage (perhaps "suplico", not read).

