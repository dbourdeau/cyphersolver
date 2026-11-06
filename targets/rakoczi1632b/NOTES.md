# rakoczi1632b: George I Rákóczi's conditions of 1632, fol. 491v-492v (BSB Clm 10401 n. 139), read with WAINUT's key

Status: in progress (write-up pending: the doubtful groups still need a blind re-read on the images, and profile.json has no fraction_read; 6 Nov 2026). Reading as contributed: read in part (Brice Dudout, 6 Nov 2026). 237 cipher words on fol. 491v-492v: 110 certain, 47 probable, 66 restored,
14 unresolved, so 157/237 = 66.2% by Daniel's count (94.1% with the restored words), below the 95% bar. WAINUT's key, completed
with 8 values from the glosses, passed a pre-registered held-out test on the whole of fol. 492v: 0.902 against 0.341 for the
best of 200 shuffled keys (margin 0.561).

**This is a satellite of `targets/rakoczi1632`, WAINUT's target, which is in progress.** The target, the key
(`key_frozen.tsv`, 72 entries), the reading of fol. 491r and the prior-art search (Szilágyi 1873 and 1882) are WAINUT's
(3 Nov 2026). None of WAINUT's files is changed here; this folder only adds fol. 491v-492v, in the way `targets/pawel1624`
builds on `targets/casimir1629`. WAINUT may prefer to fold these files into rakoczi1632; that is his call.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents.

## Document

Munich, Bayerische Staatsbibliothek, Clm 10401 (Collectio Camerariana 51), n. 139, fol. 491v, 492r, 492v (MDZ bsb00117497,
scans 1200-1202; digitised microfilm, Public Domain Mark 1.0, credited "München, Bayerische Staatsbibliothek"). No image and no
crop of an image is included here (WAINUT's target does not include them either). Same cipher as fol. 491r (numbers 1-99, extra
signs, a few 3-digit code groups, embedded in clear Latin), with Camerarius's interlinear glosses over most cipher words, except
the end of 492v (y1502-y1709).

## Key (`key.tsv`)

`key.tsv` = K, the key measured on 492v: WAINUT's `key_frozen.tsv` with its values unchanged, plus 8 values taken by script
(`scripts/build_key.py`) from the glossed pairs of 491v and 492r (`frozen/BUILD-PAIRES.tsv`): new groups 35 i, 55 x, 69 h,
81 l, {O} e, {f} l, and second values 44 t and {s} l. On those pairs key_frozen alone agrees with the glosses on 97.0% of the
letters (365 letters).

`key_reading_additions.tsv` lists values found after the measurement and used for the reading only (79 x, 84 f, 88 m, {w} h,
29 q, 75 v) and the signs seen with several values. They are not tested.

## Validation (`validation.txt`, `frozen/`)

The first test of WAINUT's key beyond his 12 held-out words of 491v. The protocol (`frozen/PREREG.md`, in French, SHA-256
8bb97f93…) was written and hashed before any of 491v-492v was transcribed. H = all the cipher of fol. 492v, transcribed on
strips with the glosses blanked (`frozen/H-CHIFFRE.txt`), then K frozen (`frozen/KEY.tsv`), then the glosses of 492v read
(`frozen/H-GLOSES.txt`), then one measurement (`scripts/measure.py`): 31 glossed words, 205 letters, score 0.902, best of 200
shuffled keys 0.341, margin 0.561; thresholds fixed in advance (>= 0.85 and >= 0.30). key_frozen alone, for description only:
0.878, margin 0.571.

One mask incident: the strip at y565 was a gloss line, not a cipher line, so the line y590 under it was excluded; fragments of
two glosses seen at y278 and y328 led to excluding those words. A rule set before the measure but not foreseen in the protocol:
words begun on the line before, or cut by the fold, are excluded. The frozen files are kept verbatim (French headers) so that
their SHA-256 can be checked (`frozen/SHA256SUMS`).

## Texts

`transcription_f491v.txt` and `transcription_f492r.txt` (cipher with the glosses, `[G: …]`), `frozen/H-CHIFFRE.txt` (492v,
cipher only) and `frozen/H-GLOSES.txt` (492v glosses with their groups). `decryption_f491v.txt`, `decryption_f492r.txt`, `decryption_f492v.txt` give the raw decode with `key.tsv` and
`key_reading_additions.tsv`. `reading.md` gives the Latin, an English summary and the
count. The clear Latin is given only where it frames the cipher words.

Summary: the rest of Rákóczi's conditions for joining the Swedish-Protestant alliance: defence of his estates; 500,000 florins a
year in two instalments, the first year in one sum before he takes the field; 16,000 German foot and 4,000 cuirassiers whose
officers swear to him; help after the peace and, in peacetime, 2,000 musketeers and 2,000 cuirassiers if a secret threat appears;
all members of the Union bound by these four points; troops, cover against the King of Poland and a trusted envoy before he
enters Hungary; payment if he must campaign in winter; mutual coordination.

## Prior work

- Camerarius's interlinear glosses are the decipherment of the time (credited `contemporary`).
- WAINUT, targets/rakoczi1632 (PR #237, 3 Nov 2026): key, fol. 491r, prior-art search (Szilágyi 1873, 1882). No change on that
  target since 4 Nov 2026 (last commit 4e0b8af13; GitHub API, 6 Nov 2026).

## Limits

- One transcription pass by an AI agent on a microfilm; no independent reader, no human palaeographer. reading_review B.
- The count is manual and was not checked independently. 66 words are restored, nearly all at the fold.
- The held-out part is 31 words (205 letters).

## Remaining gaps

- 66 restored words at the gutter fold of the microfilm - blocker: needs-physical-access; a colour scan or the original would settle most of them
- 14 unresolved words on 491v-492v - blocker: illegible; mostly at the fold or in unglossed lines
- doubtful groups (32/82, 50/80, 66/86, 56/66, signs {a} {s} {x} {c}) not re-read blind - blocker: not-attempted; one reader only

Not gaps of this reading (scope): fol. 491r (WAINUT's target); the "Bericht" of scans 1203-1205, a separate text, not a clear.

## Escalation

- [x] siblings: the key of fol. 491r (WAINUT) used and measured on 492v
- [x] clear-pages: Camerarius's glosses and the margin paraphrase of 492v used; no clear copy known
- [x] known-keys: targets/rakoczi1632 key_frozen.tsv
- [x] print: WAINUT's search (Szilágyi 1873, 1882) relied on; nothing new found
- [x] key-rebuild: 8 values added from the glosses of 491v-492r before the test, 6 more after it for the reading only
- [n/a] retry: one measurement, as pre-registered

## Credits

WAINUT (lccompany): target, key, fol. 491r and prior-art search, on which all of this rests. The glosses are Camerarius's.
Brice Dudout: transcription and reading of fol. 491v-492v, held-out test of WAINUT's key on 492v, 8 values added from the glosses.
