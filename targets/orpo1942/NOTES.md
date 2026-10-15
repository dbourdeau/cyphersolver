# Ordnungspolizei Doppelkasten radiograms, 1942 (Schmeh 30 Aug 2020): not solved; what is established

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026): this entry is the daily key of
**27 February 1942** (D33, D34, E72, D67; 970 letters). Message A115 of 16 June 1942 is in another daily key
(discriminator ARTTN) and has Bletchley's decrypt; it is a different cipher with its own page and folder,
`../orpo1942jun/` (`docs/orpo1942jun.html`), where `align115c.py`, `align115h.py` and `hsspf_decrypt_1.png` now
live. The A115 sections below are kept as the record of the attempt; `msgs.txt`, `dk.py` and `kpsolve.cs` stay here
and are shared. C43 (XOS = OSX) may be in the 27 Feb key, but its date is not verified, so it is not listed as a
document of this entry.

Source: Frode Weierud, *German Police Doppelkastenschlüssel Messages* (CryptoCellar, 5 Aug 2020;
`german-police-doka-messages.pdf`), from NARA RG 457 HCC Boxes 1386 and 202, posted by Schmeh on 30 Aug 2020.
It holds six messages, which `msgs.txt` transcribes with the discriminator group removed:

| id | date | route | letters (without discriminator) | discriminator |
|---|---|---|---|---|
| A115 | 16 Jun 1942 | SQF Mogilev (HSSPF Russland Mitte) → ALQ via DQH Berlin | 223 (odd, see below) | ARTTN |
| D33 | 27 Feb 1942 | SRS1 Rovno → DQH Berlin | 74 | KFWOJ |
| D34 | 27 Feb 1942 | SQF Mogilev → DSO Kommandostab RFSS | 160 + 86 | DNOSX / DRANR |
| E72 | 27 Feb 1942 | SRS3 Proskurov → SRS1, SRS2 Brest | 178 + 144 | SBWYY / LENRA |
| D67 | 27 Feb 1942 | SRS3 Proskurov → SRS1, SRS2 | 170 + 158 | OWQWJ / WNSXO |
| C43 | dated 28 Feb 1943 | SRS Kiev → SRS1 | 138 (part 2 lost) | SRXOS |

