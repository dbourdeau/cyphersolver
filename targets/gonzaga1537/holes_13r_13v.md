# Hole Ledger for Modena Estense Campori, Gonzaga Federico II, cc. 13r-13v (catalogue 2162)

Every bracketed token (`[...]`, `[?...]`, `{L..?}`) in `reading_13r_13v.md` is counted as an explicit hole by `word_audit_2162.py` and `research/reading_audit/v10_relabel.py` (`clear_markup=⟨⟩`).

**Totals (cipher words only, excluding inline clear Italian `⟨...⟩`):**
- Sure cipher words (exact key output in `decryption_13r_13v.txt`): **219** (`216` orthographic words)
- Explicit holes: **48**
- Total cipher words: **267** (`264` orthographic words)
- Strict `read_share`: **`0.820` (`82.0%`)** -> **`read in part`** (under the 95% threshold; even the 22 open codes/nulls alone give an upper bound of `91.8%`).

## Breakdown by Category

| Category | Count | Items |
|---|---:|---|
| Open proper-noun nomenclators (`{L2?}`, `{L9?}`, `{L30?}`, `{L36?}`, `[46]`, `[82]`) | 13 | `{L2?}` (4×), `{L30?}` (3×), `{L9?}` (2×), `[46]` (2×), `{L36?}` (1×), `[82]` (1×) |
| Open two-digit codes / candidate nulls (`[23]`, `[24]`, `[27]`, `[28]`, `[29]`, `[31]`, `[53]`) | 9 | `[27]` (2×), `[53]` (2×), `[23]`, `[24]`, `[28]`, `[29]` (`zg`), `[31]` |
| Contextual or uncertain readings | 9 | L01 `[?Fasgnino]`, L03 `[?destimato]`, L04 `[?vero]` `[?è]`, L05 `[?natura]`, L19 `[?si]` `[?è]`, L21 `[?raccomandatione]`, L23 `[?parte]` |
| Scribal slips or rare allographs | 17 | L02 `[più]`, L03 `[più]`, L05 `[ho]`, L06 `[in]`, L08 `[sprezzarà]`, L09 `[el]`, L10 `[demostrato]`, L11 `[quele]`, L13 `[rispetto]`, L15 `[causa]`, L16 `[Al]`, L19 `[alli]`, L19 `[resa]`, L23 `[essendo]`, L27 `[peggiore]`, L27 `[posse]`, L28 `[ultimo]` |

## Line-by-Line Register of All 48 Holes

