# Robert Reade (Paris) to his cousin, 19 April 1641 (BL Harley MS 7001 ff. 148-149; DECODE R7766)

Catalogue entry 136 "... (Paris) to unknown recipient", 19 Apr 1641 (rule-scored, class C). Worked 22 Sept 2026.
Outcome: read in part.
- 89.8% of the cipher tokens (193 of 215) are read from values on the key.
- 3.7% (8) are read from values rebuilt here (grade C).
- 6.5% (14) are conjectured (grade M, see gaps). Re-measured 30 Sept 2026 (see Corrections).

## What the record is

DECODE R7766 (4 images): a three-page holograph letter in English, mainly clear, with two passages in a numerical
cipher (about 254 groups). It is signed "R. Reade" and dated "Paris 19 Apr 1641". The endorsement reads
"1641: April 19: my Cousin Reade from Paris" and "Given by Mr G. Holmes". The writer is Robert Reade, Secretary Sir
Francis Windebank's nephew and secretary, who followed Windebank into exile in Paris (December 1640). The recipient
is a cousin at the English court, probably Thomas Windebank, the Secretary's son. The clear text covers:
- a false report that Reade had called the Lords (or Commons) fools;
- the trial of "my Lord Lieutenant" (Strafford);
- the King's box of papers and Mr Treasurer's copy;
- the Queen's business;
- Walter Montagu's arrival;
- Sir William St Ravy leaving for England;
- Mr Forster.

## Key

DECODE R9115 (BL Add MS 32256 f. 4 and its continuation page) is headed "Windebank to his Son. Paris. March 1642"
and "Windebank's C[ipher] continued 1640". It is an 18th-century Deciphering Branch reconstruction of the Windebank
family cipher, and it reads this letter.
- The numbers 1-50 are single letters. The odd ones are marked + (nulls), and the even ones are letters
  (2 c, 4 f, 6 n, 8 h, 10 r, 12 t, 14 a, 16 g, 18 p, 20 b, 22 u/v, 24 o, 26 l, 28 e, 32 k, 34 m, 36 i, 40 s, 42 x, 44 d).
- 51-100 are letters and syllables (51 r, 53 c, 54 l, 55 s, 56 a ... 73 and, 74 am, 75 as, 93 again, 97 an, 98 acquaint).
- The symbol letters are: m n, E o, ω m, Ǝ r, ⊔ i, + l, φ s, Δ t, looped sign n, * y, ⊕ a, Φ b, π c, ɔ d, ∪ e,
  ∩ f, δ g, C p, □ q.
- The code runs from 100 to 735 in alphabetical order (128 be, 183 can, 202 do, 276 from, 323 him, 362 King,
  457 Parliament, 524 return, 572 to, 574 the, 578 that, 636 will, 732 England, 735 France).
Values are transcribed in `key.py`. The key images are git-ignored.

## Files
- `ct.txt`: transcription of both cipher passages (254 groups). Several apparent digits proved to be symbol letters:
  8 = φ, 2 = ɔ, D = n-sign.
- `key.py`: the key as read here, plus the conjectures dict `C`.
- `reading.txt`: the reading, with the measurement.

## Reading (summary)

Passage A: in case a proclamation goes out against Windebank ("my [455]"), as against the last [673]:
- they have not enough against him to confiscate his fortune;
- they would be glad (660, a conjecture: willing, glad or ready) to take advantage of his refusal to return upon the summons;
- his person could not be "strong" (safe, secure; 562 on the key) if he returned;
- the only way is for His Majesty to prevent it.

Passage B: Reade is told that Sir William St Ravy "has done Mr Forster no good offices here" and that "they have an
eye over him". This matches the clear text that follows it.

## Remaining gaps
- code groups 90, 160, 319, 359, 444, 452, 455, 487, 539, 650, 660, 673, 718 (x2) - blocker: no-key-material; blank in the only surviving key reconstruction (R9115); the only further source is Reade's other ciphered letters to Thomas Windebank, Paris, Jan-May 1641, calendared in CSP Domestic 1640-41 (TNA SP 16/476 ff., 'some sentences in cipher', printed unread) - needs-physical-access (TNA originals, not on DECODE or free online); each occurs once or twice, conjectured from context and alphabetical slot (6.5% of tokens; 203 done and 729 Court were later found as side notes on the key sheet)

