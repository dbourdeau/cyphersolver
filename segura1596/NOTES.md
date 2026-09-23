# Matheo de Segura to the Constable of Castile, 8 August 1596

Status: read

BnF espagnol 336 no. 99 ff.196r–198r; Gallica btv1b100325613 views 336–340. The old view-280 locator is wrong: that image is f.164. Cipher passages are on views 337 and 338. Work date: 23 September 2026.

## Prior art
Tomokiyo's GL.htm marks the volume Most Solved after Lasry's 2023 work on other letters; spanish3.htm and unsolved.htm still explicitly list this short letter undeciphered. The live pages were obtained over HTTP with a descriptive User-Agent after HTTPS failed. No external plaintext for this target was found or used. This is the last item on that list, not an independent audit of every letter in the volume.

## Access
Gallica highres, IIIF, item and manifest requests failed with 403; the browser failed too. Wikimedia Commons mirrors supplied the full-resolution images using a descriptive User-Agent. Files are named `Espagnol_336_-_btv1b100325613_(338_of_366).jpg` (substitute view number). The public-domain manuscript is BnF's; only small attributed crops are published here. Views 334–342 and nearby later letters were inspected, including all five written target pages; no decipherment was visible. The dateline and signature are on view 340.

## Result

See reading.md for the edited text and English translation. The striking passage reads: **dizen que el mundo se acabará o morirá el rey por setiembre. Él bien cerca dello paresce que anda. Creo en Dios.** The clear introduction attributes this to a grave councillor reporting a meeting about a recent comet. The shorter passage reads **A Ponte creo cierto … conforman él y Escudero**. A Ponte/Aponte and the apparent repetition of clear *se conforman* followed by cipher *conforman* remain editorial difficulties; neither is silently repaired.

All 125 cipher tokens (35 distinct sign labels) have proposed values. Six singleton tokens remain grade M; the other 119 are I (95.2% when all M values are excluded). No independent key or decipherment verifies these values, so no H/C grades are claimed. `decode.py` reproduces the literal text, TSV grades, coverage and the site reveal from `cipher_tokens.txt` and `key.json`. This is a reconstruction of the used signs, not the complete historical key. The proposed homophonic system includes two nulls and one special doubled-letter sign, all three context-dependent.

## Method and unsuccessful moves

The initial 114-token, 32-type draft mistakenly joined signs. A Python homophonic annealer and a speculative *pronostico* crib did not solve it. The crib was discarded. C# annealing with the repository's Spanish Golden Age order-5 model ran 250 restarts per variant: joined/corrected, dots collapsed, and split plus dots collapsed. Only the last found the connected phrases *dizen que el mundo*, *el rey*, *paresce que anda* and *Escudero*. The logs retain imperfect candidate outputs; none is represented as the final reading.

Image reinspection split `dc` into qshape+d (qu), `lb` into l+b (el), and a joined B-like form into l+three (es). The two signs e D at the end of the clear introduction belong to *dizen*. The final looped J is distinct from L. A square c and a hooked qshape must be distinguished. The overwritten end of the second comet line is provisionally m, giving *setiem-bre*. The broad openC in the first passage gives *cierto*. Dots above and below signs are not collapsed in the final transcription. Deleting Hd and rd gives the first passage; ud supplies ll in *dello*. This final resegmentation has 125 tokens, not 114.

Compared the published Descovar, Fuentes–Pimentel (1595), Ibarra–Doria (1592), Ibarra–Zúñiga (1593), and Cg.13 sign inventories on cryptiana. No direct match was found. **Devos 1950's full key tables were not obtained and are not claimed to have been tested.** Searches of the available printed/online references and local DECODE harvest found no independent target reading or matched record. Known late numerical keys were not a usable direct key to these signs.

## Remaining gaps

No cipher token lacks a proposed value. Six tentative singleton assignments are explicitly marked M in reading.md and token_reading.tsv: Hd=null, rd=null, openC=t, Q=n, X=m, ud=ll. Their independent confirmation is blocked by no-key-material: no contemporary key, parallel ciphertext or decipherment located. Name segmentation, pronouns and punctuation remain editorial, not additional recovered signs.

## Escalation

- [x] siblings: views 334–342 and nearby later letters inspected; no matching decipherment located.
- [x] clear-pages: all five written pages inspected; they supply context, date and signature, not the encrypted plaintext.
- [x] known-keys: five published comparator inventories inspected; no match. Devos full tables unavailable, explicitly left unverified.
- [x] print: GL.htm, spanish3.htm, spanish4.htm, unsolved.htm and web/library searches checked; target still listed undeciphered.
- [x] key-rebuild: three annealing variants, then image-based segmentation and extension to every sign used.
- [x] retry: every run decoded with final key; six context-dependent tokens retained as M rather than claimed certain.

## Reproduction and publication

Run `python segura1596/decode.py`; it asserts all eight literal decrypted runs and writes token_reading.tsv, coverage.json and docs/reveal/segura1596.json. Solver trials are preserved separately. Full page images, downloaded modern web pages, generated binaries and language-model arrays are excluded from Git; retrieve the Commons files by their view numbers. The published crops allow comparison with the cipher.

No DECODE record was identified, so there is no DECODE update to queue. No atlas route is asserted: Madrid is explicit, but the recipient's location on this date has not been established. No safely identified individual portrait of the sender was found; the recipient's Commons results included the Somerset House group, not a verified individual crop, so portraits are omitted. The key-web record is unlinked because the key was rebuilt only from this text. Publication follows the repository writeup skill in an isolated origin/main worktree.
