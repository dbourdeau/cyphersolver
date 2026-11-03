# Independent verification: francescoeste1546 (Francesco d'Este to Ferrante Gonzaga, 13 Apr 1546), c. 42r

Verifier, 3 Nov 2026. Adversarial check. No solver file was edited. Scratch work, crops and the rebuild were done outside
the folder.

## Verdict

**FIX before any PR. Status: read in part (c. 42r only; 42v-43r not transcribed).**
The system is real and the contemporary interlinear decipherment matches the signs. The held-out tests reproduce and are
well above the shuffled baselines. The c. 42r deliverable still has transcription errors that an eye check catches
easily, several gloss misreads, a misaligned marked reading in L09, L11 and L12, a check that does not tie the reading to
the clear, and vendor names and local paths in five scripts.

NOTES.md says "Every line was then read by eye on full-size crops". The errors below, among them five clearly written
signs missing at the end of L11, show that the eye check was not done or did not work.

## 1. Blind transcription first

Before opening any solver transcription, decryption, reading or key file, I cut c. 42r (`scans/c0_full.jpg`) into
full-size half-line strips and transcribed every cipher line myself, using only the legend names. That gave 483 sign names
on 15 lines: the solver's 14 lines, plus the opening group after "Sapera dunq". This covers the whole of the internal
held-out passage (solver L07-L13). I read the gloss over every line independently.

Comparison by aligned sign (difflib): **54 disagreeing units out of about 470, so 11.5% raw.**

Each disagreement was settled on crops enlarged 1.25x to 2x:

- **Naming or convention only, about 21 units.** These are not errors:
  - the raised loop after omega (`w o` vs `w`);
  - a dropped raised o before v in `o v` pairs (the solver writes `v` alone in L03 ×2, L10, L12 ×2; in a few places the
    loop is visible, but the value r is unaffected);
  - the hatted n before x (`M` vs `h`);
  - `u l` vs `U`;
  - the f-sign called `n` vs `h`;
  - phi `P` vs `q`.
- **Verifier wrong, about 8 units.** L00 first sign m, not pi. L02 "particolare": A, not "s a". L04 struck group: psi and
  "m m", not "y m u". L07 "promessa": `r w L`, not `r o L`. L12 "volerne": `5`, not `s`. L12 first sign: phi.
- **Solver wrong, about 22 units, plus a 4-sign group omitted**, as settled on crop:

| line (solver numbering) | solver | crop shows | effect |
|---|---|---|---|
| before L00 ("Sapera dunq ...") | (missing) | `n o pi w` | a 4-sign cipher group left out of the transcription and the counts |
| L00 last group | `T q m` | `T e m` (long sweeping tail, the same shape as the e earlier in the line) | unglossed group |
| L01 | `8 q? A o +` | `8 e 4 o +` (clear open 4) | unglossed group |
| L05 end | `T T` | `T 4` | unglossed 6/4 group |
| L06 end | `q?` | a goblet/Y sign with a diagonal stroke (not q) | unglossed |
| L07 "attesa" | `q r b o + r n o q` | `q r b o + n o q` (no extra r) | spurious unglossed unit |
| L08 "che" | `3 w o +` | `3 ps o +` (clear psi) | creates a false mark {w=h} |
| L09 "beneficio" | `w o + s n x A w o m` | `w o + 4 s n x A w o m` (a 4/+ sign between o+ and s) | the solver's alignment collapses: {+n}, [n?], {x_A=f}, {o_m=c} |
| L10 "Spagna" | `[] x q o v y 4 m` | `[] x q ps 4 m` (one psi; no o v) | inserts an r into Spagna |
| L11 end | ends `[] U x` | `[] U x n o o + 4` (five clear signs) | "sen" of *senza* is lost; L12 then gets {+s}{+e}{+n} |
| L12 "determinare" | `... h c x A o v` | `... h c x 4 q o v` | "na" is forced onto A ({A=a}, {+n}) |
| L13 "da" | `q L` | `e L` (the da-sign, the same shape as in "e L" earlier in the line) | false {+d} |
| L13 "lei" | `A o + w` | `T o + w` | false {L_A=l} |

