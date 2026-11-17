# Printed editions sweep: HathiTrust full text and Colonial Office transcripts (2026-11-17)

Run by Andrew Beling (GitHub `ajbeling`) with Claude Code agents (Claude Opus, Claude Sonnet) on 16-17 Nov 2026. No
person has checked any of it. Nothing here is deciphered except where a test is reported as failed. The rows follow `research/archive_sweep_2026-10/BRIEF.md`;
this pull request adds this folder only (CONTRIBUTING.md: "as a pull request with nothing else in it"), so the merge
into `research/leads.json`, the coverage update and the index row are left to the maintainers.

**Result: 18 rows in `candidates.json`, none with a `vetting` block.** Two are printed ciphertexts (the numbers are set
in type and the editor says they are unread); sixteen are manuscript leads where an edition or calendar says a passage
is in cipher and was not deciphered, but does not print it. The duplicate check was run on origin/main da9b4c93c
(17 Nov 2026) and run again on 7d9b91fb8 (22 Nov 2026: `known.py` on the distinctive names, a search of
`research/leads.json` and `catalogue.json` for each row's names and years, and `merge.py` restricted to this folder,
which reports 18 rows, 18 new): no row is covered. Seen means seen in the printed edition (`seen: "print"`): no manuscript was viewed for any row.

| # | Year | Item | Holder (as the source gives it) | Cipher |
|---|---|---|---|---|
| 0 | 1703 | duc de Bourgogne → Philip V, 21 and 28 Jan | Alcalá, now AHN Madrid (inference); printed Baudrillart and Lecestre I pp. 21, 26 | **353 numbers printed**, key lost; transcription here |
| 1 | 1650 | Willem Frederik of Nassau-Dietz → William II, letters 937, 944, 950 | printed Groen van Prinsterer 2e sér. IV pp. 336-354 | 133 numbers printed; the 950 passage bare |
| 2 | 1781 | Holker No. 12 and enclosure → Castries | AN AE B I 945 ff. 116-126 | letter partly, enclosure wholly |
| 3 | 1781 | Oster → [La Luzerne], 3 Oct | AN AE B I 945 ff. 132-133 | whole letter |
| 4 | 1781 | Barbé-Marbois No. 20 → Castries, 10 Nov | AN AE B I 945 ff. 150-159 | "a major portion" |
| 5 | 1782 | Létombe → Castries, Boston, 20 Feb and spring | AN AE B I 209 ff. 149-150, about 153-154 | parts |
| 6 | 1688 | Hoffmann → Leopold I, London, 13 Aug | HHStA Vienna | a passage, "Schlüssel fehlt" |
| 7 | 1538 | Miniato Ricci → Parisani, Corfu, 30 Sep | Archivio Ricci, vol. X p. 138 | closing lines, "senza chiave" |
| 8 | 1540 | papal nuncio at Ferdinand's court, 1540 and 1541 | Naples, Carte Farnesiane 738 (copy) | two passages; a printed key to try |
| 9 | 1832 | Simon Deutz → Massa, for the Duchess of Berry, Lisbon | autograph, whereabouts unknown | invisible-ink figures |
| 10 | 1546 | report to Ulm, Schmalkaldic war | Stadtarchiv Ulm (inference) | two passages |
| 11 | 1630 | Casale letter (Mazarini to F. Barberini: inference) | not named | four lines |
| 12 | 1650 | Hyde → Toby Mathew | Clarendon MSS (inference) | "the remainder" |
| 13 | 1525 | letters to Castiglione's circle, 1525-26 | "filza 160" | three passages |
| 14 | 1807 | French consul in Egypt (Drovetti: inference) | consular series (inference) | three lines |
| 15 | 1594 | Henri IV → Bellièvre | BnF manuscripts | two lines |
| 16 | 1644 | d'Estrades, The Hague | AE CP Hollande 33 f. 216 | one line |
| 17 | 1627 | Zucconi → Cesare Gonzaga, intercepted | not located | many lines, partly deciphered then |

Each row's `status`, `prior_art` and `verify` give the editor's words, what was checked and the next step. Facts taken
from another research note and not checked again by us are marked "reported, not re-checked by us".

## What was searched

### HathiTrust full text (three sessions, 16-17 Nov 2026)

Phrase searches across the full-text index (`babel.hathitrust.org/cgi/ls`, phrase mode), then in-volume searches and
the text-only page view (`/cgi/ssd`) to read each hit; about 195 page loads in all, at one load every 30 seconds or
more after the first session drew a 429 at its 82nd load (about 2.6 loads a minute). Nothing was downloaded from
HathiTrust; the Bourgogne pages were read on the Internet Archive copy.

Phrases, with result counts (all volumes / full view where both were recorded):

- English: "the remainder is in cipher" 11/11; "cipher undeciphered" 319/222; "cypher undecyphered" 57/47; "not
  decyphered" 284/197; "in cipher and not deciphered" 11/8; "undeciphered cipher" 64/54; "cypher not decyphered" 40;
  "lines in cipher" 331/236; "words in cipher" 1,055/745; "no key to the cipher" 112/91; "cipher which has not been"
  26/21; "cipher has not been" 101; "to which there is no key" 670/493 (too broad); "could not be deciphered" 7,035
  (too broad); "key has been lost" 643.
