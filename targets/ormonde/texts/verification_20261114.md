# Maltravers to Ormonde: verification of 14 Nov 2026

By Brice Dudout (*L'Europe chiffrée*), with Claude Opus 5.5. This checks the reading of 15 Sept 2026 again and adds to it.
Sources: HMC *Ormonde* I (1895) pp. 28–29, from Internet Archive `calmarqormonde01greauoft`, page images n43 and n44.
Knowler, *Strafforde's Letters* I (1739), from the OCR of Internet Archive
`bim_eighteenth-century_the-earl-of-straffordes_strafford-thomas-wentwo_1739_1`. The figures below are given by OCR line.

## 1. The print checked again

The two page images were read again for all 59 figures. They agree with `ciphertext.txt`, comma for comma, including
the missing comma in `174 99`. On a close crop, **26** in *angry* and **31** before 174 are clearly printed as such.
The check was done after reading `ciphertext.txt`, so it is not blind. The manuscript (NLI, Ormonde Papers) is not
online, so a misprint by the HMC transcriber cannot be ruled out. The page also prints a third letter from Maltravers,
from Adare on 30 Sept 1634, and a fourth from Arundel House on 10 July 1635. Neither has any figures, so there is no
further ciphertext under this key.

## 2. Code 185 read: the Lord Deputy (probable)

Letter 2 reads: *You desire to know what 93 **185** 95 hath written unto 99 **149** concerning Crosby … of which I can
give you no account of at all … 95 **186** 98 hath written unto 98 **218** 97 much in praise of [Ormonde] … and upon
his motion [Ormonde] is to be a councellor.*

1. **The same sentence frame.** The two clauses have the same shape, *X hath written unto Y*, and each name stands
   between nulls. Maltravers answers Ormonde's question about the letter on Crosby by passing on what he knows of the
   Lord Deputy's letter.
2. **Knowler shows a single dispatch.** In Knowler vol. I, the only writing of Wentworth on Crosby before 22 Jan 1635
   is the dispatch *The Lord Deputy to Mr. Secretary Coke*, signed "Dublin-Castle this 16 of December, 1634" (OCR
   l. 40578–41476). Its items 17–18 deal with Crosby's vote against the bill on murders and his "cautelous Petition
   for his restoring to the Board" (l. 41106, 41229). The same dispatch praises Ormond and proposes to make him "a
   Counsellor … the Exchange of the Earl of Ormond for Sir Piers Croſby" (l. 41324). So the letter Ormonde asked
   about and the letter Maltravers reports on are one dispatch, and its writer is the Lord Deputy. The other hits in
   Knowler are later and do not change this: Coke's answers of March–April 1635 (l. 45534, 49944), Coke's letter on
   Crosby coming over without leave (l. 55063), and Howell's letter of 1 Jan 1635 (l. 58548).
3. **Two figures for one name.** 185 sits next to 186. In this key every letter has a block of consecutive figures
   (b 7–9, c 10–12 …), and Maltravers uses a second figure of the block when he doubles a letter (49 50, 28 29, 11 12).
   A nomenclator built the same way would give the Lord Deputy both 185 and 186.

Point 3 depends on how the blocks are aligned, and the vowels leave that open (see §3), so it is only supporting
evidence. Points 1 and 2 are what make 185 probable.

**149 stays open.** Wentworth sent the 16 Dec dispatch to Coke, and that same day he sent duplicates to Laud: "You will
find by these Duplicates of my Letters to the Secretary" (l. 40491, letter to "your Grace", 16 Dec 1634). 149 is
therefore Coke under a second figure (218 being Coke), or Laud, or the King, whom 143 already names. The text gives no
way to decide.

## 3. The vowel blocks are still not fixed

Option A gives each vowel 5 figures (64–88). Option B gives a 3 figures and each other vowel 6 (64–90), so every block
starts on a figure ≡ 1 (mod 3), as the consonants and the nulls (91) do. Under B, 89 = u, which makes *letteru*. That is
a second misfit beside 26, so on the text alone B does not do better than A. Both are kept, and the reading does not
depend on the choice. A frozen key with option B written in (SHA-256
`b30e4206e7120b19d2fed91be78fc7c666cfa85c349417519ee98d20f269691b`) records the proposal. **Not measurable:** the text
has 59 figures, 28 of them letters, so no fresh portion of 150 groups or 300 signs exists.

## 4. Date corrected

NOTES §4a gives the Ormonde dispatch as "Dublin 22 Dec. 1634". In Knowler it is signed **16 Dec 1634** (l. 41476). The
letter dated "Dublin, 22 Dec. 1634" (l. 41609) is a different one, to Lord Cottington, and does not mention Crosby or
Ormond.

## 5. Strict count (cipher units, nulls left out)

| unit | figures | value | grade |
|---|---|---|---|
| 1 | 65 35 21 26 59 | angry (26 = k by the grid) | probable |
| 2 | 113 | with / against | probable |
| 3 | 186 | the Lord Deputy | sure |
| 4 | 143 | the King | sure |
| 5 | 28 69 49 50 70 44 89 | letter[s] | sure |
| 6 | 186 | the Lord Deputy | sure |
| 7 | 185 | the Lord Deputy | **probable (new)** |
| 8 | 149 | ? | unresolved |
| 9 | 10 44 79 47 8 59 | Crosby | sure |
| 10 | 270 | Crosby (assigned in the letter) | sure |
| 11 | 186 | the Lord Deputy | sure |
| 12 | 218 | Secretary Coke | probable |
| 13 | 174 | Ormonde | sure |
| 14 | 221 | the Parliament | probable |
| 15 | 31 | ? (m by the grid) | unresolved |
| 16 | 174 | Ormonde | sure |
| 17 | 64 | a | sure |
| 18 | 11 79 85 35 12 69 28 29 79 44 | councellor | sure |
| 19 | 174 | Ormonde | sure |

Sure 12, probable 5, restored 0, unresolved 2. That makes **17 of 19 cipher units read as sense (89.5%)**, against 16 of
19 (84.2%) before. Counting the words of `letters_reading.md` (clear text and cipher, 133 words), 2 are unread, so
131/133 (98.5%). The share Daniel's tool recorded on 24 Oct was 93.8%, and that tool also counts the `[?…]` marks as
holes. On cipher units the reading is still under 95%: **read in part**.