- **Unresolved, 4 units.** L08 signoria: `+` or `4` (I lean to 4). L02 struck group, last sign: q or e. L00 Sicilia:
  extra `v` after omega. L13 "da", second sign: L or u.

**Settled substantive error rate of the solver transcription: about 22 of 463 signs (4.8%), or about 26 of 467 (5.6%)
counting the omitted opening group.** Eight glossed words are directly affected: che, beneficio, attesa, Spagna (L10),
senza, determinare, da, lei. Nearly every error is in the direction of making the reading look worse, not better. I found
no sign moved toward the clear.

### Gloss (independent read)

I read the gloss myself over the whole page. It agrees with the solver's `clear_c42r.txt` except here:

- L06: the gloss reads **"de l'animo"** (cipher `pi s` = d e), not "do". The solver's {q_pi=d}{s=o} is an artefact: q is the
  4-marked group.
- L12: the gloss reads **"volerne"**, not "volere". It matches `a m T 5 (o) v 4 o +` exactly. The solver gave the `4 o +`
  to "de-" of *determinare*.
- L13: the last gloss word is **not "mai"**. It starts with an ascender and has 4-5 letters, most likely "tutto". The
  signs `A a r b m` give t-u-t-t-o under the key. The solver's {A=m}{a_r=a}{b_m=i} comes from the gloss misread.
- Clear text around the cipher, used in `reading_c42r.md`:
  - "me ne **allegro** però" (crop shows "allieg..."), not "allitigo". It makes sense: "I am sorry the matters must be
    consulted in Spain; I am glad of it however, because meanwhile, Your Excellency coming ...".
  - "**E che** ben mi dispiace", not "Ella".
  - "non si restarà di fare": future tense, "it will not fail to be done", not "did not stop me".
- The lines over `q U x n q` (gloss "a V.Ex. S.M.tà") and `L ps 4 m m` (inside "Spagna") may be abbreviation or title
  bars rather than deletions. "Struck" is an interpretation and should be marked as open.

## 2. Rebuild

I copied the folder without scans or caches and ran `python -I scripts/read42r.py` and then `scripts/check_marks.py`.
`key_c42r.tsv`, `decryption_c42r.txt`, `reading_marked_c42r.txt` and `validation/heldout_c42r.txt` are **byte-identical**.
check_marks exits 0 with "86 (verbatim 52, marked 34); 13 runs".

Fault injection:

- `T=l` changed to `T=r` (L00): **FAIL, exit 1.**
- `b=t` changed to `b=s` (L03): **FAIL, exit 1.**
- The `{+n}` no-sign mark deleted in L09: **passes, exit 0.** check_marks never compares the reading's letters with
  `clear_c42r.txt`, so a letter of the clear can be silently dropped, or the reading can drift from the clear. This gap
  must be closed: the joined letters of each line must equal the clear's letters.

## 3. Held-out tests

- **Inside c. 42r** (frozen on L00-L06, applied to L07-L13): 160 of 212 = 75.5%. Shuffled tables: mean 23.0%, max 32.1%.
  Reproduced. It is graded against the gloss read (`clear_c42r.txt`), an independent contemporary text, not against the
  solver's own reading. But it uses the solver's flawed transcription and their gloss read, including the misreads above.
- **42v-43r** (`heldout.py`, pass A or B, frozen c0 key): 841 of 1151 = 73.1% (shuffled mean 28.3%, max 39.6%) and 774 of
  1151 = 67.2% (26.6% / 37.3%). Reproduced. It is graded against a model gloss read that was not checked, over unsettled
  model passes. It shows the key generalises. It is not a reading of 42v-43r.
- Both use DP alignment with free skips. The shuffled baseline controls for that, and the gap is large, so the key is real.

## 4. Counts and the honest headline

As filed: 99 word-slots, made of 86 glossed words and 13 unglossed runs (14 with the omitted opening group).

