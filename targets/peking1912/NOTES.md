# peking1912: Peking telegram on the restoration of the Dalai Lama's title, October 1912 (lead 2465)

Status: read (Brice Dudout, 11 Nov 2026; integrated 12 Nov 2026; method read with known key, class read; 31 codes, 30 give the character as written = 96.8%, 1 emended and not counted; plain Chinese standard telegraph code read by rows; translated approximately in English by the General Staff in 1912, so not a first break). The transcription has not been checked against the image by anyone but the contributor.

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent (protocol, reading, controls, write-up).
Lead **2465**, found by Daniel Bourdeau in the Abhilekh Patal sweep, who suggested trying the standard telegraph code and
Campbell's 1907 key (lead 2466). Pull request #431.

## Document

National Archives of India, Foreign Department, **Deposit Cypher, 1912, Nos. 86-87**, 14 pp. (Abhilekh Patal
PR_000004118254; duplicate PR_000006222155). Record title: "Message in Chinese Cypher from Yaoshikinan, Peking which cannot be
properly decyphered". Seen after login in the online reader; **no image is included** (no reuse licence shown).

- p. 3: Viceregal Lodge, Simla, 3 Oct 1912: a telegram received in an unknown code, "We have been unable to decypher this".
- p. 4: two identical telegrams (one through Kalimpong); draft to Col. A. H. Bingley (General Staff).
- p. 6: the groups, 25 groups of five digits, copied in four columns (7, 6, 6, 6).
- p. 8: Bingley, 8 Oct: a translation "so far as we can make sense of it"; suspects a trap (a test of whether the British read the Chinese code).
- p. 9: the General Staff's translation, two readings (A, B) "according to the placing of the stops".
- pp. 10-13: telegrams of 9 Oct 1912 to Bengal and to the British Minister at Peking: "Probably it is a trap".

## System

No cipher: the **Chinese standard telegraph code** (four-digit codes), sent in groups of five digits. The 125 digits read
**by rows** (four groups per row, as the groups were sent) form one stream of 31 four-digit codes plus one filler digit (the
final 0). Read down the columns, as the copy is laid out, it gives nonsense, which explains the Foreign Department's failure.
Table: Unicode Unihan (`kTaiwanTelegraph`, `kMainlandTelegraph`), Unihan.zip from unicode.org, SHA-256 4c93ea9c...; codes used
in `key.tsv` (CC BY 4.0).

## Method and controls (`frozen/`)

The protocol (`frozen/PREREG.md`, in French, SHA-256 463105518d1693e8092eb5a673c4d4435b4be1edb37a4677fc545a6e5a24a36d) was
written and hashed before the attack, by the contributor's record (the pull request is a single commit). It fixed the crib
words from the 1912 translation, the hypotheses (H0 plain code in
several orders and cuts; H1 a 5-digit additive; H2 Campbell's "transparency" relation; H3 the General Staff's column formula of
1908; H4 a 4-digit additive) and the success criteria. H0 by rows worked at once; H1-H4 were not run.

Controls (`frozen/controles.py`, output `frozen/controles.out`; needs a code table built from Unihan, not included):
crib score by rows 19, by columns 0; 1,000 random orders of the 25 groups max 6 (mean 1.22); 1,000 random 4-digit
additives max 1. The two halves of the text read independently (scores 14 and 5).

## Reading

電悉。大總統早經允准復回達賴名號，並允到京，格外歡迎優{徇 → 待}。是否通過，速覆。

"Telegram received. The President has long since approved restoring the Dalai [Lama]'s title, and also allows him to come
to the capital, where he will be specially welcomed and generously treated. Reply quickly whether [it] has passed or not."

