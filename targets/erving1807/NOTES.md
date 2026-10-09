# Erving to Madison, Madrid, 24 March 1807 (Founders Madison/02-13-02-0559): the holes in Madison's decode

Private letter No. 21, "In the Cypher of the Legation", which is Pinckney's code. The Madison editors (PJM-SS 13:529-31)
print Madison's interlinear decode as it stands and say the key has not been found (Weber 152-53).

## Sources read (2026-09-18)

- **RC1**, NARA RG 59 DD Spain vol. 10 = microfilm **M31 reel 12, frames 0283-0286** (naId 188605361; manifest
  `objects_reel012.json`, downloader `dl.py`). Code groups in ink, with Madison's decode between the lines.
- **RC2 "Duplicate"**, LoC Madison Papers mjm014714, images `tile.loc.gov/storage-services/master/mss/mjm/09/0600/0603d.jpg`,
  `0604.jpg` ... `0607.jpg` (direct tile URLs work although loc.gov pages are Cloudflare-blocked). Same groups, no decode.
- **Pinckney's code in his own despatches**: M31 reel 7 frames 0346-0352 (22 Feb 1803, one copy with Wagner's decode,
  frame 0348) and reel 8 frames 0083-0084 (Jan 1804). Same code: 1651 the, 133 of, 1343 and, 244 to, 1578 that,
  1181 se, 69 in (Wagner: "the In-tend-ant" = 1651.69.1586.103), 1515 late, 1583 ter (927.624.1583 "having a terri-").
- Group list with Madison's readings: `erving_groups.txt`. Some line alignments of the opening paragraph are
  approximate; the groups at the holes were checked on both copies.

## Results

| Founders | groups (both RCs agree) | reading | evidence |
|---|---|---|---|
| "to the […]" (n. 8, JM "se al e") | 69.1651.1183.1497.1298 | **in the scale** | 69 = *in* (JM himself: "his retreat *in* Ha--er", 742.69.724; "went *in*-cog" 664.69.956; Wagner 1803 "the *In*tendant"), so JM's "to the" is his slip. 1497 = *al* (JM, and Gi-b-*r al*-tar). 1183 read *se* by JM (se-em-ed); the word se-al-e can only be *scale* ("of importance in the scale; again, to raise up..."), so either the key's 1183 is *sc* or Erving took the neighbouring group. The clause is the second of Erving's list: first ... again ... lastly. |
| "Haweder", "Ha——er" (n. 5) | 724.529.934 (5 times) | **Hanover** | 724 = Ha, 934 = er in all five; JM left 529 blank or guessed "wed", but at "exchange Hanover for Gibraltar" he decoded the same three groups as "Hanover" himself; 529 = *nov*. |
| "see the he was more so" (n. 6) | 1578.926.390.720.1219 | **see that he was more so** | 1578 = *that* in all other places, as the editors say; the code is right and JM's "the" is a slip. |
| "Giblartar [sic]" | 1619.1508.1497.1594 (twice) | **Gibraltar** | the second occurrence JM wrote "Gibraltar"; 1497 = *al*, so the group order is Gi-b-ral-tar. The [sic] belongs to JM's decode, not to Erving. |
| "sp[eak]" (n. 4) | 244.1212.133 | **to sp[eak] of** | 1212 = *sp* (gra-sp, 408.1013.1212); the rest of the word is missing in **both** copies, so the omission is Erving's. Stays as the editors print it. |
| "been lately doing" (n. 7) | RC2: ...1164.1515.38.769.66... | *been late-ly do-ing* | 1515 = late (Pinckney 1803), 38 = ly, 66 = ing. |

So every hole in the printed text closes: the only real loss is Erving's own dropped *-eak*. Madison had the key. The
holes are his slips, not missing key entries.

## Not done

- A full Pinckney key. The pairs above come from this letter and two Pinckney pages. Pinckney's decoded despatches of
  1802-04 (Founders 02-03-02-0170, 02-03-02-0313, 02-04-02-0419, 02-04-02-0611, 02-06-02-0346 with Brent's
  3-page decipherment, 02-06-02-0560, 02-07-02-0022; list in `pinckney_chain.tsv`) are on M31 reels 7 and 8 and would
  give a few hundred more pairs by the roll-13 method. `codescore.py` scores frames for code texture (it also hits dense
  plain handwriting; read the sheets).
- **Erving to Madison, 10 Aug 1807**, M31 reel 12 frames 0362-0366: several pages of this code with no decode on the
  NARA copy. Erving wrote on 22 June 1807 that the department could not read some of his letters. This is the next target
  for a rebuilt Pinckney key; check first whether Founders prints a decode (99-01-02 series).
  Done 4 Oct 2026 (outside contribution, PR #21): Founders prints it decoded (99-01-02-1993); the code was aligned
  with that text and the key rebuilt, see [`../erving1807aug/`](../erving1807aug/).
