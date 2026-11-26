# Dumas's key-text cipher, 1776-1781: every cipher passage in his letters to Congress, with the passages the editions leave out

Status: read (read with known key; written up on 24 Nov 2026, docs/dumas1777.html). 928 of 948 cipher words in the 18
readings, 20 holes; the three blotted numbers are illegible, the other holes are the writer's slips and omissions.

Class: read (read with known key). This is not a break. The key and the system were set out by Dumas in 1776 and
re-established from the Committee's enciphering table by Satoshi Tomokiyo; most passages carry the contemporary
decipherer's letters. Andrew Beling, with AI agents, 14 November 2026 (pull request #667, merged 15 November 2026 as a
folder with no site page). The page was written by the maintainers on 24 November 2026, after the recount, the key
replay and the reading review set out under "Maintainers' checks" below.

## Who read it before us

- **The Committee's decipherer or decipherers, 1776-1779.** Letters are written over the numbers on most pages of
  item 93 vol. 1 and on the M332 copies: faint pencil in 1776, ink from 1777. The hand is not identified. A second AI agent
  of ours compared the inked glosses with James Lovell's own number-letter table (item 51 vol. 2, image 186): the letter
  forms are compatible with Lovell's (looped d, two-stroke r, pointed v, small closed e), but single interlined letters
  are too few to identify a hand, so this is **not** an identification.
- **Benjamin Franklin.** A member of the Committee of Secret Correspondence to which the 1776 despatches went; Dumas set
  out the key and the counting rule in his letter of 30 April 1776. Franklin used the cipher himself (to Dumas, 16 August
  1781) and recommended it, as Tomokiyo shows.
- **The editors.** Jared Sparks, *Diplomatic Correspondence of the American Revolution*, vol. 9 (Boston, 1830, the date `sources.md` gives for the
  copy searched; this line said 1829 until 24 Nov 2026), and Francis
  Wharton, *Revolutionary Diplomatic Correspondence*, vols. 2-4 (1889), printed translations that include the decoded
  content of many cipher passages and leave others out. Peter Force, *American Archives*, fifth series, vol. 2 (1851),
  cols. 99-103, printed despatch D of 1776 with the numbers, an interlined decipherment and a translation. The *Papers of
  Benjamin Franklin*, vol. 22 (1982), printed the letters of 30 April and 14 May 1776 in French with the cipher passages
  decoded in brackets, from the decoding interlined on the manuscript.
