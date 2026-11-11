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
