# 1567: final check before the ledger

Written 3 Nov 2026 by an independent AI reader. No solver file was changed. No human palaeographer has checked anything here.

## Verdict: confirmed with corrections

The key, the system and the Italian hold on all eight documents, and the 1636 letter is the same key. The status table is
overclaimed in its numbers, not in its conclusions. Word totals are inflated, the 1636 strict count is wrong, one sign
swap survives in c. 7r, and three "lost" 1636 signs are on the page.

## 1. Blind test

Method. I read the signs from the strip sheets and full-resolution crops, and saved each reading before opening any
transcription, decryption or reading file. The readings are in the appendix. This was not key-free: I needed the sign
chart, and I recognised Italian as I went. VERIFY.md and the solver's key-free reader cover that side. The 73v strips are
at 0.72 scale, so I rechecked every dispute on the full-resolution blocks.

| Document | Signs read | Differences | Rate |
|---|---|---|---|
| c. 7r | 381 | 9 | 2.4% |
| cc. 9 | 286 | 3 | 1.0% |
| c. 11r | 258 | 2 | 0.8% |
| c. 13r | 220 | 6 | 2.7% |
| cc. 16 | 279 | 5 | 1.8% |
| cc. 20 | 212 | 1 | 0.5% |
| c. 23r | 232 | 2 | 0.9% |
| cc. 73-74 | 472 | 8 | 1.7% |
| All | 2340 | 36 | 1.5% |

Counts are edits in a local alignment of each segment to the solver's signs. I did not sample the last 244 signs of
cc. 73-74, chiefly c. 74r rows 8-15, or c. 7r l. 13-17.

After zoom, most of the 36 are my errors, unreadable signs or weak pairs:

- My errors: `c 2 A` for `c A` three times in c. 7r (the dotted d read as d + i); show-through taken for a box at c. 9r l. 5;
  the wide d read as two signs at c. 9v l. 1; c. 11r l. 7 and l. 10; c. 13r l. 4; c. 23r B5; c. 73v row 6 (one closed sign
  read as two).
- Weak pairs or stains, not decidable by shape: V/v three times; g against tailed t at c. 13r l. 6 ("quattro", supported by
  c. 15); the sign under the stain at c. 23r "irreparabile"; the blot at c. 20r l. 13 and c. 73v row 4.
- Solver wrong: c. 7r l. 8 (below), and the three edge signs of c. 73v (section 4). That is about 4 places in 2340, 0.2%.

My reading through the key gives the claimed sense, line after line, in every document. Examples: `noisiamorisolutidimostrarelafronte`,
`milanochenehanofattofuggirelemigliaiaper`, `bisognachesmsirisoluadapplicar`, `tesiperderanoisuostatiimperiali`.

### Is it the same key in 1636, and is it 1636?

Yes to both. All 20 values occur in my own 472 signs and give sentences with `key.tsv` unchanged. The hand is new and adds a
caret for doubles. The date line reads clearly "Di Mod.na li 2. feb.o 1636" (enlarged crop). c. 73r has "1636" pencilled at
top left and "S. Ottavio Bolognesi" at the foot. The content fits only those years: Savoy and Parma as allies with French
cavalry, Signor Siro out of his State.

The brief's "1 Feb 1636" is not this letter. The page says 2. In NOTES, 1 Feb is c. 72, to Forni.

Bolognesi's post: nothing opened places him in February 1636. He lived 1580-1646 and served Modena (inventory, search extract
only). The letter speaks of S. M., ministers and "stati imperiali", which fits an imperial court, and contradicts nothing.
Vienna in 1636 remains unproved. The Castelnovo di Sotto entry was not found in any source opened. Hanlon's account of
Modenese incursions against Parma in winter and spring 1636 fits the setting only in general.

## 2. Decryption rerun

My own script from `key.tsv` and the transcriptions: 4858 sign positions in 8 documents, 0 differences from the decryption files.
The sign counts in `key.tsv` match c. 23r exactly. Consistency only; it says nothing about the signs.

## 3. Agreement of the files

Reading against decryption, letter by letter: no unmarked change of letter in any document. Against that:

- **cc. 73-74: restored signs unmarked in the Italian.** The transcription and decryption bracket them, the notes mention
  most, but the reading prints them plain: almeno, però, infinitamente, siamo, costretti, disaggi. Also the n of sofrivano. The
  header says every such letter is marked. The 91.9% in NOTES rests on this.
