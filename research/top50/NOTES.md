# Klaus Schmeh's "Top 50 unsolved encrypted messages", cross-referenced and re-checked

Source: https://scienceblogs.de/klausis-krypto-kolumne/the-top-50-unsolved-encrypted-messages/

The list ran as a post series on Cipherbrain, one article per entry, from **8 February 2017** (no. 50)
to **12 April 2020** (no. 1). So "solved since publication" has to be measured against each entry's
own post date, not against one date for the whole list. `top50.json` records all fifty with their
URLs and post dates.

**Two facts govern how the list must be read today.** Cipherbrain stopped publishing on 31 December
2022, when ScienceBlogs.de closed; Schmeh is active at klausschmeh.net but the Cipherbrain archive
is frozen. And the Top 50 index page was **never retro-annotated** — it still describes Rivest's
timelock as unbroken "18 years later" although Schmeh himself posted the solution in May 2019. The
index is therefore useless as a status source, and every entry below was checked independently.

**Headline: nine of the fifty are closed, and the list does not say so.** One of them is a hoax
entry that has sat unmarked for nine years.

---

## 1. Closed since the list was written

| # | Entry | What actually happened |
|---|---|---|
| 48 | Rivest's timelock (LCS35) | **Solved 2019, twice independently.** Bernard Fabrot finished 15 April 2019 after ~3.5 years of sequential squaring on one consumer CPU; Cryptophage (Peffers, Öztürk, Drake, Johnson) finished 10 May 2019 on FPGAs. Verified by Rivest, capsule opened at MIT 15 May 2019, fifteen years earlier than designed. Successor puzzle CSAIL2019 is now open |
| 42 | Bonus 22 (M-209) | **Solved 20 January 2018 by George Lasry**, confirmed by the challenge author Jean-François Bouchaudy. It was the last open one of his forty M-209 problems; all forty are now solved |
| 35 | Cryptograms from the crypt | **Solved August 2019 by Richard Bean.** A book cipher on Francis Thompson's *The Hound of Heaven*, found by sweeping ~37,000 Gutenberg texts. Plaintext: "A number of successful experiments of this kind would give strong evidence for survival." Self-verifying, uncontested |
| 32 | The silk dress cryptogram | **Solved 2023 by Wayne Chan** (*Cryptologia* 48(5), 2024). Not a personal cipher at all: US Army Signal Service telegraphic weather code, pinned to a single date, **27 May 1888**, with stations including Bismarck, Winnipeg and Calgary. Why the sheets were in the dress is still unknown |
| 27 | Ferdinand III's letters | **Solved October 2017 by Thomas Ernst**, in the comment thread of the Top 50 post itself. A digit-pair code on the Habsburg **AEIOU** motto, with each non-numeric sign encoding its count of strokes or semicircles. These are the letters to Archduke Leopold Wilhelm (1640/41), not the Brussels letters of `targets/ferdinand3/` (see section 2) |
| 15 | The Rilke cryptogram | **Explained February 2021** (Tobias Schrödel and Schmeh; Floe Foxon, *Cryptologia* 2022): not a cipher. The four-letter groups are adjacent keys on a German QWERTZ typewriter — Morse practice material |
| 14 | Codex Seraphinianus | **Not a cipher, on the author's own statement** (Serafini, Oxford, 11 May 2009): the script is asemic. Only the base-21 page numbering was ever decoded |
| 21 | The YOG'TZE case | **Closed as a case, April 2025.** Hagen police and prosecutors closed the death as a single-vehicle accident; investigators doubt the slip of paper ever existed. Seven characters, never a cipher |
| 39 | The Riverbanks Ripper | **Not a real case. An April Fools' joke.** Posted 1 April 2017. The ciphertext is a single character. The transcription is credited to "George Fabyan"; the first murder is set in Geneva, Illinois, home of Riverbank Laboratories; the fifth is dated 1 April. Schmeh never added a disclaimer and it still sits unmarked in the list |

## 2. Corrections this forces on our own tracker

