# Ferdinand III <-> Cardinal-Infante Ferdinand (1634, 1635, 1640) — tracker item #16

Status: written up 9 Oct 2026 (docs/ferdinand3.html). Split outcome (profile outcome.parts):
- R1889 (16 Nov 1635): key recovered based on adjacent plaintext (the draft R954), complete: 450/463 tokens (97.2%)
  give the draft's letter, the rest copy slips.
- R1890 (22 Feb 1640): key recovered from ciphertext-only (on top of the R1889 alphabet), complete: 782/782 tokens
  assigned, 3 copy slips, one obscured sign.
- R1887 (28 Oct 1634): key recovered based on adjacent plaintext (the letter's own clear "promovere haud dedignetur"
  as crib) + annealing and context, partial: 88.4% of tokens read as sense (93.9% with conjectures); a 6-token word
  and a 16-token span open (open-codes), still open after a last dictionary + LM attempt (work/gap1887.py).
Prior solution: Andrew Aymeloglu (github.com/aaymeloglu/unsolved-ciphers, 18-23 Sept 2026; Tomokiyo's list "Two of
Three Solved"); see "Prior work and what was independent" below.

Brussels, Algemeen Rijksarchief, Secrétairerie d'État allemande, inv. 540. DECODE R1887 (28 Oct 1634, old style:
graphic symbols + three-letter codes), R1889 (16 Nov 1635) and R1890 (22 Feb 1640) (new cipher: two-digit codes
+ letters). Latin cleartext.

Skipped 2026-09-15: all three DECODE records are "Access mode: Authentication required" (images and transcriptions),
and the Brussels archive is not online. No ciphertext obtainable → cannot be attempted without a DECODE account.

## 9 Oct 2026: access restored (DECODE cookie)
- Fetched all 8 images to `img/` (git-ignored): R1887 4 pp. (I9345-9348), R1889 2 pp. (I9350-51), R1890 2 pp. (I9352-53).
- DECODE transcriptions (transcriber "XZ", Jan 2021) exist for R1889 (DOC_R1889_D3605) and R1890 (DOC_R1890_D3604),
  saved in `decode/`. None for R1887. Record status on DECODE: "Non-decrypted".
- R1886 and R1888 record pages return empty (no record); R1885 = Sercambi chronicle, R1891 = Croiset 1798 codebook,
  R1892 = KHA Willem V. No key record in the neighbourhood.
- R1889 is Cardinal-Infante -> Ferdinand (King of Hungary), Brussels 16 Nov 1635 (DECODE catalog name has it right);
  R1890 is Ferdinand III (as Emperor) -> Cardinal-Infante, Vienna 22 Feb 1640.

## Prior-solution check (9 Oct 2026)
- Schmeh Top 50 #27 "Ferdinand III's encrypted letters" (Klausis Krypto Kolumne, 7 July 2017) is a DIFFERENT pair of
  letters: Ferdinand III to his brother Archduke Leopold Wilhelm, 20 July 1640 (copy from Prof. Leopold Auer, Vienna)
  and a 1641 letter from Hildegard Ernst's 1996 chapter. Thomas Ernst solved those (blog post 7 Oct 2017,
  "Zifra Piccolominea": number pairs, non-numeric signs = their stroke counts, vowels from AEIOU; key A 00/01/11,
  E 02/12, I 03/13, O 04/14, Z 10, B 20, P 21, F 22, L 23, R 24, K 30, H 31, G 32, M 33, S 34, T 40/41, C 42, N 43, U 44).
  Nothing in that post or its comments mentions Brussels, the Cardinal-Infante or DECODE R1887-R1890.
  **So `research/top50/NOTES.md` line ~37 ("Ferdinand III ... found-solved") is wrong for this target**: the
  Brussels letters are not the Top 50 letters. (Correction for research/top50, not made here: outside this folder.)
- Ernst's Piccolomini key does not fit R1889/R1890: their numbers run 02-54 (R1890) and 0-39 (R1889), mixed with
  single letters and (R1890) letter groups (pli, op, hi, tis ...). Different system.
- Literature lead: Hildegard Ernst, "Geheimschriften im diplomatischen Briefverkehr zwischen Wien, Madrid und
  Brüssel 1635-1642", MIÖG 100 (1992): exactly this correspondence; may print the keys.
- A reading published by others exists: github.com/aaymeloglu/unsolved-ciphers, folders ferdinand-1634/ and
  ferdinand-1635-1640/ (Sept 2026). Not opened before the ciphertext-only attempt below.

