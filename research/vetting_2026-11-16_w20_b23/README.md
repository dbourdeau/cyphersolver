# Vetting wave 20, batch 23 (16 Nov 2026): 18 TNA leads

All 18 leads are TNA items and none is digitised, so the checks ran on the TNA Discovery API: item details
(`/API/records/v1/details/<id>`) and, new this batch, full volume listings from the children endpoint
(`/API/records/v1/children/<parentId>?limit=500`, paged with `&batchStartRecordId=<last id>`). `disc.py` and `kids.py` do
both; the raw JSON is in `src/`. The volume listings settled most leads: a "Deciphered copy" note, a copy filed beside the
original, a missing leaf, or the key itself. `make_proposals.py` writes `proposals.json`. Tomokiyo's and Lasry's lists
came from the 15 Nov download; Tomokiyo's `chauran.htm` was fetched on 16 Nov. The Google Books API quota was used up.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 1887 | none | high | Blocker stands: FO 335/145/6 is catalogued only as "Telegrams in cypher", and it is not digitised |
| 1888 | none | high | Blocker stands: GFM 10/476/1 is "Turkish ciphers vol. 1", frames 824-866 of the film, which nobody has seen |
| 2801 | none | medium | HO 42/73 f. 220 is a "cryptic letter partly in code": possibly veiled language; needs a view |
| 2802 | none | medium | The enclosed letter "refers to places in code" (veiled place names); probably not a cipher; needs a view |
| 2800 | none | medium | The catalogue only says "apparently in code"; needs a view |
| 2791 | none | medium | Shaftesbury's "draft ... in cypher" could be ciphertext or a clear draft; needs a view |
| 1159 | partly_read | medium | Most PRO 30/57/4 code telegrams are filed with a translation or decode; 4/119 is already catalogue 871 |
| 1137 | partly_read | medium | PRO 30/55/16/147 is the "Proposed Cypher" key; 24/76 was summarised from the British Museum clear; the Quebec clears are worked in targets/carleton1782 |
| 1136 | partly_read | medium | Clear duplicates and full summaries in PRO 30/11/3; Ross and Saberton print it. **Split:** 3/6-7 (de Kalb letters in number cipher), 3/207-209 ("not deciphered") |
| 1804 | none | medium | Blocker stands: "Cipher Marseilles" (f. 197) reads like a key label; the only other cipher item in the volume is the key at f. 39 |
| 1154 | key_lookup | medium | The complete key is SP 106/6 nos. 32-33 (Tomokiyo, chauran.htm); /75 is "Missing at transfer"; the volume's undecoded leaves are catalogue 870 |
| 1795 | read | high | f. 123 is a "Deciphered copy. See f.124"; f. 124 is the original, partly in cipher |
| 1884 | read | medium | f. 168 is a letter-book copy in which Stepney gives the content of Paget's cipher letter (précis again at f. 173) |
| 2793 | none | low | The SP 90/2 summaries cover the cipher matter; no note says "deciphered"; needs a view (probably read) |
| 2794 | read | medium | Former reference E17: TNA says the E papers were published in the 1723 Commons report; the "code" is cant names |
| 1780 | none | medium | f. 38 is a covering letter; no record of the cipher piece in SP 78/181; probably not_cipher |
| 2796 | read | medium | f. 371 is the same letter, "Copy which was intercepted by Admiral Matthews", filed beside f. 365 |
| 1794 | read | medium | Each of the eight has its clear text in the series (/16/12-13 are duplicates of /16/10-11, two marked "[original partly in cipher]") |

## Record errors found

- 1795: the lead's shelfmark (SP 89/12/73, f. 123) is the decipherment, not the cipher. The cipher is SP 89/12/74 (f. 124).
- 1884: the lead's date "1693" belongs to Paget's letter (2 Oct 1693). The item itself is dated 8/18 Jan 1694, and it is a
  letter-book copy (hand of Plantamour), not a received letter.
- 1137: PRO 30/55/16/147, the first link, is the key ("Proposed Cypher"), not a letter.
- 1154: the record says the key "may be on SP 84/165/36 and /70". Those are additions to the cipher. The full key is
  SP 106/6 nos. 32-33.

## Routes

- TNA children endpoint: `limit` up to 500 (1000 returns 400); page with `batchStartRecordId` (inclusive). The `note`
  field ("Deciphered copy", "Partly in cipher", hand) is only in the details call, not in the children listing.
