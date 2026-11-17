# Mémoire en chiffre du XIIe décembre 1560: BnF fr. 3157 no. 67

Status: read in part (24 Oct 2026: the second reading measures under 95% of words read as sense on the per-document bar; 98.9% of cipher words were measured earlier on cipher words only; key broken here, ciphertext only)

Lasry review (25 Sept 2026): In private communications, Lasry wrote that he independently solved it in 2023 (improved Feb 2026) but his solution has not been published. Kept in the ciphertext-only list (outcome.first_break = 'unpublished prior').

Catalogue 276. BnF fr. 3157 ("Recueil de lettres et de pièces originales", Montmorency papers), item 67,
"Mémoire en chiffre du XIIe decembre 1560". Gallica btv1b90598645. Worked 22-23 Sept 2026.

**Result.** An anonymous report to the connétable de Montmorency ("vostre grandeur") from a Catholic
gentleman of the Agenais, a neighbour of the sieur de Fumel, dated 12 December 1560, a week after the death of
François II. It is entirely in cipher, ten pages, 1,715 cipher words. It had no decipherment and no known key.
The cipher was broken here from the ciphertext alone: a homophonic substitution with two-stroke units and four
code words. The reading covers 1,700 of the 1,715 cipher words (99.1%; 98.9% before the retry resolved 3 more). By the key replay of
16 Nov 2026, 1,201 of the 1,715 cipher words (70.0%) are the key's exact output, 130 more differ only by i/y or a declared
second value, 354 are read with a marked emendation, and 16 are left unread (the earlier figure of 108 emended words
counted only the marks then in the reading files).

## Where it is

- The BnF notice (archivesetmanuscrits cc496207) puts each item's folio before the item number, so item 67 is
  ff. 152r-156v, not f. 158. f. 158 starts item 68, Marillac's clear despatch from England.
- Gallica views: f.152r = view 153 (right page); 152v/153r = view 154; 153v/154r = 155; 154v/155r = 156;
  155v/156r = 157; 156v = view 158 (left page). The dorse (view 159, left) has "henry second" in a later
  hand and a line of cipher signs.
- Heading on f.152r, in clear: "Du xiie decembre 1560". There is no address, no signature, and no decipherment
  in the item or on the neighbouring leaves. The Villars letters around it (items 65, 66, 69, 71, 72) are in
  clear and contain no key.

## The cipher

- **Script.** A cursive pseudo-script with the words divided by "/". Sign code: `SIGNS.md`, plus the extra codes
  defined in the comment lines of each `transcription/<fol>.txt`.
- **Homophonic.** e = x, ff; n = r (a smaller, rounder form of x: the main transcription trap); s = m, n, nn, 3;
  r = s, S, s3; i = i, D, y, e; u/v = zo, io, d; and so on.
- **Two-stroke units.** zo = u, pp = m, io = u, s3 = r, ff = e, :. = o, nn = s, lz = d.
- **Polyphonic signs.** δ (d) stands for g, b and u/v (langaiges, bien, gouvernement): g 93 times, b 62, u 5 in the
  reading (key.txt listed it as u until 16 Nov 2026). ‡ (D) is i and sometimes a (avecques, abus). c is l and sometimes a.
  3 is s, and x at the end of a word (deux, ceulx). These second values are in the third column of `key.txt`.
- **Whole-word codes.** Z = pour (also used as the syllable, "y pourvoient"); 4 = roy; c+, i+, e+ = et;
  F, g = sieur. There are no name codes: every person and place is spelt out.
- **Key.** `key.txt`, read by `decrypt.py`; the mechanical decrypt is in `decrypt_lines.txt`.

## How it was broken

1. **Access.** Located the item: the catalogue gave f. 158, but the cipher is on ff. 152r-156v. Fetched the ten
   pages at full resolution from Gallica IIIF (`fetch_pages.py`) and cut them into half-width 3-line bands
   (`half.py`).
2. **First transcription.** Three agents transcribed the pages into ASCII sign codes (`transcription/`). One of
   them was stopped by a tool block after three pages; a fresh agent did 153v-154r.
3. **Plain substitution fails.** One sign per letter, annealed with `solve.py` (fr-1530-despatches 5-gram,
   word spaces kept), gave gibberish (-4.2/char).