- Sign-for-sign with no mark: 52 words.
- With marked repairs: 34 words.
- Read as sense: 86 of 99 = 86.9%, or 86 of 100 with the omitted group.
- Strictly verified, 52 of 99 = **52.5%**.

After the corrections above, several marks would disappear: che, da, lei, beneficio, senza, volerne, tutto, de, venendo.
That cannot be claimed until the files are redone.

**Honest headline:** "c. 42r: 86 of about 100 cipher words read through the contemporary decipherment (52 checked sign by
sign, 34 with marked repairs). About 14 short groups under the writer's 6/4 marks are unread. 42v-43r (40 lines) not
transcribed." That is **read in part**, well under the 95% bar. For the letter as a whole, about 440 of about 1,830 signs
are covered.

## 5. Reading files graded

- **`reading_c42r.md` — B.** It makes coherent sense because it is the contemporary gloss. Weak places:
  - "do l'animo" should be "de l'animo";
  - "volere" should be "volerne";
  - "da lei mai" should be "tutto" (the English "ever" is nonsense);
  - "me ne allitigo" / "I take my stand on it" should be "me ne allegro" / "I am glad of it";
  - "Ella ben mi dispiace" should be "E che";
  - "did not stop me from doing it" has the wrong tense and subject;
  - the [6]/[4] groups are unread;
  - "struck" is an interpretation.
- **`reading_marked_c42r.txt` — C.** The alignment is wrong in several lines:
  - L11: "venendo" is spread over the 6/4 groups ({e=v} {T_n_o=e} {q_a=n}). In fact `a s 4 o+ 4 pi m` = venendo exactly.
  - L12: {+s}{+e}{+n}{P=z} for "senza".
  - L09: "beneficio" collapses.
  - L06: {q_pi=d}{s=o}.
  - L13: "da", "lei" and "mai".
  - L08: {w=h}.

  Many of the 34 "marked" words are artefacts of transcription or gloss errors, not real gaps.

## 6. Vendor names and local paths

- `scripts/gloss.py`, `scripts/inventory.py`, `scripts/pass_c.py`: provider and model id strings (a provider name and a model id; replaced by this phrase in the copy
  filed with the target).
- `scripts/gloss.py`, `inventory.py`, `pass_blind.py`, `pass_blind_prompt.py`, `pass_c.py`: hard-coded local Windows
  paths (user directory).
- These scripts also import a local helper module that is not in the folder.
- `scripts/__pycache__/` is present and must not be committed.
- NOTES.md says "a vision model" and "two different vision models". This must become "AI language-model agents".
- No hits in the data, reading or NOTES text otherwise. No mention of other archives.

## 7. Prior art

One web search ("Francesco d'Este" "Ferrante Gonzaga" 1546 cifra Granvela "marchese del Vasto") found no edition or
decipherment of this letter. This agrees with the solver's check (only the pointer in Dan's entry 1564).

## Must fix

1. Correct the transcription:
   - add `n o pi w` (opening group);
   - L00 `T e m`;
   - L01 `8 e 4 o +`;
   - L05 `T 4`;
   - L06 last sign: not q;
   - L07 drop the extra r;
   - L08 `3 ps o +`;
   - L09 add the 4/+ in beneficio;
   - L10 `[] x q ps 4 m`;
   - L11 add `n o o + 4`;
   - L12 `x 4 q o v`;
   - L13 `e L`, `T o + w`.

   Then check the 4 unresolved signs and restore the raised o in the `o v` pairs.
2. Correct the gloss reads: de, volerne, tutto (recheck at full size). Correct the clear context in reading_c42r.md:
   allegro, E che, restarà.
3. Rerun read42r.py and check_marks.py, and recount. Add to check_marks a test that the reading's letters equal the clear.
4. Remove vendor ids, local paths, the local-helper dependency and `__pycache__`. Reword "vision model" in NOTES.
5. State the headline as read in part, with the strict 52-of-99 figure next to the 86-of-99. Withdraw or redo the claim
   that every line was read by eye on full-size crops.
6. Mark the "struck" groups as possibly abbreviation bars.
