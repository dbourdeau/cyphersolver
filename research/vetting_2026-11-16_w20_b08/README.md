# Wave 20 vetting, batch b08 (16 Nov 2026)

These are proposals only. `research/leads.json` and `catalogue.json` were not touched. `proposals.json` (merged from
`parts/<id>.json` by `add.py`) holds one proposal per lead, in the gate's vetting shape. Script access only. Tomokiyo's
`unsolved.htm` and Lasry's `GL.htm` were fetched 15 Nov 2026 and searched with `cgrep.py`.

## Results

| Lead | Verdict | Conf. | Deciding fact |
|---|---|---|---|
| 2191 | open | medium | Bierther II/8 p. 405 (editor): Menzel to Maximilian, Hamburg 1633, 'größtenteils in Chiffre, deren Auflösung jedoch fehlt'; page confirmed by GB feed (HPIVNCmjZHEC PA405). Caveat: Richel's contemporary résumé exists (Geheimer Rat 195). |
| 2674 | read | medium | Columbia finding aid: telegrams 'deciphered by Armenian military intelligence'. Decipherments are what is filed. Language is Russian. |
| 1168 | partly_read | medium | Series of 125 units. LBC says cipher passages 'a volte' carry a clear transcription by the receiving offices. No unit list online. |
| 1483 | read | medium | All six CPDOC summaries give the plaintext content. The lead's link has a stray trailing '-' (404); without it the link works. |
| 1484 | partly_read | medium | Most CPDOC summaries give the content. The fonds holds 34 'cifrados e traduzidos'. Only some vague radios remain. |
| 903 | duplicate | high | The bundle's real calendar items are now catalogue 956 and leads 957 and 1007. Two of the named items do not exist in the volume. |
| 2804 | partly_read | medium | CSP Eliz. 1598-1601 p. 495 no. 132 ('— Rogers', Dec 1600, not Oct): report deciphered except italics and most of the inserted love letter. |
| 2805 | duplicate | high | Same as lead 1005 (Holt to Owen and Bayley, 14 Oct 1598, SP 12/268 no. 79, closed not_cipher). The lead's 1600 / SP 12/275 is wrong. |
| 2806 | duplicate | high | Same as catalogue 960 (Woodford to Nethersole, 3 Aug 1620, SP 14/116 no. 59). Catalogue 960 itself wrongly says 1611 / SP 14/65. |
| 2803 | read | high | CSP Dom. Charles I Addenda 1625-49 (1897) p. 690 no. 343: the editor built a key and printed the full decipherment. Date 19 Jan 1645/6, SP 16/539. |
| 2807 | read | high | CSP Dom. Charles II 1663-64 p. 266: no. 17 cipher, no. 18 'Decypher of the preceding letter'. SP 29/80, 4 Sept 1663, Williams to Bennet. |
| 2155 | none | low | Duke catalogue behind Anubis, ArchiveGrid Cloudflare 403. 'Language in code' not shown to be a cipher. |
| 2940 | none | low | Durham finding aid gives only 'English, Arabic and cypher'. Registers not digitised. Whether the clear text is beside the entries is unknown. |
| 2901 | none (keep as lead) | medium | Code-book words (Berne-vocabulary style) for stock phrases, about 133 telegrams. No code book found. Not a cipher target. The real cipher in HIL/64-65 is already leads 2899-2900 and catalogue 2907-2909. |
| 2449 | open | low | AIS AM.272.1.97 title '(salakirjas)' = in secret writing, 19 ll., 1907, no transcription. Private, weak. |
| 1128 | open | medium | Klinckowström I p. 155: 'lettre en chiffre (non déchiffrée)' of Gustav III to Fersen, 28 Feb 1792. Other letters there are 'déchiffrée'. |
| 2217 | none | medium | Lettere V-VII cite eight GC 137 pieces, none at c. 13r (archive.org full-text search). Open question: is the same-sized clear strip c. 12r its plaintext? |

## Routes found or confirmed this pass

- archive.org full-text search works on lending-only books without a login:
  `https://archive.org/services/search/beta/page_production/?user_query=identifier:<id> <terms>&page_type=search_results&service_backend=fts`
  (`fts.py`). Highlights are capped at about five per item. This route settled the Lorenzo de' Medici *Lettere* question.
- Google Books gdata feed (`gbfeed.py`): the preview link carries `pg=PA<n>` when a page matches, which confirms a page
  number even without a snippet. The googleapis Books API is over its daily quota (429).
- Bot checks: DDB / Archivportal-D (proof-of-work), Columbia findingaids (Anubis), Duke archives (Anubis), ArchiveGrid
  (Cloudflare 403). All need Chrome.
- PARES was not used (429 all day, per the brief); no lead in this batch needed it.

## Record errors found

- 2217: the id appears twice in leads.json for the same item. The second copy is the fuller one (status + vetting_note).
- 1483: the link has a trailing '-' and 404s.
- 2674: language should read Russian.
- 2803: the date is 19-24 Jan 1645/6 (not 1644-45) and the volume is the Addenda 1625-49 (1897), Vol. DXXXIX no. 343.
- 2804: the date is early Dec 1600 (not Oct), no. 132, sender '— Rogers'.
- 2805: the date is 14 Oct 1598, Vol. CCLXVIII (SP 12/268), not 1600 / CCLXXV.
- 2806 / catalogue 960: catalogue 960 gives 1611 and SP 14/65; the item is 3 Aug 1620, SP 14/116 no. 59.
- 2807: SP 29/80 nos. 17-18, 4 Sept 1663, Robt. Williams to John Thomson [alias Edw. Riggs], to Bennet.
- 1128: the note is on p. 155, not p. 156.
- 903: the bundle's 1594 dates are wrong; its items date from 1591-1593.

## Files

`prior.py` (prior vetting records for an id), `cgrep.py` (Tomokiyo/Lasry lists), `ctx.py` (context in a text file),
`gbfeed.py`, `fts.py`, `add.py`; `parts/` (one proposal per lead); `img/` (git-ignored downloads: calendar
texts, BNCF strips, Durham/LBC/CPDOC pages).
