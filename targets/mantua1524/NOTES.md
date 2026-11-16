# mantua1524: three cipher leaves sent to Federico II Gonzaga in 1524, one homophonic key (BAV Vat. lat. 8214, ff. 298r-v, 68r, 198r)

Status: in progress. Read in part with a key recovered from the text alone, contributed by Andrew Aymeloglu (work of 15 Nov 2026, issue #697 of 16 Nov 2026; repository `aaymeloglu/unsolved-ciphers`, folder `mantua-1524`, CC0, commit f0ffa76). By the project's count (only strict segments are read): 50% of 284 cipher words; 298r-v 38%, 68r 55%, 198r 79%. No page yet; a reviewer other than the contributor records the reading grade before it merges.

Catalogue 2368 is f. 298r-v. Ff. 68r and 198r are new finds (the contributor paged all 816 images of the volume); they enter as leads through `research/sweep_2026-11-16_vat_lat_8214/`, not as catalogue entries. One key, one folder.

## The documents

Biblioteca Apostolica Vaticana, Vat. lat. 8214, a volume of letters and extracts sent to Federico II Gonzaga, marquis of Mantua, in 1523-24. It belongs with Castiglione's papers in the BAV: catalogue 2368's vetting gives them as Vat. lat. 8204-8214; the contributor counts Vat. lat. 8199-8213 as the same bequest as 8214. Images on DigiVatLib (IIIF, 1962 px full size); `aaymeloglu/images.tsv` lists the IIIF URL and SHA-256 of each leaf used. None is copied here.

- f. 298r-v: "Ex litteris Suardini datis Victorie? 26 Februarii", an extract of a letter of Giovan Battista Suardino at the Imperial court; heading and 23 lines on the recto, 8 on the verso; clear Italian with cipher runs in nearly every line. Catalogue 2368.
- f. 68r: a letter almost all in cipher, no heading, among the Milan items of January 1524; 23 lines, first person plural.
- f. 198r: "Ex litteris D. Cappini dat. in Robio 8 Aprilis 1524" (Capino de Capo); 26 lines of clear Italian with two cipher lines (17-18).

No other page of the volume has cipher, a gloss, a clear copy or a key (the contributor's page-by-page pass).

## The cipher and the key

A homophonic substitution over Latin letters, digits and signs, in which some letter pairs are single units: `m i`, `o o`, `c c`, `d d`, `b b`, `l o`, `n o`, `p a`, `l a`, `b o`, `m o`, `g r`, `g 1`, `b u`. The single o never stands alone, which is what showed the pairs; without joining them the anneal did not converge. For example 9 = a, 2 = e, crossed 9 = o, `m i` = i, 8 = r, doubly crossed p = u/v, crossed double s = l, x = n, 7 = c, `o o` and `l o` = t, s = d, 4 = h. 54 units, 38 with a value. No key sheet, gloss or contemporary decipherment is known, so every value is grade S. `aaymeloglu/key.json` gives each value with its supporting words and a confidence class: A (several independent words), B (two independently secure words), W (two words, one resting on an uncertain sign or unit), C (one word). Only A and B values can make a segment strict.

Exceptions to a single substitution remain and are shown as such in the reading: `l o` gives t securely but five readings want l; `p+` and `p#` must read per in *per lui* and *per la morte*; x must stay x in *exercito*; i must read e in *denari*; H would need incompatible values. DECODE R7860 (a Mantuan key of 1524-25, ASMn AG b. 423 f. 8) and R7865 (d'Atri, c. 1510) were compared by the contributor and do not fit.

## Method

1. Transcription sign by sign from the full-size BAV images, with alternatives `x{y}?` for doubtful signs; 68r second-checked on 5 of 23 lines plus targeted image checks of disputed signs.
2. Pair-unit merges: letter pairs that behave as one sign joined into units (the list above), each tested by re-annealing with and without it (below).
3. Annealing: a homophonic simulated annealing with a 4-gram character model (the contributor's `cipherkit`, `it` corpus: Venetian dispatches of 1589, Albèri's Relazioni, Machiavelli; j/v/k/y folded) on the three leaves pooled, which gave a first key with the frequent letters and several sinks.
4. Hand refinement: values fixed by hand only where several independent words agree (Prospero, Carpi, heredi, investitura, Cremona, fatto, fiume, Februarii); further units joined where repeated words required them. Every decision and its supporting words is in `aaymeloglu/audit/decisions.md`.

Each segment (one run of cipher between clear words, as transcribed) is graded strict (every unit A or B, no code sign, no transcriber alternative, the reading spells the key output), forced (one weak unit, code sign or alternative, but only one reading gives a word), lenient (the reading departs from the key output or was chosen by sense), doubt or unread. `aaymeloglu/verify.py` recomputes every key output from the transcriptions and `key.json`, enforces these rules and prints the counts; it runs unchanged from this folder (`python3 targets/mantua1524/aaymeloglu/verify.py`; only its usage line was edited).

## Controls

As the contributor states them (`aaymeloglu/README_aaymeloglu.md`, Controls; outputs in `aaymeloglu/audit/`):

- Key shuffle on the text used for fitting (200 shuffles, lines 68r 20-23 excluded): 4-gram z = 14.5; lexicon-string segments 81 of 191 against 19.0 ± 5.9. Circular for a hand-tuned key: it shows the key is far from a relabelling of the same values, not that each word is right.
- Reserved lines 68r 20-23, set aside before the hand refinement and scored by rules written before the count (`aaymeloglu/audit/reserved-lines.md`): 19 of 31 segments are lexicon strings against 4.8 ± 1.6 for 200 shuffled keys; 10 of the 20 fully keyed segments of 4+ letters against 0.06. This is a **fit-consistency check with leakage, not a held-out test**: the annealed key the refinement started from was fitted on all lines including these, its decode of them had been printed once, and a shuffled-key null does not model the trying of many keys and merges. With the later `b u` unit and two image corrections on line 23 the counts are 22 of 31 and 13 of 20, reported apart. A passage transcribed and frozen before decoding is the missing predictive test.
- Leave-one-out: freeing one unit and choosing its value by the 4-gram model returns the key value for most units but not for I, i, 6, b, pa, bu, bb, g1, o, S; those values rest on words and names, not on the model.
- Merges tested both ways (A values fixed, re-annealed): splitting `l o` or `n o` loses hits (79 to 68 and 74); splitting `p a` or `b u` is inconclusive.
- Matched synthetic control: an unaided anneal of f. 298 alone (406 units) recovered 35-60% of synthetic homophonic Italian of the same shape; on about 1,200 units and 38 symbols it recovered 94% in one run of three and 45% in two (on an earlier unit scheme). Pooling the three leaves is what made the solve possible, and an unaided anneal is unreliable at this length, which is why the frequent values were checked against words.

## The Codex review

A second model (Codex) reviewed the work independently (`aaymeloglu/audit/codex-review.md`): it checked 174 signs in 19 key groups on the images, reproduced every key output and the control arithmetic, and checked the historical claims, finding Benzoni's account of the urine deception (below). Its transcription corrections at 298v 04/6 and 68r 23/4, 23/5, its reading "ve parirà" and its historical corrections are applied. It could not locate the segment 68r 19/2; two loop-and-descender signs are visible there on the image and the segment is kept, unread.

## Check by the project (comment on issue #697, 16 Nov 2026)

`verify.py` reproduces every count; a decoder written by the project from `key.json` gives the key output for all 227 segments (1,197 units); the 298r and 198r image hashes match the BAV copies; the two cipher lines of 198r agree with the scan sign for sign (the first sign of *Barbon* could be 6 or b; both give b). The key is fitted on all three leaves together, the pair merges were chosen after the fact, and nothing was held out.

## What the letters say

**f. 298r-v.** Suardino at Charles V's court (at Vitoria from 5 January to 6 March 1524, which fits the doubtful heading) on Carpi, confiscated from Alberto Pio and granted to Prospero Colonna, who died at Milan in late December 1523: he was told that [BOX] had given Carpi to Prospero for him and his heirs but had not made the investiture, and might draw a sum of money from it in this need of Italy and compensate the heirs otherwise. On the verso the Chancellor answers that the grant stands for the heirs despite the death, though the investiture was not made, and that it was not yet determined whether Carpi had been taken away by right. The grant without investiture is already in Petrucci's life of Colonna (DBI 27, 1982); the letter gives the state of the question at court in February 1524. BOX is a code sign: the Emperor where he is the grantor, more naturally the Marquis in "che [BOX] fosse preposto ad ogni altro".

**f. 68r.** A "we" told not to ride out feigns illness: rode a horse the day before yesterday and showed in the evening that it had tired him, schooled a jennet and made a show of hurting his back, and "havemo questa matina mandato fori alli medici ... orine fatte tingere a posta con sangue ... facendo uscire voce che havemo ... orinato sangue ... da poter mostrare al [..] Duca di Sessa et a chi ve parirà, ma per la verità siamo sano et gagliardo como mai fossimo". Benzoni's life of Federico II (DBI 45, 1995) tells the same deception and Federico's admission of it to Castiglione, so 68r is plausibly Federico to Castiglione, his ambassador at Rome; that is an inference from the match, as the leaf names neither. The Duke of Sessa was Charles V's ambassador at Rome in 1524.

**f. 198r.** After the clear "...prima la tregua di Spagna per il maneggio del Arcivescovo di Capua", in cipher: "se retirerà questo exercito de fiume in fiume, et poi in Pavia, Cremona et Milano", then clear "secondo dice", cipher "Barbon". A conditional, prospective retreat, not a report of an itinerary followed. The cipher reads Cremona sign for sign.

## Counts

The project's rule (issue #697): only sure words count. Strict segments are read; forced, lenient, doubtful and unread ones are holes. That gives **50% of the 284 cipher words: 298r-v 38%, 68r 55%, 198r 79%**, the figures used in `profile.json`. Parts of 298r (lines 1-17) and 68r (lines 01-10) are close to "decoded, not read", and the reviewer is asked to look at them.

The contributor's segment counts (`verify.py`):

| Leaf | Segments | Strict | Forced | Lenient | Doubt | Unread |
|---|---|---|---|---|---|---|
| f. 298r-v | 69 | 36 | 9 | 13 | 4 | 7 |
| f. 68r (incl. reserved lines 20-23) | 145 | 95 | 11 | 21 | 7 | 11 |
| f. 198r | 13 | 10 | 2 | 1 | 0 | 0 |
| all | 227 | 141 | 22 | 35 | 11 | 18 |

`aaymeloglu/running_text.py` reproduces the project's count: each whitespace-separated token of a segment's reading is a word (so an unread group such as `[H g o]` counts three, and the heading "26", a cipher row graded unread, counts one), a word split between segments is one word, read only if every segment in it is strict. It gives 143 of 284 (50.4%): 298r-v 37 of 98 (37.8%), 68r 95 of 172 (55.2%), 198r 11 of 14 (78.6%). The running texts mark holes by words instead: an unread segment with no reading is one word (the least the decode shows; an estimate), so the same 143 read words stand among 253 (56.5%); that figure is given for the reader and is not the one recorded.

## Reading and texts

For each document, in `aaymeloglu/`: the transcription (`transcription-298.tsv`, `transcription-68r.tsv`, `transcription-198r.tsv`), the decryption line by line against it (`decryption_<doc>.tsv`: units, key output, reading and tier of every segment), the running text of the leaf, every word in order with holes sized (`reading_<doc>.md`), and the English with the same holes (`translation_<doc>.md`). The running texts are generated by `running_text.py` from the transcriptions and `reading-words.tsv` (`--check` reports a stale file); the English was written by hand from them and from the contributor's `reading.md`. In the running texts a word read from a strict segment is plain, a proposal from any other segment is `[?word]`, a code sign `[?BOX]`, an unread segment `[...]` or `[... n]`.

The contributor's own reading with notes per passage is `aaymeloglu/reading.md`; the sign inventory `aaymeloglu/signs.md`.

## Remaining gaps

- The source of Benzoni's quotation for 68r ("orine" tinte di "sangue", "sano et gagliardo") - blocker: needs-physical-access; the candidate texts (a clear minute in Federico's copialettere, ASMn, Archivio Gonzaga; a decipherment among Castiglione's papers in the BAV; La Rocca's notes) are not online as far as checked (Escalation, print)
- The ASMn original of f. 298 (Suardino, Archivio Gonzaga, Carteggio estero: Spagna) may carry a chancery decipherment; likewise Capino's letter of 198r (Carteggio estero: Milano) - blocker: needs-physical-access; not online, not seen; it would give the first values above grade S
- Victorie in the heading of 298r (key output `uf[n]fctorie`; the minim cluster after the crossed p shows three minims, not the four of `m i`) - blocker: illegible; the full-size image does not settle the cluster; the court's presence at Vitoria makes the place plausible
- `l o` reads t in most words but l in five (canceltere twice, lattro, caualto, alti) - blocker: open-codes; no graphic rule found to separate the two; a doubling device is speculation; those words are lenient
- Code signs BOX, H and IZ (also CROSS and the looped C@), and the single-occurrence signs `p@`, `b+`, `8+`, `) )` - blocker: open-codes; BOX has no single referent (the Emperor as grantor, the Marquis in one place), H would need incompatible values
- 68r lines 01-02 blotted and partly clear; the name at 07-08 (key output `cchilte`, `borronei`) and the clear "salve" (02, 10) unread - blocker: illegible; lines 01-02 are blotted on the only image, and the name and "salve" have no second occurrence that reads
- 68r second check partial: 5 of 23 lines plus targeted checks of disputed signs - blocker: not-attempted; the other 18 lines can be second-checked from the images
- One-word values (q, o, bb, c, S, b, g1, p+) and the weak units mo, gr, bu - blocker: too-short; about 1,200 units in this key; any further letter in it would test them

## Escalation

- [ ] print: **the source of Benzoni's quotation first.** G. Benzoni, "Federico II Gonzaga", DBI 45 (1995): "Ai medici - lo confessò F. stesso al fido Castiglione - esibì 'orine' tinte di 'sangue' ... era 'sano et gagliardo'". The decode of 68r gives "orine fatte tingere a posta con sangue" and "siamo sano et gagliardo como mai fossimo" (the latter on the reserved lines 20-23). His Fonti include Bibl. ap. Vaticana, Vat. lat. 8214; B. Castiglione, *Lettere*, ed. G. Gorni (Milano-Napoli 1969); and Id., *Le lettere*, ed. G. La Rocca, I (Milano 1978). Candidate sources: (1) a clear minute of the letter in Federico's copialettere (ASMn, Archivio Gonzaga, Copialettere, early 1524); (2) a contemporary decipherment among Castiglione's papers (Vat. lat. 8199-8213, the same bequest as 8214); (3) La Rocca's notes to the letters of early 1524, which may quote Federico's letter from either. Also unchecked: the later edition of Castiglione's *Lettere famigliari e diplomatiche* (ed. La Rocca, Stella, Morando, Einaudi 2016). What was run: archive.org has neither the Gorni nor the La Rocca edition; one web search on the quoted phrases with Federico, Castiglione and 1524 found nothing. None of the candidates is online as far as checked. Finding the source is the real test of the key and decides whether 68r counts as read from an existing text.
- [x] siblings: all 816 images of Vat. lat. 8214 paged by the contributor: cipher only on ff. 68r, 198r, 298r-v; no gloss, clear copy or key. The other Castiglione volumes (Vat. lat. 8199-8213) not paged
- [x] clear-pages: the clear passages of all three leaves are transcribed and used as context; none is a decipherment of the cipher
- [x] known-keys: DECODE R7860 (Mantuan key of 1524-25, ASMn AG b. 423 f. 8) and R7865 (d'Atri, c. 1510) compared by the contributor and do not fit; the Gonzaga keys of the 1520s in ASMn not reached
- [x] key-rebuild: annealing with pair-unit merges, then hand refinement from words; leave-one-out and merge tests run (Controls)
- [ ] retry: after a source text or an ASMn decipherment is found, or after the second check of 68r is completed

## Credits and tools

Work by Claude Code agents (Claude Fable, Claude Opus): transcription, the volume-wide page scan, annealing with `cipherkit`, then hand refinement word by word; independent review by Codex; Andrew Aymeloglu reviewed the result. Credited as Andrew Aymeloglu (contributor id `aymeloglu`).

## Files

| File | Content |
|---|---|
| `aaymeloglu/key.json` | the key: every unit with its value, grade, supporting words, confidence, leave-one-out value |
| `aaymeloglu/transcription-298.tsv`, `aaymeloglu/transcription-68r.tsv`, `aaymeloglu/transcription-198r.tsv` | one row per segment (cipher, clear, raised), alternatives kept |
| `aaymeloglu/reading-words.tsv` | units, key output, reading, tier and note per cipher segment |
| `aaymeloglu/decryption_298.tsv`, `aaymeloglu/decryption_68r.tsv`, `aaymeloglu/decryption_198r.tsv` | the decryption line by line against the transcription (generated) |
| `aaymeloglu/reading_298.md`, `aaymeloglu/reading_68r.md`, `aaymeloglu/reading_198r.md` | running text of each leaf, every word in order, holes sized (generated) |
| `aaymeloglu/translation_298.md`, `aaymeloglu/translation_68r.md`, `aaymeloglu/translation_198r.md` | English, same holes |
| `aaymeloglu/running_text.py` | builds the running texts and decryption files, prints the word counts |
| `aaymeloglu/verify.py` | recomputes the key output, enforces the tier rules, prints the segment counts |
| `aaymeloglu/reading.md`, `aaymeloglu/signs.md`, `aaymeloglu/README_aaymeloglu.md` | the contributor's reading with notes, sign inventory and account |
| `aaymeloglu/images.tsv` | the BAV IIIF images used, with SHA-256 |
| `aaymeloglu/audit/` | decisions log, reserved-line protocol, the Codex review, control outputs |
