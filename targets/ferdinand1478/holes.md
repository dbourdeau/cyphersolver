# Hole Ledger & Word-Sense Audit — Zaragoza AHPZ C_CRAR/000001/0024 (Cat. 2854)

Every bracketed token (`[word]`, `[?word]`, `{oo?}`) in `reading_2854.md` is counted as an explicit hole by `word_audit.py` and `research/reading_audit/v10_relabel.py` (`clear_markup=⟨⟩`), following Cyphersolver's "Only sure words count" convention (every word departing from the literal witness-key output, settled by an AI model on the image, or inferred from `#2854` alone without witness attestation counts as a hole on the 95% threshold).

## Summary Totals (Cipher Words Only, Clear Framing Excluded)

- **Sure cipher words (verbatim from witness-attested/grid entries in `decryption_2854.txt`):** **656** (of 770 cipher words)
- **Explicit holes:** **114**
  - **Open nomenclator (`{oo?}`):** **1** (`L40`, sole unmapped token out of 1,915 = `0.05%`)
  - **Uncertain corrupt / extraneous / ink-smudged spans (`[?fiyees]`, `[?nebe]`, `[?be]`, `[?uuestra] [?alteza]`):** **5** (`L11–L12`, `L41`, `L60`, and 2 smudged words at `L61`)
  - **Model-settled scan amendments (`L03 [supiera]`, `L45 [uuestra] [alteza]`, `L62 [seruicio]`):** **4**
  - **Codes inferred from `#2854` alone (`fa`, `fi`, `fo`, `96`, `99`):** **15** (`[quanto]` `3×`, `[qual]` `2×`, `[quel]`/`[aquel]` `2×`, `[cerdenya]` `4×`, `[francia]` `4×`)
  - **Target-only Grade-3 singleton inferences without witness gloss (`b_dot=f`, `d_bar_dot=m` + `3=be`, `b_a=e`):** **3** (`L04 [cifra]`, `L11 [embexador]`, `L11 [hermana]`)
  - **Scribal encipherment slips, omissions, or secondary polyvalent values (`[word]`):** **86** (`18 + 10 + 8 + 50`)
- **Strict `v10_relabel` `read_share`:** **`0.852` (`85.2%`, `656/770`)** -> classified **`read in part`**, with **`outcome.key = "partial"`** and **`outcome.method = "read from existing decipherment"`**.

*(Note on `95 = Sicilia` in `CRAR_22`: `95 = Sicilia` on `L38, L39, L41` (`3×`) is attested in the contemporary interlinear decipherment of sibling `AHPZ C_CRAR/000001/0022` (`L02, L06, L19`); note that the `94 -> 95` digit check on `CRAR_22` was inspected on enlarged crops by AI models only, not by a human palaeographer.)*

## Breakdown of All 114 Explicit Holes by Category

### 1. Sole Unresolved Nomenclator (`1` word)
- `L40`: `{oo?}` (`oo`, 1 token): *"so color de los fechos de `[cerdenya]`, mandarle uenir a `{oo?}` que fazerle boluer a Sicilia"* — kept open (García Larragan reads *aquí*).

### 2. Uncertain Short Corrupt, Extraneous, or Ink-Smudged Spans (`5` words)
- `L11–L12`: `[?fiyees]` (`25 74 p_bar` = `fi ye es`) between *"la [reyna] mi [hermana]"* and *"dixe"*.
- `L41`: `[?nebe]` (`34 4` = `ne be`) in *"Y en `[?nebe]` la uenida al del `[castellano]`"*.
- `L60`: `[?be]` (`3` = `be`) extraneous syllable in *"como bien uisto `[?be]` les `[sea]`"*.
- `L61`: `[?uuestra] [?alteza]` (`gi du`? under ink smudge after *determine*; García Larragan reads *lo que*).

### 3. Model-Settled Scan Amendments (`4` words)
- `L03`: `[supiera]` (`45=pi`, amended by AI model on enlarged crop from initial `44`).
- `L45`: `[uuestra]` `[alteza]` (`gi`, amended by AI model on enlarged crop from initial `91`).
- `L62`: `[seruicio]` (`10=ci`, amended by AI model on enlarged crop from initial `20`).

### 4. Codes Inferred from `#2854` Alone (`15` words)
- `fa = quanto` (`3` words): `L10` `[quanto]`, `L33` `[quanto]`, `L36` `[quanto]` (García Larragan reads *carta*).
- `fi = qual` (`2` words): `L33` `[qual]`, `L49` `[qual]`.
- `fo = quel` (`2` words): `L44` `[quel]`, `L54` `[aquel]` (`q_bar fo`).
- `96 = Cerdenya` (`4` words): `L39` `[cerdenya]`, `L40` `[cerdenya]`, `L45` `[cerdenya]`, `L46` `[cerdenya]` (note `L38 Cerdenya` is spelled syllabically `9 gt_dot 14 e_tail B` from witnessed signs and stays unbracketed).
- `99 = Francia` (`4` words): `L13` `[francia]`, `L16` `[francia]`, `L25` `[francia]`, `L29` `[francia]`.

### 5. Systematic `e_dot` (`= o`) Written for `e_tail` (`= n`) (`18` words)
- `L02` `[ferrando]` (`ferraodo`), `L02` `[rossellon]` (`rosselloo`), `L08` `[non]` (`noo`), `L14` `[rossellon]` (`rosselloo`), `L16` `[pretende]` (`pretieode`), `L18` `[rossellon]` (`rosselloo`), `L25` `[non]` (`noo`), `L27` `[inconueniente]` (`incooueniente`), `L32` `[sin]` (`sio`), `L33` `[enpachar]` (`eopachar`), `L37` `[mandado]` (`maodado`), `L39` `[negociacion]` (`negociacioo`), `L41` `[castellano]` (`castellao`), `L49` `[bien]` (`bieo`), `L50` `[casamiento]` (`casamieoto`), `L54` `[excellente]` (`excelleote`), `L58` `[presuncion]` (`presuocioo`) & `[quieran]` (`quierao`).