| # | Line | Reading token | Cipher form | Unedited `decryption_13r_13v.txt` | Category & explanation |
|---:|---|---|---|---|---|
| 1 | L01 | `[?Fasgnino]` | `s4filaxagi` | `\|fanlnino/fasgnino\|` | Contextual/uncertain: addressee in Heading 1 remains open (possible garbled *Cagnino* or agent name). |
| 2 | L02 | `[23]` | `.23.` | `[23]` | Open numeric group (candidate null before `[46]`). |
| 3 | L02 | `[46]` | `46` | `[46]` | Open nomenclator: person criticised in Section 1 (recurs on L10). |
| 4 | L02 | `[più]` | `lizh` | `\|lggu/puu\|` | Scribal slip: `z` written for `3` (`li3h` = *più*). |
| 5 | L03 | `[più]` | `lizh` | `\|lggu/puu\|` | Scribal slip: same `z`/`3` shape as L02 (`li3h` = *più*). |
| 6 | L03 | `[?destimato]` | `icrftb394gb` | `des[t]oimato` | Contextual/uncertain: bare `t` has no standalone key entry (*destimato* / *discostumato*). |
| 7 | L04 | `[27]` | `27` | `[27]` | Open numeric group between `non` and `⟨considerando⟩` (candidate null; recurs on L17). |
| 8 | L04 | `{L2?}` | `{L2}` | `{L2}` | Open underlined-`L` nomenclator (4× total; candidate: King Francis I of France). |
| 9 | L04 | `{L30?}` | `{L30}` | `{L30}` | Open underlined-`L` nomenclator (3× total; candidate: Marchese del Vasto or Guido Rangone). |
| 10 | L04 | `[?vero]` | `uiro` | `h[i]eb` | Contextual/uncertain: requires substantial emendation (`tireb` = *vero*). |
| 11 | L04 | `[?è]` | `e` | `r` | Contextual/uncertain: paired with L04 `uiro` (`e` written for `r` = *è*). |
| 12 | L05 | `[ho]` | `igb` | `sso` | Rare allograph: sole occurrence of `ig` functioning as `h` (vs. regular `ig=ss`). |
| 13 | L05 | `[?natura]` | `fiirsibp 4` | `n[i]eto[p] a` | Contextual/uncertain: garbled two-part token (`fiirsibp 4` for `finsihpi4` = *natura*). |
| 14 | L06 | `[in]` | `iffi` | `[i]sn` | Scribal slip: doubled `ff` / `if` for `in` (`xfi`/`3a`). |
| 15 | L06 | `[53]` | `53` | `[53]` | Open two-digit code (recurs on L22; candidate function word *non*). |
| 16 | L06 | `[24]` | `24` | `[24]` | Open two-digit code between `⟨tenere⟩` and `conto` (candidate null or modifier such as *alcuno*/*gran*). |
| 17 | L08 | `[29]` | `zg` | `ut` | Open short group before `fortuna` (visually `zg`; either a 29-like numeric null or *vo[stra]*). |
| 18 | L08 | `[sprezzarà]` | `riliérla4é4` | `sprelnara` | Scribal slip: `la` written where *sprezzarà* / *sprezarà* needs `zz4` or `l4`. |
| 19 | L09 | `[el]` | `ir&` | `[i]el` | Scribal slip: stray initial `i` stroke before `r&` (`el`). |
| 20 | L10 | `[demostrato]` | `icrggifsie4sigi` | `\|detosfdato/detostrato\|` | Scribal slip: `gg` written for `dg` (`icrdgifsie4sigi` = *demostrato*). |
| 21 | L10 | `[46]` | `.46.` | `[46]` | Open nomenclator (same referent as L02 `[46]`). |
| 22 | L11 | `[quele]` | `meiri4r` | `qr[i]sae` | Scribal slip: `ei` written for `ti` (`mtiri4r` = *quele*). |
| 23 | L11 | `{L9?}` | `{L9}` | `{L9}` | Open underlined-`L` nomenclator (2× total; candidate: Emperor Charles V). |
| 24 | L12 | `{L36?}` | `{L36}` | `{L36}` | Open underlined-`L` nomenclator (1×; territory: candidate Monferrato, Milano, or Savoia). |
| 25 | L12 | `[31]` | `.31.` | `[31]` | Open two-digit code between `se` and `fussi` (candidate null). |
| 26 | L13 | `[rispetto]` | `drflirzogi` | `[d]espetto` | Scribal slip/variant: initial `d` yields `[d]espetto` (*rispetto* or *dispetto*). |
| 27 | L13 | `{L2?}` | `{L2}` | `{L2}` | Open underlined-`L` nomenclator (same referent as L04). |
| 28 | L13 | `{L9?}` | `{L9}` | `{L9}` | Open underlined-`L` nomenclator (same referent as L11). |
| 29 | L14 | `[28]` | `28` | `[28]` | Open two-digit code between `⟨Il⟩` and `vescovo de Casale` (candidate null). |
| 30 | L15 | `[causa]` | `ipirtiri4` | `c[i]eusa` | Scribal slip: `ir` written for `4` (`ip4tiri4` = *causa*). |
| 31 | L16 | `[Al]` | `+ &` | `[+] l` | Heading 2 initial `+` mark before `&` (`l`) = *Al* (or *Dal*). |
| 32 | L16 | `{L2?}` | `{L2}` | `{L2}` | Open underlined-`L` nomenclator (Heading 2 addressee). |
| 33 | L17 | `[82]` | `82` | `[82]` | Open nomenclator: place or source from which news arrived (`De [82] venero nove`). |
| 34 | L17 | `[27]` | `.27.` | `[27]` | Open numeric group between `la` and `fior` (same code as L04; candidate null). |
| 35 | L18 | `{L2?}` | `{L2}` | `{L2}` | Open underlined-`L` nomenclator (destination of troops: `erano passati al {L2?}`). |
| 36 | L19 | `[alli]` | `&lli` | `llp` | Scribal slip: `&lli` (`llp`) for `4&lx` (*alli* / *delli*). |
| 37 | L19 | `[?si]` | `fix` | `ni` | Contextual/uncertain: `fi·x` decodes as `ni`; exact wording of Hesdin's surrender is less secure. |
| 38 | L19 | `[?è]` | `ri,` | `s,` | Contextual/uncertain: comma-separated prefix of `ri,érri4` (`s,resa` / *s'è resa*). |
| 39 | L19 | `[resa]` | `érri4` | `\|reel/resa\|` | Paired with preceding `ri,` in `ri,érri4` (`s,|reel/resa|`). |
| 40 | L21 | `[?raccomandatione]` | `e4,s.{ar}` | `[e4,s.{ar}]` | Open abbreviated cipher token after `⟨domandando alcune lre⟩ de`. |
| 41 | L21 | `{L30?}` | `{L30}` | `{L30}` | Open underlined-`L` nomenclator (same referent as L04 and L27). |
| 42 | L22 | `[53]` | `53` | `[53]` | Open two-digit code (same code as L06; candidate function word *non*). |
| 43 | L23 | `[?parte]` | `fi4ésir` | `\|narte/slrte\|` | Contextual/uncertain: `fi` (`n`) written where *parte* needs `li` (`p`). |
| 44 | L23 | `[essendo]` | `rigrfiigi` | `stenss[i]` | Scribal slip: missing `c` in `rigrfi[ic]gi` (*essendo*). |
| 45 | L27 | `{L30?}` | `{L30}` | `{L30}` | Open underlined-`L` nomenclator (subject of closing paragraph). |
| 46 | L27 | `[peggiore]` | `tirizxbér` | `\|ueggiore/usuiore\|` | Scribal slip: initial `t` written for `l` (`lirizxbér` = *peggiore*). |
| 47 | L27 | `[posse]` | `tibigir` | `uoss[i]e` | Scribal slip: initial `t` for `l` and stray `i` (`libigir` = *posse*). |
| 48 | L28 | `[ultimo]` | `tiusixdigi` | `uhtimo` | Rare allograph/slip: `u` (`h` elsewhere) stands for `l` in *ultimo*. |
