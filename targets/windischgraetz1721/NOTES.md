# Windischgrätz brothers, Brussels 18 Nov 1721 (DECODE R5029)

Status: read in part, 21 Sept 2026; second pass 5 Oct 2026 (85.6% measured). Written up as `docs/windischgraetz1721.html`.

Ciphered letter, Brussels, 18 November 1721, catalogued on DECODE as Leopold Viktorin von Windischgrätz to his
brother Ernst Friedrich (DECODE R5029, "Non-decrypted", 8 pp., homophonic + nomenclator, numerical). Holder: SOA
Plzeň, pracoviště Klášter u Nepomuka, Rodinný archiv Windischgrätzů, inv. nr. 1433, karton nr. 202. Catalogue item 68,
class A (rule-scored). Five DECODE images: p2 = first page ("Brüssel den 18. 9bris 721", "Hochgebohrner Graf"),
p3 and p4 = two openings, p5 left = last page (signed "h. C."?), p1 = the same last page seen from the back.

## The key

The DECODE record carries a reconstructed key (`DOC_5029_…xlsx`) by **Jakub Mírka**, 19 June 2023, made from the
brothers' letters of the second half of 1721, most of which have interlinear decipherments. His code list includes codes found in this letter, but no reading of it is published; DECODE says non-decrypted.
Letters: two numbers each, A = 24/36, B = 12/48, C = 23/35 … Z = 1/37 (first column
counts down 24…1 through the alphabet in a fixed shuffle, second = first + 12 or + 36; table in `key.tsv`). Codes
above 48 are a small nomenclator; Mírka identifies 52 affaire, 54 Althann, 85 der/dem, 86 die, 121 geheim, 128 Graff,
135 hat, 145 ich, 152 Kayser, 197 Plan, 198 Prinz, and guesses 99 [Engländer?], 103 [Emp…?], 151 [K…?],
167 [Micosch?], 191 [Ostendische Compagnie], 195 [Pentenrieder], 213 [Starhemberg?]. Ernst Friedrich wrote on 27 Sept
1723 that he had received "the cipher key" with his brother's last letters.

## What was done

1. Images and the xlsx fetched with the project cookie (`decode/`, git-ignored).
2. The letter is German in clear with 13 enciphered passages. All numbers transcribed by eye from the full-resolution
   images: `ct.txt` (clear context in brackets). 181 groups: 122 letter groups, 59 code groups.
3. `dec.py` applies Mírka's table; output `dec.txt`. Every letter-spelled passage gives German at once, which checks
   the key: MIR · NICHT · EXCUSATION ZU MACHEN · HALTET · LIEBE · VERLIEHRET · DES · ZU · ZUSEHE · UNSER AN[…] ·
   VERLIEHRE · SUCCESSION · NIE[H]EMAHLEN ANZUNEHMEN · DIENSTE ZU · GETH[A]N.
4. No cryptanalysis was needed. 148 of 181 groups (82%) have a value; 33 code groups (23 distinct codes) stay open:
   78, 99?, 101, 102, 103?, 111, 130, 131, 139, 146, 149, 151?, 164, 167?, 168, 172, 181, 182, 204, 205, 206, 209, 225.

Slips: "1.39.4" is written with a 2-like flourish before the 4 (read ZUSEHE, not ZUAEHE); 45 (H) stands where A is
wanted in GETHHN and an extra H appears in NIEHEMAHLEN, either the writer's slip or a second value for A not in the key.

## The reading (gist)

The writer, who is at the Congress of Cambrai or close to it, replies to a letter of 1 November:

- The Emperor [103?] will not at all [130 209]; the Emperor himself advised [146] **to make an excuse** (*eine
  Excusation zu machen*). If "I" am supported from there, the advice is good; otherwise not, for [205] **holds**
  under hand, probably also [172] the Prince.
- [205] will surely tell no one, not even Althann. *Manus manum lavat* with [205].
- On the matter of [78] it is hard to believe how not only [151] but everyone **loses** the **love** for [103],
  even the Emperor himself, daily; after the courier finally, after so long, brought **the Prince's plan**.
- [225] has arrived, [103] for over two months [182 101]; the Emperor looks on quite calmly (**zusehe**). The
  [Engländer?] and [111] want to go home, and then **our** [139] and [204] would get little credit … "I" shall
  succumb, the Prince triumph, and the Emperor will rather [168] **lose** [78] and the …
- The Congress should open soon; the courier from Madrid brought Pozobueno the order to reserve, in exchanging the
  renunciations *ratione titulorum*, the article that Windischgrätz agreed with Beretti Landi at The Hague.
- To think of a limit to **the succession** [182] suits him, since he made it a point of honour **never to accept**
  it, so that [182] … "I have the Prince [206]" … for whose **services to** [131], which is shameful.
- Last page: only **to** [149] the Emperor **done** [131]; he asks for his brother's goodwill toward his services and
  his great expenses, and for the Congress to open.

