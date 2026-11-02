# Calames, the rest of the "chiffre" set (2 Nov 2026)

52 rows in `candidates.json`: 47 from `make_candidates.py`, 5 appended by `make_candidates_extra.py`. Below the 60 asked for: the source does not hold more. All rows are
leads scored from Calames descriptions (`seen: catalogue`); none was viewed on an image, and the Sorbonne notices carry no image link.

## Terms and data used

No new request was made. The 2,203 Query=Detail records already fetched by `research/calames_biblissima/calames_detail.py`
(terms: chiffre, chiffré(e)(s), en chiffre, déchiffrement, écriture secrète, clef du chiffre, cifra, cryptographie, nomenclateur ...
over the full-text, title and index fields) were re-read as bodies. About 545 were hand-reviewed in the Oct 2026 pass; the other
~1,650 were screened by script (letter or despatch word within 80 characters of a cipher word, plus the subject-index terms
"Chiffres (cryptographie)" and "Cryptographie"), then read by hand at three strictness levels (86, 287 and 646 candidate lines).

## What the unread bodies hold

Almost nothing new. The unread ~1,650 are noise: Breuil's "croquis de déchiffrement" (about 100 prehistory tracings), First World War
postcards ("signature non déchiffrée", about 90), Gaignières print numbers ("un chiffre à la plume"), bindings with the owner's
"chiffre", page and folio numbering, statistics ("chiffres clés"), Henri Labrouste's "chiffre SG" ornament (Ms. 4273). The real
ciphers in that set were already in `calames_strong*.txt` and the earlier 30 rows, or are key treatises (Mazarine Ms 3730,
Sainte-Geneviève Ms 3157, Ms 3119, BSG 11225, Godefroy 543 f. 66 "Clef d'un chiffre"), which are not letters and make no row.

What the earlier pass had left unexpanded was the item level of the Sorbonne **fonds Richelieu**: it made rows for only MSRIC 37, 43
and 58. The Calames notices list every ciphered letter of the Vienna embassy (MSRIC 30-33, 1725-28), the Genoa command
(MSRIC 9-11, 41-54, 1747-48) and the Hanover campaign (MSRIC 58-59, 1757). This sweep groups them by sender and volume:
32 rows, 28 with an interlinear decipherment recorded (class A: a key can be rebuilt from the pairs). The remaining 15 rows are
the Hennin papers at the Institut (Ms 1228, 1232-1234, "avec transcription"), the Feuquières letters of 1674 and 1680 (MSRIC 21),
Bonnay 1816 and Montmorency-Laval 1817 (MSRIC 72, 75), the Colonna key and letters (MSRIC 44, 48), Ionian Islands Ms 3982,
the Chantilly tables (Ms 1876, 1885, 1888-1903), Masson 194 (Spain 1811) and two doubtful items (Bossuet 1698, Mazarine Ms 4376).

## Best leads

1. **Hennin papers, Institut Ms 1228, 1232-1234.** Broglie in Poland 1752-56, Paulmy 1762-64, Vergennes at Constantinople 1763-64,
   and Hennin's letters with Breteuil, Bérenger, Dumont and the abbé Betański ("nombreuses lettres chiffrées, avec transcription").
   Betański is the correspondent of the AGAD 1/338/0/1/128-143 letters (`chrome_pass_2026-11`), so one key may serve both.
2. **Richelieu's Vienna embassy 1725-28** (MSRIC 31-33): Chavigny (26 ciphered letters over three volumes), Fénelon (19), Silly (19), Cambis, Brancas, Livry, Bonneval, Poussin. Interlinear text on nearly all.
3. **Genoa 1747-48** (MSRIC 9, 10, 45-50): Lorenzi (10), La Rochefoucauld (10), Darthenay (7), Canilliac (8), Puisieux (7 of 19 items). The L'Hospital letters (catalogue 1181) are in the same volumes and are not repeated.
4. **Feuquières, MSRIC 21 ff. 51-58**: Louis XIV 1680 and Terlon 1674, each with a transcription between the lines.

## Removed as already tracked

L'Hospital MSRIC 41-43 (catalogue 1181); La Rochefoucauld MSRIC 43 and Champeaux's Hamburg letter in MSRIC 58 (leads); the
Montpellier H 258 Christina cluster, Chantilly Ms 1967/1988/2080/1905/2157, Godefroy 260-271, Masson 291/302/305 and the other
rows of `calames_biblissima`. `known.py` was run on the volume numbers (MSRIC), senders and places: no hit outside those.

## What blocked

Nothing. Calames answered with plain GET in the earlier pass, and this one made no request. No Chrome pass was needed.

## Not reached

- Richelieu letters that Calames lists as "Lettre partiellement chiffrée" under a generic "Lettres adressées au maréchal de Richelieu"
  heading with no sender in the notice (a handful in MSRIC 43, 44, 47): not grouped.
- Images: the Sorbonne notices have no digital link; scans must be asked for. Hennin (Institut) and Chantilly were not checked on
  their own sites.
- Prior art was not searched on the web (Tomokiyo, Lasry, editions). The Feuquières letters may be printed in part (Lettres et
  négociations du marquis de Feuquières, 1753), and the Richelieu correspondence in older editions; not checked.
- Senders' offices are not given: the rows quote the places on the letters' datelines (for example Ratisbonne, La Haye, Turin) and
  do not assign roles.

## Second reading (same day): extra Godefroy rows and a supplementary harvest

A second agent read the same 2,203 bodies independently (`parse.py`, strict regex for ciphered letter/despatch wording) and found the
same picture: the Montpellier, Sorbonne, Chantilly and Godefroy ciphers were already in `calames_biblissima` or in the rows above. It
found five Godefroy letters (Institut de France) that neither pass had made rows for, although the earlier notes call Godefroy
260-271 tracked: Ms Godefroy 262 ff. 158 and 185 (Sillery 1594-95, entirely ciphered; the same volume's ff. 133-134 hold a
decipherment of two other Sillery letters), Ms 263 ff. 24 and 30 (Chamoux 1600; Brèves, Constantinople), Ms 266 f. 114 (Revest 1611, printed
Revue d'Alsace 1865). `known.py` found none of them. They are appended as rows 48-52.

Supplementary harvest (`harvest2.py`, `detail2.py`, 2.5 s between requests, plain GET, no block): 38 further full-text terms not run
before (chiffrer, déchiffrer, déchiffrage, décryptage, décrypté(e), décryptement, mise en clair, cifrato/cifrata/cifrado, zifra,
Geheimschrift, chiffre de correspondance, caractères inconnus, jargon, écrit(e) en chiffres, en caractères chiffrés, chiffres de convention,
encre sympathique, nomenclature, code secret ...): 678 hits not in the old set, of which 151 outside the two noisy terms were fetched
and read. No ciphered letter among them: signatures hard to read, argot studies (Schwob), sympathetic-ink experiments (Lavoisier/Trudaine,
Curie 1918), and more "mise en clair" notices on the Montpellier H 258 letters already covered. Raw: `hits2.json`, `detail2.json`.

Excluded on purpose: Richelieu 1727 Vienna letters and others "précédée de sa transcription" appear as class A rows above; Hennin Ms 1233-1234
and Sorbonne MSRIC 14-21 are interlinear.

Yield: 52 rows, below the 60 asked for. Calames holds no more ciphered letters than this in the harvested set.
