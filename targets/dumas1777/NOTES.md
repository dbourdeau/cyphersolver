# Dumas's key-text cipher, 1776-1781: every cipher passage in his letters to Congress, with the passages the editions leave out

Status: in progress (folder only, no site page yet; target files and checks only)

Class: read (read with known key). This is not a break. The key and the system were set out by Dumas in 1776 and
re-established from the Committee's enciphering table by Satoshi Tomokiyo; most passages carry the contemporary
decipherer's letters. Andrew Beling, with AI agents, 14 November 2026.

## Who read it before us

- **The Committee's decipherer or decipherers, 1776-1779.** Letters are written over the numbers on most pages of
  item 93 vol. 1 and on the M332 copies: faint pencil in 1776, ink from 1777. The hand is not identified. A second AI agent
  of ours compared the inked glosses with James Lovell's own number-letter table (item 51 vol. 2, image 186): the letter
  forms are compatible with Lovell's (looped d, two-stroke r, pointed v, small closed e), but single interlined letters
  are too few to identify a hand, so this is **not** an identification.
- **Benjamin Franklin.** A member of the Committee of Secret Correspondence to which the 1776 despatches went; Dumas set
  out the key and the counting rule in his letter of 30 April 1776. Franklin used the cipher himself (to Dumas, 16 August
  1781) and recommended it, as Tomokiyo shows.
- **The editors.** Jared Sparks, *Diplomatic Correspondence of the American Revolution*, vol. 9 (1829), and Francis
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
contemporary glosses. (3) The text of the cipher passages the printed editions leave out: ten passage groups, below. Most
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
  `_en`).
- Share read (numbers giving the accepted letter, principal copies): 4,498 of 4,503; the five others are three blots,
  the conjectural 54 in "sont" (14 June 1778) and the guessed "&" (20 Sept 1779).

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
| 14 May 1776 (B) | Printed with the cipher read; the Franklin Papers silently correct five slips of Dumas. |
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

The May-June 1779 passages concern the same merchant house as the repository's `neufville1779` target, proposed in our
pull request #587, which is open and not merged at the time of writing (14 November 2026).

## Images

The images are federal records, free in the National Archives Catalog; references above are to its image numbers
(`?objectPage=N` on the catalog pages). No crops are committed, as for the repository's other targets of this kind.

## Limits

- The Franklin Papers were checked only by reading the 1776 letters and the 14 Aug 1777 letter and by a few keyword
  searches on Founders Online. Founders Online refuses scripted access, so only a few searches were made, and the
  Dumas-to-Franklin letters of 1777-1779 were not paged through.
- Item 93 vols. 2-4 were screened on contact sheets only.
- The decipherer's hand is not identified.
- Nothing was checked by a person. The two transcription passes and the reading agents are AI agents of ours; the
  second agent is ours too, so its check is not an outside check.

## Remaining gaps

- Three blotted numbers (1776-08-10 image 41 L18; 1776-09-01 image 51 L03; 1777-04-12 image 55 L19) - blocker:
  illegible; their letters (g, s, b) are supplied by sense and counted as unread.
- Not gaps in the key but writer's slips, restored by conjecture and counted as unread: 54 in "sont" (1778-06-14, all
  three copies) and 24 after "Jones" (1779-09-20, both copies); both numbers are clear on the image.

## Files

`inventory.tsv`, `inventory_pages.tsv`; `key/` (key text, position table, build script, `KEY.md`, `FREEZE.txt`, the second
agent's key); `tests/test1/`, `tests/test2/`; `transcriptions/R*_A`, `R*_B` (both passes), `reconciled/`,
`second_agent/`; `readings/*.md`; `letters/`; `print_check.tsv`; `validation.tsv`; `scripts/` (`decode.py`,
`reconcile.py`, `alt.py`); `sources.md`; `profile.json`.
