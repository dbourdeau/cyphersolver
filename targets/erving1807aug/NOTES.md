# Erving to Madison, Madrid, 10 Aug 1807, No. 24 "Duplicate": the code decoded with a rebuilt Pinckney key

Status: read (complete by the read bar: 1,125 of 1,145 groups, 98.3%, give sense without conjectures); key recovered in
part (414 rows), based on plaintext from an external source (Founders Online). Outside contribution by Feyseel Nur
(PR #21, 4 Oct 2026), with Claude Opus 5.5 subagents for the transcription, key rebuild and decode; adversarial review by
OpenAI Codex in `codex_review/` (verdict: confirmed but overstated). Write-up: `docs/erving1807aug.html`.

Sibling: `../erving1807/` (Erving's No. 21 of 24 March 1807 in the same code, read from Madison's decode; its NOTES
listed this letter under "Not done").

## Sources

- **The duplicate**, NARA RG 59, Despatches from US Ministers to Spain, vol. 10 (24 Aug 1805 - 19 Apr 1808) = microfilm
  **M31 reel 12, frames 0362-0367** (catalog NAID 188605361, catalog.archives.gov). Headed "In Mr Pinkneys Cypher, the
  Cypher of ye Legation", "No 24", "Duplicate", "Madrid Augt. 10th 1807"; postscript of the 11th on 0367. Code groups in
  ink, dotted, inside clear text; **no decode on this copy**. 0365 right and 0366 are clear text. The left edge of the
  third page (0363 right) and the right edge of the fourth (0364 left) are partly in the binding.
- **Founders Online, early access 99-01-02-1993** (`fo_99-01-02-1993.txt`, the page as saved): the letter decoded, as
  plain English, with **ten blank gaps** and some supplied words in angle brackets; source line "DNA: RG 59--DD-Diplomatic
  Despatches, Spain". It does not print the groups or say how they were decoded.
- **Pinckney to Madison, Madrid, 22 Feb 1803**, M31 reel 7 frame 0348 (vol. 6, NAID 188604008), with Jacob Wagner's
  interlinear decode: the independent check (`wagner_pairs.txt`).
- **Erving's 24 March 1807 letter** (`../erving1807/erving_groups.txt`, Madison's decode): further pairs, used by the review.

## Founders' text and this copy

- Header: Founders "In the ⟨Cypher⟩ of the Legation. No. 24 Duplicate"; the film "In Mr Pinkneys Cypher, the Cypher of ye
  Legation" (a blot on "Legation").
- Clear text: both have "my unofficial letter of March 4th" (the image reads "March 4"; the letter meant is No. 21 of
  24 March). `reading.txt` prints "March 24th": that is an emendation, not what the film shows. Founders prints "you will
  not probably annex", the film "you probably will not annex".
- Several Founders brackets fall where this copy loses digits in the binding: ⟨ ⟩ has been informed ({15}78), deceive
  him ⟨ ⟩ ({1}343), ⟨Prince⟩ ({1}661), ⟨a⟩gents ({..}79). Others do not (176.979.1593, 1544.251, 1154.691.111 are
  whole). Whether the editors decoded this duplicate or used another copy is **not settled**; nothing depends on it.

## Method

1. Transcription of the code passages from frames 0362-0367 (`transcription.txt`; frame/line, groups in [ ], ^ caret,
   {..} digits lost in the binding, struck groups noted). The acceptance passage is entered twice (0362.3b and 0363L.1);
   it counts once.
