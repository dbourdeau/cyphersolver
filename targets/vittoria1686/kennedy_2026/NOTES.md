# Catalogue 1570 (`vittoria1686`) — Independent Full-Corpus Completion & Ink Audit

**Contributor:** Matthew Kennedy (Independent Researcher, ORCID `0009-0000-7198-7250`)  
**Date:** 21 November 2026  
**Builds on:** **WAINUT / `LcCompany`**, PR `#226` (3 Nov 2026, `targets/vittoria1686/`), which first recovered the swapped-pair numerical key and read 172/198 number words (86.9%) via AI agents without human paleographic verification.

## Summary of New Additions Beyond PR `#226`

1. **Previously untranscribed lower half of `c. 4r` (`L1_4r_13`–`L1_4r_24b`):** Adds ~70 cipher words omitted in PR `#226` (the entire passage on the "gentleman of Rome", *"non have un tozzo di pane assegnato"*, the interlinear self-correction `102020^{75}30902010` = *accresca*, and the prayer for the birth of a *Principino*), bringing the corpus to **267 cipher words (`1,028` alphabetic tokens) + `16` nomenclator words + `2` unmarked plain numerals (`1000`, `50`)**. Also confirms `3 = z` in `8573370` (*tozzo*, `c. 4r`) alongside 4 Letter-1-only dropped-zero `3[0]=e` collisions (`0/48` in Letters 2–4).
2. **Resolution of all open gaps in `targets/vittoria1686/NOTES.md` (`## Remaining gaps`):**
   - **`c. 3v`:** `[?stimo]` → **`stamo`** (`908510607`); `[?sperate]` → **`disperate`** (`155090653075108530`); `[?sequestratore]` (`seculnorio`) → **`secutorio`** (`903020285775507`, legal writ of execution); `[?Spagna]` (`spaltta`) → **`Spagna`** (`906510405510`); `carriate` → **`Carriati`** (Prince of Cariati); `[...]` (`banatte`) → **`abbatte`** (`10.5..5.10858530`).
   - **`c. 4r`:** `[?tutti] [?politici] [?nelli]` → **`tutti pollicinelli`** (`852858550 65745455020505530454550`); `[...]` (`uocire`) → **`uscire`** (`29020507530`); `[?S.]` (`g`) → **`9:` = `S.`** (dropping `0` before colon abbreviation mark in `S. Paulo`); cleartext idiom confirmed as *esser di volata*.
   - **`c. 11r`:** Resolves all four `[...]` holes and WAINUT's unexplained `10 00` group: **`citat(ion)e di D. Paulo Ruffo [per] li d(ucat)i 1000 di Bisceglia una con l'inter(ess)i a 5 p[er] 100`** (`2050851085^e`, `15^i`, plain numeral `1000`, `25510`, `5055853075^i`).
   - **`c. 20r`:** Resolves **`159 = per`** and **`182 = V.E.`** (*Vostra Eccellenza*, their brother Vincenzo Gonzaga, Count of San Paolo di Civitate and later Duke of Guastalla), plus `13 = et` (see Transcription doubts below for comparison with PR `#226`'s `15 = d'`).
   - **`c. 21r`:** Resolves **`109 = Duca`** (Paolo IV di Sangro, 6th Duke of Torremaggiore), `22745` = **`vuol`**, `30 357` = **`e ho`**, and flags unmarked `50` before *carre* as plain numeral **`50 carre`** paralleling `1000` on `c. 11r` (noting visual ambiguity with `50 = i`).
   - **`c. 22r, 22v, 23r`:** Resolves `22r` `[...]` (`couolo`) → **`il vescovo lo`** (*il vescovo lo voleva carcerare*), `22v` `[?Vesc.]` → **`vesco[vo]`**, and `23r` → **`luogo ten(en)te di Cam(er)a e [?let(tere)] precet(t)i`**.
