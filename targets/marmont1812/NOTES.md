# Marmont to Jourdan, 1812 (catalogue 751), with Jourdan to Soult, 28 May 1812, and Jardet to Marmont (catalogue 724)

Status: read in part (Brice Dudout, 28 Oct 2026; N.34, Jourdan to Soult, read: 267 of 267 cipher numbers read in their sense, 250 certain, 9 probable, 8 restored from the sense, 0 unresolved; N.73, Marmont to Jourdan, read in part: about 150 of 176 numbers (about 85%); counted in numbers, not words; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Published write-up:
https://bdudout.github.io/europe-chiffree/en/documents.html#jourdan-1812

## Documents

Three pieces of the AHN Depósito de la Guerra collection, all Army of Portugal / King Joseph traffic of 1812 that fell into
Spanish hands:

- **DIVERSOS-COLECCIONES,134,N.73** (PARES https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3109832; catalogue 751): copy of Marmont to Jourdan, Salamanca, 1 June 1812,
  plain text with enciphered passages (176 numbers). Read in part (about 85%), see below.
- **DIVERSOS-COLECCIONES,134,N.34** (PARES https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3156392): contemporary Spanish translation of Jourdan to Soult, Madrid,
  28 May 1812, the enciphered passages left as numbers (267), initialled "Monsalud". **Read** (this folder's main text).
- **DIVERSOS-COLECCIONES,133,N.29** (PARES https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3101366; catalogue 724): Colonel Jardet to Marmont, Paris, 6 March 1812.
  **Existing decipherment**: the AHN piece is itself a "copia descifrada conforme", the full plain text, with the Spanish
  reconstruction of the key attached (image 11): a homophonic cipher of 48 numbers built on Voltaire's line (Tancrède)
  "À tous les cœurs bien nés que la patrie est chère" (1 = a, 2 = t, 3 = o, 4 = u, 5 = s ...), numbers 49 and above being
  nulls. It is also no. 1 of the Scovell file (Oman, Peninsular War V, app. XV). Nothing to decipher.

Eight weeks before the battle of Salamanca, Marshal Jourdan, King Joseph’s chief of staff, orders Soult to reinforce Count d’Erlon’s corps against General Hill, or to send it across the Tagus at the bridge of the Arzobispo if Wellington calls Hill back to him. The letter was intercepted: a contemporary Spanish translation survives in the Archivo Histórico Nacional, with the enciphered passages left as numbers, undeciphered. They read with the table of the 1812 Grand Chiffre.

## System

Grand Chiffre of 1812 (the British “Great Paris Cipher”): a repertory of 1,200 numbers (letters, syllables, words) extended to 1,400 with additions for Spain (1211 = the Army of the Centre, 1214 = the English army, 1300 = Lord Wellington, 1383 = the Tagus); several numbers for frequent words (homophones).

## Key

`key_1812_entries.tsv`: the entries of the deciphering table of the 1812 Grand Chiffre (Service historique de la Défense,
"B n° 30") needed here, read on Jean-François Bouchaudy's photographs (http://www.jfbouch.fr/crypto/napoleon/index.html),
starting from the 226 entries read for King Joseph's letter of December 1812 (https://bdudout.github.io/joseph-napoleon/,
and your `targets/napoleon/`). No cryptanalysis: the external table was applied. The photographs are not reproduced.

## Validation

Mechanical decoding (main value of each entry, no correction by the sense) scored with a French character-trigram model
learnt on an independent text (Marmont's Mémoires, vol. IV, Gutenberg 33807), against 1,000 tables in which the same values
are assigned to the numbers at random. N.34 was held out while the table was being read for 751:
N.34 rank 2/1000 with the frozen entries (−2.184 vs p99 −2.217), rank 0/1000 after the seven re-read cells (−2.145 vs p99 −2.209).
751: rank 9/1000 with the frozen entries (−2.248 vs p99 −2.249, a narrow pass), rank 1/1000 after the re-readings.
Two word-coverage scores tried afterwards did not discriminate (long multi-word entries inflate the permuted tables) and are
not used.

## Reading of N.34

First published decipherment, to our knowledge. 267 cipher numbers. Read: 259 (97.0%), of which 250 certain (93.6%) and 9 probable {x}; 8 numbers do not give the expected value in the table and are restored from the sense [x] (copying errors by the translator, or table cells that cannot be read on the photographs). None is left unresolved.

Files: `transcription_N34.txt`, `decryption_N34.txt` (each line, the value of each number), `reading.md`, `translation.md`.

## Marmont to Jourdan, 1 June 1812 (N.73, catalogue 751)

Same cipher. About 150 of 176 numbers read (≈ 85%); the Spanish copyist's errors (forms of 1, 3/9, transposed digits)
stop the rest. Readable: "C'est qu'il n'y a qu'une certitude absolue et des opérations capitales commencées dans le Midi qui
puissent l'emporter sur les probabilités d'une opération dans le Nord"; "J'écris itérativement au général Caffarelli";
"Il serait bien désirable que le général Drouet suivît les mouvements du général Hill"; "en préparant un matériel
d'artillerie à Talavera". Wellington wrote on 7 June 1812 that he had "one intercepted letter from Marmont to Jourdan; which
I am endeavoring to decipher" (Gurwood, Dispatches IX); it is no. 28 of George Scovell's file (Oman V, app. XV), whose
manuscript decipherment was never printed. Files: `transcription_N73.txt`, `decryption_N73.txt`, `reading_N73_partial.md`
(working notes, French).

## Notes

- The context. On 19 May 1812 Hill took and destroyed the forts and the pontoon bridge of Almaraz, the only solid crossing of the Tagus between the Army of Portugal (Marmont) and the Army of the South (Soult). Joseph, appointed commander-in-chief in Spain, is trying to bring into action d’Erlon’s (Drouet’s) corps, detached from the Army of the South. On the same day Jourdan wrote a parallel letter to Marmont (printed in Marmont’s Mémoires, vol. IV): it has the bridge of the Arzobispo, “difficult for the artillery, but I do not think it impracticable”, and the “eight hundred horse” of the Tagus valley. Already on 7 May Jourdan had given d’Erlon orders in almost the same words (Du Casse, Mémoires du roi Joseph, vol. IX, p. 6).
- The names. Foy’s division (Army of Portugal) was guarding the Tagus valley; Treillard commanded the troops of the Army of the Centre in the Tagus valley; Miravete is the pass and fort above Almaraz; the bridge of the Arzobispo lies upstream, on the Talavera road. Foy’s name is written 1011, which the table gives as “Foi s”: probable reading {Foy}.
- The intercepted copy. The letter survives in a Spanish translation that keeps the cipher numbers as they were, initialled “Monsalud”. The Marqués de Monsalud then commanded Spanish troops in Extremadura; on 11 June 1812 Wellington wrote to Hill that Monsalud believed Joseph had ordered Soult to approach the Tagus, but “did not send me the paper on which he founds this notion” (Gurwood, Dispatches, vol. IX). That paper may be this one; it is only a hypothesis.
- The eight restorations. 208 (renf[or]cer), 598 ([ba]ttre), 88 ([au] contraire), 62 (pas[ser]), 1085 (co[u]vrir), 266 (flan[c]), 981 and 372 (me[ner]) do not give the expected syllable in the table: errors of the Spanish copyist (who at places confuses 1 and 7, 3 and 9, 5 and 6) or cells that the photographs do not let us read. Probable readings: 320 (a T-shape in the table), 525 (“lon”), 1011 ({Foy}).
- The two other pieces of the file. The copy of Marmont’s letter to Jourdan, Salamanca, 1 June 1812 (134,N.73, PARES, catalogue no. 751) is in the same cipher; we read about 85% of it (“… capital operations begun in the South that could outweigh the probabilities of an operation in the North”; “I write repeatedly to General Caffarelli”; “by preparing artillery material at Talavera”), the Spanish copy being too faulty to go further. It is the letter that Wellington says on 7 June 1812 he had intercepted and was “endeavoring to decipher”; it is no. 28 in George Scovell’s file of ciphers, who made a manuscript decipherment of it, never printed (Oman gives only a one-line summary). Colonel Jardet’s letter to Marmont, Paris, 6 March 1812 (133,N.29, PARES, no. 724) is a “copia descifrada conforme”: deciphered at the time by the Spaniards, with the key attached, a 48-number cipher built on Voltaire’s line (Tancrède) “À tous les cœurs bien nés que la patrie est chère”.
- Prior work. Nothing of this letter in Scovell’s list (Oman, Peninsular War, vol. V, app. XV: nos. 26–27 are letters of 26 May to Soult, on the fall of Almaraz), nor in Du Casse (Mémoires du roi Joseph, vol. IX), Marmont’s Mémoires (vol. IV), Jourdan’s Mémoires militaires, Wellington’s Dispatches (vol. IX) or his Supplementary Despatches (vol. VII).

## Remaining gaps

- N.34: eight numbers restored from the sense (208, 598, 88, 62, 1085, 266, 981, 372) - blocker: illegible; copying errors in the Spanish copy or unreadable cells of the table photographs (88 may be 58 and 62 may be 64, to check on the image)
- N.73 (751): about 26 numbers unresolved - blocker: needs-physical-access; the Spanish copy is miscopied at these points; the original in the Scovell papers or the French minute would settle them

## Escalation

Added on review, 27 Oct 2026.

- [x] siblings: 133 N.29 (Jardet to Marmont, 6 March 1812) opened: a different cipher (48 numbers on a line of Tancrède), deciphered at the time; kept as context, not part of this target (one key, one entry)
- [n/a] clear-pages: the Spanish copies translate the clear text only; no decipherment of the cipher passages
- [x] known-keys: the 1812 Grand Chiffre table (SHD "B n° 30") is the key, applied unchanged
- [x] print: Oman (Peninsular War V, app. XV), Du Casse (Mémoires du roi Joseph IX), Marmont's and Jourdan's memoirs, Wellington's Dispatches and Supplementary Despatches searched (contributor)
- [n/a] key-rebuild: the table is known; nothing to rebuild
- [x] retry: the 26 unresolved numbers of N.73 tried as digit confusions of the Spanish copy (contributor); the remedy is the French minute or Scovell's papers
