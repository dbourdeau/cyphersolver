# Bouillé to the minister, Martinique, 29 Mar 1780, no. 398 (ANOM COL C8 A 79 ff.57-59v)

Status: draft for Daniel (nothing pushed). Brice Dudout with AI agents (Claude Opus 5.5), 23 Nov 2026. Images:
Archives nationales d'outre-mer (France), COL C8 A 79, IREL FRANOM23_C8A_079_0079-0087 (free reuse, ANOM decision
2018-1, with credit); not in this folder. Same code as targets/bouille1778, martinique1778, grassebouille1779
(Bouillé's "chiffre du 25 avril 1778"); one key, one entry: Daniel may fold this into grassebouille1779.

## Prior work
Two cipher passages (f.58v, 166 groups; f.59, 197 groups). Image 0085 is a **modern archivist's translation**
("Traduction des passages chiffrés", sheet headed Ministère d'État - Affaires culturelles), as for no. 415 (f.70,
image 0106) used in grassebouille1779. Not in the catalogue or targets (checked 23 Nov 2026). Print not searched.

## Test (protocol hashed before any computation: PREREG_fr.md, SHA-256 bfff864f...)
- Key: K8 of targets/grassebouille1779 (`key.tsv`, SHA-256 6dbabfcd...), unchanged; nulls 163, 586, 257 empty.
- Portion: both passages, 363 groups, vs the modern translation; both hashed before the run.
- **Result: 0.9483 characters; best of 200 shuffled keys 0.2550 (mean 0.157) → pass.** Words 206/232 (88.8%).
- K8 values the run suggests (not applied): 137 (in "rentrer"), 111 (objecté), 835 (eau), 92 (besoins), 702
  (craignent), 425 (sorte), 591 (différence), 571 (désire), 728 (glorieuses), 296 (aucune).

## Content
After news that 2,000-2,500 British troops had reached St Lucia and Vaughan and Prescott were come to besiege St
Vincent and Grenada, Bouillé asked Guichen for three ships to carry the 2,000 embarked men and take St Kitts at once;
Guichen refused, his squadron short of water. The British at St Lucia now fear a siege; Bouillé will supply the
southern islands then cruise with the squadron and 3,000 men; "nous avons manqué un coup superbe qui pouvoit
terminer la guerre". Guichen's instructions forbid risking the fleet or keeping any island.

## Postscript of 11 April (f.59v, not in the modern translation; read with K8 after the test)
`P.S. du 11 avril` 250 278 503 391 361 178 88 103 402 636 / 101 651 361 331 339 776 44 44 641 304 191 251 727 841 516
→ "L'escadre par{t} après-de[main] jeudi au nombre de vingt-deux vaisseaux ; j'ai embarqué tro[is …]".
{part}: 503 = par (K8) + 391 (t?); [main]: 361 178 decode "de bien", read "demain" by sense (11 Apr 1780 was a
Tuesday, so "après-demain jeudi" = 13 Apr, the day Guichen's fleet sailed from Fort-Royal before the battle of
Martinique, 17 Apr 1780). The sentence runs past the foot of f.59v; image 0088 was not downloaded.
