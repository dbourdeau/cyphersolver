# nanking1930: Chiang Kai-shek and Ma Fuxiang to the 13th Dalai Lama, Nanking, September 1930 (lead 1359)

Status: read in part (Brice Dudout, 11 Nov 2026; integrated 12 Nov 2026; method read with known key; the two Nanking telegrams, pp. 14-15, in the plain Chinese standard telegraph code: 221 of 230 codes give the character as written and read as sense = 96.1%; p. 14 150 of 155 = 96.8%, read; p. 15 71 of 75 = 94.7%, read in part; six codes emended by one digit and three unresolved are not counted). Summarised in English by the Government of India in 1930, so not a first break. The transcription comes from the viewer's OCR text layer and has not been checked against the images by anyone but the contributor. The Dalai Lama's code-word telegrams in the same file (pp. 9, 11, 12, 22-23) are another system and are not read.

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent (protocol, reading, controls, write-up).
Lead **1359**, found by Daniel Bourdeau in the Abhilekh Patal sweep. Pull request #434.

## Document

National Archives of India, External Affairs Department, **Sikkim (Political), 1930, File No. 5-P**, 49 pp. (Abhilekh Patal
NAIDLF03824535): "Interception of cypher telegrams addressed to Dalai Buddha, Lhasa, from Nanking Hojep telegraph office".
Seen after login in the online reader; **no image is included** (no reuse licence shown).

- p. 14: Nankinghojep → Dalai Buddha, Lhasa, 155 four-digit groups (Chiang Kai-shek).
- p. 15: XJS. Nankinghoje → Dalai Buddha, Lhasa, 75 groups (Ma Fuxiang).
- pp. 9, 11, 12, 22-23: telegrams of the Dalai Lama (Norbulingka) in 10-letter code words: p. 11 to Marshal Chiang Kai-shek,
  p. 12 to Ma Fuxiang, Chairman of the Tibetan-Mongolian Committee (both 22 Sept 1930), p. 9 to "Singchi c/o Thinyik Calcutta",
  pp. 22-23 to Ma Fuxiang and to Yoong Kun Dzasa (13 Oct 1930; the same text shifted by one word).
- p. 16: Weir (Political Officer, Sikkim), Gyantse, 6 Oct 1930, sends "the cypher and marginally noted code messages" to Simla
  and asks for paraphrases.
- p. 18: Foreign and Political Department to Weir, D.O. 29 Sept 1930: an English abstract of the Nanking messages.

## System

pp. 14-15: **plain Chinese standard telegraph code**, no encipherment, read in typing order (seven groups a line). The last
group of each is a date code (韻目): 元 = the 13th, 庚 = the 8th. Table: Unicode Unihan (`kTaiwanTelegraph`, else
`kMainlandTelegraph`), Unihan.zip from unicode.org (SHA-256 4c93ea9c...); codes used in `key.tsv` (CC BY 4.0).

## Method and controls (`frozen/`)

The protocol (`frozen/PREREG.md`, in French, SHA-256 23aba69bf00a4271b9b4eaed373bbab77ce688f2c13367eb65bca91d3b50871c) was
written and hashed before the attack, by the contributor's record (the pull request is a single commit). It fixed the crib
words, the hypotheses and, for the code words, a held-out message
(p. 9) to be measured once if a key were found. The plain code worked at once on pp. 14-15.

