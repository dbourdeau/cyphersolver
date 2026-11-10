# Sega 1591b: Filippo Sega, Bishop of Piacenza, Paris, early January 1591, duplicate (AAV Francia 32, ff. 49v-54v), read in part with Meister key 65

Status: read in part (Brice Dudout, 29 Oct 2026, submitted 10 Nov 2026; 1,319 enciphered words, 1,091 read in their sense = 82.7%: 886 certain, 205 probable, 3 restored, 225 unresolved; below Daniel Bourdeau's 95% rule; the copy is incomplete).

Contributed by Brice Dudout (Europe chiffrée), 10 Nov 2026. Not in the catalogue (it belongs to the withdrawn no. 881, "Sega, Francia 32"); submitted as a new cipher with solution, read in part.
Published write-up (partial reading, unresolved words shown in place): https://bdudout.github.io/europe-chiffree/en/documents.html#sega1591-dupl

Proposed as its own target because it is a different document from the two letters of targets/sega1590 (another letter, another date, another DECODE record, about eight pages of cipher) and from Lasry's targets/sega1591 (9 Jan 1591, BnF fr. 3613, different content). If you prefer it as a third document of sega1590, it can be moved there; the read-bar rule would then make sega1590 "read in part". Your call.

## Document

Archivio Apostolico Vaticano, Segreteria di Stato, Francia 32, ff. 49r-54v: "Dupp.ta" (duplicate) of a letter of Filippo Sega to an "Ill.mo et R.mo Mons.r" (the series is addressed to Cardinal Enrico Caetani), Paris, shortly after 20 December 1590 ("L'ultime mie furono delli 20 di Dicembre"); dated here early January 1591 by its content and its place in the volume.
F. 49r is in clear (Biron in Normandy, munitions from Holland, the "pratica del Commercio" with Navarre); ff. 49v-54v are almost entirely in cipher, with short clear passages. The copy stops at the foot of f. 54v in the middle of an enciphered sentence, with no subscription; ff. 55-56 are another letter (to the Pope, 9 January 1591).
Images: DECODE R5615 (views 2-12), https://de-crypt.org/decrypt-web/RecordsView/5615 - not included (DECODE terms: research use only). No contemporary decipherment of this letter in the DECODE records of Francia 32 (R5612-R5618, R5621).

## System and key

Meister (1906), key no. 65, "cifra servita in legatione sub Sisto V" (pp. 435-436): letters as digit pairs, vowels as signs on the pair or on a single digit, nulls 7 8 9 0, code letters and symbols for common words, three-digit nomenclator.
George Lasry identified this key for Sega's letter of 9 January 1591 (targets/sega1591). Applied here unchanged (`key.tsv`, the same file as targets/sega1590).

## Validation

No new measurement for this letter (it has no contemporary decipherment). The key is the one validated for targets/sega1590, with the protocol written and hashed before calculation: Sega's letter of 21 December 1590 (Francia 32, ff. 228v and 231) against its contemporary decifrato on f. 230 (DECODE R5621, https://de-crypt.org/decrypt-web/RecordsView/5621): 268/287 characters (0.934) and 56/65 words (0.862), against at most 0.551 / 0.492 for 200 controls with permuted letter values; criterion 0.85 / 0.75 met. Caveat: transcriptions made with the key in mind.

## Reading

1,319 enciphered words: 886 certain (67.2%), 205 probable (15.5%), 3 restored (0.2%), 225 unresolved (17.1%). Read in their sense: 1,091 (82.7%; 1,094 = 82.9% if the 3 restored words are counted). Below Daniel Bourdeau's 95% threshold: read in part. Share read by page (%, restored included, from the final count of 29 Oct 2026): 49v 93.3, 50r 95.8, 50v 95.2, 51r 96.2, 51v 82.8, 52r 76.7, 52v 84.7, 53r 74.9, 53v 73.6, 54r 72.5, 54v 83.5. The opening blocks B1-B5 (all enciphered segments from f. 49v to f. 50v line 9, 205 words) read at 94.6% (171 certain, 23 probable, 1 restored, 10 unresolved) after Brice Dudout's blind re-reading of four signs (plate C08); the denser pages ff. 51v-54v are much weaker. The copy is incomplete: f. 54v ends inside the cipher, with no subscription.

Each of the 88 blocks was frozen before it was decoded; one final count was made at the end of the letter (no stopping when the running share crossed 95%). Brice Dudout chose, on 29 Oct 2026, to publish the whole letter as a partial reading with the missing words visible, rather than only its better-read opening.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Remaining gaps

- 225 unresolved words, two thirds of them on the dense pages ff. 51v-54r (pale ink, show-through from the verso, pairs that do not align with the key) - blocker: needs-physical-access; only the DECODE study images were used, a better image or the original at the AAV is needed to settle the signs.
- Signs absent from Meister's printed key: the long s with a crook (6 times, always before a noun), a delta at the head of a clause where the sense calls for che, and a few single marks (crossed looped stroke, triangle on a bar, barred f) - blocker: open-codes; kept unresolved rather than guessed.
- The end of the letter: the copy stops at the foot of f. 54v inside the cipher, with no subscription - blocker: needs-physical-access; the original or a decifrato of this letter is not among the DECODE records of Francia 32.

## Escalation

- [x] siblings: all DECODE records of the series opened (R5612-R5618, R5621); no decifrato of this letter (R5613 holds the decifrato of the 9 Jan 1591 letter only); ff. 55-56 next to it are another letter (to the Pope, 9 Jan 1591).
- [x] clear-pages: f. 49r and the clear passages between the enciphered blocks checked: they are the letter's own clear text, not a decipherment.
- [x] known-keys: Meister key 65, the key of this legation, validated on the decifrato of 21 Dec 1590 (R5621); the other system of Sega's letter of 2 July 1591 (R5618) was tested on that letter and rejected; no other key of the series is known.
- [x] print: no edition of Sega's dispatches of 1590-1591 found (Acta Nuntiaturae Gallicae do not cover Sega; M. Penzi 2017 is a study; Lasry's sega1591 is another letter); checked 29 Oct 2026.
- [n/a] key-rebuild: the key is a printed historical key applied unchanged by rule; extending it from this text would need a new held-out validation, so signs missing from the print are left unresolved.
- [n/a] retry: no second pass over the whole letter; the count is the single final count fixed in advance (no stopping when the running share crossed 95%), with the per-block re-readings and the blind plate C08 included; a new pass would need better images.

## Notes

- Content (summary): League Paris under Navarre's blockade, early January 1591: the commerce negotiation and passports; Cardinal de Gondi's refusal of the oath of the Union; canons tempted to rally to Navarre; preachers against "Senlis"; the writer stays in the city to hold it to its duty; Brissac's mission for Mayenne; a request for a thousand paid Spanish and Italian foot and victuals; hopes of taking Saint-Denis by escalade until the Duke of Parma arrives; a plan to detach the princes of the blood and the Catholic nobility from Navarre; a monitory against Navarre's followers; plots discovered at Orléans, Nantes and Chalon; a divided Union government (City, Parlement, Council) and a "weak head" (Mayenne); the proposed remedy: the Pope to take Paris and the Île-de-France under the protection of the Holy See until the Estates and the canonical election of a Catholic king.
- Same hand and same key as the letter of 26 Nov 1590 (targets/sega1590, DECODE R5612, https://de-crypt.org/decrypt-web/RecordsView/5612); the "instrutione ... con le mie delli vintisei di Novembre" of f. 49v refers to that letter.
- Prior work: no edition of Sega's 1590-1591 dispatches found (the Acta Nuntiaturae Gallicae do not cover Sega; M. Penzi 2017 is a study); checked 29 Oct 2026.