## Ciphertext-only attempt, R1890 (9 Oct 2026)
- Parsed DECODE's transcription (work/parse1890.py): 786 cipher tokens, 107 types (two-digit numbers 02-54, single
  letters, letter groups pla/ple/pli/plo/plu, ap/ep/ip/op/up, ca/ce/ci/co/cu, ha/he/hi/hu, tis/tes/tus/tos ...).
- Repeats: "hi 41 x pli 21 47" / "18 41 x pli 21 46" / "hi 41 x pli 21 46" (46~47 homophones?); "ip c up 43/42/44",
  "ga 14 me 19 hi" / "ga 14 me 18 hi"; "g au 50 plu" twice. Consecutive numbers look like homophone groups.
- work/hsolve.py: numba annealer, symbol->letter, `la` 5-gram (lang) + chi-square letter-frequency term
  (the `la` model alone collapses to "iiii...": it scores 'i'*100 at -1.51/char, better than real Latin at -1.87).
  Control (work/sim.py): synthetic 786-token Latin homophonic text with 108 symbols is recovered 99.7% in 3/16
  restarts at -1454 (-1.85/char).
- R1890: 16 restarts x 4M and 60 restarts x 10M: no convergence; best -1975 (-2.5/char), different gibberish each run.
  Constraint "letter group = its vowel" (pli=i, op=o ...): worse (-2188). So R1890 is not a plain one-symbol-one-letter
  homophonic in Latin as transcribed: nulls, syllable/word codes or a different language are likely.

## The draft R954 (9 Oct 2026)
- R1889's own DECODE record (saved 15 Sept, `decode_1889.html`) already says "seems to correspond to a draft with
  the same date" and points to R954, 1887, 1890; R954 points back. R954 = ARA Brus SEA inv. 540, 16 Nov 1635,
  "Draft by Cardinal-Infant Ferdinand", status "Decrypted": the right column is the full Latin draft with the
  passages to be enciphered underlined; the left margin holds the secretary's encipherment with plaintext glosses.
  Images fetched (`img/IMG_R954_I4976_P1.png`, `..._I4977_P2.png`, 1616x2309). (We were pointed to R954 again by
  the aaymeloglu SOURCES.md, read after the failed R1890 run; the pointer itself is on our own saved DECODE pages.)
- This is adjacent plaintext for R1889: the key is recovered by aligning the draft's underlined text with R1889's
  cipher (work/align1889.py).

## R1889 key recovered from the draft (9 Oct 2026)
- work/align1889.txt: all 74 cipher words of R1889 (463 tokens) aligned one-to-one with the draft's underlined
  text (my transcription of R954 from the images). Token splits checked on the R1889 image where DECODE's spacing
  was ambiguous: "04 10" is `0 4` (ad) + `10` (h of hyberna); "2000m" is `20 c 0 m` (prae-); "37731" in civitas is
  `37 7 31` with an arc under 7 3 1; "71" in archiepiscopatu is `7 1`; "52" in difficulter is `5 2`;
  "i u" in hiberna (p.2) is `1 11`; "0 9" = ab; "3 9" in "ex" = 39.
- Key (work/key1889.json; majority vote, counts in align1889.py output):
  a 0 n t z | b 8 9 | c 7 x | d 3 4 | e 6 m p | f 2 5 | g 16 17 | h 1 10 | i(y) 11 12 15 24 h | l 18 19 | m d e (6) |
  n 22 32 | o a f l | p 20 g | q 30 33 | r c i q | s 25 26 31 | t 34 37 | u(v) 23 35 38 y | x 39.
  Letters and numbers are both cipher symbols; "." marks word ends (not always). Doubled letters written double.
- work/measure1889.py: 450/463 tokens (97.2%) give the draft's letter under the majority key; 62/74 words exact.
  The 13 deviations: `6` stands for m four times (iam, praesidium, tum, militi) and for e eight times, so 6 is
  e/m (two values or a copy slip by the same hand); `m` = m once (regium); `7` = a (civitas) and = u (locisque);
  `9` = p (provisum; elsewhere b); `2` = n (concedi; elsewhere f); 'civitate' written `7 15 23 z 34 m` (civate, "it"
  omitted); "prinncipis" doubled n; "hctenus" without a. All are in words whose reading the draft fixes.
