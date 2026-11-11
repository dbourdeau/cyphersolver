# Caulaincourt to Napoleon, Congress of Châtillon, 1814: the undeciphered letter of 25 February (AN AF/IV/1676 no. 131) and its keyed siblings

Status: in progress (partial key rebuilt from two contemporary decipherments in the same key; no. 131 not yet read; more siblings need the archive).

Catalogue no. 534, archive request ar-240. Contributed by Jean-Loko (archive visit of 7 Nov 2026, photographs),
with Claude Code (Claude Opus 5.5 and Sonnet 5.5) for the transcriptions and the key alignment.

## The visit

Archives nationales, Pierrefitte-sur-Seine, 7 Nov 2026. Plaquettes 4/III and 4/IV of the Secrétairerie d'État
(Relations extérieures) are both in carton **AF/IV/1676** (call numbers from the AN inventory FRAN_IR_003828, exported
from the virtual reading room: 4/III and 4/IV in AF/IV/1676, 2/V in AF/IV/1677, 1/II in AF/IV/1678, Prusse in AF/IV/1690).
The carton was served on microfilm. The pages were photographed from the reader screen with a phone (48 photos); the
images are not committed and are held by the contributor. The screen's moiré makes some digits uncertain (2/7, 4/8, 3/5).

## The documents

| no. | date | folios | what it is | state here |
|---|---|---|---|---|
| **131** | 25 Feb 1814 | 890-892 | Opening in clear (f. 890r), then 465 groups, clear closing and autograph signature. Inventory: *en grande partie chiffrée (et sans le déchiffrement)*. No decipherment on or with it. | **the target**; transcribed twice, not read |
| 130 | 25 Feb 1814 | 884r-v (continues f. 885) | Cipher with the **contemporary decipherment written under each line**. The inventory does not say it is ciphered. | 273 groups transcribed with the interlinear text and word positions |
| 170 | 6 Mar 1814 | 969-973 | Cipher, 1,346 groups, with a **pale pencil decipherment word by word under most lines** (not in the inventory). Report of Floret's visit with Metternich's letter. Clear closing, cipher postscript. | transcribed twice; glosses read in part |
| 171 | 6 Mar 1814 | 974-976 | Contemporary decipherment of no. 170 (970 words), headed *Déchiffrement*. | transcribed |

Inventory corrections (FranceArchives, plaquette 4/IV): nos. 170-171 are given as f. 968, but no. 170 is ff. 969-973 and
no. 171 ff. 974-976; no. 172 (*le déchiffrement manque*, given as ff. 974-981) must therefore start at f. 977. No. 130 is
a cipher with an interlinear decipherment.

### The clear opening of no. 131 (f. 890r)

> Sire, J'ai reçu le soir à cinq heures la note dont j'ai l'honneur d'envoyer copie à Votre Majesté. Le Poste autrichien
> qui servait de Sauvegarde à la ville et de garde d'honneur aux Plénipotentiaires s'est retiré par la route de Langres
> avec le Général qui le commandait. J'ai donné sur le champ des ordres au Maire pour qu'il réunisse une partie de la
> garde nationale pour veiller à la sûreté de la ville et à ce que les membres du Congrès jouissent de toute leur
> inviolabilité. Nous n'avons cependant que d'une manière incertaine la nouvelle de l'arrivée de quelque troupe légère
> française à Saint-Parre. Un paysan venant de Barre[?] dit qu'il y a encore de l'infanterie ennemie et que le pont sur
> la Seine est coupé. Les secrétaires de Lord Castlereagh sont toujours là et l'attendent. Les Lords Cathcart et
> Aberdeen ont envoyé des invitations pour Dîner chez eux Demain et après Demain. [cipher follows]

A marginal note in another hand explains the enclosed note of the plenipotentiaries (25 Feb): it asks the duke of
Vicenza for the safety due to a neutralised town, Châtillon, which the events of the war had placed within the French
lines.

### No. 130, read from its interlinear decipherment

Bassano, answering on 23 Feb a private letter of Caulaincourt of the 19th on the Emperor's orders, quoted it "avec une
inexactitude que j'aime à croire involontaire". Caulaincourt had written that peace "seroit toujours honorable si elle
étoit vraiment raisonnable"; Bassano turned this into an assurance that "il ne tient qu'à nous de faire une paix
vraiment raisonnable", and asked by what overtures Caulaincourt knew which allied conditions were firm and which could
be given up. The text breaks off at the foot of f. 884v; f. 885 was not photographed.

## The system

A numeric nomenclator to about 1200 (the highest group read is 1200), groups separated by dots, some underlined. It
codes whole words (paix, que, les, pour, dans), syllables (Bassano = 952 · 959 or 663 · 395) and some letters. Frequent
words have homophones (que = 264, 669, 1191). The numbers of frequent words are unrelated, so the table is not
alphabetical as far as checked.

