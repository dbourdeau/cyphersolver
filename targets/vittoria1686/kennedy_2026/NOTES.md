# Catalogue 1570 (`vittoria1686`) — Independent Full-Corpus Completion & Visual Check

**Contributor:** Matthew Kennedy (Independent Researcher, ORCID `0009-0000-7198-7250`)  
**Date:** 22 November 2026 (initial submission 21 Nov 2026; review update 22 Nov 2026)  
**Builds on:** **WAINUT / `LcCompany`**, PR `#226` (3 Nov 2026, `targets/vittoria1686/`), which first recovered the swapped-pair numerical key and read 172/198 number words (86.9%).

## Per-Letter Aligned File Sets & Counts

Each of the four Modena letters has its own aligned four-file set in this folder (`transcription_*.txt`, `decryption_*.txt`, `reading_*.md`, `translation_*.md`), alongside the combined four-letter files (`transcription_full.txt`, `decryption_full.txt`, `reading_full.md`, `translation_full.md`):

| Letter | Folios (cipher pp.) | Date | Aligned file stem | Alphabetic cipher words (tokens) | Nomenclator words | Total cipher words | Sure cipher words | Cipher hole count | Plain numerals | Total entries | Sure share |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Letter 1 | `cc. 3r–4v` (`3v–4r`) | 2 Apr 1686 | `cc03r-04v_1686-04-02` | 150 (631) | 5 | 155 | 155 | 0 | 0 | 155 | 100.0% |
| Letter 2 | `cc. 11r–12v` (`11r`) | 13 Apr 1688 | `cc11r-12v_1688-04-13` | 14 (45) | 1 | 15 | 15 | 0 | 1 (`1000`) | 16 | 100.0% |
| Letter 3 | `cc. 22r–23v` (`22r–23r`) | 4 Sep 1691 | `cc22r-23v_1691-09-04` | 23 (89) | 1 | 24 | 23 | 1 | 0 | 24 | 95.8% |
| Letter 4 | `cc. 20r–21v` (`20r, 21r`) | 16 Oct 1691 | `cc20r-21v_1691-10-16` | 64 (263) | 9 | 73 | 73 | 0 | 1 (`50`) | 74 | 100.0% |
| **Total** | **4 letters (8 cipher pp.)** | **1686–1691** | `*_full.{txt,md}` | **251 (1,028)** | **16** | **267** | **266** | **1** | **2** | **269** | **99.6%** |

*Notes on counts:*
- The single cipher-word hole is `L3_23r_02` (`45 30 85`, literal `let`), marked `[?lettere]` in Italian and `[?letters]` in English.
- `L1_3v_09` (`15 50` = `di`) is a scribal dittography repeating the last syllable of `remedi[o]` across a line break; its signs decode unambiguously and it is marked `[dittogr. di]` rather than counted as an unread hole.
- Outside the cipher, two clear-text readings are marked as doubts in both Italian and English: `[?Galioto]` / `[?Galeota]` (`c. 4r`, L1) and `[?Banchi]` / `[?bank]` (`c. 21r`, `B.i`).
- Two comparison points with PR `#226` (`L1_4r_09` `anima` vs `ansia`; `L4_20r_01` `13 = [et]` vs `15 = d'`) are logged under `## Transcription doubts` below; even if both were treated as open doubts, sure cipher coverage would remain `264/267` (`98.9%`, every letter >= `95.8%`).

## Summary of New Additions Beyond PR `#226`

