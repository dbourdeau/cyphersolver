# Trémais to the minister of the Marine, cipher letter, Montréal, 6 Nov 1759

Status: read in part (23 Nov 2026)

Catalogue 1392. ANOM COL C11A 104 ff.346-347v (CABAC_PIAF_60950), 3 images (LAC e000875270-272,
[record](https://nouvelle-france.org/eng/item/details?id=27542)). Charles-François Pichot de Querdisien Trémais, the commissaire
sent in 1759 to work under the intendant Bigot and report on the abuses, to the minister (Berryer). French. About 1,350 number
groups (1,277 in the text, 73 in marginal notes) among clear words. It is the covering letter for a copy of his letter of
22 Sept 1759 (ff.342-343v, record 27540), whose contemporary decipherment is bound at ff.344-345.

## State on 23 Nov 2026

**Deciphered in part with a key recovered from adjacent plaintext** (the September letter and its clear copy), extended from
the letter itself, then every unread or doubtful place retried against the image and the extended key (`retry_346rv.tsv`,
`retry_347rv.tsv`). `reading.md`, counted by `count_reading.py`: 357 cipher words sure, 92 conjectural, 25 unread runs (67 groups,
about 23 words); of an estimated 472 cipher words that is 0.756 sure and 0.951 with the conjectural words. The total is an
estimate (unread runs have no word count), so this is not the README word measure. Under the read bar on sure words: read in part.

Control (`control_frozen_key.py`, `control_frozen_key.out`): the September-only key, frozen (sha256 884d92f0...), applied to
November with the first digit alternative everywhere, scores -2.424 log-probability per character (model fr-1750-nospace) on
the runs it covers; 200 shuffled tables give best -2.617, median -3.247; none reaches the real key. The key file was built
before any November decode, but its transcriber was given a guide list of values that came from issue 810.

What the letter says. Trémais sends a copy of his September letter and adds: however reprehensible M. Bigot may be, for the
pernicious example of "un commerce immense ... d'où sont résultés une infinité d'abus dont il n'a point arrêté le cours" and
for the other faults of his administration, "on ne sauroit néanmoins sans injustice l'accuser d'avoir seul causé tous les maux
qui ont affligé le Canada ni d'avoir seul donné lieu à la prodigieuse augmentation des dépenses de cette colonie: les désordres
ont eu bien d'autres sources". The memoirs without number that came out of the country show the passion that dictated them.
In the posts "le militaire y est absolument despote": works are paid on its certificates, everything leaves the stores and the
provisions go to the detachments on its orders, rations are delivered on notes signed by the majors of the corps; "aussi y
voit-on [beaucoup] de fortunes considérables", down to the simplest infantry officer and the soldier; officers committed "des
bassesses dont un simple soldat eût été partout ailleurs sévèrement puni"; a small number of "officiers de plume" did well too.
Then his plain opinion (partly conjectural): Canada lacked a governor and an intendant and the army a chief; the governor has
good sense and kindness but lost everything by his "facilité"; "M. Bigot a de l'esprit" but could only make a middling
intendant, his aim being "un repos agréable"; the two "n'étoient donc à proprement parler que des fantômes ... incapables
d'opérer par eux-mêmes ou craignant le travail", obliged to rely on subalterns: authority "résidoit réellement dans M. Péan,
aidé de M. Mercier", who "de concert avec les secrétaires des deux chefs les ont également gouvernés". They were backed by a
man (the munitionnaire by the sense, so Cadet; his code number 480 is not confirmed) "tiré de l'état de garçon boucher",
"un homme impayable ... d'une activité que rien ne peut déconcerter", "digne d'estime", "homme de néant, toujours prêt à
obliger", repaid "de la plus basse ingratitude"; "sans lui on eût eu bien de la peine à faire subsister les armées". Last a
portrait (Montcalm by the sense and by a doubtful reading of the September number 69): wit and talents "qui en eussent fait un
excellent jurisconsulte", a prodigious memory, "né d'un caractère violent", without "la fermeté qu'il faut pour retenir des
troupes dans la discipline", who favoured the soldier in everything, shut his eyes, and "perdoit la tête dans les occasions où
il étoit le plus important de la conserver"; "enfin personne n'a selon moi plus contribué que lui de toutes les manières à
la ..." (two unread words). The close in clear asks pardon for leaving "le cercle" of his instructions.

## System and key

A syllabary-nomenclator, numbers 1 to about 700, disordered (two-part): letters, syllables, words (115 or 3 = M. Bigot,
209 = Canada, 148 = troupes, 30 = soldat, 633 = magasins?), with two or more homophones for common units. Words and names not
worth coding stand in clear. The instruction of 3 Feb 1759 gave Trémais "un chiffre particulier à lui" (Roy 1959-60, p. 13).
The table is not found.

In the September letter Trémais wrote **both homophones of most units**, stacked one over the other (497 over 119 = p,
219 over 466 = s) or joined by a dash (12-437 = de, 15-287 = le, 81-178 = homme). In November he wrote one number per unit.
The September pair therefore gives the homophone classes as well as the values.

- `sept_clear_copy.txt`: the clear copy ff.344-345, read in full.
- `sept_cipher_aligned.tsv`, `sept_key_from_pair.tsv`, `sept_align_build.py`: 564 cipher slots aligned, 168 numbers with a value
  (87 confirmed by recurrence). Open conflicts: 437 (de and ta), 89 (au / qui), 176 and 274 (tu).
- `key_overrides.tsv` (6 choices among the conflicts), `key_nov_extension.tsv` (values fixed from November, each with its word).
- `nov_transcription_v2.tsv` (independent transcription), `nov_transcription_diff.tsv` (against issue 810), `decode_nov.py`.
- Mechanical coverage: 1,131 of 1,350 groups get a value from the September key with the six override choices (0.838); the frozen September-only key of the control, first digit alternative only, values 956 of the 1,277 main-text groups (0.749). The diff of the two transcriptions counts 1,279 main-text numbers, the final transcription 1,277.

Retry corrections to the key (in the retry files, not all copied to the key tables): 32 is 92 = mé on these pages; 192 is
mostly 132 = er; 197 = nt as in September (u is 137); 385 = su is a misread 382; 195 = où/ou; 417 = un/une; 233 = bien;
212 = dans; 473 = n; 402 = fort; 99 = dont; 310 = bon; 161 = fe; 374/376 = t(u).

## Why it does not read whole: the images

LAC serves one rendition, 1125 px for a two-page spread (624 px for a single page); a digit is 4 to 5 px high. Two independent
transcriptions of November (issue 810, and the one made here before opening it) agree exactly on 737 of 1,279 numbers (58%);
279 could not be decided on the image. 40 of the 53 lines of f.346v lose their end in the gutter. With a table one digit wrong
gives a wrong syllable, and with a partial key the sense cannot always choose.

## Known keys tried

- C11E 10 numerical sheet e001295274 (Vaudreuil 1757): rejected earlier (0.063 against 0.229 for shuffled keys, Dudout, PR 273).
- C11E 10 numerical sheet e001295272: 98 rivière, 108 tion, 115 guerre. Rejected (Trémais 98 il, 108 r, 115 M. Bigot).
- C11E 10 numerical sheet e001295276 (Montcalm 1758): 98 comme, 108 quoique, 115 eau. Rejected.
- Every key file in the repository (1,294 files) against 22 Trémais pairs: none matches two.

## Prior work and credits

- Brice Dudout (PR 273, 5 Nov 2026): found that the September letter has its decipherment bound after it and in the LAC
  transcripts (reel C-2402 pp. 523-527), rejected the Vaudreuil table, built a partial key from the pair.
- emgeorrk (issue 810, 19 Nov 2026, Codex-assisted): first partial decipherment of November: transcription of 1,327 groups,
  a 188-entry working key, 49 strong passages (among them mon instruction, résulté une infinité d'abus, arrêté le cours,
  prodigieuse augmentation des dépenses de cette colonie, traitement, sévèrement puni, souverainement, basse ingratitude,
  sa conduite, tempérament, déplorable confusion, mépris). Kept in `prior/`. The values taken from that work are marked
  "issue 810" in `key_nov_extension.tsv`. No pull request; the contributor confirmed the credit as given here on 24 Nov 2026 and issue 810 was closed that day.
- This session: the stacked-homophone finding, the full September alignment, the second transcription and the agreement
  measure, the two rejected tables, and the reading in `reading.md`.
- No published reading found: Roy's dossier ("Dossier Charles-François Pichot de Querdisien Trémais", RAPQ 1959-60, pp. 3-22 as cited by the Dictionary of Canadian Biography; read on BAnQ numérique, numerique.banq.qc.ca/patrimoine/details/52327/2276324; the instruction of 3 Feb 1759 ends "On lui remet ci-joint un chiffre particulier à lui pour sa correspondance dont il ne fera usage que pour les choses secrettes dont il aura à rendre compte.") prints neither this letter nor the table;
  the LAC transcripts leave it out; web searches (FR/EN) found nothing.

## Transcription doubts

The whole transcription is doubtful at this resolution: two independent transcriptions agree on 737 of 1,279 numbers, and
`nov_transcription_diff.tsv` lists each disagreement with the decision. The places below are those the retry left conjectural
or open, each checked on a 6-8x crop with no overlay, against the decode and against the other transcription (issue 810).
The places the retry graded sure are in `retry_346rv.tsv` and `retry_347rv.tsv` with the same three checks.

- 219 (f.346r l.11) - read: [dans?] [open]; checked: image, decode, transcription; one group before "mes recherches"; the sentence wants dans or en; 219=s and 217=la give neither; crop q11.png cannot decide the digits; no second plac
- 46[79] (f.346r l.19) - read: [quelque?] [conjectural]; checked: image, decode, transcription; image reads 467 or 463; 663=quelque (September) needs 4/6 and 3/7; "pour" (450) not excluded; sentence: Que ... répréhensible que soit M. Bigot
- clear: rapprochent (f.346r l.30) - read: [respirent?] tous la [conjectural]; checked: image, decode, transcription; clear word, not cipher; crop r30_1.png is compatible with respirent
- 15 3[37][029] (f.346r l.32) - read: [l'intérêt?] [conjectural]; checked: image, decode, transcription; one unknown word-number (330/332/337) after le; "l'intérêt qui réunit les hommes les divise aussi" fits, but no second place confirms the value; was u
- 271 108 [39][27] (f.346r l.34) - read: [crime?] [conjectural]; checked: image, decode, transcription; 271 for 231 (7/3), 92=mé; the i is not written (or 108 hides 74/76=ri); sense: ce qui semble un crime dans les autres; was unread
- 157 [23][29] (f.346v l.3) - read: du [ … ] [open]; checked: image, decode, transcription; crop p03.png reads 157, 39; 29=va gives nothing; a word-number (du Roi?) with no second occurrence
- 192 66 108 227 des 6[37]3 (f.346v l.6) - read: tout sort des [magasins?] [conjectural]; checked: image, decode, transcription; 633 has no value from September (449=magazins there, medium); same number 346v.32; magasins fits both, not proved
- 4[37]7 {47[46]} et autres 4[23][39] {411} à des 30[29] 32 339 (f.346v l.8) - read: de [ … ] et autres [ … ] à des [armées?] [open]; checked: image, decode, transcription; crops p08a-c.png confirm 474 (or 476), 433, 411, 309, 92, 339; 474 and 411 occur nowhere else; ar-mé-es is the mechanical decode but the phrase is not
- 20 262 156 18 469 475 (f.346v l.9) - read: la ration ne leur [est?] [conjectural]; checked: image, decode, transcription; 475 occurs once; est is what the grammar asks
- {[14]16} {2[27]…} 15 227 (f.346v l.9-10) - read: [billets?] [conjectural]; checked: image, decode, transcription; crop v_L09-12_b.png reads 214 (or 114), 279; 214=bi, 279=l; first digit doubtful
- 152 (f.346v l.15) - read: [beaucoup?] [conjectural]; checked: image, decode, transcription; 152 is not "des": it stands before "de fortunes" here and before "d'esprit" at 347r.31 (avec 152 d'esprit et des talens); beaucoup fits both, tant not
- 1[279]6 {405} (f.346v l.18) - read: [ … ] [open]; checked: image, decode, transcription; crop p18.png: 196 or 176, then 405; 405 recurs at 347r.11 and .22 without a value; the sense wants "où étoit" or the like
- 165 260 1[29][29] (f.346v l.18) - read: [officier?] [conjectural]; checked: image, decode, transcription; fi and er are sure (260 for 240, 192 for 132); the first group 165=a does not give "of", and ci is not written; 136=officier is used at lines 25 and 2
- {[56]7} (f.346v l.20) - read: [un?] [conjectural]; checked: image, decode, transcription; a two-digit number before pays; un is wanted (un pays où la vie est d'une cherté ...); no second occurrence
- [12][12] {288} 21[279] (f.346v l.28) - read: et de [ … ] [open]; checked: image, decode, transcription; 288 has no value; crop z28b.png cannot decide 219/217; d'épée would suit after "de plume et" but nothing supports it
- 4[37]7 80 257 26[37] {288} (f.346v l.28) - read: [ … ] [ayent?] [conjectural]; checked: image, decode, transcription; a-y-e are sure; the last group reads 288 but 248=nt would make ayent (same doubt at 347r.43 important); the group before (427 or 437) and the clear wo
- {4…} 219 491 (f.346v l.28-29) - read: fait [leurs?] affaires [conjectural]; checked: image, decode, transcription; 46. at the gutter; 469=leur (September); affaires sure
- [23]63 [14][12]9 157 169 (f.346v l.30) - read: [qu'eux?] [conjectural]; checked: image, decode, transcription; crop z30a.png: 363, 4?9, 1?7, 16?; e-u-x needs 157 for 137 and 169 for 142; 363=cu standing for qu' recurs at line 42; "personne n'en avoit plus d'occ
- {388} 262 126 (f.346v l.30) - read: [ … ] [open]; checked: image, decode, transcription; 388 occurs once; no word found (sense: et il en est ... qui en ont bien profité)
- {5…} (f.346v l.30) - read: ⟨…⟩ [open]; checked: image, decode, transcription; one group cut by the gutter before "aux prix" (quant?)
- [58]0 (f.346v l.31) - read: [comme?] [conjectural]; checked: image, decode, transcription; a conjunction is wanted before "on s'est trouvé obligé"; 50 occurs once
- 101 ⟨…⟩ 4[46]1 108 271 263 196 (f.346v l.31-32) - read: se [fournir chez?] [conjectural]; checked: image, decode, transcription; fo-u-r would be lost in the gutter; 196=z rests on this place only
- 633 (f.346v l.32) - read: les [magasins?] [conjectural]; checked: image, decode, transcription; as line 6
- 287 18… 2[02][48] (f.346v l.32-33) - read: [ … ] [open]; checked: image, decode, transcription; second group cut by the gutter; "suivi les leurs" would fit the sense but the groups do not spell it
- 36[18] (f.346v l.34) - read: qu'on [y?] [conjectural]; checked: image, decode, transcription; cut by the gutter; same shape as the y of pays (346r.30)
- 98 157 80 (f.346v l.35) - read: [il y a?] [conjectural]; checked: image, decode, transcription; 157=du does not fit; y (259) needs two digits changed
- 4[68][79] (f.346v l.35) - read: [ … ] [open]; checked: image, decode, transcription; a number word (trois, quatre?) before "ans"; 467=un does not agree with the plural
- 8 {10…} ⟨…⟩ 466 (f.346v l.35-36) - read: [termes?] [conjectural]; checked: image, decode, transcription; 10. at the gutter = 108; me lost; fits the "fixés aux" that follows
- {498} (f.346v l.36) - read: [ … ] [open]; checked: image, decode, transcription; a word-number, once only: what the terms were fixed to (lettres de change? paiements?)
- {1…} (f.346v l.36) - read: [de?] [conjectural]; checked: image, decode, transcription; cut by the gutter; "De tout cela est provenu"
- 66 4[37][278] (f.346v l.40) - read: [manquoit depuis?] [conjectural]; checked: image, decode, transcription; crop p40a.png reads 45 (or 65), 432; 45=manqué and 412=depuis are September values; 432 for 412 is not one of the usual confusions; the sense that fol
- 472 47[39] 126 27 (f.346v l.40) - read: long[temps?] [conjectural]; checked: image, decode, transcription; 126 is 106=g on the image (crop p40b.png); lo-n-g sure; 27=temps is new (also "en 27" in marginal note C, not tested); was unread
- 26[01] ⟨…⟩ 452 (f.346v l.41-42) - read: étoit sans [chef?] [conjectural]; checked: image, decode, transcription; ch lost in the gutter between 260 and 452; was unread
- {280} (f.346v l.42) - read: [le gouverneur / M. de Vaudreuil?] [conjectural]; checked: image, decode, transcription; the subject of the portrait that precedes M. Bigot; perhaps the 28. of line 40; once only
- 28[59] (f.346v l.42) - read: [qualité?] [open]; checked: image, decode, transcription; word-number after "pour toute"; once only
- [23]6[23] (f.346v l.42) - read: [qu'?] [conjectural]; checked: image, decode, transcription; same use as line 30
- du [13]1[07] 1[01][15] 1[36][29] 226 (f.346v l.42 (interlinear)) - read: [du bon sens?] [conjectural]; checked: image, decode, transcription; an insertion above the line (crop p42ins.png), tiny; 310=bon as in bon-té on line 43; n and s need 169 for 149 and 236 for 219; a clear word (avec?) f
- 407 2[12]6 (f.346v l.42) - read: un [ … ] [open]; checked: image, decode, transcription; 116 once only (fonds?)
- 4[37]7 [23]10 8 (f.346v l.43) - read: [de bonté?] [conjectural]; checked: image, decode, transcription; 310=bon new (two places, both on these two lines); replaces "de la débilité?"
- {2…} 305 130 8 (f.346v l.44-45) - read: [docilité?] [conjectural]; checked: image, decode, transcription; first group cut by the gutter (2..); docilité (224=do) suits "duquel il n'étoit rien que l'on ne pût attendre" better than facilité (205)
- 17[46] 268 219 227 {10…} 226 {374} (f.346v l.46-47) - read: [peu instruit?] [conjectural]; checked: image, decode, transcription; 174=peu (September); 268 for 261=in; u lost in the gutter; 374 is t (274), as at 347r.17 état and 347r.18; "mais peu instruit il ne pouvoit faire qu'u
- 4[23]7 429 162 1[02]6 111 (f.346v l.48-49) - read: [ … ] [open]; checked: image, decode, transcription; the start of the word is in the gutter of line 48; -nement or -tement, then two groups not understood (en paix, 109?)
- 1[46][59] {233} 26[39] 315 227 (f.346v l.50) - read: [du bien de l'?] état [conjectural]; checked: image, decode, transcription; 233=bien; the first group (142/149/169 on the image) read as du; "de l'" is not written; état sure
- 20… (f.346v l.50) - read: [ces deux ⟨chefs⟩?] [conjectural]; checked: image, decode, transcription; cut by the gutter; 206=deux from 347r.5-6
- de (clear) (f.347r l.2) - read: aidé de [conjectural]; checked: image, decode, transcription; clear word, too small on the image to confirm "aidé"; unchanged
- [23]23 (f.347r l.3) - read: [ … ] (homme? expected) [open]; checked: image, decode, transcription; one group; prior transcription read 93; 223 = r gives nothing; 81/178 homme not reachable; no second occurrence of 323
- pour 469 [23][23]2 85 (f.347r l.4) - read: pour leur [ … ], qui [open]; checked: image, decode, transcription; 3[23]2 (prior 322 = v, or 382 = su) gives no word; 85 taken as 89 = qui (same at 347r.14 and 346r.25 "les maux qui ont affligé"), conjectural; "qui" g
- 206 (f.347r l.5) - read: des deux chefs [conjectural]; checked: image, decode, transcription; 206 = deux from this line and 347r.6 only; unchanged
- 192 206 (f.347r l.6) - read: tous deux [conjectural]; checked: image, decode, transcription; as 347r.5
- 3[23]2 (f.347r l.7) - read: [sur?] toutes les parties [conjectural]; checked: image, decode, transcription; 382 = su (3/8); r not written; one group only
- 165 2[359]2 (f.347r l.7) - read: [ … ] [open]; checked: image, decode, transcription; 252/292/232: 292 = re (Sept, low) gives "a-re"; no word; the digits are not separable on the image
- 4[023]0 [46]37 20 32 [46][37]3 1[59]2 (f.347r l.7-8) - read: où il leur étoit [ … ] [open]; checked: image, decode, transcription; first group unknown (400/420/430); 32 may be faire or 92 me; several French fits (… de … faire …), none spelled by the groups
- 165 469 162 339 433 339 (f.347r l.8) - read: Les choses [ … ] [open]; checked: image, decode, transcription; every group has a value but no word comes out; 162 may be 142 x or 452 ef as in l.5; digits not separable
- en [46]87 (f.347r l.8) - read: ces [ … ] personnes [open]; checked: image, decode, transcription; clear word reads "ces" on the image (crop r_l06_09b), not "en"; 687 unknown, once only (a number word? deux/quatre)
- 480 (f.347r l.11) - read: [Cadet / le munitionnaire?] [conjectural]; checked: image, decode, transcription; single code, once only; "celui-ci" of l.12 refers to it and is the man "tiré de l'état de garçon boucher" (l.17-18), i.e. the munitionnaire Cadet; ide
- ce qui s'en trouve (clear) (f.347r l.11) - read: ce qui s'est passé [conjectural]; checked: image, decode, transcription; clear words reread on the crop r_l10_12a: "s'est passé" rather than "s'en trouve"
- 89 4[46][46] 1[27] 4[01]7 405 200 (f.347r l.11) - read: [ … ] [open]; checked: image, decode, transcription; 405 and 200 have no value (405 once more at 346v.18, unread there); 4[46][46] may be 466 s, 446 or 449 magasins; no reading
- 8[59] seulement (f.347r l.14) - read: qui restèrent [conjectural]; checked: image, decode, transcription; 89 = qui; the clear word reread on crop r_l13_15a as "restèrent" ("seulement" does not make the sentence); the clear word is small
- 15 360 15 119 (f.347r l.14) - read: le camp [conjectural]; checked: image, decode, transcription; 360 for 341 ca and 15 for 55 m: two groups changed; fits "de Beau…" and "l'armée se retira"
- de 125 89 281 359 (f.347r l.14) - read: de Beauport [conjectural]; checked: image, decode, transcription; bé-au sure; 281 and 359 have no value (po-r-t wanted; 359 also 346v.34 unread); the place would be the camp of Beauport, left on 13 Sept 1759
- des 499 15 169 219 (f.347r l.15-16) - read: des talens [conjectural]; checked: image, decode, transcription; 499 does not reach 437/315 ta by one digit (prior read 633); le-n-s fit; same spelling ta-le-n-s at l.31
- l'une 262 298 (f.347r l.17) - read: [on l'a?] tiré [conjectural]; checked: image, decode, transcription; ti-ré sure; the clear word before it reads "l'une" in both transcriptions and cannot be settled on the image
- 165 407 4[01]7 (f.347r l.18) - read: à [ … ] une [conjectural]; checked: image, decode, transcription; à … une fortune; the middle group (407 as read = b or un) is unexplained, possibly a repeated or cancelled group
- [23]6[39] (f.347r l.19) - read: que [conjectural]; checked: image, decode, transcription; 349 = que (Sept) by 6/4; joins fortune to the next clause; could also be 263 e
- en 262 396 339 101 (f.347r l.21) - read: de noblesse [conjectural]; checked: image, decode, transcription; clear word looks like "de" on crop r_l20_23a; 396 for 394 bl; the first group reads 262 (= ti) in both transcriptions but "no" is wanted here and agai
- rendre 352 (f.347r l.23) - read: rendu service [conjectural]; checked: image, decode, transcription; 352 single code, once only; forced by "rendu … à des …"; clear word rendu/rendre
- 26[23] 39[46] 339 (f.347r l.23) - read: nobles [conjectural]; checked: image, decode, transcription; same first group as noblesse l.21; replaces the earlier guess "misérables", which three groups cannot spell
- [58][39] 86 169 2[23]6 8 (f.347r l.25) - read: [de] conduite [conjectural]; checked: image, decode, transcription; conduite sure; the group before it (59/83/89) has no value that gives de or sa
- 80 7[27] (f.347r l.27) - read: à [faire?] [conjectural]; checked: image, decode, transcription; 72 = vo or 77 (no value); a verb before subsister is wanted
- 265 8 [23]10 [23]61 169 151 (f.347r l.28) - read: dans l'abondance [conjectural]; checked: image, decode, transcription; 310 = bon confirmed at 346v.43 (de bonté); 361 da; 169 for 149; the group read 8 is unexplained (80 a with a digit lost?); was unread
- 408 166 227 (f.347r l.29) - read: le salut [conjectural]; checked: image, decode, transcription; 166 = a elsewhere (346r.15); "lu" wanted; unchanged
- en 317 (f.347r l.30) - read: dépendoit [de là?] [conjectural]; checked: image, decode, transcription; 317 = la; the clear word before it (en/de) cannot be settled on the image; "dépendoit en la" is not French
- [58]9 (f.347r l.31) - read: Quant à [M. de Montcalm?] [conjectural]; checked: image, decode, transcription; 59 as read has no value; 69 = M. de Montcalm in September (f.342v l.36); 5 for 6 is not among the usual confusions; the portrait fits him
- 1[15][25] (f.347r l.31) - read: avec [beaucoup?] [conjectural]; checked: image, decode, transcription; prior 115, here 152; one group before d'esprit; value not fixed
- que cet ennemi fait (clear) (f.347r l.31-32) - read: qui en eussent fait [conjectural]; checked: image, decode, transcription; clear words reread on crops r_l30_33a/b; "cet ennemi" makes no sentence with what follows
- 469 98 (f.347r l.33) - read: il n'étoit nullement [ … ] [open]; checked: image, decode, transcription; two groups, ?-il; 469 = leur gives no word (habile, militaire … are not spelled); no digit alternative helps
- necessaire 1[18]5 (f.347r l.33) - read: entendoit [très?] [conjectural]; checked: image, decode, transcription; clear word reread as "entendoit" on crop r_l30_33b; 185/115 one group before "bien", value not fixed
- 18 [46]37 417 26[16] 20[79] 2[23]1 8 298 (f.347r l.35-36) - read: né d'un caractère [conjectural]; checked: image, decode, transcription; c-té-re sure; ca (341) and ra (20) each need more than one digit against the reading 26[16], 20[79]
- 98 115 (f.347r l.40) - read: il le [conjectural]; checked: image, decode, transcription; 115 as read is the title number of l.2; "le" (15) wanted
- 268 263 137 16[23] (f.347r l.41) - read: les yeux [conjectural]; checked: image, decode, transcription; e-u sure; 268 is not y (259/348) by one digit; 162 for 142; was unread
- 2[34]0 ses 12 466 191 226 (f.347r l.41) - read: sur ses désordres [conjectural]; checked: image, decode, transcription; 191 (once only) must hold "ordre"; last group is not s as read
- 18[27] 2[46]1 [23]18 (f.347r l.44) - read: [ … ] [open]; checked: image, decode, transcription; 182/187 and 218/318 have no value and no second occurrence in the main text; only the middle group (241/261 in) decodes
- 126 261 (f.347r l.45) - read: en [faveur?] [conjectural]; checked: image, decode, transcription; 261 = in gives "en in"; a word like faveur is wanted; not confirmed
- 168 de 8 108 1[79]6 (f.347r l.45) - read: des troupes de [terre?] [conjectural]; checked: image, decode, transcription; 168 for 148 troupes sure (same at 346v.22 "des 1[46]8 té-r-re"); the third group of terre is read 1[79]6 where 298 is wanted
- 98 219 195 39[456] 296 240 [35]7[46] (f.347r l.47) - read: il s'oublioit [conjectural]; checked: image, decode, transcription; ou-bl-i and final t sure; 240 as read = fi where o is wanted (two digits from 276); was unread
- 265 673 12 317 [46][23]6 (f.347r l.49) - read: à la [ … ] de la [ … ] [open]; checked: image, decode, transcription; 673 = n gives no word, so the group is another number; 426/436/626/636 once only; the sense wants "ruine/perte de la colonie", not spelled
- 46[79] 108 ⟨…⟩ 4[39]7 265 298 106 287 (f.347v l.1-2) - read: force de la règle [conjectural]; checked: image, decode, transcription; 46[79] for 463 fo; "ce" falls in the gutter at the end of line 1; was an unread run

## Remaining gaps
- 92 conjectural words across ff.346r-347v (`reading.md`, each with its numbers in the retry files) - blocker: illegible; the sense fits but a digit or a once-seen value is not confirmed, and the LAC images cannot decide a digit (4-5 px high; 58% agreement between two transcriptions); HD scans from ANOM, or LAC reel F-104, would settle them
- 25 unread runs, 67 groups (f.346v: 13, f.347r: 12; graded "open" in the retry files) - blocker: no-key-material; numbers with no value in the September pair, most of them seen once (39, 474, 411, 405, 288, 388, 487 or 687, 498, 289, 116, 200), or all-valued runs that give no word because a digit is misread
- line ends of f.346v (40 of 53 lines) and of f.347v - blocker: illegible; lost in the gutter of the microfilm frame, needs the original or a new photograph
- marginal notes of ff.346r and 346v (73 numbers) - blocker: illegible; 62 of the 73 numbers are of low confidence
- the names by code number (480 the munitionnaire, 69? Montcalm, 280 the governor) - blocker: no-key-material; Trémais's table (Marine C 246, now MAR/C/7/246, or the minutes of B 109-110) is not found

## Escalation
- [x] siblings: the letter of 22 Sept 1759 (ff.342-343v) is the only other Trémais cipher letter in the LAC description of C11A 104-105; used as the key source
- [x] clear-pages: ff.344-345 is the decipherment of September only; no decipherment of November is bound with it, and the C-2402 transcript omits the letter
- [x] known-keys: the three numerical sheets of C11E 10 and every key file in the repository; none fits
- [x] print: Roy 1959-60 read; web searches; nothing
- [x] key-rebuild: September pair aligned in full with homophone classes; about 60 values added or corrected from November
- [x] retry: every unread run and conjectural word of ff.346r-347v retried on new 6-8x crops with the extended key (268 places: 181 sure, 64 conjectural, 23 open) and regraded; frozen-key control run
