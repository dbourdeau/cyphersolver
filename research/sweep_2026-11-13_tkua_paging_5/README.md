# TKUA paging pass 5 (13 Nov 2026): Indkomne breve, imperial memorials, Stenbock

Continues `research/sweep_2026-11-11_tkua_paging_4/` (scripts copied: `ao.py`, `ra_online.py`, `full.py`, `crop.py`; `q1.sh`/`q8.sh` queue sheets).
**Result: `candidates.json` is `[]`. No rows, no key leads.** The pass was short (about 40 sheets viewed); it did not reach the
paging-4 "sheets made, not viewed" list or the 18th-century Brandenburg/Nederlandene/Polen units.

## Viewed (400 px frames, 20 a sheet; cipher none seen unless noted)

| Unit | Series | Images | Viewed |
|---|---|---|---|
| 260199 | Tyske Kancelli, Indkomne breve c.1513-1675, part 1 | 302 | 1-301 by 4 |
| 260202 | Indkomne breve 1602-75 | 398 | 1-397 by 4 |
| 260643 | Kejseren: imperial envoys' memorials 1700-27 | 431 | 1-429 by 4; 409-410 at 1500 px: a receipt for goods, numbers are bill-of-lading numbers, not cipher |
| 261567 | Sverige: Stenbock memorials 1712-17 | 742 | 1-477 by 4 (481-742 not viewed) |
| 260488 | Indkomne breve 1676-1770, first volume | 517 | by 8 to about 313 (stride-8 sheets, poor film, not complete) |

## Not done
- 261567 481-742; 260488 rest; 260489-260491 (sheets for 260489 on were being made when stopped); Gehejmeregistratur 260237 ff.
- Everything in the paging-4 "Not done" and "Sheets made, not viewed" lists, and the 18th-century units 260779-260844, 262125-262197, 261418-261458, 261305.
- Chiffer 1670-1709 (unit 260610), Juel table and Ahnlund 1920 for Galt: not touched.

## Routes
- `api.rigsarkivet.dk/ao/v1/...` by curl from this network: no block, a 20-frame sheet in about 25-60 s. Scratch: `/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/tkua5/sh`.
- Sampling at 1 in 4 on 400 px frames can miss a short cipher passage inside a clear letter.
