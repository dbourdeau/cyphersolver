# R1854 image 2 — an unnamed Gonzaga agent (Rome) to Gianfrancesco Gonzaga, 9 August 1428

Read 22 Sept 2026 (key recovered from the ciphertext alone); written up at docs/r1854.html. Split on 14 Oct 2026 under
the one-key rule (George Lasry): DECODE R1854 "Mantova enciphered letters" holds four letters to Gianfrancesco
Gonzaga in four ciphers, and each is now its own entry. This folder and slug keep image 2. The others, each a
different cipher with its own page:

- image 1, Pandolfo Malatesta, Rome 22 Apr 1428 (not solved): `targets/malatesta1428/`
- image 3, Ricc. de Mutiliana, Forlì 6 Nov 1428 (key from the contemporary gloss): `targets/mutiliana1428/`
- images 4-5, Francesco de' Cattanei, Rome 13 and 21 Feb 1430 (one key, ciphertext-only): `targets/cattanei1430/`

The shared tools stay here and serve all four folders: `solve.py` (homophonic annealer), `solve_syl.py`,
`refine.py`, `occ.py`, `show.py`, `splitocc.py`, `ctx.py`, `mk_validation.py <folder>`, `decode/` (DECODE fetcher
and record views). Images are not public domain: kept git-ignored (`decode/`, `img/` in the main checkout); no page
image is published.

## The record

DECODE R1854 "Mantova enciphered letters", 5 images, status "Partially decrypted", graphic signs, no metadata (no
sender, date, language, shelfmark). Catalogue #152 "Unknown sender to unknown recipient" (Mantova State Archive).
Key record R1853 "Mantova keys" (14 images) = the Gonzaga chancery cipher register of c. 1401–1420 (folio 1: "Zifra
cum Malatesta dni Pandulfi", "Zifra nova cum fratribus de Malatestis", "Zifra ultima cum Karolo de Malatestis";
later folios keys of 1406–1419). None of its keys fits any of the four letters.

| image | date / place | sender | language | cipher | signs | entry |
|---|---|---|---|---|---|---|
| P1 (I8411) | Rome, 22 Apr 1428 | Pandolfo Malatesta, archbishop of Patras | Latin clear + 3 cipher runs | letter-like signs, unknown system | 262 | malatesta1428, not solved |
| **P2 (I8412)** | **Rome, 9 Aug 1428** | **unnamed Gonzaga agent (lozenge mark)** | **Latin** | **homophonic + nulls + 2 codes** | **1,802 (`p2v3.txt`)** | **this entry, 1,757/1,802 = 0.975** |
| P3 (I8413) | Forlì, 6 Nov 1428 | "Ricc(ardus?) de Mutiliana" | Italian, clear + runs | homophonic + nulls + 3 name codes, interlinear decipherment | 894 | mutiliana1428, 0.972 |
| P4 (I8414) | Rome, 13 Feb 1430 | Francesco de' Cattanei | Latin | homophonic + "et"/"con"/"-rum" signs | 1,537 | cattanei1430 |
| P5 (I8415) | Rome, 21 Feb 1430 (verso) | Francesco de' Cattanei | Latin | same as P4 | 199 | cattanei1430; P4+P5 1,704/1,736 = 0.982 |

## Image 2: method

Ciphertext-only. `solve.py` (homophonic annealer on the shared `lang/` Latin model, with frequency prior,
optional costed nulls) after fixing Δ = q and `17` = u from contact (Δ precedes 17 in 21 of 29 cases). Then per-sign
and per-occurrence rescoring (`refine.py`, `occ.py`) and glyph splits confirmed in the image: bold ∇ = s, thin dotted
∇̇ = null; tailed circle = p, plain circle = h; ᵹ = x vs bold 8 = f. Syllable signs 3 = con, S = et, 8t = rum.
Nulls K, W, #, Y, 19, wq, M, O, F, 20, D, dotted ∇. Codes ARW (= cardinalis, 2×) and ARO (1×, unread).
Key `key7.txt` (earlier stages key2-key6, key_p2; `keys.txt` = key7 with comments); reading `reading_p2.md`.

## Content in brief

Marriage negotiations reported through ser Vittorio and Giovanni de Orlandis: a countess (comitissa) agrees to the
match of her daughter; the subjects object that the lord of Mantua is too far away and "Carolus est nimis iuvenis ad
talia" (Carlo Gonzaga, b. 1417); Antonio Colonna and the cousins of domina Palma.

## 5 Oct 2026

Images re-fetched from DECODE with the saved cookie into `img/` (git-ignored). P2 L28 (image checked:
`= 14 j 14 P w 7 &` = l e u e n d e r): "persuaserat matri et filie u[t] vel(l)e(nt) vendere ter(r)as ipsas" (17 signs
newly read; replaces "vellent venire(?) [?] ipsas"). Re-count: P2 1757/1802 (0.975).

## 14 Oct 2026: split

The 11 Oct validation ran on the four keys pooled; `mk_validation.py` now writes one `validation.tsv` per entry and
`_validate.py` was re-run on this key alone. `make_profile.py` wrote the old combined profile and is superseded.

## Remaining gaps
- P2 code ARO (1×, "in filium [ARO]") and ~45 signs in doubtful spans (L15 "habet m num b de ue ad", L27, L31-32) - blocker: too-short; single occurrence, no sibling letter in this cipher

## Escalation
- [x] siblings: R1853 (register, 14 images) read for keys; all other Mantova records on DECODE opened (R7858-R7888 = Archivio Gonzaga E.I.2 b. 423, 16th-17th c. keys; R7888-R7890 = 1395 Armanini); none for 1428-30; the other three letters of R1854 are in other ciphers
- [x] clear-pages: image 2 is wholly in cipher; no decipherment on it
- [x] known-keys: the register keys tried; none fits
- [x] print: web search (Gonzaga, cifra, 1428); nothing printed for this letter
- [x] key-rebuild: key rebuilt ciphertext-only and extended by per-sign and per-occurrence rescoring
- [x] retry (5 Oct 2026): images re-fetched, open spots re-cropped at 3-4x; L28 read
