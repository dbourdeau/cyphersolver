# Görtz memorandum 1717, KB Stockholm I.g.18 (DECODE R4350): German numeric code

Status: no write-up (attempted, closed unread: 809-group German nomenclator, no key on DECODE or in print; ciphertext-only attack below solvability, synthetic control failed)

Catalogue 206: "Murberg, Johan, Görtz, Georg Heinrich von to unknown recipient", National Library of Sweden, DECODE R4350.

## What it is (viewed 22 Sept 2026)

- DECODE R4350 is not a 4-page letter: its one PDF (`IMG_R4350_I26104_P.pdf`, 114 images) is the whole volume
  *Bref och Handlingar angående Baron von Görtz 1717–1721*, collected by Johan Murberg (KB I.g.18, 1785). Images are
  git-ignored (`goertz1717/img/`, fetched with the bordeaux cookie).
- The cipher is in one piece: a German memorandum on a peace settlement in the Great Northern War (King Augustus and
  the Polish crown, Stanisław, the Czar, Livonia/Estonia/Viborg/Narva, England-Hanover, Prussia, Denmark, the Norway
  expedition), 1717, in a copyist's hand. The writer is plainly Görtz or someone near him writing to Charles XII.
  The cipher passages are the sensitive conditions. They sit in PDF pp. 34 (items "1°" and "2°"), 35 (top), 37 (bottom),
  38 (most of the page) and 41 (middle). Other pages show numbers only as show-through.
- Transcription: `transcription.txt` (with clear words kept in brackets); groups only in `groups.txt`.
  Measured: 809 groups, 175 distinct, IC 0.0175; top 778 x67, 748 x32, 113 x28, 687 x24.
  About 10 groups at the ends of lines on the left-hand pages (pp. 34, 38) are lost in the binding gutter (`?`).
- The copyist left common words in clear inside the cipher (und, auch, wol sonder zweifel, würde, in zwischen, ein,
  können, wider, denn, seyn, als auch, ich, eine, allermassen, welches, es). There is no interlinear decipherment.

## System (what the statistics say)

- Numbers 1–848, 175 used. Frames like `712 49 113`, `712 80 113`, `712 848 113`, `712 548 113` show homophones.
  `286 687` occurs 15 times; `778` is 8% of groups, but splitting on it gives no word-length pattern, so it is not
  a word separator. This is probably a homophonic nomenclator of about 850 entries (letters with homophones, plus
  syllables and words), German plaintext.

## Remaining gaps
- all five cipher passages (809 groups) - blocker: no-key-material; Görtz's German code is not on DECODE (only his French 4-digit code R7691) or in print, and ciphertext-only solving at 809 groups over 175 symbols failed even on a synthetic control

## Escalation
- [x] siblings: the whole Murberg volume (114 images) viewed; no other cipher, no decipherment. DECODE 1710s Swedish records swept: BL Add MS 32287 keys R7690-R7702 downloaded (`keys/`)
- [x] clear-pages: none; the clear text round the cipher is the memorandum itself, not a decipherment
- [x] known-keys: R7691 "Baron Gortz à la Haye 19 Oct 1716" is a French 4-digit code (1000-9900); R7690 (1707) is a French code 10-540; R7692-R7702 are Gyllenborg's French codes. None fits a German 1-848 code
- [x] print: web search for the memorandum and a Görtz cipher; nothing found. The 1717 London *Letters which passed between Count Gyllenborg, the Barons Gortz, Sparre...* prints Gyllenborg-affair letters, not this memorandum
- [x] key-rebuild: homophonic letter annealer (`hanneal.py`, de-modern order 5, clear words as fixed context), 8 seeds x 3M moves, best -2.05/char, gibberish; French, Swedish, Italian worse; alphabetical-syllabary annealer (`msolve_de.py`, from swieten1757) 8 seeds, word salad. Synthetic control (809 German letters in 174 homophones, `runs_synth.txt`) also not recovered, with or without a KL frequency prior (`hanneal2.py`)
- [x] key-rebuild, second pass (same day): control rebuilt from in-corpus modern German (`synth2`, true text -1.63/char at order 4). Long anneals (20M moves, T0 3-12, orders 4/5, 8 runs) all stop at -1.90 in an e/n-flood optimum; exhaustive per-group hill-climb with shotgun restarts (`hclimb.py`) -1.96/-2.02; fixed letter-count swap annealer (`hanneal3.py`) -2.55. The control is never recovered, so the real text (harder: syllable/word codes, 1717 spelling) is out of reach of these tools. A far stronger solver (AZdecrypt-class, large 5-6-gram tables) is the only ciphertext-only route left.
- [n/a] retry: nothing was read, so there is nothing to re-run with an extended key

## Leads for later
- Riksarkivet Stockholm holds Görtz's papers (Görtziana, Holstein-Gottorp chancery). A German key of about 850 entries
  from 1716–18 there would read this directly.
- The original of the memorandum (not Murberg's copy) may carry an interlinear decipherment.