- Plaintext of the enciphered passages (draft wording; copy differences noted above):
  "Ad hyberna vero quod attinet, [quae Regia Dig.tas ac Dil.o vra] pro iam dicto exercitu Caesareo in
  Archiepiscopatu ac Civitate Treuirensi fieri desiderat. ... Verum cum civitas Treuirensis iam inde a ducentis
  annis sub [Regiae suae Cat.cae Maiestatis] stet protectione atque [eo nomine] ab eius milite [semper quando id
  necessitas postulavit] fuerit praesidio munita, [uti etiam fuit cum] Gallus vexilla regia superans eandem
  occuparet; [Conveniens esse arbitror, ut] praesidium hoc regium in dicta civitate locisque circumiacentibus
  [conservetur, ex quibus] sumet alimenta necessaria [tum ad] sui ipsius uti convenit, tum principis electoris
  (cui hactenus ex aerario [Regiae suae Cat.cae Maiestatis] provisum fuit) sustentationem. [...] [quod] militi
  Caesareo in dictis locis difficulter hiberna concedi possint, [aeque boni laturam]."
  Sense: the Cardinal-Infante refuses imperial winter quarters in the archbishopric and city of Trier, which has
  been under Spanish protection and garrison for two hundred years (since the French took it), and asks that the
  Spanish garrison keep the town and its surroundings for its own and the Elector's upkeep.

## R1890 syllabary recovered from the ciphertext (9 Oct 2026)
- R1889's letter key applied unchanged covers 424 of 784 R1890 tokens (work/dec1890.py); the rest are numbers 14,
  21, 36, 40-54 and letter groups.
- Free-value annealing (work/syl1890.py: each unknown symbol -> letter/bigram/trigram, `la` model) pointed at
  48=no, 51=re, 53=ro, 54=ru, 41=le, 42=li: numbers in vowel series. Hypothesis: every extra symbol is one
  consonant + a vowel in AEIOU order, the vowel shown openly in the letter groups.
- work/fam1890.py: one consonant (or cluster) + orientation per family, other symbols free; 40 restarts x 80k.
  All top restarts converge on the same solution (-2061):
  40-44 = la le li lo lu; 45-49 = na ne ni no nu; 50-54 = ra re ri ro ru; pla..plu = ta te ti to tu;
  ap..up = ca ce ci co cu; ca..cu = ma me mi mo mu; ha..hu = da de di do du; tas/tes/tis/tos/tus = ba be bi bo bu;
  an..un = sa se si so su; au/eu/ou = pa pe po (pu); me/mi/mu = fe fi fu; ga/gi = a i (bare vowel?); at/et/ot = ga ge go.
  Free: 21=o, 36=x, b=m, o=a, 14=c?, fu=f?, ko=si?, li=i?, lx=c?.
  Decrypt opens "communicabit Dilectioni Vestrae orator Serenissimi Regis Catholici marchio Castagneti ea quae
  circa novum apparatum militis in circulo Westphalico ab electore Coloniae et statibus illius circuli inceptum ..."
  So the 1640 key = the 1635 alphabet + a 15x... syllable table, recovered here without outside material.
- Completed by context (9 Oct): g-family = h (ga=ha: habere, hactenus, hac, Hatzfeldius; gi=hi: marchio);
  ?t = g+v (it=gi regis/iniungimus, et=ge indigeat, ot=go negotium); uu=pu (publici); tos=bo (boni);
  ko=do (domus), fu=mu (comunicabit), lx=oc (occurrat), li=xi (existentium), 14=tz? (Ha-14-feldius, twice;
  value from the name only). DECODE's uncertain "l/z?" is z (=a) in all 7 places (ea quae, praeiudicium,
  nostrae, debeat, custodiae, praeter, aut); "c/1? o/0?" is the group `co` (=mo: admovere, image checked);
  "pla/u?" is plu (contulimus); "g^.a" is the group ga (Westphalico).
- Result: all 782 tokens assigned (work/key1890_extra.json + key1889.json; work/R1890_literal.txt). Literal slips
  of the copy: "igitua" (`t` where r expected, image checked: plain t), "materi" (final a missing), "expredse"
  (3=d where s expected), obscured last sign of line 1 (orato[r]).
- Cross-check made only after this recovery: aaymeloglu/unsolved-ciphers KEY.md (18 Sept 2026) gives the same
  syllabary family for family, the same singleton values, the same l/z->z and c/1o/0->co amendments, and the same
  Latin text. Two independent recoveries agree.

