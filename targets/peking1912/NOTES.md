# peking1912: Peking telegram on the restoration of the Dalai Lama's title, October 1912 (lead 2465)

Status: read (Brice Dudout, 11 Nov 2026; class already solved; 31 codes, 30 certain + 1 doubtful = 96.8%; plain Chinese standard telegraph code read by rows; translated approximately in English by the General Staff in 1912, so not a first break).

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent (protocol, reading, controls, write-up).
Lead **2465**, found by Daniel Bourdeau in the Abhilekh Patal sweep, who suggested trying the standard telegraph code and
Campbell's 1907 key (lead 2466).

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
written and hashed before the attack. It fixed the crib words from the 1912 translation, the hypotheses (H0 plain code in
several orders and cuts; H1 a 5-digit additive; H2 Campbell's "transparency" relation; H3 the General Staff's column formula of
1908; H4 a 4-digit additive) and the success criteria. H0 by rows worked at once; H1-H4 were not run.

Controls (`frozen/controles.py`, output `frozen/controles.out`; needs a code table built from Unihan, not included):
crib score by rows 19, by columns 0; 1,000 random orders of the 25 groups max 6 (mean 1.22); 1,000 random 4-digit
additives max 1. The two halves of the text read independently (scores 14 and 5).

## Reading

電悉。大總統早經允准復回達賴名號，並允到京，格外歡迎優{徇 → 待}。是否通過，速覆。

"Telegram received. The President has long since approved restoring the Dalai [Lama]'s title, and also allows him to come
to the capital, where he will be welcomed with exceptional favour and generous treatment. Reply quickly whether [this] has
got through or not."

- 30 of 31 characters certain. Code 1770 gives 徇; read 1769 = 待 (優待, the General Staff's "generous treatment").
- The General Staff's reading **A** ("the restoration of the Dalai Lama's title") is right: 復回 governs 名號.

## Prior work

General Staff, Simla, 8 Oct 1912: approximate English translation in the same file (credited `india_general_staff`, prior
solution). Lead 2465 open as checked 11 Nov 2026; web search found nothing printed.

## Remaining gaps

- Code 1770 (illegible: a one-digit slip; the copy itself is clear).
- Sender and addressee, and "Yaoshikinan" of the record title (needs-physical-access: other pages of the file, the Kalimpong duplicate).
- Context to check: historians date Yuan Shikai's order restoring the title to 28 Oct 1912; this telegram, received by 3 Oct, already says 早經允准 "long since approved".