- **Word totals are inflated.** The solver's counter in `readings_final.py` removes "At the foot..." only for the letter
  comparison, not for the count, so the editor's English is counted as cipher. Totals are 3 or 6 too high in c. 7r, cc. 9,
  c. 11r, cc. 16 and cc. 73-74.
- NOTES "One sign stays illegible" (1636) is false, and two editorial notes with it (section 4).
- Status header "8 of 13": seven letters are read, c. 13r is 8 lines only, five letters are unread.

## 4. Silent repairs and wrong signs

| Place | Page | Solver | Effect |
|---|---|---|---|
| c. 7r l. 8 | `x 3 9 2 g V T`, "strigne" | `x 3 9 2 V g T`, "stringe" | **Silent repair.** Same meaning, but the signs are swapped, unmarked, in a letter never retranscribed |
| c. 73v row 8 | last sign `A`, whole, past the strip end | `?`, "lost at the edge" | A legible sign called lost. "a Milano" stands on the page |
| c. 73v row 4 | last sign `N`, whole | `[N]`, "cut at the edge" | Same cause |
| c. 73v row 10 | `V N` legible | `[V] N` | Same cause |
| reading c. 73v row 7 | one sign | nece[ss]ità | Two letters for one sign; should be nece[s]ità |
| c. 74r row 0, sign 4 | vertical sides, unlike the clean triangle 6 signs on | `D`, "procetterci" | Leans to box: prometterci. Sense still open, so it stays doubtful |
| c. 13r l. 5, clear | fe + minims + o, looks like "fermo" | *ferro*, "by the sword" | Clear text, but a meaning claim. "promettere a fermo" fits better. Mark doubtful |
| c. 73r, clear | looks like "questa notte" | [?questa passata] notte | Check |

Cause of the three edge cases: the strip script stops at x = 4993 on a 5245 px block, and the paper runs on past it.

Held on zoom: c. 73v row 2 is the f shape, as the solver says; no[n] is a real editorial change. c. 73v row 10: the tick after
s and the open curve under the caret are as logged. The curve is not the reversed g of this hand, so disaggi is sense only.

The later hand of c. 15 and c. 22 is the key's source. So the key was got from a later clear copy, not by cryptanalysis. Dan
should be told that plainly.

## 5. Words and status

My counts, cipher passages only, elisions split, editor's English removed.

- A: words reading as sense, doubtful words out.
- B: A, also without writer's slips and changed readings (no[n], circo[s]tanze, confiden[t]i, qualco). Lost or blotted signs
  stay, and so do the closed a and open c, a shape variant seen in several letters.
- C: no restored or changed letter at all, unmarked ones included.

| Document | Solver | Words | A | B | C | Status |
|---|---|---|---|---|---|---|
| c. 7r | 109/110 | 107 | 106 (99.1%) | 106 | 106 | read |
| cc. 9 | 257/258 | 252 | 251 (99.6%) | 250 | 245 (97.2%) | read |
| c. 11r | 65/65 | 62 | 62 (100%) | 61 | 61 (98.4%) | read |
| cc. 16 | 216/217 | 211 | 210 (99.5%) | 209 | 197 (93.4%) | read |
| cc. 20 | 50/50 | 50 | 50 (100%) | 48 (96.0%) | 42 (84.0%) | read, margin one word |
| c. 23r | 68/68 | 68 | 68 | 68 | 68 | read, transcription job |
| c. 13r 8 lines | 58/58 | 58 | 58 | 58 | 55 (94.8%) | read in part, transcription job |
| cc. 73-74 | 159/160 | 154 | 153 (99.4%) | 147 (95.5%) | 135 (87.7%), 136 once row 8 is fixed | read, provisional, margin nil |

Decision on the flagged three. Dan's test is words reading as sense, and a marked hole does not stop a word reading. His
5% is meaningless if every slip may be corrected and then counted, so B is the honest test. All three pass B. cc. 16 is safe.
cc. 20 and cc. 73-74 pass narrowly, and cc. 73-74 needs a second full reader to stand. Print A, B and C for every
document, and do not rest "read" on A alone. Also disclose the sense-settled calls: 117 n/h places, tailed t/g, closed a, open c.

"Read" means the cipher. Clear passages are a first pass. **Entry: read in part. 7 letters read, c. 13r read in part, 5 unread.**

## 6. Prior art: open

Eight calls used.

Could not open: Doglio, *Lettere* (1967), no scan found, though the volumes are confirmed as 1609-33, 1634-37, 1638-46; the Reggio
inventory (DNS failure); the 1843 *Memorie* (Google Books redirect, not followed at the call limit); Muratori, *Annali*, 1636, passage
not found; Hanlon, *The Hero of Italy*, seen as an extract only.

