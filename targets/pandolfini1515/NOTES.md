# pandolfini1515: Francesco Pandolfini to the Otto di Pratica, Vercelli, 6 and 8 Sept 1515 (ASF MAP CXXXVII doc. 666), read in part with Brice Dudout's key v6

Status: **read in part** (12 Nov 2026; independent blind review 12 Nov 2026: read in part, grade B). Catalogue **2393** (lead and vetting by Daniel Bourdeau, 6 Nov 2026). The key is
**Brice Dudout's key v6** of `targets/pandolfini1514` (Pandolfini's 1514-15 French embassy cipher, rebuilt from the
MAP LXXII pairs), applied here unchanged to a letter of September 1515: the same system and the same key. This target
is proposed as its own folder because the letter is in a different filza and year; the credit for the key is Dudout's.
Contributed by WAINUT (AI language-model agents). No ASF image or derivative is included.

## Document

Archivio di Stato di Firenze, Mediceo avanti il Principato, filza CXXXVII, doc. 666, cc. 674r-674 bis v (MAP images
133979-133982; IIIF `https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/00100137/A0001463.ptif`
to `A0001466.ptif`; 1392 px on c. 674r, 1272 px on the others, the server maximum). A contemporary copy: "Copia della
l(ette)ra del mag.co or(ato)re Franc.o Pandolphini a S(ignori) Otto di pratica", dated in clear "die vj septembris 1515
in Vercelli", with a clear postscript "Tenuta a dì viij" (8 Sept) and a further cipher postscript after "Suggellando la
presente ho hauto lettere". The last page (674 bis v) also carries a short clear note to Lorenzo de' Medici and his
address. 50 cipher lines in six blocks: 674r 19 (one of them inserted at the foot, keyed by the mark 0/10), 674v 13,
674 bis r 10, 674 bis v 8.

## System and key

Consonant signs with the vowel as a superscript figure (1-5 = u, o, i, e, a), bare vowel signs (3 = a, W = i, O = o,
Q = e, p = u), doubling by a double bar (t#, n#, c#, δ#; H = ll), word signs (F et, M non, α per, D che, D^n con,
B ancora, T^m Sua Maestà, T^0 secondo, qu più) and numbers between points: 22 occurrences of 5 distinct groups in this
letter (.4. Cristianissimo 10, .20. Svizeri 7, .2. papa 3, .15. 1, .22. 1; .15. and .22. are not in v6).
This is the system Dudout describes for 1514-15. `key_frozen.tsv` is his `key_v6.json` (origin/main) converted to rows,
with three shape aliases (our H = his 4#, δ = his G, δ# = his G#), frozen before any reading of this letter
(SHA-256 8cdd0da0...; 92 lines = 2 comment lines + 90 entries: 5 vowel, 33 base, 38 token, 9 code, 2 null, 3 alias).
`key.tsv` (92 lines = 1 comment line + 91 entries) adds one sign, Φ = x (a larger looped φ, read from context in "lo exercito" twice and in
"expedita"). Nothing else was added.

Seen in this letter and kept out of the key (marked as repairs in the reading): J (ʃ) reads s in "assente" (r04, v13)
but f in "offerte" (r13); 2 reads b as well as c (Bufaloro, Biagrasso, Binasco, bon, bastardo), as Dudout's v5a
alternative says; bare 5 reads h in "havendo" (b02), his "5 nu = h" alternative; superscripts are often written one
sign off; a bare 4 in v10 stands for .4. without points.

## Held-out test

No line of this letter was used to build v6, so the whole letter is held out. `scripts/heldout.py` decrypts the
transcription with the frozen key and with five control keys whose consonant values are shuffled, and scores each with
Dan's `docs/_check_reading.py --file` (unspaced), re-run on the final files and scripts (12 Nov 2026, origin/main
65cdcd9d5): frozen key coverage **0.820**, clean share 0.925; controls coverage **0.629-0.685**, clean share
0.702-0.848 (`work/heldout_result.txt`). An earlier run with a decoder that still dropped the sign d together with the
block-end marks gave 0.813 against 0.629-0.678; the independent reviewer, with three further controls (seed 777),
measured 0.819 against 0.589-0.691. The unspaced clean share is lenient (the controls score high on it), so the
coverage gap is the number that counts. In the reading, 592 of 771 words (76.8%) are read verbatim from the decryption.

