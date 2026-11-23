# Mexican embassy, Washington, to the consul at Eagle Pass, 17 April 1917: the "clave Murciélago" telegram

Status: read in part (Andrew Beling, with AI agents, 23 Nov 2026). 26 of 37 words come out of the key uncorrected (70.3%; README 95% word bar), and 11 words carry a sender's slip read from the sense. The sentences run from end to end. Key recovered from the cipher text alone. No person has checked the reading; an independent AI reviewer reproduced it blind (model reading, below).

## Document

- **Archive:** AHGE-SRE (Acervo Histórico Diplomático, Secretaría de Relaciones Exteriores), Archivo de la Embajada de México en Estados Unidos, leg. 507, exp. 6. The original was **not seen**.
- **Our source:** the halftone of the telegram printed as fig. 10, p. 339, in Roberto Narváez, *Criptografía diplomática, política y militar en México (1813-1926)* (Mexico: SRE, 2019). We worked from phone photographs of a loan copy. No image is committed and none of the book's tables is reproduced here.
- **Credit:** Narváez published the telegram and its context (pp. 338-342). He says the message stayed impenetrable to the consul, and he prints no reading.
- **The sheet:** typed, headed "WASHINGTON D.C. ABRIL 17 de 1917." and addressed to "SR. JOSE M. ARREDONDO, CONSUL DE MEXICO, EAGLE PASS, TEXAS." The clear preamble reads "MENSAJE AYER CIFRADO CLAVE MUERCIELAGO REPITOSELO CLAVE TREINTAIUNO". In English: the message enciphered yesterday (16 April) in the Murciélago key, repeated to you, key thirty-one.
- **Context, from the book:** in April 1917 several consuls (Douglas, San Francisco, New Orleans, Eagle Pass, Brownsville) wrote that they could not decipher embassy telegrams. On 17 April Arredondo replied that he could not read this one "con clave Murciélago ochentaidos" (word 82 of the consular key list, p. 339). Narváez explains the confusion as consuls using the wrong key list (p. 338).
- **Historical setting:** the United States had declared war on 6 April 1917. On 13 April Wilson created the Committee on Public Information by Executive Order 2594; the formal Censorship Board came only in October 1917. The "comité censura nombrado por presidente Wilson" of a 16-17 April telegram can only be that committee. The identification is the independent reviewer's.

## System and key

- **Simple substitution** with a reciprocal alphabet (`key.tsv`): A-X, B-U, C-S, D-Q, E-P, F-M, G-L, I-Z, N-W, O-V, R-Y, and T stands for itself.
- **Unseen letters:** cipher A, H, I, J and K do not occur. H, J and K have no known value.
- **Evidence:**
  - The index of coincidence is 0.071, flat over periods 1-12. That is one alphabet, not a keyword run through the Murciélago square named in the heading.
  - The book's square with key word 31 of the printed list was tested first, under a frozen plan, and missed.
- **Cipher D, M and N** have at most one clean occurrence each:
  - D, once, in "que";
  - M, twice, but one is the doubtful position 121;
  - N, twice, but one is the extra letter in "falsas".
  
  Their values rest on the reciprocal pairing, which the other 18 letters show without exception. That is an assumption about the system.
- **Not a keyword alphabet:** 3,791 keywords (including MURCIELAGO) were tried, both directions, all 26 offsets. The best score (-3144.2) is below every shuffled control.
- **Against the keys printed by Narváez:**
  - not the Murciélago square (p. 333 instructions, fig. 8);
  - not the 1915 "Clave Garduño" reciprocal table (p. 311), which shares one pair;
  - not any of the nine reciprocal rows of Seguín's 1916 plana (fig. 7, p. 326), though two rows share several pairs.
  
  It is a reciprocal alphabet of the same family that the book does not print.
- **The book's explanation stays open.** Fig. 9 is captioned as one of two key lists. "Clave treintaiuno" could be alphabet no. 31 of a second, numbered list of such alphabets, as in Seguín's numbered plana. That would fit Narváez's wrong-list explanation. It has not been tested.

## Method

All work was done on 23 Nov 2026 by AI agents (Claude Opus 5.5) run by Andrew Beling. Files are in `work/`.