- **Satoshi Tomokiyo**, Cryptiana, "Dumas' Cipher - Benjamin Franklin's Favorite Cipher" (2008-09,
  https://cryptiana.web.fc2.com/code/franklin.htm), re-established Dumas's own 13-line key text and homophonic system of
  1776 from the Committee's enciphering table.

**What we add.** (1) The full inventory: every Dumas item with cipher in the Papers of the Continental Congress, item 93
vol. 1 (National Archives microfilm M247, https://catalog.archives.gov/id/502964761) and the copies in the Miscellaneous
Papers (M332 roll 2, https://catalog.archives.gov/id/464815090): 21 letters or enclosures, 4,503 number places in the
principal copies and 2,401 in other copies, each transcribed twice. (2) A test of the printed key against the
contemporary glosses. (3) The text of the cipher passages that are not in the editions checked: ten passage groups, below. Most
of them carry the contemporary decipherer's letters, so they were read at the time and are **unpublished contemporary
decipherments**. Fully bare, with no decipherment of the time on any copy: the sentence of 25 September 1777 (repeated
bare on 14 October 1777) and the postscript of 2 September 1781. The English letter of [after 17 May] 1779 is bare, but
its 17 numbers are glossed in the May letter and the name is written in the margin of the 21 June copy.

## Inventory

Images are those of the National Archives Catalog: "93" = item 93 vol. 1 (502964761), "M" = M332 roll 2 Dumas file
(464815090). Machine-readable in `inventory.tsv`; page-by-page screening rows from both passes in `inventory_pages.tsv`.

| id | Date | Mark | To | Images | Numbers | Glosses | In print |
|---|---|---|---|---|---|---|---|
| 1776-04-30 | 30 Apr 1776 (+ unsigned letter of 6/9 May) | first report; Extrait | Committee of Secret Correspondence | 93: 16-19, 23-24; copy 27-30 | 1,464; copy 1,372 | pencil, partial; copy full | yes, cipher read (Franklin Papers 22; Sparks; Wharton) |
| 1776-05-14 | 14 May-6 June 1776 | B | same | 93: 31-35 | 1,001 | partial | yes, cipher read (Franklin Papers 22) |
| 1776-08-10 | 30 June-10 Aug 1776 | C | same | 93: 39, 41 | 168 | full | yes, cipher read (Sparks; Wharton) |
| 1776-09-01 | 1 Sept-10 Oct 1776 + Suite | D | same | 93: 47, 51-53 | 116 | partial-full | yes, cipher read (Sparks; Wharton; Force for 52-53) |
| 1777-04-12 | 12 Apr 1777 | E | same | 93: 55 | 79 | full | yes, cipher read (Sparks; Wharton) |
| 1777-08-02 | 2 Aug 1777 | N | same | 93: 81 | 63 | full | **no** |
| 1777-08-14 | 14 Aug 1777 | extract to Franklin | same | 93: 90; M: 3 | 100 + 100 | full; M mostly bare | content printed from the clear original (Franklin Papers 24) |
| 1777-09-25 | 25 Sept 1777 | R | same | 93: 108 | 32 | **bare** | **no** |
| 1777-10-14 | 14 Oct 1777 | S | same | 93: 110 | 32 | **bare** | letter printed, cipher sentence omitted |
| 1777-11-04 | 4 Nov 1777 | T (+ extract) | same | 93: 114-115; 117 | 134 + 134 | glossed | **no** |
| 1777-11-28 | 28 Nov 1777 | V, enclosure | same | 93: 124-126 | 370 | glossed | **no** |
| 1778-02-24 | 24 Feb 1778 | B2 / C2 | Committee for Foreign Affairs | 93: 143-144; M: 9-10 | 346 + 346 | glossed | **no** |
| 1778-04-27 | 27 Apr 1778 | H2 / D2 | same | 93: 154; M: 13 | 107 + 107 | glossed | **no** |
| 1778-06-14 | 14 June 1778 | N2 / M2 | same | 93: 160; M: 20, 23 | 139 + 140 + 140 | glossed; M 23 bare | **no** |
| 1778-07-31 | 27/31 July 1778 | names list | same (enclosure) | 93: 173 | 138 | glossed | letters printed with blanks; list **not** |
| 1778-08-17 | 17 Aug 1778 | heading to Van Berckel | same (copy) | 93: 195, 201 | 25 / 28 | glossed / partial | yes |
| 1779-05 | May 1779 (printed 15 May) | Q3/R3 | same | 93: 242 | 108 | faint | run 1 printed; runs 2-6 **omitted** |
| 1779-05-after17 | [after 17 May] 1779 | S3/T3 | same | 93: 239 | 17 | bare | **no** |
| 1779-06-21 | 21 June 1779 | S3 | same | 93: 253 | 17 | bare, name in margin | **no** |
| 1779-09-20 | 20 Sept 1779 | N4 / Z3 | same | 93: 260; M: 72 | 34 + 34 | partly; M bare | yes, cipher read (Wharton 3:333; Sparks) |
| 1781-09-02 | 2 Sept 1781 | P.S. to F6 | President of Congress | 93: 493 (plain copy 488-489) | 13 | **bare** | letter printed, cipher sentence omitted |

Screening: every page of item 93 vol. 1 (503 images) and the M332 roll 2 Dumas file (211 images) by both transcription
passes, from contact sheets and then at reading size. Item 93 vols. 2-4 were screened on contact sheets only; no cipher
was seen there, but the sheets are low resolution.

## The key

Details in `key/KEY.md`. Each number is the position of a character in 13 printed lines of Dumas's 1775 Amsterdam
edition of Vattel, *Le Droit des gens*, "Lettre de l'éditeur à Monsieur ***" (pp. III-V), 682 characters from
"Voulez-vous sentir la différence?" to "dans leur juste résistance." (`key/keytext_1775.txt`). Counting rule (Dumas,
30 April 1776, "Tout a son nombre"): spaces are not counted; apostrophes, hyphens (line-end hyphens included), commas,
full stops, "&" and the reference mark "*" are; positions run 1-682 straight through, with line ends at Dumas's totals
57, 114, ..., 666, 682. Accents ignored in use; every occurrence of a letter is an alternative number for it.

Our file and the 13 lines on Cryptiana's page differ in one position of 682: **position 515**, where the page prints
"suciombent" for "succombent", a typing slip (515 = c is confirmed in use, the c of "ici" on 14 June 1778, glossed c).

Frozen: `key/key_positions.json` sha256 `36276e0a73f3dd58d8940202b7c97033fb706bb576317083a083a2808744ae74`
(`key/FREEZE.txt`).

## Tests

- **Test 1** (`tests/test1/`, plan in `TEST_PLAN.md` with the hash written before the run): a key built from the 1778
  glosses on M332 images 9, 10 and 13 (342 numbers, sha256 `5e5fc9cc...`) predicted the glosses on M332 image 20:
  106 of 108 covered numbers (98.1%) after one transcription correction checked on the image (105 of 108 as first
  transcribed); 200 shuffled keys: mean 7.9%, max 14.8%. Not blind: one transcriber did both sides.
- **Test 2** (`tests/test2/`, plan written before the run): the printed-text key, built without any gloss, against the
  contemporary glosses on item 93 image 173 (July 1778, a page chosen in advance and not used in test 1): **129 of 134
  (96.3%); 129 of 130 (99.2%) leaving out glosses the transcriber marked uncertain**. 200 shuffled keys: mean 7.1%,
  max 14.9%. Pass (criterion: at least 90% and above every shuffle). The misses are glosses read one number off or
  illegible. Caveat stated in the plan: the reading agent had already decoded image 173 with this key.
- **Statistical validation** (`docs/_validate.py`, `validation.tsv`, the French documents only, 4,129 numbers): reading
  -2.008 per letter (fr-1750-nospace); random keys -5.269 (z 39.7); key fitted to shuffled text -3.482 (z 85.9). Verdict
  pass. The annealer reached only -3.528 on the real text, so the shuffled-refit null is weak here; the gloss tests are
  the stronger evidence.
- **Independent second agent.** It rebuilt the key from Cryptiana (the 515 point above), transcribed four passages on its
  own (`transcriptions/second_agent/`: 2 Aug 1777, 14 June 1778, May 1779, 2 Sept 1781; and the 12 April 1777 count
  check) with the same numbers and readings apart from one number, and redid the print check. Its corrections are applied
  (next section).

## Transcriptions and readings

- Two independent passes for every cipher run: forward (A) and backward (B), `transcriptions/R1_A ... R5_B/` (one file
  per image; glosses written number/letter where seen). Aligned page by page they agreed on about 95% of numbers before
  any image check; nearly all the rest were misalignments or blots, settled on crops. The reconciled numbers per
  document are in `transcriptions/reconciled/` (`*` marks a number kept as written but emended in the reading).
- One reading file per letter in `readings/` (sources, reconciliation decisions, numbers, raw decode, normalized text,
  translation, share read, emendations, print check). The texts for the profile are in `letters/` (`_decode`, `_text`,
  `_en`). Since 24 Nov 2026 the `_text` files mark the cipher passages with ⟦ ⟧, a letter corrected or supplied by sense
  with `[x]` (a hole), and a letter given by another cipher copy or by the decipherer's letter over the number with
  `{+x}` (read); the `readings/*.md` files keep the contributor's first marks (square brackets for cipher, round ones
  for emended letters).
- Share read, the contributor's count of 14 Nov 2026 (numbers giving the accepted letter, principal copies, a number
  counted as read when its letter was restored with certainty): 4,498 of 4,503; the five others are three blots,
  the conjectural 54 in "sont" (14 June 1778) and the guessed "&" (20 Sept 1779).
- Share read, the project's measure (24 Nov 2026; README Conventions: cipher words only, holes by words, a word with a
  letter corrected or supplied by sense is a hole): **928 of 948 cipher words, 20 holes**. Per reading, cipher words and
  holes: 30 Apr 1776 305 / 2; despatch B 223 / 6; despatch C 32 / 1; despatch D 22 / 1; 12 Apr 1777 19 / 1; 2 Aug 1777
  14 / 0; 14 Aug 1777 21 / 1; 25 Sept and 14 Oct 1777 16 / 0; 4 Nov 1777 30 / 0; 28 Nov 1777 87 / 2; 24 Feb 1778
  64 / 1; 27 Apr 1778 21 / 1; 14 June 1778 26 / 1; July 1778 names 26 / 0; 17 Aug 1778 heading 8 / 0; 1779 Neufville
  passages 24 / 1; 20 Sept 1779 6 / 2; 2 Sept 1781 4 / 0. Every reading is at 0.95 or more except 12 Apr 1777 (18 of
  19) and 20 Sept 1779 (4 of 6), which are read by the short-text floor (fewer than 40 cipher words, at most 2 holes).
  The extract of despatch C (1776) is at 31 of 32 only because four of its words take one letter from the decipherer's
  letters over the numbers (Hortalez, d'Espagne, simplement, puissance), which count as plain text beside the cipher; by
  the key alone it is at 27 of 32. The words are counted by the reading-audit tool, which splits at an apostrophe
  (l'Angleterre is two words).
- Key replay (`replay.py`, `replay.tsv`, `replay.json`; `python docs/_replay.py dumas1777`): of the 4,503 number places
  of the principal copies, 4,479 give the reading's letter exactly and one more is c written for k ("cing of Prussia");
  18 are marked emendations; 1 is unread (the guessed "&"); 4 have no key value (the three blots and 698, out of range,
  in the letter of 30 Apr 1776). No unmarked difference.

**Corrections after the independent check, applied in this folder:**
1. 1776 despatch D, images 52-53, **are in print**: Force, *American Archives*, 5th ser., vol. 2, cols. 99-103, gives the
   numbers, an interlined decipherment ("— le ministre même"; "Ma d a m U l o d e r") and a translation. The first
   reading's emendation of 641 is dropped: the text is "Madam V. Loder", Dumas's forwarding address, which Wharton vol. 2
   also prints ("chez Mad. V. Loder, à la Hague", Committee to Arthur Lee, 12 December 1775).
2. 2 August 1777, line 12: the image shows **14** (glossed n), not 12; the emendation is removed.
3. May 1779: the preference for "J. de Neufville & fils" is reported as "leur voix unanime", the view of "vos amis, là &
   ici", not as Dumas's own; and the cipher says "On trompe l'ambassadeur de F=", quoted as it stands.
4. 20 September 1779: the numbers spell "csmmodore jones e his"; the contemporary decipherer wrote S and E over them;
   "Commodore" is certain and the "&" is a guess.
5. 14 June 1778: "sont" rests on a marked emendation (54, n to s).

## The passages not in print

Recount from the second agent's list. Not in the editions checked: 2 Aug 1777; 25 Sept 1777; 4 Nov 1777; 28 Nov 1777;
24 Feb 1778; 27 Apr 1778; 14 June 1778; the July 1778 names list; the 1779 Neufville passages. Printed with the cipher
passage left out: 14 Oct 1777 (the same sentence as 25 Sept), the May 1779 letter after its first passage (part of the
Neufville group), and the 2 Sept 1781 postscript (Wharton 4:657). Counting the sentence of 25 Sept/14 Oct once and the
1779 Neufville passages (May runs 2-6, [after 17 May], 21 June) once, that is **ten passage groups, in thirteen
letters**.

**Catalogue entry 784** (William F. Friedman Collection, Marshall Foundation, item 14: extracts marking the cipher
passages Wharton's *Revolutionary Diplomatic Correspondence* vols. 4-5 printed as undeciphered, c. 1779-1782; class B,
"not viewed"). Of our ten passage groups, only the postscript of 2 September 1781 falls in those volumes: Wharton
4:655-658 prints the letter of 30 August 1781 and its postscript of 2 September with the cipher sentence left out
(p. 657). Whether item 14 lists that sentence cannot be told here: the item was not seen. The other nine groups are of
1777-1779, in Wharton vols. 2-3, outside the entry's range. This folder does not claim or close entry 784.

The ten groups:

1. **2 Aug 1777 (N)**, glossed. "Depuis quelque temps le [courier du Bas-Rhin] ne m'écrit plus ... Je viens de faire de
   bonnes ouvertures pour des négociations [secrètes avec des gens de la régence d'Amsterdam]." (No emendation.)
2. **25 Sept 1777 (R)**, repeated in **14 Oct 1777 (S)**, bare. "[Le paquet, L, est dans le vaisseau pris.]" His packet
   L was in the captured ship (in S it follows the account of the Dutch ship taken in the Channel). Wharton 2:407-408 and
   Sparks 9:329-330 print S without it.
3. **4 Nov 1777 (T)**, glossed. "[C'est votre serviteur, qui a fait insérer la pièce au Mercure, & publier la Lettre
   hollandoise, etc.] J'ai toujours [sur le corps ici toute la cabale ennemie. Mais je suis à vous.]"
4. **28 Nov 1777, enclosure "2d Extraits" of his correspondence with [le Courier du Bas-Rhin]** (V), glossed. His
   correspondent will make a memorial on [Embden] "[que je ferai parvenir au Roi en main propre, par le moyen de personnes
   qui l'approchent tous les jours ... Je sais qu'il a la plus forte envie de fonder une marine]"; "[Mr. Lee étoit allé à
   Berlin]"; American privateers should be free "[d'entrer à Embden]" with their prizes; if blockaded, "[vous saisir de
   Brême, de Stade, &c. que vous ferez bien de garder]". Four emended numbers (88, 390, 217, 276), all supported by the
   gloss or a neighbouring number.
5. **24 Feb 1778 (B2/C2)**, glossed. He can "[me procurer les dépêches des ministres de la Rép(ublique) dans les cours de
   l'Europe, & ... j'en envoie les extraits régulièrement]" to the Commissioners; "[Une maison hollandoise à Amst(erdam) a
   ouvert une souscription de dix mille pièces, pour envoyer quatre vaisseaux ... négocier directement avec votre
   continent. Il y a déjà trois mille pièces de souscrites.]" (410 emended in both copies; 298 in B2 from C2.)
