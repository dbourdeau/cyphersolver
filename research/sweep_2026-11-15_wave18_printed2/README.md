# Printed series sweep, wave 18 (printed2), 16 Nov 2026

Continuation of `research/sweep_2026-11-15_wave16_printed/` (text work only, curl / Python against archive.org OCR and
British History Online). Nothing outside this folder was edited. Downloads in `raw/` (git-ignored).

**Status: done, 16 Nov 2026.** Output: `candidates.json`, 5 rows (`build.py`): 4 B, 1 C. No row was seen on the
manuscript; all rest on printed calendars and the BL catalogue.

| # | Item | Shelfmark | cls | Confidence |
|---|---|---|---|---|
| 1 | Unsigned letter partly in cipher, undeciphered, on Monck's movements 1659-60, imperfect | BL Add MS 32093 f. 423 (Malet); HMC 5th Report p. 314 | B | high that it is unread (two independent descriptions); extent unknown |
| 2 | Wotton to the Council, Paris 18 Oct 1556, greater part of 3 pp. in cipher, undeciphered | TNA SP 69 (piece not identified); CSP Foreign Mary no. 548 | B | high; Wotton 1554 key R354 on DECODE may or may not fit |
| 3 | Randolph to Cecil, Edinburgh 26 Feb 1561, P.S. of four lines of cipher on a slip, undeciphered | TNA SP 52/6 (not verified); CSP Foreign 1560-61 no. 1034; CSP Scotland I no. 964 | B | high, but short |
| 4 | "Eleven small folios of cypher in numbers" that Blencowe failed to break, 1706 | BL Harley/Portland papers (Add MS 70xxx, volume not identified); HMC Portland VIII pp. 234-235 | B | medium: the editor only guesses these are the letters Blencowe meant |
| 5 | Pointis to Louis XIV, camp before Londonderry 17 Jun 1689, "part of the letter is undeciphered" | TNA SP 63/352 no. 5; CSP Dom. W&M 1689-90 p. 154 | C | low: Wallis's decipher in Add MS 32499 probably fills it |

`known.py` was run on every name, date, phrase and shelfmark in these rows: no hit for the items themselves. Tomokiyo's
unsolved list and Lasry's GL.htm were fetched (`raw/unsolved.htm`, `raw/GL.htm`) and grepped: none of the five appears.

Not Continental Congress / Official Records: closed with no rows by `research/sweep_2026-11-11_printed_series`
(wave 16 README, "First finding"); not repeated.

## Step 1: the late wave-16 texts

The wave-16 corpus (`../sweep_2026-11-15_wave16_printed/raw/`, read in place, not copied) holds 1,176 archive.org texts.
112 of them had never been through an "unread phrase" pass (`n_note`, `n_fast_new`, `n_all1/2` stats); they are the
late HMC reports (about 70: Portland, House of Lords, Fifth Report, Heathcote, Hamilton, Roxburghe, Rye, Lincoln,
Shrewsbury/Talbot, Egmont, Lothian, Sackville ...), 22 "Fontes rerum Austriacarum" volumes, about 30 Google `bub_gb_`
scans (mostly further Fontes volumes, incl. II/56-57 Pribram-Landwehr, Privatbriefe Leopold I. an Pötting), six
Fiedler "Relationen venetianischer Botschafter", and the Calendar of Confederate Papers. List: `late_ids.json`.

Passes (wave-16 scripts, `RAW` env var added so they read the wave-16 `raw/`):
- `ex_fast.py` (unread phrase with a cipher word within 200 chars): 23 hits (`n_late.json`), all read.
- `ex_eng2.py` (placeholders such as "[cipher]", "remains undeciphered"): 5 hits (`late_eng2.txt`), nothing.
- `allc.py` with a German/French/Italian/English unread filter: 81 windows (`late_allc.txt`), all read.

Kept: Blencowe's failure on "eleven small folios of cypher in numbers", 1706 (HMC Portland VIII pp. 234-235), and,
through the Fifth Report's Malet MSS, the BL record of Add MS 32093 (below).

Windebank to Hopton, 16 Oct 1634 (Fifth Report p. 312, Malet MSS: "Nearly all in cypher, not decyphered. (9 pp.)")
looked like the best find, but it is **dropped**: the BL catalogue of the Malet volumes (Add MS 32091-32096;
`raw/bl_*.json`) describes it as Add MS 32093 f. 57, "partly in cipher, with a duplicate partly hologr. without cipher",
its enclosures "accompanied with deciphers", and the 17 Oct letter (f. 82) "cipher, with decipher". Windebank's own draft
is also printed in Clarendon State Papers I p. 154 (Calendar of Clarendon SP I no. 392). A filed clear duplicate blocks it.