2. Alignment of every group with the Founders text at that place (`aligned.txt`, 1,145 groups in 68 runs; X = no value,
   ? = conjecture, # = digits partly hidden, (sic) = Erving's slip read as intended).
3. Key (`key_pinckney.tsv`, 414 rows: the 395 numbers of this letter and 19 from Wagner's page), each value with its
   attestations. The code is partly alphabetical: 742-745 at/ate/ated/ation, 870-880 their/them/then/.../there/
   therefore/these/they/thin/thing, 884 this, 887 tho', 1340/1341/1343 an/ance/and; higher numbers break the order. A
   caret or triangle over a group marks a plural.
4. Erving's slips: 66 (ing) for "in" three times; 665 for 605 in "change"; 870 their for they; Hanover as 724.549.943
   twice and 724.549.934 once, while 943 is "ly" in un-friend-ly (the March letter has 724.529.934). 310 is "ceiv" in
   deceived and "liev" in believed.
5. Check against Wagner 1803 (`wagner_pairs.txt`): 47 group numbers shared; **45 compatible**; 584 indeterminate (na in
   the key, nation in the alignment, Wagner "nations?"); 943 has no Wagner value (friend-943-ship). Not 46/47, as first
   claimed.
6. `build_reveal.py` writes `groups.txt` (for measuring) and `docs/reveal/erving1807aug.json` (the counter-project
   passage, 67 groups, values checked against the key).

## Measure

- `aligned.txt`: 1,145 groups; 9 without a value (X), 11 marked conjectures. **1,136 have a value (99.2%); 1,125 give
  sense without the conjectures (98.3%)**: the headline, as fraction_coherent.
- The transcription has **1,147 positions** once the repeated passage is counted once: two uncertain positions have no
  aligned group (see Remaining gaps). Over 1,147: 1,125 = 98.1%.
- Codex's **conservative sensitivity count**: excluding the conjectures, the 37 hidden-digit groups and nine contextual
  emendations, 1,081 of 1,147 = **94.25%**. A declared sensitivity count, not a measured error rate.
- Outside support (Codex, strict match against Wagner and the March pairs): **716 tokens (62.5%), 141 group types**;
  same-value recurrence or outside support: **908/1,145 (79.3%)** (not 80.5% as first claimed). About a fifth of the
  groups rest on the Founders text alone.
- Image check: 53 groups re-read on the images (purposive, legible runs and the three Hanover spellings), **0 digit
  mismatches**; not a population error rate.

## The Founders gaps (Codex grades, `codex_review/gaps.md`)

| Founders | Groups | Code | Grade |
|---|---|---|---|
| ⟨ ⟩ has been informed | {15}78.1010.284 | THAT GOVERNMENT | solid (1578 prefix hidden) |
| flattered with ⟨ ⟩ of personal | 176.979.1593^ | EXPECTATIONS | plausible |
| given for ⟨ ⟩ | 408.633.69.191.728^ | for-GIVEN for HIS [633] INTRIGUES | speculative (633 open; "past" a guess) |
| deceive him ⟨ ⟩ | {1}343 | AND | solid |
| not destitute of ⟨ ⟩ | 632.849.1147.455.1482 | ?-r-i-?-? | open ("pride" a guess) |
| France ⟨ ⟩ to England | 1544.251 | HOSTILE | solid (same pair in "in fact hostile") |
| as a dernier ⟨ ⟩ | 1154.691.111 | RESORT | solid |
| his troops ⟨ ⟩ has no | 244.724.549.934.1343 | TO HANOVER AND | solid |
| expectation of ⟨ ⟩ seeing | 133 | nothing missing | no coded word in the gap |
| tranquillize ⟨ ⟩ the alarm ⟨or⟩ | 877.1497.13? / 244.1387.982.1497 | THESE AL[ARMS], TO CONCEAL | solid for THESE; the arms numeral is hidden |

Six solid additions. Confirmed supplied words: ⟨must⟩ 1250.1203, ⟨see⟩ 1181.1298 (with NOW 429), ⟨character⟩ 603,
⟨Prince⟩ 1661; "to ⟨be⟩ employed" = SO 1219; "here ⟨are⟩" = IS 1484. Three disagreements: "very best informed ⟨persons⟩"
= VERY [368] AU-THO-RI-TY (748.887.137.1362; 368 best? conflicts with 368 ni in Catalonia); "the vast costs brought
about by the war" = the vast [767.679.378] SPAIN BY THE WAR; "the character of that with which his" = CHARACTER OF THAT
WHICH HIS (no "with").

## What it says

Godoy (the Prince of Peace) paid for the Hanover bargain "OUT OF HIS OWN FUNDS"; with the peace Hanover goes to
Westphalia, and he "believes that he has been DECEIVED AND is FURIOUS". A KINGDOM OF EBRO (Catalonia, Navarre, Biscay)
is projected, and the invasion of Portugal "IS NOW seriously RENEWED with a view to ACTUAL CONQUEST". Godoy's
counter-project: a separate peace with England through Russian mediation, and "as a DERNIER RESORT HE WILL MAKE AN
ALLIANCE of some sort WITH ENGLAND!" A portrait of the French ambassador Beauharnais. Postscript of the 11th: Spain to
send an army into Portugal, French troops to replace it; the Emperor has written to the King about the Prince of
Asturias; Godoy sees no course "BUT IMPLICITLY TO SUBMIT".

## Remaining gaps
- code group 633 ("his [?] intrigues", over a struck group) - blocker: open-codes; occurs once, no sibling value
- code groups 632, 455, 1482 ("destitute of ?-r-i-?-?") - blocker: open-codes; each occurs once; "pride" fits but is not decoded
- code groups 767, 679, 378 ("the vast [?] Spain by the war"; Founders "costs brought about") - blocker: open-codes; each occurs once
- one group ending in 4, frame 0364 right page, left edge ("affecting candor, [?] perfectly false") - blocker: illegible; digits lost in the binding
- 916 after "the Prince of [x47]" in the postscript - blocker: open-codes; 916 is "as" elsewhere, no sense here
- position after 1114.244 ("advised him to"), frame 0367 left, at the hole in the leaf - blocker: illegible; the sense needs no word
- first position of the last line, frame 0367 right ("submit [?] all"), under the facing leaf - blocker: illegible; probably 244 "to"

## Uncertain readings (grades as in README Conventions)

- M: 368 best; 586/1424 narrow/low (split assumed); 66 West; 169.80.115 d'af-fai-res; x47 Asturias; 1543 t in except;
  310 ceiv/liev; the emendations of 943 (x2), 66 (x3), 665, 870.
- I: 176.979.1593 expectations (fitted in a Founders gap); 878.1394 they are (alphabetical slot after 877 these;
  Founders "whatever these are"); the 37 groups with hidden digits, restored from context.
- C: the rest, from the Founders text (716 of them also supported by Wagner or the March pairs).

## Escalation
- [x] siblings: Erving's No. 21 of 24 Mar 1807 (`../erving1807/`) and Pinckney's 22 Feb 1803 despatch with Wagner's decode (reel 7 frame 0348) used; reel 8 frames 0083-0084 (Jan 1804) not decoded here
- [x] clear-pages: frames 0365 right and 0366 are the letter's own clear text, not a decipherment; the duplicate has no decode
- [x] known-keys: the header names Pinckney's cypher; Wagner's 1803 decode and the March pairs are the decoded texts in it that were tried
- [x] print: Founders Online early access 99-01-02-1993 is the only printed or online text found; it supplied the plaintext
- [x] key-rebuild: key rebuilt by alignment with the Founders text, extended by recurrence and the alphabetical runs (414 rows)
- [x] retry: every open group re-tried against the key, Wagner and the March pairs, and graded by the Codex review; the open ones occur once

## Files

| File | Contents |
|---|---|
| `transcription.txt` | groups as read from frames 0362-0367, with the clear words |
| `aligned.txt` | group = value, in order, 1,145 groups |
| `groups.txt` | the same groups only, one run per line (for `--measure --drop-first`) |
| `key_pinckney.tsv` | the rebuilt key, 414 rows with attestations |
| `wagner_pairs.txt` | the 1803 check pairs from frame 0348 |
| `reading.txt` | the decoded letter and the Founders gap table (contributor's; "March 24th" there is an emendation of the film's "March 4") |
| `fo_99-01-02-1993.txt` | the Founders Online page as saved |
| `build_reveal.py` | writes `groups.txt` and `docs/reveal/erving1807aug.json` |
| `codex_review/` | OpenAI Codex's adversarial review: `review.md` (verdict), `gaps.md`, `audit_notes.md`, `metrics.json`, token and Wagner audits, the scripts. Only paths were changed on copying: the scripts and `metrics.json` point at this folder and at `../erving1807/erving_groups.txt`, and `fo_1993.txt` is `fo_99-01-02-1993.txt` here. `image_sample.py` needs the line crops, which are not committed (their hashes are in `image_metrics.json`). |

DECODE: the letter is a NARA microfilm item, not a DECODE record, so there is no `decode_updates` entry.

No portrait of Erving was found on Wikimedia Commons (no Wikidata image; Commons searches return namesakes; Curry's
*Diplomatic Services of George William Erving*, 1890, has none), so the page shows Madison only.
