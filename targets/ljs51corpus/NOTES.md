# Penn LJS 51: transcription and key rebuilding across the whole manuscript

Status: read in part
Outcome: read from existing decipherment (the compiler's own solutions, transcribed from the masters), with keys
recovered from that adjacent plaintext for the keyed chains (`keys_eye/`, `keys.tsv`) and the tree script decoded.
Written up 28 Nov 2026 on the user's instruction ("write up now with the keys we have"), which ends the earlier hold;
page `docs/ljs51corpus.html`. Counts in `texts/stats.json` (built by `build_texts.py`).

## One key, one entry (decision of 28 Nov 2026)

Every cipher in the volume has its own alphabet (`keys_eye/REPORT.md`, "Shared alphabets?"). The write-up presents the
volume as one study of one manuscript, the compiler's casebook of solved ciphers, and lists the keys per cipher
(`keys.tsv`, one block per chain); no two ciphers are merged into one key. Two ciphers that a misbound quire split are
one cipher each (46v.11+13r.1, 20r.8+47r.1). The two ciphers of the volume with pages of their own are not documents of
this target: f. 106v (`targets/qaysarani1350/`) and ff. 48r-48v with 21r l.1-5 (`targets/ljs51f48r/`). On the user's
decision of 27 Nov 2026 five open ciphers were promoted to the catalogue (commit 7c7edcbb50): 3938 (1r.2), 3939
(12v.8), 3940 (12v.11), 3941 (3v.12), 3942 (98v.10); 30v.7 stays out of the catalogue.

## Goal (set 27 Nov 2026)

Transcribe every cipher block and every plaintext passage of Penn LJS 51 (ff. 1r-106v, 212 pages, 209 cipher chains
counted by the page pass), rebuild the key of every chain from the compiler's own plaintext and the red glosses, and
study the manuscript as a whole: the sign alphabets and their families, the techniques the compiler names, the people,
the dating, the compiler's method. End products: a sign-level transcription per chain, a key table per chain with a
measured fit, a corpus table for the paper with George Lasry, and (after review) a write-up.

## Sources

- OPenn master TIFFs `https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_NNNN.tif` (2339 x 2959 px, about 20 MB),
  local copy in `output/ljs51/master/` (git-ignored). Image = 6 + 2*(folio-1) for r, +1 for v; image 0217 = f. 106v.
- Page pass: `research/ljs51_pass/` (BRIEF.md, 17 `pages_*.jsonl`, `pages_merged.json`, `chains.json`, gap checks,
  `vet_tashifi.md`, `vet_tiff_check.md`, `prior_art.md`, `FINAL_LEADS.md`). Page-pass readings are model readings of
  1422-px images: starting points, not evidence.
- Related: `targets/qaysarani1350/` (f. 106v, read), `targets/ljs51/` (the failed parallel attempt, record only).

## Plan

0. Masters for all 212 pages; line and block crops; a chain manifest (`chains.json`) with image, lines, block id.
1. Pilot on three chains (a glossed block, a numeral block, the tashifi run) to fix the method and its measures.
2. Cipher transcription: segment glyphs on the master, cluster into sign classes per chain, label by chain.
3. Plaintext transcription from the master (the page pass is the draft), word by word, `[?]` for doubt.
4. Key rebuilding: align signs to plaintext letters (DP), read the red gloss where present, record one key per chain
   and a measured fit (aligned share, purity, nulls, dropped letters). Chains whose counts do not fit are flagged.
5. Whole-manuscript analysis: alphabet families, techniques named by the compiler against techniques found, people and
   dating (checked against biographical sources), the compiler's method and his stated rules.
6. Outputs and review: corpus table, key tables, a report to Daniel; only then a write-up.

## Work state (27-28 Nov 2026)

- Segmenter v1 (`segment.py`, `evaluate.py`): 90% of reference lines within one sign; known faults listed in README.md;
  a fix (v2, sign crops in `output/ljs51/signs_v2/`) is in progress, tuned on the by-eye counts of the chain records.
- Key tool `rekey.py` + `pilot_report.md`: tashifi key rebuilt from scratch; short chains need by-eye or joint keys.
- Chain records from the masters: `chains_0006_0029`, `0030_0053`, `0054_0077`, `0078_0101` done (89 chains, ff. 1r-48v);
  `0102_0125` in progress; images 126-217 still to do.
- English translations (done by a fork session, handed back 28 Nov): `translation_0006_0053.md`, `translation_0054_0077.md`,
  `translation_0078_0101.md`; each ends with "Suspected Arabic errors" to check on the masters (about 50 items).
- `keys_fork/`: restricted provisional rebuild (control reproduced; 6v.11 partial; 20r.8 at chance, probably two alphabets
  split at 21r l.1; 62 chains skipped for segmentation). `keys_eye/BRIEF.md`: by-eye key pilot brief, not started.
- Unanswered chains so far: 1r.2 (page damaged, red gloss unread), 30v.7, 46v.11, 48r.8 (226 signs vs a 72-letter verse).
  f. 73v l.8-12 and 74r l.3-7 are answered on 74v (l.6-7 and l.2-3; chains_0150_0173.jsonl): no longer open.
- Later done: chains_0102_0125, 0126_0149, 0150_0173 (70 chains, all answered); translations 0102_0125, 0126_0149,
  0150_0173; segmenter v2 (signs_v2); by-eye key pilot on 5 chains in keys_eye/ (all consistent, red gloss 119/119).

## People: Shihāb al-Dīn al-Mutarjim identified (27 Nov 2026)

Lead from Yıldırım & Aydın, "Mu'ammâyı Çöz", GTTAD 8/18 (2026), pp. 1013-1028 (doi 10.53718/gttad.1966046), which
cites Ṣafadī on al-Mutarjim al-Baghdādī and does not know LJS 51. The *Wāfī* entry was read on Shamela
(https://shamela.ws/book/6677/1666, ed. Arnāʾūṭ-Muṣṭafā, vol. 7, pp. 94-95):

> المترجم البغداذي: أحمد بن عبد الله بن داود بن علي بن أحمد بن محمد شهاب الدين البغداذي المعروف بالمترجم، رأيته بدمشق غير مرة،
> وهو فرد الزمان ونادرة الأوان في حل المترجم، وإمام في الكتابة المنسوبة وتعتيقها. أول وروده إلى دمشق وصف لشيخنا العلامة شهاب الدين
> أبي الثناء محمود فأحضروه إليه إلى ديوان الإنشاء فكتب له لغزا مترجما فحل المترجم واللغز في الوقت الحاضر ... وآخر عهدي به في سنة
> خمس وأربعين وسبع مائة بدمشق ثم توجه إلى القاهرة.

(Summary: Aḥmad b. ʿAbd Allāh b. Dāwūd, Shihāb al-Dīn al-Baghdādī, called al-Mutarjim. Ṣafadī calls him the best of his
age at solving ciphers and a master of proportioned script. When he first came to Damascus he was brought to Shihāb
al-Dīn Maḥmūd in the Dīwān al-inshāʾ, who set him an enciphered riddle, and he solved both cipher and riddle on the spot.
Ṣafadī last saw him in Damascus in 745/1344-45, after which he went to Cairo. He also wrote a verse blurb for Ṣafadī's
*Jinān al-jinās*.)

LJS 51 matches:
- "al-Shaykh Shihāb al-Dīn al-Mutarjim" is the main correspondent: chains 6v.11, 10v.13, 11v.11, 12v.8, 37r.11, 40v.5,
  64r.3, 65r.5 ("al-Shaykh Shihāb"), 73r.5, 78r.12. **59r.2 gives his ism: الشيخ الفاضل شهاب الدين احمد المترجم.** Aḥmad +
  Shihāb al-Dīn + al-Mutarjim + a cipher specialist: same man as Ṣafadī's, **identification firm** (pending a check of
  the 59r reading on the master TIFF).
- 60r.5: "Kamāl al-Dīn, son of the qāḍī Jamāl al-Dīn, son of al-Shihāb Maḥmūd" brings the compiler a cipher. Al-Shihāb
  Maḥmūd is the chancery head of Ṣafadī's anecdote (Shihāb al-Dīn Maḥmūd b. Salmān al-Ḥalabī, d. 725/1325, my
  identification, not checked in a source here). So a grandson of that man is in the compiler's circle.
