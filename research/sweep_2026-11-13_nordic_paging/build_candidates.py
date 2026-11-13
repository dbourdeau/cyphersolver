"""Builds candidates.json from the ROWS below (13 Nov 2026 Nordic paging sweep). Re-run after adding a row."""
import json
ROWS = []
def row(**k): ROWS.append(k)

row(year=1632, date="26 Mar 1632",
    title="Jakob De la Gardie to Gustav II Adolf: four number-cipher passages in a Swedish despatch, no decipherment on the leaf",
    correspondents="Jakob De la Gardie (field marshal) -> King Gustav II Adolf",
    place="not read (the place before 'den 26 Martij Ao 1632' is struck through / illegible at 2000 px)",
    language="Swedish", region="Scandinavia", period="1611-1650",
    shelfmark="Riksarkivet, Skrivelser till konungen, SE/RA/1133/1133.07/8 (De la Gardie, Jakob, band 1627-1632), image series R0000783, images 197-199",
    folio_note="R0000783 image 198 (right page, printed fol. number 196): in the running Swedish text, three passages of dot-separated 2-4 digit groups (e.g. '0.2106.3185.229.82.73.77.26.31.98.17.82.72.47.92.26 / 26.2837.rr.97.ium / 20.33.50.44.51.83.91.66.72.22.57 / 26.31.3185.ll.26.1420.dg.3506.99.89.92 / 43.93.33.2090') and a fourth short group ('tt.26.24.73.26.80.86') at the foot of the page, continued at the head of image 199; nothing written between the lines or in the margin. Another letter of the same volume (image 195) has number groups with a small gloss written above them: glossed, not this row",
    cls="A",
    status="Viewed 13 Nov 2026: image 198 and 199 downloaded at 2000 px and images 196, 197, 200 at 1100 px, all opened. Bare numeric nomenclator (numbers with dots, a few doubled letters 'rr', 'll', 'tt' among them); no interlinear or marginal plaintext on this leaf. Not found in any of the earlier Riksarkivet sweeps (known.py on the shelfmark and R0000783: no hit). Lead, no vetting block: no printed edition of De la Gardie's letters to the king was found or opened (HSH Kronologiskt register, archive.org handlingarrrand03scangoog, was searched: no letter of De la Gardie of March 1632 is listed).",
    why="A field marshal's despatch to the king in the last year of Gustav II Adolf, with number cipher in the same period and chancery as the glossed Oxenstierna cipher of 1633-35; the context sentences around each passage (Danish troops, 'Förstlandh', ammunition, defence) are readable in Swedish and give cribs.",
    importance=3, solvability=3, difficulty=2,
    score_note="Scored from the scan during the 13 Nov 2026 Nordic paging sweep (research/sweep_2026-11-13_nordic_paging/); viewed at native size",
    verify="Look for the letter in a printed edition (AOSB part 2 for De la Gardie is Oxenstierna's letters, not the king's; try Gustaf II Adolfs skrifter, Styffe 1861, and Svenska riksarkivets pergamentsbref/Riksregistratur calendars); compare the number groups with the glossed Oxenstierna code (1133.08/7-13) and the Riksarkivet 'Chifferklaver' key sheets (DECODE lists records such as 4319-4329) for a De la Gardie key.",
    links=[{"label": "Riksarkivet viewer, image 198", "href": "https://sok.riksarkivet.se/bildvisning/R0000783_00198"},
           {"label": "image 199", "href": "https://sok.riksarkivet.se/bildvisning/R0000783_00199"},
           {"label": "NAD record, Skrivelser till konungen 1133.07/8", "href": "https://sok.riksarkivet.se/?postid=ArkisRef%20SE/RA/1133/1133.07/8"}],
    seen="image", source="Riksarkivet paging sweep 13 Nov",
    prior_art="HSH Kronologiskt register (archive.org handlingarrrand03scangoog, full text grepped for 1632 and De la Gardie): no De la Gardie letter of March 1632; AOSB, Styffe and any De la Gardie edition not opened. DECODE RecordsList?search=Gardie lists only the Riksarkivet Chifferklaver key sheets (broad match), no record for this letter.",
    needs_archive_scan="no",
    access_note="open scans at sok.riksarkivet.se; lbiiif images need the Referer https://sok.riksarkivet.se/ for scripts")