4. **The first units.** z is followed by o in 262 of 283 cases, so "zo" was taken as one unit. The most frequent
   4-sign word, "Tzox" (23 times), fitted "que"; "Wx", "Wxm" and "hx" fitted le, les and de. With these seeded,
   the annealer produced "les derniers advertissemens", "les affaires de pardeça", "presches" and "assemblées"
   (-3.5/char).
5. **More units from alignment.** Decrypted words were lined up against the French they had to be:
   - "xrQxrhio" = entendu: r = n (a separate sign from x) and io = u;
   - "Dio:is" = avoir;
   - "3shDx+is3xppxrQ" = ordinairement: s3 = r;
   - "nn:WW:iQ" = souloit: nn = s;
   - later, "lzDm+xm" = disans: lz = d.
6. **The codes.** Short standalone groups were read from their context: "temps Z avoir secours" (Z = pour),
   "que le 4 et vostre grandeur" (4 = roy), and "c+" wherever "et" is required.
7. **Correction pass.** With the key known, four agents re-checked every line against the images, pages split
   152r / 152v-153r / 153v-154r / 154v-156v. Each changed a sign only where the image supports it
   (`transcription/corrections_<fol>.tsv`). They made about 300 x→r fixes, restored missing signs, fixed
   minim counts, and identified the looped sign y (= i). Where the image matches the transcription but not the
   key, they left it as written (scribe slips and polyphony, listed in the tsv files).
8. **Reading.** Read line by line: `reading_152r-154r.txt` and `reading_154v-156v.txt`. Emendations are in
   [ ], unread words are [..].

## A parallel pass

While this session worked, another session copied this folder part-way through the correction pass and published an "editorial reconstruction" of the same item (main commit 13e0f27b2: 97.7% by sign units, key called partial; files READING.md, VERIFY.md, coverage.*, reading_working.tsv, alignment_draft.json). It read two things this session had not transcribed, both confirmed against key.txt: the margin at 153r.14, `+mmxppdWxm Wx+ fg+ppdS3x io f:xrmx:W` = "assemblez en la chambre du conseil", and the dorse line = "Advertissemens". Both are added to `reading_152r-154r.txt`. Its files are kept for its image checks. Where they differ, the reading files here supersede them: the key is recovered (all ten pages corrected against the images, including 152v and 153r, which the parallel pass had not corrected) and the reading covers 98.9% of cipher words.

## Content

