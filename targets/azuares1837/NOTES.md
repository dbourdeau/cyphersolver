# azuares1837: Manuel Azuares to the Carlist Secretary of State, London, 8 Sep 1837 (catalogue 2421)

Status: read in part (Brice Dudout, 9 Nov 2026; 285 of 361 cipher words = 78.9% without restorations; one table validated by our protocol, M5 0.882, margin 0.374 against the best of 1,000 shuffled tables).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry 2421 (Daniel Bourdeau's
Spain sweep of PARES, AHN Diversos-Colecciones, vetted 9 Nov 2026). No DECODE record, no edition found.

## Document

Archivo Histórico Nacional, Madrid, DIVERSOS-COLECCIONES, 161, N.2 (PARES 3735838): letter no. 780 (marked "Duplicado")
of Manuel Azuares, Carlist agent in London, 8 Sep 1837, 12 images. Runs of cipher in letters are set in clear Spanish on
views 03-12, with a few digit groups (nomenclator). The images are online on PARES without login; **no image, crop or
thumbnail is included here**, because the reproduction licence was not found on the record.

## System and key (`key.tsv`)

- Letter-for-letter substitution of Spanish written in the same cursive hand as the clear text (letters, a long s ſ, a
  round r like z, ll and ñ as single units). The unit e/c stands for u or b.
- **One table per group of pages**, not one per run: K3 (p. 3), K5 (pp. 4-5), T6 (pp. 6-7), T8 (p. 8), T9 (pp. 9-12).
  Each change of table is announced by a group x + l/z/g/h (xgzl, xzlg, xlgz, xlzh, xlzgh), probably an indicator; not
  resolved.
- Digit groups 4607229, 5071574925, 5344727605, 507, 403710131 are not resolved.
- Only **T6** is verified (see below). K3, K5, T8, T9 give coherent Spanish but are not validated.

## Validation (`validation.txt`, `frozen/`)

First protocol (held-out set = view 12): negative, view 12 is under another table. Amendment 01, frozen before any new
decoding: five passages of views 06-11, a table learnt on the first half of each and measured once on the second half,
with a correction for multiple comparisons (reference = best of all 1,000 shuffled tables, 0.508). **P063 (06.17-23)
validated: M5 0.882, margin 0.374.** P062, P081, P092, P112 negative (held-out halves of 51-71 units). The verified table,
applied unchanged, reads the rest of pages 6-7; we count those words certain, and declare that this is not a new measurement.

## Reading (`reading.md`, `translation.md`)

361 cipher words: 70 certain (T6), 215 probable, 67 restored, 9 unresolved -> 78.9% read without restorations, 97.5% with
them; counted by hand on `decryption.txt`, approximate. `reading_review` B.

Content: Azuares reports talks with the Austrian chargé d'affaires: the Powers (Austria, Britain) contemplate making Maria II
an absolute queen and reviving the old Portuguese Cortes, with General Goblet ("Globet") guiding Prince Ferdinand, even at
the cost of Dom Miguel's rights; Lisbon would treat with Don Carlos on mutual security once he reached Madrid. Azuares
objects that this would recognise the usurpation and would not give a lasting peace.

Corrections at our review before publication (9 Nov 2026): words absent from the cipher removed from an earlier draft
("de Lisboa", "del Norte", "se"; "se trata de" and "existe en" are clear text); doubtful words moved to unresolved; the
certain class limited to the verified table.

## Remaining gaps

- Readings under tables K3, K5, T8, T9 (215 probable words) - blocker: too-short; their held-out halves (51-71 units) could not beat the corrected reference; fresh cipher under the same tables or a second human reader would settle them.
- Five indicator groups and five digit groups (4607229, 5071574925, 5344727605, 507, 403710131) - blocker: open-codes; each occurs once, no nomenclator found.
- 04.02 (18 units) and 9 unresolved words - blocker: illegible; a reading of those lines at full resolution by a human reader.

## Escalation

- [n/a] siblings: N.5 of the same volume (Villafranca, catalogue 2422) uses another system (additive key on a written alphabet); no sibling in the same letter cipher found.
- [n/a] clear-pages: no clear minute or decipherment on the 12 leaves.
- [x] known-keys: none held in the repository or on DECODE for Carlist agents (catalogue vetting, 9 Nov 2026).
- [n/a] print: no edition found.
- [x] key-rebuild: tables rebuilt per group of pages; T6 validated.
- [x] retry: every line re-decoded with its group table at the review of 9 Nov 2026 and regraded (decryption.txt); the open words stay open. A new held-out test of K3/K5/T8/T9 needs never-decoded cipher under them (other Azuares letters in volume 161).

Prior work checked 9 Nov 2026 by the GitHub API only: catalogue 2421 "open", no key held; no target, issue or PR on
Azuares, 2421 or Carlist ciphers (only carlos1903, unrelated); nothing in research/leads.json.
