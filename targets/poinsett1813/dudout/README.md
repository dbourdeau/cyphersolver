Status: in progress (Brice Dudout, 3 Nov 2026; 13 new code values from an 1811 interlinear decode; 1813 coverage 161 -> 170 of 437 groups, no sentence reads yet). Next step: scans of Poinsett's 1811 despatches (10 May, 25 and 30 July) and any "decyphered" sheets.

# Poinsett's code: values from an 1811 interlinear decode (HSP)

Contribution by Brice Dudout. Daniel's files in the parent folder are unchanged.

## Source

Historical Society of Pennsylvania, Joel R. Poinsett Papers (Gilpin collection), vol. 1, folder 10: Poinsett to the
Secretary of State, Buenos Aires, 29 June 1811, p. 2. Two lines in code (19 groups) carry the plain text written over the
groups. Read from research photographs taken at the HSP; the photographs are not published here.

    They have informed ^ me that some arms° are on the way from the U States at private contract
    1121 713 1348 210^ 1178 284 973 204 514 531 1355 305 310 1355 98 1215 752 236 1179

## What it gives

- Same code as `key_1814.tsv`: four values are confirmed, 1348 in, 284 that, 1355 the, 1179 ct (in "contract").
- 13 new values (`key_1811_additions.tsv`): 1121 they, 713 have, 210 form, 1178 me, 973 some, 204 arm, 514 are, 531 on,
  305 way, 310 from, 98 United States, 752 private, 236 contra.
- Marks: a caret after a group adds -ed (210^ = "formed" in "informed"); the small circle adds -s (204° = "arms"), as
  already seen in the 1814 decode.
- 1215: the decoder wrote "at" here; `key_1814.tsv` has 1215 = a. Left unchanged; either the clerk wrote "at" for the
  idiom or 1215 is a/at.

## Effect on the 1813 letter

`decode_1813_plus.py` applies `key_1814.tsv` plus the additions to `transcription.tsv` (output `decode_1813_plus.txt`):
170 of 437 groups have a value (0.389), against 161 (0.368) with `key_1814.tsv` alone. Some phrases begin to read,
e.g. "... sed of arm ..." (possessed of arms) and "foot of arm[s] and the ...". No sentence reads yet.

Open point: 708 = posi (a syllable split of "disposition" in 1814) gives "posi have" twice and "posi" six times at the
head of phrases in 1813. Either the split is wrong or 708 has another value there (a pronoun such as "I" would fit
"... have ..."). Not changed.

## Other 1811 material seen in the same volume (for the record)

- Despatches of 29 March, 16 June (original, duplicate, triplicate) and 20 June 1811, and a letter from Monroe to
  Poinsett of April 1811, are in this code (1355, 1397, 1554 frequent; 3 = Great Britain). No decode on them.
- The despatches of 20 March and 11 April 1811 use a different code (no 1355, 1397 or 1554; 790, 798, 1030 and 1399
  frequent). The 11 April letter has a separate sheet "Mr Poinsett's letter of the 11th April 1811 decyphered" (folder
  7), so that second code can be rebuilt from it when the full sheet is available.