Controls. The protocol fixed this crib: 達賴 / 喇嘛 / 蔣 / 中正 / 馬福祥 / 貢覺仲尼 / 貢覺 / 堪布 / 中央 / 誠意 / 統一 / 擁護 /
函 / 悉 / 電. **The contributor's control script (`frozen/controles_A.py`) does not use it: the crib was changed after
decoding.** It has 棍堪布 (a spelling of Kun Kanpu's name that could only be known once the telegrams were decoded) and 誠, and
drops 貢覺仲尼, 貢覺, 堪布, 誠意 and 函. The first version of these notes and the profile said "crib words fixed in the
protocol", which was not accurate. Figures both ways, crib words of two or more characters against 1,000 random orders of
the groups:

| crib | p. 14 | p. 15 | best of 1,000 random orders |
|---|---|---|---|
| the crib in the protocol (rerun at verification, 12 Nov 2026) | 12 | 9 | 4 and 3 |
| the changed crib of `controles_A.py` (`frozen/controles_A.out`) | 14 | 10 | 4 and 3 |

With the protocol's crib and all word lengths the plain reading scores 14 (p. 14) and 11 (p. 15); over all 9,999 non-zero
four-digit additives the best scores 5 and 3. (`controles_A.out`: 1,000 random additives max 2, changed crib.) The
protocol's bar (coherent Chinese from end to end, at least three crib words, p < 0.01 against the controls) is met with the
protocol's own crib. Both halves of each telegram read.

## Reading (`reading.md`, `translation.md`)

**p. 14, Chiang Kai-shek:** 棍堪布來，面遞惠書及答覆八事，{均}悉。…中藏關係本極密切，前因主國者不以真誠相見，致失國師及藏衞民衆心理…今幸國師…以真誠擁護我中央政府…從此中藏一家，完成統一，至堪欽慰。除{切}囑蒙藏委員會馬委員長福祥慎重辦理外，先此覆謝，並祝健康。[?]蔣中正。元。

**p. 15, Ma Fuxiang:** 暌違廿餘載，馳念良殷。頃晤棍堪布，詢悉道躬佳勝，至深欣慰。國師竭誠擁護中央，極荷{蔣}主席嘉{許}，詳情已由主席電覆。所有尊事，福祥{竭}誠辦理，以期公私兩[?]。祈釋慧念。敬祝嘉福。馬福祥。庚。

Read share, by the README read bar applied as written: an emended code is a supplied value and is not counted.

| telegram | codes | as written (counted) | emended by one digit (not counted) | unresolved | read share |
|---|---|---|---|---|---|
| p. 14 | 155 | 150 | 3: 9971→0971 均, 7399→7299 音, 0634→0434 切 | 2: 4156 (盬), 5492 (萌) | 150 = 96.8%, read |
| p. 15 | 75 | 71 | 3: 5582→5592 蔣, 6069→6079 許, 4500→4550 竭 | 1: 5129 (呤) | 71 = 94.7%, read in part |
| both | 230 | 221 | 6 | 3 | 221 = 96.1% |

The contributor's figure, counting the six emended codes as read: 227 of 230 = 98.7% (153 of 155 and 74 of 75).

The unresolved codes:
- 4156 (盬) in 慧?明心: one digit away, 4158 = 目 gives 慧目明心, and 6 for 8 is a common misreading (candidate added at
  verification, 12 Nov 2026; the first version said no one-digit neighbour fits). 慧眼 (眼 = 4190) is two digits away. Not
  counted as read.
- 5129 (呤) in 公私兩?: no one-digit neighbour fits. The set phrase 公私兩便 (便 = 0189) is two digits away.
- 5492 (萌) before 蔣中正: probably a false start for 5592 蔣.

The 1930 abstract (p. 18) matches point by point, on the contributor's summary of it (the page was not seen at
verification): the letter brought by Kun Kanpu (棍堪布), support of the central government (擁護中央), China "not honest or
considerate" (不以真誠相見), "complete unity" (完成統一), greetings from Ma Fuxiang.

Dates: 元 = the 13th and 庚 = the 8th are the regular day values of the rhyme code; the month comes only from the file. This
leaves a problem of order: Ma's telegram, dated the 8th, says 詳情已由主席電覆, "the Chairman has already answered by
telegram", but Chiang's is dated the 13th. Open (noted at verification, 12 Nov 2026).

## The code-word telegrams (not read; another system, not part of this entry's reading)

