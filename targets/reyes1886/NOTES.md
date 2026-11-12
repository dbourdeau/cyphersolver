# reyes1886: Bernardo Reyes to Ignacio Revueltas, Monterrey, 1 April 1886 (catalogue 1447)

Read in part (strict share 5 of 12 cipher words, 41.7%), 12 Nov 2026. Written up on the site (reyes1886.html) at the
integration of PR #472.

## Document

- CEHM-Carso, Fondo DLI (Archivo del General Bernardo Reyes), DLI.4.634.1, one page. Record:
  https://www.cehm.org.mx/Buscador/FichaBasica/113807?Tipo=A. Image (open, no login):
  http://visor.cehm.org.mx/assets/docx/fondos/jzd/DLI/4/634/1/DLI.4.634.1.0001.jpg (fetched 12 Nov 2026; not in git).
- A letter in clear Spanish with ten short cipher runs (68 two-digit groups, 12 words). The CEHM summary ("Informa que
  Garza Galán y Cervantes tienden a reconciliarse. Desconfía de políticos. [La mitad del texto cifrado]") overstates
  the cipher share: only the key words of one passage are in cipher, and the clear text already carries the
  reconciliation news. The cipher words are the ones the summary does not give: what Reyes really thinks of
  Garza Galán.

## System

The War Ministry key used between Reyes and Revueltas (War Ministry, Mexico City) in Dec 1885 - Apr
1886: a simple homophonic substitution, one two-digit group per letter, one to three groups per letter
(a 17 47 87; e 13 43 83; i 19 49 89; o 21 31 61; n 23? 33 63; r 57 77 97; t 56 76 96 ...), word division kept by the
clear words between runs, groups joined by hyphens. Not the "clave del Sr. Presidente" (four-digit code with
three-digit groups), which Reyes used for telegrams from Dec 1885 (DLI.3.454.1; DLI.3.455.1 page 2 and DLI.3.525.1
are in that system and were not used). Not the "nuevo cuadro de cifras" Revueltas sent on 16 Mar 1886
(DLI.4.623.1): on the back of that letter Reyes answers that he has lately used the old key ("he usado últimamente
la clave antigua") because of the distance from the capital, and the old two-digit key is what 634.1 uses.

## Key source and held-out tests

- Key pairs: DLI.3.524.1, Revueltas to Reyes, Mexico City, 9 Dec 1885, "Carta cifrada y traducción": the cipher
  letter (page 1, top of page 2) and the contemporary translation on page 2. Images:
  http://visor.cehm.org.mx/assets/docx/fondos/jzd/DLI/3/524/1/DLI.3.524.1.0001.jpg and `.0002.jpg`.
  `transcription_524.txt` aligns each cipher run with the translation's words; `decryption_524.txt`
  (`scripts/decrypt_524.py`) decrypts every row with the frozen key beside the translation's words. 245 letter pairs from 25 rows give 41
  groups (`key.tsv`); no group has two values. Rows tagged `!` were left out because they do not align one group to
  one letter: the silent h of "ha" not enciphered, "posib(l)e" with a letter dropped, "armada" (in the cipher, not in
  the translation), "dirija" (84 where i is expected), "bueno" enciphered with the c group 16, and the bottom line cut
  by the scan. The right edge of page 1 is cut by the scan; groups lost there are `??`.
- Frozen: `key_frozen.tsv` (= key.tsv, sha256 in FROZEN.sha256), built from 524.1 only.
- Test 1 (inside 524.1, `scripts/heldout.py`): key built from rows 1-15 only, applied to rows 16-31 and graded
  against the contemporary translation: 99 of 114 letters right (0.868), 0 wrong, 15 letters on groups the
  training half had not seen. On groups it knew: 99/99.
- Test 2 (target): the frozen key covers 60 of the 68 groups of 634.1 (0.882); 8 groups (7 kinds: 12, 20, 23, 40,
  53, 65, 82 twice) do not occur in 524.1. 634.1 has no contemporary decipherment, so this is coverage, not accuracy.
- Order of work, stated plainly: the 634.1 runs were transcribed (pass 1) and tentatively read from the clear
  context before the sibling was fetched (the words fit the surrounding sentence almost uniquely). The key was then
  built from 524.1 alone. The frozen key's mechanical output agrees with that earlier context reading in all 60
  covered groups; this is an agreement check, not a blind test.

## Reading

Mechanical decryption (`decryption_634.txt`, `scripts/decrypt.py` with key_frozen.tsv):
`pro[53]e[82]oso | suvia[40]e | ca[20]ital | miedo | rn[12]ero | pendie[23]te | conducta | di[82]ose[65]or | dejar | eso`.

Reading (`reading_634.md`, marks checked by `scripts/check_marks.py`, which passes): provechoso, su viaje, capital,
miedo, r{+a}nchero, pendiente, conducta, dicho señor, dejar, eso. The fills are v (53), ch (82, twice, same value in
both places), j (40), p (20), ch (12), n (23), ñ (65). 20 p and 23 n share the final digit with the known p (30, 60)
and n (33, 63) groups, as the homophones of a, e, i do; 12 and 82 share theirs. In R5 the writer left out the a of
"ranchero" (77 = r is firm in 524.1); Revueltas's letter of 24 Mar 1886 (DLI.4.630.1) asks Reyes not to drop letters
in his cipher. Before R5 the writer struck out a clear word (probably "canalla") and put the cipher word instead.

Passage: "... y esto me ha dado idea de lo **provechoso** que fué **su viaje** á la **capital**, y me he felicitado
de que lo haya verificado; pero de todos modos, como yo le tengo mas **miedo** á un **ranchero** que á un politico,
estaré **pendiente** de la **conducta** de **dicho señor** sin **dejar** por **eso** de estrechar como he
estrechado nuestras relaciones." ("... how useful his journey to the capital was ... but since I fear a rancher more
than a politician, I shall keep watch on the conduct of that gentleman, without ceasing for that reason to draw our
relations closer.")

Word counts (cipher words): 12; 5 verbatim from the signs (su, miedo, conducta, dejar, eso); 7 with letters
filled from context on groups not in the frozen key (eight groups, two of them in provechoso: provechoso, viaje, capital, ranchero, pendiente, dicho,
señor), one of them (ranchero) also with an added letter; 0 holes; 0 from a gloss. The clear text (about 115 words)
is read from the image; in the reading the abbreviations Sr, Gral and compº are written out and the struck word is
left out.

Dan's reading checker (`docs/_check_reading.py --file`, origin/main of 12 Nov 2026): reading_634.md clean share
0.722 (18 sentences, 13 clean, shape reading); the Spanish letter section alone 0.818 (11 sentences, 9 clean; the
holes are names and word-list gaps: Monterey, 1º/86, Garza, tienden); translation_634.md 0.765;
decryption_634.txt 0.0 (one unspaced line of runs, not a reading).

State: **not prose** (after the independent review of 12 Nov 2026; target class stays **read in part**). The
cipher is 10 runs of one or two words each (12 words, 68 groups) set into a letter written in clear Spanish; the runs
form no sentence of their own, and the sentence is carried by the clear text. This is the shape of ralamb1657
(images 104 and 114), where short runs inside clear letters are marked not prose. The runs are given with our decode
with key_frozen.tsv and an English gloss. Every cipher word is identified, but 7 of the 12 rest on one context-filled
letter each (41.7% verbatim from the signs).

## Review

An independent AI language-model agent (blind review, 12 Nov 2026) cropped five cipher lines of DLI.4.634.1 from the
image before opening the transcription: 50 of the 68 groups checked, all agree with `transcription_634.txt` (the 13
of `78-13-65` has an open-topped 3 and was read as 13 by both). It also checked the first three lines and one row of
DLI.3.524.1 page 1 against `transcription_524.txt`, reproduced `FROZEN.sha256`, `check_marks.py`, `decrypt.py` and the
held-out test (99/114, 0 wrong), and read the letter with the runs in place as one coherent passage. It made no
correction to the signs or the reading. Grade B: the reading holds, but 7 of the 12 words rest on one context-filled
letter each, and ranchero also has a restored a (the weakest word: two departures, 12 = ch from context and the
dropped a). It set the text to not prose rather than read in part, on the ralamb1657 rule.

## Integration check (12 Nov 2026)

Done by the integrating session. Reproduced: FROZEN.sha256 matches key_frozen.tsv; check_marks.py passes; heldout.py gives
99 of 114 on test 1 (0 wrong, 15 letters on groups the training half had not seen) and 60 of 68 groups covered on 634.1.
Rows of transcription_524.txt checked against the contemporary translation by hand (row 1, particular =
30 17 77 76 19 16 74 68 87 57). The image of DLI.4.634.1 was fetched from the CEHM viewer (no host refused); the
transcription agrees with the page.
**New test, not in the PR.** The two translated telegrams in this key that the contributor listed and did not use were
fetched and read with key_frozen.tsv unchanged (my own transcription of the numbers, which carry overlines on the page):
DLI.4.631.1 (24 Mar 1886, "Clave antigua", translation "Por correo de hoy escribo á Ud extensamente sobre asunto
relativo á colocación del Sr. Lozano"): 47 letters right, 0 wrong, 14 on groups not in the key. DLI.3.416.1 (28 Oct 1885,
"debe decir á la autoridad legal y legítimamente constituída"): 44 right, 0 wrong, 5 not in the key. Together 91 right,
0 wrong, 19 unknown. They also give 23 = n (twice) and 65 = ñ, two of the seven context-only groups of 634.1, so five
remain on context alone (12, 20, 40, 53, 82); the other new values (for example 24 = m, 28 = l, 95 = t) are not used here.
Strict share: the read bar counts a group valued by the sense alone as not read, so the 7 words with such letters
(eight groups) count as not read: 5 of 12 = 41.7%; the profile's earlier fraction_read of 1.0 is replaced by 0.417. The state
"not prose" for the runs stands (the sentence is carried by the clear text), as for ralamb1657.
Not checked: the full set of signs of 524.1 against its image (only the first rows); the order of events (the first
context reading before the key) rests on the contributor's record.

## Remaining gaps

- Groups 12, 20, 40, 53, 82 - blocker: open-codes; values from context only (ch, p, j, v, ch). 23 = n and 65 = ñ were
  first on this list; the integration check confirmed them on DLI.4.631.1 and DLI.3.416.1 (above). More "cifrada y
  traducción" letters of the channel (Dec 1885 - Apr 1886) in Fondo DLI would confirm the rest. The fondo's other
  cipher items found in the sweep list (Díaz letters) are in the President's key.
- "r{+a}nchero", the weakest word (raised by the reviewer) - blocker: open-codes; two departures, the writer's
  dropped a and 12 = ch from context. It fits the struck clear word and the "than a politician" contrast.
- The struck clear word before R5 ("canalla"?) - blocker: illegible; struck through by the writer, nothing else
  decides it.
- 524.1, right edge of page 1 - blocker: needs-physical-access; cut by the scan, a few groups there and the last
  line are lost (rows tagged in `transcription_524.txt`).

Not reading gaps (clear text or checks, not cipher): the closing formula after "Sabe Ud." is clear text and left
abbreviated; no full blind second transcription has been made (the independent review checked 50 of 68 groups and the
integration check compared the page) and no human palaeographer checked the text.

## Escalation

- [x] siblings: DLI.3.455.1, 3.524.1, 3.525.1, 4.623.1 and 4.630.1 opened; 524.1 gave the key; 455.1 p. 2 and 525.1
  are in the President's four-digit code; 623.1 is the new table of 16 Mar 1886, which Reyes says he did not use.
- [x] clear-pages: the "Traducción" on 524.1 p. 2 used for the key and the held-out test; 634.1 has no decipherment.
- [x] known-keys: DLI.3.416.1 and DLI.4.631.1 (same key, with contemporary translations) opened at the integration check and decrypted with the frozen key: 91 right, 0 wrong; they confirm 23 = n and 65 = ñ.
- [x] print: four web searches in all (two by the contributor, two at the integration check, 12 Nov 2026: Reyes/Revueltas clave cifrada 1886 edition; Narváez on Mexican cryptography with Reyes, Garza Galán, Cervantes) and the catalogue's own check: only Narváez's 2019 SRE book and articles in general and Ríos Vázquez's thesis on Porfirian espionage turned up, none naming this letter. Narváez 2019 and the thesis were not opened; the Reyes papers' own printed edition, if any, was not found.
- [x] key-rebuild: the seven groups not in the frozen key filled from the clear text around the runs; 82 = ch holds
  at both of its places.
- [x] retry: every run decrypted again with the frozen key and the context values; `scripts/check_marks.py` passes.

## Prior art (checked 12 Nov 2026)

Two web searches (Reyes Revueltas 1886 carta cifrada Garza Galán Cervantes; Reyes clave Ministerio de Guerra
1885 descifrado) found only general work on Reyes in Nuevo León and on Porfirian espionage (e.g. Ríos Vázquez in
Estudios de Historia Moderna y Contemporánea de México); no edition or decipherment of this letter. The catalogue's
own note (28 Oct 2026: known.py, Narváez articles) found none. The repository's 29 Oct 2026 note
(research/dudout_2026-10-29/CORRECTIONS-FOR-DANIEL-2026-10-29.txt, agent reyes-1909) had already identified the cipher
as the War Ministry's "clave antigua" and listed DLI.3.416.1, DLI.3.524.1 and DLI.4.631.1 as translated letters in it;
it did not decipher 634.1. The CEHM record gives only the two-line summary.
Catalogue entry 1448 (#245, PR #308, López Portillo to Reyes, 1909) is a different letter and key.

## Collision check

12 Nov 2026: origin/main (0b5d5d8c0) has no target folder for DLI.4.634.1, Reyes/Revueltas or catalogue 1447
(mentions only in research/latam_mexico, Dan's own sweep); no open PR or issue names them. Repeated before
finishing (see the final report).

## Statistical validation

`docs/_validate.py` on `validation.tsv` (`scripts/mk_validation.py`: the 245 usable key pairs of 524.1 with the
contemporary translation's letters, plus the 68 groups of 634.1 as read; 634.1 alone, 71 letters, is too short for
the test): 313 tokens, 48 types, es-modern: reading -1.714 per letter, random keys -6.835 (z 9.0), key annealed onto
the shuffled text at best -2.891 (z 8.8). Verdict: pass. Most of the tokens are the key source's, so this mainly
confirms the key against the contemporary translation.

## Method note

Signs transcribed twice from the image (pass 1 at 1x, pass 2 from fresh 2x crops), reconciled in
`transcription_634.txt` (68/68 agree). Work by AI language-model agents for WAINUT; no target-specific human
intervention.
