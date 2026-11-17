# Wave 20 vetting, batch b09 (16 Nov 2026)

Leads: 2862 2493 2492 2550 2537 2053 2052 2051 2698 2606 2499 1675 2504 2592 2605 2588 2496 2495.
Proposed vetting blocks are in `proposals.json` (applied by the lead agent; leads.json and catalogue.json untouched).
Scripts: `add.py` (merge one proposal), `cgrep.py` (grep Tomokiyo's unsolved.htm and Lasry's GL.htm, fetched 15 Nov 2026).
Images in `img/` (git-ignored).

## 2862 Gonzaga di Guastalla, Alcort papers (DARA): read

DARA item pages and their PDFs fetch by script (no Chrome needed): the item page's attachment link gives
`https://opacaraimagenes.aragon.es/<xx>/<yy>/FHB_CD_ALCORT_D_<nnnn>.pdf`. All four cipher sheets have a decipherment
filed beside them, in a decipherer's spaced letter-by-letter hand: D/0040 -> D/0041 (Spanish), D/0043 -> D/0045
(headed Guastalla 28 July 1683), D/0047 -> D/0048 (23 Aug 1685), D/0051 -> D/0054 (headed 9bre 168[3]; DARA dates
it 1684). Closed as read. The four numeric cipher/plaintext pairs should give the key; worth testing on catalogue
2860, 2861, 2864 (other Alcort cipher items, D/0055, 0056, 0086).

## 2493 Chotzis 'cryptographic document' and 2492 Petimezas EDES cryptograms (GAK): no verdict

Both GAK inventory records re-fetched by curl (they answer); both are fonds-level lists with one-word mentions
('Κρυπτογραφικό έγγραφο'; 'κρυπτογραφικά σημειώματα', 'κρυπτογραφήματα') and no item, extent or plaintext note.
arxeiomnimon.gak.gr still does not connect. Blocker stands: needs GAK scans.

## 2550 Charles of Guelders, three letters (Gelders Archief 0001): no verdict

Nijhoff, Gedenkwaardigheden VI/2 no. 867 still unreachable: archive.org has I-V and VI/3 only (six copies listed by
advancedsearch); Google Books API returns 429 (daily quota 0); HathiTrust full-text search is Cloudflare 403;
Delpher and archieven.nl result pages are JS-only. Lasry's GL.htm has a Duke of Guelders cipher (fr. 3015 f. 16,
c. 1526-36): a possible key, recorded in the note.

## 2537 Arent van Wassenaer correspondence 1707-11 (Gelders 0525 inv. 1240): open, low confidence

Archive description only ('Deels in geheimschrift', no decipherment noted); no DECODE, cryptiana, edition or web hit.
Same footing as catalogue Rosendael inv. 577. Low confidence: recipient's bundle, interlinear decipherments possible.

## 2053 Tilden diary, 2052 Marshall endpapers (Gilder Lehrman): no verdict

Gilder Lehrman item pages give Cloudflare 403 to curl. Tilden p. 34 behind login (no published transcription found
by web search); GLC05605 not digitised. Blockers stand.

## 2051 Kanawha telegrams (GLC02414): partly_read

targets/kanawha1863 NOTES: .341, .229, .344 have 1863 clear copies (.114, .137, .138); .339 none, read in part there.

## 2698 Sijtsma 'Geheimschrift' 1871 (Groninger Archieven 561 inv. 439): not_cipher

Full EAD fetched (OAI): inv. 439 is a loose tabula-recta sheet taken from a photo album; neighbours 436-441 hold no
message, and no other cipher item exists in the fonds. A key sheet with no text: closed.

## 2592 Mary Stuart 1571 (Rep. 11 Akten Nr. 10019): read

ACTApro record pages fetch by curl. Full title: Mary Stuart to [Norfolk] ... '(Dechiffrierung und Übersetzung eines
Geheimberichts)', 6 Bl. A decipherment with translation: read. Lead error: addressee is Norfolk, not Philip II.

## 2588 Derfflinger 1674 (Rep. 34 Nr. 5876): read