**Status.** Message A115 has a plaintext: Bletchley's decrypt, reproduced in Hanyok, *Eavesdropping on Hell*
(NSA 2005). It reports the partisan ambush on the Bobruisk–Mogilev road (16 men of Pol. Batl. 51 killed) and the
destruction of the village of Borki, whose inhabitants were "liquidated". Hanyok leaves Borki unlocated; it is
Borki, Kirovsk district, Mogilev region, destroyed with six neighbouring settlements on 15 June 1942 by the
Dirlewanger battalion, Einsatzkommando 8 and police after partisan attacks on the Mogilev-Bobruisk road
(Dirlewanger's report: 2,027 dead; memorial on the site). Zhukov, *Okhotniki za partizanami. Brigada
Dirlevangera* (military.wikireading.ru/62640), gives the same 16 dead of Pol. Batl. 51. Pointed out by Ilya
(reader email, Sept 2026); also mogilev-region.gov.by and partizany.by/battles/tak-pogibla-derevnya.
Crib value for the 27 Feb traffic: none found (the DK layout makes isolated place names weak cribs); the
plaintexts of the February messages might survive in Belarusian/Russian archives, but none located. The five 27 February 1942 messages
remain unread, as they are in Schmeh's 2021 list of unsolved WWII ciphers ("partially solved" refers to A115).
The Bletchley decrypts of the February traffic would be in TNA HW 16/17 (verbatim German police messages; HW 16/18
is May–June 1942), which is not online.

## One key for 27 February

Weierud reads the discriminator as the last three letters in any order, and warns that O and Q are hard to tell
apart. Read that way, the 27 February parts use exactly four discriminators: WOJ (D33, and D67 part 1 read as
OWOWJ), OSX (D34 part 1, D67 part 2), ANR (D34 part 2, E72 part 2) and WYY (E72 part 1). That matches "four
discriminators per daily key" (Weierud; GPD note G). Parts of one message carry different discriminators, and
Mogilev and Proskurov traffic shares them, so all seven parts (970 letters) are one key. C43's XOS also
matches OSX, which suggests it is misdated or that a key ran over more than one day.

A115: the 228-letter count in both intercepts and in the German header leaves 223 after the discriminator. That
is odd, so the German clerk added or dropped a letter. The ciphertext only pairs up if the stray letter is among
the first ~9. Counted from the end, it has 25 repeated digraphs (19 digraph types repeat); counted from the start
it has 8, which is chance level.

## The system (checked against primary sources)

- `schluesselanleitung-dk-1940.pdf` (OKH draft, 2 Dec 1940) and `-1941.pdf` (OKW, Dec 1941): two 5×5 boxes; the
  plaintext is written in double lines of **17**; the pairs are the letters that stand one under the other; a
  remainder is split in half; each pair is enciphered **twice** with the same boxes. For same-row pairs, the cipher
  letter is the one to the right. In `dk.py`, both manuals' worked examples encipher letter for letter (the 1941
  manual's p. 5 misprints `tylhu` for `tvlhu`, which p. 6 has right). The spelling conventions: CH→Q, ß→SZ, the
  hyphen written STRIQ.
- NSA (Cryptologic Quarterly, "WWII German Army Field Cipher", from Wayback: `wb_world_war_II.txt`): the Army
  "NI" is the same scheme with **21-letter** lines and the **left** neighbour for same-row pairs. Its worked
  examples (EU→VR→QZ; en→FL→NC; ea→HK→TT) reproduce exactly. X marks numbers, names and sentences; ZWO; CH→Q.
- Hanyok: the police changed from double transposition to double Playfair in November 1941. So February 1942
  is double Playfair.
- A useful identity for the cross-row case of both passes. Write each letter as (A-row, A-col, B-row, B-col). The
  intermediate letters are v1 = A[B-row c1][A-col c2] and v2 = B[A-row c2][B-col c1]. Then p1 = A[B-row v1][A-col v2]
  and p2 = B[A-row v2][B-col v1].

## What was tried

| hypothesis / method | result |
|---|---|
| single encipherment, all seven parts pooled, line length 1–30, pair order as written and reversed | best −5.91/letter (German ≈ −3.9): **excluded** |
| single encipherment per part, and per discriminator group, L ∈ {1, 17, 21}, both pair orders | −5.0 to −5.6 (overfitting noise): **excluded** |
| double encipherment, simulated annealing on quadgrams (synthetic 970-letter test with known key) | never leaves noise (−6.0); from the true key with 4 swaps it does not climb back |
| staged unigram → bigram → quadgram; steepest-ascent ILS; parallel tempering; relabel moves; row/column product score; Sinkhorn relaxation on GPU; hard EM (plaintext as a variable) | all fail on synthetic data. The true key is the unigram optimum (−1.221), but its basin is only ~8–10 swaps; random starts stall at −1.39 to −1.42. The local optima share no row or column structure with the key (precision ≈ 1/6, chance) |
| same with the **true** τ (A-cell→B-cell map) fixed, searching only the letter labelling | still fails (−1.42): the difficulty is conjugation through a random cell permutation, not the key size |
| z3 SAT with 20–37 known pairs | no answer in 15 minutes per case |
| **known plaintext, meet-in-the-middle score** (`kpsolve.cs`: both intermediates compared row by row and column by column) | **solves 111/111 synthetic pairs from random starts in about a minute**; 80 pairs nearly (68/80); fails at ≤60 pairs or with 10% wrong pairs |
| aligning Bletchley's A115 text to its ciphertext, key-free (repeated cipher pairs ⇔ repeated plaintext pairs; exact backtracking over spellings, X separators, numbers, address/signature placement, Borki/Mohilew/Bobruiisk variants, 222 or 224 letters, L = 1–24) | **no consistent alignment**. The same search recovers a synthetic spelling in 35 s. So the enciphered wording differs from Bletchley's rendering (abbreviations, order, or extra matter), or the police layout differs from both manuals |

This matches the public record as far as it goes: single-pass double-box text is broken at 100–150 letters
(source for that figure not kept here), and no published attack breaks a double pass through the same boxes.
(Corrected 18 Sept: an earlier line cited Schmeh's 2 Aug 2020 challenge as double-pass; his 30 Aug post says it
used the most basic, Wikipedia-rules variant, so it is probably single-pass and not evidence either way.) The
second pass through the same boxes leaves a local search no gradient.

**Unchecked lead.** Weierud's scans of the five February sheets are stamped "G.P.D. 665", items 1–5; an example
sheet of 7/2/42 is G.P.D. 620, and Hanyok cites GPD 353/14.9.41 and GPD 467/30.11.41. At about two issues a day,
665 falls near 27 Feb 1942. If so, GPD 665 is the Bletchley decrypt issue to request under TNA HW 16, and C43
("28/2/43", item 1 of the same stamp) is really 28 Feb 1942, which fits its OSX discriminator. Inference from the
scans only; not verified.

## What would finish it

1. **About 80 plaintext/ciphertext pairs for one key.** `kpsolve.exe` then recovers the boxes. For 27 February
   that means Bletchley's decrypts (TNA HW 16/17) or a long stereotyped header. For A115 it means the exact
   German wording. Once aligned, A115 would also confirm the police layout (17 or 21, left or right). It would
   also show whether police boxes were random or keyword-built; keyword-built boxes would open a keyword search
   for 27 February.
2. Some genuinely new ciphertext-only idea for a second pass through the same boxes. Nothing tried here, and
   nothing published, provides one.

## Files

`msgs.txt` (ciphertexts; D67 group 2/6 corrected to ZAVGO per the operator's check line), `dk.py` (reference
implementation, verified on both manuals), `build_lm.py` (25-letter German n-gram tables), `dksolve2.cs`
(SA / ILS / tempering, staged scoring, same-row direction switch), `kpsolve.cs` (known-plaintext solver),
`emsolve.cs`, `relax.py` (failed attacks, kept for the record), `../orpo1942jun/align115c.py` / `align115h.py` (A115 aligners, moved 14 Oct 2026),
`mksyn.py` (synthetic test sets). Sources: Weierud's PDF, both German manuals, the Truppenschlüssel paper
(`mcts.pdf`), and the NSA articles (`wb_*.txt`, `eaves.txt`).