**Who wrote it.** The writer is a Catholic gentleman of the Agenais, a neighbour of the sieur de Fumel ("monsieur
de Fumel qu'est mon prochain voisin"). He is not Blaise de Monluc: he names "le sieur de Montluc" in the third
person, and Monluc's brother Lioux as an adversary. He corresponds with "le chief" and fears for his life. The
name is not in the text. "Le chief" is Antoine de Bourbon, king of Navarre, governor of Guyenne, residing "en sa
ville de Nérac".

**What it reports, in order:**
- Since his last advertisements, things have gone "de mal en pis": two preachers now where the towns used to have
  one. Madame de Castelpers and mademoiselle de Boesse, wife of captain Montseignac, attend the preaching with a
  great following.
- The rebels, hearing that the king was sending the sieur de Termes with companies, got some seigneurs to write to
  the king that everyone here lives in obedience. They only want time to raise troops and to wait for foreign
  help.
- An assembly at Clairac, in Agenois, of about 2,000 rebels resolved to resist any royal force, "disans qu'ils
  aiment mieulx mourir les armes en main que si le roy les faisoit executer par ung bourreau". Many great
  seigneurs and nobles have secret understanding "avecques ceste canaille".
- The seigneur de Caumont's brother is abbé of Clairac, and the Caumont places all have ministers.
- Reclus, judge of the Caumont lands, and Boissonade, syndic of the Agenois, were elected by the favour of
  Caumont and the chief to carry the tiers état's doléances to court: this is the États généraux of Orléans. The
  juge mage and magistrates of the présidial of Agen decided that they should hide the truth. The juge mage has
  gone to court to keep them quiet.
- Monsieur de Biron assembled 500 soldiers, mostly arquebusiers, to take the castle of Bergerac on the king's
  order, then sent them home after talking to the inhabitants. He did the same at Villeneuve and Montflanquin.
  Biron is allied to Mesmi, a principal rebel captain.
- The rebel captains (Mesmi, La Caze, Jehan de Mesmes, La Borde de Villeneuve, Chaulmont) stay at Nérac. The king
  should order the chief, who claims to be innocent of the conspiracy (Amboise), to hand them over.
- Monsieur de Lioux, brother of the sieur de Montluc, is going to court, and he and the chief's company threaten
  anyone who speaks against the chief.
- The rebels spread the rumour that Termes's companies have been countermanded. The writer dares not leave his
  house except at night and asks to withdraw to court.
- The rebels circulate a tract "qu'ils intitulent l'edict faict par Dieu le pere", and he sends a copy. He also
  encloses a letter from a bourgeois of Agen.
- The rebels count on "ung prince", on foreigners "du costé de Genève" and on the Swiss cantons, to whom they
  would hand two strong frontier towns of Guyenne.
- Fumel, back from court, threatens him. A packet sent through Fumel, with a letter from the chief, may not have
  arrived. He encloses a letter from the garde des sceaux of the présidial of Cahors.

## Prior work

- **Searches.** Checked 22 Sept 2026: no DECODE record, not on Tomokiyo's or Lasry's (GL.htm) lists. Web searches
  for the names and places found no edition or decipherment.
- **Brunet.** Serge Brunet, "Clairac et le début des guerres de Religion (1560-1562)" (in *Clairac et la Réforme*,
  2019) could not be opened (academia.edu 403). It may use the Montmorency papers but cannot have read this cipher
  unless deciphered elsewhere.
- **Keys tried.** The brief asked for Lasry's Henri II and Charles IX tables (GL.htm) to be tried first. They are
  images of different symbol sets, and this script matches none of them, so the key was rebuilt from the
  ciphertext instead.

## Verification 3, 23 Oct 2026

The v3 sweep flagged this reading at 0.21 on the explicit-hole measure. It scored `reading_154v-156v.txt` alone, with
its `154v.01` line prefixes and `#` header as text. Both reading files cut to the text (`reading_152r-154r.txt`,
`reading_154v-156v.txt`) score **0.755 on explicit holes** (111 of 147 sentences; each half 0.76), 0.54 plain (1560
spelling the word list lacks), hole rate 0.073; the 108 bracketed emendations count as holes. The sentences hold.
Kept read (grade B); `outcome.texts[0]` now names the two files as its `reading`. It rests on the key broken here
and the images, with no contemporary decipherment or copy. `READING.md` is a normalised editorial version, not
the reading that is scored.

## Key replay, 16 Nov 2026

Cécile Pierrot (Le Monde, 16 Nov 2026) applied the posted key to the posted transcription and got 67% of the words of the
reading, 77% allowing polyphony, with one sign carrying seven values and the adjustments not mentioned. `docs/_replay.py`
(adapter `replay.py`) repeats the test: before any change, 1,106 of 1,715 cipher words exact (64.5%), 74.8% with the
polyphony these notes declared, 76 words marked and 340 differing with no mark. Her finding stands.

What was done:
- **Key.** `key.txt` gave δ (d) as u; the reading has it as g 93 times, b 62, u 5. The row is now `d g`, with b and u
  declared as second values; a for D, a for c and x for 3 are declared too (third column). `decrypt_lines.txt` regenerated.
- **Reading.** `mark_emendations.py` bracketed every letter the key does not give and every word where a sign is left
  out, and wrote the seven cipher words the reading leaves out in braces. No letter of the reading was changed.
- **Result after marking** (before the image check): 1,175 of 1,715 cipher words exact (68.5%), 76.1% with i/y and the declared
  second values, 394 emended and marked, 16 unread, no unmarked difference.

### Image check of the x emendations, 16 Nov 2026

The ten pages were fetched again (openapi.bnf.fr IIIF, full size) and the 75 places where the sign x (e) is read as
another letter were looked at on 2x crops, line by line. The small bold n-sign (r) and the wide e-sign (x) can be told
apart at that size, and so can the sign with a hanging loop (y).

- **48 words corrected in the transcription**, in two passes (`transcription/corrections_<fol>.tsv`, dated rows):
  16 x → r (n), among them ung (twice), predicant, grandeur, personnes, environ, disans, n'irriter, langaiges (twice),
  quelcun, l'advenir, n'ause, signee; 16 x → y (i): Despuis, puis (twice), parti, cy devant (twice), suite, n'y, Guyenne
  (twice), royaulme, moyens, envoyent, voye, ayant, and the fourth sign of Clairac; x → i in qu'il (156r.21, a single
  minim); two transpositions (152v.26 and 155v.02, rx = ne); 152v.28 `+Hx…` is `+lz…`, the unit lz (d), so the word is
  adverti as the key gives it.
