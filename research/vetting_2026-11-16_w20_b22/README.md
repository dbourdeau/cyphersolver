# Vetting wave 20, batch 22 (16 Nov 2026)

Claude Code session (Claude Opus 5.5). Leads 2688 2682 2681 2679 2680 2584 2684 2685 1632 2878 2154 2220 2221 2219 2095 2786 2785 2787.
Proposals only (`proposals.json`); nothing applied to `research/leads.json` or `catalogue.json`. Vetting blocks pass `vetting_problems`
apart from the verdict rule for closed leads. Tomokiyo and Lasry lists: the copies fetched 15 Nov 2026 (`prior.py`, `prior_out.txt`: no hit
for any lead). One script per lead (`l<id>.py`, `ltna.py`, `lblocked.py`, `lteleki.py`) writes its entry through `common.py` / `put.py`.

## Results

| lead | verdict | conf. | deciding fact |
|---|---|---|---|
| 2688 | read | high | all four Martinuzzi 1542 regests deciphered on file (interlinear / separate sheet) and printed in Károlyi, Történelmi Tár 1878 |
| 2682 | read | high | all 30 Malvezzi cipher regests in Türkei I Kt. 8-9 carry a contemporary or 19th-c. decipherment; 27 cite Nehring, Austro-Turcica |
| 2681 | partly_read | medium | Czernovich: 153 cipher regests 1556-66, all deciphered except 45148 (14 Feb 1565, partly) and duplicate 44618 (16 Aug 1562) |
| 2679 | partly_read | medium | Stöckl: all deciphered or with clear copies (46258 has clear copy 46363) except 46230 (18 Sep 1569) |
| 2680 | read | medium | Provisionali: the all-cipher 46702 is a second exemplar of the deciphered 46703 of the same day |
| 2584 | key_lookup | low | fol. 178 one cipher page; fol. 180-184 of the same Konvolut is 'egy darab rejtjelkulcs' (47912); Ungnad key R392; part of lead 1220 |
| 2684 | duplicate | high | Donellanus and Mednyánszky letters deciphered on file; undeciphered residue is already catalogue 2455 and 1231 |
| 2685 | not_cipher | medium | Gembicki to Péter Zrínyi, 4 Oct 1669: Latin original with enclosed keys; key material for DECODE, not a ciphertext |
| 2785 | read | high | TNA: both Hillyar reports 'deciphered at the Admiralty', decipher summarised in the catalogue |
| 2786 | read | high | TNA: 'Written in cypher code and decrypted' |
| 1632, 2878, 2154, 2095, 2220, 2221, 2219, 2787 | none | low | blockers in `proposals.json` notes |

## Record errors found

- 2688: 154594 (29 May 1542) is to Johann Wese, archbishop of **Lund**, not Esztergom; the four pieces are fol. 193-196, 205-207, 210-215, 218.
- 2681: the series is about 153 cipher regests (Kt. 12-21, 1556-66), not 10.
- 2684: senders are Fr. Nicolaus Donellanus OSA and Jónás Mednyánszky; the open pieces are catalogue 2455 / 1231.
- 2685: sender Andreas Gembicki, recipient Péter Zrínyi; the letter is plain Latin with keys enclosed.
- 2785: the cipher enclosures are ff. 251-252 **and** 253-254.

## Routes and blocks today

- Hungaricana archives regests by script (`hsearch.py`, `regest.py` from batch 12): worked all session. Hungaricana Library answers too,
  but holds only citations of Teleki Mihály levelezése, not the volumes.
- DDB Solr API gave the full LABW record for 1632 (`q=id:<DDB id>`).
- TNA Discovery API details by curl: worked.
- OAC finding aid by curl: worked (2878 folder title only). Stanford SearchWorks: no answer to curl.
- TARO (txarchives.org): Anubis proof-of-work bot check. books.google.com page view: 403 'automated queries'; Books API quota exhausted.
  Google Books volume ids for Teleki levelezése II, IV, VIII are in the 2219-2221 notes for a Chrome session.
