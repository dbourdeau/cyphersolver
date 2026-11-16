# gerlach1252: the four repeated slips of the pp.124-137 blind pass, and their cause

> Filed in the repository 16 Nov 2026: this note was written in a working folder. Paths in it map as follows: `key_v2.tsv` and
> `key_v1_to_v2.diff` are at `targets/gerlach1252/`; `SHEET_v2.md` and `SHEET_v1_to_v2.diff` are in `blind/p138-150/`; `crops/`, `work/align.py`,
> `work/freq.py`, `FETCH_LOG.txt` are beside this file. `img/`, `work/errs.json` and the `siblings/` paths are working files, not filed.
> The fresh blind pass it proposes was run: `blind/p138-150/` (95.2% strict, see NOTES.md).

16 Nov 2026 (Brisbane). Input: PR #686 judge (`siblings/gerlach1252/p124_137/judge/judge.tsv`), blind files
BLIND_a (pp.124-130) and BLIND_b (pp.131-137), label sheet `blind_packet/SHEET.md`, frozen key
`key_frozen.tsv` (sha256 7e6f0b8a...). Independent evidence: upstream/main `targets/gerlach1252/`
(transcription, decryption and reading of pp.7-19 and the accepted partial pages 40, 107, 112, 115, 156, 177),
Kohn's key sheet (p.260-261, scans 0265-0266) and the Wellcome IIIF images. Nothing frozen was edited and
pp.124-137 were not re-decoded. Image GETs: `FETCH_LOG.txt` (plain curl, 2-3 s apart).

## Bottom line

| Slip (judge) | Count | Verdict | Cause |
|---|---|---|---|
| l where u/v wanted | 187 from 4L (of 195 l-slips) | **(b) naming confusion** | The u sign of the later hand is Kohn's closed "printed" 4 (4U). Reader A labelled it 4L (106 slips), reader B 4L (81) or 4R (67). The key value 4U = u is right. |
| r where u wanted | 71 from 4R | **(b) naming confusion** | Same sign as above, labelled 4R (67 of them by reader B). |
| g where d/k wanted | 55 from ARW | **(a) key omission + (b) naming confusion** | 24 are SIG + SEVEN ("de", as in den, der, wider, andern) read as one ARW (b). 30 are k: Kohn's k group has an o-with-arrow sign that key.tsv leaves out, so the readers had no label for it and wrote ARW (a). 1 unclear. |
| f where long s wanted | 27 from MM | **(b) naming confusion** | The sign is S3 (angular pi with a stroke through the top), labelled MM by reader B only. MM = f is right for the rounded m. |

None of the four is (c) scribal variation: the shapes are distinct on the page, Kohn's sheet gives them
separate places, and each slip is tied to one reader (a scribal habit would show in both). [derived]

Counts are from `work/align.py`: it lines up each judged letter with its blind label (301 of 306 lines align;
4 of the 5 that do not are BAMD sign-off lines, whose clear capitals count as judge units, and p.124 L18 has the
`=?` mark; those 5 lines carry 4 more slips by eye: ARW for k in p.124 L07, 4L for u in p.124 L18 and p.136 L10,
4R for u in p.136 L23, not in the table). [measured]
Per reader, from the same alignment [measured]:

| label slip | reader A, pp.124-130 | reader B, pp.131-137 | total |
|---|---|---|---|
| 4L for u | 106 | 81 | 187 |
| 4R for u | 4 | 67 | 71 |
| ARW for de/k | 39 | 16 | 55 |
| MM for s | 0 | 27 | 27 |
| 4U used at all | 16 (all right) | 0 | 16 |

## 1. 4L and 4R for u (258 slips): (b)

Evidence independent of pp.124-137:

