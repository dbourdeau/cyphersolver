# Deboli → Stanisław August, St Petersburg cipher despatches, 1788 (Unsolved Catalogue 417)
Status: read in part (Brice Dudout, 28 Oct 2026; no. 038 of 13 May 1788, 911 of 943 groups with a key value, about 0.86 read as sense on a held-out pair).

Contributed by Brice Dudout (Europe chiffrée, https://bdudout.github.io/europe-chiffree/), with Claude Opus 5.5 agents.
The key is Daniel Bourdeau's 1789 key (`targets/deboli1789/key_pass.tsv`), completed on 1788 pairs.

## The volume and its decipherments

AGAD Warszawa, Zbiór Popielów (zesp. 12) 428: 112 cipher despatches of Deboli to the King, 4 Jan - 26 Dec 1788
(letter list https://www.agad.gov.pl/inwentarze/ZbPop428.xml; scans http://agadd2.home.net.pl/metrykalia/12/album/428/).
The cabinet's Polish decipherments are the same-date texts in ZbPop 417 (list ZbPop417.xml), as `deboli1790` found for
the new-code despatches.

- **The older code is deciphered too.** The 4 Jan pair (428 k. 1 / 417 k. 17, "reçu le 15") and the 11 Jan pair (428 k. 5 /
  417 k. 20, "reçu le 22") align on their opening lines: `1332 1332` = "do do" at the only doubling ("do doniesienia"),
  `158` = "ni" in nic / doniesienia / nikim, `1970` = "Nie-" opening both letters, `803` + KMci (`1413a`, `1328 1015a`) and a
  homophone `277a` for the second "W" of WKMci on 11 Jan. So the despatches in the older code have their decipherment in
  ZbPop 417 as well (existing decipherment).
- **Pairing:** every despatch of 428 has a same-date text in 417 except nos. 038 and 039. No. 104 is 28 Nov (AGAD list
  typo "1788.11,28"); no. 059, dated "21 Juillet" on its verso, is 11 July by the order of the leaves (428 has no other
  11 July) and matches 417 k. 179.
- **The two codes alternate through the whole year**, not only until the spring: the older code (groups to about 2450;
  992, 893, 787, 1332 frequent) is still used on 25 July, at the opening of 8 Aug (switching to the new code at `4000`
  on k. 150r), and on 23 Sept 1788; the 1789-91 code is used on 13, 20, 30 May, 3 June, 29 Aug, 4 and 11 Nov.

## The despatches of 13 May 1788 (nos. 038 and 039): no clear text

ZbPop 417 jumps from 9 May (k. 113-116) to 16 May (k. 117). Both 038 (k. 74-75v) and 039 (k. 76-77v) are dated
"St Petersbourg ce 13 May 1788" and signed Deboli. The 3 June decipherment (417 k. 139) refers to this letter:
"słów Bezborodki do mnie wyrzeczonych, o których doniosłem WKMci w liście de 13. Maji".

- **038** (943 groups, 1789-91 code without a leading 4000) is transcribed in full and read in part here.
- **039** opens in another table (groups 2300-3409, framed by 9933, the French table also seen in Dec 1789) and ends with
  about 30 groups after 4000 in the Polish code. Not read. The 9 May 1788 despatch (428 k. 71-73) uses the same 9933
  table and has its French clear text (417 k. 113-114): a pair to start that table.

Content of 038 (gist secure, details not): a great dinner given "for that famous privateer lately taken into the service
here" (very probably John Paul Jones, who joined the Russian service in spring 1788); Stackelberg at table; Deboli voices
Polish unease at the King of Prussia's designs; the answer that the project of alliance will be prepared to be concluded
at the Diet, "which we shall try to turn into a Confederation", and the words "the essential thing is that we should be
able to come to your aid when it is needed; the rest of the arrangement will only be for security"; two impressions of
Deboli, the second coming from "the words underlined above, which I do not well understand" (underlined groups on k.75r);
an arrangement "with Ostermann" about Gdańsk.

## Key K4

`key_K4.tsv` = `targets/deboli1789/key_pass.tsv` unchanged + additions learned only on 1788 pairs (cipher despatch /
same-date decipherment): 12 values and 3 nulls (C02: e.g. 1085 Osterman, 1420 Stackelberg, 1980 Austr-, 2181 de Caché),
6 values attested at least twice (C03), 11 alternative values added automatically (C04: e.g. 637 list|ła, 360 ie|nie).
Each stage was frozen (SHA-256 in the key header) before its validation pair was opened. Learning pairs in `pairs/`
(20 May, 30 May, 3 June, 29 Aug, 4 Nov 1788).

## Measures (honest)

Validation on a pair never used for learning: 11 Nov 1788 (428 no. 099, k. 235r + 235v ll. 1-11, 341 groups; clear text
417 k. 276-277, 176 words), `validation/`. Measure written before computing: the cipher groups are aligned (dynamic
programming) on the cabinet's decipherment; a group is **read as sense** if it is a null, or if its value (or one of its
alternatives) equals the aligned stretch of clear text, up to two letters of ending or one letter of spelling.

| measure | K4 | 200 shuffled controls |
|---|---|---|
| groups read as sense (`scripts/sense.py`) | **0.862** | max 0.199, median 0.152 |
| exact words (`scripts/measure.py`) | 0.750 | max 0.131 |
| characters (`scripts/measure.py`) | 0.882 | max 0.289 |
| words within two letters of ending | 0.909 | - |

K3 gives 0.859 on the same pair, and 0.836 on 8 Aug 1788 (also held out). The score plateaus near 0.86 even on learning
pairs (0.83-0.84): part of the gap is the alignment itself, part is that the code writes stems and syllables and the
cabinet supplied endings from the sense. So the true share of 038 that is read is nearer 0.86 than the **96.6% of groups
with a key value** that `read.py` counts (911 of 943). Hence "read in part".

## Files

- `transcription/c038_1788-05-13.txt`: the 943 groups (0/8 loop ambiguities marked `^`).
- `reading/c038_1788-05-13.decoded.txt`: line by line, groups and values.
- `reading/c038_1788-05-13.txt`: Polish text in sentences, holes marked; `reading/c038_1788-05-13_en.md`: English.
- `key_K4.tsv`, `pairs/`, `validation/`, `scripts/` (`python3 scripts/sense.py key_K4.tsv validation/c099_1788-11-11_cipher.txt validation/p098_1788-11-11_clear.txt 200`).

Next step: a group-by-group human review of 038 (and of the held-out pair) to settle the alternatives and holes; the
French table of 039 from the 9 May 1788 pair.