## R1890 reading (Latin, our decryption; word division and ae/v editorial)
Comunicabit Dilectioni Vestrae orato[r] Serenissimi Regis Catolici marchio Castagneti ea quae circa novum apparatum
militis in circulo Westphalico ab electore Coloniae et statibus illius circuli inceptum, ac quae inde in
praeiudicium boni publici et etiam domus nostrae vereamur incommoda, secum fusius contulimus. Cum igitu[r] illud
negotium celeri remedio indigeat, neque alius pro eo occurrat modus quam ut et nos festinanter collectionem
militis, qui in potentiorem numerum quam dictus apparatus se extendat, in illis partibus instituamus, si alias
liberam dispositionem ibidem servare et praecavere velimus ne ille circulus alieno arbitrio subiiciatur,
ordinavimus eapropter quatenus comes Hatzfeldius se confestim Coloniam transferre atque huic operi qua maiore
potest celeritate manum admovere debeat. Deficientibus vero nobis pro eo sumptibus necessariis, petimus a
Dilectione Vestra denuo perinstanter quatenus iis quae sibi praedictus orator in hac materi[a] distinctius
expositurus est omnimodam fidem habere et considerata rei gravitate desideratos hactenus centum mille florenos
Coloniam custodiae nostrorum ibidem existentium commissariorum (quibus expre[s]se iniungimus ne quidquam ex illis
praeter expressum mandatum nostrum aut comitis Hatzfeldii assignationem expendant) consignari curare velit.
(Ambassador = the Spanish envoy, marques de Castaneda; Hatzfeldt = Melchior von Hatzfeldt.)

## R1887 (28 Oct 1634): transcription and key rebuild (9 Oct 2026)
- No DECODE transcription exists. Transcribed here from I9345-I9347 (rotated 90 deg; per-line crops):
  `transcription/R1887.txt` (30 physical lines, labels explained in its header), 474 tokens
  (`transcription/R1887_tokens.txt`, measured: 474 tokens, 119 distinct counting superscript variants).
  Cipher passages: P1 two lines after "cum"; P1 six lines after "facile colligere liceat" running into nine P2
  lines; eleven P2 lines after "Eandem perbenevole rogans"; two P3 lines after "posteritatem debetur gloria".
- System: a different repertoire from 1635/1640. Three-letter groups in vowel series (xar/xer/xir/xur, tas..tus,
  tan..tun, pan..pun, for/fer/fir/fur, sil/sul/sed, lis/les/los/lus), two-letter groups (ob/eb/ib/ub,
  ad/ed/id/od/ud, oc/ic/uc/ec, he/hi/ho/hu, ir/ur), numbers 2-48 and graphic signs (triangle, slashed =, struck
  m/D/f/o, crossed n/a, Z-forms, female sign ...), several with superscript marks.
