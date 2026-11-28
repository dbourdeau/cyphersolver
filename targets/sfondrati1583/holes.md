# Hole Ledger & Word-Sense Audit — Terranova -> Sfondrati (Cat. Nos. 2077 & 2518)

Every bracketed token (`{tok?}`, `{N~?}`, `{stain?}`, `[word]`, `[?word]`) in `reading_2077.md` and `reading_2518.md` is counted as an explicit hole by `word_audit.py` and Cyphersolver's `research/reading_audit/v10_relabel.py` (`clear_markup=⟨⟩`), which agree to the exact integer across both documents (0 doubtful words, 0 undeclared marks).

## Summary Totals (Cipher Words Only, Clear Framing Excluded)

| Document | Clear Markup | Sure Cipher Words (`v10` = `word_audit`) | Explicit Holes (`v10` = `word_audit`) | Total Cipher Words | Strict `read_share` | Extent Verdict (>= 0.95) |
|---|---|---:|---:|---:|---:|---|
| **Cat. 2077** (`BYU Vault MSS 771`, selected 5 items, Aug–Sep 1583) | `⟨⟩` | 1,272 | 496 | 1,768 | **0.719** (`71.9%`) | `read in part` |
| **Cat. 2518** (`BYU Vault MSS 518 f. 3 item 2`, 5 Oct 1583) | `⟨⟩` | 128 | 68 | 196 | **0.653** (`65.3%`) | `read in part` |
| **Combined** | — | **1,400** | **564** | **1,964** | **0.713** (`71.3%`) | **`read in part`** |

## Hole Breakdown by Category (Exact Sum = 496 + 68 = 564)

| Category | Cat. 2077 (`reading_2077.md`) | Cat. 2518 (`reading_2518.md`) | Total | Description |
|---|---:|---:|---:|---|
| Open `Cg.12` nomenclators (`{tok?}`) | 221 | 30 | 251 | Unglossed Tier-A closed-class codes (`{ful?}`, `{sa?}`, `{95?}`, `{Si?}`, `{xol?}`, `{xa?}`) and Tier-B political/diplomatic entities (`{sim?}`, `{hom?}`, `{him?}`, `{58=?}`, `{cem?}`, `{98e=^?}`, `{hol?}`, `{Co?}`, `{vul?}`, `{vil?}`, `{gil?}`, `{com?}`, `{nul?}`, `{55?}`, `{71=^?}`, `{21=?}`, `{38=?}`, `{48=?}`, etc.) kept unsubstituted. |
| Literal numeral overbars (`{N~?}`) | 10 | 2 | 12 | Overbarred calendar days and sums (`{11~?}`, `{8~?}`, `{4~?}`, `{100~?}`, `{3~?}`, `{15~?}`, `{2~?}`, `{5~?}`, `{10~?}`). |
| Water-stain lacunae (`{stain?}`) | 0 | 3 | 3 | Three bleached manuscript spots on `#2518 p. 1 L01–L03` (marked `[stain]` in `diplomatic_2518.txt`, zero guessing). |
| Uncertain or residual local spans (`[?word]`) | 28 | 2 | 30 | Unresolved, damaged, or short residual spans (`[?humala]`, `[?e]`, `[?designio]`, `[?ad]`, `[?ado]`, `[?enti]`, `[?ela]`, `[?didilu]`, `[?lleuo]`, `[?do]`, `[?tan]`, `[?entendidas]`, `[?alguna]`, `[?ageno]`, `[?o]`, `[?uisto]`, `[?diyor]`, `[?lo]`, `[?span]`, `[?no]`, `[?yey]`, `[?primigenitura]`, `[?dar]`, `[?consi]`, `[?chichiest]`; `#2518`: `[?e]`, `[?temes]`). |
| Graphic alternatives, Grade-3 singletons, absorbed open signs & scribal repairs (`[word]`) | 237 | 31 | 268 | Whole-word brackets for every contextual alternative (`21=da`, `16=bu`, `26=du`, `34` vs `32+=pli` scan doubt), cursive `11+/11| -> 14+/14|` disambiguation, every Grade-3 singleton dependency (`[los]`, `[proprio]`, `[yo]`, `[a]`, `[aduertir]`, `[instrucion]`, `[honrrado]`, `[peligro]`, `[oficio]`, `[embiar]`; `#2518`: `[hora]`, `[uoluntad]`, `[madrid]`, `[suyo]`), all 7 absorbed open signs (`[tomar]`, `[margen]`, both `[cuya]`, `[sabe]`, `[de]`, `[aduertido]`), and every clerk/scan repair departing from literal `decryption_2077.txt` / `decryption_2518.txt`. |
| **Total explicit holes** | **496** | **68** | **564** | **Exact match to `v10_relabel.py` (`496 + 68 = 564`).** |

## Mechanical Open-Token Counts

- **Cat. `#2077` (`decryption_2077.txt`):** `242` open mechanical tokens (`3,116 - 2,874 = 242`) across `86` open types (the difference between `242` raw mechanical open tokens and `231` `{tok?}`/`{N~?}` tokens in `reading_2077.md` comes from the 7 open signs absorbed inside bracketed `[word]` repairs, `3°` omitted by declared circled-cancellation convention on Item 19 p. 1 L05, and 3 open tokens merged into bracketed `[?word]`/`[word]` spans such as `[orejas]`/`[semejante]`/`[alojada]`).
- **Cat. `#2518` (`decryption_2518.txt`):** `35` open mechanical tokens (`323 - 288 = 35`) across `26` open types (`32` kept as `{tok?}`/`{N~?}` in `reading_2518.md`, plus `3` absorbed inside bracketed `[pliego]`, `[cumplimiento]`, `[cuya]`).
- **Combined:** `277` open mechanical tokens across `91` open types in `key.tsv`.

## Provenance-Graded Nomenclator Candidates (Kept Outside Readings)

- **Plural group candidate (`{98e=^?}`):** Occurs `2×` in Item 6 alongside Joyeuse and Nevers (*franceses* remains an unverified contextual hypothesis and is left open).
- **Tier-A closed-class Spanish candidates:** `{ful?}` = *para*, `{sa?}` = *más* (*de más*), `{95?}` = *como*, `{xol?}` = *lo que / quanto*, `{xa?}` = *muy / tan*, `{Si?}` = *-mente* adverbial suffix.
- **Tier-B diplomatic entity candidates:**
  - `{sim?}` = *V. S.* (*Vuestra Señoría*, Baron Paolo Sfondrati).
  - `{hom?}` = *S. A.* (*Su Alteza*, Duke Charles Emmanuel I of Savoy in `#2077`; in `#2518` its referent is ambiguous between *Su Alteza* and *Su Majestad* and is left unforced).
  - `{him?}` = *S. M.* (*Su Majestad*, King Philip II).
  - `{58=?}` = *Duque*; `{cem?}` / `{cem^?}` = *Señor* / *Señores*; `{hol?}` = *persona*; `{nul?}` = *Príncipe* (Gian Andrea Doria); `{55?}` = *Don* (Pedro de Aragón); `{71=^?}` = *escudos / ducados*; `{21=?}` = *correo / despacho*; `{38=?}` = *correo / despachar*; `{48=?}` = *dinero / cambio*; `{Co?}` = *gente / compañía*; `{gil?}` = *plática*; `{vul?}` = *respuesta / resolución*; `{vil?}` = *resolución / orden*; `{com?}` = *servicio*.
