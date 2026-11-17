# Wave 20 vetting, batch b05 (16 Nov 2026)

18 leads: 1850 1171 1177 1849 1197 1176 1198 2917 2926 1605 2831 2829 2830 2733 2731 2735 2724 2742.
Proposals in `proposals.json` (gate-shaped `vetting` blocks; nothing applied to `research/leads.json` or `catalogue.json`).
Tomokiyo `unsolved.htm` and Lasry `GL.htm` were fetched 15 Nov 2026 (session scratchpad copies, grepped with `tl.py`).
Scripts: `tl.py` (Tomokiyo/Lasry grep), `gimg.py` (Gallica via openapi.bnf.fr IIIF), `fetch_text.py`, `amc.py` (BnF
Archives et manuscrits cipher components via the Omont audit's `am.py`), `add.py` (merges `p/*.json` into proposals),
`grep_prior.py` (earlier vetting outputs). Images and raw pages in `img/` (git-ignored).

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 1850 | read | medium | Mazarine Ms 4376's cipher items are the Du Fargis letters plus name keys of March 1650; the 1650 recueil "Journal de M. le Cardinal duc de Richelieu" prints the Du Fargis letters and the name key (Fabula 2024 article) |
| 2733 | partly_read | high | Salviati 1525 is fr. 2933 no. 11 f. 54 = target salviati1525 (Lasry, in part); f. 54r seen |
| 2917 | partly_read | medium | BL Add MS 32499 item 25, ff. 285, 285b: "Two letters, apparently Jacobite ... Copies; partially deciphered" = Wallis's interlined conjectures |
| 2926 | open | low | HMC Portland VIII p. 235: "eleven small folios of cypher in numbers", Blencowe failed; no reading printed; volume of Add MS 70001-70523 not identified; Bobin's keys beside them untested |
| 2829 | read | high | fr. 3645 notice: Biron nos. 9, 20 and no. 55 "avec chiffre et déchiffrement"; only no. 52 (f. 92, 11 Nov 1591) has none (possible narrow lead, not online) |
| 2830 | read | high | fr. 3362 no. 10 "avec chiffre et déchiffrement"; no. 56 f. 85 is a Farnese key ("Chiffres nouveaux pour le secretaire de monseigneur Alexandre") |
| 2731 | read | high | fr. 2988: f. 1 solved by Andersson 2017; Ranzo read (ranzo1528); nos. 7-55 are Mary Stuart's letters (Lasry, Biermann, Tomokiyo 2023); Raince no. 2 is a clear copy (seen) |
| 2735 | read | high | fr. 3045 no. 29 ff. 36-38v; f. 38v has an interlinear decipherment (seen); DECODE R4231 (fr. 3045 fol. 36) solved |
| 2724 | key_lookup | medium | Tomokiyo's nevers.htm publishes the Ceppo-Nevers and Nevers-Birago (1572) keys for these fr. 3251 letters; only no. 63 (target birago) is undeciphered; fr. 3252 no. 24 = birago1571 |
| 2742 | duplicate | high | Lanssac 26 Apr 1573 is fr. **4735** no. 51 f. 124 (component display), = target lanssac (read); no. 141 has its decipherment |
| 1171, 1177, 1849, 1197, 1176, 1198, 1605, 2831 | none | - | blockers below |

## Not assessed (blockers)

- 1171: Montpellier H 258 is on the Foli@ viewer (302 to curl now, JS session); the Calames notice is a JS shell. Needs Chrome.
- 1177, 1176: Chantilly Ms 1905 / Ms 2080 not digitised; the notices name only a decipherment table. Calames works by curl again (16 Nov).
- 1849: Sorbonne MSVC 3 no. 39, authorisation only; "chiffres" may be numerals.
- 1197: Ste-Geneviève Ms 2571 fol. 58 (1713, not 1752), no scan.
- 1198: BNU Ms.1.833; the printed CGM t. 47 (1923) p. 385 adds nothing ("Manuscrit cryptographique", 115 ff.).
- 1605: BNE Digital and datos.bne.es 403 (Cloudflare).
- 2831: Clairambault 528 notice cc13874f found; one "lettre chiffrée" among pp. 91, 101, 115, not digitised.

## Record errors found

- 2742: the corrected shelfmark in the 16 Nov audit (fr. 4734, tome I) is itself wrong: the BnF component display gives Français 4735 (tome II), f. 124, as targets/lanssac already has.
- 2735: the Cenalis letter runs ff. 36-38v; its cipher passage (f. 38v) carries an interlinear decipherment the notice does not mention.
- 2731: the audit's "No decipherment noted" is true of the notice, but the 26 pièces en chiffre are published as solved (Mary Stuart, 2023), and Raince no. 2 is a clear double, not cipher.
- 2724: the BnF notice marks most Birago letters "avec chiffre" only, but Tomokiyo notes decipherments with nos. 14, 20, 42 and 87; the three cipher lines seen on f. 82 are bare.
- 2831: the lead says three letters are ciphered; the notice says one "lettre chiffrée" among pp. 91, 101, 115.
- 1197: date 1752 is wrong (fol. 58 letter is 1713).
- 2917: shelfmark should add ff. 285, 285b (the copies).