Each 10-letter word is two 5-letter code words, CVCVC and VCVCV in turn (p. 9 starts with the vowel-initial form), as in the
pronounceable code language allowed by the 1928 Brussels telegraph rules. Letters are restricted by position (no x at the start
of a CVCVC word; h and l rare), as in artificial-word codebooks. pp. 11 and 12 share the opening words (faxed etepo), the words
"fubes ibexe" and the closing words (jopof opila rayod akawo). p. 12 is corrupt in places (an 11-letter word, "Bebaxeridn",
two illegible letters), with a shift of one or two letters. (The remark on the 1928 Brussels rules is the contributor's and
was not checked here.)

- p. 11 (51 words): faxed etepo supok ojena keboj ajaca ratac ihoko joxog aleka wibax arobi kacac owaza jaxag ometo mapoz amibe sibaw ofiwo gipabaze(8 letters) tikav ewake badew icoli vazad ipita libew ewoco zewak esagi lidif alowi cobax ivapo viper acavi wawic oraca kahot owifi vufid ucala yenam enoza fubes ibexe jopof opila rayod akawo
- p. 12 (38 words): faxed etepo sufax iwajo cicop oraza pizaf ubesi bexevirribu(11 letters) pevay ujuzi hamut a?apo subad epave feyuw anice lesas iba?e wecop itawi bebax eridn zamiz ajaro wewaf apobe miyig awejo pokoy awini cenow eteti bijop ofopi laray odaka wo
- p. 9 (39 words): apimo zamam omovujahm(9 letters) ijuba pivov uzulo corob ekovu dajin ewibo gapim ijewa kopux azeri joxax utaca layix inulo pakif ugipo rafab ezobu jajat izevi gikap imuha tabez iyowu mafog ebije rodot ozize kofog osaha movem ejawa bifix unuye cijor
- pp. 22-23: not transcribed (pale captures).

Tried: a table of CV syllables for digit pairs (each word = a four-digit telegraph code + a filler letter), with the guess that
the shared closing words spell 達賴喇嘛 (6671 6351 0812 0859): inconsistent. The alphabetical rank of the words gives nothing.
There is no crib: the p. 18 abstract covers the Nanking telegrams, not these replies. The held-out message (p. 9) was never
used; with no key, no measurement was made. These transcriptions were not tested at verification.

## Prior work

Foreign and Political Department to Weir, 29 Sept 1930 (p. 18): an English abstract of the Nanking messages (credited
`india_foreign_political`, prior solution; the contributor had credited `india_general_staff`, changed at integration). Who decoded the telegrams in 1930 is not stated in the pages described; that it was
the General Staff is a presumption. Web searches by the contributor and two at verification on distinctive phrases found
nothing printed. The Chinese printed document collections on Tibet and the central government were not searched; a 1930
telegram of Chiang Kai-shek to the Dalai Lama may well be printed there (see Remaining gaps).

## Integration check (12 Nov 2026)

Pull request #434, verified independently before integration; the corrections above and below come from that verification.

- **Decoding reproduces.** A decoder written for the check, with a table built from Unihan.zip (same SHA-256 as `key.tsv`
  states), gives the claimed character for all 221 codes read as written; the nine exceptions are exactly the six emended and
  three unresolved codes listed. The frozen group files equal `transcription.txt`. `frozen/controles_A.py` rerun gives
  `controles_A.out` byte for byte, and `frozen/decodage_A.out` is reproduced.
- **Emendations.** Each of the six is exactly one digit, and the character as written does not fit: 9971 has no character;
  7399 餅, 0634 胴 (Mainland field only), 5582 蔂, 6069 訌, 4500 空. 4550 竭誠 also occurs as written earlier in p. 15.
- **Crib.** Changed after decoding (see Method and controls); figures for the protocol's crib added.
- **Read share.** The headline is the strict figure, 221 of 230; p. 15 is under 95% and is read in part, so the class is
  read in part (it was "already solved", with 98.7%).
- **Transcription.** It comes from the viewer's OCR text layer, "checked against captures" by the contributor's agent; 6615
  (p. 14) and 7308 (p. 15) were half hidden by the cursor and are confirmed by the sense only. Any of the nine odd codes
  could be an OCR error and not a telegraph slip.
