# baluze1709: Étienne Baluze (Paris) to the cardinal de Bouillon, 10 May 1709, Médiathèque Georges-Delaw, Sedan, fonds Gourjault, carton 199: cipher transcribed, contemporary decipherment aligned, partial key

Status: in progress (content existing: the contemporary interlinear decipherment gives the sense of every cipher passage but three; key partial, 5 sure values, 31 probable, 4 person signs fixed by the decipherment; no #728 count is claimed while the key is partial). Next step: other ciphered letters of Baluze to Bouillon from carton 199, asked for through the library, to fix the key.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. No new reading is claimed: the letter carries a contemporary decipherment between the lines. What is new is the transcription of the cipher, the alignment of the decipherment on it, the finding that barred groups are nulls, and a partial key, with what the decipherment fixes kept apart from what is inferred.

## Source and credit

Médiathèque Georges-Delaw, Sedan, fonds Gourjault, carton 199, piece 8, ff. 24-26 (f. 26 in clear). Signed by Baluze; a Charavay sale label (December 1906) is attached. The folder of the carton reads "1 à 217", most likely folios.

Images: Médiathèque Georges-Delaw, Sedan (fonds Gourjault, cartons 170 and 199), obtained through the Société d'histoire et d'archéologie du Sedanais (SHAS). The form of this credit has been asked of the SHAS and will be adjusted to its reply.

**No image is in this repository, and none may be added**: the photographs were sent for research use only. The shelfmark is given instead.

## The letter

Baluze has shown the cardinal's letter of 30 April to the abbé Bignon, who will never miss an occasion to serve him with the chancellor and elsewhere; but the cardinal must not be surprised if "things do not go so fast": the chancellor has to be brought back "from his prejudices". The letter ends on the advice to write "franchement" and "fidelement". In the decipherment's words (cipher passages in italics, clear words of the letter in roman):

> J'ay fait voir à *M. l'abbé Bignon* la lettre du 30 avril, qu'il ne *perd* ny ne *perdra jamais aucunes occasion* de vous *rendre ser[vice?]* (…) *M. le chancelier* & ailleurs, s'il en a les occasions. Vous estes à *M. le cardinal de Bouillon* qu'il ne doit pas s'estonner si les choses *ne vont* pas *si viste* que la personne (…) faire *revenir le chancelier de ses préventions* (…) que *Baluze* me paroit bien persuadé que *l'abbé Bignon* [...] (…) que j'escris à [66 + 95] (…) rien de mieux que *d'escrire franchement* (…) *fidelement*.

"(…)" is clear text not transcribed here; `[...]` and `[66 + 95]` are cipher with no legible gloss. This is the decipherer's text, not a reading of ours, and it is not counted.

## The system

Two-digit groups (00-99) for letters and syllables, with homophones (66/39 per, 67/13 d); a small nomenclator of signs for persons (ɸ, +, J, combined as ɸ+, 0 ɸ, +J, J+); and **barred groups, which behave as nulls**. The bars stand at the height of the clear; the decipherer never writes a syllable over a barred group, and he puts dashes in his clear at their places ("ne vont —", "si viste — —", "franchement — fidelement —"). With the barred groups removed, the words of the decipherment fit the groups closely: perd = 66 67, perdra = 39 13 75, si viste = 82 92 86, franchement = 17 75 35 06 36 51, fidelement = 27 16 46 95 51. One place goes against it: in "vont" (93 95 [35 barred] 51), the barred 35 may stand for n, as 35 does in "franchement". The same numbers occur barred and unbarred (02, 13, 35, 36, 48, 51), so the bar, not the number, makes the null.

## The key (`key.tsv`), in two layers

**Fixed by the decipherment** (`decryption.txt`): which groups stand under which word (the place of each word of the clear and the dashes bound it), and the person signs, each glossed by a name: ɸ+ = Bignon (twice), 0 ɸ = the chancellor (twice; the 0 is a separate digit), + = the cardinal de Bouillon (once), +J = Baluze (once; the sign after + is not quite the J of J+). J+ and "66 + 95" have no legible gloss; "M. le C. Bouillon" written at the head of f. 25 may be the gloss of 66 + 95 or the address.

**Inferred** (the value of each group inside a word):

- sure, the same value in two independent words: 16 = de, 34 = n, 56 = ne, 75 = ra, 76 = re;
- probable, one word and the simplest split: 31 values (66 per, 67 d, 39 per, 13 d, 40 ja, 32 ma, 97 i, 02 s, 11 d, 48 s, 08 c, 62 r, 77 i, 41 p, 87 tions, 81 s, 49 es, 82 si, 92 vi, 86 ste, 93 vo, 51 t/ment, 17 f, 35 n, 06 ch, 27 fi, 46 le, 04 au, 14 cu, 60 ne?, 43 sion);
- in conflict: 95 (o in "vont", me/e in "fidelement"), 91 (ve in "préventions", ni/e in "revenir"), 57 (ca in "occasion", r/nir in "revenir"), 36 (e in "franchement", s or o in "aucunes occasion"); "76 46 76" in l. 4 does not give "service"; the groups before the signs (61, 64, 70, 96, 97, 99) may be titles (M., le, l'abbé) or letters.

About 60 distinct groups occur outside the nulls. The conflicts cannot be settled from one letter.

## Counts

No count under rule #728 is claimed. A word is sure only when the decipherer, the key and the context agree, and here the key is mostly inferred from the decipherment itself, so it cannot check it. The decipherment covers every cipher passage except "66 + 95" (l. 9), "J+" and the end of l. 8.

## Files

`transcription.txt` (groups line by line, with the clear words of the letter in comments), `decryption.txt` (each word of the contemporary decipherment, the groups under it, the nulls, the values of the key), `key.tsv` (partial key in two layers).

## Prior work

Nothing in `catalogue.json` or `research/leads.json` (main 42068aa8, 19 Nov 2026), in the targets, or in the open pull requests for Gourjault, Baluze, Bréant, Réveillon or Sedan (the only Baluze hits are BnF fonds Baluze shelfmarks of other targets); no printed edition of this decipherment found by web search (18 Nov 2026). The contemporary decipherment is credited as prior solution.

## Remaining gaps

- 31 values seen in one word only, and four conflicts (95, 91, 57, 36) (blocker: too-short).
- The groups before the person signs, J+ and "66 + 95" (blocker: too-short).
- One group struck through by the writer (l. 10) and one under a blot (l. 8) (blocker: illegible).
- The clear text of ff. 24-26 not transcribed in full (blocker: not-attempted).

## Escalation

- Two or three other letters of the same series from carton 199 (pieces next to piece 8 first), ideally with their decipherment, or the table itself, would fix the key. A question on the other ciphered pieces of cartons 170 and 199 was sent to the library on 18 Nov 2026.

## Tools

Claude Opus 5.5 agents (transcription from the photographs, alignment, key, write-up); Brice Dudout obtained the photographs and answered a blind reading sheet on doubtful shapes (18 Nov 2026, two controls passed: 67 not 65 in "perd", 57, 46, the separate 0 of "0 ɸ"). No model API calls.
