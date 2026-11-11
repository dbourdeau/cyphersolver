# Bellièvre papers (BnF fr. 15890-15911) on Gallica, screen of 11 Nov 2026 (cloud session) - 0 candidates

Continues `../sweep_2026-11_bellievre_gallica/` (arks, canvas counts) and `../gallica_sweep/` (fr. 15906, 15900 (1), 15891).
Result: **no open cipher**. Five cipher letters were found in two volumes, all already deciphered or printed in clear
(`not_candidates.json`). `candidates.json` is `[]`; no key-only items (`key_leads.json` not written).

## Routes (this network)
- `openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/full/800,/0/default.jpg`: works with curl/urllib, 2-3 s per image,
  occasional 500/503/reset (retried). One sequential fetcher (`fetch_all.py`). `pct:` region requests work for close-ups.
- `archivesetmanuscrits.bnf.fr/ark:/12148/cc461166` and `.../cc461166/c<d0eNNNN>`: answer curl here (200). The fonds page
  carries the summary inventory; every item notice was text-searched for chiffr/cifr: only fr. 15906 (Entragues, known).
  Item ids: 15901 d0e3995, 15902 d0e4463, 15903 d0e4967, 15904 d0e5358, 15905 d0e5711, 15907 d0e6841, 15908 d0e7228,
  15909 d0e7777, 15910 d0e8224, 15911 d0e8555 (15890-15899 are described on the fonds page itself).
- gallica.bnf.fr not tried (403 per brief). archive.org full texts and de-crypt.org RecordsList search answer curl.
- cryptiana.web.fc2.com answers over https (http gives 302).

## Method
About 4,000 canvases could not be read sheet by sheet in one session, so a detector ranks them and only the hits are read:
- `det.py`: connected components per canvas; score = (glyph-sized separate components) - 3 x (long joined strokes) in the
  best 110x44 px window. Cipher written in separate signs scores high, cursive low. Calibrated on known cipher canvases
  (fr. 15906 (2) c93-94, c349-350; fr. 16127 c20, c125: scores 27-54) against clear pages (mostly < 20).
- `rank.py <dir> <thr> [scale]`: scores every canvas, tiles a 390x300 native-scale crop of the best window of each hit
  (20 per sheet), which I read. Threshold 20 for microfilm openings; 24 at scale 0.5 for colour single-page scans.
  Scores are kept in scratch (`<vol>_scores.json`), not in the repo.
- `sheets.py` / `pagesheets.py`: ordinary contact sheets, used around each find and for fr. 15905 (2) c5-87.
- Limits, stated plainly: the detector finds blocks of cipher (two lines or more of separate signs/figures). A letter with only
  a few isolated code signs or one short group in running text (the Entragues type, score 27-28 on reference) can fall
  under the threshold, and italic/humanist hands produce most of the false hits. Canvases under the threshold were NOT
  viewed, except where a contact sheet is listed. So "no cipher seen" below means no cipher block, not no cipher sign.

## Coverage (exact; details in `screen_log.md`)
| fr. | ark | canvases fetched / scored | hits read | sheets read | result |
|---|---|---|---|---|---|
| 15905 (2nd ark, ff. c. 330-680) | btv1b9063808z | 363 / 363 | 76 (thr 20-22) | page sheets c5-87 | none |
| 15905 (1st ark) | btv1b90638227 | 341 / 341 | 25 | - | none |
| 15911 | btv1b52521582d | 907 / 907 | 254 (thr 16 to c136, then 24) | c470-693 | 3 cipher letters, all printed in clear |
| 15904 | btv1b9064051h | 480 / 480 | 63 | - | none |
| 15903 (microfilm) | btv1b9064052x | 436 / 436 | 112 | c42-50, c250-258 | 2 cipher letters, both deciphered in the volume |
| 15903 (colour, same volume) | btv1b10501677p | 858 / 858 | 40 of 227 | - | same two items |
| 15902 | btv1b9063602s | 627 / 627 | about 135 of 143 (last crop sheet unread) | - | none |
| 15894 | btv1b525216318 | 125 / 0 | 0 | - | not screened |
| 15897, 15898 (2 arks), 15890 | | 0 | | | not reached |

Note for the next sweep: btv1b10501677p and btv1b9064052x are one volume digitised twice (fr. 15903), not two halves.

## Cipher found, and why none is a candidate
1. **fr. 15911 ff. 238-242, 281-285, 302-304** (canvases 483-491, 569-577, 611-615): Henri IV to Bellièvre and Sillery at
   Vervins, 14 March, 9 April and 14 April 1598, originals signed Henry / de Neufville, about 90 lines of cipher in all
   (two-digit figures 61-99, letters, +, #, dotted signs; no decipherment on the leaves, margin notes summarise the clear
   text only). Viewed at 1500 px (ff. 241v, 242r, 302r, 304r, 285r). Their full clear text is printed from the Court's
   copies in *Mémoires et correspondance de Duplessis-Mornay*, t. VIII (1824), letters LXX, CXIX, CXXV
   (archive.org `mmoiresetcorresp08morn`, opened; the clear lines framing the f. 241v and f. 302r cipher blocks match the
   print, which runs straight through the enciphered sentences). Berger de Xivrey, *Lettres missives* IV (opened,
   `recueildeslettre04henr`) prints the later Vervins letters from the same copies. So: plaintext in print = not open.
   They are good known-plaintext material for the 1598 Court cipher. Searches: DECODE RecordsList "Bellièvre", "Bellievre",
   "15911", "Vervins" = no records; "Sillery" = 2 records (R2785, R2786, BnF fr. 18043/18044, 1615-17, unrelated);
   Tomokiyo `henryiv.htm` = no mention of Vervins, fr. 15911 or these letters; `known.py 15911` = sweep notes only.
2. **fr. 15903 f. 41** (canvas 47 microfilm / 89 colour): Catherine de Médicis to Bellièvre, April 1574, about 12 lines of
   cipher; the decipherment "Deschiffrement de la lettre de la Reine mere du mois d'Avril 1574" is filed at ff. 40r-v.
3. **fr. 15903 f. 244r** (canvas 254 / 497): a 1575 letter with four short cipher passages, each deciphered interlinearly.

## Excluded
Italic and small dense hands, Italian/Latin/Spanish/German-hand letters, 17th-century copies, microfilm target frames,
a secretary-hand postscript of Charles IX (fr. 15902 f. 228v, opened at 1300 px).

## What remains
- fr. 15894 (1168 canvases; 1598-1606), 15897, 15898, 15890: fetch with `fetch_all.py <scratch> 15894 15897 ...`, then
  `rank.py`. At 3 s per image about 3 hours of fetching.
- A sheet-by-sheet read of the sub-threshold canvases of the volumes above, if isolated code signs matter.
- fr. 15892, 15893, 15895, 15896, 15899, 15900 (2), 15901, 15907-15910 have no Gallica ark (earlier README); not checked again.
- Not done for the Vervins letters: checking whether the Court's cipher key survives (BnF fr. 3995-type collections) and
  whether the print's wording inside the enciphered passages is verbatim.