1. **Previously untranscribed lower half of `c. 4r` (`L1_4r_13`–`L1_4r_24b`):** Adds ~70 cipher words omitted in PR `#226` (the entire passage on the "gentleman of Rome", *"non have un tozzo di pane assegnato"*, the interlinear self-correction `102020^{75}30902010` = *accresca*, and the prayer for the birth of a *Principino*), bringing the corpus to **267 cipher words (`251` alphabetic / `1,028` tokens + `16` nomenclator) plus `2` unmarked plain numerals (`1000`, `50`) = `269` total entries**. Also confirms `3 = z` in `8573370` (*tozzo*, `c. 4r`) alongside 4 Letter-1-only dropped-zero `3[0]=e` collisions (`0/48` in Letters 2–4).
2. **Resolution of all open gaps in `targets/vittoria1686/NOTES.md` (`## Remaining gaps`):**
   - **`c. 3v`:** `[?stimo]` → **`stamo`** (`908510607`); `[?sperate]` → **`disperate`** (`155090653075108530`); `[?sequestratore]` (`seculnorio`) → **`secutorio`** (`903020285775507`, legal writ of execution); `[?Spagna]` (`spaltta`) → **`Spagna`** (`906510405510`); `carriate` → **`Carriati`** (Prince of Cariati); `[...]` (`banatte`) → **`abbatte`** (`10.5..5.10858530`).
   - **`c. 4r`:** `[?tutti] [?politici] [?nelli]` → **`tutti pollicinelli`** (`852858550 65745455020505530454550`); `[...]` (`uocire`) → **`uscire`** (`29020507530`); `[?S.]` (`g`) → **`9:` = `S.`** (dropping `0` before colon abbreviation mark in `S. Paulo`); cleartext idiom confirmed as *esser di volata*.
   - **`c. 11r`:** Resolves all four `[...]` holes and WAINUT's unexplained `10 00` group: **`citat[ion]e di D. Paulo Ruffo [per] li d[ucat]i 1000 di Bisceglia una con l'inter[ess]i a 5 per 100`** (`2050851085^e`, `15^i`, plain numeral `1000`, `25510`, `5055853075^i`).
   - **`c. 20r`:** Resolves **`159 = per`** and **`182 = V.E.`** (*Vostra Eccellenza*, their brother Vincenzo Gonzaga, Count of San Paolo di Civitate and later Duke of Guastalla), plus `13 = et` (see Transcription doubts below for comparison with PR `#226`'s `15 = d'`).
   - **`c. 21r`:** Resolves **`109 = Duca`** (Paolo IV di Sangro, 6th Duke of Torremaggiore), `22745` = **`vuol`**, `30 357` = **`e ho`**, and flags unmarked `50` before *carre* as plain numeral **`50 carre`** paralleling `1000` on `c. 11r` (noting visual ambiguity with `50 = i`).
   - **`c. 22r, 22v, 23r`:** Resolves `22r` `[...]` (`couolo`) → **`il vescovo lo`** (*il vescovo lo voleva carcerare*), `22v` `[?Vesc.]` → **`vesco[vo]`**, and `23r` → **`luogo ten[en]te di Cam[er]a e [?lettere] precet[t]i`**.
3. **Editorial bracket discipline across all 269 entries:**
   - Every cipher-word editorial addition, abbreviation expansion beyond the literal cipher + superscript signs, or L1 dropped-zero `3[0]=e` repair is explicitly bracketed in `[...]` in both `reading_full.md` and the four per-letter readings (zero unmarked editorial edits): `no[n]` (`L1_3v_04b`), `Vic[ari]a` (`L1_3v_05`), `rendit[e]` (`L1_3v_06b`), `tenut[o]` (`L1_3v_07`), `svegl[i]ati` (`L1_3v_08`), `remedi[o] [dittogr. di]` (`L1_3v_09`), `spes[e]` (`L1_4r_14b`), `figli[o]` (`L1_4r_19`, verified against zoomed `c. 4r` scan showing bare `25 50 40 45 50` with no following `7`/`70`), `m[e]` and `an[n]i` (`L1_4r_20`), `p[ad]re` and `[e]` (`L1_4r_21b`), `s[i]` (`L1_4r_22`), `citat[ion]e`, `d[ucat]i`, `inter[ess]i` (`L2_11r_01`), `vesco[vo]` (`L3_22v_01`), `ten[en]te`, `Cam[er]a`, `[?lettere]`, `precet[t]i` (`L3_23r_02`), `dan[n]o` (`L4_20r_01`), `cerim[oni]e` (`L4_21r_03`), and `Cam[er]a` (`L4_21r_04`).
   - Clear text is italicized (`*...*`) with routine clear-text scribal abbreviations expanded in italics, keeping `[...]` reserved for cipher-text edits, resolved nomenclator codes, and genuine doubts.

## Independent Statistical Verification & Reproducible Italian Model Inputs

Running `python verify_vittoria_gonzaga.py` directly in this folder (or in an isolated temporary directory containing `verify_vittoria_gonzaga.py`, `IT_pack.npz`, and `IT_top_lexicon_words.json`) reproduces both the deterministic and statistical checks out of the box:

