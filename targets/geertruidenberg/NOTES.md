# Torcy to the plenipotentiaries at Geertruidenberg (3 April 1710) and Villars to Polignac (1 June 1710)

Status: attempted, open (2026-10-09). Both cipher parts unread: no key on DECODE, in Add MS 61575 or in print; the French copy of Torcy's letter is in AE CP Hollande t. 223 (not online).

## 2026-10-09: images and DECODE transcriptions fetched

- DECODE R8755 (7 images, `img/R8755_P1..7.jpg`, git-ignored) and R8756 (2 images). DECODE transcription documents
  `decode/DOC_8755_*.txt`, `decode/DOC_8756_*.txt` (Tomokiyo's files, the same ones his dead links pointed to).
- R8755 page map: P1 = f.38r clear; P2 = f.38v clear (9 lines) then 17 cipher lines; P3 = f.39r blank; P4 = f.39v
  endorsement; P5 = f.40r, P6 = f.40v, P7 = f.41r cipher, ending in clear "Je suis &c".
- **The letter opens in clear.** DECODE's transcription skips it ("..."). Transcribed in `torcy_clear.txt`: Torcy
  acknowledges the plenipotentiaries' letter of 27 March and theirs to the King of 29 March, says the long despatch
  answers them, then answers Vanderdussen's plea for the R.P.R. ministers (not in the galleys but shut in castles for
  preaching to the new converts; a matter of the King's ordinances, foreigners not concerned; priests are treated
  far worse in England). The secret part follows in figures.
- DOC notation: "11^0" = 110, "31^6" = 316, "311^" = 311, "7*29" = 729 (the ^ marks a 1 written as a dotted i).
  Ciphertext in `torcy_ct.txt` (694 tokens as parsed, before the fixes) and `villars_ct.txt`.
