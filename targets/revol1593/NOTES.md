# Nevers to Revol, August–October 1593, in the Court symbol cipher no. 60 (catalogue no. 21, part)

Status: in progress. Key no. 60 is fully in hand, but three passages (ff. 115, 176, 198) were located and never
transcribed and f. 88v has no reading; the work is owed, not blocked (see Remaining gaps). The 7 Oct letter
(fr. 3986 no. 68), "not located" in the first session, is f. 146v (Tomokiyo's list, second session; split review 14 Oct 2026).

Split on 14 Oct 2026 from `targets/nevers1593/` under the one-key rule (George Lasry, 14 Oct 2026). The two letters to
Pisany are in Nevers's numerical cipher no. 46 and stay in `targets/nevers1593/` (nevers1593.html): a different cipher,
with its own page. This entry is the Court symbol cipher no. 60 (Tomokiyo's numbering; BnF fr. 3995 ff. 108-111,
"Chiffre baillé à Monsieur de Nevers, Montereau, aoust 1593") and the letters of Nevers to Louis de Revol, secretary of
state, written in it: fr. 3985 f. 88 (21 Aug), f. 115 (27 Aug, one line), f. 176 (2 Sept, no. 88 with duplicate
no. 94), fr. 3986 f. 146v (7 Oct), f. 157v (Coire 9 Oct, no. 75), f. 198 (Desenzano 23 Oct, no. 101).

**Outcome: read with known key, read in part.** Key no. 60 transcribed from the images (17 Sept) and corrected from
issue #32 (Robert Węglarek, tunarob, 12 Oct 2026). Only fr. 3985 f. 88r gives words: *de absolution*, *le Roy*,
*qu'il* (shuffle-controlled, P = 0.0002); on f. 146v Tomokiyo's anchors (*l'absolution*, *à la vérité*, *intérêt*)
come out of the table but the text between them does not yet read. Blocker so far: the copyist's cursive forms.

Files: `key60.txt` (the enciphering sheet f. 109 and the deciphering table ff. 110v-111, with the issue #32
corrections), `decode60.py`, `atlas60.md` (the copyist's forms), `ct_3986_f146v.txt`, `ct_3986_f157v.txt`,
`f88/` (issue #32 transcription of f. 88r-v, `shuffle_control.py` and its result). The printed Instruction of 31 Aug
(`instruction_31aug_print.txt`, a crib) stays in `targets/nevers1593/`. Gallica routes and canvas numbers are in
`targets/nevers1593/NOTES.md` (Sources and routes). Page crops in `docs/revol1593_*.jpg`.

## The Revol letters and key no. 60 (17 Sept 2026, first session)

* fr. 3985 no. 66, 27 Aug 1593, ff. 113–114v (c. 226–230): the copy is in clear from "Mons^r de Revol, n'ayant point
  eu response sur le faict de l'absolution" to the date; the recurring sign is the copyist's "que". Nothing to decode.
* fr. 3986 no. 75, Coire 9 Oct 1593, ff. 156–157v (c. 306–309): clear copy with about 90 symbols of cipher no. 60 in
  the first lines of f. 157v (letters, Roman numerals, crosses, digits). Full-resolution page and crops kept in the
  session scratch of 17 Sept (`revol/B309*.jpg`, not kept), not yet read.
* fr. 3986 no. 68 (Vese 7 Oct), fr. 3985 no. 88 (2 Sept, with its duplicate no. 94) and fr. 3986 no. 101 (Desenzano
  23 Oct) were not located on the image: the downloader was throttled (HTTP 429, two other sessions on Gallica) and
  stopped at fr. 3985 c. 320 and fr. 3986 c. 388.
* Key no. 60 (fr. 3995 ff. 108–110, c. 208–211, full-resolution images fetched) is a symbol alphabet with about five
  homophones per letter, a full syllabary (ba be bi … si) with symbols and two-digit figures, Roman-numeral names and
  places, word signs and nulls. Reading the Revol passages by eye against the table is possible but slow; the better
  route is the deciphered sibling material in the same volumes: Henri IV to Nevers, Chartres 6 Oct 1593 (fr. 3986
  f. 152, c. 298, whole page in no. 60 with interlinear decipherment) and the Instruction of 31 Aug (fr. 3985 no. 77).

## Second session, 17 September 2026: key no. 60 and the Revol passages

* Tomokiyo's dedicated article on no. 60 (`henryiv2.htm`, "A Decoding Table Sorted by Symbol Similarity") lists every
  letter in the key: Nevers to Revol at fr. 3985 f. 88 (21 Aug), f. 115 (27 Aug, one line: the earlier pages are in
  clear, as found in session 1), f. 176 (2 Sept), fr. 3986 f. 146v (7 Oct), f. 157 (9 Oct), f. 198 (23 Oct), fr. 3987
  f. 66, fr. 3989 ff. 3, 169, fr. 3990 f. 27; and the interlined Henri IV letters at fr. 3985 f. 204, fr. 3986 ff. 58,
  151, 174, 191, fr. 3987 ff. 25, 54, 143, fr. 3988 ff. 99, 119, 143, fr. 3989 ff. 59-60. The Instruction of 31 Aug
  is fr. 3985 f. 126 with cipher from f. 130, printed with clear in Memoires de Nevers ii, 492-498; that volume is
  not online (Gallica bpt6k6435941k and bpt6k8717151d are both part 1; Google Books gives no full view).
* Full-resolution canvases fetched (one fetcher, 4 s spacing, no 429): fr. 3985 c. 175-178, 230-231, 260-263,
  352-355, 408-409; fr. 3986 c. 116-117, 286-289, 296-298, 348-349, 382-383, 396-398; fr. 3995 c. 207-213.
* `key60.txt`: the enciphering sheet (f. 109) and the complete deciphering table (ff. 110v-111) transcribed; plus
  the cursive values read off the interlined crib fr. 3986 f. 151 (Henri IV to Nevers, Chartres 7 Oct 1593:
  plusieurs, contre, de la, promesse, respondre, il y a, Bellievre, Villeroy, Zamet). `decode60.py` applies it.
* `ct_3986_f146v.txt` (nine lines) and `ct_3986_f157v.txt` (four lines) transcribed at 2.4-2.6x from deskewed,
  ink-projection line cuts. Decoder output confirms Tomokiyo's anchors on f. 146v (l'absolution, a la verite,
  interest) and the function words around them; the rest does not yet read, because the copyist's cursive forms
  (ue/ur/ıı/v ligatures, 4-shapes, p-loops) map to two or three table entries each. f. 157v: no anchor secured.
* Not done: the 21 Aug, 2 Sept and 23 Oct passages were located and cut (contact sheets in the session scratch)
  but not transcribed; no reading of any Revol letter is complete. Coverage stays 2 of 7 read; the key for the
  other five is now fully in hand, the blocker is palaeographic (copyist's forms), not cryptographic.
* Next pass: build a glyph atlas of the copyist's forms from the crib page f. 151 (same hand as the copies), then
  re-transcribe f. 146v and f. 157v with that atlas before touching ff. 88, 176, 198.

## Addendum, same day: the Instruction crib found twice over

* Memoires de Nevers part 2 IS on Gallica: ark bpt6k64451005 (969 views, "avec mode texte"). It is not returned
  by SRU dc.date/creator searches; it was reached through the catalogue notice cb31011834g. OCR per page via
  RequestDigitalElement E=ALTO (rate limit: one fetcher, >10 s spacing, 429s otherwise and the block lasts
  minutes). The Instruction of 31 Aug 1593 is at views 541-548 = pp. 492-499, saved in
  instruction_31aug_print.txt. ContentSearch on the ark works for spot lookups (Reuol at PAG_324/425/453/513).
* Better still: the manuscript Instruction in fr. 3985 (canvases 260-269 fetched at full resolution; cipher
  pages 264, 266, 268) is INTERLINED with the office decipherment in the same copyist's hand as the Revol
  letters. The glosses match the print word for word (second/third/fourth/fifth parties of the proposition,
  "du droit de la couronne", "quites et absouls du serment de fidelite", "et jure a leur sacre",
  "et garde apres inuiolablement", "qu'il n'y aura ..."). Three full pages of glyph-plaintext pairs in the
  target hand: this, not f. 151 alone, is the glyph-atlas source for the next pass.
* So the copyist-forms blocker now has two independent controls: the interlined Instruction (fr. 3985
  c. 264-268) aligned against the print, and the interlined 7 Oct King's letter (fr. 3986 c. 296-297).

* Caution recorded after re-reading f. 157v at 3.2x with the atlas: much of what was transcribed there as
  symbols is faded clear cursive run together (line 1 ends "...qui ne ... pan...", line 2 has long clear
  stretches). ct_3986_f157v.txt over-reads cipher; the true cipher on that page is shorter than four full
  lines. Re-segment clear vs cipher before re-transcribing. The f. 146v block (canvas 287) is real cipher
  throughout and stays the primary target for the atlas pass.

* f. 146v recut at 3.2x into sixths (N146_* in session scratch, region x 0.12-0.92, y 0.40-0.72 of canvas 287,
  deskew -1.0 deg, ten line peaks at 68/176/284/392/504/608/728/840/952/1064 of the region). Line 2 tile 3
  shows a clean run `++ p (perp) u r u y S f (perp) -e T y p` consistent with the atlas (y=s, T=n, ++=u);
  full alignment of the nine lines against atlas60.md is the remaining work of the next pass.

## Issue #32 (tunarob), 12 October 2026: key no. 60 corrections and f. 88r

Robert Węglarek (GitHub tunarob) sent corrections to `key60.txt`, a tag split, and a transcription and partial
reading of fr. 3985 f. 88r-v (Nevers to Revol, 21 Aug 1593), made with LLM help (Claude Code) and not checked by a
palaeographer. We checked every claim on the full-resolution IIIF images (fr. 3995 canvases 209 and 212-213, fr. 3985
canvases 176-177, fr. 3986 canvas 296; Gallica's `/iiif/` route returned Cloudflare 403, `openapi.bnf.fr/iiif/image/v3/`
worked).

* Key no. 60, 10 of 12 numbered corrections confirmed and adopted (block at the end of `key60.txt`): b's first
  homophone is o- (ring, tail right), not ꝝ, and tu is -o- (our tags gave tu for b); c's fourth is a flag on a stem
  (·x is d only); i has five homophones incl. a hook+cross; o's fifth is \\ not //; m's fourth is ɱ not ccc; u's fourth
  is 2+ not 4; ‡ (one stem, two bars) = d and ‡ with a loop = u; ♀ = u on f. 111; ∩+ = g; o-o = c; o+o = y.
  Rejected: be is a slanted uncial d (kept); the f. 111 compounds f++, O++, ++C, ++O have two stems and ONE bar (kept ++).
* Tag split adopted: ſ+ = l, 4+ = i (open 4), 4+b = bien (closed 4 with cross, f. 111), 4 = x (closed 4), 2+ = u or J
  (f. 111 glosses it "u, J", so it can carry i, as on f. 151), n+ = p (the p-sign that was mis-tagged 2+).
* Re-tag of the old transcriptions: f. 146v "l'absolution" now has ſ+ for l (was 4 = x); "bien" is 4+b; the copyist's
  ++ is tagged ⱶⱶ (= u, atlas60.md) because the sheet's ++ is i. Unresolved tokens after the re-decode: f. 146v 29/204
  (was 27; ꝝ no longer has a value), f. 157v 68/226 (unchanged). Neither page reads further.
* fr. 3986 f. 151: the contributor's ~40 agreeing sign types fit our own crib of ~30; not re-aligned here.
* f. 88r (`f88/ct_3985_f88.txt`): R5 `g ∂ o- Ⱡ ſ+ 20 8 ++ π ⊥` = **de absolution**, checked on the image; it reads only
  with the corrected b. R6 has oo+ = **le Roy** and the compound f++ = **qu'il** (the contributor split it as f ++).
  Shuffle control (`f88/shuffle_control.py`, result file beside it): the 86 cipher tokens of R3-R6 give a 10-letter
  lexicon word; 0 of 5000 token shuffles reach 10 (P = 0.0002). The contributor's global test (P = 0.065) diluted this
  local anchor. R3-R4 "absolusion" is a candidate only; Tomokiyo's "conversion" in R3 needs q = c and the key gives
  q = te, so it is not supported.
* f. 88v: 116 units transcribed by the contributor; no reading under key no. 60 (he also tried keys 65, 66, 76).
  Not re-checked symbol by symbol here.

## Remaining gaps
- fr. 3986 f. 146v, Revol 7 Oct 1593 (nine cipher lines, key no. 60) - blocker: illegible; transcribed at 2.4-3.2x but copyist's cursive forms map to two or three table entries; atlas pass started, not finished
- fr. 3986 f. 157v, Revol 9 Oct 1593 - blocker: illegible; faded; clear cursive and cipher run together, cipher extent not yet segmented
- fr. 3985 f. 88r (21 Aug) - read in part (de absolution, le Roy, qu'il); rest of R3-R6 - blocker: illegible; bitonal microfilm copy in the copyist's cursive, the contributor's transcription has variant readings at about one sign in six and no colour scan exists
- fr. 3985 f. 88v (21 Aug) - blocker: not-attempted; transcribed by the contributor (116 units, issue #32), no reading under key no. 60; not re-transcribed here
- fr. 3985 f. 115 (27 Aug, one line), f. 176 (2 Sept, no. 88/94), fr. 3986 f. 198 (23 Oct, no. 101) - blocker: not-attempted; located and cut but never transcribed; key no. 60 is fully in hand

## Escalation
- [x] siblings: the King's interlined letters fr. 3986 f. 151/152 (7 Oct 1593) and the interlined Instruction of 31 Aug (fr. 3985 c. 264-268) used as cribs in the copyist's hand
- [x] clear-pages: interlined Instruction and f. 151 found; f. 115's earlier pages and the 27 Aug copy are in clear
- [x] known-keys: Tomokiyo's no. 60 (fr. 3995 ff. 108-111) transcribed and applied; the contributor also tried keys 65, 66, 76 on f. 88v
- [x] print: Memoires de Nevers ii (Gallica bpt6k64451005) Instruction pp. 492-499; Tomokiyo henryiv2.htm lists every letter in no. 60
- [x] key-rebuild: key no. 60 re-checked on the images after issue #32 (12 Oct 2026): 10 corrections adopted, tags 4/2+ split; the copyist glyph atlas from the Instruction (c. 264-268) is still to finish
- [x] retry: f. 146v and f. 157v re-tagged and re-decoded with the corrected key (no gain); f. 88r decoded from the contributor's transcription, de absolution + le Roy + qu'il, shuffle-controlled (12 Oct 2026); ff. 176, 198 still to do