## Escalation
- [x] siblings: R7767 (Harley 7001 f. 202, 1645) is a different Committee of Both Kingdoms cipher; Add MS 32256 key volume (R9113-R9219) searched by correspondent; only R9115 is Windebank's. All 1630-50 keys in the volume opened: R9114 (Laud 1636) is a blank printed grid, R9116 (Charles I to the Queen 1642) a frequency tally, R9117-R9119 are 1644-45 royal keys; none carries Windebank values
- [x] clear-pages: none; the clear text around the passages was used as context
- [x] known-keys: R8694 (Browne, Add MS 72438) tried first and failed; R9115 fits
- [x] print: CSP Domestic 1640-41 (archive.org full text) grepped: Reade's letters to Thomas Windebank calendared with cipher passages left unread, no decipherment; this confirms the recipient. Calendar of the Clarendon State Papers vol. 1 (1872, archive.org full text) grepped: Windebank's papers there stop at his flight (Dec 1640), no Reade letter, no 1641 key; web and Windebank literature searched; letter not printed or calendared (Harleian, not in CSP Domestic)
- [x] key-rebuild: alphabetical bracketing of the code filled the blanks as conjectures (524 return, 562 secure, 573 they, 660 willing ...; 600 take is on the key). Corrected 30 Sept 2026: 562 is "strong" on the key, and 660 has no slot support (see Corrections)
- [x] key-rebuild (LM): en-1640s ranking of bracket-consistent candidates for the 13 blanks (`lmfill.py`) does not discriminate (prefers the shortest word, e.g. come/he/of); no conjecture upgraded
- [x] key-rebuild (constrained search): `beamfill.py` scored every en-1640s corpus word lying alphabetically between each blank's nearest key neighbours in full decoded context. 5 of the 12 open code values have out-of-order neighbours on the key (only>offered, out>our, such>shall, when>England), so the code is not strictly alphabetical and the bracket admits nothing; elsewhere the top candidates are function words or noise (can, he, js, ed). Nothing upgraded; single-occurrence code words cannot be fitted by annealing/EM, which need recurrences
- [x] key-rebuild (seeded anneal): `annealfill.py`, coordinate ascent over the 2000 most frequent corpus words per blank code, seeded with the conjectures, objective = en-1640s LM on both passages: converges to function words (was, he, and, that, a); 0 of the blanks keep a sense reading. The LM rewards frequency, not meaning, on single-occurrence code words; nothing upgraded
- [x] key-margin (5 Oct 2026, push to 95%): the 650 margin entry on R9115 f.1 read at full resolution: '650. w[r]it' with h above (writ/with/wait?), not 'way', and none of these fits the context, so 650 stays M; no side notes for the other 12 open values on either key page. Still 201/215 = 93.5%; 95% needs 4 more of the 14 single-occurrence blanks, blocked on key material (TNA SP 16 Reade letters, physical access)
- [x] retry: all groups re-run with the corrected glyph readings (φ, Δ, ɔ, δ); 191 of 215 read from key values, 11 more from rebuilt values (re-measured 30 Sept 2026: 193 and 8, see Corrections)

## Corrections

- 30 Sept 2026, checked against the key images (git-ignored; main checkout `harley7001/img/`):
  - 562: the continuation page of R9115 (IMG_R9115_I42591_P2, 551-600 column) plainly reads "562. strong". The first
    key transcription had it (`'562':'strong'` in key.py), but a later line of key.py overwrote it with a rebuilt
    "secure", counted as grade C. The key value is restored. The passage reads "I do not find how his person can be
    strong if he shall return", strong in the period sense of safe or secure (H). The letter's group was re-checked
    on the image: it is 562.
  - 660: regraded from C to M. On the first page (IMG_R9115_I42591_P1) the block 651-675 is the printed 751-800 grid
    renumbered by hand. Its only values are 652 you, 662 you, 664 your and 666 yet; 663 is a faint crossed entry,
    not read here. 660 is blank. A w-word such as "willing" would stand near 636 will, and no y-word gives the sense
    of "they would be ___ to take the advantage". So willing (or glad, ready) is a conjecture from context and moves
    to `C` in key.py.
  - 573: the continuation page has a partly legible entry, "573. u. th…". The "u." mark is the one before 559
    "u. safe". The word begins th (probably the), and the rest runs under the double ruled line at the column
    edge. The strokes just beyond the rule are the r line of the alphabet column next to it. The entry fits the
    rebuilt they/the but cannot confirm it, so 573 stays C.
  - Re-measured with key.py: 193 key (89.8%), 8 rebuilt (3.7%), 14 conjectured (6.5%); key and rebuilt together
    93.5% (was 94.0%). The old split, 191/11, counted 573 four times; ct.txt has it three times (they, the, they).
  - Seen in passing, not resolved: the first page's margin list beside 591-600 carries 638-650 (e.g. 639 where,
    648 wise). Its 650 entry is written but hard to read ("w…t" with an h above: with? writ?). key.py lacks it, and
    the reading conjectures 650 "way", so the 650 entry needs a closer look.