1. **Transcription.** Three transcriptions were made from the book photographs: `transcription_pass1.txt` (agent), `transcription_pass2.txt` (a helper given only the images, blind) and `review/blind_transcription.txt` (the independent reviewer, blind). Each has 246 letters, and they differ only at the letters listed under Transcription doubts. `transcription.txt` gives the readings used.
2. **Plan.** `work/PLAN.md` was written and hashed (`PLAN.sha256`) before the runs. It sets the hypothesis, the solver, the corpus, the controls and the pass mark: Spanish sentences over at least 90% of the letters in clean words, plus a held-out check. The order rests only on local file times: plan 00:13:01 EST, first control run 00:13:44.
3. **Controls first** (`work/runs/controls_summary.json`, every seed and score in `work/runs/*.tsv`):
   - three shuffles of the 246 letters scored -2964.3, -2939.3 and -2923.6, with no Spanish;
   - three 246-letter passages of real Spanish (from `targets/carranza1915`, held out of the corpus) under random keys came back 99.2%, 99.2% and 99.6% right.
   
   The method works at this length.
4. **Solve.**
   - The solver is simulated annealing on Spanish letter 4-grams built from *Archivo Santander* XIV (Internet Archive OCR) and the Spanish readings of 13 Mexican 1906-1914 targets in this repository. It used 40 restarts with fixed seeds.
   - Best scores: -2490.9 on pass 1 and -2473.7 on pass 2. That is above all shuffles and inside the range of the enciphered controls.
   - The machine key was wrong on five rare cipher letters: D, L, M, N and O. L = g and O = v come from the pass 2 solve (both well attested by their pairs: cipher G = l 9 times, cipher V = o 28 times). D, M and N were set by the reciprocal pairing and the sense.
5. **Held-out check.** The key solved on letters 1-170 reads letters 171-246 unchanged apart from the sender's slips. Cipher K at position 243 (pass 1 only) does not occur in 1-170. On pass 1 as transcribed, the tail ends "...cocprobarlo caso necmswrio".
6. **Pass mark.** The plan's 90% letter mark was **missed**: 159 of 246 letters (64.6%) are in clean words. The cause is enciphering slips spread over eleven words, not unread passages.
7. **Model reading by an independent reviewer** (`review/`). Before seeing this work, a separate AI agent made its own blind transcription and solved it with its own code (`review/my_solve.py`) and its own corpus (Spanish Wikipedia extracts, not committed). It got the same paired key and the same Spanish sentence, word for word (`review/independent_solution.txt`). It also re-ran the scripts in `work/scripts/` and reproduced every run file byte for byte. This is a model reading, not a person's.

To re-run: `python3 -I targets/eaglepass1917/decrypt.py` from the repository root rewrites `decryption.txt` (standard library only). For a doubtful letter, use for example `--alt 121=N`. The solver scripts in `work/scripts/` need numpy and point to local paths on our machine (the corpus is not committed). They are kept as the record of the runs.

## Reading

See `reading.md` (Spanish, holes marked) and `translation.md`.

> Para {presentar} los a comité censura nombrado {por} {presidente} Wilson {necesito} mándeme mayor brevedad posible nombres {periodistas} y agentes información {que} propalan {falsas} {noticias} y agitan opinión principalmente con noticias complots {alemanes}. Debemos poder {comprobarlo} caso {necesario}.

> To present them to the censorship committee appointed by President Wilson, I need you to send me as soon as possible the names of journalists and information agents who spread false news and stir up opinion, chiefly with news of German plots. We must be able to prove it if necessary.

**Counts.**

| basis | words | letters in clean words |
|---|---|---|
| readings in `transcription.txt` | 26 / 37 (70.3%) | 159 / 246 (64.6%) |
| if position 121 is N | 25 / 37 (67.6%) | 148 / 246 (60.2%) |
| if position 241 is P (against the photographs) | 27 / 37 (73.0%) | 168 / 246 (68.3%) |

The repository's key replay (`python docs/_replay.py eaglepass1917`, through `replay.py`) reports "reproduces (every difference marked)": 27 of 37 words exact and 233 of 246 letters exact. Ten words are marked. It scores "falsas" as exact because it charges the extra cipher letter N to the gap beside the bracket. The strict count above charges it to the word, which gives 26 of 37.