3. **Independent statistical verification (`verify_vittoria_gonzaga.py`):**
   - Unique DP tokenization with zero language priors: `269/269 (100.00%, 0 ambiguous, 0 failed)`.
   - Blind 21-to-21 bijective SA trained solely on Letter 1 (1686) with zero cribs generalizes to unseen Letters 2–4 (1688–1691) at **`381/397 (95.97%)`**, clearing 50,000 random-key quadgram trials at `Z = +6.51σ` (`0/50,000`) and 10,000 Italian lexicon trials at `Z = +9.44σ` (`0/10,000`).
   - Full-corpus 50,000-trial quadgram MC: **`Z = +6.84σ` (`0/50,000`)**; exact algebraic 9-pair swapped bijection probability `1/18! = 1.56 × 10⁻¹⁶`.

## Transcription doubts

Checked against native-resolution Biblioteca Estense Universitaria IIIF crops (`cc. 3v, 4r, 21r` verified visually stroke-by-stroke; no overlay):

- `450`, `2010550`, `902304045108550` (`c. 3v` L4) - read: `li`, `cani`, `suegl[i]ati`; checked: image, decode; Letter 1 shows adjacent-`5` haplography across token boundaries (`45+50` written `450`; `55+50` written `550`) and omitted `50` in `sueglati`. By Letter 4 (`c. 21r` L6), Vittoria writes full `4550` (*li*).
- `2074545[1/2]0853075104530` (`c. 4r` L1) - read: `Collaterale`; checked: image, decode; the first `1` in `10` has a curved top loop resembling `2` (either hooked `1` paralleling Letter 4 curved `1`s or a minor `20`-for-`10` pen slip).
- `9:` (`c. 4r` L5) - read: `S.` (*S. Paulo*); checked: image, decode; `90` (`s`) drops its trailing `0` directly before the colon abbreviation mark `:`.
- `1055506010` vs PR `#226` `10 55 90 50 10` (`c. 4r` L7) - read: `anima` (PR `#226`: `ansia`); checked: image, decode, transcription; the medial digits are tight in the ink (`50 60` vs `90 50`) — *ci passa l'anima* ("pierces our soul") fits standard 17th-c. Italian idiom, whereas *ci passa l'ansia* ("our anxiety passes away") reverses the worried tone of the sentence; both readings are flagged transparently for reviewer inspection.
- `13` vs PR `#226` `15` (`c. 20r` L2) - read: `[et]` before `interesse di [V.E.]` (PR `#226`: `d'interesse da [182]`); checked: decode, transcription; the single digit pair between `dan[n]o` and `interesse` merits native-tile re-verification between `13` (*et*) and `15` (*d'*).
- `50` (`c. 21r` L6 before `2010757530` *carre*) - read: plain numeral `50` (*50 carre*); checked: image, decode; visually unmarked (identical to cipher `50 = i`), but feminine plural *carre* never takes masculine article *i* and parallels unmarked plain numeral `1000` in `c. 11r` (*li d(ucat)i 1000*).
- `453085` (`c. 23r` L2 before `657530203085^i` *precet(t)i*) - read: `[?let(tere)]`; checked: decode; decodes literally as `l-e-t`, plausibly *let[tere]* (writs) or possibly `253085` (*fat[ti]*); kept bracketed as doubtful.
- `753060301550 1550` (`c. 3v` L9), `853055285` (`c. 3v` L7), `90` (`c. 4r` L22) - read: `remedi[o] [dittogr. di]`, `tenut[o]`, `s[i] presto`; checked: image, decode; preserved literally in `decryption_full.txt` and marked in `reading_full.md`.

## Conditions of Use of Images & Tools Used

- **Archival images:** Consulted online via Biblioteca Estense Universitaria di Modena / Lodovico Media Library under **CC BY-NC-SA** terms (official IIIF manifests linked in `../NOTES.md`). **Zero Modena images are committed** in this folder or pull request. A formal inquiry regarding prior local transcriptions and commercial reproduction procedures has been sent to Biblioteca Estense Universitaria di Modena (`ga-esten@cultura.gov.it`, 21 Nov 2026).
- **Tools used:** Python dynamic-programming tokenizer, blind bijective simulated annealing, and Monte Carlo verification (`verify_vittoria_gonzaga.py`), assisted by AI paleographic workflows and visually audited against native Modena IIIF crops by Matthew Kennedy and an independent human-level visual reviewer.
