# farnese1547: the French ambassador's letter from Rome, 10 August 1547, copied in cipher (ASF Mediceo del Principato 384 c. 76r), key rebuilt from its decipherment of the time (c. 79r)

Status: read in part (Brice Dudout, 9 Nov 2026; c. 76r read by the key 79.0%: 131 certain, 61 probable, 51 restored from the contemporary decipherment c. 79r, 0 unresolved, of 243 words; key partial by our protocol, 0.695 vs 0.218 on held-out lines). The text itself is known from c. 79r, the decipherment of the time; what is new is the key. c. 78r, the Farnese letter of catalogue 2339, is not read.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Lead: catalogue **2339**, found and vetted by
Daniel Bourdeau (second ASF Florence pass, 6 Nov 2026), whose "verify" asked to "read cc. 70-71 and 76-79 to see which systems
the chancery had broken". No image is included (ASF PAD images, licence not found).

## Documents

Archivio di Stato di Firenze, Mediceo del Principato 384 (Carteggio universale di Cosimo I), a gathering of August 1547:
- **c. 76r**: "Copia d'un Cap.lo d'una l(ette)ra di Roma de x d'Agosto 1547", 18 lines of continuous figures (about 1,671).
- **c. 79r**: same heading, about 16 lines of clear Italian: the decipherment of the time of c. 76r (the French ambassador at
  Rome reporting what he wrote to Henri II). Our transcriptions: `transcription_76r.txt`, `cleartext_79r.txt`.
- **c. 78r**: "Copia / D'una littera del card.le Farnese", the bare cipher of catalogue 2339: not read (see below).

## The system and the key

A homophonic substitution with a **prefix code**: 6, 8 and 9 stand alone (e, o, a); every other code has two digits (e.g.
01 = r, 05 = n, 07 = d, 23 = t, 27 = s, 70 = i, 74 = t; 10 = che, 24 = et). A dot over either digit does not change the value.
Some codes are nomenclature (Ambasciatore, Francia, Inghilterra) and are not yet in the key. `key_76r.tsv` is the key learnt on
L01-L13 only, as frozen.

## Validation (`validation.txt`)

Protocol hashed before either page was transcribed; held-out part = the last five cipher lines of 76r (L14-L18); one
measurement: character agreement **0.695** against at best 0.218 for 200 shuffled keys (margin 0.477). Thresholds fixed in
advance: >= 0.85 validated, 0.60-0.85 with the margin **partial**. The key is therefore **partial by our protocol**; the shortfall
comes from codes unseen in L01-L13.

## Reading (`reading_76r.md`, `translation_76r.md`)

By the key alone: 243 words, 131 certain, 61 probable, 51 restored from 79r, 0 unresolved: **79.0% read (certain + probable)**,
under the 95% rule. With 79r the whole text is known, but 79r retouches the wording in places (listed in `reading_76r.md`): the
cipher is the source. One transcriber (an AI agent), one pass, no independent re-reading.

## c. 78r (catalogue 2339), not read

Tried on c. 78r before this work, by criteria fixed in advance (BUILD part, M5): the Klee key of `targets/vatican5` 0.098,
**A. Meister, *Die Geheimschrift im Dienste der päpstlichen Kurie* (1906), pp. 176-177, tables no. 1 and no. 2** (as coded by
Daniel in `targets/farnese1541`) 0.174 and 0.183: **all negative**. Under the protocol the 76r key could be applied to 78r only
if validated, so it was not; 78r's own held-out lines (L12-L18) are still untouched. 78r has the same surface profile (0 never
doubled, never followed by 1-5) but the system is not established.

## Prior work (re-checked 9 Nov 2026)

No target for this gathering in this repository (farnese1541 and vatican5 are the 1541-42 papal ciphers). Daniel's vetting of
6 Nov 2026 found no edition or study of the gathering (Della Casa-Farnese correspondence, ed. Comelli 2022, vol. II, checked in
full text; DECODE, Cryptiana, Lasry: nothing). c. 79r is a decipherment of the time, so the content of c. 76r is not new.

## Remaining gaps

- c. 76r: 51 of 243 words restored from c. 79r (nomenclature codes for Ambasciatore, Francia, Inghilterra, and rare homophones unseen in L01-L13) - blocker: open-codes; the text reads and is known from c. 79r, the codes can be filled from the restored words
- c. 78r (catalogue 2339), the Farnese letter: not read - blocker: no-key-material; Klee and Meister 1906 nos. 1-2 negative, the c. 76r key is only partial and was not applied (protocol), no decipherment in the gathering

## Escalation

- [x] siblings: cc. 70-80 of the filza opened; c. 70 (Amanio) is another system (bigrams 21-39) with its decipherment at c. 71; c. 79r identified as the decipherment of c. 76r
- [x] clear-pages: c. 79r (same heading as c. 76r) transcribed and aligned; it is the decipherment of the time
- [x] known-keys: Klee (targets/vatican5) and Meister 1906 nos. 1 and 2 (targets/farnese1541) tried on c. 78r, negative
- [x] print: Della Casa-Farnese correspondence ed. Comelli 2022 vol. II searched in full text (Daniel's vetting, 6 Nov 2026); DECODE, Cryptiana, Lasry: nothing
- [n/a] key-rebuild: the key was deliberately not extended after the held-out measurement, so that key_76r.tsv stays the measured key; filling the codes from the restored words is the next step
- [n/a] retry: c. 76r is fully covered by its decipherment c. 79r, so no group is unread; c. 78r waits for a validated key
