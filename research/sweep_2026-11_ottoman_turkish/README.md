# Ottoman and Turkish sweep (2 Nov 2026)

`candidates.json` holds **6 rows** (built by `make_candidates.py`), far short of the 60 asked for. They are leads scored
from catalogue text, none viewed on an image. Nothing was padded.

## Why so few

The Turkish-side sources are closed to scripts, and the European archives that hold Ottoman-related ciphers were already
swept by earlier passes (HHStA Türkei I in `aut_hhsta`, `central_archives`, `sweep_2026-11_hhsta_ais`; AGAD in
`polish_archives`/`chrome_pass_2026-11`; TNA State Papers in `sweep_2026-11_tna_state_papers`; Dubrovnik/Greek in
`sweep_2026-11_balkans_greek`). What was left is what these 6 rows are.

## Sources tried

| Source | Result |
|---|---|
| BOA, katalog.devletarsivleri.gov.tr | Reachable, but the catalogue needs a member login with a CAPTCHA (`LoginOnay.aspx`). Not logged in, not swept. Needs the user to search it. |
| yazmalar.gov.tr (Turkish manuscripts) | TLS name mismatch on https; plain http returns 404. Not swept (and it lists books, not letters). |
| Atatürk Library (katalog.ibb.gov.tr), TBMM, Topkapı | No connection from this machine. Not swept. |
| Archives Portal Europe | Cloudflare check ("Just a moment"). Not tried in Chrome: `sweep_2026-11_archivportal_more` covers that ground. |
| SALT Research (archives.saltresearch.org; Ottoman Bank and Turkish private archives) | curl 403; opened in Chrome without a check, 18 terms (şifreli, şifre anahtarı, şifreli telgraf, rumuz, kod defteri ...) as same-origin `fetch`, 2.5 s apart, one tab, closed. Gave 1 row (Eldem). The 1940-41 Başvekalet circulars "şifreli suret" are plain copies of ciphered orders, not ciphertext. |
| TNA Discovery API | About 50 Ottoman-flavoured queries (Constantinople, Porte, Smyrna, Aleppo, Pasha, Grand Vizier, Ainslie ...) plus FO 78/195/142/861/424/881/139/352 series searches, to 1950. 205 records, nearly all noise (HW 15 Soviet-in-Istanbul 1944, YLG Lloyd George 1920-22, SP 91 Russia). 5 new rows; SP 105/60/121, /7, /135 and SP 35/50/82 were already leads. |
| Nationaal Archief, Legatie Turkije (1.02.20), consuls at Smyrna (1.02.22), Coly (1.02.19) | Whole inventories dumped through the EAD API and grepped for cijfer/geheimschrift/sleutel: only **keys**, no ciphertext (see below). |
| Europeana API | Ottoman place words AND cipher words, 1300-1950, text only: 97 records, all BnF Persian/Turkish literary manuscripts or noise. 0 rows. |
| Kalliope | Already exhausted by `kalliope_ddb`/`central_archives`; 224 "Chiffre" records in total; not re-run. |

## Key leads (bare keys, no ciphertext; not rows)

Nationaal Archief 1.02.20 (Legatie Turkije), digitised: inv. 17 (keys, secret writing used with the States General and
Dutch diplomats, 1668), 164 (cijferschrift keys), 628, 686, 785 (sleutel geheimschrift). 1.02.22 inv. 112 (a cipher key
for the Dutch diplomatic service, 1611; physical only). Useful for Dutch Levant letters in the Staten-Generaal files.

## Not reached

BOA (login), Turkish libraries, Hungaricana (403), Salt's Ottoman Bank scans (rows only for the Eldem notebooks),
ASVe bailo despatches (no item-level catalogue), Genoa and Malta, the Romanian and Serbian archives, archive.org
full text for Ottoman terms (covered by the `ia_*` sweeps).