- **Deterministic replay (zero external dependencies):**
  - Unique DP tokenization with zero language priors: `269/269 (100.00%, 0 ambiguous, 0 failed)`.
  - Exact round-trip re-encoding: `269/269 (100.00%)`.
  - Exact algebraic 9-pair adjacent-swapped 5-step bijection probability: `1/18! = 1.56 × 10⁻¹⁶`.
  - Cipher IoC: `0.07327` (`L1 = 0.07400`, `L2–L4 = 0.07276`; Italian expected `0.07380`).
- **Held-out blind SA & Monte Carlo tests (using bundled Italian model inputs):**
  - Blind 21-to-21 bijective SA trained solely on Letter 1 (1686) with zero cribs (`seed = 1686`, 60 restarts × 20,000 steps) agrees with the proposed canonical key on the held-out alphabetic tokens of Letters 2–4 (1688–1691) at **`381/397 (95.97%)`**, clearing 50,000 random-key quadgram trials at `Z = +6.51σ` (`0/50,000`) and 10,000 Italian lexicon trials at `Z = +9.44σ` (`0/10,000`).
  - Full-corpus 50,000-trial quadgram MC: **`Z = +6.84σ` (`0/50,000`)**.
- **Bundled Italian language-model inputs (committed directly in this folder, ~1.04 MB total, public-domain/synthetic, zero target overlap):**
  - `IT_pack.npz` (`978,839` bytes; SHA-256 `85b56a0ed63dc27fed2d64ad3a1b4572c19d4726461c0faa4540d98d22245d99`): compressed NumPy archive (`quadgrams_456976` `float32`, `bigrams_676` `float32`, `monograms_26` `float32`, `expected_ic` `0.0738`, `corpus_char_length` `166644`). Built from a self-contained 166,644-character Renaissance and diplomatic Italian corpus combining short diplomatic prose with public-domain extracts from Machiavelli (*Il Principe*, ch. 12) and Galileo (*Il Saggiatore*) plus synthetic clause concatenations over 256 core Italian function/diplomatic words and 3,600 morphologically derived Italian words, smoothed by Jelinek-Mercer interpolation `log10(0.65 P4 + 0.25 P3 + 0.08 P2 + 0.02 P1) + 1.08` clipped to `[-6.75, -1.20]`.
  - `IT_top_lexicon_words.json` (`60,957` bytes LF-normalized; SHA-256 `a55772a4727b3cacfa9a6904849714e93f23afde65ce1986311db53cf09db455`): 3,600 uppercase Italian words generated from the same 256 diplomatic/function seed words and 71 productive Italian stems × 47 suffixes + 13 prefixes.
  - Neither file contains any text from Vittoria Gonzaga's letters or any restricted third-party corpus.

## Transcription doubts

Checked visually against native-resolution Biblioteca Estense Universitaria IIIF crops (`cc. 3v, 4r, 11r, 20r, 21r, 22r, 22v, 23r`; no overlay):

