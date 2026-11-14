# Francisco de Vargas (Venice) to Charles V, 25 August 1552

Status: in progress (re-read 23 Oct 2026, b36: the letter now reads from its contemporary decipherment; no site page or README row yet, left to the write-up pass)

**23 Oct 2026, re-read (REREAD_BRIEF batch b36, Claude Opus 5.5): R9967 read from the contemporary decipherment on the letter.** All 16 DECODE images opened at full size (their P numbers are out of page order; the archive numbers 0001-0016 in the headers give the order). The decipherment, in a second hand in the left margins, at the page feet and between the lines, is one continuous text across 14 pages; transcribed in full with the clear paragraphs (`texts/R9967_decipherment.txt`) and checked against the cipher without a key: the clear words left in the cipher lines agree at ten places, and the codes `ager` cardenal, `pollo` papa, `s-o` el, `x-o` del, `n-o` al recur consistently (`texts/R9967_code_check.tsv`). Reading `texts/R9967_reading.md`, English `texts/R9967_en.md`, log `texts/R9967_reread_log.md`. b17 on the body 0.701 plain, 0.996 explicit holes. Content: the Pope suspected over Siena (Sant'Angelo, the legate [?Mignanelli]), the Duke of Florence, the Duke of Urbino and Venice, the conde de Pitigliano's son, the French secretary Serri to be seized, the Salerno fleet at Porto Ercole.

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): no transcription or decipherment of R9967 is in the repository; the marginal decipherment is on the DECODE images only. R9967 is *decoded, not read* in profile.json; class already solved is kept (deciphered in the margin, Tomokiyo).

Earlier status (before the 22 Oct 2026 reading audit): no write-up

Catalogue entry 197. AGS, Estado, leg. 1320, ff. 35-38; DECODE R9967 (listed as "Non-decrypted", 16 pp.).

## Result: already read (deciphered at the time, cipher identified by Tomokiyo)

Satoshi Tomokiyo's cryptiana page on Spanish ciphers of Charles V (cached copy at
`targets/vasto1527/prior/spanish2C_now.htm`) gives this record:

> Francisco de Vargas to Charles V, 25 August 1552 AGS,EST,LEG,1320,35-38. DECODE R9967. Deciphered in the margin.
> Again (!), after reconstructing the cipher, this turned out to be the same as Imperial Cipher of 1544-1554.

So the letter was deciphered on arrival, with the decipherment written in the margins. Tomokiyo rebuilt the key from it
and found it was the Imperial Cipher of 1544-1554 (also used by Juan de Vega, R9964). DECODE's "Non-decrypted" means
only that no decryption is attached to the record.

Nothing new to read, so no write-up. The DECODE images were not viewed in this session (21 Sept 2026; all 16 were viewed and the decipherment transcribed on 23 Oct 2026, b36, above): the ruling rests on Tomokiyo's
check. If anyone wants the text, the marginal decipherment on the leaves is the place to start.

Catalogue entry 197 removed on 21 Sept 2026. DECODE status correction queued (`decode_updates/queue.json`).

## Remaining gaps

- eight words of the marginal decipherment and the legate's name ([?Mignanelo]) - blocker: illegible; small margin hand at DECODE's 1850 x 2600 px (PARES lower); only the AGS originals would settle them
- sign-by-sign check of the spelled cipher runs - blocker: not-attempted; the cipher runs are not transcribed. Key material for it now exists: the sign tables of `targets/gonzaga1549/` (3 Nov 2026) and `targets/gonzaga1549/wainut/`, and the Simancas reconstruction of 1866, AGS D/00203 no. 243 (issue #618, 14 Nov 2026; see `targets/gonzaga1549/NOTES.md`). Its code list has Cardenal ager and Papa pollo, as `texts/R9967_code_check.tsv` found on the letter (ager three times, pollo four)
- closed 23 Oct 2026 (b36): the marginal decipherment fetched, transcribed and read

## Escalation

- [x] siblings: Juan de Vega R9964 uses the same Imperial Cipher of 1544-1554 (Tomokiyo)
- [x] clear-pages: 23 Oct 2026 (b36) the decipherment on the leaves transcribed in full; neighbours R9966, R9968 are other letters
- [x] known-keys: the Imperial Cipher of 1544-1554 identified by Tomokiyo
- [ ] known-keys, 14 Nov 2026 (issue #618, Brice Dudout): the Simancas reconstruction of 1866 and the two sign tables in the repository are available; the cipher runs are not yet transcribed and checked with them
- [x] print: Tomokiyo gives no edition; not needed, the decipherment on the leaves is complete
- [n/a] key-rebuild: the key is known
- [x] retry: 23 Oct 2026 (b36) the letter read from the decipherment
