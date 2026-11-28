# Hole audit and apparatus for c. 78r (`reading_78r.md`)

Every departure of `reading_78r.md` from the unedited mechanical witness decryption (`decryption_78r.txt`, generated strictly from `key_mdp384_witness.tsv` applied to `transcription_78r.txt`) is counted as a hole under the repository's cipher-words-only rule (16 Nov 2026) and sure-words-only rule (19 Nov 2026). Because `key_mdp384_witness.tsv` is rebuilt from sibling decipherments (`c. 76r/79r`, `c. 77r`, `c. 147r/148r`) rather than a surviving archival key sheet, the one-digit-slip exemption (14 Nov 2026) does not apply.

## Summary counts (`word_audit_78r.py` & `v10_relabel.py`)

| Metric | Sure / Mapped | Holes / Unmapped | Total | Share |
|---|---:|---:|---:|---:|
| **Official Cyphersolver cipher-word share (`v10_relabel` / `v2_score`, `clear_markup=⟨⟩`)** | **251** | **107** | **358** | **70.1% (`0.701`)** |
| Orthographic cipher words (apostrophe contractions = 1 word; clear spans excluded) | 240 | 107 | 347 | 69.2% (`0.692`) |
| Sensitivity: if recurring `c. 78r`-only homophones (`key_78r_extensions.tsv`, 18 words) were counted | 269 | 89 | 358 | 75.1% (`0.751`) |
| Witness-key cipher token coverage (`decryption_78r.txt`) | 1,288 | 49 | 1,337 | 96.3% (`0.963`) |

**Classification verdict:** Strict `read_share = 0.701` (and `0.751` even with target-inferred homophones) is decisively below `0.95`. Under Cyphersolver extent rules (95% of cipher words giving sense), `c. 78r` has **partial** extent (`profile.json` state `read in part`), comparable to `c. 76r` (`0.790`, partial) and `augustoni1612` (`0.726`, partial).

## Breakdown of the 107 holes by class

1. **Unresolved codes, literal numerals, and delimiter spans (15):**
   - `L01`: `[76]` (`7^6^`, sender title), `[47]` (`4^7`, recipient code), `[84]` (`84̂`, place of writing), `[22]` (`22̄`, barred literal calendar day), `[1547]` (plain Arabic year parsed as `15 47 = uf` by the mechanical key), `[65]` (`6 5` at line end, visually `65` or `67`).
   - `L02`: `[61]` (`61̄`, barred calendar day, possibly scribal transposition for `16`).
   - `L03`: `[18]` (`18̂`, lobbying target, historically Venice/Signoria).
   - `L05`: `[...]` ×2 flanking witness `Signor` (`70 6^7 70 03 9` = `i Signor ila`, likely Doge / Signoria).
   - `L10`, `L12`: standalone `[55]` before `Sua Santità` and `richiesta` (possibly abbreviated `p[oi]` / `p[er]`).
   - `L17`: `[...]` (`[71:NULL] ah[58]au` clause break / unread group).
   - `L19`: `[87]` (`8^7` before `de Riens`, ecclesiastical title for Charles de Guise, kept distinct from witness `8^9 = Vescovo` on `L25`).
   - `L21`: `[80]` (`8^ 0^7`, topic/clause delimiter before `11 = Sua Santità`).

2. **Contextual / historical hypotheses unattested in sibling witnesses (22):**
   - `L01`: `[?le]`, `[?letere]` (`o[36]fere`), `[?Ambasciatore]` (`9^2`, adjacent to witness `9^3 = Ambasciatore`).
   - `L03`: `[?una]` (`20 59`), `[?Svizzeri]` (`41̄`, strong historical match via Della Casa Letter 333, 9 July 1547), `[?principe]` (`4^3`, adjacent to witness `4^2 = Principe`).
   - `L08`: `[?ancora]` (`1^9`), `[?questo]` (undotted `16` for `1^6`).
   - `L09`: `[?di]`, `[?loro]` (`52 70 09 8 00 8`), `[?il]` (`2^2`).
   - `L15`: `[?buono]` (`u[08]no`), `[?app]reso` (`[58]reso`).
   - `L16–L17` (disputed passage flagged in `independent_check/VALIDATION.md`): `[?dal]`, `[?Dominio]` (literal `dandomino`), `[?darmene]` (`[59]melte`), `[?del]` (`[16]l`), `[?di]` (scan shows `11 70 6 04 8 = Sua Santita ieso`, not `51 70`), `[?che]`, `[?il]` (`10 20 03 = bhl`).
   - `L22`: `[?di]` (preceded by uncancelled scribal false-start `0` before caret `{^51}`).
   - `L27`: `[?questi]` (undotted `16` for `1^6`).

