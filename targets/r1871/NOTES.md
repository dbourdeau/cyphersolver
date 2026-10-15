# DECODE R1871 — Sebastiano Foscarini, Paris, 11 September 1680 (ASVe Busta 30, catalogue 264)

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). This entry used to hold two unrelated
despatches; R1873 (Alvise Mocenigo, Rome, 25 April 1558) is a different cipher, read from Paolo Bonavoglia's
published decipherment, and now has its own entry ([`targets/r1873/`](../r1873/NOTES.md), page `r1873.html`).
This entry keeps R1871 only.

**Outcome: not solved.** Bonavoglia ("Decifra dispacci veneziani", crittologia.eu/critto/venezia_nomenclatore.html)
lists this despatch as deciphered, but his decipherment could not be retrieved, and the ciphertext-only attempt here
did not read it. Session 2026-09-22. (The old verdict "both already read, by Paolo Bonavoglia" held only for R1873.)

Catalogue 264 ("... (England?) to unknown recipient, 2 ciphertexts, 1555–1558") merged the two records. Neither is
from England. The "England?" region and the 1555 date come from DECODE's R1871 metadata, which seems to have been
copied from its neighbour R1872 (Giovanni Michiel, Brussels, 19 Mar 1555, also in Bonavoglia's list).

## The despatch

- Images `IMG_R1871_I8939`–`I8940` (2 PNG). f. 4 (not 1555): one page of continuous digit cipher under
  "Ser.mo Principe", marked "#117 P.S. Sola", signed "Sebastian Foscarini Amb.r", dated "Parigi li … 1680"; the
  dorse is addressed to the Doge with the docket "11 Sett. 1680 … n.o 117".
- Bonavoglia's list includes "1680-09-11: Dispaccio di ambasciatore Sebastiano Foscarini", the same despatch.
  He says the Foscarini cipher was used at both Paris and Madrid and was "troppo regolare e ordinato".
- His decipherment could not be retrieved: the interactive page returns HTTP 500 (22 Sep 2026), the Wayback snapshots
  show only the default (Mocenigo) despatch, and his dedicated page `storia/SebFoscarini_Parigi16800911.html`
  (indexed by search engines: "busta 171A, Senato, Dispacci Francia, entirely in cipher except salutation and
  signature") is 404 on www and connection-refused on web.crittologia.eu; not in the Wayback Machine or archive.today.

### Attempt here (22 Sep 2026): not read

- Transcribed the whole cipher page (23 lines, 1,839 digits; `tx.txt`, `r1871_digits.txt`) from deskewed line strips
  (`rot.png`, `lines/`), two agents, first pass (3/5 and 2/0 are the likely confusions; L22 middle weakest).
- System: **3-digit groups**. The rare digits 0, 7, 8, 9 occur only in the third place: within each line their
  positions are constant mod 3 over long stretches, and the phase jumps are transcription slips. `seg3.py` segments
  to 612 groups (593 of 3 digits; `groups.txt`, `runs.txt`): 211 distinct, first digit 1–5 (6 rare), second 1–6,
  third 0–9 → a table of about 300 codes (110–569). Top groups 156 ×22, 517 ×20, 256 ×19, 152 ×16, 459 ×15.
- Not an alphabetical (ordered) table: Sukhotin's vowel test puts vowel-like and consonant-like codes side by side
  (151/156 vowel-like, 152–154 consonant-like).
- Rejected splits: 2-digit pairs (gap parity random); self-delimiting [1-4]*[5-0] and [1-5]*[6-0] tokens (annealing
  gives no Italian).
- Solvers, all with a clean Italian 4-gram (`q4.npy`, `buildq4.py`: the shared it-cinquecento/it-modern models score
  "iiii…" above real text because the nunziature OCR has i-runs for m/n/u):
  monotone syllabary annealer (`msolve.py`, 12 seeds; recovers a synthetic ordered control only in part) → same
  non-Italian text every seed; free letter-per-code annealer (`anneal3.py`) → −2.15/char, not Italian; free
  letter/syllable annealer (`usolve.py`, 8 seeds) → fluent-looking but seed-dependent gibberish (overfit), or
  degenerate "mentemente…" at high bonus.
- Why it fails: 211 free code values against 612 groups is beyond the unicity distance of an Italian LM for a
  homophonic + syllabic table. It needs the key (ASVe *Cifre, chiavi e scontri*, not on DECODE: the only Venetian key
  records there, R1788–R1790, are 16th-century Pasini tables), more ciphertext in the same key (Foscarini's other Paris
  and Madrid despatches, 1680–84, ASVe Senato Dispacci Francia 171A and Spagna), or Bonavoglia's decipherment.

## Remaining gaps

- R1871, whole despatch (1,839 digits, 612 groups) unread. Blocker (outside): key not available anywhere reachable;
  one page of ciphertext too short for a blind solution of a ~300-code homophonic table; the existing decipherment
  (Bonavoglia) is offline.

## Escalation

- [x] siblings: DECODE has no other Foscarini 1680s despatch (Busta 30 records R1869–R1875 checked); other
  despatches in the same key are in ASVe busta 171A, not digitised. R1873 (now `targets/r1873/`) is another cipher.
- [x] clear-pages: none on the record (clear salutation and signature only).
- [x] known-keys: DECODE's Venetian key records (R1788–R1790, 16th-century Pasini tables) do not match.
- [x] print: none found; Bonavoglia's pages are the only reading. Retry
  `crittologia.eu/storia/SebFoscarini_Parigi16800911.html` and `venezia_nomenclatore.html?dispaccio=SFoscaParigi`
  later, or ask Paolo Bonavoglia for the key.
- [x] key-rebuild: done (above): monotone, free letter and letter/syllable annealers, no Italian.
- [n/a] retry: needs more ciphertext in the same key or the key itself before a rerun is worth it.

## Assumptions for George's review

- Outcome "not solved" although Bonavoglia lists the despatch as deciphered: his decipherment was never seen here, so
  it is recorded as a pointer, not as a prior reading used.

## Steps

1. Fetched R1871/R1872/R1873 record pages and all 12 images with the shared DECODE cookie.
2. Viewed all pages: identified sender, place and date from the clear text, signature and dockets.
3. (R1873 only, now in `targets/r1873/`: CSP Venice vi grep.)
4. Followed Tomokiyo's note on R1872 to Bonavoglia's page; its archived copy holds only the R1873 decipherment
   and the list naming the Foscarini 11 Sep 1680 despatch.
5. Transcription, segmentation and the solver runs above (22 Sep 2026).
6. 14 Oct 2026: R1873 split off into its own entry (`targets/r1873/`).