- **Kohn's sheet** (crops `kohn_p260_z_y_x_w_u_t_s.jpg`, `kohn_p260_r_q_p_o.jpg`, `kohn_p260_n_m_l_k_i_h_g_f_e.jpg`): three
  different figure-4s in three groups. u group: PHI + a closed printed 4 with flat foot. r group: a kite-4 with
  the stem through and a pointed foot, + EUR. l group: OL + an open 4 + a 4 with a curled foot. key.tsv has
  4U = u, 4R = r, 4L = l, which matches. **No key value is wrong.** [measured on the image]
- **Accepted upstream pages in the same later hand**: the contributor labelled the u sign 4U on pp.40-177 (51 of
  1,301 signs, 3.9%; "und" written `4U H SIG` 5 times, `4U X DQ` 3 times), and those pages read as sense
  (furgenomen, uerstanden, uirtzehen). On pp.7-19 u is mostly PHI (284) and 4U is rare (6): the scribe's
  preferred u sign changes between the early and the later pages. [measured, `work/freq.py`]
- **On the pp.124-137 images the three shapes are distinct.** p.124 L01: the r of "werme" is the pointed kite,
  the u of "und" and of "drucket" is the closed flat-footed 4 (`p124_L01_werme_r4R_und_u4U.jpg`,
  `p124_L01_drucket_u_closed4.jpg`); p.124 L02 "curium" has two closed 4s for u (`p124_L02_curium_u_closed4.jpg`), while
  the l of "mol" is an open 4 with two unjoined strokes (`p124_L02_mol_l_open4.jpg`); p.124 L06 "von"
  (`p124_L06_von_u_closed4.jpg`). p.137 L21 "buch" (u, closed flat foot) against "beschriben" (r, pointed kite) in
  the same line (`p137_L21_buch_u4U_vs_schriben_r4R.jpg`). [measured on the image]
- Pattern by reader: A labelled the closed 4 as 4L (and only 16 times as 4U); B never used 4U and split it
  between 4L and 4R. The shapes are the same on both readers' pages, so the slip is in the naming. The old sheet put "4U"
  third and called it "modern form"; the scribe's u is the ordinary printed 4, which a reader takes for the
  default "4". [derived]

Fix: sheet only (4U description, look-alike set). Key unchanged.

## 2. ARW for d/k (55 slips): (a) + (b)

- **Kohn's sheet** (`kohn_p260_g_group.jpg`, `kohn_p260_n_m_l_k_i_h_g_f_e.jpg`): g group = o joined by a bar to a
  flat-topped 7 (ARW) + "2e" (G). **k group = heart, a reversed-3 with bars, and a small o with a straight
  arrow.** key.tsv has only HRT for k: the o-arrow sign is missing (a). [measured on the image]