**Ferdinand III: the Top 50 letters are not our target (corrected 9 Oct 2026).** This paragraph used to say
that `targets/ferdinand3/` (then `TARGETS.md` item 16, *"skipped (DECODE login)"*; TARGETS.md was retired on
2 Oct 2026) had been solved by Thomas Ernst in October 2017. That was wrong. Ernst's solution ("Zifra
Piccolominea", Klausis Krypto Kolumne, 7 Oct 2017) concerns the Top 50 letters: Ferdinand III to his brother
Archduke Leopold Wilhelm, 20 July 1640, and a 1641 letter from Hildegard Ernst's 1996 chapter. Our target is a
different correspondence, Ferdinand (King of Hungary, then Emperor) and the Cardinal-Infante Ferdinand,
Brussels SEA 540 (DECODE R1887, R1889, R1890, 1634-1640), and Ernst's key does not fit it. Those letters were
first read by Andrew Aymeloglu (github.com/aaymeloglu/unsolved-ciphers, Sept 2026) and independently here; see
`targets/ferdinand3/NOTES.md` and the write-up `docs/ferdinand3.html`. The lesson stands in a narrower form:
check the solver community before the archive, and check that a published solution is for the same documents.

**The gold bars get independent corroboration.** Our `targets/goldbar/` result was statistical: 21 of 26
letters occur exactly ten times, chi-squared 1.251 on 25 degrees of freedom, P = 9.3 × 10⁻¹³, so the
inscriptions were constructed rather than enciphered. The documentary case points the same way and
we had not recorded it: the aircraft depicted is a Boeing 247 class, in service from 1934 and so
after the claimed 1933 date; "General Wang Jialie" was only made Lieutenant-General in 1936; the
year is Gregorian rather than Minguo; some characters are simplified forms not official until
1955–56; and one bar references 1948. Two independent lines, one statistical and one documentary,
agreeing that these are not 1933 cryptograms.

**Entry 34 touches our Stepney work.** Schmeh's two cited nomenclator messages are the **Manchester
cryptogram** of September 1783, from the 4th Duke of Manchester to **Sir John Stepney**, at the
Clements Library, and the van Gelder cryptogram of 1809. Our tracker item 10 is a Stepney letter of
1702 to a different Earl of Manchester. Different generation, same two families, and the Clements
Library told a reader in 2017 that a single letter is not enough and a corpus would be needed —
which is exactly the finding we reached independently on our own Stepney item.

## 3. Open, but not settleable by cryptanalysis

Listed rather than scored, so the tracker does not pad itself with things no method can decide.

| # | Entry | Why not |
|---|---|---|
| 4 | Kryptos K4 | 97 characters. The plaintext was recovered from Sanborn's papers in the Smithsonian by Kobek and Byrne in September 2025 — explicitly *not* a cryptographic solve — and the archive sold at auction for $962,500 in November 2025; the buyer revealed itself as Paradigm in June 2026. The method remains unbroken and the plaintext unpublished |
| 1 | Voynich | adjudicated 2026-09-15, not deciphered | Six computational tests with adversarial re-runs and five literature sweeps: plain or simply enciphered European language excluded; the two live hypotheses (verbose/slot encoding vs structured meaningless generation) not separated by any statistic yet. See `targets/voynich/NOTES.md` |
| 2 | Zodiac | Z408 solved 1969 (the Hardens), Z340 solved 5 December 2020 (Oranchak, Blake, Van Eycke). Z13 and Z32 are 13 and 32 symbols — too short for any verifiable solution |
| 5 | Somerton Man | The man was identified as Carl Webb in July 2022 (Abbott and Fitzpatrick), still not officially confirmed. The code is ~45 letters of probable initials and the identification did nothing for it |
| 6 | Rohonc Codex | A writing system, not a concealed message. Király and Tokai (*Cryptologia* 2018) claim a reading, endorsed by Benedek Láng, disputed by Nick Pelling. Not settled |
| 26 | Dorabella | 87 characters. Wase (2023) shows it is unlikely to be monoalphabetic English or Latin, which undercuts most claims at the root |
| 20 | Pigeon cryptogram | 135 letters. GCHQ: without the codebook it cannot be decrypted, nor any claim verified |
| 10 | McCormick notes | FBI CRRU and the ACA both failed; Pelling judges it private shorthand rather than a cipher |
| 50, 41, 11 | Cylob, Blitz, Untersberg | Provenance or authenticity unresolved; Blitz has only 8 of an unknown number of pages released |
| 37, 36, 22 | Shugborough, Fair Game, Powers | Ten letters; a disputed transcription of film credits; a dedication widely read as initials |
| 45, 13 | World Record, Double Column Reloaded | Compute races, not cryptanalysis. Both verified at 0 solves |

## 4. Open, tractable, and new to the tracker — scored

Scored on the tracker's existing scale: feasibility for model-driven work — multilingual reading,
historical cribs, cross-referencing digitised editions, fast solver building — not for this repo's
existing tooling.