row(year=1627, date="6 Apr 1627 (read 'den 6 Aprilis 1627'; header 'Aprilis 627')",
    title="Johan Banér to Gustav II Adolf: seven number-cipher passages in a Swedish letter of April 1627, no decipherment on the leaf",
    correspondents="Johan Banér (colonel, later field marshal) -> King Gustav II Adolf",
    place="not read",
    language="Swedish", region="Scandinavia", period="1611-1650",
    shelfmark="Riksarkivet, Skrivelser till konungen, SE/RA/1133/1133.07/3 (Banér), image series R0000623, images 356-357 (printed fol. 42-43)",
    folio_note="R0000623 image 357, left page (the letter begins on the right page of image 356 and ends on the right page of image 357 with 'Datum ... den 6 Aprilis 1627'): about 25 lines of running Swedish carrying seven passages of colon-separated 1-3 digit groups (e.g. '85,26,3,15,32,96 / 111,51,60,86,52,20,53 / 100,17,66,8,20,26 / 116,33:96,72:35,45:85,52,70,24,29,56,98,31,10,35,40:71,116,37,3,18,58,29 / ...'), with a Roman 'III' and a possible 'anno 1559' written among them; no writing between the lines or in the margin. Image 358 (a postscript of 7 April) is in clear",
    cls="C",
    status="Viewed 13 Nov 2026: image 357 downloaded at 2000 px, images 356 and 358 at 1100 px. Bare numeric nomenclator in running text; nothing interlinear, marginal or on a separate sheet near it. The volume (R0000623) was only reached by the detector top-64 windows, so other leaves with cipher may remain unlooked at. Known.py on the shelfmark, R0000623 and 'Johan Banér': no hit. Lead, no vetting block: no edition of Banér's letters to the king found or opened.",
    why="A letter of 1627 whose context (Prussian campaign, cavalry, 'Correspondentz', Danish and Polish affairs) is readable Swedish and gives cribs; the code is earlier than the glossed Oxenstierna nomenclator of 1633-35 and may be a Banér-specific one.",
    importance=3, solvability=3, difficulty=3,
    score_note="Scored from the scan during the 13 Nov 2026 Nordic paging sweep (research/sweep_2026-11-13_nordic_paging/); viewed at native size",
    verify="Check whether the letter is printed (Banér's despatches of 1627 in Handlingar rörande Skandinaviens historia or in a Banér biography, e.g. Sjögren / Fryxell-type editions) and whether a Banér key is among the Riksarkivet Chifferklaver sheets or in 1133.07 volumes of the same fonds; look at the other Banér volumes for a glossed letter in the same code.",
    links=[{"label": "Riksarkivet viewer, image 357", "href": "https://sok.riksarkivet.se/bildvisning/R0000623_00357"},
           {"label": "image 356", "href": "https://sok.riksarkivet.se/bildvisning/R0000623_00356"},
           {"label": "image 358", "href": "https://sok.riksarkivet.se/bildvisning/R0000623_00358"}],
    seen="image", source="Riksarkivet paging sweep 13 Nov",
    prior_art="Not opened: any edition of Banér's letters of 1627. HSH Kronologiskt register (archive.org handlingarrrand03scangoog) full text not searched for Banér 1627 yet. DECODE: the key records R4122, R4123, R4325 (Banér keys, from decode_updates/queue.json via targets/baner1640) are known; the letter itself is not recorded there under this shelfmark (queue.json and known.py: no hit).",
    needs_archive_scan="no",
    access_note="open scans at sok.riksarkivet.se; lbiiif images need the Referer https://sok.riksarkivet.se/ for scripts")

json.dump(ROWS, open('candidates.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(ROWS), 'rows')
