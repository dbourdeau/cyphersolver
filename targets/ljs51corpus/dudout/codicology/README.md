# Penn LJS 51: quire joins, catchwords and quire signatures (codicology check)

Brice Dudout, with an AI agent (Claude Opus 5.5), 28 Nov 2026. Images: University of Pennsylvania, LJS 51, OPenn
(Penn IIIF JPEG, 2343 px; public domain). No TIFF masters, no physical examination.

## Prior work (Daniel Bourdeau)

`targets/ljs51corpus/identity_readings.md` §10 (commit 9bdbf7b019), `NOTES.md` and `keys_eye/REPORT.md`
(commits d2548784c7, 44d521b44a): quire 3 (ff. 13-20) belongs between f. 46 and f. 47 (46v→13r, one key split in
ا|لاثام; 20v→47r, the riddle cipher 20r.8+47r.1); f. 21r l.1-5 ends the 48r.8 cipher, so 21r followed 48v and quire 4
(ff. 21-28) "probably also stood after f. 48"; the joins 12v→? and 28v→49r are "still to check"; العاشر on 46r and
Penn's q6-q7 collation do not fit. This check takes those joins as the starting point and does not redo the key
work behind them.

## What was done

24 joins were listed and the criteria fixed before the images were fetched (local freeze, no measurement, so no
#1023 post): the 12 quire boundaries of the present binding (Penn collation 1² 2¹⁰ 3-4⁸ 5¹⁰ 6⁴ 7⁶ 8-12¹⁰ 13⁸),
the 6 joins of the Bourdeau model, and 6 joins inside quires as controls. For each, the catchword (lower left of the
verso), the end of the verso, the start of the recto and the alphabet of any cipher running across were recorded.
Two readings: one with context, one by a blind reader on anonymised crops in shuffled order (no folios, no
hypothesis). They agree on 21 of 24; the three differences are the joins where the first reading used evidence
from outside the pair (Bourdeau's keys, or J04). Details: `joins.tsv`, `signatures.tsv`.

## Results

1. **28v→29r is continuous (certain).** The catchword اذا at the foot of 28v is the first word of 29r, and 28v l.13
   «والبيتان المترجمان هما» after a poem in -ra is answered by the two -ra verses on 29r l.1-2. So **28v→49r is
   ruled out** (49r opens with cipher): quire 4 is followed by f. 29, not by f. 49.
2. **Quire signatures in one hand** (top outer corner of the recto, oblique, with small alif strokes): 46r العاشرة,
   48r الحادي عـ[شر] (trimmed, probable), 49r الثالثة, 69r الخامس(ة), 89r السابع(ة); 59r and 79r trimmed. Only
   العاشر on 46r was noted before.
   - 49-98 are regular quinions numbered 3 to 7, in their original order. Their boundaries J07-J12 read on, except
     48v→49r.
   - If 46r and 48r open quires 10 and 11, quire 10 is a quinion 46 + 13-20 + 47. Bifolium 46/47 is the outside,
     and Penn's q3 is the four bifolia inside. This gives Bourdeau's 46v→13r, 20v→47r and 47v→48r with no loss. It
     also removes his q7 objection: 46/47 is the outer sheet of another quire, not part of a six-leaf q7. Quire 11
     opens at 48r and goes on at 21r (48v→21r).
   - Quires 10-11 then stood after quire 9, that is after at least part of ff. 49-106, not between 46 and 49.
3. **A cycle shows that the stretch ff. 29-45 is not intact.** Taken together, the joins read 29…45 → 46 → 13-20
   → 47 → 48 → 21-28 → 29. Two breaks fall inside Penn's q5:
   - **30v→31r**: the catchword of 30v is a sign of the cipher 30v.7, but 31r opens a new item in Arabic. So the
     cipher ran on to a page that is now lost or displaced. This would explain why 30v.7 has no end and no solution
     anywhere in the volume (Bourdeau: 1,034-passage search, nothing).
   - **36v→37r**: the catchword سر does not match 37r l.1, a cipher with red glosses.
4. **12v→?** is still open. 12v is not continued by 13r, 29r or 21r (different alphabets, or the page is already
   taken), so a loss after 12v is likely.
5. Penn's note "Catchwords on each page, lower left verso" does not hold for 12v, 13v, 20v, 46v, 47v or 48v as the
   leaves are now. Catchwords are words (28v, 58v, 88v), a cipher sign (30v, 68v) or a word divider (20v).

## Limits

Points 2 and 3 rest on images only; sewing, stubs and conjugate leaves need the volume. The reading of the 48r
signature is trimmed. Questions for Penn: is 46/47 one bifolium? Is 48 conjugate with a leaf of ff. 21-29? Which
leaves of ff. 29-38 are singletons? No new cipher reading is claimed here.