- **"de" cases (24)**: den, dem, der, wider, andern, anderthalbe, gemeldet, linde, umbwunden, deckel, geschwinde,
  feder. On the image the "ARW" in "den" is a SIG (o with a steeply rising tail) followed by a separate 7
  (SEVEN): p.124 L01, p.130 L20, p.131 L02 (`p124_L01_den_SIG_plus_SEVEN.jpg`, `p130_L20_den_SIG_plus_SEVEN.jpg`,
  `p131_L02_den_SIG_plus_SEVEN.jpg`). Two signs read as one, because the old ARW description ("small o joined by
  a bar to a 7-like hook") also fits SIG + SEVEN written close (b). Key values SIG = d, SEVEN = e are right.
- **k cases (30)**: kolben, klein(e/n/er), kessel, kupfern, kunst, komme, konnet, keller, kan, kiel, and the k of
  ck in ewigkeit, stecken, ecken, tecken, deckel, mercket, fertigk, hinwegk. On the image the k is o + bar +
  a pointed, peaked hook: p.130 L20 "tecken", p.130 L17 "klei-", p.131 L04 "kesel" (`p130_L20_tecken_k_oarrow.jpg`,
  `p130_L17_klei_k_oarrow.jpg`, `p131_L04_kesel_k_oarrow_s_S3.jpg`); the g of "finger", p.130 L19, has the flat
  7 top (`p130_L19_finger_g_ARW.jpg`). [measured on 5 crops; the g/k difference is small and was checked only on
  these crops]
- Upstream note: the accepted p.177 L16 "glein" (ARW) is probably the same k sign, so "glein" is likely "klein"
  and not a dialect spelling. Not changed here. [derived]

Fix: key_v2 adds `k OAR`; sheet adds OAR and says SIG + SEVEN are two labels.

## 3. MM for long s (27 slips): (b)

- **Accepted upstream**: MM = f on pp.7-19 (pulfer, drauf, funf), rounded cursive m with arches and nothing on
  top (p.16 L17, `p16_L17_MM_f_accepted.jpg`). S3 = s in the later hand, angular pi with a stroke rising through
  the top: p.177 L04 "waser" (`p177_L04_waser_S3_accepted.jpg`). Kohn's s group has this sign fourth. [measured]
- p.137 L20 "wasser", labelled MM by reader B, is the same angular S3 shape (`p137_L20_wasser_S3_labelled_MM.jpg`);
  p.131 L03 and L04 (S3 and the s of "kesel", `p131_L03_S3.jpg`, `p131_L04_kesel_k_oarrow_s_S3.jpg`) show the
  sign with a small tick on top, which the old sheet's "rounded m with cap" fits better than "m/pi-like with a
  cross on top". Reader A made no MM slips. [measured]

Fix: sheet only (MM and S3 descriptions, look-alike set). Key values unchanged.

## Minor, not in the four

THE for i (13): theta vs dotted circle (`e[b]n` = ein). Probably naming too; added to the look-alike sets,
not checked on the image.

## Files

- `key_v2.tsv` (sha256 b4706238...), diff `key_v1_to_v2.diff`: adds `k OAR` and `l 4C` (Kohn's third l sign, a 4
  with curled foot, not seen in the text); sharper shape notes for ARW, SIG, MM, S3, 4L, 4U. **No letter value
  changed.**
- `SHEET_v2.md` (sha256 775ea445...), diff `SHEET_v1_to_v2.diff`: same descriptions with no letters or example
  words, adds OAR and 4C, adds a "Look-alike sets" section.
- `crops/` (23 image crops), `img/` (downloads), `FETCH_LOG.txt`, `work/align.py`, `work/freq.py`, `work/errs.json`.

## Not done / open

- Not tested by decoding: with no re-decode of pp.124-137 (as instructed), the gain from v2 is unmeasured. The
  judge's ceiling of about 98.7% is only a hypothesis. The fresh blind pass on new pages is the test.
- The g/k (ARW/OAR) difference rests on 5 crops. If the fresh pass shows readers cannot separate them, the fallback
  is (c) for k only: the scribe writes the g sign for k.
- The reversed-3 in Kohn's k group (QQ is q in key.tsv) is not resolved.

## Proposed fresh pages (blind pass with key_v2 + SHEET_v2)

Checked against upstream/main (read: pp.7-10, 13-19; openings of 40, 107, 112, 115, 156, 177) and against every
upstream PR head (523 refs fetched; only #686 touches gerlach1252, pp.124-137). Page numbers seen on the scans
(scan = page - 7 here). [measured]

| page | scan | note |
|---|---|---|
| 138 | b19695561_0131 | full cipher page, about 30 lines; follows the p.137 aqua regis recipe (some context risk) |
| 139 | b19695561_0132 | full cipher page; BAMD sign-off and a larger-hand heading near the foot |
| 140 | b19695561_0133 | full cipher page |
| 150 | b19695561_0143 | cipher, BAMD sign-off and a new section; clear Latin margin note ("vide f. 32", "Multiplicatio"): blind readers copy it in { } |
| 90 (spare) | b19695561_0083 | cipher with a coloured drawing at the foot; text of a different section, so less context leak |