**One key for 25 February and 6 March.** The values written by the decipherer of no. 130 (798 = par, 84 = en, 904 = une,
910 = lettre, 800 = à, 18 = et) are those found independently by aligning no. 170 with no. 171. No. 131, written the same
day as no. 130, is presumably in the same key.

## Transcriptions (`transcriptions/`)

Each cipher was read twice, independently, from the photographs (reading A with Claude Opus 5.5, reading B with
Claude Sonnet 5.5), and reconciled group by group with `scripts/consensus.py`. A group is firm when the two readings
share a single value; otherwise the consensus keeps the candidate set (`?[a|b]`) or both readings (`{A:… | B:…}`).

| file | agreement | open disagreements |
|---|---|---|
| `n130_consensus.txt`, `n130_merged.txt` (with the interlinear text T and word positions P) | 95% | 12 |
| `n131_consensus.txt` | 94% | 24 |
| `n170_consensus.txt` (+ `n170_gloss_anchors.tsv`, 440 pencil glosses read with their group) | 83% | 207 |

`n171_decipherment.txt` is a diplomatic transcription of no. 171; `n171_plain_for_alignment.txt` drops the lines that are
in clear in no. 170 (opening, closing paragraph, signature). Reading A of no. 131 counts the f. 890v lines from the
clear line, so its L02 is reading B's L01.

## The partial key (`key/`)

`scripts/aligner_multi.py` rebuilds one table from all sources at once by soft EM alignment: each number takes a unit
(a piece of a word, a whole word, two or three short words, or nothing), uncertain digit readings stay candidate sets,
the 170 pencil glosses and the 130 word positions are anchors, and a fixed length penalty per group stops degenerate
solutions (frequent numbers as nulls, rare ones swallowing whole phrases). Run:

```
python scripts/aligner_multi.py --paire transcriptions/n170_consensus.txt transcriptions/n171_plain_for_alignment.txt transcriptions/n170_gloss_anchors.tsv --interligne transcriptions/n130_merged.txt --sortie key/key
```

Result (`key/key_partial.tsv`, alignment in `key/alignment.txt`): 582 numbers aligned, **105 with a firm value** (seen
at least twice, posterior at least 0.6). The 130 lines align almost word for word with their interlinear text. Values
seen once in no. 170 are not reliable yet.

## No. 131 so far

`key/n131_trial_decode.txt` (`scripts/dechiffrer.py`): 83% of the numbers of no. 131 occur in nos. 130 and 170, but only
140 of 481 groups take a firm value, and the result does not build sentences. **Nothing of no. 131 is read.**

## Print

- Fain, *Manuscrit de mil huit cent quatorze* (1823), appendix no. 29: a Caulaincourt letter to Napoleon dated Châtillon,
  6 Mar 1814 (*La question qui va se décider…*), printed in clear (`print/fain1823_no29_6mar1814.txt`, from Project
  Gutenberg 33796). It is not the text of no. 171; it is a candidate for no. 172 (same date, *le déchiffrement manque*),
  to be checked against its length and structure.
- Houssaye, *1814* (1888), quotes Caulaincourt's letters to Napoleon of 24 and 27 Feb and 1, 11 and 13 Mar 1814 from
  "Arch. des Affaires étrangères, fonds France, 668", probably Mémoires et documents, France 668 at La Courneuve, where
  clear copies of the Châtillon correspondence may survive. Not checked.

## Remaining gaps

- **No. 131, the whole cipher**: needs physical access. The key is too thin; more decipherments in the same key are in
  the same carton (below).
- **No. 172** (6 Mar 1814): needs physical access; not photographed, starts at f. 977.
- **Nos. 191-192** (mid-March): needs physical access; not photographed.
- **Digit readings of no. 170**: illegible on the phone photographs for 17% of groups; images exported from the reader
  should settle most.

## Escalation

1. Export the images from the microfilm reader (the AN reader offers saving) instead of photographing the screen.
2. Photograph the interlinear decipherments of plaquette 4/IV: 169bis (f. 968), 179 (11 Mar), 185 and 187 (13 Mar),
   and the rest of no. 130 (f. 885).
3. Photograph the cipher/decipherment pairs 161-162, 163-164, 165-166, 168-169, 173-174, 176-177.
4. Rerun `aligner_multi.py` with them; apply the key to no. 131 and fill the holes from context, marking every
   context value doubtful until it holds at each occurrence.
5. Photograph no. 172 and test Fain no. 29 as its plaintext; photograph nos. 191-192.
6. At La Courneuve, look for Mémoires et documents, France 668 (Houssaye's citation) and a 1814 cipher table.
