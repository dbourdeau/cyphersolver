# Mémoire en chiffre du XIIe décembre 1560: BnF fr. 3157 no. 67

Status: read (98.9% of cipher words; key broken here, ciphertext only)

Catalogue 276. BnF fr. 3157 ("Recueil de lettres et de pièces originales", Montmorency papers), item 67,
"Mémoire en chiffre du XIIe decembre 1560". Gallica btv1b90598645. Worked 22-23 Sept 2026.

**Result.** An anonymous report to the connétable de Montmorency ("vostre grandeur") from a Catholic
gentleman of the Agenais, a neighbour of the sieur de Fumel, dated 12 December 1560, a week after the death of
François II. It is entirely in cipher, ten pages, 1,715 cipher words. It had no decipherment and no known key.
The cipher was broken here from the ciphertext alone: a homophonic substitution with two-stroke units and four
code words. The reading covers 1,696 of the 1,715 cipher words (98.9%). 108 words are read with a marked
emendation, and 16 scattered words are left unread.

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
- **Polyphonic signs.** δ (d) stands for u/v, b and g (gouvernement, bien, langaiges). ‡ (D) is i and sometimes a
  (avecques, abus). c is l and sometimes a.
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

## Remaining gaps

- 16 scattered words (of 1,715), each tried against the image and the key, context not decisive: 152r.16 (x),
  152r.26 (mx on), 152v.06 (Q+), 152v.26 (3xzo fxz), 153r.31 (Wzoxedn), 154v.03 (WxmJn), 154v.24 (C+ DzoSx3),
  155r.29 (x+ S), 155v.16 (mixppxrQxppxm), 155v.17 (3xrnnQxS), 155v.22 (S) - blocker: open-codes; each is once,
  and the signs are read but the word does not resolve
- the writer's name - blocker: no-key-material; not in the text, no signature or address

## Escalation

- [x] siblings: leaves ff. 147-163 opened; Villars letters in clear, dorse f.157v has only a cipher line and "henry second"
- [x] clear-pages: no decipherment in the item or next to it; f.158 is item 68 (Marillac), not a decipherment
- [x] known-keys: Lasry GL.htm Henri II/Charles IX tables checked, different symbol sets
- [x] print: web search for the names/places, Brunet 2019 (not reachable); nothing printed of this text found
- [x] key-rebuild: homophonic key rebuilt by seeded annealing and word alignment; units zo, pp, io, s3, ff, nn, lz, :. found
- [x] retry: all unread words re-run with the final key after the image correction pass; 3 more resolved (ainsi, ainsin, ayants)