| # | Entry | Odds | Why |
|---|---|---|---|
| **46** | **ADFGVX residue, 1918** | **high** | The sleeper on the whole list. Lasry, Niebel, Kopal and Wacker broke the Childs corpus and **published the keys**; the 22 messages Schmeh lists are not unbroken ciphers but *mutilated transmissions* against known keys. In the comment thread alone, 12–13 were read in 2017 by Biermann, Armin, Baertl and Lasry. Schmeh promised a consolidating article and never wrote it, so those solutions exist only as scattered comments and **no clean table of which are solved has ever been published**. Roughly 9–10 were never touched. Task is garble reconstruction against a known key and German military register, ~3,964 letters available |
| **28** | **Urquhart's poems, 17th c.** | **high** | Numeric, fully published, Urquhart's own printed corpus finite and digitised. The distich is 64 numbers (values 1–70), the octastich ~272 (values 1–201) — the shape of an index into a book. **There is a live, testable dispute**: Vals AI announced on 31 Aug 2026 that Claude Fable 5.1 solved the distich as a book cipher on Urquhart's *Proquiritations*; Reticuli Labs published a rebuttal on 1 Sept 2026 arguing the rule fails at 10 of 64 positions and scores at chance, and that the distich does not appear in the verified 1653 text. No historical-cipher expert has endorsed either. This repo can settle it by re-running the claim against the actual text, which is exactly the kind of decisive test it already does. **The octastich is untouched** |
| **19** | **Kaliningrad bottle post** | **high** | ~1,000+ characters across seven sections — by a wide margin the most text of any open item on the list, and the only one with enough for statistics. Latin alphabet with heavy diacritics, 37 symbols, index of coincidence ≈ 0.054, consistent with Russian. **A crib claim is outstanding and unpublished**: commenter "Frank" (Feb 2021) said the plaintext is from the 1876 Russian Synodal Bible and never published the method. That is directly testable against a digitised Synodal text |
| **3** | **Debosnys, 1882–83** | **high** | **Attempted 15 Sept 2026** (`targets/debosnys/NOTES.md`). A transcription *was* made, by Sektu in 2017 (1,188 glyphs, 425 types, decomposed into sub-glyphs), but never released. New: the 20-line cipher poem is rhyming couplets by its line-final glyphs (9 of 10 couplets match, 0 of 9 boundaries), and line lengths are syllable-scale, so the plaintext is phonetic French verse. Combined with Matthew Brown's 2021 plagiarism finding, the known-plaintext hunt becomes a shape search over French verse |
| **47** | **Köhler, Abwehr 1944** | skipped | **Attempted 15 Sept 2026** (`targets/abwehr/NOTES.md`). Every tractable hand system and any Enigma excluded statistically against controls; what survives (a mixed-tableau prayer-book key or a one-time pad) is not attackable without the book or the FBI's plaintexts |
| **8** | **Catokwacopa, 1875** | medium | **Attempted 15 Sept 2026** (`targets/catokwacopa/NOTES.md`). The interleave-with-omissions mechanism and the Oxford reading (Estes, Dave, Ernst, Krajčovič) were measured rather than extended: the pairing is structural, most published readings are exact, name cribs are unique among 1,645 names (CONINGTON, JOWETT, SHIRLEY, HERTFORD), two exact alternatives found (CHANGE ADOPTED, HOLIDAYS EXAMINE), and lines 9/26, 12, 23, 29 are shown undecided by the letters |
| **33** | **Censorship manual steganograms** | blocked | **Attempted 15 Sept 2026** (`targets/censorship/NOTES.md`). Shift direction and predicted Morse sequences established; the carrier is pen marks beside the tram bands, 2–5 px in the best public image, so dots and dashes cannot be separated. Blocked on a high-resolution scan of TNA KV 2/2424 |
| 12 | Scorpion letters, 1991 | attempted 2026-09-15, closed | S5 transcribed (180 symbols, 145 distinct, every repeat at a multiple of 16), S1 transcribed here (70, 53 distinct, weak period-5 signal p = 0.04). Both are below the unicity distance for a homophonic key (key 249 vs 224 bits, 682 vs 576 bits) and matched controls show the annealer returns fluent English at 3-13% accuracy, so every claimed solution is unfalsifiable. Needs S2-S4 or a glyph-feature key model. See `targets/scorpion/NOTES.md` |
| 23 | Copenhagen cryptogram | attempted 2026-09-15, closed from the scan | Transcribed twice (20 and 25 symbols); ten languages x six token conventions plus a word-separator hypothesis, 5-gram annealing with dictionary re-ranking: nothing readable, best -2.7 nats/letter, while matched controls of the same length in Danish, German, English, Latin and Swedish are recovered at 96-100% and -1.4 to -2.1. Not a simple substitution of those languages as read, or both readings share an error. Danish fits no better than Latin. Needs the original slip or a better scan. See `targets/copenhagen/NOTES.md` |
| **18** | **Moustier altar inscriptions** | medium-low | ~100 characters over two altars. Huylebrouck's 2022 hypothesis ties it to Trithemius's *Ave Maria* scheme, each ciphertext letter standing for a prayer word — testable. But Thomas Ernst's caution is serious: the stonecutter used letter extenders and at least four distinct L-shapes, so the standard transcriptions may conflate distinct symbols and the published frequency counts may be misleading |
| **17** | Roosevelt cryptogram, 1935 | attempted 2026-09-16, explained | Number block read at glyph level from the 300 ppi Internet Archive scan of *The Friedman Legacy*: a permutation of 1..52 (singles 1-9, tick-joined pairs 10-52, each once) with 18 zeros in groups of 6, 6, 3, 3. Ernst's doodle claim confirmed. Statistics reject a fair shuffle (rank correlation +0.39, 16 rising chains vs 26.5, run 39 40 41 42; p 0.002 to < 5e-6) and fit a hand-written list; a riffled deck fits worse. Ordered homophonic and rank-key readings annealed with an English 5-gram model reach -2.6 nats/letter with junk while 7 of 8 matched 52-letter controls are read at 88-100 % and -1.5 to -2.0. Unordered keys untestable. Needs the original sheet (NSA Friedman Collection). See `targets/roosevelt/NOTES.md` |
| **29, 30** | **Pollaky; Harry-Caroline and Tissie-Jabber** | low | Victorian agony-column ads, scans public, but each is ten words or so. Tissie-Jabber is four-letter groups over the alphabet {a,b,c,d,n,o} — highly structured and possibly not letters at all; Ernst suggests race bets. Pollaky destroyed his records, so no key will surface |
| **16** | Lima, Ohio robbery, 1916 | low | ~110 letters, and **variant transcriptions are a real obstacle**. Pelling proposed two alternating monoalphabets in April 2025; the follow-up partial readings are mutually inconsistent |
| **9** | Rubin, 1953 | low | One typewritten slip, ~a dozen lines. Contains the plaintext names "Dulles" and "Conant" plus pseudo-words. No claimed solution of any standing |
| **7, 31, 44** | Cigarette case 1909; MLH 1974; bullet 1944 | low | Four engraved lines; four lines of ballpoint symbols; 44 letters. All far too short |
| **43** | Rayburn, 2004 | low | ~80 mixed characters, all underlined or struck through. The recurring and plausible reading across both the Schneier and Cipherbrain threads is that it is a **handwritten password list**, not a cipher |
| **25** | SS radio message, 1944 | low | Six lines, and **probably a forgery**: wrong German typography, wrong SS rank abbreviations, an anachronistic stamp, contradictory unit locations. Treat as questionable before spending anything on it |
| **24** | Erba murder, 2006 | low | A few lines on one Bible page. **The blocker is sourcing**: only a press photograph circulates, with no authoritative transcription |
| **38** | Sufi Fiddle | low | Seven lines of unidentified Arabic-derived script; **no transcription has ever been published**, only photographs, and the script itself is not identified. A palaeography problem before it is a cipher problem. Provenance rests on a novel's afterword |

## 5. What to do next, if anything

Three of the four **high** entries are unusual in that the work is not "break a cipher" but
"finish something somebody already started and abandoned":

* **46** needs a published table of which of the 22 ADFGVX messages are solved, assembled from a
  2017 comment thread, plus garble reconstruction on the ~9–10 nobody has touched. The keys are
  known. This is closer in kind to the Armstrong-to-Madison codebook work than to a real unsolved
  cipher, and it would be a genuine service to the field.
* **28** has a claim made in August 2026 and a rebuttal made in September 2026, neither adjudicated.
  The materials are digitised and the test is mechanical.
* **19** has a named crib — the 1876 Synodal Bible — asserted and never demonstrated.

**3 (Debosnys)** turned out to have a transcription already (Sektu, 2017, unreleased); its cipher poem is
now known to be rhyming couplets, which makes a shape search over French verse the next step.

---

### Files

| file | what it does |
|---|---|
| `top50.json` | all fifty entries with titles, article URLs and post dates |
| `crossref.py` | the classification: closed, not-tractable, already-tracked, open |
| `arts/` | source articles for the candidates assessed above |