New to the file: B. A. Raviola (ed.), *Corti e diplomazia nell'Europa del Seicento. Correggio e Ottavio Bolognesi (1580-1646)*,
Mantova 2014. It is the first place to look for his posts and his ciphers. Not opened.

Scans said to be open at HathiTrust, not opened: *Opere scelte* (1817), De Castro, *Fulvio Testi e le corti italiane* (1875). No
letter collection by Testi is listed there. Nothing found shows these letters printed, and nothing shows they are not. Claim
no novelty.

Sources: [Reggio inventory, search extract only](https://archiviodistatoreggioemilia.beniculturali.it/getFile.php?id=810);
[Testi editions, Wikipedia](https://en.wikipedia.org/wiki/Fulvio_Testi);
[Doglio record](https://www.helveticarchives.admin.ch/detail.aspx?ID=730769);
[Online Books Page, Testi](https://onlinebooks.library.upenn.edu/webbin/who/Testi%2c%20Fulvio%2c%20conte%2c%201593%2d1646);
[Hanlon, The Hero of Italy](https://academic.oup.com/book/1748).

## 7. Must change before a PR

1. c. 7r l. 8: restore `g V`, reading "strigne". Give c. 7r the sign-first pass the others had.
2. c. 73v: row 8 `A`, row 4 `N`, row 10 `V`, all unbracketed. Delete "one sign stays illegible" and the two edge notes. Recut
   strips to the true paper edge.
3. Reading of cc. 73-74: bracket [a]lmeno, per[ò], in[f]initamente, siam[o], cos[t]retti, disa[g]gi; write nece[s]ità.
4. Fix the counter. Restate totals as 107, 252, 62, 211, 154, and print counts A, B, C.
5. Second full reader on cc. 73-74, above all c. 74r rows 8-15, the part not sampled here.
6. c. 74r row 0: say the sign leans to box. c. 13r: `[?fermo]`, and drop "by the sword". Recheck c. 73r "[?questa passata]".
7. Header: 7 read, c. 13r in part, 5 unread. State that the key came from a later clear copy.
8. NOTES: add Raviola 2014. Keep prior art open, and say Vienna in 1636 is unproved.

## Appendix: blind readings as saved

Sign codes per `key.tsv`; `^` before a sign is a caret; `?` unread. Saved before any solver text was opened, except that the
c. 73-74 line labelled 74r5 was retyped once for notation, and four c. 20 lines were tidied, before comparing. c. 23r B-rows are the
solver's binarised strips; c. 7r, c. 13r and c. 23r were checked on the colour strips.

```
[c7]
L3 4A+2xNDvTD 2A92+A2Vt+Tx3N#?V3NcT4A
L4 9T3TV32NVTcT4#92VD 2#Tc2DN99Tg2NTg42x3A
L5 DNoT#92g2NVT2VDN99 Tgg2NA33N9V2A3NTg+A9c2A
L6 3NcAg42A4ToAV2TDANV V#9TDT33Nc2DNVx323+29x2
L7 2VxA/2NVT3AcTV39N24 3T9o2VTc2+TV32D2Vt+T
L8 g2N9V2 24VTgN32N x3 92gVT Tc+/232AoN g9AVcT
L9 oTV3TDvT4TDNxTc2t+ Tx3Nx2gVN9TVNV+Ac2A
L10 VNA39A+T9xNxN44T D23A3T+2VTg42Nrr2D2T
L11 xTT#Nxx2/24Tg+Ac2Ag gVA3T24#+V3NcT44A#9T
L12 +TV32NVTxA##2AoNDVT +2#9ToT9A24#T92DN4N
[c9]
L3 39A3NT24oN332+NDvTcAt+T 43A4o2V2x
L4 39Nc2DTxA9T r+rA33NA4cN33N9TgTV+2 VN
L5 ot+AVcNxTV32o Nc2rT92 9x24A92x+4?7 2NVT2V3N9VN
L6 A4VTgN72NcT 4 T+TcTooN4ADNx A2VDAo2VA9x2
L7 #T9+2AcT44T4+ VgvT77Tc+//23AooNDvT
vL1 cA9T2V+VoTccTx2 oN3To#NxNcc2xrA72N VTA4c+DAc2g+Ax
vL2 3A44AAVN2x2# N39T//TDNVDTcT9TDN99Tg g2NA44A439N
vL3 24#92VD2#A3Nc2D
[c11]
L4 24c+DAcT44A o29AVcN4ADN9
L5 9At+A4DN9 2xDv2NTDvT+2x2A#T Vx2T9Nc2rN9
L6 oA9AVDvTD NV39Nc24+2#9NATxx2 TDA+xTcA3TVT
L7 #A93TAx+A TDDT44TV7AT9ADDNV3A 3T4T24rA33N#+
L8 9NTV+cNDNoT x3AxTV7Ac2o2V+294NNx
L8b DToA94N
L9 AV72xA9A/ TVTDvT#2+3Nx3N4Ao#42 r2Dv2A3T#T9
L10 DvT4AxN+T9 Dv2Ar2c+D2AVN42Vc+D AA39AxD+9A9
[c13]
L1 #T9AgT+N4A9T4Tx2
L2 3NcT44Tx+TVTgN72A72NV2VArA33TADN3Tx32o2V2
L3 x392T3A442o#T9A3N9Tx3TxxNNrrT93Tg9AVc2xx2oT
L4 cT44A#T9xNVAVNV39ATcTVNx392x3A32TDvTg42T
L5 r2?2+V3NAcTx2/29TT#9NoT33T9TA  2Vt+Tx3T
L6 ?3+9/N4TV7Tc23A42At+2VcTD2o24ArAV32Tt+Agg9N
[c16]
rL4 #+Nx+DTcT9T
rL5 c24Tgg2T9ND vT#9NxTg+TVcN4A g+T99A2V23A
rL6 DN3Tx32o2V2
vL3 T//ToT9A2o#2T3A4A gg9A+A942c2+A
vL4 V3Agg2N
rL6b ?39r ADD2AVN2Vx3A V7Ac?+T9
rL7 cAVN2cAVA92T o+V232NV2T4T4A9g V2xx2oTNrrT9
rL8 3TrA33TcA4 oA9DvTxTc2+244Ar9A VDAxT9+29A4N
rL9 9Nc2V+23NT c2#9T3Tx3Nt+AV3TA 44To+V272NV2Tg
rL10 42Tc2cN+T9T DvTV N23TV2AoN/T V#9N+Tc+3T4T
[c20]
rL8 g2A+N2x3T xxN+TcT3TDvT4TD NxTcT4#92VD2#T
rL9 c2DN99Tgg2Nx VN#Txx2oAoTV3T2 VDAo2VA3T
rL11 DNoTDvT
rL12 x2AVNt+D42 r2DA32cAg9AVc2xx2oT D29DNV3AV7T#
rL13 N93AVNxTDNx+ x#2g2NV2TgT4Nx2
rL16 t+AV3Ng4 2ArrA92cT4x2
rL17 gVN9c+DAcT44A o29AVcN4ATt+T442cT 4#92VD2#TcT4
[c23]
B1 D2DNV3TV32AoNDvT2VrN9o2A3T24DA9VT+A4ToAA++T9323TDv
B2 DN3Tx3T2VrN9oA72NV2x2AVN3A42DvTVNV#NxxAVN#9T
B3 g2+c2DA9TAVNx3922V3T9Txx2cA3Tg42T4T#2+gTVT9A42DvT
B4 x2A#Nxx2/24TT92DN9cA3T+2DvTxxTVcN299T+A9A/24T
B5 24#9TD2#272Nc2t+Tx3Nx2gVN9TVN2cN/2AoN#9ToT9T
[c73]
L1 VN2x2AoN92xN4+32c2oNx39A9T4Ar9NV3T
L2 ADv2D2vA3AV3NN^rTxNTxTVNV#N39ToNc2rTVcT9T4A
L3 DAo#DgVDc2rTVcT9ToNA4oTVN4T#2A^7T#2+#92VD2
L4 #A42#9NV3TA3+^3T4N#N93+V23ADvTxA+T9T o2N
L5 cAr9NV3A9TToN9 32r2DA9T2V2o2D2 D292VD9T
L6 xDT#T9N2Vr2V23AoTV3TDvTx2Ao NDANx39T^32
L7 2Nt+Tx3AVT DT+23A2V3To#NDvT 24VN+39Nx3
L8 A3NTxDNVDT93 A32x2oNx2#T94TgTV3 2oAVcA3TA
L9 o24AVNDvTVTvAVNrA^3Nr+^g29T4To2 g42A2A#T9
L10 4ArAoAcTc2x A^c22V3N4T9A/242D vTxrr92+AN
74r5 /2xNgVADvTxox292xN4+Ac A^#42DA9
74r6 oAg2N9oTV3T A^4TDNxTc23A42A A439 2oTV
74r7 3Tx2#T9cT9AVN2x+Nx3A322o#T92A42
```
