# Sarmiento's cipher table (Besançon BM Ms 2093, ff. 100-103): partial key material for leads 1085/1086

Status: partial key material, not a target. Table transcribed and frozen; one pre-registered check on a glossed letter of the same volume gives 0.697 against at best 0.103 for 200 shuffled tables (our bar was 0.85, so partial, not validated). Not tested on the RAH originals of leads 1085/1086, which we have not seen.

Brice Dudout, with Claude, 9 Nov 2026. Follow-up to issue #346.

## Source
- **Besançon, Bibliothèque municipale, Ms 2093**: "Tome IV : correspondance du cardinal-infant don Ferdinand avec Antonio Sarmiento (8 février - 29 novembre 1639)", 118 ff. It belongs to Ms 2090-2115, "Correspondance diplomatique d'Antoine Brun, 1636-1656": 20th-century copies by the Vicomte Albéric de Truchis de Varennes of the original letters in the Archives générales du Royaume, Brussels (gift of Truchis de Varennes). The library record notes: "f. 100-103 : table des chiffres de la correspondance d'A. Sarmiento".
- Record and images on Mémoire vive: https://memoirevive.besancon.fr/ark:/48565/bdlj8qv932pr (table = views 116-119; checked letter = f. 24, view 31; other glossed cipher letters on views 27-41).
- **No image is attached or derived.** Mémoire vive states "Tous les droits de reproduction sont réservés" and asks that any publication of unpublished documents be notified to the library; the library is being notified of this transcription (message prepared 9 Nov 2026). Please cite as "Besançon BM Ms 2093, ff. 100-103".
- Our write-up (FR/EN/JA, with the whole table as text): https://bdudout.github.io/europe-chiffree/en/sarmiento-1639.html

## Files
- `table_ms2093.tsv`: the frozen transcription (548 rows; SHA-256 6d2f8d68aa3b57a74eb7d4b1c9b8cba1751a7d7588e112eed76cea0608fdc6cd). Columns: view, folio, section (N = numbered table 1-326 on ff. 100-102; S2 = unnumbered columns A-H on f. 102; G3 = three-letter groups on f. 103), line, column, code, value, certainty (sûr / douteux / vide), note (in French). Spelling of the copy.
- `check_f24.json`: the single measurement (461 of 661 glossed tokens decoded exactly as the interlinear gloss = 0.697; all 706 tokens 0.653; 200 shuffled tables, seed 20261109: max 0.103, mean 0.005).

## The table
A Spanish nomenclator: 1-30 letters (homophones: three for i, two each for a, e, o, u; then va ve vi vo vu, ca), 31-90 syllables in series (ce ci co cu, sa..su, da..du, la..lu, al..ul, cha..chu, fan..fun, man..mun, van..vun, tan..tun; que x3, de x2), 91-326 words and names in rough alphabetical order (213 numbers have a value; the rest are blank in the copy): Duque de Baviera / Lorena / Savoya, Dios, Flandes, Francia, Fran.co de Melo, emperador, Esguicaros, Italia, marques de Leganes, M.is de Castaneda, Milan, Napoles, principe Thomas, Piamonte, Rey... f. 102 adds unnumbered syllable columns, a letter-for-letter column (C written, D plain: p = n, x = u, d = g...), underlined capitals for words (B Fondamento, F guerra, M gente, R governo, O Genova), and signs; f. 103 has three-letter groups for words (cli batalla, cru Borgoña, gle cardinal, Iut S.M., luc secreto, ral Valtelina, nuf V.M....).

## The check (pre-registered, one measurement)
Protocol hashed before any cipher page was opened (SHA-256 4656a6e6...; addendum dd732192...). The cipher of f. 24 was transcribed on strips with the interlinear gloss masked (706 tokens, SHA-256 b133cf49...), decoded mechanically with the frozen table, then compared with the copyist's gloss, read afterwards: **0.697 (461/661) against max 0.103 for 200 shuffled tables**. Pre-registered bar 0.85: **partial, not validated**. No second measurement.

Post-hoc analysis of the 200 misses (no evidential value): mostly our reading of the table, not a different system. (1) Columns A and B of f. 102 are cipher/plain pairs line by line (an = pa, on = po, at = ma, it = mi, ax = fa, ha = na, he = ne, hi = ni, ho = no, ya = ra, ye = re, yo = ro, ap = xa, ut = mu, et = me); we had left them unpaired (108 misses). (2) Nos. 3 and 2, read "2" and "ʒ" in the table, are r and n in the gloss. (3) An un-underlined H stands for t, distinct from underlined H = gracia. These corrections are **not** in the frozen TSV and have not been measured.

The plaintext of the Besançon letters is given by the copyist's gloss: no new reading is claimed.

## Why it matters for leads 1085/1086
RAH, Salazar y Castro A-87: Philip IV to Sarmiento (ff. 16-140, 17 Mar 1638 - 31 Dec 1639) and the Cardinal-Infante to Sarmiento and Saavedra (ff. 256-311, 1638-39), mostly in cipher; per the RAH finding aid (Daniel's vetting of 29 Oct 2026) about half have period decipherments bound beside them, and several Philip IV letters of 1639 (30 Jan, 19 Feb in part, 17 Jun, 22 Nov, 31 Dec) have none. Same correspondence and years as Ms 2093, so this table is very probably the key, or a close relative. If A-87 images are obtained, the bound decipherments give a held-out test and the bare letters can then be read. A reproduction request to the RAH is prepared on our side.

## Credits
Daniel Bourdeau (leads 1085/1086); Bibliothèque municipale de Besançon / Mémoire vive (Ms 2093); Rafael González Cañal, "Tres escritos desconocidos de D. Diego Saavedra Fajardo", Murgetana 73, notes 8-17, for Sarmiento's 1638-39 mission.