- First family anneal (work/fam1887.py: one consonant + the shown vowel per family, rest free) collapsed to bare
  vowels (the `la` model's "iiii" weakness); with consonants forced it gave Latin-like but unconverged text.
- Crib: the last cipher passage (P3) is followed by the clear words "promovere haud dedignetur"; the cipher
  `D/ m/ y ob 10 9 ten | o/ != 2 K | he hi b ed xur 16` aligns with exactly these words (+3 trailing signs v/ V f/).
  That fixes ob=mo, ten=re, he=de, hi=di, ed=ne, xur=tu and D/=p, m/=r, y=o, 10=u, 9=e, o/=h, !==a, 2=u, K=d,
  b=g, 16=r, i.e. the families ?b=m+v, t?n=r+v, h?=d+v, ?d=n+v, x?r=t+v.
- With the crib fixed (work/fix1887.json) the anneal converges (all top restarts agree): f?r=c+v, ?c=v+s,
  ?r=f+v, l?s=g+v, t?s=s+v, p?n=l+v, s?l=b+v; signs tt=s, triangle=n, 3/5=q, 43=in, 42=en, a+=i, S=t, n+=c,
  Z=i, Z/=s, f/ and f=m, 4=m (also n, s), 13^9=ll, Z^9=ll (superscript 9 doubles: 13^9 ll, Z^9 ll, n+^9 ct).
  work/key1887.json; `python work/dec1887.py -v` prints every token with its value.
- Reading word by word: work/align1887.txt; measure: work/measure1887.py ->
  474 tokens: ok 324, emend 95, conj 26, open 22, null 7 => **88.4% of tokens read as sense**, 93.9% with
  conjectures.
- Latin (our reading; [..] conjecture, (?) open):
  "Cum communis Augustissimae nostrae domus salutis stabiliendae ratio summopere requirat ... facile colligere
  liceat ipsum nullos [ausus quos] restituendis illis, qui in fidem ac tutelam ipsius se coniecerint, principibus,
  imprimis Wirtenbergico et Durlacensi, profuturos esse crediderit, intermissurum. [Eventus] vero inde (crisdus)
  non minoris emolumenti vel detrimenti rebus Dilectionis Vestrae quam meis [partibus?] sit allaturus. Ideo cum
  quantum in me est subvertendis hisce communis nostrae domus hostium conatibus intendere non desinam, idem illud
  studium in Dil. Vestra excitare maximopere necessarium duxi. Eandem perbenevole rogans ut mediante aliquo, qui
  distractis illorum in diversas partes animis facilius mihi ad peragendum hunc ipsorumque (... 16 tokens ...)
  negotium armorum suorum motu et diversione, commune quod uterque praetendimus praedictae Augustissimae nostrae
  domus commodum, non minor [quam ea] quae ex conflictu Nordlingensi maximo suo merito ipsi apud Seren[issimum]
  ... posteritatem debetur gloria, promovere haud dedignetur."
- Comparison (made after our reading): aaymeloglu ferdinand-1634/README.md + READING.md (23 Sept 2026) have the
  same family values and nearly the same text, with the same open spans (their A05, A13, A15, A30, A35). Where we
  differ: we read `tus y tun f` as *suorum* (they *quorum*), propose *ausus quos* (A05, they leave a??sq?s),
  *eventus* (A13, they leave equnntus), *quam ea* (A35), and confirm on the image that their "probable ib" in
  intermissurum is ib (`ll` in our first pass).

## Last attempt on the two open R1887 pieces (9 Oct 2026, write-up session)
- Crops re-viewed (img/l87 P2_1055b = P2.02, P2_2836b and P2_2972a/b = P2.14-15). The transcription stands:
  `n+ m/ a+ 45 hu tt/`; in the span the second 4 carries a comma (`4,`), `4)` a parenthesis, `h^ga` is h under a
  superscript loop "ga", and the stroke over `S e~` may be the descender of the line above, not an abbreviation mark.
- 45 = s, not ti: in communis (P2.07-08, `for ub Δ^9 a+ | 45`) it can only be s, so the literal word is c-r-i-s-du-s.
- work/gap1887.py: every value each sign takes in the letter (letter groups keep their shown vowel, since the
  families show it openly; 4 in m/n/s/none; the singletons 4), h^ga, e~ any letter), pruned to strings that
  segment into words of the la-gutenberg corpus, ranked by the `la` LM in the sentence context.
  P2.02: 571 segmentable candidates; the best (tres de, credi, crit id, gradus) do not fit "Eventus vero inde ___
  non minoris ... sit allaturus"; no adjective or participle in -us fits the signs.
  P2.14-15: 1,704 candidates, all fragments (min an tiri satis relatum ...). The sentence needs a verb for "qui ...
  facilius mihi ad peragendum hunc ipsorumque ___ negotium" and a masculine noun for "hunc"; nothing in the
  candidate set supplies both.
- Result: both pieces stay open (open-codes). Every sign has a value; the words do not resolve, so either the
  encipherer slipped more than once or a sign value is wrong. Hildegard Ernst, MIOG 100 (1992) may print the 1634 key.

## Prior work and what was independent (exact sequence, 9 Oct 2026)
1. 15 Sept: target skipped (no DECODE access). 30 Sept: the aaymeloglu/unsolved-ciphers repository found in a
   literature search (readings of all three letters, 18-23 Sept 2026); not opened.
2. 9 Oct: images fetched; the ciphertext-only homophonic attack on R1890 run and failed (above), before any of his
   files was opened.
3. After that failed run, his README and SOURCES.md were read. The README says the 1640 letter's additions to the
   1635 alphabet are mostly syllables; SOURCES.md points to the draft R954 (a pointer already on our own saved
   DECODE record pages for R1889). His KEY.md, READING files and ferdinand-1634/ were not opened.
4. R1889 key recovered from R954; R1890 syllabary recovered by the family anneal; R1887 transcribed and its key
   rebuilt from the in-letter crib. So the R1890 work was done knowing that the extra symbols are mostly syllables;
   no value came from his files.
5. Only then his KEY.md, READING-1640.md and ferdinand-1634/README.md + READING.md were compared (agreement and
   differences recorded above).
- research/top50 (Schmeh Top 50 #27, Thomas Ernst 2017) concerns other letters (Ferdinand III to Archduke Leopold
  Wilhelm, 1640/41, Zifra Piccolominea); corrected in research/top50/NOTES.md in the write-up commit.