- R8756 (Villars to Polignac, Camp d'Arleux 1 June 1710) is a copy, clear opening and close, 173 groups between,
  range up to 575.

## 2026-10-09: prior-solution check

- Tomokiyo's live `blencowe2.htm` (last modified 3 Nov 2024) unchanged: both letters listed as undeciphered by
  Blencowe; no reading. His two transcription files are still 404. Web search: no edition or decipherment found.
- Neighbour records R8746-R8774 (Add MS 61575) listed: R8748-R8752 Petkum 1709 (decrypted; key R8766),
  R8753/R8754 anonymous 10 Feb 1710 (DE=56, partially interlined), keys R8757-R8770.

## 2026-10-09: known keys tried

| key | result |
|---|---|
| Tomokiyo 11B, Desmarets 4 June 1710 code (DE=56/221, ~568 values; `tomokiyo/desmarets1710_key.tsv`, ~190 values from his table) | Villars: 41/173 groups covered, nonsense, the top group 340 (x10) absent. Torcy: nonsense. Not the code of either |
| R8766, Torcy-Petkum code 1709 (two-part, 1-774, deciphering grid ruled to 850) | DE = 43/140 (Tomokiyo); Torcy's letter has 43 once and 140 never, and 42 (2nd commonest) = "correspondance". Not the same assignment |
| R8768, marquis de Rose code (1-578, DE=12, Jacobite names, 1715-18) | Villars has no 12; names are post-1714. Not tried further |
| R8767 (one-part, 1-996, DE=215, English names: Dartmouth, Devonshire, église anglicane; c.1712-14) | Torcy has no 215; English-court nomenclature; Torcy's letter (top group 1.7%, many homophones) is not a one-part code of this kind. Not it |
| R8768 detail | key sheet viewed: Jacobite-period names (Ormond, Bolingbroke, Lorraine, Roi de Suède), 1-600 grid. Villars' 340/28/32 not checked cell by cell; ruled out on date and on DE=12 absent |
| DECODE R587 (TNA SP 106/7, two-part French code, ~800 groups, DECODE transcription `keys/DOC_R587_D2734_2734.txt`) | applied to Torcy: 483/690 groups covered, word salad (Livonie, Prusse, Berlin, Keyserlingh): a Northern/Prussian code. Ruled out |
| BnF fr. 6204 f.31-32 "Sixieme Clef a Chiffrer" (Tomokiyo: DE=400/411/423, 720-999 nulls; viewed on Gallica, header row only: single letters 540-590) | Torcy has "355 423 411" and "423 411 733" = "de de": ruled out on the DE homophones alone (key not transcribed) |
| Other fr. 6204 War-ministry keys (Tomokiyo's DE values: Maumort 68/229/242, Lauzun 143/205/297, Usson 1701 37, Tallard 597/811/783, Bouchu 250, Villeroy 104/617/766, Boufflers 31/290, Vendôme 34, St-Maurice 78/161/346, no.10/11 48/210/568) and Usson 1702 (311/331) | counted DE homophones in Torcy: each 0-7 hits in 690 groups, too few for "de" in French. Not transcribed, not pursued. (Tirconel 13/46/219 has 12 hits but is a 1688-91 Ireland key) |

## 2026-10-09: transcription checked

- R8755: all 83 cipher lines compared with the images: the DOC transcription is right apart from notation.
  The struck groups are left out of `torcy_groups.txt` (690 groups, 285 distinct, values 1-823; measured).
  "288 729" occurs twice, which settles the DOC's "7*29" as 729.
- R8756: DOC "575" is 515 (so the range is 3-560); the DOC "_" after 524 is an underline, not a gap.
  `villars_groups.txt` 173 groups, 106 distinct (measured).

## 2026-10-09: print and context

- **Legrelle**, *La diplomatie française et la succession d'Espagne* (1st ed.) vol. 4 p. 546 and n. 2 quotes
  this letter's clear sentence ("Les prêtres sont traités bien plus durement en Angleterre ... dont on vous a
  parlé") and cites it as "Torcy aux plénipotentiaires, 3 avril 1710. — Hollande, t. 223". That confirms the
  identification and places the French file copy (minute or register) in AE Correspondance politique Hollande
  223 (La Courneuve). Legrelle quotes nothing from the cipher part. (`print/legrelle_1ed_v4.txt`.)
- **Torcy, *Journal inédit*** (ed. Masson 1884), 30 March - 3 April 1710 (`print/torcy_journal.txt`): the council
  of 30 March confirmed the orders already given, adding only the mediators (Denmark, King Augustus); the courier
  left on the 31st (the "longue depeche" of the clear text = the King's letter of 31 March, Legrelle iv 544-546).
  On the 3rd Torcy read the King the plenipotentiaries' letter of 29 March ("rien d'important"); letters from
  The Hague expected peace with a partition of Sicily and Sardinia for Philip V. Thematic only: no verbatim crib.
- **Villars, Mémoires** (Vogüé) vol. 3 appendix (`print/villars_mem3.txt`): prints Villars to Polignac 24 May
  (no. 48) and 28 June (no. 52), Polignac to Villars 1 June (no. 51), Villars to Voysin 1 June (no. 50, same day,
  same subject as the clear opening), but not this 1 June letter to Polignac.

## 2026-10-09: ciphertext-only prospects

Torcy: 690 groups, 285 types, values to 823, top group 50 at 1.7%, IC 0.0042; only two repeated trigrams
(19 523 42; 46 576 135) and no longer repeats. That is a two-part code of 800+ values with homophones, the
Foreign-Office "grand chiffre" type (compare R8766, 774 values in an 850-cell grid). A rebuild from 690 groups
with only thematic context is not realistic (compare desmarets1710: 471 groups, 568 values, unread; hellen1752,
spaen1808). Villars: 173 groups, 106 types, too short for anything without a key.

## Remaining gaps
- Torcy 3 Apr 1710, cipher part (f.38v-41r, 690 groups) - blocker: needs-physical-access; no key on DECODE, in Add MS 61575 or in print; the French copy is in AE CP Hollande t. 223 (La Courneuve, not digitised), and 690 groups of an 800-value two-part code are too few to rebuild
- Villars 1 Jun 1710, cipher part (f.44, 173 groups) - blocker: no-key-material; a different code (range 3-560, 340 x10) with no key found, and too short for a ciphertext-only attack

## Escalation
- [x] siblings: R8746-R8774 (all of Add MS 61575 on DECODE) opened; Petkum 1709 letters (key R8766) and the anonymous 10 Feb 1710 letter (R8753/R8754, Blencowe's partial decipherment, small code to ~409) are different codes; keys R8757-R8770 are English or post-1711
- [x] clear-pages: R8755 f.38r-38v is the letter's own clear opening (transcribed, `torcy_clear.txt`), not a decipherment; R8756 has clear opening and close only
- [x] known-keys: R8766, R8767, R8768, DECODE R587, Tomokiyo 11B (Desmarets 1710), BnF fr. 6204 Sixième clef, DE-homophone screen of the other fr. 6204 keys and Usson 1702: none fits
- [x] print: Legrelle iv (cites the AE copy, quotes only the clear part), Torcy Journal inédit, Villars Mémoires iii, Tomokiyo blencowe2/louisxiv: no decipherment
- [n/a] key-rebuild: nothing reads, so there is no seed; 690 groups of an 800+ value homophonic two-part code and 173 groups of the Villars code are below what a ciphertext-only rebuild needs
- [n/a] retry: nothing was read to retry

## DECODE queue
- R8755: metadata blank for sender/receiver. Sender Jean-Baptiste Colbert, marquis de Torcy; receivers the French
  plenipotentiaries at Geertruidenberg (maréchal d'Huxelles, abbé de Polignac); Versailles, 3 April 1710. The dorse
  endorsement "3 April 1709" is a slip for 1710 (f.38r is dated 1710; Legrelle iv 546 n.2 cites the letter as 3 April
  1710, AE CP Hollande t. 223). Cleartext language French (f.38r-38v and the closing are in clear). The DOC
  transcription omits the clear text: offer `torcy_clear.txt`. Notation note for the DOC: "11^0"=110, "31^6"=316,
  "311^"=311, "7*29"=729 (confirmed by the repeat "288 729").
- R8756: the metadata lists "Duc de Villars" as receiver; Villars is the sender (signed "Le Mar Duc de Villars"),
  the receiver is the abbé Melchior de Polignac at Geertruidenberg; written at the camp of Arleux, 1 June 1710; a
  copy. DOC corrections: "575" is 515; the "_" after 524 is an underline, not a gap.
- R8754/R8753 (lead, not checked here): Tomokiyo gives DE=56 for this anonymous 10 Feb 1710 code, as for the
  Desmarets 4 June 1710 code (his 11B); if they are one code, Blencowe's partial decipherment on f.29 could extend
  the desmarets1710 key.



BL Add MS 61575 ff. 38-41 (DECODE R8755, five pages, endorsed "M Blencow cannot decypher them") and f. 44
(DECODE R8756, two pages). Cryptiana entries "French Ministers at Geertruidenberg (1710)" and "Marshal Villars
and Abbé de Polignac (1710)"; Tomokiyo's article `blencowe2.htm` gives only the high-frequency groups
(Torcy: 50 x12, 42 x10, 122 x9, 451 x9, 5 x8, 107 x8, 236 x8, 77 x7, 135 x7, 175 x7, 269 x7, 411 x7, 821 x7;
Villars: 340 x10, 28 x5, 32, 91, 158, 248, 267, 371 x4) and says the two used different ciphers.

## Status 2026-09-16: blocked at the ciphertext

The tracker's premise (2026-09-15) was that Tomokiyo's transcriptions were online. They are not:

| route | result |
|---|---|
| `cryptiana.web.fc2.com/code/blencowe_geertruidenberg.txt`, `blencowe_polignac.txt` (the links in his article) | 404 on the live site (both redirect to fc2's error page); never captured by the Wayback Machine. His other transcription files (`richelieu1629.txt`, `perwich.txt`, `elizabeth_moray.txt`) still resolve, so these two were probably never uploaded |
| DECODE R8755 / R8756 record pages | readable without login (metadata: "Torcy to ministers at Geertruidenberg [transc]", "Villars to Polignac [transc]", a transcription document exists for each). Images and documents: "Authentication required"; the file server returns 200x317-px thumbnails only (`TH_IMG_R8755_I40509_P1.jpg` saved here), unreadable |
| British Library Add MS 61575 (Blenheim Papers) | not digitised; the interim BL catalogue is browse-only after the 2023 cyber-attack |
| Klausis Krypto Kolumne | no post on either letter |
| printed plaintext (Legrelle, Torcy's *Mémoires*, Polignac correspondence) | not checked: pointless until the ciphertext exists |

So nothing can be attempted here. Registration with DECODE (de-crypt.org) is blocked by organisation policy on
account creation; that step, or an email to Tomokiyo asking for the two files, is Daniel's.

## What to do once the ciphertext is in hand

* Torcy's 3 April 1710 letter is four folios in a "great cipher" with groups to at least 821, probably the
  Foreign Office one-part design of the period (cf. the 1702 Usson code, 568 entries, and Tomokiyo's item 11B,
  a Geertruidenberg-period code DE=56/221 with about 568 entries, which should be tried first as a key).
* The negotiation is one of the best-documented in French diplomacy: Legrelle, *La diplomatie française et la
  succession d'Espagne* vol. 4; the Torcy *Journal* and *Mémoires*; the plenipotentiaries' (d'Huxelles, Polignac)
  correspondence. Cribs for a same-week letter under the same code are likely.

Files: `blencowe2.htm` (Tomokiyo's article), `decode_8755.htm`, `decode_8756.htm` (record pages),
`TH_IMG_R8755_I40509_P1.jpg` (the thumbnail DECODE serves without login).
