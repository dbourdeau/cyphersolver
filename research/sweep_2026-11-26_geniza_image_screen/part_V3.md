# Part V3: PGP 17961 and 41368 (26 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5) for Daniel Bourdeau. Both documents seen; neither is a cipher. No row written (`candidates_V3.json` is `[]`).

## 17961, CUL T-S AS 156.48 verso: not a cipher (ordinary Hebrew-script writing, turned sideways)

- Seen: image 2 (2000x1373 px whole slip; cipher area re-fetched from CUDL at 2000 px across, about 85% of the slip width, then rotated 90 degrees counter-clockwise). Slip about 9 x 4 cm, 8 columns of short word groups in blotchy ink.
- Rotated, each "vertical line" is one short word group in ordinary Hebrew letters (mem, vav, resh, tav, he, bet, gimel, pe, ayin, lamed, nun are recognisable); the "curly dotted signs" are splotchy ink and the Judaeo-Arabic dots on gimel, dalet, tet and tsade. No sign outside the Hebrew alphabet; no sign inventory beyond 22 letters. I could read the shapes but not give a full transcription (words such as ומרות / הרבות / גם / פרע... are tentative), so the verso is not read, but it is not an unusual script. It is not Maghribi or rotated Arabic.
- Context: the recto is Alan Elbaum's digital edition (PGP footnote 2022; Judaeo-Arabic note on 20 raṭl of white rice, Binyamin, Bishr). The verso text is probably a continuation or an added note written with the slip turned 90 degrees.
- Duplicates: `known.py` "AS 156.48": no hits; "17961" only unrelated Calames rows; `decode_search.py` "T-S AS 156.48", "Genizah", "Geniza": 0 rows; not in leads.json, catalogue.json or any candidates.json.
- Prior art searched: PGP footnotes.csv (recto edition only); web search shelfmark with cipher/decipher/secret script (only PGP pages, nothing for this shelfmark); Tomokiyo `unsolved.htm` and `GL.htm` fetched and grepped for Genizah, Geniza, Cairo, Bohak, Judaeo, Hebrew, the shelfmarks: no hit.
- Keys: none applicable; Bohak ring-letter key and Elbaum's dotted alef-tet cipher (T-S AS 205.186) do not match (plain Hebrew letters, no ring signs).

## 41368, CUL T-S AS 185.19 verso: not a cipher (Hebrew alphabet exercise)

- Seen: image 2 (1519x2000 px whole leaf) plus a CUDL region crop of the text (607x2000 px native strip, rotated 90 degrees clockwise). Image 1 (recto) could not be fetched (proxy resets), so the recto is known only from the PGP description.
- Two lines of one neat square Hebrew hand, each letter with a small tick (serif or dot) over or under it. Rotated, they read as the Hebrew alphabet in pairs, with final forms: אב גד הוזח טי כך למם נן סע פף צץ (line 1) and the same sequence again (line 2, the left end cut off, ending around קר שת). So: a letter exercise (alphabet written twice, with final forms), the genre PGP calls writing exercises (T-S AS 210.5) and Cambridge files under T-S K5. No acrostic, no shuffle. A signature-like scrawl sits at upper right.
- PGP description (Elbaum, Dec 2025, probably of the recto): note to Muʿallim Mordekhay, probably Ottoman-era; opening line "Why do you say that I went to the synagogue and didn't pray?", read as Judaeo-Arabic colloquial. No cipher mentioned.
- Duplicates: `known.py` "AS 185.19": no hits ("41368" matched only unrelated Ilten notes); `decode_search.py` as above: 0; not in leads.json or catalogue.json.
- Prior art searched: PGP footnotes.csv (no record for this document); web search shelfmark with cipher/decipher/secret script (only the PGP page, no cipher claim); web search on Geniza alphabet exercises with final forms (genre well attested); Tomokiyo unsolved.htm and GL.htm grepped: no hit.
- Keys: none needed.

Routes: CUDL IIIF by plain curl (proxy resets some requests; retries worked except 41368 recto), PGP dump, footnotes.csv, cryptiana by curl. Not checked: FGP catalogue, CUDL search (WAF), Elbaum's unpublished editions beyond the PGP footnote.