Content check against the clear parts of the same letter (two passages compared): the cipher of 674v lists the terms of the Gallarate agreement
(a state of thirty or forty thousand francs of rent for the Duke of Milan, a pension, a hundred lances, a wife of the
King's blood; money for the Swiss in instalments over six years, a yearly pension, Swiss kept in the King's pay), which
the clear text of 674 bis r sums up ("un milione d'oro ... et ha sua M.tà obligho di havere a tenere ... di loro sempre a
soldo suo"; the sum in the cipher is a conjecture, [?novecento] mila, and stays doubtful against the clear "un milione"); the cipher of 674 bis v ("lo accordo era concluso tra Maestà et li Svizeri") matches the clear postscript of
674v ("fu concluso lo accordo fra il X.mo et li Suizeri"). Names that come out of the decryption and fit place and date:
Bufalora, Abbiategrasso (Biagrasso), San Cristoforo by Porta Ticinese in Milan, Gallarate, the Duke of Savoy, the Bastard
of Savoy, Lautrec, "il generale che fu di Milano" (identified by the contributor as Sebastiano Ferrier, from the clear of 674v), the Duke of Guelders,
Binasco, Lodi, Parma and Piacenza.

## Transcription

Two passes. Pass 1 of 674r was made from 2x strips (`scripts/strips.py`) before any decoding. The key was then tested on
it (as the triage asked), so pass 1 of 674v and 674 bis and all of pass 2 were made by an agent that knew the key:
**not blind**. Pass 2 re-read every line from fresh 2.5x strips with a different framing and changed 19 places, each
settled on the strip: r03 6^5 6 r^5 8^2 (passato); r04 6^2 6 (posso), 3^5, δ bare, 5^2 c 8^2 (molto),
9^5 d 5^3 3 J r^4 (trovarmi assente); r05 6^2 (campo), d 5^5 (Parma); r07 9^5 9^5 (trovava); r10 6^2 d (Porta);
r12 x^2 (populo); r16 and b06 Φ (exercito); r18 6^2 (campo), 6 6^2 6 8^5 (resposta); v04 t# (sottoscripte);
b01 and b03 r^5 (impresa); b02 Q Φ 6^4 (expedita). Files: `transcription_666_pass1.txt` (all pages; also per page
`_pass1_r`, `_pass1_v`, `_pass1_b`), `transcription_666_pass2.txt`, reconciled `transcription_666.txt`
(SHA-256 2eb2358f3148... now; f1b4864fab72... before the two review changes below; 1346784c... before the block-end
marks were renamed END, token content unchanged). 1974 tokens, 45 distinct base shapes.

## Reading (`reading_666.md`, `translation_666.md`)

Words 771: 592 verbatim, 137 with a marked repair (mostly a superscript one sign off, or 2 = b), 15 conjectural,
27 holes (counted one each; by length the holes hide about 41 words). Read as sense 94.6%, under the 95% rule: read in
part. `scripts/check_marks.py` rebuilds the decryption and passes (every departure marked). Dan's checker:
`reading_666.md` as written (with the marks) clean share 0.681 (64 of 94 sentences); the same reading with the marks
resolved to the read side, conjectures left out (`work/reading_666_readside.txt`), 0.734 (47 of 64 sentences, coverage
0.961). The reviewer's own resolution (conjectures kept as words) gave 0.797.

Content: Pandolfini, at Vercelli with the pope's orator, will do what the pope's orator does, who
will not go on to the King until the pope changes his resolution. He is away from the camp; news is better had by way of
Parma and Piacenza. The French camp had been four or five miles from Bufalora and was said to be heading for
Abbiategrasso; troops of Milan quartered at San Cristoforo by Porta Ticinese went back; Milanese envoys came to the King
at Bufalora with great offers and victuals, and since the hoped-for goodwill of the Milanese did not show, the King is
surprised and angry. The Swiss army is not far from Gallarate; yesterday the Duke of Savoy, now declared for France, went
with the Bastard of Savoy, Lautrec and "the general who was of Milan" (identified by the contributor as Ferrier) to the Swiss camp for the answer on the agreement. The terms
follow (674v). Then (674 bis r): the enterprise of Milan is as good as done; with [15] and the Swiss on his side the King
may try Naples this year; he keeps the [22] in his pay six more months; the Duke of Milan has been offered terms, will not
accept, and may end a prisoner. Postscript (674 bis v): the Duke of Guelders has arrived; a friend writes from Binasco
that the agreement was concluded, that the Spaniards who meant to join the Swiss have left, and that the French camp was
moving towards Lodi; Pandolfini and the pope's orator are without safe-conduct.

## Independent review (12 Nov 2026)

A blind reviewer (an AI language-model agent that took no part in the solution) read the folder and the images:
state **read in part**, grade **B**. Sign spot-check on the images before opening the transcription: four cipher lines,
about 150 signs (674r r08 and r13, 674 bis r b02 and b08); base shapes agree in about 95% of signs; the reviewer found no
case of an invented sign and confirmed one pass-2 change made after the key was known (r10 "6^2 d", Porta). The
reviewer re-ran `check_marks.py` and `decrypt.py` (identical output) and confirmed that `key_frozen.tsv` is what
`make_key.py` builds from `targets/pandolfini1514/key_v6.json`. About 24 sentences read against the translation: 21
coherent with at most about one hole in ten words; three passages not clean (v01-v02, v08-v09, b03-b06).

The reviewer read five signs differently. Each was checked again on the 2.5x strips:

- r13, the second of "J J" in "offerte": the reviewer reads p. On the strip it has a closed loop at the top, like p,
  with the bar of the J running into it. Changed to `p?` (doubtful); "offerte" is now a marked repair (`of{u/f}erte`)
  instead of a verbatim word.
- r08, "3^2 2^3" inside the hole of the lord's name: the reviewer reads "2 S". The 3 is clear on the strip, the sign
  after it is not; `2^3` is now marked doubtful (`2^3?`). The hole stays a hole.
- r08, the r^3 after F ("et si dice"): the reviewer reads barred t. On the strip the sign has the flat top of this
  hand's r and no bar through the stem; kept as r^3 (open point below).
- b08, "6^5 d" in "partito": the reviewer reads "6 O?". The strip shows the round d with its ascender turned left;
  kept (open point below).
- b08, the 5^3 before α ("mi persuado"): the reviewer reads 3^3. The strip shows the flat top of a 5, unlike the two
  round 3 signs that follow; kept (open point below).

The `?` marks do not change the decryption (`decrypt.py` drops a trailing `?`). Word counts after the change: 771 =
592 verbatim + 137 marked repair + 15 conjectural + 27 holes.

## Prior work (checked 12 Nov 2026)

Dan's vetting of 6 Nov 2026 (catalogue entry 2393): Desjardins-Canestrini, Négociations II (1861), prints Pandolfini's
letters of 26-27 Aug 1515, not this one; nothing in Tomokiyo or Lasry; Usteri, Marignano (1974) cites the original in
the Otto di Pratica, Responsive filza 12 fol. 274b (not opened). One web search on 12 Nov 2026 (Pandolfini, Vercelli,
September 1515, Otto di Pratica, Gallarate, cifra): nothing on this letter or its cipher. No printed decipherment known.
Collision check 12 Nov 2026 (origin/main, live repository, open and recent PRs, issues): no folder, PR or issue covers
2393; `targets/pandolfini1514` covers only MAP LXXII.

## Remaining gaps

- 27 holes (about 41 words) - blocker: illegible; decoded but no sense found, and the 1392 and 1272 px images are the
  server maximum. The largest: r08 the lord's name, r09 the subject, v02-v03 a clause, v08-v09 the purpose of the Swiss
  pension, b04 the King and the mountains, b06, b08, bv05, bv07.
- Codes .15. and .22. (b02, b05), not in v6 - blocker: open-codes; .15. stands beside "li Svizeri" as the King's ally
  (the Venetians?), .22. is kept in pay six months (Dudout's 1514 guess for .22. is lanzichenech).
- Signs whose value here differs from v6 or is unknown - blocker: open-codes; J s/f, 2 b/c, bare 5 h, F^0, E, B^0, the
  overlined number group in v07; recorded as marked repairs, not added to the key.
- Independent blind transcription - blocker: not-attempted; the transcription is not blind after pass 1 of 674r. The
  reviewer's spot-check (about 150 signs in four lines) is a partial check only.
- Five signs read differently by the reviewer - blocker: illegible; the server-maximum images do not settle them
  (r08 r^3 or barred t; r08 "3^2 2^3" or "2 S"; r13 J or p; b08 d or O; b08 5^3 or 3^3). Two are now marked doubtful,
  three kept after a second look; all five should be settled by a human reader on the images. Superscripts sit between
  signs in several places, so their attachment is a judgment call.
- Heavy context repairs, to be treated as doubtful - blocker: illegible; the decoded signs give no sense as they stand:
  {cidi/Bia}gras{+so} (r08), {narfioa/[?Francia]} (r17), {nvecot/[?novecento]} (v07; the clear says "un milione d'oro").
- The original in the Otto di Pratica (Responsive, filza 12 fol. 274b) - blocker: needs-physical-access; not known to
  be digitised; it may carry a decipherment of the time.

## Escalation

- [x] siblings: Dudout's pandolfini1514 (MAP LXXII, same writer and system) gave the key; neighbours 665 and 667 are not a decipherment (Dan's vetting, 6 Nov 2026)
- [x] clear-pages: the clear passages and postscripts of 666 itself were read; they are not a decipherment, and two of them were compared with the cipher (Held-out test)
- [ ] known-keys: only v6 was applied; Dudout's earlier v3 and v4 were not tried separately
- [ ] print: Desjardins-Canestrini II, Tomokiyo and Lasry (Dan's vetting) and one web search; Usteri, Marignano (1974) not opened
- [ ] key-rebuild: one sign added (Φ = x); .15., .22. and the signs with other values not rebuilt
- [ ] retry: the holes were not retried with an extended key
