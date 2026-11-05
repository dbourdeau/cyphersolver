# leopold1680 worklog

- 2026-11-04 access: BNE Digital viewer for RES/261/58 opened in Chrome (no Cloudflare challenge). Page 5 is the letter; fetched `/bd/es/pdf?id=...&page=5` (454 KB, one embedded image 1654 x 2473 px) into `img/` (git-ignored) and cropped strips.
- 2026-11-04 transcription: 20 lines of number groups, 250 groups, into `transcription.txt`; doubtful readings marked `?` (181?, 75?, 45?, 104?, 120?). Strokes through the groups not transcribed.
- 2026-11-04 statistics: 85 distinct values (86 with the `?` variants), min 10, max 224, IoC 0.0165, top 39 x13, 50 x11, 62 x9, 123 x9. Block structure 10-17 / 30-67 / 72-105 / 108-154, nothing in the 20s. Bigram 62 39 x6, trigram 59 129 104 x2.
- 2026-11-04 prior art: web searches (English, German), vetting pass of the same day (known.py, Tomokiyo habsburg.htm): no decipherment, no key. Leads: Auer's chapter, OeStA, AHN.
- 2026-11-04 control: `solve_homophonic.py control` on two 250-letter Spanish texts of my own, enciphered with random 81-82-symbol homophonic keys; 300,000 steps x 6 restarts, es-golden-age-nospace (order 5). Letter accuracy 4-22%, best scores -487 to -540 against a true plaintext at about -380: the search does not reach the answer at this size. Added `es-golden-age-nospace` to `lang/models.json` for this.
- 2026-11-04 solver: same annealer on the letter, 6 restarts, best -488.6; output is pseudo-Spanish with no stable words; rejected because the control fails.
