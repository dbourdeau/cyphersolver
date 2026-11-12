# Nicolò Sadoleto, Ferrarese envoy to Matthias Corvinus, Pozsony 1482 (ASMo Ambasciatori Ungheria b. 1/9)

Status: in progress

**23 Oct 2026, re-read (REREAD_BRIEF batch b22)**: DECODE R1103 and R1106 carry only page images. R1106's contemporary slips 26a (Vestigia 1319) and 26b (Vestigia 4004) transcribed in full as far as the photographs allow (R1106_slips_26a_26b.txt) and a partial reading built on them, following the cipher where its read spans differ (R1106_reading.md, R1106_en.md; b17_score 0.731, explicit holes 0.846). The 26a part (the two p. 2 paragraphs: the Queen, the King of Hungary's moves, the League's spending, Venice) builds sentences; the 26b part (p. 3) keeps holes in most sentences because the right halves of 26b and of p. 3 are faded: still decoded, not read (illegible). R1103 (to King Ferrante, Vestigia 1294) re-cropped line by line: no word beyond 'vostro' accepted (illegible). Log: R1103-R1106_reread_log.md.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **read in part**. R1101's
seven-line block (checked against the clear copy 7a) and R1102's passages A-C (D in part) build Italian sentences.
**R1103 and R1106 are decoded, not read**: R1103 gives one isolated word from the faded block, R1106 only a collation
of a few clauses with the clear witness 26b. About half the cipher lines read (estimated); the earlier 65% is
withdrawn as a reading figure. Two gaps below are not-attempted, hence in progress.

Outcome: read in part (updated 21 Sep 2026; write-up docs/sadoleto1482.html revised). Remaining gaps are image-limited. See `review_20260920.md` for the new
evidence and corrections. R1102 has substantial cipher on the facing manuscript
page 3 beyond the seven-line block previously read. Its opening `ducati` confirms
the currency; a later passage gives an annual payment for six or seven years.
The follow-up `verified_groups.md` verifies literal `dom Francesco` and identifies
X's referent as the Signoria of Venice from an occurrence in R1106 aligned with
contemporary clear witness 26b. Several connective words and further passages
remain unread; the historical results below preserve the earlier investigation.
`cipher_inventory.md` also records an additional R1102 cipher line on page 4
and possible partial interlinear plaintext; no complete separate clear copy
of R1102 has been found.

**Current reading:** `r1102_working_edition.md` consolidates the corrected
R1102 extracts, separating its five cipher-bearing regions and identifying
unread material consistently. `alignment_r1101.md` corrects the earlier
R1101 page reference; `alignment_r1106.md` maps the contemporary slips.

### Current evidence and reading limits

- **R1101:** contemporary witness 7a exists. Original/clear boundaries and
  several local passages agree; whole-letter word-by-word collation is unfinished.
  DECODE I5655 is the final original page, not manuscript page 2.
- **R1102:** literal `dom Francesco` and X's Venetian-government referent are
  verified. The repeated group K in the opening and monetary passages refers
  to the Hungarian king, checked against two R1101/7a passages; see
  `repeated_k.md`. Cipher coverage includes pages 2, 3 and 4. The current edition
  retains all unresolved U labels and uncertain readings. Vestigia's legacy
  note reports decipherments on attached/pasted sheets, but none has yet been
  identified as a separate complete clear witness in the cached images.
- **R1103:** no continuous reading is established. The old fragment proposals
  below remain tentative except isolated `vostro`, now verified against the
  reconstructed alphabet and R1101's `nostro` control. See
  `r1103_image_audit.md`; this does not establish a sentence.
- **R1106:** 26a/26b cover the identified principal cipher regions, but internal
  completeness remains unverified. `r1106_parallel_reading.md` records local
  comparisons and spelling differences, including an omitted triangular sign
  in `anzi`, now verified by the independent R1101/7a z control in
  `z_control.md`.
- **Additional controls:** `june24_control.md` locates the June letter's marginal
  annotation. Its literal correspondence with the cipher is still unproved.
  `published_source_leads.md` distinguishes inspected previews from unavailable
  full texts. `source_cache_audit.md` records the still-unverified DECODE
  attachment access separately from successful full-image access.

The direct comparison of proposed R1102 `offerta`/`effecto` initially supplied
no independent ff control. A subsequent comparison with R1101/7a `affinita`
now establishes ff and supports `offerta` (C), resolving U02. `effecto` remains
M because its following e is not securely separated. See `ff_control.md`.

**Historical record below:** the 19 September conclusions, source table and
open list are preserved as the earlier investigation. Claims there of complete
clear-copy coverage, absence of R1102 decipherment evidence, seven-line-only
R1102 coverage, or still-unresolved `dom`/X are superseded by the current
evidence above. They must not be used as the current outcome summary.

Outcome: read in part (19 Sep 2026). R1102's cipher block read in gist; R1101 and R1106 have contemporary clear
copies on Vestigia (7a; 26a/26b), so were read at the time; R1103's faded block yields fragments only.