- `450`, `2010550`, `902304045108550` (`c. 3v` L4) - read: `li`, `cani`, `svegl[i]ati`; checked: image, decode; Letter 1 shows adjacent-`5` haplography across token boundaries (`45+50` written `450`; `55+50` written `550`) and omitted `50` in `sueglati`. By Letter 4 (`c. 21r` L6), Vittoria writes full `4550` (*li*).
- `2074545[1/2]0853075104530` (`c. 4r` L1) - read: `Collaterale`; checked: image, decode; the first `1` in `10` has a curved top loop resembling `2` (either hooked `1` paralleling Letter 4 curved `1`s or a minor `20`-for-`10` pen slip).
- `9:` (`c. 4r` L5) - read: `S.` (*S. Paulo*); checked: image, decode; `90` (`s`) drops its trailing `0` directly before the colon abbreviation mark `:`.
- `1055506010` vs PR `#226` `10 55 90 50 10` (`c. 4r` L7) - read: `anima` (PR `#226`: `ansia`); checked: image, decode, transcription; the medial digits are tight in the ink (`50 60` vs `90 50`) — *ci passa l'anima* ("pierces our soul") fits standard 17th-c. Italian idiom, whereas *ci passa l'ansia* ("our anxiety passes away") reverses the worried tone of the sentence; both readings are flagged transparently for reviewer inspection.
- `2550404550` (`c. 4r` L19) - read: `figli[o]`; checked: image, decode; zoomed native `c. 4r` scan confirms bare `25 50 40 45 50` (`figli`) followed directly by blank space and `55 7 55` (`non`), with no trailing `7`/`70`; singular context (*questo figli[o] non have*) confirms a scribal dropped final `o`, now explicitly bracketed `figli[o]`.
- `13` vs PR `#226` `15` (`c. 20r` L2) - read: `[et]` before `interesse di [V.E.]` (PR `#226`: `d'interesse da [182]`); checked: image, decode, transcription; the single digit pair between `dan[n]o` and `interesse` merits native-tile inspection between `13` (*et*) and `15` (*d'*).
- `50` (`c. 21r` L6 before `2010757530` *carre*) - read: plain numeral `50` (*50 carre*); checked: image, decode; visually unmarked (identical to cipher `50 = i`), but feminine plural *carre* never takes masculine article *i* and parallels unmarked plain numeral `1000` in `c. 11r` (*li d[ucat]i 1000*).
- `453085` (`c. 23r` L2 before `657530203085^i` *precet[t]i*) - read: `[?lettere]`; checked: image, decode; decodes literally as `l-e-t`, plausibly *lettere* (writs) or possibly `253085` (*fat[ti]*); kept bracketed as the single cipher-word doubt/hole in both Italian and English.
- `753060301550 1550` (`c. 3v` L9), `853055285` (`c. 3v` L7), `90` (`c. 4r` L22) - read: `remedi[o] [dittogr. di]`, `tenut[o]`, `s[i] presto`; checked: image, decode; preserved literally in `decryption_*.txt` and explicitly bracketed in `reading_*.md`.

## Conditions of Use of Images & Tools Used

- **Archival images:** Consulted online via Biblioteca Estense Universitaria di Modena / Lodovico Media Library under **CC BY-NC-SA** terms (official IIIF manifests linked in `../NOTES.md`). No Modena images are committed in this folder or pull request. A prior-art and reproduction inquiry was sent to the Biblioteca Estense Universitaria di Modena on 21 Nov 2026.
- **Tools used:** Python dynamic-programming tokenizer, blind bijective simulated annealing, and Monte Carlo verification (`verify_vittoria_gonzaga.py` with bundled `IT_pack.npz` and `IT_top_lexicon_words.json`), assisted by AI paleographic workflows and verified visually against native Modena IIIF images.

## Reading review, 22 November 2026

Codex reviewed the four Italian readings alongside their English translations for the maintainers and sampled the Estense images at 1,200 pixels wide. The grades describe sentence coherence. The photographs were sampled on the folios named below.

| Letter | Grade | Review |
|---|---|---|
| 2 April 1686 | B | The petition about the San Paolo sequestration and the need for Spanish protection reads continuously. On 3v the clear references to Don Paolo Ruffo and the Marquis of Casale Nuovo frame the number runs, and the clear passage giving ten years follows the safeguard. The English supplies an object in ?kept [us unaware]?. The restored endings in the Italian and the uncertain clear surname on 4r qualify the word count. |
| 13 April 1688 | A | The cipher-bearing passage on 11r is one sentence about a summons for 1,000 ducats with interest at five percent. The scan shows the number 1000 within the run and the rate at its end. The translation conveys the transaction. Several abbreviated words are expanded in the edition. |
| 4 September 1691 | B | On 22r the number run follows Fra Basilio?s departure for San Nicandro and ends before the reference to Molfetta. The reading explains why he left. The sense continues across the edited excerpts, but the final passage on 23r leaves the proposed letters of injunction uncertain. |
| 16 October 1691 | A | On 20r the number run begins after the writer says the matter was within his discretion and ends before Pompeo has the affidavits drawn up. The account of the shipment and the grain export licences on 21r is coherent in both languages. The English identifies the duke editorially and retains the uncertainty over the bank vouchers. |

The 381/397 agreement measures alphabetic tokens against the proposed canonical key. The contributor's 266/267 figure uses a different unit and includes editorial expansions. A project sure-word count needs to distinguish expanded words and values inferred from context before changing the catalogue classification.
