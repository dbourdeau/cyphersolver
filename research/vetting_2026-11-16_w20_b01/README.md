# Wave 20 vetting, batch b01 (16 Nov 2026)

Leads: 2710 2709 2708 2711 2699 2700 2701 2702 2703 2704 2707 2706 2705 (AHNOB via PARES) and 2930 2931 2932 2933 2935
(AHU via DigitArq). Proposals in `proposals.json` (written by `make_proposals.py`); prior-art greps in `prior.py` / `prior_out.txt`.

## Access this session
- **PARES** (pares.cultura.gob.es) still answered **HTTP 429** on 16 Nov 2026, to curl from this machine and to WebFetch
  (a different network). No record or image was reopened. Record titles come from `research/pares_ags/hits.jsonl` and
  `research/sweep_2026-11_spain_nobility_aca/screen.json`. The ministry's `www.mcu.es/ccbae` exhibition pages also gave 429.
- **DigitArq** API `/api/docs/details/<id>` answered; every AHU record in this batch still has `hasImages: false`.
- Tomokiyo `unsolved.htm` and Lasry `GL.htm` were the copies fetched on 15 Nov 2026. known.py was run per lead (`prior.py`).

## Results
| id | verdict | confidence | deciding fact |
|---|---|---|---|
| 2708 | open | medium | PARES: "Correspondencia cifrada remitida por el príncipe de Ligni ... al conde de Oropesa", 1670, no images, no decipherment named; no prior art. Place is Sicily, not Brussels |
| 2709 | open | low | PARES: "por cédula y despacho cifrado" (FRIAS,C.635,D.33-41, 1647), no images; drop C.1389,D.28 (no cipher in its title) |
| 2711 | not_cipher | medium | "serie de cifras" with a note "Dos copias para Sánchez Román y otra para la demanda" plus a list of 1906 plenary dates: numbers for a lawsuit |
| 2710 | none | - | "remitiendo dos cifras" = key tables sent; probably a key lead; PARES 429 |
| 2699, 2700, 2701, 2705, 2706 | none | - | titles name no cipher (hit came from unseen text); images online but PARES 429 |
| 2702 | none | - | titles name no cipher; no images; can't quote the archive's cipher description |
| 2703 | none | - | D.17 has a "Copia carta cifrada" (probably the decoded copy); Osuna Rome letters carry plain copies; only D.8 and D.29 name a cipher |
| 2704 | none | - | the PARES title would pass, but an mcu.es exhibition page shows a "carta parcialmente cifrada" of a Milan governor with its decryption (429, unchecked) |
| 2707 | none | - | three writers (split it); images online but PARES 429; CT.15,D.5 "Fragmento cifrado", CT.18,D.56 hit "no descifrada" |
| 2930-2933, 2935 | none | - | the 14 Nov blocker stands: no scans, and the descriptions don't say whether cipher groups or decodes survive |

## Record errors found
- 2708: place "Brussels -> Madrid" is wrong. In 1670 Ligne was viceroy of Sicily (Parliament, castles, Messina).
- 2709: the second record, FRIAS,C.1389,D.28, names no cipher in its title.
- 2711: the year 1800 is a placeholder. The companion document is dated 1906.
- 2701: D.88 is a request for a new cipher, not ciphertext.
