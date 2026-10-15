# Comte d'Affry (The Hague) to the Marquis de Stainville at Vienna, August 1757 (DECODE R1071)

Status: attempted, not solved — 0 of 761 code groups deciphered; a code of its own (code C), no key material.

Split on 14 Oct 2026 from `affry1757` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter was
filed with d'Affry's ten intercepted letters to Rouillé and Bernis (Jan 1757 - Jan 1758), which share one code whose
key was rebuilt from Lyonet's decipherments; this one uses another code. Those letters are
[`targets/affry1757/`](../affry1757/NOTES.md) (a different cipher, with its own page). The work below was done in the
affry1757 sessions of 19 Sept and 5 Oct 2026 and is carried over from its NOTES; the R1071 files (`cipher_C.txt`,
`decode/DOC_R1071_D1843_1843.txt`) moved here on 14 Oct 2026.

Work date: 2026-09-19. Catalogue item 213 (class C), restored on 14 Oct 2026 and narrowed to this letter,
outcome "attempted, open".

## The document

Koninklijk Huisarchief, The Hague, Prins Willem V inv. 192; DECODE R1071
(https://de-crypt.org/decrypt-web/RecordsView/1071), "KHA_A31_PWV_inr192_L.A._d'Affry_to_E.F._de_Choiseul_1757-08-07",
3 pp., DECODE note "Intercepted codeletter, unsolved". Receiver on DECODE: Étienne François, Marquis de Stainville,
later Duc de Choiseul (1719-1785), French ambassador in Vienna. The affry1757 page dates it 4 August 1757, no. 485;
DECODE gives 7 August. Images `IMG_R1071_I5592_P1` – `I5594_P3` (git-ignored, main checkout
`targets/affry1757/img/`, shared source folder, not moved); the leaves are photographed sideways (rotate -90 to read).

## Transcription

- `decode/DOC_R1071_D1843_1843.txt`: DECODE's digit transcription.
- `cipher_C.txt`: the groups parsed from it by `../affry1757/parse.py` (19 Sept 2026): 761 tokens, 357 distinct
  (measured 14 Oct 2026). Not re-transcribed from the images. Looking at P1 for the page snip (14 Oct 2026): line 1
  has 240 where DECODE has 24, and line 7 ends `1116 1158`, which the parse keeps as one token `11161158`; the
  DECODE 8-read-as-0 trap found in the sibling letters may also occur here.

## What was tried

1. (19 Sept 2026) Group-frequency cosine between all the inv. 192 letters: R1071 stands apart from the Jan-Feb and
   Apr 1757 - Jan 1758 letters (which turned out to be one code).
2. (19 Sept 2026) The 651-group key voted from Lyonet's decipherments (`../affry1757/key_M.json`) applied to R1071:
   nonsense, so a different code.
3. (19 Sept 2026) Images reviewed: no clear copy or decipherment among them (unlike eight of the siblings).
4. (14 Oct 2026) DECODE harvest (`research/catalogue_harvest/decode/list.json`, `views_b.jsonl`) searched for other
   records of d'Affry, Stainville or Choiseul: only the inv. 192 letters and a 1763-64 Choiseul record in BL Add MS
   32263; no key record.

## Prior work

De Leeuw (2000) records that Lyonet broke d'Affry's first code by June 1756 and "two more French ones", and that
d'Affry's code to Choiseul from Dec 1758 was broken later. Lyonet's decipherments survive as Nationaal Archief
1.01.50 inv. 221 and 223, not digitised (checked 19 Sept 2026). Bussemaker (1906) prints Fruin's extracts of
d'Affry's letters to the French government; none for this date was matched to R1071. Prior solution: in archive
(probably, if inv. 223 holds it), not seen.

## Remaining gaps
- R1071, all 761 code groups - blocker: no-key-material; a different code (code C) from the rest of inv. 192; no decipherment among the images, the Nationaal Archief 1.01.50 inv. 221/223 decipherments are not digitised, and no key record is on DECODE.

## Escalation
- [x] siblings: all inv. 192 records (R1052-R1076, R2067) opened; eight carry Lyonet's decipherments, none for R1071.
- [x] clear-pages: the three R1071 images hold only figures; no clear copy.
- [x] known-keys: d'Affry's 1757 key (key_M, 651 groups) applied: nonsense; DECODE harvest searched for other d'Affry/Stainville/Choiseul keys (14 Oct 2026): none.
- [x] print: De Leeuw 2000, Bussemaker 1906, Coquelle 1904 checked in the affry1757 sessions; no text of this letter.
- [n/a] key-rebuild: a code of unknown structure (357 distinct groups in 761 tokens, values up to about 1,200) with no crib; a ciphertext-only rebuild is not feasible at this length.
- [n/a] retry: nothing to rerun without key material.

## Next

The Nationaal Archief 1.01.50 inv. 223 decipherments (d'Affry to B., Jul 1757 - Dec 1758) or the Vienna embassy's
code of 1757 (AE Paris, Correspondance politique Autriche). With either, re-transcribe R1071 from the images first.
