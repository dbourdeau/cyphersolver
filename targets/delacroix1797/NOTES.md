# Delacroix to Létombe, Paris, 25 Messidor an V (13 July 1797): despatch No. 5 in a French numeric code (catalogue 649)

Status: in progress (not deciphered; attempted 2 Nov 2026, no reading; blocked on the clear minute or a key, which need archive access)

No value of the code is established. Everything below about what groups mean is a hypothesis. The structural findings
in "What the numbers show" are measured.

## The document

- NARA RG 59, Despatches from US Ministers to Great Britain, vol. 5 = microfilm M30 roll 4, frames 0244 right, 0245 left
  and right (catalog naId 188512917). A clerk's copy marked "Dup.", "(Copy)", "No. 5 Duplicata". Enclosed in Rufus King's
  No. 53, London, 12 Nov 1797, which says: "I have no means of decyphering it."
- Heading in clear: "Le Ministre des relations extérieures au citoyen Letombe consul à Philadelphie, exerçant
  provisoirement le consulat général de la République Française aux États Unis". Close in clear: "Salut et fraternité",
  "Ch. Delacroix".
- Transcription by Michael Brackx (issue #122, 27 Oct 2026), `ciphertext.txt`: 653 groups, 297 distinct, values 2-1198
  (`_check_profile.py --measure`). His doubtful readings are listed in the issue. Frames viewed here at reduced size to
  confirm layout and page-foot catchwords; the transcription was not re-collated digit by digit in this session.

## Context

Létombe's reply No. 42, 22 Brumaire an VI, is printed in Turner, *Correspondence of the French Ministers* (1904), pp.
1076-77, from the ministry's decipherment (États-Unis vol. 48, f. 355). He admits having mixed consular and political
matters in his letters since the minister's departure, says he dictates the figures of his political letters himself,
and promises more attention to "ce qui m'a été prescrit par la dépêche du 25 Messidor dernier". So part of No. 5 probably
concerns how that correspondence is kept. This is a likely subject, not a crib with known wording.

## What the numbers show (measured)

1. **Neighbouring numbers cluster.** Summing min(f(n), f(n+1)) over adjacent values gives 162; 3,000 random
   reassignments of the same frequencies onto 2-1198 average 98, and none reached 162.
2. **Near-repeats vary by small steps** (`solver` session output; a search for aligned passages differing by at most 3):
   - `263 267 705 806 711 405 81 973 486` / `326 265 705 806 711 405 83 972 485` / `416 268 705 806 711 405 81 973 82`
   - `383 338 439 958 235 39 1083 489 1052` / `262 338 440 958 234 39 1083 489 1052`
   - `500 235 689 124 152 882 755 240` / `1163 234 689 123 151 882 755 247`
   - `310 174 973 266` / `1031 174 971 268`; `379 973 1122 317` / `596 973 1122 316`
   - `540 327 799 350 39` / `498 326 800 350 39`; `715 417 269 705 806` / `494 416 268 705 806`

   Inference: at least some entries own several consecutive numbers (homophones in small blocks), for instance 971-973,
   265-269, 81-83, 416-417, 326-327, 799-800, 234-235, 123-124, 151-152. Blocks are inferred from context, and their edges
   are unknown. The earlier reading of 972/973 and 81/82 as evidence for a one-part alphabetical code is not supported:
   a calibrated test found no alphabetical order ("Second round" below), and these pairs are better explained as homophones.
3. **711 and 400 fill one slot** in `705 806 _ 405` (5 and 2 times), so homophones also sit far apart.

Comparable in kind to the numeric syllabic nomenclators with homophones in `bouille1778`, but that is a comparison, not a
proof of the system.

## What was tried (2 Nov 2026)

1. **Annealing with the numbers in alphabetical order** (`solver/solve1.py`, Turner 5-gram). Degenerate: favours long words.
2. **Homophonic syllable annealing with a character model** (`solver/solve2.py`), with a length cap and overuse penalty.
   French-looking output, no agreement between seeds. Calibration on synthetic letters of the same size, with known keys
   and Turner text (`solver/calib.py`): true key scored 802-1338, annealed junk 1692-1789, token accuracy at most 0.037. This
   objective cannot find the key, and its outputs carry no information.
3. **Word-bigram Viterbi objective** (`solver/wsa.py`, `wordscore.py`). It separates true from junk on the synthetic
   letters (about -0.9 to -1.5 against -2.3 per character, with the test text inside the training corpus, which flatters the
   truth), but the search cannot reach the truth: at 300,000 iterations token accuracy stayed at or below 0.037 unpinned
   (`calib3.py`), 0.34-0.40 with 30-33% of tokens pinned correctly, and 0.60-0.65 with 51-53% pinned (`calib4.py`), which is
   only about 8-12 points above the pinned share. A tenfold-longer unpinned run (3,000,000 iterations) reached at most 0.028.
4. **Competing cribs on the real text** (`solver/realtest.py`, 4 seeds, 300,000 iterations): `705 806 711 405` + `265-269`
   as *la République* -2152 to -2128, as *le gouvernement* -2146 to -2100, nonsense control -2311 to -2232. Both beat a
   control whose pins are not French, which says little. They do not separate from each other. No output reads.
5. **Hand phrase matching.** Unverified ideas: `705 806 711 405` = République or gouvernement; `338 439 958 235 39 1083 489
   1052` = correspondance politique, or indépendance plus two groups; `1031 782 315 39` = confiance; `327 799 350 39` =
   puissance. None survives a check on all its other occurrences, and I retracted several while testing them. In particular
   405 was first taken as *ment*, then *que*. See `cribs.tsv`.
6. **Known keys** (`solver/keyscan.py`, each against 50 permuted copies of itself): Bouillé K6, Damas, the Martinique
   table, Mercier 1761, Ennery 1765, d'Affry code X, Champigny 1744. All within their own null range (for example Bouillé
   -2.900, null max -2.711; Ennery -3.005, null max -2.798). Ruled out. None is a Foreign Ministry key of the 1790s; no such
   key is held here or was found on DECODE metadata.
