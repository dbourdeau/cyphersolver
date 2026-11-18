# renard1549/vienna: the French original of the 12 July 1549 dispatch, with its contemporary decipherment

Added 16 Nov 2026 by Malcolm McBratney, working with Claude (Anthropic). The reading of this dispatch is **Ivan Sourvillo's**
(this target, from the Spanish copy at Modena). This folder adds the original and tests his reading against it; it changes none of his files.

**Document.** Simon Renard to Charles V, Paris, 12 July 1549. HHStA Wien, AT-OeStA/HHStA StAbt Frankreich, Diplomatische Korrespondenz 17,
Konvolut Juli 1549, fol. 13-14 [sourced: HHStA letter GZ 2026-0.947.186, 13 Nov 2026]. The archive sent the contributor a working scan
(4 pages, 200 dpi, md5 cb6ae0afef714450be9450cbaef1f859). The images are not committed here; the archive supplies scans on request.

**What the page holds** [measured from the scan]: the whole body is in cipher (fol. 13r 30 lines, 13v 28, 14r 9). A second hand in black ink
wrote a French decipherment above, beside (left margin) and below the cipher on each page. The sender's clear text is only the closing
prayer, date ("De Paris ce douzie[sme] de Juillet 1549") and the signature "Simon Renard"; address "A Lempereur" on 14v.

**No person has checked these transcriptions.** The French and the cipher were transcribed by AI models (Claude) from the working scan; the scan is not online.

**Files**
- `FR_CLEAR.txt`: the French clear text, transcribed as written (zones T/M/B = decipherer, C = sender, N = later note), frozen before any alignment.
- `CIPHER.tsv`, `SIGNS.tsv`: the cipher sign by sign with neutral labels S01-S69 (67 lines, 1,513 signs), frozen with FR_CLEAR (`FREEZE.txt`).
- `RESULTS.md`: layout, the key, the tests, the comparison with Sourvillo's reading, the key family and what it might open. `LOG.md`, `PRIOR_ART.md`.
- `key_renard1549_vienna.tsv`, `ALIGNMENT.tsv`, `DECODE_fullkey.txt`, `HOLDOUT*.txt`, `pipeline.py`, `holdout_bootstrap.py`, `seed_*.json`.

**The comparison with the Modena reading** (RESULTS.md section 5; Vienna wording = cipher decoded with the key, checked against the decipherment) [derived]:
it agrees on the Navarrese informant of the lord of Tende, the castle of Nice, the King and his Council, Cara the Duke's controller,
Tende with twelve galleys and 300 soldiers under cover of the fort at "Antiboul", the villages in the val d'Oste, the bastard of Savoy,
the Constable and the letters to be shown. It differs on four points: "soixante deux ou trois souldartz savoyens" (62 or 63, not 63);
"prieur de Lombardie" (not Savoy); the second plotter is "Chauvey secretaire dudit duc" (so the code word *amo* = secretary, and the
identification with Antonio de l'Eschaulx is not supported by name or office); the courier leaves "mardi ou mercredi". It names the
ambassador at Genoa: "Figueroa". Whether the differences come from the Spanish translator or the reading is not settled (Modena images not seen here).

**The key is not proven.** It was rebuilt from the decipherment ("key recovered based on adjacent plaintext"): 127 signs over 1,513 tokens,
1,201 (79.4%) on their majority value [measured]. Held-out test on the last 13 of 67 lines: first pass 73.8% of letters, but its aligner
seed was written with the whole letter in view; two leak-free reruns gave 56.7% and 64.8%, under the contributor's own 65% line.
Every run is far above the shuffled-key controls (max 27.0-28.9%, 0 of 10,000) [measured]. The cipher looks like the PP1 family
(Saint-Mauris/Granvelle, 1544-1554) on structure only; not compared sign by sign with a published table.

The plaintext of this dispatch was never secret: the decipherment is on the page. What is new here is the French text of the original and
the check of the Modena reading against it. No claim of a first reading is made.
