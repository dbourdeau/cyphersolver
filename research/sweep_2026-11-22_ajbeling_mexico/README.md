# Mexico, 1830 and 1917: NARA M97 and Narváez 2019 sweep (2026-11-22)

Run by Andrew Beling (GitHub ajbeling) with AI agents (Claude, model `claude-opus-5-5`), from his own computer and
network, on 21 and 22 Nov 2026. Not a full sweep of an archive: two leads, one found on a National Archives microfilm
by following a footnote, one from a printed book. No person has checked the transcriptions. Nothing was solved.

## Routes

- **National Archives Catalog** (catalog.archives.gov): the catalog's own JSON search, then
  `/proxy/extractedText/189100166` (the catalog's machine reading of every frame of M97 roll 6), then the frame images.
  Free, no login, nothing blocked; 12 requests.
- **Roberto Sergio Rodríguez Narváez, *Criptografía diplomática, política y militar en México (1813-1926)*** (Mexico
  City: Secretaría de Relaciones Exteriores, Dirección General del Acervo Histórico Diplomático, 2019; ISBN
  978-607-446-152-7). Read from photographs of a library copy. The book is in copyright: no image or long passage of
  it is in this folder; pages and figures are cited instead. Its earlier article on the same military telegrams,
  Narváez, "Algunos ejemplos de criptografía militar mexicana (1860-1879)", *Historia Mexicana* 65:2 (2015), is open
  access.
- **Blocked:** historicas.unam.mx (the UNAM digital edition of Bosch García's documents on Butler) refused connections
  on 22 Nov 2026, from curl and from a web fetch.

## Finds

1. **Anthony Butler's letter of 30 Oct 1830 in "my private Cypher"** (row 1). M97 roll 6, frame 233. Ralph E. Weber,
   *United States Diplomatic Codes and Ciphers, 1775-1938* (1979), ch. 7 n. 31 (p. 204 as Narváez cites it), cites it for the words "my private
   cypher"; we found it on the film by paging the frames around Butler's papers of October 1830. One leaf, two pages,
   dated "Mexico 30 October 1830", "Dear Sir", unsigned. Plain English, with code numbers standing among the plain
   words from the second paragraph on: 55 numbers (43 different values, 1 to 614) and 4 signs. Nothing is written
   over the numbers or in the margins. Frames 232 and 234 were looked at and have no decipherment; frames 230-231
   were seen only at a glance and 235-236 only in the catalog's machine text, which shows none. Transcribed twice
   from the image, the second time blind; the readings that still differ (215 or 315, 110 or 116, 527 or 327, 525 or
   523, the cut-off group) are listed in our notes and are not given here as settled.
   - **A frozen test with three context probes missed.** A test against the State Department code of these years (1385 = the; Butler's
     own letters of 1834 use it), with its plan and the table frozen before the run, missed. Three context probes fixed
     before any look-up all failed (0 of 3), and no run of numbers reads as English. No number is above 660 (0 of
     54), where 65% of the numbers in Butler's 1834 letters in that code are; that the range would not fit was known
     when the plan was written, so only the probes are a real test. Nothing else was tried. The plan and result are
     held in our local files, not in this folder.
   - **Who it was written to is not established.** The endorsement below the text reads "Mr Butler / To J. S. M— /
     my private Cypher", closed by a bracket. Its second line is an abbreviation of a few letters ending in a capital
     M and a dash, not a written-out name; our two readings agree on "J. S. M—" and neither is sure of the first two
     letters. Narváez (p. 131 n. 46) reports that Weber read the initials "J. S. M." with a query, and himself reads
     the nearly complete name of the Briton O'Gorman; he describes the letter (p. 131, n. 45) as the second of two
     documents addressed to Charles Th. O'Gorman, Esq. What is certain: frames 230-232, just before it on the film,
     are copies of Butler's letters of 28 and 29 Oct 1830 to O'Gorman, the British consul general; the endorsement
     does not spell O'Gorman as we see it; and the letter asks its reader when "Mr Taylor" (the United States consul
     at Vera Cruz) is expected back and about articles to be forwarded from New York or Philadelphia, which reads as
     a letter to an American. We give the addressee as not established.
   - Narváez also writes that the two final paragraphs are wholly veiled. On the frame, the numbers are mixed with
     plain words in each of the last paragraphs; no paragraph is in numbers alone.
2. **F. J. Lobo, consul at Clifton, Arizona, to Ignacio Bonillas, 25 Nov (1916 or 1917)** (row 2). Narváez 2019,
   pp. 344-345, fig. 14 and nn. 48-49: two telegrams, of 25 and 26 Nov, that Bonillas could not decipher, in
   AHGE-SRE, Archivo de la Embajada de México en Estados Unidos, leg. 507, exp. 6, unfoliated. Bonillas asked Lobo on
   27 Nov (oficio A-743) whether his office had the "Murciélago" key. Narváez did not find Lobo's answer, and the
   "Murciélago" square printed in the book (fig. 8, p. 335) fails on the pictured telegram. Fig. 14 pictures the
   telegram of 25 Nov (three typed lines of five-letter groups); the one of 26 Nov is not pictured. The caption says
   1916, p. 345 says November 1917; the year is open. The row sorts under 1917, the year of the book's text. We have not transcribed the figure.

## Left out

- **Mexican military archive (AH-Sedena), carpeta 9288, 1869-1872** ("Telegramas en cifras cuya traducción se
  ignora", 18 telegrams from eight officers). Narváez 2019 p. 183 and *Historia Mexicana* 65:2 (2015) p. 848 say he
  deciphered 16 and gave the readings to the archive on 7 Dec 2013 (acknowledged by oficio S.H.-275, 5 Feb 2014); the
  book prints six. Neither text says which two were not deciphered, prints them, or gives their folios, and the
  folder is not online. Not specific enough for a lead; the next step is to ask the archive which two readings are
  missing from the 2013 deposit.
- Kerlérec's despatches (catalogue 829 and 830): already covered by `targets/kerlerec1759`.

## Duplicates and prior art (22 Nov 2026)

- **`known.py`**, at main `cec2f70fc`: 189100166, "Anthony Butler", O'Gorman, MP7157, Bonillas, Clifton, Murciélago,
  Murcielago, AEMEUA, "leg. 507": no hits. "M97" finds other M97 frames only (catalogue 650 and 653, the jqa and
  morris1813 targets); "Lobo" finds unrelated Portuguese and Spanish rows.
- **DECODE** keyword search (`decode_search.py`): Butler, O'Gorman, "Mexico 1830", Mexico, Bonillas, Lobo, Clifton,
  Murcielago: nothing relevant.
- **Cryptiana** snapshot `unsolved.htm`: no Butler, Lobo, Bonillas or Mexico.
- **Lasry and HistoCrypt:** no paper on either letter found; not searched beyond the web searches below.
- **Web:** Butler with "private cypher" and 1830 Mexico; Lobo, Clifton, Bonillas, "Murciélago" and "telegrama
  cifrado". Nothing beyond Weber and Narváez.
- **Editions:** Weber 1979 and Narváez 2019 print no reading of either. Carlos Bosch García, *Documentos de la
  relación de México con los Estados Unidos*, vol. II, *Butler en persecución de la provincia de Texas* (UNAM 1983),
  covers 31 Dec 1829 to 29 May 1836 from the Mexican and United States archives and may print the 1830 letter; it
  could not be opened (host refused connections). This is why row 1 has no vetting block.
- **Open issues and pull requests** searched for Butler, M97, Bonillas, Narváez, 9288: none on these letters.

## What is left

- Bosch García vol. II at 30 Oct 1830.
- More text in Butler's private cipher: his private letters of 1829-31 in the Van Buren and Jackson papers (Library of
  Congress). M97 roll 6 frames 214-229 and 237-247 were read only in the catalog's machine text, not as images.
- AHGE-SRE leg. 507 exp. 6: both Lobo telegrams, A-743 and any answer, to settle the year and look for a decipherment.