- French: "passage non déchiffré" 33/16; "chiffres non traduits" 34/18; "chiffre non traduit" 39/17; "en chiffres sans
  traduction" 23; "le reste est en chiffre(s)" 14 and 8; "lignes en chiffres" 281/208; "suivent des chiffres" 235/143;
  "chiffre n'a pu être" 624; "clef de ce chiffre" 140; "pu trouver la clef" 311; "non déchiffrée" 346; "lettre
  chiffrée" 3,431 (first 100 titles only); "dont nous n'avons pas la clef" 626; "sans la clef" 1,362 (too broad);
  "en chiffres non déchiffré" 0.
- Italian: "cifra non decifrata" 22/15; "righe in cifra" 102/54; "non si è potuto decifrare" 27; "manca la chiave"
  148 (figurative); "segue cifra" 31; "cifra non deciferata" 0.
- German: "folgen Chiffern" 22/20; "unaufgelöste Chiffern" 20/18; "nicht dechiffriert" 546/71; "nicht dechiffrirt"
  76; "Schlüssel fehlt" 2,072 (too broad); "nicht entziffert" 8,891 and "unentziffert" 2,608 (too broad); "Chiffern
  nicht aufgelöst" 0.
- Spanish: "sigue en cifra" 136/95; "cifra sin descifrar" 12/0 (search-only volumes); "sin descifrar" 2,775 (too
  broad); "no se ha podido descifrar" 338.
- Also Dutch and Latin: "in cijfer" 1,624/943; "niet ontcijferd" 624; "niet gedechiffreerd" 0; "regels in cijfer" 0;
  "notis arcanis" 169/127; "ziferis scriptum" 0.