6. **27 Apr 1778 (H2/D2)**, glossed. One more letter from Paris is expected "[pour frapper un grand coup]"; "[ces
   mesure(s) ... sont bien concertées]", good news next month. (No emendation.)
7. **14 June 1778 (N2/M2)**, glossed. "[cimenter] & [fortifier] le parti [formé] ... pour [ruiner l'influence angloise
   ici, détacher cette République de] vos ennemis, [la concilier à vous & à vos amis. Amsterdam, Harlem, Dort] & [Delft
   {s}ont pour nous.]" "sont" rests on the marked emendation 54 n to s.
8. **July 1778, the names left blank in the Van Berckel letters**, glossed. "[le Pensionnaire d'Amsterdam — La Haie — le
   Grand Pensionnaire — Amsterdam — Leurs Hautes Puissances — E. F. van Berchel.]" The letters are printed with blanks
   (Wharton 2:666-667; Sparks 9:333-335); most names can be guessed from the editors' headings, so this is a small addition.
9. **The 1779 Neufville passages.** May 1779 (Q3/R3), faintly glossed, runs 2-6 after the printed run 1 ("cabal of
   Genevan and Swiss bankers"): "Ce sont vos amis, là & ici, qui m'ont fait agir; leur voix unanime est, [— que J. de
   Neufville & fils mérit(ent)] seul [— votre confiance] à Amsterdam, que les précédents [ont été] de [faux amis.] On
   [trompe l'ambassadeur de F=]." And the English letters of [after 17 May] 1779 (bare) and 21 June 1779 (bare run, name in
   the margin): "What I have [had] the honour to tell you in my Letters Q3, R3, May 17th, of [J. de Neufville & fils] must
   be so understood, that it not exceeds the mercantile line".