Session of 19 September 2026. Target: catalogue entry "Sadoleto (Pozsony) to Ercole I / Ferrante, 4 ciphertexts",
DECODE R1101, R1102, R1103, R1106 ("partially decrypted", graphic signs). Pre-1497: a reading beats the 1497 record.

## Prior art
- Never printed. Magyar diplomácziai emlékek (Nagy & Nyáry 1875–78) skipped Sadoleto's letters; MDE IV p. 77 has one
  passing mention. Mátyus Norbert, "Nicolò Sadoleto követjárása Magyarországon (1482–1483)", *Vestigia* 3 (2020)
  150–163 (https://real.mtak.hu/119767/9/Vestigia3.pdf): the letters "were not copied, so not published"; prints the
  20 June 1482 letter in full and quotes short clear passages of 15 July, 11 Sept, 12 Dec 1482. Nothing on cipher.
- W. Somogyi, *Vestigia* 3, 216–230, n. 25: the letter of 24 June 1482 (Vestigia 1280) has a marginal decipherment.
- Cremonini, *RSU* 16 (2017) n. 39: ASMo Cifrario b. 4 fasc. 1 = a key "per corrispondere con Nicolò Sadoletti a
  Napoli tra 1479 e 1480", reconstructed in the 19th century; unpublished, not digitised. No 1482 key known.
- Tomokiyo (cryptiana): nothing.

## Sources in hand (images git-ignored in `img/`)
DECODE (cookie `targets/bordeaux/decode/cookie.txt`), all 4320×3240 two-page spreads, record JSON in `decode/views.jsonl`:

| DECODE | ASMo b.1/9 no. | Vestigia | date | to | what it is |
|---|---|---|---|---|---|
| R1101 | 7 | 1284 (clear copy **1283 = no. 7a**) | 15 Jul 1482 | Ercole | long cipher passages; 7a is the full contemporary clear copy |
| R1102 | 8 | 1286 | 16 Jul 1482 | Ercole | clear letter, cipher block of 7 lines on p. 2 — **no clear copy** |
| R1103 | 11 | 1294 (copy) | 17 Aug 1482 | Ferrante (copy sent to Ercole with no. 12 = V1296) | clear copy with a 4-line faint cipher block on p. 2 — **no clear copy** |
| R1104 | 13 | 1298 (decipherments **1295 = 13a**, **1297 = 13b**) | 31 Aug 1482 | Ercole | "Decrypted" |
| R1105 | 16 | 1302 | 11 Sep 1482 | Ercole | "Decrypted" |
| R1106 | 26 | 1318 (decipherments **1319 = 26a**, **4004 = 26b**) | 27 Nov 1482 | Ercole | partly cipher; 26a/26b give the clear |

Vestigia record JSONs in `vestigia/`; originals downloaded to `img/v/` (no login).

## The cipher
Monoalphabetic substitution with some homophones, graphic signs, word divisions kept, mixed with clear words.
Working key in `key_working.md`. Confirmed by aligning R1101 p. 2 ll. 1–3 with 7a: "…pigliare questa impresa, et
non lassasse pretermittere questa opportunità laquale mai più fo, né forse sera, e che lo facesse per lo amore…".

## 7a clear copy, p. 3 (Vestigia 1283 image 2, right page), as read
1 che io havea da la M.tà del S. Re Ferdinando su questa, et anche dal S. Conte de …
2 …che per nessuno modo io dovesse domandare questo Re per utilità sua, attento
3 la sua natura, et anche … dove el Florentino voleva che io anche ricordasse
4 per questo …, io non volse, et gli dixi la casone, e lo San(?) de' Francesco, el quale
5 anche fo per parte al ambassata che pregasse la M.tà del S. Re de Hungaria cum ogni
6 … volesse unirse e pigliare questa impresa, e non lassasse pretermittere questa
7 opportunità laquale mai più fo, né forse sera, e che lo facesse per lo amore e
8 benivolentia e per la affinità strectissima che l'ha cum tuta la liga, e per honore e glo[ria]
9 de sua M.tà et abassare una volta Venetiani per modo che l'imparasse de stare
10 fra li suoi fine. Bene è vero che poi neli parlamenti che facemo cul Secretario
11 e quelli altri dove tractavamo de tante gente …, io dixi in bono proposito che an[che]
12 minor gente poteria mo la M.tà sua pigliare de quello de la Sig.ria de Venetia
13 in pocho tempo fino a Treviso inclusive, havendo da la liga tanto contento
14 … e che non doveva credere de' … la costa per modo che …

## Log
- 19 Sep: DECODE metadata for R1100–R1118 fetched; images downloaded (cookie works); Vestigia search "Sadoleto" =
  85 items, found the clear copies 7a, 13a/13b, 26a/26b. Key being built from R1101/7a and R1104/13a.

## Results (19 Sep 2026)
- **Key recovered** (`key_working.md`): a monoalphabetic cipher of graphic signs with a few homophones (e, n, o, r, a),
  word divisions kept, clear words mixed in, "quid" (in clear letters) = "perchè". Verified against 7a on R1101 p. 2
  ll. 1–3 ("pigliare questa impresa, et non lassasse pretermittere questa opportunità laquale mai più fo, né forse
  sera, e che lo facesse per lo amore…") and against 13a on R1104 ("epsa me dice che è certa che la liga non…";
  "perchè Millano et Fiorenza non voriano…").
- **R1101 (15 Jul 1482)**: read at the time; its clear copy is 7a (Vestigia 1283). Not a new reading.
- **R1106 (27 Nov 1482)**: read at the time; decipherments 26a (Vestigia 1319, "Quanto sia per le gratiose…") and
  26b (Vestigia 4004). Not aligned sign by sign here.
- **R1102 (16 Jul 1482)**: no clear copy known; **read in gist** (`reading_r1102.md`): Sadoleto learnt in great secret,
  while leaving Buda for Pozsony, what had been written to Francesco Quirino at court: [the Venetians] wanted Matthias's
  friendship, offered him **Veglia** (Krk, seized by Venice from Count Giovanni Frankopan in 1480), to make his natural
  son ("e bastardo", i.e. János Corvin) captain of their fleet, and to pay him **100,000 [ducats] a year**, the same
  sum Sadoleto says in 13a would buy Matthias's entry into the war for the League. Syntax "como [X] haveva scripto ad Francesco Quirino"; gaps: the informant's title (494),
  the code group 3ί2ии (probably "Venetiani"), a few words in ll. 2–4.
- **R1103 (17 Aug 1482, copy to Ferrante)**: the 4-line block is badly faded; fragments only ("… se tener che … lo
  credo … suoi … vostro … meco … che …"). Better images (UV/multispectral) or the ASMo original would be needed.

## Open
- The informant "da 494 Francesco" and the group 3ί2ии; check against the other Sadoleto letters (nos. 18–28) for
  repeats. Ercole's replies (Minute nos. 1–3, Vestigia 1252/1250/1251) may paraphrase the Venetian offer.
- R1103: Vestigia 1294 is the same Ferrante copy; no second exemplar found. Only better imaging would help.
- The 1479–80 Sadoleto–Naples key (ASMo Cifrario b. 4 fasc. 1, Cremonini n. 39) should be compared with this key.

## Remaining gaps
- R1106 decoded, not read (23 Oct 2026: slips 26a/26b transcribed, partial reading R1106_reading.md; the 26a part holds, the 26b part keeps holes in most sentences) - blocker: illegible; the right halves of 26b and of p. 3 are faded on the only photographs
- R1103 decoded, not read (one word from the faded block; re-cropped 23 Oct 2026, nothing more accepted) - blocker: illegible; see the R1103 line below
- R1102, unresolved U labels, connective words, code 494 and group 3ί2ии - blocker: no-key-material; no clear copy of R1102 found; repeats in nos. 18-28 not yet checked
- R1103, 4-line faded block on p. 2 - blocker: illegible; badly faded, fragments only; UV/multispectral imaging or the ASMo original needed
- R1101, whole-letter word-by-word collation with 7a - blocker: not-attempted; local passages agree; full collation unfinished
- R1106, internal completeness against 26a/26b - blocker: illegible; 26a collated in full (R1106_reading.md), 26b's right half faded

## Escalation
- [x] siblings: DECODE R1100-R1118 metadata and images; Vestigia 85 Sadoleto items; clear copies 7a, 13a/13b, 26a/26b found
- [x] clear-pages: 7a, 13a, 26a/26b aligned; June 24 marginal annotation located; R1102 p. 3/4 cipher found
- [ ] known-keys: not done — the 1479-80 Sadoleto-Naples key (ASMo Cifrario b. 4 fasc. 1, Cremonini n. 39) not compared; not digitised
- [x] print: Vestigia 3 (Mátyus, Somogyi), MDE, Cremonini 2017, Tomokiyo: no decipherment printed
- [x] key-rebuild: key_working.md from 7a/13a; ff and z controls, repeated K, dom/X verified
- [ ] retry: not done — sweep nos. 18-28 for repeats of 494 and 3ί2ии, then rerun R1102's U labels

## R1101 first page against 7a, 12 Nov 2026 (Brice Dudout)

The first original page of R1101 (Vestigia 1284 photograph (103)) had not been read. Its lines 1-8 were transcribed
blind with `key_working.md` and frozen by SHA-256 before any look at 7a; lines 2-8 (79 words, 306 cipher letters,
outside every passage aligned so far) were pre-registered as a held-out portion. One measure against 7a (Vestigia 1283
photograph (101)): character agreement 0.764, word agreement 0.608, all 500 controls lower (random keys max 0.178,
shuffled 7a max 0.295). The criterion (>= 0.85) is not met, so this does not re-validate the key: read blind, a new page
still loses about a quarter of its letters on look-alike signs and uncovered groups. Collated word by word with 7a,
the seven lines read 52 sure, 14 probable, 8 restored and 2 unresolved words of 76 (97.4% by sense): the King's terms,
money from the League for half of 10,000 horse and 10,000 foot for the first year, then a third for two years.
Proposed and not added to the key: a tt sign ("attendere"), a c variant ("dece" twice), a con/cum sign, and a single
group for the royal title. The rest of the letter is still to collate. Files: `dudout/`.
