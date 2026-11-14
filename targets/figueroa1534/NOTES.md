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
the period table AGS MPD D/00203 no. 243 ("Es del año de 1545", pointed out by Tomokiyo; issue #618). The table is not
reproduced here. Values never changed after the key was frozen by SHA-256.

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

**1553 letters: decoded, not read.** See the next section.

## Five 1553 letters transcribed and decoded (14 Nov 2026, Brice Dudout with Claude)

Letters: 1383,242 (28 May, to Juan Vázquez de Molina, 1 p.), 1383,296 (29 Aug, 4 pp.), 1383,364 (30 Aug, 3 pp.),
1383,312 (20 Sep, 2 pp.), 1383,351-353 (27 Oct, 10 pp.), all from Figueroa in Genoa, the last four to Prince Philip.
20 pages, 12,741 signs (`transcriptions/`). Each page: pass A and pass B by two separate Claude sub-agents, blind to
each other and to all values; arbitration on the image by a third sub-agent, shape only (passes agreed on 44-80 % of
signs; the low figures come from line-numbering shifts, realigned on the image). The arbitrated transcriptions were
frozen by SHA-256 before decoding. Decode: the key frozen before the validation, unchanged (`readings/*_decode.txt`).

**Reading count (Daniel Bourdeau's rule: sure / probable / supplied / unread words; 95 % = read).**

| letter | words read as sense | sure only | `_check_reading.py` clean share | state |
|---|---|---|---|---|
| 1383,242 (28 May) | 66 % | 54 % | 0.375 | decoded, not read |
| 1383,296 (29 Aug) | 75 % | 42 % | 0.239 | decoded, not read |
| 1383,364 (30 Aug) | 75 % | 46 % | 0.250 | decoded, not read |
| 1383,312 (20 Sep) | 60 % | 44 % | 0.206 | decoded, not read |
| 1383,351-353 (27 Oct) | 72 % | 38 % | 0.144 | decoded, not read |

Under the schema's bar (coherent sentences, about 0.60 clean sentences), none is "read in part" yet: holes remain in
most sentences. "Probable" words need either a shape pair this hand merges at PARES resolution (r-series vs c-series,
`L-bar` me vs the closed "4" que, y-series s vs 7-series b/v, dot counts, triangle vs sideloop) or a post-validation
conjecture: a value given after the measurement to one of about 30 recurrent signs that the label table does not
name, kept only when it gives a clean word at least three times. Examples: a 6 joined to a small l-stroke = "al"
(alteza, al principe); an o with a long cross before `mo` = "ge" (Magestad); a dotted omega = "qua" (qual, quales);
`+` = "ne"/"ze" (manera, hazer); the u-shape before an h-series sign = "ch" (dicho, hecho). None of these is applied
to the key; they are listed so that high-resolution images can test them.

**What the letters say, as far as read.** 29-30 Aug: the French and Turkish fleets in Corsica (San Fiorenzo taken;
the French fleet at Calvi, the Turkish one at Bonifacio, "more than a hundred miles" apart); Genoa cannot hold the
island alone and refused the French king's ambassador; the French seem to offer Corsica back if Genoa takes him;
dispatches go "por la via de Leon con cartas de mercaderes" because of corsairs. 20 Sep: Doria comes with 26 galleys
and 2000 Germans (figures in clear); a place surrenders on terms; the Genoese will bear half the cost of the
enterprise of the island, "assi para la seguridad de su tierra como … de Secilia y Cerdenia". 27 Oct: Bonifacio lost;
the French mean to arm 40 galleys and to call the galleys of Algiers (12 galleys, 18 galiots); galleys of Naples and
Sicily sent for (Juan de Vega); Andrea Doria named general of the enterprise of Corsica, with a ceremony of the St
George standard in the cathedral; money to be taken a cambio. 28 May: changes, asientos, the Spinola, what remains
owed. The contemporary Relaciones (1383,80-81, 89-91, 404) agree where they overlap.

**Prior work and collation.** Satoshi Tomokiyo's short drafts in the HTML comments of spanish2.htm agree with our
openings of all five ("lo que le puedo escrebir en esta", "por esta via de", "con cartas de mercaderes por las
qua[les]", "del presente", "mercaderes burgaleses"). 296 and 364 share the passage on the French ambassador; 242 and
351-353 share "a cambio". The duplicate 1383,308-311 (16 Sep) and 1383,265-266 (16 May) are not transcribed yet.

**Next.** AGS high-resolution reproductions (requested in Brice Dudout's archive register, 28 Oct 2026) would settle
the dots and the merged shapes; then test the conjectures on 1547 image 04, which is still untouched.
