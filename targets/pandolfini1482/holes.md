# Hole Ledger & Polyphonic Sure-Word Audit — Pierfilippo Pandolfini -> Lorenzo de' Medici (Cat. Nos. 2574 & 2559)

Computed programmatically by `word_audit.py` -> `sure_words.tsv` (alongside `research/reading_audit/v10_relabel.py`). Under "Only sure words count" (cf. `targets/edmondes1594/scripts/sure_words.py`), a plain cipher word is counted as **unambiguous sure** only when it aligns verbatim with the Grade-1 mechanical decryption (`key_pandolfini1482.tsv`) and at most one expansion of its polyphonic slots (`II=a/o`, `9=e/l`, `sig=t/d`, `pi=t/b`, `d=c/g`) is an attested Italian word in `lang/lexicons/it.json.gz` (count `>= 10`, folding `u/v`, `j/i`, and geminates). Plain words where two or more expansions form attested Italian words (*la/lo, a/o, cosa/casa, questo/questa, et/ed*) rely on sense and are classed as `key, by sense` (probable).

## Summary Totals (Cipher Words Only)

| Document | Clear Markup | Unambiguous Sure (`sure_words.tsv`) | `key, by sense` | Unbracketed Departures | Explicit Holes | Total Cipher Words | Strict `read_share` (`sure_words.tsv`) | `v10_relabel.py` Plain Share | Extent Verdict (`>= 0.95`) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Cat. 2574** (`MAP XXXVIII, doc. 418`, 27 Mar 1483) | `⟨⟩` | **101** (`50` mono + `51` poly) | 40 | 3 (`L25 qelo`, `L26 qo`, `L30 sea`) | 95 | 239 | **0.423** (`42.3%`) | `144/239 = 0.603` | `read in part` |
| **Cat. 2559** (`MAP LIII, doc. 13`, Apr 1483) | none (pure cipher) | **112** (`49` mono + `63` poly) | 46 | 0 | 44 | 202 | **0.554** (`55.4%`) | `158/202 = 0.782` | `read in part` |
| **Combined** | — | **213** | **86** | **3** | **139** | **441** | **0.483** (`48.3%`) | `302/441 = 0.685` | **`read in part`** |

## Explicit Hole Breakdown by Category (`139` Bracketed Tokens)

| Category | Cat. 2574 (`reading_2574.md`) | Cat. 2559 (`reading_2559.md`) | Total | Description |
|---|---:|---:|---:|---|
| Open diplomatic nomenclators | 6 | 6 | 12 | `{oo?}` (3×), `{B?}` (5×), `{invT?}` (2×), `{Hcr?}` (1×), `[...]` (1× in `#2574 L20`) |
| Open Latin cover words | 3 | 0 | 3 | `{?ocusa}` (`#2574 L20`), `{?grandis}` (`#2574 L20`), `{?grandes}` (`#2574 L24`, subject slot before `pigliassi`) |
| Contextual or uncertain local spans | 38 | 12 | 50 | Local noisy runs (notably `#2574 L05–L07`, `L10–L14`, `L24–L25`, `L29–L31`; `#2559 L01–L02`, `L07`, and `#2559 L10 [?tr]` from unresolved `V e` after `ire`) |
| Grade-2 refinements / paleographic slips | 48 | 26 | 74 | Words relying on Grade-2 refinements (`b={c,f}`, `o_base={a,d}`, `y={h,g}`, `D={c,b}`, `H=p`, `V=t`, provisional `[Rx]` in `#2574 L09 [debia]`), crop-verified `1 p 9 = che`, minor scribal slips, or mechanical departures (`#2574` `[pensieri]`/`pensier(a/o)`, `[dicono]`/`dic(t/d)(a/o)no`, `[desiderio]`/`desiedrio`, `[suo]`; `#2559` `[praticha]`, `[pocha]`, `[questa]`) |

## Cipher Nulls & Embedded Latin Cover Words (`decrypt.py` -> `decryption_*.txt`)

- **Letters emitted vs. nulls:** `#2574` emits `956/1,114` (`85.8%`) letters, omits `109` cipher nulls, maps `20` Latin null tokens, and leaves `29` open/provisional tokens (`9` `[Rx]`, `9` `[tf_lig]`, `11` open nomenclators/signs -> `1,085/1,114 = 97.4%` mapped); `#2559` emits `811/863` (`94.0%`) letters, omits `29` cipher nulls, maps `11` Latin null tokens, and leaves `12` open/provisional tokens (`3` `[Rx]`, `1` `[tf_lig]`, `8` open nomenclators -> `851/863 = 98.6%` mapped).
- **Confirmed Grade-1 cipher nulls (6 types, omitted in running prose):** `b_bar` (29×), `h_bar` (26×), `alp` (21×), `div` (21×), `x` (19×), `wavy` (7×).
- **Provisional Grade-2 signs:** `Mx` (15×, provisional null omitted in `decrypt.py`), `Rx` (12×, emitted explicitly as `[Rx]` in `decryption_2574.txt` and `decryption_2559.txt`; `Rx=che` rejected at `-35.4` raw nats), and `tf_lig` (10×, emitted as `[tf_lig]`).
- **Verified *nihil importantes* Latin nulls (7 types, omitted in running prose, matching Laurentian keys `MAP LXXII 178` & `CXIX 125`):** `LAT_nam` (4×), `LAT_Si` (3×), `V t = {LAT:ut}` (8×: 5× in `#2574`, 3× in `#2559`), `V 3 = {LAT:vz.}` (2×), `LAT_iterum` (2×), `LAT_quotiens` (1×), `LAT_dumnon` (1×).
- **Kept open as holes in `reading_2574.md`:** `{?grandes}` (occupies grammatical subject slot before 3rd-singular verb `pigliassi` on `L24`, likely a Latin cover noun like `MAP LXXII 181`), `{?grandis}` (`L20`), and `{?ocusa}` (`L20`).

## Open Diplomatic Nomenclators (All 4 Kept Unsubstituted)

1. **`{oo?}` (`o o`, 3×: `#2574 L15`, `#2559 L01`, `#2559 L12`):** Singular person seeking Faenza (`tenendo {oo?} in speranza di Faenza`, `persuadere al {oo?}`); contextual candidate: Count Girolamo Riario.
2. **`{B?}` (`B`, 5×: `#2574 L25, L26`; `#2559 L01, L16, L17`):** Grammatically plural state (`con {B?} ... con loro`) targeted by Sixtus IV's papal bull (`publicare [questa] [benedeta] bola contro a {B?}`); contextual candidate: the Venetians (*i Viniziani*).
3. **`{invT?}` (`invT` / `⊥`, 2×: `#2574 L22, L26`):** Condottiere whose re-engagement was approved at the Diet of Cremona (`che hora si riconducha {invT?} intendendo che alla dieta, così parve a tutti, si dovessi fare`); contextual candidates: Costanzo Sforza, Virginio Orsini, or Niccolò Orsini.
4. **`{Hcr?}` (`H_cr`, 1×: `#2559 L17`):** Closing diplomatic object (`disporebe ancora più {B?} [a] pratiche di {Hcr?}`); contextual candidate: *pace* (peace).
