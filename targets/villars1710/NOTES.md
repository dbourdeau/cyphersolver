# Villars to Polignac, camp of Arleux, 1 June 1710 (BL Add MS 61575 f. 44, DECODE R8756)

Attempted, not solved: 0 of 173 code groups deciphered; no key found, too short for a ciphertext-only attack.

Split on 14 Oct 2026 from `geertruidenberg` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter
was filed with Torcy's letter of 3 April 1710 to the Geertruidenberg plenipotentiaries (R8755) because both are
intercepts of the same negotiation in the same volume; it uses another code. Torcy's letter is
[`targets/geertruidenberg/`](../geertruidenberg/NOTES.md) (a different cipher, with its own page). The work below was
done in the geertruidenberg sessions of 16 Sept and 9 Oct 2026 and is carried over from its NOTES; the files moved here
on 14 Oct 2026.

Work date: 2026-10-09.

## The document

- BL Add MS 61575 (Blenheim Papers) f. 44, DECODE R8756 (two images, `img/R8756_P1..2.jpg`, git-ignored, in the main
  checkout's `targets/geertruidenberg/img/`; shared source folder, not moved).
- A copy headed "Copie d'une Lettre du mareschal de Villars a l'Abbé de Polignac, en datte du Camp d'Arleu le 1er Juin
  1710". Clear opening (the enemy have gathered their forces in their entrenchments; Villars cannot draw them out to
  battle), then "Vous scavez, Monsieur, que je suis informé" and 173 groups of figures, then a clear close. A modern
  note: "with W. Blencowe 5 June 1710".
- DECODE metadata lists "Duc de Villars" as receiver: he is the sender (signed "Le Mar Duc de Villars"); the receiver
  is the abbé Melchior de Polignac, French plenipotentiary at Geertruidenberg.

## Transcription (9 Oct 2026)

- DECODE transcription document `decode/DOC_8756_*.txt` (Tomokiyo's file, the one his dead Cryptiana link pointed to),
  checked against the images: "575" is 515 (so the range is 3-560); the "_" after 524 is an underline, not a gap.
- `villars_ct.txt` (as parsed from the DOC), `villars_groups.txt`: 173 groups, 106 distinct (measured 14 Oct 2026 with
  `_check_profile.py --measure`; IC 0.0089). Commonest: 340 x10, 28 x5, 32, 91, 158, 248, 267, 371 x4 each, as
  Tomokiyo lists in `blencowe2.htm`.
- Tomokiyo had already said that this letter and Torcy's use different ciphers; the value ranges confirm it
  (Torcy 1-823, 285 types over 690 groups; Villars 3-560).

## Prior-solution check (9 Oct 2026)

Tomokiyo's live `blencowe2.htm` (last modified 3 Nov 2024): listed as undeciphered by Blencowe; no reading. Web search:
no edition or decipherment. Villars, *Mémoires* (ed. Vogüé) vol. 3 appendix (`print/villars_mem3.txt` in the main
checkout's `targets/geertruidenberg/`) prints Villars to Polignac 24 May (no. 48) and 28 June (no. 52), Polignac to
Villars 1 June (no. 51) and Villars to Voysin 1 June (no. 50, same day, same subject as the clear opening), but not
this letter.

## Known keys tried (9 Oct 2026)

| key | result |
|---|---|
| Tomokiyo 11B, Desmarets 4 June 1710 code (DE=56/221, ~568 values; ~190 values from his table, `targets/geertruidenberg/tomokiyo/desmarets1710_key.tsv`) | 41/173 groups covered, nonsense; the top group 340 (x10) absent. Not this code |
| R8768, marquis de Rose code (1-578, DE=12, Jacobite names, 1715-18) | Villars has no 12; names post-1714. Ruled out on date and on DE absent; 340/28/32 not checked cell by cell |

The other keys of the volume and period (R8766, R8767, DECODE R587, BnF fr. 6204) were tested on Torcy's letter only
(see geertruidenberg NOTES); they were not applied to this one.

## Remaining gaps
- Villars 1 Jun 1710, cipher part (f. 44, 173 groups) - blocker: no-key-material; a code of values 3-560 (340 x10) with no key found in Add MS 61575, on DECODE or in Tomokiyo's tables, and 173 groups are too few for a ciphertext-only attack

## Escalation
- [x] siblings: R8746-R8774 (all of Add MS 61575 on DECODE) opened in the geertruidenberg session; the Petkum 1709 letters (key R8766) and the anonymous 10 Feb 1710 letter (R8753/R8754, small code to ~409) are different codes; keys R8757-R8770 are English or post-1711
- [x] clear-pages: R8756 has a clear opening and close only, no decipherment
- [x] known-keys: Tomokiyo 11B (Desmarets 1710) applied, nonsense; R8768 ruled out (no DE=12, post-1714 names)
- [x] print: Villars Mémoires iii (Vogüé) appendix prints the letters of 24 May, 28 June and to Voysin of 1 June, not this one; Tomokiyo blencowe2: no decipherment
- [n/a] key-rebuild: nothing reads, so there is no seed; 173 groups of a code of 500+ values are below what a ciphertext-only rebuild needs
- [n/a] retry: nothing was read to retry

## Lead not followed

- R8753/R8754 (anonymous 10 Feb 1710, Blencowe's partial decipherment on f. 29) is a small code to ~409; R8756's
  range (3-560) differs, but the two were not compared value by value.

## DECODE queue

- R8756: sender and receiver reversed on the record; origin camp of Arleux, 1 June 1710; a copy; DOC corrections
  575 -> 515 and the underline. Queued under `villars1710` in `decode_updates/queue.json`.