### 6. Secondary Polyvalent Values of Witnessed Signs (`10` words)
- `4` (`be` primary, `u/v` secondary in `CRAR_22`): `L01` `[screuir]` (`screbeir`), `L03` `[screui]` (`screbei`), `L05` `[screuir]` (`screbeir`), `L05` `[quiera]` (`qbeiera`), `L26` `[uiniesse]` (`beiniehse`, also `b_dbl=h` for `s`), `L31` `[uoluntat]` (`beoluntat`), `L32` `[uoluntat]` (`beountat`, `l` omitted).
- `d_bar` (`l` primary, `m` secondary in `CRAR_22`): `L43` `[cunple]` (`culple`).
- `b_bar` (`s` in `#2854`, retaining `CRAR_22` `g` once): `L57` `[peligro]` (`pelisro`).
- `gam2` (`rey` primary, extended to `reyna`): `L11` `[reyna]` (`rey`).

### 7. `44` (`pe`) Written for `4`/`L_dot` (`u`/`v`) or `54` (`re`) (`8` words)
- `L30` `[concordaua]` (`concordapea`), `L42` `[ueamos]` (`peeamos`), `L47` `[quiere]` (`qpeiere`), `L47` `[uia]` (`peia`), `L49` `[uisrey]` (`lspeisrey`, with `[al]`), `L49` `[uendra]` (`peendra`), `L56` `[quien]` (`rqpeien`, extra `gt=r`), `L62` `[entendiere]` (`entendiepe`).

### 8. Target-Only Grade-3 Singleton Inferences Without Witness Gloss (`3` words)
- `L04`: `[cifra]` (`10 b_dot 53`, target-only `b_dot=f`).
- `L11`: `[embexador]` (`t_a d_bar_dot 3 63 16 gt_dot`, target-only `d_bar_dot=m` plus `3=be`), `[hermana]` (`b_bar_dot b_a gt 38 33`, target-only `b_a=e`).

### 9. Other Single-Glyph Scribal Slips & Omissions (`50` words)
- `L01`: `[rescebi]` (`rescbei`), `[cifra]` (`cisra` = `10 b 53`, `b=s` for `b_dot=f`).
- `L06`: `[pero]` (`pereyo`, overstruck `gam6`), `[fue]` `[escrito]` (`fuescrito`, single elided `e`), `[de]` (`ge` = `19` for `14`).
- `L07`: `[lo]` (`lu` = `32` for `31`).
- `L09`: `[cumplirse]` (`culolirce`).
- `L10`: `[a]` (`ce` = `9` for `q_bar/93`).
- `L11`: `[di]` `[a]` (`ce` = `9` for `di a`).
- `L12`: `[plazia]` (`olaesa`).
- `L13`: `[concordia]` (`concordice`), `[los]` `[dichos]` `[condados]` (`eldichodados`).
- `L14`: `[con]` `[dos]` (omitted before `condiciones`).
- `L15`: `[se]` (`sa` = `48` for `49`).
- `L17`: `[sabida]` (`saberbida`).
- `L20`: `[aueriguada]` (`apesriguceda`).
- `L21`: `[aquesto]` (`aquesti` = `60` for `61`).
- `L23`: `[trabajaria]` (`trabeiceria`).
- `L25`: `[de]` (omitted in `hauia [de] dexar`), `[saluo]` (`saldeo` = `14` for `4`).
- `L26`: `[parece]` (`sarece` = `48` for `43`).
- `L27`: `[deuerle]` (`debeeqle`, `g=q` for `gt_dot=r`).
- `L28`: `[sabia]` (`sabice`, `9=ce` for `q_bar=a`).
- `L31`: `[susodicha]` (`susodiha`, `c` omitted under ink blot).
- `L32`: `[sabiduria]` (`sarurea`, `57=ru` telescoping slip for `5 17`).
- `L33`: `[screue]` (`bcreue`, `long_s=b` for `b=s`).
- `L35`: `[quiera]` (`ruiera`, `gt_dot=r` for `g=q`).
- `L36`: `[duda]` (`buda`, `7=bu` for `17=du`), `[seruicio]` (`seruici`, final `o` omitted).
- `L37`: `[de]` (`be` = `4` for `14` in `Conde [de] Cardona`).
- `L42`: `[aprouechar]` (`ceprouechar`, `9=ce` for `q_bar=a`).
- `L44`: `[en]` (`tn` = `b_tail e_tail`).
- `L46`: `[como]` (`cbo` = `B_bar 6`), `[fiziessen]` (`fizi`, ending omitted; alternative `[fizieron]`).
- `L47`: `[si]` (`to` = `61` for `50`).
- `L49`: `[al]` (`a ls` in `alspeisrey`).
- `L52`: `[leonardo]` (`leonardol`, stray `d_bar=l`), `[entonces]` (`entonqs`, `g=q` for `9=ce`).
- `L54–55`: `[sufrir]` (`cusrir`, `b=s` for `f`).
- `L57`: `[consiguiente]` (`cosireyieote`, `gam2=rey` for `22=gu`), `[tengan]` (`tenga`, final `n` omitted before `tanta`).
- `L58–59`: `[de]` `[escusar]` (`descuiar`), `[conciertos]` (`cociertos`, `n` omitted).
- `L60`: `[sea]` (`suo` = `52 e_dot`).
