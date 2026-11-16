# Vetting wave 20, batch 18 (16 Nov 2026)

18 leads: 2833 2837 2836 2109 2650 2087 2893 2517 1915 2799 2889 2718 1964 1965 1966 2938 2397 2519.
Proposals are in `proposals.json` (made from `p/<id>.json` by `merge.py`). Prior-art greps are in `prior_out.txt` (`prior.py`: known.py plus
Tomokiyo unsolved.htm and Lasry GL.htm, both fetched 15 Nov 2026). Images are in `img/` (git-ignored).

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2833 | none | - | Catalogue card (katzoom Zettel 30758): Autogr. 15/1-3 has 7 enclosures, including '3 Briefe in Geheimschrift; 3 latein. Schriftbl.'. Three cipher letters and three Latin sheets may be cipher plus decipherment. Not digitised. |
| 2837 | read | medium | Tabulae codicum VI p. 54: the 'Copia d'una cifra manifesta con la sententia contenuta in essa' is a 'brevis tractatus de cryptographia' that gives the cipher with its sentence |
| 2836 | open | medium | Kronauer's Masonic Stammbuch is digitised (ONB manifest 1004802B). Fol. 28r has about 12 lines in an invented alphabet; fol. 24r and 31r have pigpen. No decipherment on the pages, and none in Nettl 1957 or on the web |
| 2109 | none | - | Blocker stands (no image; ArchiveGrid blocked) |
| 2650 | read | medium | Open Jerusalem titles give the content of each 1907 cipher telegram (catalogued by Y. Avci), so the file copies are deciphered. The collection is closed (ISA) |
| 2087 | read | medium | Archives West finding aid (opens by curl today): the cipher key and an 'explanation of cipher' are in Mss 370, and Schiwek transcribed all the diaries in 1973. The collection is open to the public |
| 2893 | none | - | Blocker stands (f. 101a not digitised; Bodleian blocked) |
| 2517 | partly_read | low | Mignet II p. 285 uses the cipher content of the 24 Aug 1667 despatch (the margrave of Baden refused); the volume is AAE CP Brandebourg 5. The 27 July despatch is unproven |
| 1915 | read | low | The MNL abstract gives the content of the only cipher passage (CP Turquie 151 f. 11v, Tott's arrival) |
| 2799 | read | high | HMC Braye report p. 167-168: the Duke of York's holograph letter (eight words in cipher) is filed with the key and a deciphered copy, and is printed in Lords' Journals x p. 77. Date Feb 1648, not c. 1670 |
| 2889 | none | - | Blocker stands (no master scan) |
| 2718 | key_lookup | medium | The Tresoar node is an introduction line naming the Brussels Audience section 'Formulaires et chiffres', inv. 1199-1221 (inventory numbers, not dates). It is a key and form-book section, not ciphertext |
| 1964 | none | - | Blocker stands (AP Poznań, no scans) |
| 1965 | none | - | Blocker stands (AP Poznań, no scans) |
| 1966 | none | - | Blocker stands (SOAS catalogue blocked; addressee decides) |
| 2938 | open | low | Theal III p. 388: 'excepting a long letter in cypher' survives in the CO 48 enclosures, and no decipherment is printed. The batavia1800 key is the first to try |
| 2397 | partly_read | medium | The archive record says each letter has a 'parziale decodificazione' |
| 2519 | open | low | PRONI 'Some letters in code'. The 11 Nov block holds, and the 16 Nov web search found nothing |

Routes that worked today: the ONB Alma SRU and the ONB IIIF manifest `api.onb.ac.at/iiif/presentation/v3/manifest/<viewer id>` (the viewer id comes from the
redirect of `data.onb.ac.at/dtl/<id>`); the katzoom catalogue-card GIFs; Archives West by curl (no bot check today); the Tresoar API; the TNA Discovery API.
Blocked today: openjerusalem.org (connection refused), the SOAS catalogue (no connection), Archives Hub (403), Discovery HTML pages (202).