**The slips.**
- The twelve slip letters in eleven words are what the sender typed. They show clearly on the photographs, except "por", where the letter looks typed over, and position 241 (F/P).
- Five are one pattern: plain e and t exchanged. Cipher T (= t) is typed for e three times (necesito twice, alemanes), and cipher P (= e) for t twice (presidente, periodistas). Typed P and T do not look alike, so these are not misreadings.
- The pattern may come from confusing the e and t lines of a reciprocal table (T is the only letter that stands for itself), or from the Morse E/T confusion if the draft came off a telegram. Neither can be shown from one sheet.
- The other slips: presen{t}ar (F), p{o}r (Y), pre{s}idente (S, possibly seseo), q{u}e (V), an extra N in falsas, notic{i}as (C), co{m}probarlo (S), nec{e}sario (F).

## Transcription doubts

- [P/F] (position 23, ZTPSP) - read: P; checked: image, decode, transcription; F and P alike on the halftone; the three transcriptions read P, giving "comité censura".
- [Y/X] (position 40, XQVEY) - read: Y; checked: image, decode, transcription; the letter is heavily inked, apparently typed over; neither Y nor X gives the o of "por", so the word is a hole.
- [F/P] (position 73, FPFXR) - read: F; checked: image, decode, transcription; passes 1 and 2 read F, and the reviewer changed P to F on a closer look; F gives "mándeme mayor".
- [P/F] (position 82, OPQXQ) - read: P; checked: image, decode, transcription; P gives "brevedad".
- [P/F] (position 114, RXLPW) - read: P; checked: image, decode, transcription; P gives "agentes".
- [M/N] (position 121, TPCZWM) - read: M; checked: image, decode, transcription; **unresolved**: pass 1 reads M, pass 2 and the reviewer prefer N; M gives "información", N gives "inwormación" (a hole). The counts are given both ways.
- [P/F] (position 132, after the stroke in SZVWDV/PEYV) - read: P; checked: image, decode, transcription; a closed bowl on the closer zoom (reviewer); P gives "que".
- [E/B] (position 136, EXGXW) - read: E; checked: image, decode, transcription; E gives "propalan".
- [M/H] (position 141, MNX) - read: M; checked: image, decode, transcription; M gives the f of "falsas"; the N after it is an extra letter.
- [G/C] (positions 144, 232) - read: G; checked: image, decode, transcription; G gives "falsas" and "comprobarlo".
- [F/P] (position 241, SFCXY) - read: F; checked: image, decode, transcription; all three transcriptions read F, which gives "necmsario" (a hole); P would give "necesario". Kept as F because the photographs show F.
- [X/K] (position 243, SFCXY) - read: X; checked: image, decode, transcription; pass 2 and the reviewer read X and pass 1 read K; the letter looks like X over K.
- [Z/E] (position 245, ZV) - read: Z; checked: image, decode, transcription; Z gives "necesario".
- The "/" in SZVWDV/PEYV - not a letter; typed or pen stroke, not settled.

## Related

- **Lobo to Bonillas** (F. J. Lobo, Clifton, 25 Nov 1916 or 1917, same file, Narváez fig. 14, in our lead sweep, pull request 902) uses a different system. Its index of coincidence is 0.047-0.048, and this key applied unchanged gives no Spanish.

## Remaining gaps

- The archive's own image of leg. 507, exp. 6 is not seen. Every letter here comes from a halftone in a printed book photographed by phone. The reading should be checked against the original, especially positions 40, 121 and 241. This is the open step.
- The original telegram of 16 April and the second key list (with "clave 31") are in the same file and not seen.
- Cipher H, J and K: no value.
- US intercepts of 1917 embassy-consular traffic (NARA M1194, M1085) were not searched and could hold a contemporary decipherment.

## Escalation

- Ask AHGE-SRE for images of leg. 507, exp. 6 (this telegram, the 16 April original, the two key lists, the consuls' complaints and the Lobo telegrams).

## Files

- `transcription.txt` (readings used, doubts marked), `transcription_pass1.txt`, `transcription_pass2.txt`
- `key.tsv`, `decrypt.py`, `decryption.txt`, `reading.md`, `translation.md`, `profile.json`
- `work/PLAN.md`, `work/PLAN.sha256`, `work/scripts/` (solver, controls, keyword test), `work/runs/` (every seed and score; `keyword_test.json`)
- `review/` (the independent reviewer's blind transcription, solution and solver)
- `SHA256SUMS` (paths relative to this folder)
