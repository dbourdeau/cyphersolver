# Pre-registration: Tomokiyo's key on the untested cipher lines of ff. 406 and 410

Written 11 Nov 2026, before any leaf of fr. 16093 or any page of Brienne 13 was opened in this session, and before
the Brienne copies were read past the clear opening of the 8 Feb letter (the first lines of `wainut/f406_brienne_copy.txt`).

## Question
Does Tomokiyo's key for Maisse's Cipher 2, applied unchanged, give the text of the contemporary clear copies on the
cipher lines that WAINUT did not transcribe (all of f. 406's block after l. 17, all of f. 410's after l. 11)?

## Frozen before the test
- Key: `key/tomokiyo_maisse2.tsv`, read from Tomokiyo's image (sha256 `438f6c6f…`). Not changed after this point.
  A sign seen on the leaves that is not in the key is transcribed under a new name and decodes as `?`. If the leaf
  shows a sign whose identity with a key sign is doubtful, the transcription names it as seen and notes the doubt; the
  decision is made on shape before the copy is read.
- Cipher transcription: `transcription/f406_cipher.tsv` and `transcription/f410_cipher.tsv`, one row per line of
  the leaf, signs separated by spaces. Made from the leaves (Gallica btv1b90074656, canvases 457, 458, 461; openapi.bnf.fr
  IIIF) without reading the copies' cipher part. WAINUT's lines (f406 ll. 16-17, f410 ll. 10-11) are transcribed again
  as well, but are not part of the test. Hashed into `results/frozen_inputs.sha256` before the copy text is opened.
- Copy text: the Brienne 13 copy of each letter from the cipher's first words ("Le surplus de voz lettres", f. 406;
  "L'experience a faict", f. 410) to the end of the letter before the date and signature. Taken from WAINUT's
  `f406_brienne_copy.txt` / `f410_brienne_copy.txt`, completed by a new transcription of fol. 173r and fol. 194v
  (`transcription/brienne_173r.txt`, `brienne_194v.txt`). Hashed before the run.

## Test lines
Every transcribed cipher line of f. 406 from l. 18 on and of f. 410 from l. 12 on that is in cipher, i.e. not WAINUT's
lines. Lines in clear on the leaves are excluded.

**Amendment, 11 Nov 2026, made after a low-resolution look at the leaves and before any sign was transcribed.** The
cipher is much longer than NOTES says. f. 406's block fills the rest of the recto (to about l. 37) and nearly all of
the verso (canvas 458, about 37 lines, then the clear closing "Je prie Dieu ... 1593"). f. 410's block runs from
l. 10 of the recto to the foot of the page, over all of f. 410v and f. 411r (canvas 462), and three lines of f. 411v
(canvas 463) before the clear closing. That is roughly 160 lines in all. This round transcribes a fixed sample:
(a) f. 406r, every cipher line after WAINUT's l. 17, and the short cipher run inside the clear text higher up;
(b) f. 406v, ll. 1-20;
(c) f. 410r, every cipher line after WAINUT's l. 11.
The test is run on (a)-(c) only. The rest is left for a later round and is not scored here.
The cipher transcription is done by three readers (one per sample part) who do not see the Brienne copies, the
WAINUT decryption/reading/translation files, or `decode_check.py` (which carries copy text). They see the frozen key,
WAINUT's `cipher_lines.txt` (sign names only) and the leaves.

## Scoring
Text normalised to a-z, with i/j, u/v merged and y kept. For each letter, the decrypted test lines are joined in order (d)
and aligned to the copy text (T) with Python `difflib.SequenceMatcher(None, d, T, autojunk=False)`.
Score = matched characters / len(d), for both letters together. Signs that decode as `?` count as unmatched.

Scoring note, added with the amendment and before any transcription came back: the short cipher run inside the clear
text of f. 406r stands before "Le surplus", outside T, so it is not in the score; it is decrypted and reported apart.
Rows that re-transcribe WAINUT's lines are not in the score either. A token with `?` appended is scored at its reading;
`a|b` is scored as `a`; `[?]` and any sign name not in the key decode as `?`. The null decodes as nothing.
Implementation: `scripts/test_key.py`, written before the transcriptions came back.

## Control
200 keys made by shuffling the values of the key among its signs (seed 1593; word values shuffle with letter values),
scored the same way.

## Pass
Score ≥ 0.85 and score minus the best shuffled score ≥ 0.30. One run. Whatever the result, it is reported.

## After the test (not part of it)
Read the letters through, fix where each cipher block ends, list cipher/copy variants and holes, and record any key
sign that the leaves show to be wrong or missing.