3. **Recurring target-inferred `c. 78r` homophones and ligatures (`key_78r_extensions.tsv`, 18):**
   - `20 = i` (10 words whose sole departure is `20=i`, visually verified as `20` on the scan alongside witness `20=h`): `[di]` (L04), `[ringratia]` (L05), `[in]` (L08, L27), `[protonotario]` (L09), `[oferischi]` (L14, twice), `[egli]` (L16), `[ragionamento]` (L16), `[il]` (L20 barred `2̄0`, L26). (Two further words, `[audientie]` L23 and `[dandino]` L26–L27, also carry a second slip and are counted under category 4.)
   - `55 = p` (2 words solely affected): `[saprà]` (L13), `[sopratutto]` (L15). (`[tempo]` L08 also has ambiguous final `6/2` and is counted under category 4.)
   - `36 = pe` (2 words solely affected): `[per]` (L17), `[per]` (L24). (`[per]` L26 also has an extra `9` before `36`.)
   - `08 = l` (`[collegarsi]` L08), `00 = o` (`[procinto]` L04), `57 = d` (`n'[andrà]` L10), `30 = s` (`[estensione]` L19) (4 words; `10 + 2 + 2 + 4 = 18`).

4. **Model-settled scan amendments, scribal / enciphering / blind-transcription slips, and remaining disputed forms (52):**
   - `L01` `d[i]` (`71=NULL` for `70=i`), `lugli[o]` (omitted `8` before `1547`); `L02` `d[e']` (split around `61̄`), `[d]al` (`52=g` for `51=d`); `L03` `sole[citar]e` (`10=b`, `02=u`), `fa[r]` (`10=b`); `L04` `inten[des]e` (`03=l`, `05=n`); `L05` `d[a]` (omitted `9`); `L06` `parti[cular]e` (`10=b` ×2), `[ch]e` (undotted `10`); `L07` `d'alcun[o]` (`6=e` for `8=o`); `L08` `sarien[o]` (`6=e` for `8=o`), `tem[p]o` (`55=p`, final `6/2`), `man[t]ener` (`47=f` for `45=t`); `L10` **`[ferrara]` (`68̄`, amended by AI model on enlarged scan from initial blind `6̄`, counted as probable until human-checked)**, `tu[t]o` (`49` for `45`); `L11` `con[f]orme` (`32=i` for `31=f`), `in[t]entione` (`47=f` for `45=t`), `[d]i` (`52=g` for `51=d`); `L12` `rich[i]esta` (`10=b`), `most[r]i` (`02=u` for `01=r`); `L13` **`[quelle]` (`1^3 1^7 6 = con quello e`: choosing attested variant `quelle` still leaves the extra `6=e` unaccounted for, likely scribal repetition of final `-e` after `1^7`)**, `afet[uo]se` (`6=e` for `8=o`), `[f]are` (`32=i` for `31=f`); `L14` `[p]articularmente` (`13` for `14`), `prontamen[t]e` (`05=n` for `45=t`); `L15` `ogn[i]` (`09`), `ofiti[o]` (`29`), `[penetra]re` (`59`, `09`), `[ch]e` (undotted `10`); `L16` `[p]orta` (`13` for `14`); `L17` `rit[rat]to` (`09`), `es[s]o` (`11 70 6 04 8 = Sua Santita ieso`, see L16–L17 table below), `de[l]` (`05=n`), `Dan[d]ino` (`52=g` for `51=d`); `L18` `Pro[tono]tario` (`47=f`, `6=e`), `[t]entare` (`47=f` for `45=t`); `L19` `cardina[l]ato` (`0̄9`); `L20` `[con]ferire` (`2^3=t` for `1^3=con`), `[mon]asterii` (`37=n`, `01=r`), `priorat[i]` (`10=b`); `L22` `[te]nerla` (uncancelled false-start `0` before `{^51}` shifts `05 17 04 56`); `L23` `aud[ienti]e` (`20=i`, `10=b`), `[con]to` (barred `1̄3`); `L24` `[con]servarla` (`2^3=t` for `1^3=con`); `L25` `[di]` (ms. `01 70 = ri Ceneda`), `vi[s]itare` (ms. `07 = uiditare`); `L26` `[pe]r` (`a[36]r`), `[di]` (ms. `del Sua Santità`), `se[g]uitando` (`18^=qui`), `Dand[ino]` (`20=i`, `[30]`); `L27` `sti[a]` (omitted `9`).