- 38v.10: a verse praising Tāj al-Dīn Ibn al-Durayhim (d. 762/1361) for حل المترجم. (Correction 28 Nov: the GTTAD
  article does not quote this verse; its Table 1 only lists Ibn al-Durayhim. The verse is al-Jawlānī's, sent in cipher
  to the compiler.)

## Compiler: probably Ibn al-Durayhim (28 Nov 2026; `identity_ibn_durayhim.md`)

Verdict of the sourced check: supported, not proven. For: f. 102v "my book Miftāḥ al-kunūz fī ḥall al-marmūz", chapter
al-maqlūb (Ṣafadī's list of his works, A'yān 3:525, has a Miftāḥ fī ḥall al-rumūz; his surviving treatise is
Miftāḥ al-kunūz fī īḍāḥ al-marmūz); the Kitāb al-Ajwiba al-Shāmiyya (80v) is in his works list; the Dunaynīr/Durayhim pun
argued in the first person (49v-50r); the patron al-ʿAlāʾī = ʿAlāʾ al-Dīn Ibn Faḍl Allāh, kātib al-sirr in Cairo (62r:
"after the death of his brother the amir Ṣalāḥ al-Dīn", d. Ṣafar 760, A'yān 5:490-491), which dates 62r to 760/1359 or just
after; Aleppo with Ibn al-Wardī, Cairo-Syria travel, unpaid treasury money all match Ṣafadī. Against/open: the compiler
never names himself; the refused vizierate (45v-46r) and Alexandria (99r) are not in the biographies; 102v, 50r, 62r, 39r,
80v and 45v must be checked on the masters; Mrayati vol. 3 not read.
- The compiler's formula فحللته في الحال بحضوره (7r, and f. 106v) is the same on-the-spot solving scene as Ṣafadī's.

What follows for dating: al-Mutarjim was active in Damascus before 725/1325 (Maḥmūd's lifetime) and still there in
745/1344-45. A grandson of Maḥmūd is an adult in the book. Ibn al-Durayhim is praised in it. Together these put the
correspondence c. 1325-1360, consistent with the sweep's 1330-1370 and narrower.

Open (hypothesis, not checked): "al-maqarr al-sharīf al-makhdūmī al-ʿAlāʾī", the master to whom al-Mutarjim writes, may be
ʿAlāʾ al-Dīn ʿAlī b. Yaḥyā Ibn Faḍl Allāh al-ʿUmarī, kātib al-sirr in Cairo 743-769/1342-1367. That would fit
al-Mutarjim's move to Cairo after 745. Test against the book's place names (65r.5 says the compiler wrote "in Aleppo") and
the ʿAlāʾī's titles. Also still to check: Ibn Ḥajar, *al-Durar al-kāmina* (Aḥmad b. ʿAbd Allāh), for a death date.

## f. 48r l.8 - 48v l.13 deciphered (28 Nov 2026; `solve_48r/REPORT.md`)

Blind annealing (ar-mamluk, word spaces) read it as the f. 21r rhymed-prose riddle (plaintext of 20r.8); aligned,
218/229 signs (95.2%), after a 2x re-read 220/228 (96.5%), take a one-to-one key, covering 232 of the riddle's 293 letters (to جملته). Not an open lead any
more. The cipher corrects the 20r.8 record: ترميها (not توهمها), يحمد منها (not وخمد).

## Identity passages and codicology checked on the masters (28 Nov 2026; `identity_readings.md`)

- 102v l.6-10: «في كتابي مفتاح الكنوز في حل المرموز من باب المقلوب», first person, حل (not ايضاح), the compiler's own narrative.
- 50r l.6-7 (new reading): in defending «ابن دريهم» in his own cipher verse he writes «الاول ان لقب الجد الاعلى الدريهم مصغرا»:
  the laqab of his remote ancestor is al-Durayhim. The nearest the book comes to naming him.
- 49r l.8-9: «ولي تصانيف فيه» (he has written works on cipher). 62r l.6: «بعد وفاة اخيه الامير صلاح الدين» (certain).
- 45v l.10-12 corrected: called to take the vizierate of al-Sham, he refused unless the mukus were abolished, and asked to
  be excused; the release went through the patron before the sultan. 80v: الاجوبة الشامية named, without كتابي.
- He is never named by ism or nasab. Verdict: identification strongly supported.
- Codicology: quire 3 (ff. 13-20) is bound out of place and belongs between f. 46 and f. 47 (46v→13r split inside a word;
  20v→47r: 20r.8 is the first half of the riddle cipher 47r.1; "third" at 20r, "fourth" at 48r). A physical check of
  Penn's irregular q6-q7 collation is owed.
- Key wave ff. 13r-24v (keys_eye/REPORT.md): 20r.8 + 47r.1 is one cipher (336 signs, 98.8% consistent; plaintext =
  riddle verses 1-8, cipher readings differ from the clear riddle in five places). 21r l.1-5 (62 signs) is the END of the
  48r.8 cipher (read with the 48r key unchanged: the last third of the 21r prose), so f. 21r once followed f. 48v and
  quire 4 (ff. 21-28) probably also stood after f. 48; the joins 12v→? and 28v→49r are still to check.

## Unanswered chains after the recheck (28 Nov 2026; `chains_missed.jsonl`, `recheck_unanswered.jsonl`)

- 48r.8: answered by the 21r-21v rhymed prose (the plaintext of 20r.8: the same text enciphered again, 'ورابعها'), found
  independently twice: by group-length search (43/49 groups) and by blind annealing above. Leaf probably lost after f. 48.
- 46v.11 (33 signs) + 13r.1 (44 signs): one cipher in one key, split across a displaced leaf; plaintext 13r l.5-7
  (قلت لنفسي حين مالت الى وزاره الشام وفعل / الاثام اين الحجى ...). Codicology check owed (13r follows 12v in the binding).
- 49r.1 (42 signs, new record): answered by the last 12 words of the 49r l.6-7 verses; 'فلم تنحل الا بعد تعب كثير' is its.
- 12v.8 and 12v.11 LOSE their 13r candidates (13r l.5-8 answer 46v.11+13r.1): now unanswered.
- 30v.7 (81 signs, 20 groups): still unanswered after reading ff. 30r-31v and a group-length search over all 1,034
  passages (best 9/20 lengths wrong). Next: rebuild 30r.4's key and test it here.
- 1r.2: plaintext lost (page damage); red gloss unread.
Record edits owed (not yet applied): merge 46v.11+13r.1; clear 13r candidates from 12v.8/12v.11; 48r.8 plaintext = 21r,
heading ورابعها; and the 32 category-(a) readings in `errata.json`.

## f. 63v tree script and prior art (28 Nov 2026)

f. 63v (28 Nov, keys_eye/63v.trees.json, 63v.1.json): the tree script is a branch-count code on the abjad words:
right-side branches = abjad word (1 ابجد ... 8 ضظغ), left-side branches = place in the word; 78/79 trees fit (3.15 torn);
Eastern order except ص = 1/5. The record's plaintext is wrong in four words: read ايري ... لا يجوز ... يجوز فنكته (both
ciphers and the red letters agree; chains_0126_0149.jsonl and translation_0126_0149.md not yet corrected). Prior art
(`prior_art_2.md`, 28 Nov): the same rule is in Ibn al-Durayhim's Miftāḥ al-kunūz fī īḍāḥ al-marmūz (Mrayati et al.,
Arabic vol. 1, Damascus 1987, p. 335: «القلم المشجر، وهو مبني على كلمات (ابجد)», right branches = abjad word, left =
place; alif a Y fork), the only treatise author to describe it per the editors (p. 185); a tree alphabet without a stated
rule is also in Shawq al-mustahām (Hammer 1806, Arabic p. 38). Qalqashandī (Ṣubḥ 9:229-232) omits it. So the method is
known; its use in LJS 51 and the 63v decipherment are not reported anywhere read. The Miftāḥ's first kind is «باب
المقلوب» followed by ibdāl, as f. 102v assumes; the title «مفتاح الكنوز في حل الرموز» is attested in the codex's contents
leaf and in Ṣafadī (editors' note p. 309). Penn/Christie's/Schoenberg descriptions name no compiler.

## Write-up state (28 Nov 2026)

Counts at the write-up (`texts/stats.json`, from `chains_all.json` and `keys_eye/` as copied at the final build): 207
ciphers (211 chain records, less the two merges and the two ciphers with pages of their own), 15,200 signs by eye; the
compiler answers 200 in full (14,829 signs, 97.6%), 3 in part, 4 not at all. Sign counts come from the key files where
a chain is keyed (most record totals were segmenter counts), and 30v.7 is the recheck's 81. A chain that the record
called answered in part but whose by-eye key aligns at least 95% of its signs with the plaintext is counted as answered
in full (2r.4, 4v.8, 7r.5, 7v.12, 10v.1, 11r.10, 12r.8). The decryption files follow the plaintext as enciphered (from
the key files) for keyed chains, and the corrected chain record for the rest. The fraction read is not raised to "read":
seven ciphers stay open, each blocked from outside (below). The 30v.7 test with the 30r.4 key (`keys_eye/30v.7.json`, key_test_30r4): nine shapes are shared, but the 30r.4 key does not read it.

## Remaining gaps
- 1r.2 (catalogue 3938; f. 1r l.2-8, about 79 signs) - blocker: illegible; plaintext lost to the damage of the first leaf, the red gloss faint (a few letters read)
- 12v.8 (catalogue 3939; f. 12v l.8-10, 41 signs) - blocker: too-short; single-use alphabet, no plaintext ("he solved it and wrote nothing on it"); its 13r candidate belongs to 46v.11+13r.1
- 12v.11 (catalogue 3940; f. 12v l.11-13, 33 signs) - blocker: too-short; its own pen, no plaintext, same situation as 12v.8
- 30v.7 (open, not catalogued; f. 30v l.7-13, 81 signs) - blocker: too-short; single-use alphabet, no plaintext anywhere in the book (group-length search over all 1,034 passages: best 9 of 20)
- 3v.12 (catalogue 3941; ff. 3v-4r, 42 signs) - blocker: no-key-material; the written verses do not take the signs as a simple substitution (best 25 of 42, chance level), single-use alphabet
- 88v.10 (f. 88v, 44 signs) - blocker: illegible; the second line of its plaintext (89r l.2) is lost in a hole in the paper
- 98v.10 (catalogue 3942; f. 98v, 51 signs) - blocker: no-key-material; the verse is given in a full and a shortened form and the cipher fits neither by group lengths; single-use alphabet

## Escalation
- [x] siblings: the whole volume searched for each open cipher's plaintext (page pass, gap checks, recheck; the 1,034-passage group-length search for 30v.7); the misbound quire found 46v.11+13r.1, 20r.8+47r.1, 48r.8 and 49r.1
- [x] clear-pages: every clear passage of ff. 1r-106v read on the masters for the chain records; the open ciphers have none that fits
- [x] known-keys: no two ciphers share an alphabet (keys_eye/REPORT.md); the 47r key tried on 48r.8 (no), the 30r.4 key tried on 30v.7 (nine shared shapes, does not read it)
- [x] print: Mrayati et al. vols. 1-2, Mir 'Alam 2018, Qalqashandi, Safadi, Penn/Schoenberg/Digital Scriptorium (prior_art_2.md): no edition or decipherment of LJS 51
- [x] key-rebuild: by-eye keys from the compiler's plaintext for 63 ciphers; 3v.12 tested as a simple substitution (chance level)
- [x] retry: the unanswered chains rechecked on the masters (recheck_unanswered.jsonl, chains_missed.jsonl): 46v.11, 48r.8 and 49r.1 answered, 12v.8/12v.11 lost their candidates

## Transcription doubts
- tree 3.15 (f. 63v, row 3, tree 15) - read: ل; checked: image, decode, transcription (the sign cipher 63v.1 and the red letter); crown torn, L3 R4 at face value would be م, the couplet and the red letter give ل
- S6 (13r.11, f. 13r) - read: ب and once ي; checked: image, decode; one shape for both letters (a skeleton spelling), kept as written
- W4 (18r.11, f. 18r) - read: ر (8 times), م once; checked: image, decode; the one م is a look-alike, kept with the key's majority
- HK, OM, AY, XN, K (48r.8) - read: see targets/ljs51f48r; checked: image, decode; settled on that page's 2x re-read
- 43 plaintext words (errata.md, verdict c) - read: as in the chain records, marked [?]; checked: image, decode (the cipher's group lengths where keyed); not settled from the image, they keep their mark
- 22v.9 and 24v.6 sign classes - read: letter-shape classes; checked: image, decode; 22v.9 does not fit as a substitution (40%), 24v.6 breaks in the lam-alif-like and alif-like classes: both keys stay unconfirmed