- **A sign the transcription did not have.** An X whose lower-left stroke runs below the line and curls to the left stands
  where the reading has o: ont (152v.19, 154v.04), ou, Caulmont, sont, moyen, versations, Lioux, journellement, bonne,
  fondement, consequance, occasions. It had been transcribed `3x` or `x`. It is now code `G` (`SIGNS.md`), `G o` in
  `key.txt`. Thirteen places changed, each seen on the image. `3x` elsewhere is not all this sign (in ce, executer it is
  s/x and e), so the other `3x` were left.
- **Two words of the reading changed**, both to what the key now gives. 152v.25 `x:xQ` is `r:rQ`, both signs the n-sign:
  "Lesdicts de Caulmont n'ont seigneurie, place et chasteau [..] [..] n'ayent de ministres" (was [ont]). 155v.09 `Dx+rQ`
  is `Dy+rQ`: "ayant lesdicts rebelles l'auctorité" (was [estant]). `reading_en.md` follows both.
- **Confirmed as written, emendation stands** (a plain wide x on the image): 152r.03 couru, 152r.06 and .07 il, 152r.08
  qui, 152r.21 profit, 152v.17 pourroit, 153r.24 discouru, 153r.26 solliciter, 154r.27 lictiere, 154r.28 cependant,
  154v.12 ayants, 154v.20 and 155r.25 qui.
- **Seen and left, doubtful.** 152r.09 and 154v.01 (a tail that may be the loop), 152r.19, 152v.10, 153r.28, 153v.21,
  154v.02, 154v.12 (susdicts), 154v.23, 155v.15 (a large X whose foot is not clear), 156r.20 (the line begins with the
  sign 4 and a looped sign before `c+`; `D 7xi+` does not describe it, and Z is followed by signs the transcription
  lacks), 156v.02 (`ff` there is two f, cc, not the unit ff). 155v.16: the first long word and the last word could not be
  made out on the strip.
- **Not looked at.** The other emended signs (δ read as i, and 3, z, f read as other letters).
- **Result** (`replay.json`, `replay.tsv`): 1,201 of 1,715 cipher words exact (70.0%), 72.0% with i/y, 78.4% with the declared
  second values; 354 words (20.6%) emended, all marked; 16 unread; no unmarked difference. By sign units 91.7% exact. x is
  still read with more than one value in many places.

Open after this: about one word in five still rests on an emendation. The 99.1% above is the share of cipher words given
a reading, not the share the key produces.

## Remaining gaps

- 16 scattered words (of 1,715), each tried against the image and the key, context not decisive: 152r.16 (x), 152r.26 (mx on), 152v.06 (Q+), 152v.26 (3xzo fxz), 153r.31 (Wzoxedn), 154v.03 (WxmJn), 154v.24 (C+ DzoSx3), 155r.29 (x+ S), 155v.16 (mixppxrQxppxm), 155v.17 (3xrnnQxS), 155v.22 (S) - blocker: no-key-material; each is once, and the signs are read but the word does not resolve
- the writer's name - blocker: no-key-material; not in the text, no signature or address

## Escalation

- [x] siblings: leaves ff. 147-163 opened; Villars letters in clear, dorse f.157v has only a cipher line and "henry second"
- [x] clear-pages: no decipherment in the item or next to it; f.158 is item 68 (Marillac), not a decipherment
- [x] known-keys: Lasry GL.htm Henri II/Charles IX tables checked, different symbol sets
- [x] print: web search for the names/places, Brunet 2019 (not reachable); nothing printed of this text found
- [x] key-rebuild: homophonic key rebuilt by seeded annealing and word alignment; units zo, pp, io, s3, ff, nn, lz, :. found
- [x] retry: all unread words re-run with the final key after the image correction pass; 3 more resolved (ainsi, ainsin, ayants)
