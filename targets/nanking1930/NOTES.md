# nanking1930: Chiang Kai-shek and Ma Fuxiang to the 13th Dalai Lama, Nanking, September 1930 (lead 1359)

Status: read (Brice Dudout, 11 Nov 2026; class already solved; the two Nanking telegrams, pp. 14-15: 227 of 230 codes read by sense = 98.7%, plain Chinese standard telegraph code; summarised in English by the Government of India in 1930, so not a first break). The Dalai Lama's code-word telegrams in the same file (pp. 9, 11, 12, 22-23) are not read. Next step for them: find the code book (see Remaining gaps).

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent (protocol, reading, controls, write-up).
Lead **1359**, found by Daniel Bourdeau in the Abhilekh Patal sweep and vetted by him on 11 Nov 2026.

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
written and hashed before the attack. It fixed the crib words, the hypotheses and, for the code words, a held-out message
(p. 9) to be measured once if a key were found. The plain code worked at once on pp. 14-15.
Controls (`frozen/controles_A.py`, output `frozen/controles_A.out`; they need a code table built from Unihan, not included):
crib words of two or more characters 14 (p. 14) and 10 (p. 15), against max 4 and 3 over 1,000 random orders of the groups;
1,000 random 4-digit additives max 2. Both halves of each telegram read.

## Reading (`reading.md`, `translation.md`)

**p. 14, Chiang Kai-shek:** 棍堪布來，面遞惠書及答覆八事，{均}悉。…中藏關係本極密切，前因主國者不以真誠相見，致失國師及藏衞民衆心理…今幸國師…以真誠擁護我中央政府…從此中藏一家，完成統一，至堪欽慰。除{切}囑蒙藏委員會馬委員長福祥慎重辦理外，先此覆謝，並祝健康。[?]蔣中正。元。

**p. 15, Ma Fuxiang:** 暌違廿餘載，馳念良殷。頃晤棍堪布，詢悉道躬佳勝，至深欣慰。國師竭誠擁護中央，極荷{蔣}主席嘉{許}，詳情已由主席電覆。所有尊事，福祥{竭}誠辦理，以期公私兩[?]。祈釋慧念。敬祝嘉福。馬福祥。庚。

| telegram | codes | certain | probable (one-digit slips) | unresolved | read by sense |
|---|---|---|---|---|---|
| p. 14 | 155 | 150 | 3: 9971→0971 均, 7399→7299 音, 0634→0434 切 | 2: 4156 (盬), 5492 (萌) | 153 = 98.7% |
| p. 15 | 75 | 71 | 3: 5582→5592 蔣, 6069→6079 許, 4500→4550 竭 | 1: 5129 (呤) | 74 = 98.7% |

The 1930 abstract (p. 18) matches point by point: the letter brought by Kun Kanpu (棍堪布), support of the central government
(擁護中央), China "not honest or considerate" (不以真誠相見), "complete unity" (完成統一), greetings from Ma Fuxiang.

## The code-word telegrams (not read)

Each 10-letter word is two 5-letter code words, CVCVC and VCVCV in turn (p. 9 starts with the vowel-initial form), as in the
pronounceable code language allowed by the 1928 Brussels telegraph rules. Letters are restricted by position (no x at the start
of a CVCVC word; h and l rare), as in artificial-word codebooks. pp. 11 and 12 share the opening words (faxed etepo), the words
"fubes ibexe" and the closing words (jopof opila rayod akawo). p. 12 is corrupt in places (an 11-letter word, "Bebaxeridn",
two illegible letters), with a shift of one or two letters.

- p. 11 (51 words): faxed etepo supok ojena keboj ajaca ratac ihoko joxog aleka wibax arobi kacac owaza jaxag ometo mapoz amibe sibaw ofiwo gipabaze(8 letters) tikav ewake badew icoli vazad ipita libew ewoco zewak esagi lidif alowi cobax ivapo viper acavi wawic oraca kahot owifi vufid ucala yenam enoza fubes ibexe jopof opila rayod akawo
- p. 12 (38 words): faxed etepo sufax iwajo cicop oraza pizaf ubesi bexevirribu(11 letters) pevay ujuzi hamut a?apo subad epave feyuw anice lesas iba?e wecop itawi bebax eridn zamiz ajaro wewaf apobe miyig awejo pokoy awini cenow eteti bijop ofopi laray odaka wo
- p. 9 (39 words): apimo zamam omovujahm(9 letters) ijuba pivov uzulo corob ekovu dajin ewibo gapim ijewa kopux azeri joxax utaca layix inulo pakif ugipo rafab ezobu jajat izevi gikap imuha tabez iyowu mafog ebije rodot ozize kofog osaha movem ejawa bifix unuye cijor
- pp. 22-23: not transcribed (pale captures).

Tried: a table of CV syllables for digit pairs (each word = a four-digit telegraph code + a filler letter), with the guess that
the shared closing words spell 達賴喇嘛 (6671 6351 0812 0859): inconsistent. The alphabetical rank of the words gives nothing.
There is no crib: the p. 18 abstract covers the Nanking telegrams, not these replies. The held-out message (p. 9) was never
used; with no key, no measurement was made.

## Prior work

Foreign and Political Department to Weir, 29 Sept 1930 (p. 18): an English abstract of the Nanking messages (credited
`india_general_staff`, prior solution, as the probable source of the decoding). Lead 1359 open as vetted on 11 Nov 2026 ("not
tested further"); web search found nothing printed.

## Remaining gaps

- p. 14 codes 4156 and 5492, p. 15 code 5129 (illegible: no one-digit neighbour fits; an edition difference of the code book is not excluded).
- The code-word telegrams, pp. 9, 11, 12, 22-23 (no-key-material). Next: look for the code book (Mongolian and Tibetan Affairs
  Commission or Ministry of Communications, 1928-30); read the General Staff notes of January 1931 later in the same file, which
  may report a break; transcribe pp. 22-23.
