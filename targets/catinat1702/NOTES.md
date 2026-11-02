# Catinat 15 Sept 1702, camp of "Ingleshem" (catalogue 354, Cryptoole XX1702-1)

Status: attempted, open. No key, no reading. Sessions of 28 Oct 2026 (claude-sonnet-5-5, then claude-opus-5-5).

## The document
Aargau Kantonsbibliothek, Zurlauben archive (Acta Helvetica), leaf marked "Dup.ta", "Nr. 93", f. 238 (volume not
confirmed; probably AH 167, whose Bl. 85-86 is a Marly letter of 30 Mar 1702). Heading in clear: "Au Camp d'Ingleshem
le 15. 7bre 1702". Pages 1-2: 591 figures (3-464), no word division, no clear opening. Page 2 ends "140. 39. Je suis
avec plus de verité", which runs on to p. 3 (f. 239): "que je ne puis vous dire, Monsieur, Vostre tres humble et tres
obeissant serviteur. Le Mal de Catinat". So the cipher closes the body and the clear text is only the closing formula.

**Place.** Vault, *Mémoires militaires* II (archive.org `mmoiresmilitai02vauluoft`): the army left Ingenheim on 30 Aug,
stayed at Mundolsheim on the 13th, and on the 14th camped under Strasbourg, "la gauche à Eckbolsheim, sur la Bruche, où
fut le quartier général", until the 25th. "Ingleshem" on the 15th is therefore most probably **Lingolsheim**, next to
Eckbolsheim, not Ingenheim (Tomokiyo, catalogue). Probable, not proved.

**Context (Vault, for cribs).** Landau capitulated on 9-10 Sept, and Mélac's garrison left on the 12th and reached Strasbourg
on the 17th. The Elector of Bavaria took Ulm on 8 Sept. Catinat was trying to join him: the comte de Luttens and a
Bavarian officer left the camp of Eckbolsheim for the Elector and could not get past Schaffhausen. Comte d'Arco, Ricous
(French envoy with the Elector; Vault p. 574 mentions "lettres chiffrées" between Catinat and Ricous), Villars marching
to Huningue on the 25th, the prince de Bade and the roi des Romains all appear. The King answers Catinat's courier of the
14th on the 18th. A duplicate ("Dup.ta") sent to a Swiss correspondent fits a letter routed through Switzerland
towards Bavaria. That is a hypothesis about the purpose, not a finding.

**Recipient.** Probably Beat Jakob II Zurlauben (1660-1717), not the lieutenant general Beat Jakob (1656-1704). The
lieutenant general was in Italy (Mantua) in 1702 (Tomokiyo, thread comment 20, and the regest of AH 167/50).

## Files
- `ciphertext.txt`, `tokens.json`: 591 tokens. Lichtenberger's 2016 transcription plus Norbert's corrections, then
  **all 47 lines checked against the images** (28 Oct 2026). Two changes: 1.22 group 7 = 13 (was 10), 1.18 group 14 = 54.
  Doubtful groups are listed in the file header (2.10.9 = 251 or 231; 2.12.13 is cut by the fold; others).
- `img/` (git-ignored): the three page images, Bazeries-More-Letters.pdf, and the zoom crops used for the check.
- `ordered_low.py`, `grid_test.py`, `grid_control.py`, `sibling_need.py`: the experiments below.
- `research_found.md`: the archive and print search (sources searched, negatives included).

## Statistics (2016 thread, recomputed)
186 distinct, 64 singletons, IC 0.0086. Top: 50 x18, 28 x17, 22 x14, 13 x14, 30 x12, 84 x11, 393 x10. 252 tokens are
<= 99, in 141 runs of 1-6. Two long repeats give the homophones 10=17, 22=277, 101=350 (Thomas, Tomokiyo).

## What was tried (all failed or inconclusive)
| test | result |
|---|---|
| Pignerol petit chiffre 1690 key (`targets/feuquieres`, 167 groups; same IC 0.0088 and the same ~45% share below 100) | covers 247/591 tokens; 4-gram score -3.70/char, inside the relabelled-null range -2.98 to -4.06. **Not this code**: the same design, a different book (as Norbert's combined IC already suggested) |
| Tomokiyo 8B, 4 Apr 1702 royal code (only its frequency list is published) | 8B uses nothing below 22 (11% of tokens here) and 24% above 400 (6% here): **different layout** |
| Tomokiyo 1690/93, 8B, 10, d'Usson, Grand Chiffre 1691 | rejected by Tomokiyo 2016; not repeated |
| Low numbers = letters in alphabetical blocks (`ordered_low.py`) | real -2.35/token vs nulls -2.42..-2.60; decode is gibberish. Control with a true ordered key: only 35-40% of letters recovered. **Underpowered** |
| Grid layout, column = initial letter (Item 4/8B design; `grid_test.py`) | no residue signal for k = 5..30. Control (`grid_control.py`, true grids k=10/13/18): not detected either. **Underpowered** |
| Repeats as cribs | the five contexts of `41 269` are `[291 10] [10 66] [17 66] [17 10]`; with 10=17 a doubled unit follows, which fits Norbert's "l'armée". Not testable further without a key |

## How much would a sibling give? (`sibling_need.py`)
A deciphered letter in the same code of about 200 tokens would give values for about 70% of this letter's tokens. About
400 tokens would give about 85%, and about 1,000 about 97%. This is optimistic, because it assumes the same group
distribution. A sibling is the realistic route.

## Remaining gaps
The whole despatch (591 figures) is unread. Blocker: **no key material**. No sibling letter, key sheet or clear copy has
been found, and a ciphertext-only attack on a nomenclator with 186 distinct groups in 591 tokens fails on matched
controls.

## Escalation
- Siblings: the Aargau catalogue (kbaargau.visual-library.de/ah) is behind a JavaScript check and could not be searched.
  Ask the library (Dr Ruth Wüst, who brought the letter to Schmeh in 2016) for AH 167 Bl. 230-245 and any other
  Catinat or "Dup.ta" leaves of 1702.
- Clear copy or minute: the *Mémoires et correspondance de Catinat* (1819) t. III (Google Books BUT_hUwNO3UC) could not
  be read, because of the Google consent wall. Check it by hand for 14-16 Sept 1702. SHD Vincennes A1 1569 (Catinat's
  originals, 1702) is not online.
- Keys: BnF fr. 6204 no. 13/14 (495 entries, but 1711) is the nearest size match and a cheap test if its table is
  obtained. The Catinat-Ricous "lettres chiffrées" (Vault p. 574) imply a field code of that summer: look for Ricous
  papers.
- Print: Vault II and III searched, and they give no 15 Sept letter.

## 29 Oct 2026: Aargau scans (Brice Dudout)
The Aargauer Kantonsbibliothek sent free scans of Acta Helvetica AH 52/93 to Brice Dudout (received; study only until we ask about display).
They are the sibling the catalogue entry asked for; not yet transcribed here. Do not publish an image until display is cleared.