- 30 of 31 codes give the character as written. Code 1770 gives 徇; 待 (1769, one digit away) is an emendation, giving the
  set phrase 優待 (the General Staff's "generous treatment"). An emended code is a supplied value and is not counted as read.
- The General Staff's reading **A** ("the restoration of the Dalai Lama's title") is right: 復回 governs 名號.
- 是否通過 is ambiguous (corrected 12 Nov 2026; the first version of these notes settled on "whether the telegram got
  through"). It can mean whether the telegram got through, whether the matter has passed or been agreed, or whether he will
  travel through. The General Staff saw the same doubt in 1912 ("whether or not pass(ed) through": persons crossing a
  frontier, or telegrams reaching their destination). The text does not decide.
- The telegram speaks of the President (大總統) in the third person, so the sender is an official at Peking, not Yuan
  Shikai (corrected 12 Nov 2026; lead 2465 was titled "Yuan Shikai (Peking) → unknown"). The telegram names neither
  sender nor addressee.

## Prior work

General Staff, Simla, 8 Oct 1912: approximate English translation in the same file (credited `india_general_staff`, prior
solution). Lead 2465 open as checked 11 Nov 2026; web search found nothing printed. No Chinese text of the telegram was
found; the Chinese printed document collections were not searched (see Remaining gaps).

## Integration check (12 Nov 2026)

Pull request #431, verified independently before integration; the corrections below come from that verification.

- **Decoding reproduces.** A decoder written for the check, with a code table built from Unihan.zip (same SHA-256 as
  `key.tsv` states), gives 31 codes and one filler digit, and all 31 codes give the character in `decryption.txt`.
  `frozen/controles.py` rerun with that table gives the output in `frozen/controles.out` byte for byte (rows 19, columns 0,
  random orders max 6, additives max 1, halves 14 and 5). Other cuts tried at the check (row offsets 1-3, columns at four
  offsets, dropping one digit of each group at each of five positions) give gibberish.
- **Protocol.** The SHA-256 of `frozen/PREREG.md` matches, and the crib list in `controles.py` is the list in the protocol.
  That the protocol was hashed before the attack rests on the contributor's record. The method has no free parameter.
- **Emendation.** 1769 = 待 and 1770 = 徇 in the table; none of the other 35 one-digit neighbours of 1770 gives a word
  with 優. The gap was labelled "illegible"; it is an emendation of a clear copy, not an illegible sign.
- **Read share**, by the README read bar applied as written: 30 of 31 codes = 96.8%; the emended code is not counted.
- **Class and provenance.** Method read with known key (the text is in code and cannot be read without the table; no
  Chinese text existed). Class changed from "already solved" to "read", with the General Staff's English translation
  recorded as the prior solution, as `targets/ctcplain1913` (plain telegraph code, same contributor) is filed. Provenance
  changed from "mixed" to "contributed": the project supplied the lead and this check.
- **The General Staff's 1912 translation** was checked only against the contributor's quotation of p. 9 in
  `frozen/PREREG.md`. On that wording, its "Extremely gratified at generous treatment" mistranslates 格外歡迎優待.
- **Not checked: the images.** `abhilekh-patal.in` shows a human check to scripts (HTTP 202 with an empty body to the
  record pages at verification); nothing was done to go round it. The 25 groups have been read on the page only by the
  contributor's agent, from his logged-in screen captures.
- **Sender.** "Yaoshikinan" of the record title may be 姚錫光 (Yao Xiguang), an official of the Mongolian and Tibetan
  Affairs Bureau in 1912; this is a suggestion made at verification from memory, not checked against any source.
- **Date.** The telegram has no date code; "received by 3 Oct 1912" comes from the file (p. 3).
- `python docs/_check_profile.py peking1912`: valid. `python docs/_check_terms.py peking1912`: no finding.

The same public code table reads `targets/ctcplain1913` (20 telegrams of Sun Yat-sen's circle copied in Japan, 1913-16) and
`targets/nanking1930` (Chiang Kai-shek and Ma Fuxiang to the Dalai Lama, 1930, from another National Archives of India
file). They are separate entries: other archives or files, other correspondents, and here a reading order that had to be found.

## Remaining gaps

- code 1770 (徇, read 待 by emendation) - blocker: needs-physical-access; the copy as transcribed reads 71770, so the slip is in the transmission or the Simla copy, or in the transcription; only the image (behind the archive's login and human check) or the original telegraph form can tell which
- image check of the 25 groups of p. 6 by a second reader - blocker: needs-physical-access; Abhilekh Patal shows a human check to scripts and the pull request carries no image (no reuse licence shown), so only someone logged in can do it
- sender and addressee, and "Yaoshikinan" of the record title - blocker: needs-physical-access; the telegram names neither; pp. 3-5 and 7 of the file and the Kalimpong duplicate may help, and they are behind the same login
- prior art in Chinese printed document collections (a Chinese text of this telegram) - blocker: needs-physical-access; printed volumes, none opened by the contributor, at verification or here; one web search on the Chinese phrases at verification found nothing

Context to check, not a gap of the reading: historians date Yuan Shikai's order restoring the title to 28 Oct 1912; this
telegram, received by 3 Oct, already says 早經允准 "long since approved". (The date of the order is from the contributor's
notes and was not checked here.)

## Escalation

- [x] siblings: the duplicate record PR_000006222155 and the Kalimpong copy are named in the file; lead 2466 (Campbell's 1907 key, NAI File 45506) was prepared as hypotheses H2-H3 and not needed
- [x] clear-pages: p. 9 is the General Staff's English translation (two readings); no Chinese text in the file as seen by the contributor
- [x] known-keys: the public standard telegraph code (Unihan, Taiwan and Mainland fields) reads all 31 codes
- [x] print: web search by the contributor and one at verification, nothing; Chinese printed collections not opened (Remaining gaps)
- [n/a] key-rebuild: the key is a public table; nothing to rebuild
- [x] retry: all 36 one-digit neighbours of 1770 run at verification; only 1769 待 gives a word with 優