7. **Print and web.** Turner does not print No. 5. Searches found no edition or quotation of it. Schnakenbourg, "Un conflit
   sans grief ?", *AHRF* 2026/3 (no. 425), pp. 71-90, cites Létombe's letters in the États-Unis series, but only the abstract
   is open (Cairn, paywalled; read via Chrome after a 403). A search-result excerpt places Létombe to Delacroix, 29 Messidor
   an V, at CP États-Unis vol. 48, f. 73. Not checked: whether this article cites No. 5; Nasatir and Monell's calendar (1967).

## Second round (2 Nov 2026, at Daniel's request to keep attacking)

All on the word-bigram objective, after adding a limit of 5 values per entry, a reward for distinct entries and a penalty on
immediate word repeats. Synthetic letters here are held out of the language model unless stated.

| test | synthetic letters | real text | scrambled numbers |
|---|---|---|---|
| Strict one-part, homophones in blocks (`solver/mono.py`, 150,000 iterations) | -1818 to -2096, token accuracy 0.49-0.50 | -2527 to -2719 | -2596 to -2810 |
| Alphabetical inside blocks of 100 (`solver/blocks.py`, 120,000) | not run | -2220 to -2364 | -2235 to -2365 |
| Alphabetical inside blocks of 25 | not run | -2199 to -2230 | -2188 to -2218 |
| Two-part with consecutive numbers merged, word-placement moves (`solver/tied.py`, 300,000) | -2230 to -2504, accuracy at most 0.017; model not held out | -2179 to -2252 | not run |

- **One-part is the useful negative.** The method breaks about half of a synthetic one-part letter from scratch, so it would very
  probably have shown a one-part code here. The real text stays about 600 below those letters and overlaps the scrambled control
  (5 seeds each, so the comparison is rough). Strict alphabetical order is not supported, nor is order inside blocks of 100 or
  25, though those two tests were not calibrated.
- **Word-placement moves** (`solver/wsa2.py`, `calib5.py`) gave accuracy at most 0.031 from scratch, and pinning the top 20, 40
  or 80 groups gave only 3-6 points above the pinned share (`calib6.py`).
- **All real-text outputs here are noise.** Fragments such as "re pu bli que" or "de part est au" appear because the search can
  assemble common words on any input. The scrambled control does the same. They are not readings.

Conclusion so far: this search can only break a code with the alphabetical constraint. For a code without it, 653 tokens leave
the search unable to reach the true key even when the objective ranks that key first, so an outside crib of real length is
needed.

## What would move it

- **CADN Nantes, Philadelphia consulate, 519PO/1, article 1** ("Correspondance avec le ministère des affaires étrangères,
  Arrivée: mars 1793-février 1798 ...", finding aid on archivesdiplomatiques.diplomatie.gouv.fr). New lead: this is where
  the received No. 5 or a deciphered copy would be, if kept. The finding aid has no entry naming a cipher table.
- **La Courneuve, CP États-Unis vols. 47-48**: the minute of 25 Messidor an V, or Létombe's ciphered originals beside the
  decipherments Turner printed, which would give pairs to rebuild the code.
- Any of Schnakenbourg's footnotes that cite the despatch.

## Remaining gaps

- whole despatch, 653 groups - blocker: no-key-material; no key, clear minute or sibling pair found online, and ciphertext-only annealing fails its own calibration
- AMAE CP États-Unis 47-48 and CADN 519PO/1 art. 1 - blocker: needs-physical-access; not digitised as far as found

## Escalation

- [x] siblings: frames 0236-0252 have no decipherment (Brackx); catalogue and leads searched for Létombe, Delacroix, Talleyrand, Adet, Fauchet: `astrea1799` (Rozier 1798, ciphertext not online) only, and no shared key shown
- [x] clear-pages: heading and close only; King's No. 53 has no decipherment
- [x] known-keys: seven French numeric keys in the repo tried, all within chance
- [x] print: Turner 1904, web searches; Schnakenbourg 2026 paywalled; Nasatir and Monell not seen
- [x] key-rebuild: annealers (free, one-part, partly ordered, merged blocks, word placement) and hand phrase matching, calibrated on synthetic letters; no key
- [n/a] retry: nothing recovered to retry with

## Files

`ciphertext.txt` (Brackx's transcription), `cribs.tsv` (unverified hypotheses), `solver/` (scripts; the Turner text, model
tables and logs are in the untracked local `.work/delacroix1797/`), `img/` (NARA frames 0243-0245, not to be committed).