## Figure-by-figure alignment of disputed passage L16–L17

Because L16–L17 contain dense scribal/transcription departures, every group from `L16` `07` through `L17` `2^4` is aligned explicitly below (`transcription_78r.txt` → `key_mdp384_witness.tsv` → editorial reading in `reading_78r.md`, where all uncertain/departing words are bracketed as holes):

| Line | Original figures | Witness-key decode | Reading in `reading_78r.md` | Reason / status |
|---|---|---|---|---|
| L16 | `6 52 03 20` | `e g l h` | `[egli]` | Target-inferred `20=i` (`key_78r_extensions.tsv`); hole |
| L16 | `13 8 01 45 9` | `[13] o r t a` | `[porta]` | `13` vs. witness `14=p` (1-digit slip/confusion); hole |
| L16 | `07 9 05 51 8 17 70 05 8` | `d a n d o m i n o` | `[?dal] [?Dominio]` | Contextual proposal assuming `05=n` for `03=l` (`dal domino` = Signoria of Venice); disputed, both bracketed as holes |
| L16 | `24 59 17 6 03 45 6` | `et [59] m e l t e` | `et [?darmene]` | Witness `24=et` is sure; `[59]melte` does not spell *darmene* literally (requires `59→da r`, `03→n`, `45→n`); contextual hypothesis, hole |
| L16 | `13^ 45 8` | `con t o` | `conto` | Witness `1^3=con` (dot shifted right over `3`), `45=t`, `8=o`; sure |
| L16 | `16 03` | `[16] l` | `[?del]` | Unmarked `16` (`1^6=questo`) + `l`; contextual hypothesis, hole |
| L16 | `01 9 52 20 8 05 9 17 6 05 45 8` | `r a g h o n a m e n t o` | `[ragionamento]` | Target-inferred `20=i`; hole |
| L16 | `1^0 20 9 01 9 04 6 50 8 40 51 6 03` | `che h a r a s e c o e d e l` | `che harà seco e del` | Witness key verbatim; all sure |
| L17 | `01 70 45 09 45 8` | `r i t [09] t o` | `[ritratto]` | Unattested `09` in middle of *ritratto*; hole |
| L17 | `11 70 6 04 8` | `Sua Santita i e s o` | `[?di] [esso]` | Scan shows `11 70 6 04 8` (not `51 70 6 04 04 8`); `11` for `51=d` is a sharp visual departure, and `ieso` has single `04=s` + extra `70=i` (or `di esso` with `11→51` and single `s`); both `[?di]` and `[esso]` remain bracketed as holes |
| L17 | `71 9 20 58 9 15` | `[71:NULL] a h [58] a u` | `[...]` | Unread clause-break span; hole |
| L17 | `36 01 03 6 45 6 01 6` | `[36] r l e t e r e` | `[per] letere` | Target-inferred `36=pe` (`[per]` = hole); `letere` verbatim |
| L17 | `51 6 05 51 9 05 52 70 05 8` | `d e n d a n g i n o` | `[del] [dandino]` | `05=n` for `03=l` (`del`) and `52=g` for `51=d` (`dandino`); both holes |
| L17 | `04 70 9 17 8 9 02 70 04 9 45 70` | `s i a m o a u i s a t i` | `siamo avisati` | Witness key verbatim; both sure |
| L17 | `10 20 03 2^4` | `b h l detto` | `[?che] [?il] detto` | `10` (undotted `1^0=che`) + `20=i` + `03=l`; `[?che]` and `[?il]` bracketed as holes; `2^4=detto` verbatim |

## Excluded inline clear Italian passages (`⟨...⟩`)

- **Header:** `Copia. / D'una littera del Card.le Farnese`
- **L09:** `et perch[é] s'intend[e/a] [che]` — adopted in `reading_78r.md` because the looped `ch[e]` ligature matches `L23` (`manco fastidio ch[e] si potrà`); **competing paleographic expansion preserved:** an earlier reading expanded the final abbreviated monogram as `S[ua] S[antità]` (`et p[er] S. S[antità]` / `et perch[é] s'intend[e] [SS]`), and the subjunctive `s'intend[a]` vs. indicative `s'intend[e]` remains open on the manuscript abbreviation.
- **L23:** `et darli manco fastidio ch[e] si potrà`
- **L24:** `a b[e]n[e]fitio publico, et consolation' n[ost]ra` (earlier proposal `mia` rejected in favor of `n[ost]ra`)
