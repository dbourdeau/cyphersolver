# Nicholas Wotton (Compiègne/Soissons) to Queen Mary, June 1554 (BL Harley MS 1582 ff. 8-10; DECODE R8499)

Status: read in part (written up 22 Sept 2026)

DECODE refill catalogue entry 120 "N. Wottoy ? to unknown recipient", Jun 1554 (rule-scored class C). Worked 22 Sept 2026.

## What the record is

DECODE R8499 (6 images; ff. 8r, 8v, 9r, 10v, plus binding views) is a holograph despatch of Dr Nicholas Wotton,
English ambassador in France, to Queen Mary: it opens "Pleasing it your highness to understand that ...", ends "And
thus I beseech Jesu long to preserve your highness ...", dated June 1554. So "N. Wottoy ?" = Nicholas Wotton and the
recipient is the Queen. The body is mostly cipher (about 118 lines, ~3,200 signs) with clear-text connectives in
between ("the second of this present I received your highness letter of the 29 of the last ... the king being then
in his journey ... I could neither well speak with him nor with the Constable ...").

Not in CSP Foreign, Mary (BHO June and July 1554 pages checked: only Wotton to Petre 14 June and 14 July, and to the
Queen 14 July / 29 July from SP 69). No decipherment on the leaves or in print found.

## Key: DECODE R354 (TNA SP 106/2 f. 162, "France 1554")

The key is on DECODE as R354 (SP 106/2 f. 162, dated 1554, "France"): a letter alphabet with 3-6 homophones per
letter, a row of nulls ("Nihil significantia") and a large nomenclator (the Emperor, the queen's highness, the French
king, the Constable, Peter Carew, the rebels, my Lady Elizabeth, the Earl of Devonshire, the Prince of Spain, Strozzi,
Siena, Guisnes, Calais, the Low Countries, "fair words", and common words: and, the, of, to, was, what, shall, should,
have, had, hath, we, us, it, is ...). Read in `key_R354.md`. Its names (Carew, the rebels, Devonshire, Lady Elizabeth,
Prince of Spain) fit Wotton's embassy in spring-summer 1554, and the cipher of R8499 uses its signs and nulls.
Image: `img/R354.png` (git-ignored).

## Work so far

- `transcription.txt`: full sign transcription of the four cipher pages in ad-hoc tokens (158 types, 3,212 signs).
  Made before the key was found, so several tokens merge distinct key signs (w = ω and ꝏ; n = ɱ Carew and ɱ̲ we; ce =
  several loop forms; the S variants).
- `solve2.py`: incremental homophonic annealer on `lang` en-1640s; validated on synthetic controls (100% at 100-150
  signs clean; 1 run in 3 at 10% noise). Blind runs on R8499 failed: the nulls and word codes defeat it.
- With the key's nulls removed and its codes and letter values pinned (`pinrun6.py`), the text reads in part:
  "Carew was ... come to Compiègne and spake of ... with your highness' rebels with the Constable ... had many ...
  and fair words ... the pensions of the rebels ... the Low Countries ... to take part with ... the resolution taken
  between the Constable and Carew ... was departed ... satisfied ... perceived that ...". Estimated 60-70% of tokens
  read as sense; not measured against a verified text.
- Direct reading against the key confirms: p1.02 "Compiegne and spake of ... with your highness the rebels with the
  Constable"; p1.04 "... respect ...".

## Second pass (same session)

- Three reading agents worked from the key images:
  - `reading_p12.txt` (p1.01-06, about 45% sense)
  - `reading_p1b.txt` (p1.07-18, 25-35%; p1.14-18 derived from tokens, not the images)
  - `reading_p36.txt` (all of p3 and p6, 40-50%)
- Coherent stretches:
  - "that he doubting lest it be known"
  - "it were perceived that he went abroad to attempt the Emperor against"
  - "he could not find in his heart to return into [Low Countries?]"
  - "to have a gentleman"
  - "the said appointment"
  - "declared to Carew what I was and where"
  - "the Constable took"
  - "that the French king had given"
- Key corrections are in `keyfix_p12.txt`, `keyfix_p1b.txt` and `keyfix_p36.txt`:
  - x̲=s, e/=g, ꝺ=l, F=u, pt=u, ll=o, ß=w, -8=c, ∂=i
  - ⊙=the French king
  - token w merges ꝏ (and) with ω (d)
- Re-annealing with these pins did not raise the machine reading.
- Still open:
  - the frequent "ı·" sign
  - the three-valued tall s
  - the ǂ / ǂ| / ǂ· family
  - overbar/underline code variants
  - a crowned box code
- Unread: p1.19-30 and page 2 (not yet given a second pass), plus most of p1.04, 07, 14, 18; p3.01-03, 05, 16-19, 25; p6.03-05, 09, 14-22.

## Regrade (measured)

- Pages 1-2: 744 of 1,616 cipher signs read as sense (46.0%). Files: `final_p12.txt`, `key_merged_p12.md`.
  Decoded from the old tokens, not rechecked on the images.
- Pages 3 and 6: 644 of 1,329 non-null signs (48.5%). Files: `final_p36.txt`, `key_merged_p36.md`.
- Whole letter: about 47%.
- The two merged keys disagree on `ce` (null in p36, c/e in p12) and on `ss` (w vs r).
- Several tokens stand for two signs each: w, x_, u, ss, @.
- Next: re-transcribe those tokens sign by sign from the crops, apply one key to all pages, recount.

## Relabelled transcription (v2)

- Two agents split every merged token on the images:
  - Files: `transcription_v2.txt`, `labels_legend_p12.md`, `labels_legend_p36.md`.
  - w splits into AND / OMEGA (d) / HOOK_LOOP.
  - The loop sign is NULL_LOOP on p3/p6 but CURL_D (c) on p1-2.
  - @ splits into the French king ⊙ / your highness ◎.
  - x_ splits into XUND / X_BAR.
- The pinned anneal on v2 (`pinrun9.py`) reads visibly more:
  - "the Constable took it", "to talk with"
  - "the resolution taken between the Constable and Carew"
  - "Carew was departed ... satisfied ... had sent"
  - "in service to the French king", "lack of money"
- Long stretches are still garbled, so the reading remains well below 95%.
- Open:
  - values of HOOK_LOOP, SLASH_O, SS_TAIL, the Y forms, the dotted capitals
  - the codes Ie, N, 2, L2
  - page 1 crop drift

## Regrade v3 (measured on transcription_v2)

- Pages 1-2: 1,048 of 1,392 non-null signs (75.3%) counting tentative words; 722 (51.9%) firm.
  Files: `final_v3_p12.txt`, `key_v3_p12.md`, `measure_v3.py`.
- Pages 3 and 6: 1,013 of 1,345 (75.3%), strict about 70-72%.
  Files: `final_v3_p36.txt`, `key_v3_p36.md`, `measure_v3_p36.py`.
- Whole letter: 2,061 of 2,737 non-null signs (75.3%) including tentative readings; firm roughly 60%.
- Content:
  - Carew at Compiegne with the French king and the Constable.
  - The French king increased the rebels' pensions; Cardinal Farnese showed Carew favour.
  - The rebels' band to have wages; the Isle of Wight; the Prince of Spain's coming.
  - Wotton talked secretly with Carew in Paris.
  - An informer "went abroad to attempt the Emperor against the French king" and would not return into England.
  - Cornwel; twenty ensigns of new lantzknechtes; the way towards Saint Quentin; the Constable's siege; the Duke of Guise.
- Conflicts between the two v3 keys still to settle: `/` = he vs I; CURL_D null on p1-2.

## Regrade v4 (measured)

- Unified key: `key_v4.md` (`/`=he, A=me, d+=i, CURL_D null, ß=r, ß-tail=w, sy/zo=th, f=code 'be', E_DOT null).
- Pages 1-2: 732 firm + 359 tentative of 1,394 non-null signs (52.5% firm, 78.3% incl. tentative).
  Files: `final_v4_p12.txt`, `transcription_v4_p12.txt`.
- Pages 3 and 6: 1,033 firm + 51 tentative of 1,342 (77.0% firm, 80.8%).
  Files: `final_v4_p36.txt`, `key_v4_p36.md`.
- Whole letter: 1,765 of 2,736 firm (64.5%), 79.5% including tentative.
- New readings:
  - "Carew was at Compiegne"
  - "I am enformid"
  - "might be taken" / "might be kept"
  - "twenty ensignes, and lie about Laon, of new lantzknechtes"
- Open:
  - labels still merging signs: ^, ll, 6, ss, C, XUND, EE, P_
  - codes Ie (on p1-2), i, 4, S,, b=, Y_SCRIPT forms, L2, -P, CIRC_BIG, Q_TAIL, L_DOTS, N_DOT, R_DOT
  - long runs p2.25 ("the lord" + 16), p1.24, p1.28, p2.02, p2.09, p3.08-09, p3.17, p6.09, p6.13, p6.20, p6.25

## Page 1 full-resolution pass (v5)

- Lines 1-15: 270 firm / 52 tentative / 48 unread of 370 (73.0% firm, 87.0% incl. tentative).
  Files: `final_v5_p1a.txt`, `key_v5_p1a.md`.
- Lines 16-30: about 210 firm / 96 tentative / 55 unread of 361 (58.2% firm, 84.8% incl.; approximate).
  Files: `final_v5_p1b.txt`, `key_v5_p1b.md`.
- Page 1 total: about 480 of 731 firm (65.7%).
- Key splits:
  - ll: ǂ with bar = n, plain ǂ = o.
  - `>` (left triangle) = o vs `^` (upright Δ) = n.
  - pt = h.
  - the small circle is the code 'hath'.
- New readings:
  - "the ysle of Wight might be taken"
  - "he the French king hath encreasidde the pensions of dyvers of the rebels"
  - "leading of a band"
  - "fowre hundrid"
- Still open:
  - the C sign (s vs u)
  - Ie
  - CURL_D_BAR and t~ (two values each)
  - short unread runs on p1.13-15, 1.19-21, 1.24, 1.27, 1.30

## Page 2 full-resolution pass (v5)

- Lines 1-16: 302 firm / 38 tentative / 29 unread of 369 (81.8% firm).
  Files: `final_v5_p2a.txt`, `key_v5_p2a.md`.
- Lines 17-32: 201 firm / 66 tentative / 40 unread of 307 (65.5% firm).
  Files: `final_v5_p2b.txt`, `key_v5_p2b.md`.
- Page 2 total: 503 of 676 firm (74.4%).
- Whole letter now: p1 480/731 + p2 503/676 + p3/p6 1033/1342 (v4) = 2016/2749 firm (73.3%).
- New readings:
  - "the rebels may dwel in France ... til the time the French king may restowr them to the Emperor countre"
  - "certein gentlemen home send him word"
  - "in the west partis ... to take part with them ... take Plymtown"
  - "I wold first make a step to Paris ere I went ... to talk secretly with"
  - "must first speak with Carew"
  - "the resolucion taken betwen the Constable"
- Key splits: x̄-looped = e vs plain looped x = a; `^` reads o on p2 (n on p1); α· = f or k.
- Open:
  - Ie (probably Wotton's informant)
  - the 16-sign name after "the lord" (p2.25)
  - rare codes T., .M, .I, b=, N.

## Pages 3 and 6 full-resolution pass (v5) and whole-letter count

- Page 3: 532 firm / 78 tentative / 75 unread of 685 (77.7% firm, 89.1% incl. tentative).
  Files: `final_v5_p3.txt`, `key_v5_p3.md`. Key: `.B` = "not"; U_HOOK = r; F_LOOPCROSS and BBAR = f.
- Page 6: 456 firm / 126 tentative / 76 unread of 658 (69.3% firm, 88.4% incl. tentative).
  Files: `final_v5_p6.txt`, `key_v5_p6.md`. Readings:
  - "the said Cornwel"
  - "Carew namid to be twenty enseignes and lye abowte Laon, of new lantzknechtes"
  - "towardes Saint Quintin"
  - "The Constable hath ben sike"
  - "the Duke of Gwyse"
  - name "Greneberye" (tentative)
- Whole letter, all four pages on the full-resolution pass:
  1,971 of 2,750 non-null signs firm (71.7%); 2,427 including tentative (88.3%).
- Still to do:
  - unify the page keys (^ n/o, α· f/k, C s/u, CURL_D, Ie);
  - retry every unread and tentative stretch with that key;
  - resolve the rare codes: CIRC_BIG, the C-family dotted codes, Q_TAIL, TALL_F_LOOP, .p, .d, Y_LATIN, N_DOT, R_DOT;
  - read the names after "the lord" (p2.25) and after "Gwyse" (p6.27).

## Unified key v6 and full nomenclator

- `key_v6.md` settles page-to-page conflicts.
- Pages 1-2: 993 of 1,411 firm (70.4%). File: `final_v6_p12.txt`.
- Pages 3 and 6: 1,099 of 1,386 firm (79.3%). Files: `final_v6_p36.txt`, `key_v6_p36_notes.md`.
  New code: dotted y = "yet".
- Whole letter: 2,092 of 2,797 non-null signs firm (74.8%), 89.2% including tentative.
- `nomenclator_full.md`: all ~140 code entries of R354 transcribed. Proposed matches:
  - B. = of, T. = me, ꝗ. = it, crossed Z = that
  - .I = Therouanne, script y with tail = either
  - Ie (p1-2) = the Emperor's ambassador? (tentative)
  - two looped-D codes (the lords of the Council; Earl of Devonshire) to test against CURL_D
- Next: apply the nomenclator matches across all four pages and remeasure.

## Nomenclator retry (v7)

- Every code in `nomenclator_full.md` was tested against every unread and tentative stretch.
- Kept:
  - `4` = that (firm), `B.` = of (firm)
  - tentative: `.Z` = that; `T.` = me; Ie = the Emperor's ambassador (p2.03 only); L2 = Calais
- Rejected: .I Therouanne, .p, .M Trent, -P, script-y 'either'. CURL_D stays a null.
- Measured (`final_v7.txt`, `key_v7_codes.md`):

  | page | non-null signs | firm | incl. tentative |
  |---|---|---|---|
  | p1 | 734 | 66.6% | 86.1% |
  | p2 | 683 | 75.1% | 90.0% |
  | p3 | 709 | 81.8% | 90.6% |
  | p6 | 683 | 76.9% | 91.4% |
  | all | 2,809 | 75.0% | 89.5% |

- Progress by round: 47% -> 65% -> 72% -> 75% -> 75%. Gains have flattened.

## Shape pass and name lookup (v8)

- `shape_pass.md`, `final_v8.txt`:
  - Upright Δ = n (55), arched Δ = o (14); `C` barred = s (7), unbarred = u (13). The value now follows the shape.
  - Two double-transcribed signs removed.
  - New readings: "two hundred", "fowre hundrid", "mysteries".
  - Rare dotted codes match no legible cell of R354; the N and R codes are probably names absent from this copy of the key.
  - Page 1 runs re-read at full resolution: tokens confirmed, still no words.
- `names_lookup.md`: p2.25 "the lord Brymstane (Crichton of Brunstane?), a Scot" (medium); p6.27 "Gaspard"? (low).
  CSP Foreign Mary gives no crib.
- Measured v8: 2,801 non-null signs, 75.0% firm, 89.4% including tentative. Unchanged from v7; gains have stopped.

## Contemporary decipherment found (not online)

- The Harleian catalogue (1808, vol. 2 pp. 138-139, `lit/harlcat2.txt`) and the BL catalogue record (searcharchives.bl.uk
  040-002047412) both describe it:
  - "ff. 5r-7v: Letter of Nicholas Wotton (?) to Queen Mary I, 13 June 1554 (?). This is probably a contemporary copy
    deciphering the letter of ff. 8r-10v."
  - "ff. 8r-10v: Letter of Nicolas Wotton to Queen Mary I, Soissons, 13 Jun 1554. Almost wholly in cipher."
- So the letter was read at the time. The date is 13 June 1554, Soissons (not 8 June).
- ff. 5-7 are not on DECODE: only ff. 1-4 (R8498, Pickering 1553, glossed), 8-10 (R8499) and 263 (R8010) are imaged.
- The BL record has no digitised images.
- Getting ff. 5r-7v needs a BL imaging order or a reading-room visit. With that copy the remaining quarter can be
  checked and completed.
- Other sources checked with nothing found:
  - Tytler vol. 2 (letter not printed)
  - CSP Scotland i (Brunstane not in France in 1554)
  - DECODE (no other copy of the R354 key; `sibling_keys.md`, `print_check.md`)

## Remaining gaps

- Unread and tentative stretches, about 25% of non-null signs (names p2.25 and p6.27, the code Ie, runs p1.13-15, 1.18, 1.24) - blocker: needs-physical-access; the contemporary decipherment Harley MS 1582 ff. 5r-7v is not digitised by the BL or DECODE and needs a BL imaging order
- Rare code signs, about 40 (.I, .p, .d, .M, N., R., C_CEDILLA, Q_TAIL, TALL_F_LOOP, CIRC_BIG) - blocker: no-key-material; no entry on R354, the only surviving copy of the key, and no other copy on DECODE

## Escalation

- [x] siblings: DECODE key R354 found (same year, same embassy); R8010 is not a duplicate (f. 263, a later French memorandum on Navarre); R8498 (ff. 1-4, Pickering 1553) checked
- [x] clear-pages: clear connectives transcribed; the decipherment is a separate copy, ff. 5r-7v, not digitised (needs BL order)
- [x] known-keys: R354 applied (nulls, codes, alphabet)
- [x] print: CSP Foreign Mary June/July 1554 (not calendared), Tytler ii, CSP Scotland i, Harleian catalogue 1808; Tomokiyo has only the 1548 Wotton cipher
- [x] key-rebuild: unified key v6 from all pages; full nomenclator transcribed; constrained re-annealing tried
- [x] retry: every line re-read at full resolution; every unread/tentative stretch retried with key v6 and the full nomenclator (v7)