**Planted check.** Before the phrase sweep, four items we already knew were looked for: Bampfield 1659 ("remainder,
chiefly in cypher"), Newton 1612 ("mysterious letters in cipher") and Edmondes 1594 (by its cipher letters) were found;
William Lee's letter of 15 Oct 1778 was not found by its editor's phrase. So the index covers these editions and finds
what an editor flags; it cannot find cipher an editor did not flag.

**How each hit was checked for a key appendix.** "Not deciphered" in an edition may concern one name, or be undone by
a key printed elsewhere in the same volume. The Correspondence of George Baillie of Jerviswood (1842) taught this: its
"Not decyphered" notes turned out to concern two name codes in a correspondence whose cipher the editor read under
every group and whose keys he printed. So for each kept hit the volume was searched in-volume for "chiffre"/"cifra"/
"Chiffern"/"cipher" and "clef"/"chiave"/"Schlüssel"/"key", and the introduction or source note read where it could be
found. The result is in each row: for example the Nuntiaturberichte volume names a printed nuncio key (row 8), the
Groen volume prints partial readings on two of the three letters (row 1), and Guglielmotti's volume has no key at all
(row 7). Where only a search snippet was read, the row says so.

### Colonial Office transcripts on the Internet Archive (16-17 Nov, two nights)

The Library of Congress transcripts of The National Archives CO 5 (University of North Carolina at Greensboro film,
56 items): the French and Indian War reels (2,376 images) and the American Revolution reels with the Southern Indian
Department volumes CO 5/78-82 (3,308 images), paged at about 1,100 px on contact sheets by several readers, every
flag opened at full size. Every batch carried planted known code pages and two tables that are not cipher; on the
second night each batch also carried a test page made from a real transcript page with one or two lines of figures
cut from the copyist's own hand inserted. All planted code pages were found (on the first night one batch had a faulty
seed; the second night 96 of 96), the copyist-hand test page was found in all 32 batches of the second night (28 times
called cipher, 4 times unsure), and no trap was called cipher. **No cipher page:** the copyists left cipher out. Three
mentions were found: Kerlérec's intercepted letters of 1756-57 (catalogue 829 and 830; see `pointers.md`); Burgoyne to
Clinton, 23 and 27 Sept 1777, on "the old Cypher" (Clinton's mask letter, already read and printed: not a lead); and
Dartmouth's "Cypher letter K" of 1775 (key leads, below). The CO 5/96-111 despatches of 1778-83 are not in this film.

## Key leads (no ciphertext; not rows)

- **"Cypher letter K", 1775.** Dartmouth to Gage, No. 17, Whitehall 15 Apr 1775, sent by Major General Howe: the
  draft in CO 5 (about CO 5/92), seen in the Library of Congress transcript on the Internet Archive
  (`per_records-of-the-british-colonial-office-class-6_1772-01-11_1`, frame 666, transcript pp. [217]-[218]): "With this
  you will receive two sets of a Cypher & a Decypher letter K; one of which you will deliver to the Major General who
  shall have the separate Command at New York; it being His Majesty's intention that this Cypher should be occasionally
  used, not only in your Correspondence with me, but also with the Officer having that Command ... If any difficulty
  arises it will be in the names of places & persons, & therefore I send you a List of those that are most likely to
  occur, with a Cypher for each." Neither the cipher nor the name list is copied in the transcript, and no text in K is
  known. Places to look: the Haldimand Papers (British Library Add MS 21661-21892; Haldimand commanded at New York in
  1775), The National Archives SP 106 (ciphers), British Library Add MS 32256-32257.

## Not offered, and why

- **Already read, or a duplicate:** Jerviswood 1702-08 (read in print, see above); Raimondo to Giovanni de' Medici,
  27 Jun 1521 ("Segue un pezzo in cifra non decifrata", Archivio storico italiano n.s. 8 p. 30): upstream's Internet
  Archive full-text sweep saw the same note and set it aside (`research/ia_fulltext/README.md`, "too short, no
  folio"); the Catherine de Médicis-du Croc facsimile, Poinsett 1813, Hoverbeck 1662, Lisola, Fersen, Grotius (known
  upstream); La Motte 1579, Henrietta Maria 1643, Belgrano 1816, San Martín 1821 and others printed deciphered.
- **Too small or too thin to be a lead:** an envoy at Madrid on Don Carlos, 17 Mar 1568 (one name "in cifra, non
  decifrata", envoy and manuscript not identified); Retz, letters to Rome 1651 (Œuvres t. 8 pp. 36, 114: three code
  numbers in clear text, "Nous n'avons pu découvrir la clef de ce chiffre"); a French army telegram of July 1870
  ("Suivent des chiffres", Papiers secrets de l'Empire p. 62: seen only in a result list); Hoverbeck 1681 (one name).
- **Probably deciphered at the time:** a Venetian resident at Naples 1792 and a Milanese ambassador in France about
  1479 ("alcune righe in cifra", "trois lignes en chiffres"): the editors do not say unread, and both series usually
  carry contemporary decipherments.
- **Two finds that we saw only on a licensed page image and have not yet checked on a free copy:** Throckmorton,
  Orleans, 29 Nov 1560 (Hardwicke, Miscellaneous State Papers 1778, vol. 1 p. 158: "The concluding part of this
  sentence is not decyphered"); free copies to check: the Internet Archive's `miscellaneoussta01harduoft` and
  `bim_eighteenth-century_miscellaneous-state-pape_great-britain_1778_1`, then the Calendar of State Papers Foreign
  1560-61. Henrietta Maria and Jermyn, Paris, late 1644 (M. A. E. Green, Letters of Queen Henrietta Maria, 1857, p.
  263: "The cipher portion in the queen's letter is not deciphered in the original"); free copy to check: any public
  copy of Green 1857, where the italics may already give a decipherment from Jermyn's interlined copy.
- **Not reached:** the Dutch "in cijfer" list beyond Grotius; "lettre chiffrée" beyond 100 titles; the rest of the
  CODOIN "sigue en cifra" hits; Die Jesuiten und die Friedensfrage (1906); later Nuntiaturberichte and Urkunden und
  Actenstücke volumes; search-only volumes (Acta Pacis Westphalicae "nicht dechiffriert", Guicciardini Carteggi X and
  XVII, the Salazar y Castro index, the Guyane C14 inventory) that need a member login. DECODE was not searched online
  for any row, and Lasry's and Tomokiyo's pages only where a row says so.

## The Bourgogne letters (row 0)

`bourgogne1703_ciphertext.txt` gives the 353 numbers by run, with the clear text around each run and a note on how
the transcription was made (two independent readings of the page images, no difference). What was tried, all of it
FAILED and reported as such:

- **Counts.** 126 distinct values in 353 numbers, 55 used once, index of coincidence 0.0120, no doubled group, value
  23 often every second group. Synthetic French text enciphered with letter tables of 90-180 symbols cannot match the
  distinct values, singletons and top share together; a syllable-and-word nomenclator of about 300 entries matches
  every measure. Only 13% of the numbers lie above 250.
- **Four existing French keys of 1690-1703**, applied unchanged with a plan fixed beforehand: Louis XIV's code of
  1690/93 as far as published (96 of 353 numbers covered), the petit chiffre of Pignerol 1690-91 (182), the Grand
  Chiffre of 1691 (309), the Bonac-Groffey key of 1703-11 (DECODE R639; 324). Each misses against 1,000 permuted
  tables of its own units (the nearest, the petit chiffre, at the 97.9th percentile, below the 99th required); each
  passes its positive control (the duke's clear letters enciphered with that key). The d'Usson code of 1702 covers too
  few groups to test.
- **A ciphertext-only attack** was calibrated first on synthetic text of the same length: 0 of 5 successes for letter
  tables of 60, 90 and 130 symbols and for a one-part syllable code even when the solver was given the exact list of
  units. By the rule fixed in advance, no attack was run on the real text.

The way forward is the originals (row 0, `verify`): Philip V's copy may carry a decipherment, and the key the duke
sent on 7 Jan 1703 may be filed with that letter.