## Remaining gaps
- R1887 P2.02 `n+ m/ a+ 45 hu tt` (literal crisdus, after "vero inde") - blocker: open-codes; 6 tokens, every sign has a value (45 = s, as in communis) but the word does not resolve; gap1887.py finds no Latin word that fits
- R1887 P2.14-15 `4 ib ad p xir m/ a+ 4 4) xir 4 ten h^ga != S e~` (literal ?minantiri?ti?re?at?, before "negotium") - blocker: open-codes; 16 tokens, 4) h^ga e~ are singletons and 4 is m/n/s; LM span search (work/span1887.py) and the dictionary + LM pass (work/gap1887.py) give only fragments (minatur ... relatum)
- R1887 conjectures "ausus quos", "eventus", "partibus", "quam ea" - blocker: open-codes; singletons ltu, #, v/, 146, X, c/ have no second occurrence
- R1887 trailing signs (V L after "ratio", V + female sign after "ea", v/ V f/ after "dedignetur") - blocker: too-short; read as terminal fillers, no context
- R1890 one obscured sign at the end of p.1 line 1 (orato[r]) - blocker: illegible; right edge dark in the only photograph

## Escalation
- [x] siblings: R953-R955, R1885-R1892 opened; R954 (draft) is the plaintext of R1889; R1886/R1888 do not exist; no 1634 draft or key on DECODE (aaymeloglu report the SEA keys R937-R953 checked, none fits)
- [x] clear-pages: R954 draft used; R1887 has no clear copy; its own clear "promovere haud dedignetur" used as crib
- [x] known-keys: 1635 alphabet and 1640 syllabary tried on R1887 (different repertoire); Ernst's Piccolomini key tried on R1889/R1890 (does not fit)
- [x] print: Schmeh/Ernst 2017 (different letters), Tomokiyo unsolved list, aaymeloglu SOURCES (Lefevre 1934, Lunig 1712); Hildegard Ernst, MIOG 100 (1992) on Vienna-Madrid-Brussels ciphers 1635-1642 not accessible online - may print a key
- [x] key-rebuild: crib-seeded family anneal (fam1887.py) + LM context; span search for the open 16-token span
- [x] retry: all R1887 doubtful words re-read on the images (his, ltu/#, 146, o/, ll=ib, tus in ipsum, f/ in ipsum); regraded in align1887.txt; last dictionary + LM pass over the two open pieces (work/gap1887.py, 9 Oct): nothing fits

## DECODE queue
- R1889: decrypted. Key = letter alphabet recovered from the draft R954 (a 0 n t z, b 8 9, c 7 x, d 3 4, e 6 m p,
  f 2 5, g 16 17, h 1 10, i 11 12 15 24 h, l 18 19, m d e, n 22 32, o a f l, p 20 g, q 30 33, r c i q,
  s 25 26 31, t 34 37, u 23 35 38 y, x 39). D3605 corrections: "04 10" = 0 4 | 10; "2000m" = 20 c 0 m;
  "37731" = 37 7 31; "i u" (p.2 hiberna) = 1 11. Plaintext = the draft R954.
- R1890: decrypted. Same alphabet + syllabary (40-44 la-lu, 45-49 na-nu, 50-54 ra-ru, pla-plu ta-tu, ap-up ca-cu,
  ca-cu ma-mu, ha-hu da-du, tas-tus ba-bu, an-un sa-su, au/eu/ou/uu pa-pu, me-mu fe-fu, ga/gi ha/hi, it/et/ot
  gi/ge/go; 21 o, 36 x, b m, o a; singletons fu mu, ko do, lx oc, li xi, 14 tz). D3604 corrections: every
  "l/z?" = z; "c/1? o/0?" = co; "pla/u?" = plu; "g^. a" = ga. Plaintext in NOTES above.
- R1887: new transcription (transcription/R1887.txt) and partial decryption; cipher type is syllabic/nomenclator
  (vowel-series three-letter groups + graphic signs), not "Homophonic substitution". The record note "same as the
  one used in the draft, dated 1634-11-16" is wrong twice: the draft R954 is dated 1635-11-16, and its cipher is
  the 1635 alphabet, not the 1634 repertoire.
- R954: receiver "Emperor Ferdinand II ... 1608-1657" should be Ferdinand, King of Hungary and Bohemia (later
  Ferdinand III); the letter addresses "Serenissime Rex".
- Prior reading to cite: Andrew Aymeloglu, github.com/aaymeloglu/unsolved-ciphers (Sept 2026).
