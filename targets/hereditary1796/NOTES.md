# The Hereditary Prince (Berlin) to William V, 12 March 1796 (DECODE R2239; key source R2237; R2236 split off)

Status: read — R2239 read in full (21 Sept 2026); body also printed in Colenbrander 1906 (found during the attempt)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): R2236, Dutch copies in another list, was a
document of this entry until then and is now [`targets/r2236/`](../r2236/NOTES.md) (a different cipher, with its own
page). This entry is R2239, read with the list rebuilt from R2237.

Koninklijk Huisarchief, The Hague, A31 Prins Willem V, inv. nr. 337. Catalogue item 218 (DECODE R2236 and R2239,
both "Non-decrypted"). Sender: Willem Frederik, the Hereditary Prince (later King William I), in Berlin. DECODE gives the
recipient as William V; Colenbrander prints R2239's text as addressed to Prince Frederik, his brother (H.A.). The DECODE note refers to Karl de Leeuw, "Johann Friedrich Euler
(1741–1800): Mathematician and Cryptologist at the Court of the Dutch Stadholder William V", *Cryptologia* 25
(2001), 256–274, for the cipher; the article is paywalled and was not seen.

## The three records

- **R2237** (DECODE "Decrypted", 7 pp.). A clear covering letter (p. 1, "Le Projet ci-joint relativement à la
  réunion des 17 Provinces…", about Reede and two "observations chiffrées"), a clear contemporary decipherment
  (pp. 2–4), and the two ciphered observations themselves (pp. 5–7, marked (1.) and (2.), cipher mixed with clear
  words). The decipherment on pp. 2–4 follows pp. 5–7 word for word. This gives cipher and plaintext side by side.
- **R2239** (3 pp., DECODE "Non-decrypted"). Headed "Berlin 12. Mars 1796". Reading order is DECODE P2, P3, P1.
  Same system as R2237 (numbers 1–248 with letter positions and marks), French. 769 cipher groups and some clear
  words. **Read here.**
- **R2236** (4 pp.). "Copie No 1" and "Copie No 2": Dutch letters with clear Dutch words and numbers up to about
  390, plus a page of numbers up to 2835 (bleeding through R2237 p. 1). Not read: its numbers run past the rebuilt
  list, and the clear words show Dutch. It is probably another list or lists. Open.

## The system (rebuilt from R2237)

A numbered list of words and phrases (about 250 entries). Most of the list runs alphabetically in stretches of
about twenty entries (10 angleterre, 11 berlin, 12 certain, 13 difficile, 14 engager, 15 france, 17 hollande … 22
orange, 23 prusse, 24 quelque; 36 ch…, 37 du…, 38 est … 53 vienne, 55 zélande; 56 alliance, 57 bienfait, 58 cour …
75 visite). Above 100 the entries are common words and phrases ("102 le cabinet", "107 le roi", "132 je compte",
"133 on dit", "122 néanmoins"). Each group takes a piece of one entry:

| group | meaning | example |
|---|---|---|
| `N` underlined | the whole entry | 58 = cour |
| `N,p,q,…` | letters p, q, … of entry N | 12,1,3,2,4 = c r e t (certain) |
| `k/N` or `k)N` (small number top left) | entry N without its first k letters | 4)127 = chement (attachement) |
| `N(k` (small number top right) | entry N without its last k letters | 24(3 = quel (quelque) |

Both marks can combine: 2)84(3 = celle (excellence). Double underlines and bars over the last digit mark ends
of groups and carry no extra meaning that was needed. Clear words are written in among the groups.

Files:
- `r2237_assign.txt`: every R2237 cipher group aligned by hand to its plaintext from the contemporary decipherment.
  No conflicts.
- `r2237_inferred.txt`: entries completed by inference, either from the alphabetical runs and all letter
  constraints (e.g. 60 = états généraux, 62 = guillaume, 94 = quoique) or from R2239's context (234 = paris,
  211 = des, 240 = sans, 224 = londres, 229 = milord, 162 = elgin, 169 = haugwitz, 207 = comte, 98 = votre,
  71 = réputation, 49 = république, 210 = démarches, 208 = défavorables, 136 = …assur…, 176 = journal; see the crib section).
- `wordtable.py`: builds the table and decodes a group file. `show.py` prints R2239 with unread groups in
  brackets; `contexts.py N…` lists every occurrence of an entry with its decoded neighbours.
- `r2239_groups.txt`: transcription of R2239 (from the DECODE photographs). `r2239_decoded.txt`: the output.

## R2239 reading (21 Sept 2026)

Full text in `r2239_reading.txt`. Two stages:

1. With the R2237 table alone, 59% of groups; with context inference (Paris, Londres, milord, Elgin, Haugwitz,
   comte, république…), 70%, enough for the sense: a conference between Haugwitz and Lord Elgin on a Prussian
   démarche in France for the Orange restoration and the Dutch colonies.
2. A search of Colenbrander, *Gedenkstukken der algemeene geschiedenis van Nederland* II (1906), found the body
   printed as no. 752, pp. 910–911, "De Erfprins aan Prins Frederik, 12 Maart 1796" (from the Huisarchief):
   `gedenkstukken_752.txt`. Aligned as a crib it fixed the remaining entries (208 défavorables, 203 …ir,
   209 désireroient, 219 instructions, 159 constant, 115 abondance, 202 avantageux, 79 cabale, 36 chiffre,
   40 grand, 95 rassemblement, 176 journal, 29 vous, 19 larmes, 114 misère, 87 habitude …), and those read the
   **opening paragraph, which Colenbrander omits** (his text starts "Le comte de Haugwitz a fait", where the
   cipher has "Et il a fait"):

> La conférence que j'ai annoncée comme devant avoir lieu le huit entre Haugwitz et Elgin s'est effectivement
> tenue, et Lord Elgin m'a déjà communiqué le résultat, dont je [vais?] rendre compte, tandis que le comte
> Haugwitz me dit avant-hier au bal du Roi qu'il viendroit un de ces jours chez moi pour me parler sur cet objet.

The rest reads as printed, with small variants (cipher "sur cela" for "à cette demande", "avoit" for "jouissait
de"). The print was found after 70% had been read without it; it was then used as a crib (contamination: yes,
for the body). Grades: opening H except "[vais?]" (entry 244, once, I); body H (cipher and print agree).

The list rebuilt so far is in `key_wordlist.txt`; it is partial (entries not used by R2237/R2239 unknown) and some
R2239 marks were misread in transcription (e.g. groups decoding as "tude" where the print has "les", entry 87);
the reading rests on the aligned sense, not on every group.

## What stays open

- R2239: entry 244 ("je [vais?] rendre compte") only. A few groups in the body still decode wrongly because of
  misread marks; the print settles those words.
- R2236: a different list, now its own entry (`targets/r2236/`).
- The last line of R2237 p. 7 (after "la proposition") is not in the contemporary decipherment and was not read.

## Log

- 21 Sept 2026 (later): Gedenkstukken II no. 752 found (Huygens retroboeken search for "Elgin"); crib alignment;
  opening read; full reading.
- 21 Sept 2026: images fetched with the DECODE cookie (14 PNGs, kept out of git). R2237 found to carry its own
  decipherment; system worked out and table rebuilt; R2239 transcribed and read in part. R1892/R2242 (other Orange
  ciphers of 1795) use a different system (6×6 digit square).