The context (Cambrai, Pozobueno, Beretti Landi, renunciations, the Ostend Company code in the key) fits Ernst Friedrich
von Windischgrätz, imperial plenipotentiary at Cambrai, better than Leopold Viktorin; the direction in DECODE's metadata
is kept but should be checked against the hand of the brothers' other letters.

## Files

- `ct.txt`: the 181 groups by passage with clear context. `dec.py`, `dec.txt`: the reading.
- `key.tsv`: Mírka's letter table and code list, transcribed from the DECODE xlsx.
- `decode/`: images, record page and xlsx (git-ignored).
- Related: `targets/windischgraetz1720/` (Charles VI's letters to L. V. Windischgrätz, keys R5017/R5018 — a different cipher).

## Second pass, 5 Oct 2026 (push toward 95%)

1. **Siblings opened.** DECODE R5025 (27 Sept 1721), R5026 (1 Nov, the letter this one answers), R5027 (15 Nov) and
   R5028 (3 Dec, Ernst Friedrich's reply to this letter) were fetched (16 images, `decode/`, git-ignored) and every
   cipher passage scanned for interlinear glosses (ink or later pencil). Codes confirmed by a gloss:
   - **78 = Compagnie**: R5026 p.4 `85 191 78 85 152` glossed "der Ostend. Compagnie dem Kayser" (so 191 = Ostendisch
     and 78 is the noun; Mirka had put the whole phrase on 191). Reads "In puncto der Compagnie" and "verliehre Compagnie".
   - **103 = (Prinz) Eugen**: R5028 p.1 pencil "P.E." under 103; R5026 p.5 `103 contrair` glossed "Eug." Mirka's
     "[Emp...?]" was a misreading of the same gloss. Three tokens here.
   - **99 = Engländer**: gloss on R5026 p.4 and R5028 p.2.
   - **167 = Miosch (Graf)**: R5025 p.3 `128 167` glossed "Graf Miosch".
   No sibling glosses any of the other open codes (101, 102, 111, 130, 131, 139, 146, 149, 151, 164, 168, 172, 181,
   182, 204, 205, 206, 209, 225).
2. **Re-transcription.** Every cipher line of P2-P5 re-read at full resolution. In this hand 4 is a long-s shape and 5
   the same with a small c-hook above; with that, one correction: p5 `21 22 27 9 24 18` (was `... 9 45 18`) = GETHAN,
   so the "GETHHN" slip was a transcription error. NIEHEMAHLEN stays: the 45 there is clear (writer's slip).
   All other groups confirmed.
3. **Bracketing (tier B, proposals, not counted).** The nomenclator is alphabetical (52 affaire, 54 Althann, 78
   Compagnie, 99 Engländer, 103 Eugen, 121 geheim, 128 Graf, 135 hat, 145 ich, 152 Kayser, 167 Miosch, 197 Plan,
   198 Prinz, 213 Starhemberg). Fitting each open code to its bracket and every context gives: 182 nicht (3 contexts),
   131 haben (2), 172 mit (2), 130 gut + 209 seyn, 146 ihm, 149 ihro, 151 Kaiserin, 164 mehr, 168 mir, 111 Franzosen
   ("die Engländer wie auch [111] wollen nacher Haus gehen", Cambrai), 139 Hof, 205 Rialp (3 contexts; R5028 opens
   on the Marquis de Rialp). These are shown with "?" in `dec.txt`. Other words fit several of them, so under the
   read bar they stay unread.
4. **Measure.** `measure.py` (new) counts sense, not just "has a value": each letter run is checked as a German word
   and LM-scored with `lang` de-1740s; code groups count only with a listed or glossed value. The old 0.82 counted
   groups with a value; it happened to equal sense because every letter run reads, but it did not test it.

Result: 155 of 181 groups read as sense = **0.856** (was 0.82). With the tier-B proposals it would be 0.961, but
those are context fits, not readings. Not at 95%.

## Remaining gaps
- 19 nomenclator codes (26 groups): 101, 102, 111, 130, 131, 139, 146, 149, 151, 164, 168, 172, 181, 182, 204, 205, 206, 209, 225 - blocker: open-codes; no gloss in the four sibling letters R5025-R5028; alphabetical bracketing gives proposals for 13 of them (tier B in dec.py) but not proofs. A further sibling with these codes glossed (the brothers' other 1721-23 letters in SOA Plzen karton 202, not on DECODE) would settle them.

## Escalation
- [x] siblings: R5025-R5028 fetched and scanned 5 Oct 2026; 78, 99, 103, 167 confirmed by glosses; other brothers' letters in karton 202 are not on DECODE (needs archive access)
- [x] clear-pages: all five DECODE images viewed; no decipherment on them
- [x] known-keys: Mirka's key applied; R5017/R5018 (windischgraetz1720) are the Emperor's keys, a different system (1-977 syllabary), not this nomenclator
- [ ] print: not done - editions of Cambrai congress correspondence not searched; unlikely to print a private brothers' code
- [x] key-rebuild: alphabetical bracketing done 5 Oct 2026; proposals listed, not counted
- [x] retry: dec.py/measure.py rerun with the extended key and corrected transcription
