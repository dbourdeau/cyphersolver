# Ferdinand and Isabella → De Puebla, Tortosa, 28 Dec. [1495], cipher copy (catalogue 615)

Status: no write-up. Why: the content of this despatch is in print only as Bergenroth's English abstract of the
clear draft (CSP Spain I no. 113), an abstract of the clear draft, not a decipherment of the cipher copy; no. 114
notices the cipher copy but prints no decipherment of it. This contribution identifies doc. 124 with that despatch and
decodes a sample (p. 1 ll. 6-8, p. 2 ll. 1-2) with the extant key; nothing beyond the sample of the cipher copy is
read, so it gets no page (maintainer review, 27 Oct 2026). Contributed by WAINUT (https://github.com/WAINUTAI),
27 Oct 2026.
Since 14 Nov 2026 the Spanish clear text of the same despatch, AGS PTR leg. 52 doc. 129, is transcribed in `dudout/`
(Brice Dudout, PR #623; pp. 1-2 and 15 settled) and set beside the sample (last section); doc. 124 itself is still
transcribed only in the sample, so the status does not change.

AGS, Patronato Real, leg. 52, doc. 124. PARES description
[2207846](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/2207846), viewer
[show/2207846](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2207846), 4 images. Old mark "T. c. Y. 2"
(Tratados con Inglaterra, leg. 2) on pp. 1 and 4; foliation 664-665. A modern note on p. 4 reads: "Carta de los
RR.CC. al doctor Puebla en cifra incompleta". The PARES title ("sobre tratos de comercio con Inglaterra") comes from
the merchant cover words of the copy ("la conpania", "los factores", "mercaderias").

## What the letter is

It is a ciphered copy of the despatch of Ferdinand and Isabella to Rodrigo González de Puebla, Tortosa,
28 December 1495. The despatch is dated "1496" because the Spanish year began at Christmas.

- Bergenroth, *Calendar of State Papers, Spain*, vol. I (1862), **no. 113, pp. 72-75**: an English abstract of the
  clear draft (S. E. T. c. I. L. 2), with quotations.
  [BHO pp. 72-79](https://www.british-history.ac.uk/cal-state-papers/spain/vol1/pp72-79).
- Same volume, **no. 114, p. 75**: "The same despatch written in cipher. There are some alterations in the wording,
  but the substance is exactly the same. Spanish. Written in two different keys of cipher, one of which is extant."
- Bergenroth printed no decipherment of the cipher copy. The 1868 Supplement starts in 1498.

The evidence for the match comes from the clear words of doc. 124 (sample_transcription.txt):

| doc. 124 | CSP Spain I no. 113 |
|---|---|
| p. 2: "se le escrivio a catorze de mayo ... veynte de junio ... veynte e uno de jullio ... veynte e dos de agosto ... veynte e dos de setienbre con Salvador Duarte" | "Have written to him on the 14th of May, 20th of June, 21st of July, 22nd of August, 22nd of September" |
| p. 1: "nueve", "otra ... diez e siete", "otra ... treynta" | "Have received his letters of 9th of September, and 11th, 17th, and 30th of October" |
| p. 2: "agora que los factores de la conpania son venidos con la corte aqui a Tortosa" | dated Tortosa, 28 December |
| p. 1: Diego de Soria, Iohn de Santagadea, Diego Lopez de Ayala (clear) | the couriers and forwarders of nos. 113 and 117 |

Control: we split the BHO pages for CSP I pp. 57-107 into 42 calendar items and scored each against the five
sending dates of p. 2. Only no. 113 matches, and it matches all five; the next best item matches one. Out of 2,000
random five-date sets, none matched three dates in any item.

Is doc. 124 no. 114 itself? Probably, but this is not proven. No. 114 is "in two different keys", and we saw only the
Great Roman Numeral code on the lines we read. The endorsement of no. 113 mentions three copies, one by Valmarada
by sea and two via Diego de Soria. Doc. 124 may be another of those copies. Either way, no. 113 gives the
content.

## The code and the sample

The code is Puebla's Great Roman Numeral code. Its key is AGS PTR leg. 52 doc. 33
([show/2207755](https://pares.cultura.gob.es/ParesBusquedas20/catalogo/show/2207755), 200 images): an alphabetical
list of words and names numbered in Roman figures. Tomokiyo (cryptiana, "Spanish ciphers") lists doc. 124 under this
code, and he publishes many of its values.

Script forms, read on the key and in doc. 124: jV = M, d = D, dc = DC, **da = DCC**, dar = DCCC, ar = CCC. A small
ring is written over the C ligature and over final iiij/viij. The C-count of the ligatures follows the rule set out
in `targets/puebla1496/NOTES.md`.

`key_excerpt.tsv` holds the entries used here, with the key image each was read on. `decode_sample.py` applies them
to `sample_transcription.txt` and writes `sample_decryption.txt`. p. 1, ll. 6-8 decode as:

> nos fiso [?883] Diego Lopez de Ayala [?1374] **de** nueve **de otubre y** otra **de** diez e siete **de otubre y** otra
> **de** treynta **de otubre que** [?1335]

(bold = code groups). The controls in the same script give no Spanish. A shift of one entry gives "oyd" or
"paciencia" for every "otubre", and leaves "de" and "y" with no value. Shuffling the groups gives "diez e siete otubre",
"nueve que de".

Corrections made in the check (27 Oct 2026):

1. The month group is **jVda iiij = MDCCIIII = "otubre"** (key image 105, which has "oy" MDCCII, "oyd" MDCCIII,
   "otubre" MDCCIIII). The first pass had read it as "jVdc iiij" and left the month open.
2. **DCCCLV = "dotor de puebla"** is now read on the key (image 48; 854 is "dotor de talavera"). Before this, it was
   taken from Bergenroth's no. 117.
3. Key image 105 has MDCXCV as "otro/otra". Tomokiyo lists "otras".

Reading and translation of the sample: `sample_reading.txt`, `sample_translation.txt`. The key confirms the lines,
and so do the five dates in no. 113.

## A difference from the print

The cipher copy reads "de nueve **de otubre**". Bergenroth's abstract of the draft has "9th of September, and
11th ... of October". We saw no "onze" in the lines read. This may be one of the "alterations in the wording" of
no. 114, or a slip in one of the two texts. It does not affect the identification.

## Proposed catalogue change

615: an earlier-solution pointer. The content is in CSP Spain I (1862) no. 113, pp. 72-75, an abstract of the clear
draft. The cipher copy is no. 114, p. 75 ("substance exactly the same"), or a sibling copy. The catalogue's "CSP Spain
I not matched" should go. Date: Tortosa, 28 Dec. 1495. Direction: Ferdinand and Isabella → De Puebla.

## Remaining gaps

- The cipher copy beyond the sample (most of pp. 1-4) - blocker: not-attempted; doc. 124 is not transcribed beyond p. 1 ll. 6-8 and p. 2 ll. 1-6, and PARES answers HTTP 429 to this machine (27 Oct, 14 Nov 2026), so the leaves were not opened again. The reason first given (a full reading would only add the wording differences Bergenroth mentions) no longer stands: since 14 Nov 2026 a Spanish clear text of the same despatch is transcribed in `dudout/` (AGS PTR leg. 52 doc. 129, Brice Dudout; pp. 1-2 and 15 settled, pp. 3-14 two raw passes), so a full decode could be checked word by word against Spanish and would give values for the open groups. Workable: transcribe the four pages of doc. 124 from PARES in a browser, decode with doc. 33, align with doc. 129 (`align_doc129.py` does it for the sample)
- Doc. 129 pp. 3-14 - blocker: not-attempted; two raw passes that agree on the outline and differ in many words (`dudout/`), not arbitrated; no reading of doc. 124 can be checked against them yet. Doc. 130 (PARES 2207853), a second clear text by the contributor's report, is not transcribed
- Groups 883, 1374, 1335, 1813, 852, 868, 1221 and the "xxix" on p. 2 l. 1 have no value from the key yet (candidates from doc. 129 for 1813, 1221 and 29, none of them seen on the key: section of 14 Nov 2026 below) - blocker: open-codes; the key is online (AGS PTR leg. 52 doc. 33, PARES show/2207755), but in the review of 27 Oct 2026 PARES answered HTTP 429 to every request from about 11:45 to 13:10, so key images 3-9, 47-51, 70-75, 78-84 and 110-113 (where interpolation from the images already read puts these numbers: 852/868/883 on images 47-51, 1221 near 72, 1335/1374 near 80-83, 1813 near 112, 29 near 5) could not be opened. Tomokiyo's published values do not include any of them. Fill them on the next session that can reach PARES.
- Whether the ring over the C ligature ever adds a C - blocker: open-codes; the rule from the 616 key images is applied, but it was not checked group by group here

## Escalation

- [x] siblings: puebla1496 (catalogue 616, same code and key); CSP I nos. 117, 121, 130 for the couriers
- [x] clear-pages: the clear words of pp. 1-2 used for the identification; the Spanish clear text AGS PTR leg. 52 doc. 129 (PARES 2207852), reported by Brice Dudout (issue #609) and transcribed by him on 14 Nov 2026 (`dudout/`, PR #623): its settled pp. 1-2 hold the clear lines of doc. 124 p. 2 and stand beside eight of its cipher groups (`doc129_alignment.txt`)
- [x] known-keys: AGS PTR leg. 52 doc. 33, key images 20, 24, 49, 51-53, 55, 60, 66, 80, 100, 103-106, 111
- [x] print: CSP Spain I pp. 57-107 (BHO), nos. 113-114; the 1868 Supplement starts in 1498
- [n/a] key-rebuild: the key is extant and needs no rebuilding
- [x] retry: month group corrected to otubre; DCCCLV read on the key

## Maintainer review, 27 Oct 2026

Claude, reviewing for Daniel Bourdeau. The sample reads as sentences only where it is clear text (p. 2 ll. 2-6); the
ciphered part decodes to function words and the month, coherent but with five code groups open. Grade B, replacing
the contributor's self-grade. The outcome is changed from "already solved" to "read in part" (sample, read with known
key): Bergenroth's no. 113 is an abstract of the clear draft, not a decipherment of the cipher copy, so his credit is
a pointer, not a prior solution. No write-up: only a sample of the cipher copy is decoded and the content is in print.
The key images for the open groups could not be opened (PARES HTTP 429 all session; see Remaining gaps).

## Files

- `sample_transcription.txt`: p. 1 ll. 6-8 and p. 2 ll. 1-6
- `key_excerpt.tsv`: the key entries used, with their key images
- `decode_sample.py`: decoder and controls, standard library (`python decode_sample.py`)
- `sample_decryption.txt`: line-by-line output of the decoder
- `sample_reading.txt`, `sample_translation.txt`: the sample as sentences, and in English
- `dudout/`: Brice Dudout's transcription of the clear text doc. 129 (README, settled text, two raw passes), PR #623
- `align_doc129.py`, `doc129_alignment.txt`: doc. 129 set beside the sample of doc. 124 (integration check, 14 Nov 2026)

No images are in the folder. The pages are on PARES (links above).

## A Spanish clear minute reported: AGS PTR leg. 52 doc. 129 (issue #609, 14 Nov 2026)

Brice Dudout (issue #609) reports that AGS, Patronato Real, leg. 52, doc. 129 (PARES description 2207852, 20 images)
is a Spanish minute in clear with the same "commercial" drafting as doc. 124, signed Fernand Álvarez, at Tortosa, and
that its "fagamos ... guerra al Rey de Francia" corresponds to doc. 124 image 1 line 22. The issue is a pointer only:
doc. 129 is not transcribed. (Later the same day he transcribed it, PR #623: next section. The points below are the
state before that.)

- Not verified here. One request to the PARES description page on 14 Nov 2026 was answered HTTP 429 (Too Many
  Requests), the block this folder met on 27 Oct; it was not retried and not got round. Nothing of the record (title,
  date, extent, signature) has been seen by the project. PARES needs a browser session.
- Not checkable against this folder's files either: the sample here is p. 1 ll. 6-8 and p. 2 ll. 1-6; line 22 of
  image 1 is not transcribed, so the correspondence the issue names cannot be tested from what is here.
- In the repository: no file mentioned PARES 2207852 or doc. 129 before this section (`git grep`, 14 Nov 2026).
- What it would change if it holds. Bergenroth's no. 113 is an English abstract of "the clear draft"; a Spanish clear
  text of the same despatch in the same legajo would be that draft or a copy of it (not established: the old mark
  on doc. 129 has not been read). The reason given above for not reading doc. 124 in full (the content is known only
  through the English abstract, and a full reading would add only wording differences) would no longer hold as it
  stands: doc. 124 could be decrypted in full with the key of doc. 33 and compared group by group with a Spanish
  clear, which would also give values for the open groups (883, 1374, 1335, 1813, 852, 868, 1221) independently of
  the key images. The outcome method would stay "read with known key"; the clear minute would serve as the check.
- Next step (not done): open PARES 2207852 in a browser, confirm date, place, signature and old mark, transcribe the
  minute, then decrypt doc. 124 in full and align the two. Status stays "no write-up" until then.

## Doc. 129 transcribed by Brice Dudout (PR #623), and set beside doc. 124 (integration check, 14 Nov 2026)

Brice Dudout (with Claude) filed `dudout/`: the settled text of pp. 1-2 and p. 15 of doc. 129 with its old marks and
endorsements, and two passes over all 15 pages, the second blind to the first. His commit is unchanged. He did not
decrypt doc. 124 and did not align it. The check below is Claude's, for Daniel Bourdeau; `align_doc129.py` writes
`doc129_alignment.txt`. Nothing was seen on the images: PARES answered HTTP 429 to one request for record 2207852.

**The two passes on pp. 1-2** (words that agree in order, spelling levelled): pass 1 against the blind pass, 136 of
165 on p. 1 (82 %) and 102 of 137 on p. 2 (74 %). The settled text follows the blind pass on p. 1 (150 of 165) and
pass 1 on p. 2 (133 of 136; the blind pass 102 of 137). On p. 2 ll. 3-8 the blind pass reads other words ("{saluador}
{ourncia} de {corpos} / {de la} compañia no vos {rrespondemos} ..."), and pass 1 was made by a reader who knew the
clear lines of doc. 124 printed in this folder (only pass 2 is blind). So the settled p. 2 is consistent with its
passes, and its ll. 3-8 rest on pass 1 and the arbitration.

**The clear lines of doc. 124 in doc. 129.** Doc. 124 p. 2 ll. 2-6, from "partio de aca" to "cargo dello", is 103
words. In the settled text of doc. 129 (image 1 l. 16 to image 2 l. 10) 99 of them stand in order (96 %): the claim
"word for word, apart from spelling and numerals" holds, with three differences: doc. 129 has "siguiente e" where the
sample has an unread word and "y" after "mayo", "porque caminando" for "que caminando", "ternan" for "terna". In the
blind pass alone 75 of the 103 stand (73 %): the five sending dates, "con ... salvador", "compañia no vos", "porque
camina-", "en ningun lugar para vos poder", "agora que los fatores de la compañia", "adelante como lo dezis que los
fatores de la compañia ternan cargo dello". That is enough to say the two documents carry the same passage without
leaning on pass 1. The unread word of doc. 124 p. 2 l. 2 would be "siguiente", and "[poco?]" on l. 4 is "poco" in the
settled text (pass 1 only).

**The cipher groups against the clear text.** Only the sample of doc. 124 is transcribed, and its p. 1 ll. 6-8 lie in
the opening that doc. 129 has lost ("faltale el principio"). So eight groups can be set beside doc. 129, those of
p. 2 ll. 1-2:

    doc. 124   dezia sea hecho . <1813> <852?> <868> <1221?> <638> <29?> <1885> <855> . partio de aca
    doc. 129   dezis sea fecho porque {desde|despues} {alli|aca} en fin de abril que el dotor partio de aca

- The three groups that have a value from the key stand against their own words: 638 de / "de", 1885 que / "que",
  855 dotor de puebla / "el dotor". 3 of 3. Controls: the alignment moved by one or two words either way, 0 of 3;
  10,000 shuffles of the sixteen values of the key excerpt, 3 of 3 once, 2 of 3 in 145, none in 8,185. With three
  groups this shows the two texts run in step here; it is not a test of the key.
- Candidates for open groups, from the clear text only, none seen on the key: **1813 = porque** (first group after
  "sea hecho", against "porque"; it lies between "poco ..." 1778-1783 and "que" 1885 in the key's alphabetical run);
  **1221 = fin** and **29 = abril**, counting back from "de" (both groups are marked doubtful in the transcription;
  29 would stand at the head of the a's, 1221 between "el" 939 and "y" 1329). They stay candidates until key images
  5, 72 and 112 of doc. 33 are opened.
- **852 and 868 are not settled.** Two groups stand against "{desde|despues} {alli|aca} en": three words, two of them
  read differently by the two passes. By count 868 would be "en", but 868 lies between "dotor de puebla" 855 and "el
  papa" 870, and 852 two entries before "dotor de talavera" 854, where "desde" or "despues" would not be expected in
  an alphabetical list (852 is marked doubtful in the transcription; da for dar, DCCLII, would put it among the
  des-; not seen). 883, 1374 and 1335 have nothing to stand against.
- Wording: "dezia sea hecho" in doc. 124 against "dezis sea fecho" in doc. 129.

**What this changes.** The identification with CSP no. 113 gains a Spanish text in the same legajo with the same old
mark (T. c. Y. 2), the same place and day, and endorsed "Descifrada" (by the contributor's transcription; the year
word is doubtful, "seys" or "çinco"). The outcome stays "read in part" (sample, read with known key); no page of
doc. 124 is claimed read beyond the sample, and nothing is claimed for the pages of doc. 129 that are not settled.
Status stays "no write-up". Credit: Brice Dudout, transcription of doc. 129.