The same BL record gives a real row: Add MS 32093 f. 423, "Letter partly in cipher, undeciphered, relating, apparently to
Gen. Monck and his movements in 1659 and 1660. Imperfect." (the Fifth Report's "fragment ... partly in cypher about the
landing of Charles II", p. 314). The other Malet cipher items are deciphered (Add MS 32094 items 46 and 78) or already in
the repo (Add MS 32091 ff. 180, 213).

Dropped:
- Fontes II/56-57 (Pötting): about 15 "Kanzleireskript ... chiffriert, ohne gleichzeitige Auflösung" notes (1666-73).
  The editors rebuilt the three chancery ciphers and summarise each rescript's content, so "ohne gleichzeitige
  Auflösung" means no contemporary decipher filed, not unread (same rule as the calendar italics). Vol. I intro: Leopold's
  private cipher keys were lost and rebuilt by the editors.
- Fifth Report Malet MSS, other cipher items: Throckmorton to Dudley 22 May 1560 ("decyphered"; Add MS 32091 f. 180,
  in the catalogue); Moray to John Wood 13 Jul 1569 "34 lines of cypher" = Add MS 32091 f. 213 (`targets/moray`);
  Clarendon/St Albans/Coventry 1667 (all "decyphered"); Arlington to the King 27 Nov 1674 ("nearly 2 pp. of cypher
  partly decyphered", too vague to place a gap); Thurloe to Whitelocke 1653 ("partly in cypher", no unread statement).
- HMC Heathcote "[The parts in italics are in cipher, undeciphered]" (editor's reading in italics); Bennet to Fanshawe
  13 Jun and 6 Oct 1664 (worked out by the editor; already in leads).
- HMC Portland I (1891) 1640s King-Queen letters: the editor found the keys. Another Portland volume of 1891
  (`manuscriptshisg08wardgoog`) intro: names of Charles II's addressees in a cipher "the key to which has not been
  discovered" (names only, letters never sent).
- House of Lords MSS 1678: two St Germain letters to Coleman "not deciphered" (contemporary committee record; Coleman
  named the two keys the next month and the keys were in Sir John Knight's hands; probably read then).
- Seals "undecipherable", damp, Confederate "please decipher" telegrams.

## Step 2: British History Online, CSP Venetian 17-38 and CSP Foreign Edward VI, Mary, Elizabeth 1-10

`bho.py` (wave-16 crawler, unchanged) into `raw/bho/`. CSP Domestic James II, William and Mary and Anne on BHO are
premium (paywalled): those downloads held only the subscription notice and were deleted; the archive.org copies were
fetched instead (Step 3).

CSP Foreign Edward VI (Turnbull 1861): `brk.py` lists every bracketed cipher note (29). "Undeciphered" ones: nos. 97,
271, 328, 549, 588, 637, all already catalogue entries (ia_fulltext sweep); no. 654 (Vannes, "Ciphers two pages") is a
copy of his own ciphers, no unread statement.

CSP Foreign Mary (Turnbull 1861): three "undeciphered" notes (nos. 316, 453, 548). 316 and 453 are in the catalogue and
leads; **no. 548, Wotton to the Council, Paris 18 Oct 1556, is new** (row).

CSP Foreign Elizabeth vols 1-10 (Stevenson, Crosby; 1558-1574): `und.py` lists every "undeciphered / not deciphered /
partly deciphered" note with the next entry (to catch a "Decipher of the above" sibling).
- vol. 1 no. 362 (copy, the deciphered copy is no. 363), vol. 2 nos. 952 and 987 (deciphers follow as 953, 988): read.
- vol. 3 no. 411 (Melun, 9 Aug 1560, a few words): catalogue. **vol. 3 no. 1034, Randolph to Cecil, Edinburgh 26 Feb
  1561, P.S. of four lines of cipher undeciphered: new** (row; CSP Scotland I no. 964 leaves it unread too).
- "Partly deciphered" P.S. and passages (Sadler and Croft 16 Sept 1559; Throckmorton 13 Jun 1561 no. 244 and 31 Jul 1562
  no. 395; Smith's copy 13 Dec 1562 no. 1241, whose sibling is deciphered): the calendar summarises the cipher part, so
  the gap, if any, is small. Not rows.
- vol. 5 no. 1195 (Condé to the Queen, 6 Dec 1562): catalogue (ia_fulltext; Condé key R335).
- vol. 7: two contemporary statements (Throckmorton had not deciphered his commission; Lethington's letter partly shown
  to Moray). Not editorial.
- vol. 9 (1569-71): Killegrew to Cecil, Heidelberg 16 Apr and Cologne 23 Apr 1569, "wholly / entirely in cipher,
  undeciphered": the editor prints the whole text in quotation marks, so he read it (the calendar-italics rule). No. 812
  and no. 1630 (Dumbarton intercept, names undeciphered) are in the catalogue.
- vol. 10 (1572-74): Killegrew 17 Mar 1573 no. 826 ("yet undeciphered", contemporary) and [Antonio Guerras] 14 Jun 1574
  no. 1452 ("a considerable portion not deciphered") are catalogue (1001) or hathitrust items; Berwick 17 May 1573
  ("the rest was in cipher not yet deciphered") is the writer's report.
- vols 4, 6, 8: nothing.

CSP Venetian 17-38 (Hinds, 1621-1675): every cipher passage is marked "deciphered" or "the part in italics deciphered";
`ex_fast.py` and `ex_bho2.py` find only contemporary remarks ("the rest is in cipher, which I have not yet succeeded in
unravelling", vol. 18, Venetian ambassador on an intercepted Pastrana letter; senators who had not yet read despatches).
No rows.

## Step 3: CSP Domestic, years not yet read

Earlier sweeps read CSP Domestic Edward VI to Charles II and the Commonwealth on archive.org (`ia_pass2_a`,
`hathitrust`, wave 16). Fetched here from archive.org (`ids_dom.json`, `dl_dom.log`): William and Mary 1689-90 to
1694-95 (vols 1-5), William III vols 1-3 (1695-97), Anne vol. 1 (1702-03), James II vol. III (1687-89; vol. I-II
not on archive.org, the 1960 copy 401), and three Elizabeth and two Charles II scans that matched the query. CSP
Domestic William III 1697-1702 and Anne 1703-04 were not found on archive.org and are premium on BHO: **not read**.

`ex_fast.py`: 7 hits. Holt to Owen and Bayley 1598 (name numbers; leads), Paget to Throgmorton 1595 (catalogue), Squier
1666 (catalogue), index lines; **Pointis to Louis XIV, camp before Londonderry, 17 Jun 1689, "Part of the letter is
undeciphered", SP 63/352 no. 5: new but weak** (row C; Wallis's decipher in BL Add MS 32499 may fill it).

## Not done

- CSP Domestic William III 1697-1702 (vols 8-11) and Anne 1703-04: not on archive.org as full text found by the query,
  premium on BHO. James II vols I-II (1685-87): archive.org copy 401 (in copyright), BHO premium. Not read.
- CSP Venetian 17-38 and CSP Foreign 1558-74 were grepped by phrase; no page-by-page reading of every "in cipher" note
  without an unread phrase (the calendars mark decipherment explicitly, so an unmarked note is not evidence of a gap).
- The Fontes II/56-57 Pötting chancery rescripts were not checked against the HHStA originals (dropped as editor-read).
- No DECODE live search (the repo snapshot only); State Papers Online not opened, so no TNA piece/folio is verified.

## What vetting must still check

Row 1: view Add MS 32093 f. 423, measure the cipher, identify writer and recipient. Row 2: the SP 69 piece and folio;
test R354 / the Wotton 1555 cipher (Mary no. 316). Row 3: the slip in SP 52/6 (Bain no. 964); any Randolph-Cecil key
of 1560-61 in SP 106. Row 4: find the eleven folios in the Add MS 70xxx Harley papers and confirm the link to
Blencowe's letter of 22 Jun 1706. Row 5: compare with Add MS 32499 and PRONI T582/2 before keeping it.

## Log

- Step 1 (late wave-16 texts, 112): `ex_fast.py` 23 hits, `ex_eng2.py` 5, `allc.py` 81 windows; all read.
- BL catalogue JSON for Add MS 32091-32096 (searcharchives.bl.uk, plain curl, `raw/bl_*.json`, `bl_malet.txt`).
- Step 2 BHO: Venice vols 17-38 (22 vols, no failures), Foreign Edward VI, Mary, Eliz. vols 1-10 (12 vols). Domestic
  James II / W&M on BHO were paywalled: crawler stopped, files deleted.
- Step 3 archive.org: 16 CSP Domestic texts (1 failed, 401) plus CSP Scotland vols 1, 2, 9 and the Clarendon calendar I.
- `build.py` wrote `candidates.json`.
