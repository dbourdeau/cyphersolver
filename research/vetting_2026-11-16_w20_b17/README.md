# Wave 20 vetting, batch b17 (16 Nov 2026)

Leads: 2813 1929 1932 1935 1996 2809 1261 1259 1262 1260 2761 2825 2820 2821 2822 2823 2824 2834.
Proposals in `proposals.json` (built by `make_proposals.py`); nothing applied to leads.json or catalogue.json.

## Routes found or confirmed today

- **OeNB records by script**: the Alma SRU endpoint
  `https://obv-at-oenb.alma.exlibrisgroup.com/view/sru/43ACC_ONB?version=1.2&operation=searchRetrieve&query=...` answers
  curl with MARCXML (Primo answers 403). `onbsru.py '<cql>' [max]` prints the fields. Useful queries:
  `alma.other_system_number=AC13932091`, `alma.all_for_ui="Schlik" and alma.all_for_ui="chiffriert"`.
- **OeNB autograph card catalogue** (KAT-ZOOM): the 856 field of an Autogr. record links
  `katzoom.onb.ac.at/cgi-bin/katadmin/hnlview.pl?katalog=7&kz=1&start=00NNNNNN`; the card image is the GIF in that page
  (`/DB4/hnl/...gif`), fetched by curl over https.
- **Mazal-Unterkircher 1963** (Series nova catalogue) page images on manuscripta-mediaevalia.de
  (`/bilder/hs-bilder/k/HSK0752a_bNNNN.jpg`).
- **NLS manuscripts.nls.uk** is 403 to scripts, but Wayback copies exist for some records; fetch with the `id_` form
  (`https://web.archive.org/web/<ts>id_/https://manuscripts.nls.uk/...`); the plain form returns 0 bytes.
- Blocked today: NRS catalogue (403, no Wayback copy), NLW archives (403), Archives Hub (connection reset), SNAC (bot
  check), archive.org lending items (full-text search 'Item not available'), Wayback CDX (connection reset).

## Results

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2813 | read | high | NLS/Black description of Adv.MS.72.2.10 prints each cipher colophon with its reading (Aonghus mac Fearchair) |
| 1929 | none (key only) | medium | MS.14496 item (iv) 'Cypher tables, 1707-1711' in the 2nd Marquess of Tweeddale's papers; no ciphertext |
| 1932 | none | low | Currie file = proposals on cipher systems in the 1st Earl of Minto's India papers; leaves needed |
| 1935 | none | low | blocker stands (NLS leaves; edition lending-only) |
| 1996 | none | low | blocker stands (NLS 403, no Wayback copy) |
| 2809 | open | medium | NLW: 'Some of the recipes and notes are in cipher'; nothing printed or on DECODE |
| 1261, 1259, 1262, 1260 | none | low | NRS 403, no Wayback copy; earlier blockers stand |
| 2761 | none | low | OOeLA findbuch Chrome-only; regest reads like a cover letter with a key |
| 2825 | open | medium | 5 OeNB records: 'teilweise in Geheimschrift', 43 letters 1898-1912 |
| 2820 | open | medium | 22 OeNB records of Palm to Schlik 1707, mostly 'grossteils chiffriert'; shelfmark is Ser. n. 1697-1698 |
| 2821 | open | medium | 2 Colonna letters, Grosswardein Dec 1705, Ser. n. 1696 |
| 2822 | open | medium | 2 Saint-Saphorin letters 1707 (Berne and o. O.), Ser. n. 1698 |
| 2823 | open | medium | 2 Joseph I rescripts Dec 1705, Ser. n. 1696 |
| 2824 | open | low | Zane to 'Rizzini' (= Carlo Ruzzini at Utrecht), 'teilw. chiffriert'; received set, decipherment risk |
| 2834 | not_cipher | medium | OeNB card 'L.s.(Chiffern)': the note qualifies the signature; letter to Bernhard von Cles, Augsburg |

## Record errors found

- 1929: owner is the 2nd Marquess of Tweeddale (Hays of Yester papers), not 'the 2nd Hay'.
- 2820-2823: Palm's letters are in Cod. Ser. n. 1697 and 1698 (none in 1696); Colonna and Joseph I are in 1696 only;
  Saint-Saphorin's ciphered letters are from Berne / o. O. in 1698. In 1707 Schlik commanded in Italy (not Hungary).
- 2824: recipient 'Carlo Rizzini' is evidently Carlo Ruzzini, Venetian plenipotentiary at Utrecht.
- 2834: recipient Bernhard von Cles, written at Augsburg; 'Chiffern' describes the signature.
