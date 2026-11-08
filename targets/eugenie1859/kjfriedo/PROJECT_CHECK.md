# Project check of the f12 alignment and the Prince Napoléon dictionary (8 Nov 2026, issue #194)

What was checked here of Jozef Krajčovič's alignment (`f12_alignment_v2.tsv`) and dictionary (`prince_key_dictionary_v2.tsv`), by an AI
model (Claude), with the six Archives nationales images in `images/`. The BnF scans of NAF 11355 are not reachable from the
project, so the transcription of the f12r groups themselves (`prince_family_tokens_f7_f10_f11_f12.tsv`) was **not** compared with a
scan. No human has repeated this check.

## 1. The values written on the contemporary decipherments (viewed on the images)

Four of the six images were read here at the size shipped (1400 px): `img140` (f7), `img184` (f10), `img185` (f11 as received) and
`img186` (the Emperor's reply of 11 June). Every value of the dictionary that the issue lists for them is written over the
groups: f7 1817 la, 2079 division, 415 d', 150 Au, 903 te, 1126 mar, 718 re (written "ou R"), 135 ne, 404 vien, 764 dra, 116 que, 1308 par,
543 terre; f10 2157 à, 1327 Plaisance, 612 deux, 796 mille, 1293 Français, 114 à, 1818 Fl-, 1828 -or-, 541 -ence; f11 as received
2081 sera, 2162 évacué, 856 bientôt, 2218 d'Autemarre, 665 qui, 2080 est, 114 à, 832 Pavie, 432 avec, 648 tes, 1472 troupes, 1029 venir,
804 à, 1327 Plaisance (the first group of the line reads 1326 or 1327 and carries "impro" and "(Plaisance)" above it); reply 2218
d'Autemarre, 863 qu'à, 486 -près, 131 demain, 114 à, 1327 Plaisance, 432 avec, 430 de la, 951 position, 504 des, 226 Autrichiens, 137 toute, 2269 ton,
713 corps d'armée, 2157 à, 461 Lodi. The minute `img197` (page 1) has the underlined opening and the closing words; its text
agrees with the plaintext of f12 as given ("Si Plaisance est occupé par nous, oui je puis marcher sur Modène ... à d'Autemarre à Parme ...
par l'Abetone ... où il y a 10/m Autrichiens ... Massa et puis par Pontremoli en Parme", with deletions and insertions). `img198`
(page 2 of the minute) was not viewed.

## 2. Does the alignment hold? Two measures from the files

**Values from outside f12.** 46 dictionary codes carry a value written on a contemporary decipherment of another telegram (f7,
f10, f11F, reply). 15 groups of f12 carry such a code; in all 15 the alignment's meaning is the same word as the external value (10
identical strings and 5 that differ only by a variant of form: "(Gal) d'Autemarre" and "d'Autemarre", "~te" and "~te~", "ser- (serai)" and
"sera", "d'/des" and "des", "ven- (venant)" and "venir"). These are not circular for the codes whose value was not used to build the
alignment (the issue names 903 te, 1327 Plaisance, 796 mille, 504 226 des Autrichiens, 863 qu'à); the project could not tell from the
files which of the 15 were used.

**Repeats inside f12 against shifted alignments.** 23 pairs of f12 groups carry the same code. In 18 of the 23 the alignment gives the
two groups the same plaintext unit. When the same plaintext units are shifted against the groups by 1 to 15 places, the best shift gives
2 of 23 (mean 0.2); 1,000 random shuffles of the units give at most 2 (mean 0.1). So the alignment is not an accident of counting: a
wrong alignment does not repeat words on repeated codes.

## 3. What this does not settle

- The transcription of the 135 f12r groups, and of the f7, f10, f11 and f12 token streams, against the BnF scans.
- The tier B and C meanings (single occurrences placed by counting between anchors), groups 87 to 97 (Lucques ... littoral ... Massa), groups
  78 and 110, the conflicts 799 and 1149, and the 133 against 135 count.
- That the key is the same code as Lasry's Emperor–Empress key (it is not read as such here): `f11r` ancien is a different codebook and
  `f11r` nouveau probably belongs to another telegram.
- A write-up: the Prince Napoléon key would be its own target and page (one key, one entry), after the BnF groups have been compared with the
  scan by someone who can reach Gallica, and after the tier A, B and C values are frozen and a stretch is held out. The measures above are
  consistency checks on the contributor's own alignment, not a held-out test of a frozen key.
