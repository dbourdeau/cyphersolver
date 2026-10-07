# Dinteville (Langres) to the Duke of Nevers, 4 July 1592 (BnF Français 3621 no. 116, f. 130; DECODE R9451)

Status: read. Key recovered from adjacent plaintext (the interlinear decipherment of f. 128) by an outside contributor,
Alex Zarco (GitHub alejandrozarco, PR #24, 6 Oct 2026), completing a partial key published by NoAutopilot
(github.com/noautopilot/cipher-lab, `ciphers/fr3621-dinteville-1592/`). Verified and written up here 7 Oct 2026.
Catalogue item 183. First session 2026-09-21 (attempted, not read; kept below).

## Result (PR #24, verified 7 Oct 2026)

- f. 130: 514 of 522 cipher tokens read as sense (98.5%), measured by `scripts/measure.py` against `reading_f130.tsv`;
  0 emended, 8 open. f. 128 (no. 114, 1 July 1592) reads in full with the same key. Full account in `SOLUTION.md`.
- System: homophonic substitution of letters, digits and signs with diacritic variants (∇ a / ∇ with stroke t;
  Δ with tail a / Δ f; ð with cross s / ð with ascender p; ψ o / ψ+ null) and nulls (‖, ψ+, #|, aP). `#` = c or d,
  `1` = e or i by context. No nomenclator seen. Key in `key.tsv`; the subset fixed on f. 128 alone in `key_f128.tsv`.
- Why 21 Sept failed: the crosses and strokes were taken as the decipherer's marks and merged into the base signs, and
  the gloss was read "Geneve"/"d'ascendre"; it is "Gennes" and the cipher spells "dessendre". `scripts/bourdeau_test.py`
  re-runs the old `align.py` test: unique key once the marks are kept and the gloss corrected, 0 keys otherwise.
- Date: the leaf is dated "iiij^e Juillet" (4 July), as the 1882 print gives it; "3 July" (DECODE, catalogue) is a misreading.

### Checks made here (7 Oct 2026)

- Fix: `f128_signs.txt` wrote plain D where the image has the tailed delta (a) in four places (auoir, Besançon,
  quarante, n'ayans), and `key_f128.tsv` had D = a; with the final key (D = f, D+ = a) f. 128 decoded f for a four
  times. Both files now use D+; f. 128 decodes cleanly with `key.tsv`, and the f. 128-only key scores −2.11, 71% on f. 130
  (was −2.19, 68%). SOLUTION.md keeps the contributor's original figures.

- Re-ran every script: measure 514/522 (98.5%); verify real key −2.00 log-p/letter, 74% in words; f. 128-only key −2.19,
  68%; 30 shuffled keys best −4.54; re-run with 200 shuffled keys: best −4.29, median −5.37, best in-word 38%.
  blind_score 219/225 (97.3%); bourdeau_test 1 key only for the corrected gloss with diacritics kept.
- Images (Gallica btv1b52524472n, IIIF native): f. 128r view 265 gloss reads "auoir veu dassender a gennes"; the cipher
  under it begins ‖ Δ α ψ ꝑ ϖ mʒ o α # 1· □ … as transcribed. f. 130r view 269: L05 (#| ꝑ aP o # 1 2 o α c 1 □ o mʒ …
  "je demeure seu-"), L06 opening (aP o ∇ʹ #| ϖ 1 mʒ "et retou-") and L14 opening (4 ∇ mʒ ⊥ 4 + 1· 4 o ϖ ψ ⊥ "la ville le roi")
  agree with `f130_signs.txt` sign for sign.
- Print: Revue de Champagne et de Brie t. XII (1889 reprint on archive.org, `revuedechampagne12pariuoft`), p. 340:
  "m'a dit avoir vu descendre à Gène 2 millions d'or d'Espaigne. Il en a laissé à Besançon 45 mulets chargés qui
  doivent partir dans trois jours et prendre le chemin de Vesoul, n'ayant que cent chevaux d'escorte" (letter of
  1 July 1592, footnote "Lettre en chiffres"). Agrees with the decode of f. 128. The 4 July letter (f. 130) is only
  summarised there from its clear text (footnote "En chiffres"); its cipher passages are not printed, so the f. 130
  reading is new.

## Remaining gaps
- l. 4, four signs after "l'emporter" (decode "? i u s", perhaps "ou s'il"/"puis") - blocker: illegible; first sign unclear on the image
- l. 7, one sign in "qu'[?]elle y est" - blocker: illegible; sign unclear
- l. 14, last sign of "pass[e]" and the sign after "que" - blocker: illegible; key value does not fit, sign shape doubtful

## Escalation
- [x] siblings: f. 128 (no. 114) is the key source; ff. 127-131 viewed
- [x] clear-pages: f. 130 postscript and verso are clear, not a decipherment
- [x] known-keys: Tomokiyo's Nevers catalogue has no Dinteville key; NoAutopilot's partial key compared, agrees
- [x] print: Revue de Champagne XII (1882) pp. 340-341 prints f. 128 and summarises f. 130's clear text only
- [x] key-rebuild: key rebuilt from the f. 128 gloss (PR #24); f. 130-only signs valued from context
- [x] retry: open signs re-read against the key by the contributor and here; still unclear

## First session, 21 Sept 2026 (superseded)

## What the leaf is

- DECODE R9451 has one image (`IMG_R9451_I44642_P.png`, 2020 × 2881), fetched with the project cookie. The volume is
  also on **Gallica, `btv1b52524472n`**, full resolution, where the canvas is 2 × folio + 9 (from `targets/lorraine1592/NOTES.md`):
  f. 130r = **view 269**, f. 128r = view 265. So fr. 3621 *is* digitised. The blancmesnil note of 16 Sept says
  otherwise; that note is wrong.
- f. 130r is a clear French letter signed by Dinteville, dated "de Langres le iij^e Juillet 1592". It has **two cipher
  passages set inline in the clear text**: about 3 lines near the top (lines 4-7, after "du reste de Strasbourg"), and
  about 7 full lines in the middle (lines 11-17, after "Comme Leur Roy …"). Roughly 400-450 signs in all. The signs are
  letters, digits and marks: `# 4 1 0 o v w m ψ α Δ □ ¢ ∇ π ƒ z +`, some with a bar or dot, and dots after some signs.
- **There is no decipherment on f. 130.** DECODE's "with cipher and decryption" does not hold for this leaf. The
  paragraph after the date, "Monseigneur ce matin j'ay sceu … l'armee lorraine …", is an autograph postscript in
  clear French in a poor hand. It is not cipher and not a decipherment. f. 130v (view 270) carries only the address.

## The sibling that has a decipherment

- **f. 128r (view 265)** is another Dinteville letter to Nevers, "[?] Juillet 1592", in the **same sign set**, with a
  contemporary decipherment written **above** each cipher line: "… m'a dict / avoir veu d'as[ce]nder a Geneve deux
  millions d'or d'Espaigne / … quarante cinq + mulets chargez qui doibt aussi passer dans trois / jours et prendre le
  chemin de Besançon qu'un chemin de Fl[andres] …". This is probably no. 114, which the lorraine1592 notes list as
  "avec chiffre et déchiffrement". About 150 signs, three and a half lines.
- The alignment test (`align.py`) takes the 50 signs I transcribed of the second cipher line and the interlinear
  "avoir veu descendre a Geneve deux millions d'or d'Espaigne" (48 letters). It looks for a one-sign-one-letter mapping,
  homophones allowed, with up to three sign types as nulls. **No consistent mapping exists.** "auoir" sits cleanly over
  `II Δ α ψ p`, but then the same `α` has to be `d` in "d'ascendre". The decipherer also writes `+` and `|` for signs
  they left unexpanded (after "cinq"), which points to nomenclator codes for words (cens, Geneve, Espaigne). So the
  system is a letter cipher with code signs, possibly polyphonic, and my eye transcription of the glyphs is not
  reliable enough to separate these readings from ~150 aligned signs.

## Why it stops

A key would have to be rebuilt from the short f. 128 crib and then pushed onto 400+ unglossed signs of f. 130,
and that rests on a glyph transcription I could not make consistent even on the crib. It is solvable in principle,
by a careful hand transcription of f. 128 and f. 130 (and any other Dinteville letters of 1590-92 in fr. 3621 /
fr. 4716 no. 31) followed by the nomenclator-plus-LM method of pelissier1592 and lorraine1592. It was not done this
session.

What would move it: a verified sign-by-sign transcription of f. 128's three cipher lines against the interlinear,
then of f. 130. Next leaf to check for more crib: the rest of fr. 3621 for other Dinteville letters (nos. 100-120).

Checked: DECODE image of f. 130; Gallica views 263-272 (ff. 127-131); the f. 130 postscript (clear); the f. 128
interlinear; Tomokiyo's Nevers catalogue (no Dinteville key). Not checked: the other Dinteville letters in fr. 3621,
fr. 4716 no. 31 (1590). The images stay git-ignored (BnF; DECODE says publication needs the library's permission).
The site crops are from Gallica, where BnF images are free for non-commercial use.
