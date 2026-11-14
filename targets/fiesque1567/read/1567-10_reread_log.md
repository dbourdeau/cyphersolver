# Re-reading log, 1567-10 (views 6 right - 8 right), 22 Oct 2026, Claude Opus 5.5, batch b02

## Starting point
Profile: "decoded, not read" (mechanical decodes decoded_v007l..v008r, unspaced; 0 of 11 sentences clean by
docs/_check_reading.py on decoded_v007l.txt).

## Existing text?
- No contemporary decipherment on views 6-8 (looked at view 6 at 1200 px and the contact sheets of views 7, 8: no
  margin or interlinear writing beside the cipher). Not in La Ferrière (contributor's prior check). None found.

## Image checks
- View 6 (full, 1200 px; header crop 2200 px): **the letter begins on view 6 right**, dated in the docket hand
  "11 octob. 1567, Vienne" (the contributor had "Oct 1567?"). Four lines of clear text ("Madame, ma derniere lettre a
  esté du [xxv?] du moys passé ... sur ses pieds") and then about 22 lines of cipher that are **not in the contributed
  transcription** (no v006r file). The contributed v007l starts in mid-sentence. Not transcribed here (about 800 signs;
  workable from the image, not attempted in this pass).

## How the reading was built
Line by line from the decode, using a sign-by-sign listing (research/reading_audit/reread_b02_signs.py) at breaks.
Confusions read through (all already flagged by the contributor or visible in the decode):
- `fu` (barred f / ꝑ, key u) stands for **l** in several words: "fu a desunyon" = la desunion (v007r c24), "fu //"
  = la, "fu // vd c 11 H# // b o fu" = l'ambassadeu[r] (v007r c18); elsewhere u. Probably two signs merged under one
  label; not corrected in the transcription.
- `fx` (t-shape, key c) is o in many words (n fx m 3n H# 1 v vbar -| o = cognoistre, v008l c01; "ection" in affection).
- `H#` = ss in "ambassadeur" (v007r c18, v008l c04, c07), = o elsewhere.
- `=20` (pour) appears inside words where it cannot be "pour": "remer[20]cicict" (remercioit), "sama[20]estc" (Sa
  Majesté), "ma[20]dict" (m'a dict). Probably a different sign read as 20; the words read without it.
- "ibre" twice = estre (v008l c03 "bien ibre" = bien estre; c20 "ibre esueu" = estre esleu?).
- `c` (key b) = r in "ciens" (riens, v008l c25).

## Holes left
v007l c01 (start, needs view 6 right); "[?faict]", "[?loue fort]" (c04 uoueyort), "[?conseiller]"; v007r c15 "soitctcri";
v007r c22 "deme"; v008l c19 "des filles de m[...]" (dem: possibly a code for the Emperor, not in the key); v008l c21
"uaneganasncrrte"; c22 "gechaocictua"; c24 "mnese?tcnte".

## Result
_check_reading.py on the reading: clean share 0.72 (42/58; hole rate 0.089) against 0.00 for the decode. Sentences
hold on views 7-8; the letter's first cipher page (view 6 right) is unread because it is untranscribed.

## Round 2, 23 Oct 2026 (Claude Opus 5.5)
- View 6 right transcribed and read: read/r2/transcription_v006r.txt (816 signs), log read/r2/v006r_reread_log.md. The
  reading now starts at the first cipher word ("Je luy dicts que, quant je prins congé de vous ...").
- v007l c01 hole closed on the image: "et aveugles a leur interest, ont [?faict] cognoistre".
- Dz = con (four words on view 6 right). Look-alike alternates on view 6 right 3.3% (31/940 letters).
- Score, body only: 0.61 plain (0.67 before on the shorter text), 0.92 holes only, 0.70 with target spellings.
- Left: v006r c05-c06 two words; [?] words listed in the v006r log; v007r-v008l holes listed above (not re-checked).

## r2m, 23 Oct 2026 (Claude Opus 5.5): single-word holes of views 7 left - 8 right on native crops
Views 7 and 8 fetched whole at native resolution (openapi.bnf.fr IIIF, 7593 px wide; scratchpad only), each hole's line
cut into strips (two halves) and read sign by sign with the key (Dz = con). Labels found different from the contributed
transcription are listed in `r2/corrections.tsv` (r2m rows).
- Filled from the figures: v007l c10 "entendre" (u = e, a struck "La" before it); c13 "[con]seiller" (Dz); c17 "ordre et
  unyon" (the contributor's "1 a" is "ic" = et; "[?en l'unyon]" withdrawn); c20 "sont [?soubz] les mains de luy": the
  contributed line lacks the first four groups ("T‡ʒʊ v+ꝑ+ʒ Cov ϖ‖ıʒT" = sont, s-o-u-o-z, les, mains); "[?soubz]" rests on
  v+ꝑ+ʒ (s o u ? z) by sense. c23 "Sa Majesté [...] qu'il": the hole is a struck sign; no word is written, the cipher
  omits the verb. v007r c01: no "estoient" in the figures ("T o n + ꝑ ⊣ ꝑ̃" = secouru), now `[estoient]` supplied, and
  the clause ends "a son besoint." (no sign lost; the conditional has no main clause in the cipher). c02 "[con]me"
  (Dz ϖ o). c07-c08 "riens dire jusques a tant qu'on": no sign for "a" before "dire"; "zi" is the code 21 (tant), as
  this hand writes 20 "zo" and 10 "ic"; ⊢ꝑ+ʒ = qu'on. c15 "plaint [?poinct], car": ʒ+1ꝭs+ʊ = p o i [ꝭs] [+] t (two
  look-alikes), n‖⊣ = car. c19 "poussoict" (3p ‡ ꝑ ‡(ss) + 1 fx ʊ; "[?sollicitoict]" withdrawn) and "de" (b o at the line
  end). c20 "laquelle chose" (ꝑ‖ zz 7o: "[?toutesfois] que la" withdrawn). c22 "de me faire ce bien de ne croire"
  (ϖa, 13 = faire, n o, 4 1 a ʒ = bien). c23 "par le monde" (ʒ‖⊣, ꝑo; "[?plus] au" withdrawn). c24 end "luy" (ꝑ ꝑ̃ ʒ),
  "luy remonstrant". v008l c01 "et qu'il pouvoict bien cognoistre que [ϖ] et vous" (aʊ = et; the lone ϖ code). c03
  and c20 "estre", "estre esleu": "ı4" is the code 14 (est). c05 "sans [?vostre] sceu": the figure is the code 16, read
  vostre as in f. 100r c24 and the 1569 letters. c14 "croire" (fx ⊣ + ı ⊣ o). c15 "amitye qu'il est possible" (ʊʒo =
  tye; no sign missing). c19 "des filles de [ϖ]" (b a ϖ). c22 "pourchassoict la seconde pour le roy de Portugal" (zo
  = 20 pour, n L ‖ ‡ = chass). c24 "[ϖ] ne se [con]t[e]nte" (n read e). v008r c01 "Je tache [?fort]" (8 a ʊ ‖ n L a).
- Left: v007l c04 [?fort] (3y read f), c14-c15 [?bon escient] (a H# 1 o 3n, no c), c22 [?accordé] (a ffx H# ⊣, no
  "dé"); v007r c22 nothing; v008l c18 [?Plus] (f C ꝑ v, f for p); c21 "et que […] bagues": the groups ꝑ‖ʒam‖ʒ‖
  ‖ʒf++ıʊo give no word under the key (perhaps "n'a ... apporté"); v008r c01 [?fort].

## Holes counted by words (14 Nov 2026)

Owner decision of 14 Nov 2026: the read share counts holes by words; a mark with a number is that many unread words
(README Conventions). v008l c21 "et que [... 2] bagues": two cipher groups give no word (see above), counted as two unread words. The mark in "que […] bien qu'il" keeps no size: the log does not record what stands there (extent unknown). Read share 0.954 by marks (1,100 words, 53 holes) -> 0.953 by words (54 holes): still read.
