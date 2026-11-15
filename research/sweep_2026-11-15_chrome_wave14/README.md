# Chrome wave 14 (15 Nov 2026): Latin America, Africa, Oceania, Middle East probes

**Result: 0 new leads, nothing promoted.** Most of the named regions were already swept (latam_mexico, latam_brazil,
latam_southcone, latam_north, oceania_chrome, asia_*, sweep_2026-11_arabic, ottoman sweeps); what was still open was
tried and is recorded here so the next pass skips it.

| Source | Outcome |
|---|---|
| **OAC `cifrado`** (task 3) | `oac.cdlib.org/search?q=cifrado` now serves a "Let's confirm you are human" security check (Begin button). Not clicked. Task left open; retry from the owner's session after the check is cleared. |
| **Memoria Chilena** (`/602/w3-search.php?keywords=`) | Works from Chrome (plain GET, same-origin fetch, 6 s pacing). 'carta cifrada' 0 results; 'cifra' 56 hits, all minisites/capsules (Aguirre Cerda, salitre, etc.), noise; other terms noise as well. Agrees with `latam_southcone`. Note: a JS loop longer than 45 s times out the tool; run it detached into `window.R` and read it back. |
| **eHive** (South Africa/Australia/NZ museums) | `ehive.com/objects?query=cipher`: 86 objects, all royal cyphers on objects and coins. No lead. |
| **Trove** | Search results are drawn only after the API call; results pages are empty without a key (same as `oceania_chrome`, which swept it by the correspondence category). Not repeated. |
| **AGN Colombia** | `consulta.archivogeneral.gov.co` does not resolve (ERR_NAME_NOT_RESOLVED); `archivogeneral.gov.co` is a plain institutional site with no item search. Web search finds no cipher item. |
| **AGN Argentina, Peru, Uruguay, Venezuela, Cuba; Philippines; Macau; BNDigital; SIAN** | Web searches (cifra, carta cifrada, en cifra) return only studies and finding-aid PDFs, no cipher item. Not opened in Chrome: AGN Argentina and SIAN were JS-only or login-gated in `canada_latam` / `latam_brazil`; Peru's `fondosdocumentales.agn.gob.pe` is AtoM but no cipher hit surfaced. The Newberry Ayer Philippine manuscripts (430 items) are the nearest holder; no cipher described. |
| **South Africa** (NAAIRS, Cory) | Web search: only the solved Boer War cipher (NSA 'A Boer War cipher'), TNA Boer War files, and the Stellenbosch 'South Africa War Telegrammes' (203 items, not stated to be cipher). No catalogue route opened. |
| **Sri Lanka** | The VOC Colombo archive: the Ramanacoil 1674 ciphertext (Nationaal Archief 1.04.02) is the HistoCrypt 2019 paper's target, already read; Suriname 1689 also read. Nothing else surfaced. |
| **Ethiopia, Egypt (Dar al-Kutub), Turkey (BOA katalog), Iran, NLI Israel** | No item-level online route found; web search for mu'amma/ramz gives treatises on cryptology and the SOAS cipher Qur'an (read by D'Ottone) and Princeton's Baleybelen, already in `sweep_2026-11_arabic`. |
| **East Asian telegram-code collections** | Not reached beyond `asia_*` and JACAR (scan of rest_refs still running in the worktree, uncommitted). |

Not reached: South African, Sri Lankan, Ethiopian and Philippine catalogues themselves (no open item search found).