UA vol. 13 (archive.org urkundenundacten13berluoft) pp. 793-798 prints Derfflinger's few relations 'in unverkürztem
Wortlaut' (footnote 3, p. 793). Confirmed the 11 Nov sweep's exclusion.

## 2605 de Beziers decipherments 1668 (Rep. 34 Nr. 6676): read

The lead's ACTApro links return an empty page; `https://archive.spk-berlin.de/actaproweb/document/Vz_<uuid>` redirects
to the live record (new id). Record: 'Beilagen zu den Gesandtschaftsberichten von Johann Copes ... Dechiffrierungen
von Briefen des de Beziers, 1668'. Decipherments filed: read.

## 2606 BPH Rep. 35 Nr. 15 (1673): not_cipher

Full record via the document/Vz_ route: the Elector to Schwerin, 'Besorgnis über ein eigenhändig chiffriertes Schreiben
des Kaisers, das der Fürst von Anhalt erhalten hat (Faksimile und Fotokopie)'. The file is a facsimile of a letter
about a cipher letter, not the cipher letter. Closed (medium confidence).

## 2499 Luise Ulrike to August Wilhelm 1756 (BPH Rep. 56 I J Nr. 23): read (medium)

Arnheim vol. 2 (1910) is Google Books iecH_VSLsWoC (snippet). The gdata feed by curl
(`https://www.google.com/books/feeds/volumes?q=...`) still answers; books.google.com redirects to the CAPTCHA, the
googleapis Books API is over quota. Snippets: a letter '[Stockholm], 21 mai [1756]' to August Wilhelm printed in clear
with footnotes 'Chiffrebrief; nicht eigenhändig'. Printed = read.

## 1675 / 2504 Wittgenstein papers 1798, 1808 (BPH Rep. 192): 1675 no verdict, 2504 duplicate of 1675

gdata feed snippets: Stein, Briefe und amtliche Schriften II (1960) calendars 'Wittgenstein an Stein, Hamburg,
22. November 1808, Hausarchiv' declining ciphered correspondence (= I Nr. 1,11, a letter about cipher). Nassauische
Annalen 1929 (Google Books v1ASAAAAIAAJ) prints the autumn 1808 correspondence and notes 'Chiffrierte Schreiben Steins,
nur teilweise vom Empfänger aufgelöst': I Nr. 1,16 may hold partly unread Stein cipher letters. Needs that article.

## 2496 Vrybergen / Lubières 1698-1701 (Rep. 64 Nr. 935): open, low confidence

Japikse's Willem III-Bentinck correspondence is full-text searchable by script:
`https://resources.huygens.knaw.nl/retroboeken/search_new/?SearchableText%3Austring%3Autf8=<term>&book=willemiii&start=0`
(snippets in `class="snippet"`). Vrybergen and Lubières are mentioned, their reports not printed. The Rep. 64 cataloguer
writes 'mit Entzifferung' elsewhere and not here. Low confidence (recipient's papers). Overlaps lead 2586 (lists Nr. 935).

## 2495 Neuchâtel agents' reports 1703-08 (Rep. 64, eleven files): partly_read

Siblings 'mit Entzifferung', Nr. 995 interlinear, key table in Nr. 944, and Bourgeois 1887 (archive.org
neuchteletlapol00bourgoog) uses 'Montmollin à Wartemberg, 23 mars 1705 (en chiffres)' by content. Lead 2586 lists the
same files: reconcile.

## Summary

| Lead | Verdict | Confidence |
|---|---|---|
| 2862 | read | high |
| 2493, 2492 | none (GAK fonds-level only) | - |
| 2550 | none (Nijhoff VI/2 unreachable) | - |
| 2537 | open | low |
| 2053, 2052 | none (Gilder Lehrman login / not digitised) | - |
| 2051 | partly_read | high |
| 2698 | not_cipher | medium |
| 2606 | not_cipher | medium |
| 2499 | read | medium |
| 1675 | none (needs Nassauische Annalen 1929 / Stein II/2) | - |
| 2504 | duplicate of 1675 | high |
| 2592 | read | high |
| 2605 | read | high |
| 2588 | read | high |
| 2496 | open | low |
| 2495 | partly_read | medium |

All vetting blocks pass `vetting_problems` (apart from the expected non-open verdict line).