10. **2 Sept 1781, P.S. to F6**, bare. "[The city is Dort.]" Sparks 9:464 and Wharton 4:657 print the P.S. without it;
    the plain copy (images 488-489, checked on the image) leaves it out and does not name the city.

Also new but not counted as a passage: the Extrait copy of 30 April 1776 adds "[notre homme de la Haie]" (not printed).

## Print check

Passage by passage in `print_check.tsv` (status, reference, differences, and the second agent's notes). Summary:

| Item | Result |
|---|---|
| 30 Apr 1776 | Printed with the cipher read. Two corrections to the Franklin Papers: "ministre de **France**" for "fiance" (571 = r in both copies, glossed r); "**Les** alliés" for "Des alliés" (70 = l by the key in both copies, but the contemporary gloss over 70 on image 27 looks like d: the slip was the period decipherer's and the editors followed the interlined decoding). |
| 14 May 1776 (B) | Printed with the cipher read; the Franklin Papers silently correct six slips of Dumas (print_check.tsv). |
| C 1776 | Printed with the cipher read; the cipher spells "Hortelez" (print Hortalez). |
| D 1776 | Printed with the cipher read: 47 and 51 in Sparks and Wharton; 52-53 in Force. |
| 12 Apr 1777 (E) | Printed with the cipher read. |
| 14 Aug 1777 | Content printed from the clear letter to Franklin; the cipher extract names "l'Ambassadeur de France à la Haie" where the clear letter has the cover name "le Facteur". |
| 17 Aug 1778 heading | Printed (Van Berckel named). |
| 20 Sept 1779 | Printed with the cipher read: Wharton 3:333 "Commodore Jones' squadron"; numbers as written "csmmodore jones e his squadron". |
| The ten groups above | Not in the editions checked, or printed with the cipher passage left out. |

Editions searched: Wharton vols. 2-4 and Sparks vol. 9 (Internet Archive text, both agents); Force, *American Archives*,
4th series vols. 5-6 and 5th series vols. 1-3 (second agent); the Franklin Papers on Founders Online by reading the 1776
letters and the 14 Aug 1777 letter and by a few keyword searches.

## Context

What the letters say (our readings, above): Dumas at The Hague reports openings with people of the Amsterdam regency
(1777), a subscription by an Amsterdam house for direct trade with America and access to the Republic's diplomatic
despatches (1778), the towns he counts as "pour nous" (1778), a Prussian channel through the Cleves gazetteer for
American privateers at Emden (1777), the friends' preference for J. de Neufville & fils and the French ambassador being
deceived (1779), and Dort as the city behind a resolution on the French loan (1781).

Established history, with the references checked here: Dumas was the Committee's agent at The Hague, with letters
forwarded "chez Mad. V. Loder" (Committee of Secret Correspondence to Arthur Lee, 12 December 1775, Wharton 2). E. F.
van Berckel was Pensionary of Amsterdam ("Dumas to Van Berckel, Pensionary of Amsterdam", Wharton 2, 1778). The duc de
La Vauguyon was French ambassador at The Hague (Dumas's extract of 12 April 1777, "les ministres de France à la Haie,
l'abbé Desnoyers, & le duc de la Vauguyon"; his memorials as "Ambassador of France", Wharton). Arthur Lee wrote to the
Committee on 18 March 1777 that he meant to sound the Emperor and the King of Prussia: "The one wishes to promote the
port of Ostend, the other of Emden" (Wharton 2:295), and wrote
from Berlin in June 1777 (Wharton 2). William Lee sent Congress a draft treaty arranged with John de Neufville "on the
part of the pensionary and burgomasters of Amsterdam" (Frankfort, 25 February 1779, Wharton 3). John Paul Jones arrived
"in the Texel" with "the remains of my little squadron on the 3d instant" (Jones to Morris, Amsterdam, 13 October 1779,
Wharton 3:375); Dumas's letter of 20 September says he is leaving for the Texel with instructions for the squadron.

Inference (ours): the 1777-78 passages show Dumas's covert work with the Amsterdam regents and merchants a year before
the Lee-Neufville draft treaty; the 1779 passages show him relaying a strong recommendation of de Neufville against other
houses; the Emden enclosure shows him using a Prussian channel to press for a port open to American privateers. That the
editors left these passages out because they were cipher, rather than by judgement of importance, is not shown; Wharton
says he omitted some letters "as without public importance".

The May-June 1779 passages concern the same merchant house as the repository's `neufville1779` target (pull request
#587, merged on 14 November 2026). That folder holds Jean de Neufville's own syllabic code with Baudouin: a different
cipher, with its own folder. No other target in the repository uses Dumas's key text; `targets/pcc1780` and
`targets/lovell1781` only mention the key sheets filed in PCC item 59.

## Images

The images are federal records, free in the National Archives Catalog (use restriction "Unrestricted" on the catalog
record); references above are to its image numbers (`?objectPage=N` on the catalog pages). The contributor committed no
crops. Three crops were cut for the site page on 24 Nov 2026 (`docs/dumas1777_lead.jpg` from image 81,
`docs/dumas1777_bare.jpg` from image 108, `docs/dumas1777_dort.jpg` from image 493); the page images themselves are not
committed.

Image numbers: the folder's image N is the N-th object of the file unit in the order of the catalog's object ids. The
object list the catalog's API returns (`https://catalog.archives.gov/proxy/records/search?naId=502964761`) has two
objects out of that order (the 73rd and the 170th of the list), so images 73 to 216 stand one place later in the list
(image 81 is the 82nd object, image 108 the 109th, image 160 the 161st); images 1-72 and 217-503 are in place. Found on
24 Nov 2026 when images 41, 55, 81, 108, 160 and 493 were fetched for the checks below.

## Reading review

The contributor's grades of 14 Nov 2026 (18 entries, all B) were recorded by Andrew Beling's own AI agents as
preliminary, "for a maintainer to confirm or replace" (`CONTRIBUTING.md`: a reading merges only with a
`reading_review` "recorded by the reviewer, not by the author of the reading"). On 24 Nov 2026 the maintainers'
integration reviewer (an AI agent, not a person) read the 18 readings as sentences against their translations, with
the key replay and six page images, and recorded its own grades in `profile.json` in their place: 16 A and 2 B (the
extract of despatch C of 1776, where four words lean on the decipherer's letters, and 20 Sept 1779, where two of six
cipher words are holes). Each note says what was and was not looked at. No person has checked a reading.

## Transcription doubts

Every cipher run was transcribed twice (forward and backward passes) and the doubtful figures were settled per letter:
140 decisions are listed under "Reconciliation decisions" in the `readings/*.md` files, 91 of them with what an
enlarged crop of the image shows; the others were settled by the second cipher copy of the same letter and the decoded
word, and the "Remarks" of each file say which. The places below are those that stay doubtful or that a hole rests on.

- # (1776-08-10, image 41 L18) - read: [g] of char[g]é, a hole; checked: image, decode, transcription; "23" and a hidden last figure under a blot, the decipherer's letter over it blotted too (looked at again 24 Nov 2026); pass A "#", pass B 236?; 238 = g
- 4? (1776-08-10, image 41 L17, second number) - read: e (simpl{+e}ment), from the decipherer's letter; checked: image, decode, transcription; the second figure is under a blot (40 = y, 48 = e); both passes 40; the decipherer's e stands over it (24 Nov 2026)
- # (1776-09-01, image 51 L03) - read: s (Prus{+s}i[a]), from the decipherer's letter; checked: image, decode, transcription; the number is under a blot, both passes "#", the letter over it is s
- 25 (1776-09-01, image 51 L03) - read: [a] of Prus{+s}i[a], a hole; checked: image, decode, transcription; "?5" under a blot (pass A 25, pass B 5); neither 25 = r nor 5 = e gives a; the letter over it is not clear
- 5# (1777-04-12, image 55 L19) - read: [b] of l'ab[b]é, a hole; checked: image, decode, transcription; a first figure 5 and an ink blot (both passes; seen again at 2x on 24 Nov 2026); the decipherer's letter over it has a looped ascender, b or l, with its foot lost in the blot (both passes read l?); b is at 500, 518 and 572
- 59[0/8] (1776-05-14, image 35 L20) - read: [c] of Fran[c]e, a hole; checked: image, decode, transcription; last figure retouched, 0 or 8; 590 and 598 both = e, 591 = c
- 88 (1777-11-28, image 124 L2) - read: b ({+b}as-Rhin), from the decipherer's letter; checked: image, decode, transcription; two blotted figures, kept as 88 = l; letter N of 2 Aug 1777 has 118 = b in the same word
- 8? (1779-05, image 242 L17) - read: 89 = e (trompe); checked: image, decode, transcription; "8" and a blotted second figure on a 2x crop, both passes 84; the decipherer's letter is e
- 14 (1777-08-02, image 81 L12, seventh number) - read: 14 = n (Bas-Rhin); checked: image, decode, transcription; first read 12; the second agent read 14 on the image, the decipherer's letter is n (seen again 24 Nov 2026)
- 54 (1778-06-14, image 160 L24, last number) - read: 54 = n as written; "[s]ont" is a conjecture and a hole; checked: image, decode, transcription; a clear 54 on the image (24 Nov 2026) and in both M332 copies

## Maintainers' checks

- 15 Nov 2026, before merging pull request #667 (the review on the pull request): a position table built from
  `key/keytext_1775.txt` was identical to `key_positions.json`; a separate decoder on all 29 reconciled files gave the
  folder's letters except at the marked emendations; test 2 re-ran at 129 of 134; on the National Archives Catalog
  images the numbers of three passages the editions omit (2 Aug 1777, 25 Sept 1777, 2 Sept 1781: 108 numbers) agreed
  number for number. The review noted, for the write-up: the share by words for the short letters; the square brackets
  of `letters/*_text.txt` clashing with the project's supplied-letter mark; and a count of 2,388 numbers in the copies
  files against the 2,401 above.
- 24 Nov 2026, integration review (an AI agent for the maintainers): the reading files re-marked and the share
  recounted by words (above); the key replay added. The first replay run found five unmarked differences, corrected in
  the readings: the cipher repeats the plain word written just before it in three more places than the enclosure of
  28 Nov 1777 (2 Aug 1777 "le", 14 Aug 1777 "à", 24 Feb 1778 "des"); "Pensionaire" has one n in the numbers; and the
  numbers stop at "mérit", now read "mérit[e]" (the plain "seul" after it is singular), not "mérit(ent)". The copies
  files hold 2,401 number places by our count (18 of them lost at the scan edge or blotted, so 2,383 numbers).
- 24 Nov 2026, images: 41, 55, 81, 108, 160 and 493 of item 93 vol. 1 looked at (see "Transcription doubts" and the profile
  step). The 32 numbers of 25 Sept 1777, the 13 of 2 Sept 1781 and the 43 of run 2 of 2 Aug 1777 are as transcribed.
- 24 Nov 2026, print: Cryptiana's page gives the key text and decodes none of the letters. The Internet Archive texts
  of Sparks vol. 9 and Wharton vols. 2-3 were searched by date and keyword: Sparks prints 14 Oct 1777, 15 May 1779 and
  the postscript of 2 Sept 1781 without their cipher sentences, and has no letter of 2 Aug, 25 Sept, 4 Nov or 28 Nov
  1777, 24 Feb, 27 Apr or 14 June 1778, or 21 June 1779; Wharton 2-3 have no letter of those dates and none of the
  passages' wording. Web searches for the passages, Founders Online included, found nothing. These are searches of OCR
  text, not a page-by-page reading. Not checked: the Adams Papers volumes, and any letterbook copy kept by Dumas.

## Limits

- The Franklin Papers were checked only by reading the 1776 letters and the 14 Aug 1777 letter and by a few keyword
  searches on Founders Online. Founders Online refuses scripted access, so only a few searches were made, and the
  Dumas-to-Franklin letters of 1777-1779 were not paged through.
- Item 93 vols. 2-4 were screened on contact sheets only.
- The decipherer's hand is not identified.
- Nothing was checked by a person. The two transcription passes and the reading agents are AI agents of ours; the
  second agent is ours too, so its check is not an outside check. The maintainers' checks of 15 and 24 Nov 2026 were
  made by AI agents as well.
- Catalogue entry 784 is left as it is: the Friedman item was not seen, and nothing here shows which passages it lists.

## Remaining gaps

Twenty holes in 948 cipher words (count of 24 Nov 2026, "Transcriptions and readings" above). None is a gap in the key,
and none can be worked on from the material: three numbers are illegible, and in the other places the number is clear
and gives another letter, or the letter is not written.

- Three blotted numbers (1776-08-10 image 41 L18, char[g]é; 1776-09-01 image 51 L03, Prussi[a], with the next number
  25 = r; 1777-04-12 image 55 L19, l'ab[b]é) - blocker: illegible; the letters are supplied by sense (the s of Prussia
  also by the decipherer's letter) and the three words are holes.
- "[s]ont" (1778-06-14, 54 = n in all three copies) and the "&" after "Jones" (1779-09-20, 24 = e in both copies):
  no outside blocker; the numbers are clear and what the writer meant is a conjecture, so both are holes.
  "C[o]mmodore" in the same letter of 1779 (12 = s) is certain by sense and is a hole under the strict rule.
- Thirteen more words with one letter corrected or supplied by sense, each a hole under the strict rule though the
  word is not in doubt: e[t], d[e] (30 Apr 1776); l[i]eu, parol[e], de[s], gu[e]rre, m[o]urir, Fran[c]e (14 May 1776);
  l'[e]spouse (14 Aug 1777); vo[u]s, d[e] Stade (28 Nov 1777); souscriptio[n] (24 Feb 1778); mesure[s] (27 Apr 1778);
  mérit[e] (May 1779). Nothing blocks them and nothing would close them: they are Dumas's slips and omissions.

## Files

`inventory.tsv`, `inventory_pages.tsv`; `key/` (key text, position table, build script, `KEY.md`, `FREEZE.txt`, the second
agent's key); `tests/test1/`, `tests/test2/`; `transcriptions/R*_A`, `R*_B` (both passes), `reconciled/`,
`second_agent/`; `readings/*.md`; `letters/`; `print_check.tsv`; `validation.tsv`; `scripts/` (`decode.py`,
`reconcile.py`, `alt.py`); `replay.py`, `replay.tsv`, `replay.json` (the key replay); `sources.md`; `profile.json`.