- **Not checked: the images.** `abhilekh-patal.in` shows a human check to scripts (HTTP 202 with an empty body to the record
  page at verification); nothing was done to go round it. Nothing in this folder has been verified on the image by anyone but
  the contributor, who was logged in.
- **Class, method, provenance.** Method read with known key; class by the read bar; the 1930 English abstract is the prior
  solution (an abstract, not a translation; no Chinese text). Provenance changed from "mixed" to "contributed".
- **Lead 1359.** Its vetting note of 11 Nov 2026 describes a reading of the file through the document viewer from the cloud,
  without the site's human check: the same route as the eight verdicts held in `research/COVERAGE.md`. The lead's closing
  verdict now rests on the contributor's logged-in reading (this pull request), and that vetting is recorded as superseded.
- `python docs/_check_profile.py nanking1930`: valid. `python docs/_check_terms.py nanking1930`: no finding.

The same public code table reads `targets/ctcplain1913` (20 telegrams of Sun Yat-sen's circle copied in Japan, 1913-16) and
`targets/peking1912` (a Peking telegram of October 1912, from another National Archives of India file, sent in five-digit
groups). They are separate entries: other archives or files and other correspondents.

## Remaining gaps

- p. 14 codes 4156 (慧?明心; candidate 4158 目) and 5492 (before the signature), p. 15 code 5129 (公私兩?; 便 is two digits away) - blocker: needs-physical-access; each may be an OCR error, a typing slip in the copy or a telegraph slip, and only the image (behind the archive's login and human check) can tell; a difference between the 1930 code book and the Unihan table is not excluded
- the six one-digit emendations (p. 14: 9971, 7399, 0634; p. 15: 5582, 6069, 4500), which keep p. 15 under the read bar - blocker: needs-physical-access; if the image shows the emended digits the OCR was wrong and the codes count as read; the image check is open only to someone logged in to Abhilekh Patal
- image check of the 230 groups by a second reader, with 6615 and 7308 (half hidden by the cursor on the captures) - blocker: needs-physical-access; Abhilekh Patal shows a human check to scripts and the pull request carries no image
- prior art in Chinese printed document collections (a printed Chinese text of either telegram) - blocker: needs-physical-access; printed volumes, none opened by the contributor, at verification or here; web searches found nothing
- the order of the two telegrams (Ma's, dated the 8th, says the Chairman has already answered; Chiang's is dated the 13th) and the month - blocker: needs-physical-access; the dates of handing in are on the telegraph copies and in the rest of the file, behind the same login
- the Dalai Lama's code-word telegrams, pp. 9, 11, 12, 22-23 (another system) - blocker: no-key-material; 5-letter code words, no code book found, no crib; next: look for the code book (Mongolian and Tibetan Affairs Commission or Ministry of Communications, 1928-30), read the General Staff notes of January 1931 later in the same file, which may report a break, transcribe pp. 22-23

## Escalation

- [x] siblings: the other telegrams of the file were opened by the contributor (pp. 9, 11, 12, 22-23: code words, another system, not read); `targets/peking1912` and `targets/ctcplain1913` use the same table and need no key from here
- [x] clear-pages: p. 18 is an English abstract of the Nanking messages, not a text; it confirms the content and gives no character for the open codes
- [x] known-keys: the public standard telegraph code, Unihan Taiwan field then Mainland field, reads 221 codes as written
- [x] print: web searches by the contributor and two at verification on distinctive phrases, nothing; Chinese printed collections not opened (Remaining gaps)
- [n/a] key-rebuild: the key is a public table; nothing to rebuild
- [x] retry: the one-digit neighbours of each of the nine odd codes run through the table at verification and again at integration: six give the expected word, 4156 has the candidate 4158 目, 5129 and 5492 have none that fits the phrase (5592 蔣 for 5492 repeats the next code)
