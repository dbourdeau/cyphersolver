# Michel Le Tellier to Pierre de Marca, 26 April 1644 — BnF Baluze 103 f. 50r-v (DECODE R2742) — NOTES

Status: in progress (21 Oct 2026). A contributed reading (Harumi-Matsuba, issue #54), made and checked by AI only; it
stays read in part until a person checks the 626 signs against views 111-112 and the open signs are retried.

**Outcome: read with known key, read in part, contributed.** Harumi-Matsuba applied Satoshi Tomokiyo's table of the
"Le Tellier-Marca Cipher (1644)" (cryptiana louisxiv0.htm), with additions checked on the sister letter f. 230r and
its period decipherment f. 232r, and sent a connected reading of the whole letter (issue #54, 20 Oct 2026; repository
https://github.com/Harumi-Matsuba/letellier1644-public, data CC BY 4.0, code MIT). Their transcription is Claude's,
corrected against OpenAI Codex passes; **no human has checked it**. Measured here: 600 of 619 cipher units (96.9%)
carry a key value that stands in their reading; the f. 171r calibration (theirs) gives 91.3% of signs right, so the
sign error on f. 50 is likely near one in eleven, absorbed by context on 18 of 32 lines.

This is not `targets/letellier/` (Le Tellier to Castelnau, 1657, a different cipher, skipped 15 Sept 2026).

## The letter

- BnF Baluze 103 (Affaires de Catalogne, correspondance de Marca), f. 50r (20 cipher lines, dated in clear "Du 26e
  avril 1644") and f. 50v (12 cipher lines); f. 51 is the address leaf ("receue le 3 may, resp. le 4 may"), f. 52
  filing slips. Gallica ark:/12148/btv1b9001389d views 111-112 (images via the BnF IIIF server
  `openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9001389d/f111/...`; gallica.bnf.fr/iiif answered with a Cloudflare
  page on 21 Oct 2026).
- Michel Le Tellier, secretary of state for war, at court, to Pierre de Marca, visitor general (later intendant)
  in Catalonia, newly arrived in Barcelona.
- DECODE R2742 ("BnF_Baluze103_f50"): holder field "Baluze 103, f.51-52" (the cipher is f. 50r-v), author Le
  Tellier, no place, status Decrypted with no decryption text (Tomokiyo's upload: key and paper). Siblings R2743
  (f. 171-173), R2744 (f. 189-191), R2745 (f. 200-206), R2746 (f. 230-233), each with its period decipherment.
- No period decipherment of f. 50 exists in the volume: the contributor looked at all 743 views. The 1921 Baluze
  catalogue's "dont quelques-unes chiffrées, avec traductions (fol. 50, 171, 189, 200, 230)" holds for the other four.

## What it says (contributor's reading, summarised)

The Barcelona councillors, preparing Marca's lodgings, chose the house of a friend of Marshal de La Motte, who hoped
in that way to learn everything Marca does and writes; Marca is warned to be on his guard. Barcelona's agent at court
complains that the packets the Catalans send him are opened [?] at La Motte's; the Queen wishes Marca to watch this,
report, and stop it. Joined French text: `contributed/docs/READING.en.md`.

## Files

- `contributed/`: the contributor's files, copied 21 Oct 2026 from the public repository (main branch): `data/key.tsv`
  (sign names, values, source T/S/X/C), `data/transcription_f50.txt` (final), `data/transcription_f50_before_xcheck.txt`,
  `data/decoded_f50.txt` (bare decode), `data/SIGNS.md`, `data/tomokiyo_table_signs.tsv`, `data/f230r_*`, `data/f232r_*`,
  `calib/` (f. 171r blind reading, f. 172r reference, hashes), `controls/`, `second/` (independent Codex pass and
  vote record), `docs/*.en.md` (method, reading, open points, prior check), `NUMBERS.md`, `SOURCES.en.md`, `LICENSE`,
  `ATTRIBUTION.md`.
- `measure.py` / `measure.txt`: our re-measure (own decoder, lang/ model).

## Checks made here (21 Oct 2026)

1. `measure.py`: 619 cipher units (626 sign tokens by `_check_profile.py --measure --drop-first`; clear words out,
   the pair =11 =o as one), 616 with a value (99.5%). fr-1600-letters (order 5, no spaces): bare decode -2.490/char,
   joined reading -1.977, 200 shuffled keys median -5.087, max -4.500, 0/200 at or above the bare decode. The key is
   right; the language model cannot say whether the context repairs are.
2. DP alignment of each line's signs with the contributor's line reading: 600/619 (96.9%) of units have a key value
   that stands in the reading. This is the share the key, not context, supplies; it is not a check of the
   transcription.
3. Their calibration recomputed from their files: 339/360 letters (94.2%; they give 337/360 with a slightly different
   normalisation). Note: the reference f. 172r text is itself their AI transcription of the period decipherment.
4. Image spot-check (BnF IIIF, 2400 px): lines r01-r03, r17-r20, v01, v12, 167 signs. The sign count agrees on all
   nine lines and no sign reads differently, except the plain 6 / small sigma choice (their own disputed list) and the
   cross before =3 on r19, which shows two bars (they flag it as ‡‡ in OPEN but transcribe pb). This look is by
   Claude as well; it is not the human check the reading lacks.

## Verification 5, 23 Oct 2026

Plain-bar check (French 1644): the entry pointed at the bare decode `contributed/data/decoded_f50.txt`. The
contributor's joined French reading is now `f50_reading.md`: plain 0.6, explicit 0.667, at the bar (open signs, supplied
endings, the name Marca). Keeps read; the human sign check on views 111-112 ("Next") is still the way to lift it.

## Independent verification by Brice Dudout (PR #572, 14 Nov 2026)

Brice Dudout (PR #572, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) decoded
`contributed/data/transcription_f50.txt` with `key.tsv` and the code groups of Tomokiyo's table and the contributor's
`METHOD.en.md`: the bare decode equals `decoded_f50.txt` on 725 of 725 letters. Re-run here: same.

Reading side. Of the 741 letters of the line readings, 24 are marked as supplied and 13 more come from no sign. Nine
are the documented *qu'il* from an unbarred 12. Four were silent supplies, which the transcription confirms (no sign
there): *pr[is] soing* (r02-r03: no i, and one s sign for two), *c[e] que* (v03), *[d]'icy* (v04), *p[a]ssent* (v06).
They are now bracketed in `f50_reading.md` (our scored copy; the contributor's `READING.en.md` is unchanged).
Read share recounted with `v10_relabel.measure`: 0.924 before, **0.904** after (178 words, 19 holes). Read in part, as
before.

Open signs, as he reads them on Gallica views 111-112 (not repeated here on the image, not counted as read):
- r02 `p` is the s of Tomokiyo's table, as in v01 *paquets*; the word it belongs to is still not understood.
- the dots around r04 `22` also stand between plain letters in r03, so they do not mark a code group.
- the hooked mark of r06 `23` stands over the 3 only: perhaps 2 and a marked 3 rather than a code 23.
- v05 `18` carries a full bar; the code words run in alphabetical order (9 pour, 11 que, 12 qui, 26 vous), and 18
  falls between *qui* and *vous*, where *sçavoir* fits. Still a guess, with one more argument.
No key correction. The human check of the signs is still owed.

## Remaining gaps
- signs and code groups without a value: p (r02), the sign ending r03 (l… logis?), 22 (r04), 23 with a hooked mark (r06), Ꝺ 22 (r16), the double-barred cross before =3 (r19), =18 (v05) - blocker: no-key-material; each occurs once; =18 is not in the four sister letters and their decipherments
- 18 of 32 lines where a sign was chosen from context or letters are missing (r02-r07, r10-r13, r15, r16, r19, v05, v08, v10-v12) - blocker: no-key-material; the transcription was made and checked by AI only, workable by a person reading the signs on views 111-112

## Escalation
- [x] siblings: ff. 171, 189, 200, 230 and their period decipherments (172, 190, 205-206, 232) used by the contributor for the key and the code groups; all 743 views searched, no decipherment of f. 50
- [n/a] clear-pages: f. 51 is the address leaf, f. 52 filing slips; Marca's reply of 4 May (view 121) does not touch the lodging or the packets
- [x] known-keys: Tomokiyo's 1644 table is this letter's key; additions checked on f. 230r/f. 232r (412/424 signs)
- [x] print: HathiTrust and Internet Archive phrase searches 0 hits; Issartel 2010 read; Sanabre 1956, Dubarat, Torreilles not read in full (contributor's PRIOR_CHECK)
- [x] key-rebuild: values added from the f. 230r alignment; =18 and the 23-hook sign not in any sister letter
- [x] retry: language-model control and DP alignment re-run here on the contributor's transcription; nothing new read

## Next

- A person to check the signs on views 111-112, starting with the 18 marked lines.
- Ask Satoshi Tomokiyo whether he holds a reading of f. 50 (he lists it as undeciphered).
- DECODE R2742: folio f. 50r-v (not f. 51-52); status Partially decrypted with the reading attached
  (`decode_updates/queue.json`).
