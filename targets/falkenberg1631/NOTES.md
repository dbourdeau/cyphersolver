# falkenberg1631: Dietrich von Falkenberg (Magdeburg) to Gustavus Adolphus, 28 March 1631: letter-and-nomenclator key validated, content existing

Status: in progress (integration check of 14 Nov 2026, PR #571: the key and its held-out test reproduce and the letter has a decipherment of the time on the next two images, so its content exists; folder only, no page and no ledger row, because the open pieces below can still be worked from the images in hand. Strict share of the contributor's own reading before the clear copy was seen: 92 of 172 cipher tokens sure = 53.5 %.)

**Contributor's status:** read in part by sense before the clear copy was found, now existing. Contributed by Brice Dudout, Europe chiffree, with a Claude Opus 5.5 agent (29 Oct 2026). In Daniel's leads.json as leads 1126 (this letter) and 1127 (unsigned letter of 2 March 1631); no catalogue entry, no target.

## Document
Riksarkivet, Stockholm, SE/RA/1133/1133.07/~/10 (Skrivelser till konungen, Gustav II Adolf, volume "F"), image R0000785_00133 (fol. 101), "D. 28 Mars 1631", ciphered; followed on 00134 (fol. 102, signed "D. v. F.") and 00135 (fol. 103) by two clear copies of the time. Images under Public Domain Mark; none reproduced here. The neighbouring letters of Falkenberg (Dec 1630 - March 1631, images 112-132) are glossed between the lines by the Swedish chancery.

## System and key
Two-digit numbers 10-99 = letters in bands of three consecutive homophones (attested values: a 72-74, b 69-71, c 48-50, d 45-47, e 24-26, f 22-23, g 75-77, h 66-68, i 51-53, k 43-44, l 27-29, m 19-20, n 78-80, o 63-65, p 54-56, r 30-32, s 15-17, t 81-83, u/v 60-62, w 57-59, z 12 and 14; f 21, m 18, k 42 and z 13 only by the band pattern, and 42 reads r once in "veraendert"; 9, 10, 85, 86, 88, 90, 92, 97-99 are nulls in K2. K1, the validated key, lacks 12, 19, 22, 23, 43 and 51); numbers 100-3999 = an alphabetical nomenclator (about one code per word, roughly strict alphabetical order: 126 abgesandt ... 3961); abbreviations (rr = und, ee = nicht, d.g. = zu, x = bey, aa = mit, E. K. Mt = Eq/2110, g = die, u = ist ...). key.tsv is K1; frozen/ holds K2 (K1 + about 90 values from the other glosses; K2 sha256 63531dca...b677) and its additions.

## Validation
K1 on the held-out letter of 17 March 1631: letters 39/43 = 0.907, codes 22/24 by the frozen script (24/24 after two normalisation misses); controls 0.233 / 0.125. See validation.txt.

## Reading and prior art
Before the clear copies were seen: of the 172 cipher tokens 92 sure (53.5 %, strict count), 20 probable, 25 restored (79.7 % with these; 84.3 % in a first count), 35 unresolved. The clear copy of the time (images 134-135) makes the content existing; Dittmar no. 33 said the letter was not deciphered and was wrong. Nothing else found in print on the key. Nothing in this repository except the two leads; the vetting of lead 1126 already records the two clear copies (from our corrections of 29 Oct 2026), lead 1127 is vetted "partly read" from Dittmar p. 363 no. 31.

## Integration check (14 Nov 2026, PR #571)

Checked by the project on the merged files; the contributor's files are unchanged apart from this section, the status line,
the gaps and the escalation list.

| claim | contributor | ours | how |
|---|---|---|---|
| hashes | PROTOCOLE 8ccb6650..., K1.json bf4f4e03..., K2.json 63531dca... | all three match | sha256sum |
| K1 on the held-out letter of 17 March | letters 39/43 = 0.907, codes 22/24 = 0.917; controls max 0.233 / 0.125 | identical (control means 0.053 / 0.016); 17 code tokens of the letter have no K1 value | `frozen/validate.py` run as filed |
| K1 built without the held-out letter | yes | every source in `frozen/K1_codes.tsv` is 121R, 126R, 129R or 130R; none is image 131 | own count |
| reading before the clear copy | 92 sure, 20 probable, 25 restored, 35 unresolved of 172 | same counts from `reading_tokens.tsv`; strict share 92/172 = 53.5 % | own count |
| transcription | - | lines L01-L08 and N03-N07 compared with image R0000785_00133 (about 130 groups): all agree; the doubtful "37?9" of L02 is 3729 on the image | Riksarkivet IIIF, fetched by script with a Referer header |
| clear copy on image 134 | two clear copies of the time | image 134 right page seen: headed "D. 28 Mars 1631", signed "D. v. F.", it follows the cipher phrase by phrase ("nach Sparenbergs Verreisen hatt s[ich] hier ziemlich verändert. Dan Tilli selbst ankommen ...") and carries corrections between the lines, so it is a decipherer's working copy; image 135 not opened | image |
| own decoder | - | written from `frozen/K2.json`, run on `transcription.txt`: the letter runs give Garleben, Saltwedel, Vertröstung, meisten, Chemnitiu(s), abusirt, Seite, Holtz, essen, Campangne; the codes give the words of the clear copy | own script |

- **Order of events.** The protocol, K1 and the choice of the held-out letter are "before" by the contributor's record: one
  commit, hashes with no outside timestamp. `HANDOFF.md` and `build_K2.py`, which the protocol and `frozen/K2.sha256`
  name, are not in the PR.
- **The pass.** The codes score by the frozen script is 22/24; "24/24" is a judgment made after the run and is not the
  figure of record. The gloss of the held-out letter was read by the same AI transcriber, with several doubtful words.
- **Second held-out test (K2, 22 Jan 1631): inconclusive** by the contributor's own statement (three glossed lines). It
  is not a pass. K1 is the only key with a formal measurement; K2 adds about 90 glossed values without one.
- **One key, one entry.** Not the key of `targets/chemnitz1631` (Martin Chemnitz, Nuremberg, 1631: a different table,
  with letters on a cycle of 24 and no four-digit nomenclator) and not that of `targets/magdeburg1647` (letter
  substitution of the archbishopric's envoys, 1646-47). The Chemnitius whom this letter names is the same man; the
  ciphers are not related. Falkenberg's other letters of the volume (images 102-132) use this key and are glossed.
- **Class and method.** The text of the letter is the decipherment of the time (class: already solved). The key was
  rebuilt from the glosses of the neighbouring letters (method: key recovered based on adjacent plaintext), and passed
  its one pre-set measurement. Key state: partial (K1 lacks 12, 19, 22, 23, 43, 51 and 17 codes of the held-out letter;
  the codes listed under Remaining gaps had no value when the letter was read).
- **Leads.** Lead 1126 was already closed as read on 29 Oct 2026 (the clear copies); it now points here. Lead 1127
  (2 March 1631) is untouched. Not on DECODE (`decode_updates/queue.json`: skip).
- **Why no page.** Workable from the images in hand: a full transcription and translation of the clear copy (the filed
  `decryption.txt` is a quick reading with doubtful words and stops before the end of part 2), the re-keying of the
  codes it identifies, a strict count of the cipher against it, and the search for the letter of 2 March.

## Remaining gaps
- Codes never glossed (1807, 3729, 3629, 501, 3783 1/2, 3770, 3961, 2430, 211, 1091, 2720, 3724, 3147, 1313, 518) and nine abbreviations: now identified for most from the clear copy, to be re-keyed.
- The clear copy (images 134-135) is filed only as a quick reading with doubtful words; part 2 not re-read; image 135 not compared; no full translation. Workable.
- No strict count of the cipher against the clear copy yet (the 53.5 % is the reading made before it was seen). Workable.
- Lead 1127 (2 March 1631) not located in images 100-137 (probably glossed). Workable: the volume is online.
- Other letters of the volume (images 102-110) not exhausted; collection Falkenberg SE/RA/720223 and Stallman letters not digitised.

## Escalation
Siblings: lead 1127. Clear pages: found (images 134-135). Known keys: none published. Print: Dittmar, Kirchhoff checked via the paraphrases. Key rebuild: K1/K2 done.

Next (14 Nov 2026): transcribe and translate the clear copy in full; re-key K2 from it and count strictly; page the volume for the letter of 2 March; then write up.
