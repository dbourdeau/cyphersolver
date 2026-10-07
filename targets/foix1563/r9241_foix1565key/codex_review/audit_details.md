# Audit evidence and reproducibility

Verdict: see [review.md](review.md). The short verdict applies to the requested key_final.json, reading_final_raw.txt and align_final.txt. These keys and alignment were unchanged during the run. Parent reading.md changed to v4; its later snapshot is explicitly not the tested key. No v4 conclusions are tested here.

## Sources and scope

- Cipher chart: [S. Tomokiyo, Paul de Foix (1565)](https://cryptiana.web.fc2.com/code/henryiii.htm#Foix0), read directly from supplied CharlesIX_Foix.png and henryiii_utf8.htm. The enlarged image is key_enlarged.png. The page identifies letters dated 11 October 1565, BnF fr.15971 ff.21 and 26. It does not establish this 1563 letter’s complete reading or novelty.
- Independent corpus: [Montaigne, Essais, Livre I, Wikisource](https://fr.wikisource.org/wiki/Essais/Livre_I/Texte_entier), retrieved with the web tool. Shell networking failed; the saved web extracts are montaigne_web_0.txt through montaigne_web_14.txt. These are sampled excerpts, not a claim to have downloaded the complete volume. Extraction deduplicates by source line and retains paragraphs longer than 90 characters; this reduces standalone verse/navigation but does not eliminate every embedded Latin quotation.
- Corpus: 873 retained paragraphs, 215,668 training letters; 55,981 reference letters held out by every fifth paragraph. Long s, ligatures, accents and nasal abbreviations normalized; j/y→i, v/w→u. No Catherine text used to train the independent model or dictionary.
- Dictionary: 2,118 Montaigne words of length 4–14, frequency ≥3. Maximum nonoverlapping character coverage, allowing unmatched characters. The dictionary uses all Montaigne extracts, including reference paragraphs. Thus reference coverage is a contextual comparator, not an independently held-out dictionary assessment. Coverage is neither grammaticality nor transcription accuracy.
- Supplied transcription, provenance notes, and code were inspected; the original 1563 manuscript itself was not independently examined. The correspondence between manuscript glyphs and token names remains conditional on that transcription. Metadata/date/novelty are not independently authenticated by this statistical review.

## Independent implementation

prepare.py builds conditional Witten–Bell character probabilities of orders 1–5 directly from Montaigne counts. audit.cpp implements decoding, shuffles and fitting. It imports no claimant code. analyze.py independently computes coverage, inventories, candidate-path products and minimum edit distances. reproduce.py separately reads the old probability table only as data to check the historical statistic.

The new beam has width 48; each token uses exactly the specified candidate list. Unmapped final-key signs have all 22 letters available independently at each occurrence, each with prior −0.7; listed alternatives use prior −0.15×index, as in the claimant’s model. Nulls emit no letters. The same priors, candidate sizes, word signs and beam apply to real and token-order-shuffled inputs. Independent optimization uses order 5, not the claimant’s order 6. Reported scores exclude priors and are mean log10 probability per emitted letter, including lower-order starts. Histories reset at each passage.

The alphabet-size assertion initially caught a development typo before any scores were produced; it was corrected and all reported runs completed. Independent Python/C++ agreement on the real singleton baseline: {'python_score': -1.5820079923796897, 'cpp_score': -1.58201, 'difference': 2.0076203102181722e-06}.

## Published-key transcription and uncertainty

published_key.json contains the reviewer’s visual transcription, not a fit to this letter. The singleton baseline uses the first value of each ambiguous glyph domain; published_poly is a sensitivity test allowing the chart’s potentially confusable forms. The values read by letter group are:

```text
a: ^ D       e: a b 3       c: 4 7 Dl
d: x g X     f: N (x/X ambiguous with d)
g: 4t        h: k          i: # 2 e
l: f         m: r          n: m B
o: n d       p: tb z       r: p
s: Z3 ff sz  t: th Bs (3/B ambiguous with e/n)
u: c (f ambiguous with l)
et: E3       faire: hb
6=je 8=luy 10=dict? 26=bien 30=est 31=pour 32=par
34=tant 35=il 36=puis 37=me 39=sieur 40=faict
50=que 12=quil 70=toute 83=le 84=la 17=veult
```

The reviewer leaves graphic matches such as H, T2, Yb, Rx, qf, qs and others unresolved instead of learning them from the target. Plain versus crossed x/X is especially uncertain; including both d/f is a sensitivity domain, not proof of intentional polyphony. This is a conservative *subset* of the chart: 51 observed types / 826 occurrences mapped, including four clear-word types explicitly assumed null; 205 occurrences unmapped. No claim is made to have independently reconstructed every graphic alias. The claimant’s wider seed is tested separately using AST literal extraction, never execution. Its independent-corpus result is 8.89 SD above token shuffles.

The baseline skips unknown glyphs, reproducing the claimant’s treatment; the barrier sensitivity instead resets history and prohibits dictionary matches across each unknown. Both retain strong token-order signals. Dropping the repeated two-token catchword is a prespecified supplied assumption. Tokens after this deletion: 1,031, divided 515/205/99/212, with 93 types. The older NOTES.md counts describe older transcription states.

## Randomization tests

Seeds: C++ mt19937(20261004), frequency test Python Random(9241), old-metric reproduction Random(7). Each row below has 200 independent permutations. SD is population SD; z is descriptive standardization, not a validated Gaussian tail. p=(1+number ≥ real)/(201). No multiple-search/key-selection correction is claimed.

| Key / shuffle | Real score | Control mean ± SD | z | p | Coverage real / mean / max |
|---|---:|---:|---:|---:|---:|
| published_single_order | -1.58201 | -1.89393 ± 0.02913 | 10.71 | 0.0050 | 0.169 / 0.097 / 0.127 |
| published_single_barrier_order | -1.28520 | -1.57969 ± 0.02713 | 10.85 | 0.0050 | 0.154 / 0.083 / 0.110 |
| published_single_identity | -1.58201 | -1.53043 ± 0.19104 | -0.27 | 0.6368 | 0.169 / 0.362 / 0.697 |
| published_poly_order | -1.48813 | -1.80997 ± 0.03005 | 10.71 | 0.0050 | 0.212 / 0.107 / 0.141 |
| published_poly_barrier_order | -1.21750 | -1.52204 ± 0.02744 | 11.10 | 0.0050 | 0.189 / 0.089 / 0.119 |
| published_poly_identity | -1.48813 | -1.46832 ± 0.18090 | -0.11 | 0.5473 | 0.212 / 0.395 / 0.701 |
| claimant_seed_order | -1.58527 | -1.88300 ± 0.03347 | 8.89 | 0.0050 | 0.154 / 0.096 / 0.129 |
| claimant_seed_barrier_order | -1.34995 | -1.64737 ± 0.02891 | 10.29 | 0.0050 | 0.145 / 0.084 / 0.112 |
| claimant_seed_identity | -1.58527 | -1.52328 ± 0.18576 | -0.33 | 0.6418 | 0.154 / 0.389 / 0.676 |
| final_order | -0.98252 | -1.64907 ± 0.02688 | 24.80 | 0.0050 | 0.375 / 0.118 / 0.162 |
| final_identity | -0.98252 | -1.21249 ± 0.13686 | 1.68 | 0.0498 | 0.375 / 0.365 / 0.577 |
| published_single_stratified_identity | -1.58201 | -2.09479 ± 0.11809 | 4.34 | 0.0050 | 0.169 / 0.088 / 0.124 |
| published_poly_stratified_identity | -1.48813 | -2.02392 ± 0.12165 | 4.40 | 0.0050 | 0.212 / 0.091 / 0.127 |
| claimant_seed_stratified_identity | -1.58527 | -2.00473 ± 0.10257 | 4.09 | 0.0050 | 0.154 / 0.087 / 0.121 |
| final_stratified_identity | -0.98252 | -1.81622 ± 0.10757 | 7.75 | 0.0050 | 0.375 / 0.105 / 0.155 |
| published_single_numbers_identity | -1.58201 | -1.57107 ± 0.01544 | -0.71 | 0.7512 | 0.169 / 0.197 / 0.246 |
| final_numbers_identity | -0.98252 | -0.99286 ± 0.00807 | 1.28 | 0.0846 | 0.375 / 0.390 / 0.428 |

Order shuffles pool all tokens then restore original passage lengths: the exact multiset of candidate lists and occurrence counts is preserved. Full identity shuffles permute all sign types, including word signs/nulls/unknowns; they can give frequent signs whole-word outputs and alter output length substantially. These are deliberately broad sensitivity controls, not a calibrated substitute for type-preserving controls. Their unexpectedly high coverage illustrates the metric’s susceptibility to recycled word signs.

Stratified identity shuffles permute only letter-sign identities within equal candidate-list cardinalities; word signs, null-bearing signs and unknown signs remain in place. They preserve the numbers of one-/two-/three-/four-way letter choices at the occurrence level. Numeric-meaning shuffles permute the 14 observed, published numeric word-sign values, holding all other mappings fixed. Their weak result does not disprove the numerical key: corrupted letter contexts and a letter-only LM may have little power to distinguish these word assignments.

The final-key order controls give EXACTLY the same per-occurrence freedom to random ciphertext as to the real text. They do not recreate selection of the final candidate domains on the real target; therefore the large final-key gap is conditional evidence, not a post-selection significance claim.

## Reproduction of the old metric

```json
{
  "real": -1.5174622535705566,
  "n30": {
    "mean": -1.7506669481595358,
    "sd": 0.03144657912762223,
    "z": 7.415900268278641
  },
  "n200": {
    "mean": -1.759443275332451,
    "sd": 0.031000429153893932,
    "z": 7.805731351673862,
    "max": -1.6821805238723755,
    "p": 0.004975124378109453
  }
}
```

The 7.5-SD description is approximately correct. The old statistic is conditional on the chosen transcription, key aliasing, null assumptions, corpus, model and unknown deletion. With 200 permutations, zero exceedances cannot justify the tiny Gaussian p-value sometimes implied by “7.5 sigma.”

## Held-out key fitting

Training uses only the designated passages plus the chart. Fixed words and clear nulls stay fixed; all other signs receive one globally consistent letter. Unknowns start as e, published signs at their first chart value; a second restart randomizes observed free letter assignments. Six coordinate-ascent sweeps maximum, 22 candidate letters per sign. Select the better training score of the two restarts. Untouched test-only unknowns retain the default; no test score selects parameters or restarts. Same procedure for 30 order-shuffled controls in each direction. This intentionally avoids importing the full-text-fitted final candidate domains. It tests a deterministic adjustment family, not every possible polyphonic optimization, and local optimization can fail.

| Training → test | Test before | Training fitted | Test fitted | Control test mean ± SD | Test p | Test word coverage / control |
|---|---:|---:|---:|---:|---:|---:|
| (1)+(2) → (3)+(4) | -1.62549 | -1.08672 | -1.25866 | -1.58081 ± 0.04366 | 0.0323 | 0.192 / 0.118 |
| (3)+(4) → (1)+(2) | -1.56051 | -1.02399 | -1.61228 | -1.61120 ± 0.03511 | 0.5484 | 0.078 / 0.115 |

Forward transfer survives on LM score, while independent dictionary coverage is only weakly separated (p=0.0968). Reverse transfer fails (LM p=0.5484; coverage p=1.0). The short training half has only 311 tokens versus 720 in the other direction. Failure is a limitation of this validation/optimizer, not a proof that the underlying cipher is wrong. Because the supplied transcription and historical key identification were already selected using the whole artifact, these are conditional cross-validation tests, not a genuinely untouched prospective specimen.

## Freedom, phrases and leakage

Final domains: 11 multi-valued types / 185 occurrences; 19 unmapped types / 26 unrestricted occurrences. Product of per-occurrence domain sizes is 10^112.059017. This counts candidate paths, not necessarily distinct strings and not independent fitted parameters. It is not by itself a proof of overfitting.

```json
{
  "tokens": 1031,
  "types": 93,
  "unknown_types": 19,
  "unknown_occurrences": 26,
  "multi_types": 11,
  "multi_occurrences": 185,
  "log10_paths": 112.0590170869461,
  "unknown": {
    "i6": 2,
    "pl": 1,
    "Ld": 1,
    "zo": 1,
    "c'": 1,
    "93": 3,
    "80": 3,
    "qs^o": 1,
    "O": 1,
    "82": 1,
    "m+": 1,
    "Lc": 1,
    "ae": 1,
    "M": 1,
    "51": 1,
    "Ax": 2,
    "zt": 2,
    "t7x": 1,
    "zf": 1
  },
  "multi": {
    "Z3": {
      "n": 21,
      "values": [
        "e",
        "s"
      ]
    },
    "tb": {
      "n": 28,
      "values": [
        "p",
        "h"
      ]
    },
    "X": {
      "n": 17,
      "values": [
        "s",
        "d",
        "u"
      ]
    },
    "f": {
      "n": 18,
      "values": [
        "l",
        "u"
      ]
    },
    "so": {
      "n": 17,
      "values": [
        "e",
        "que",
        ""
      ]
    },
    "3": {
      "n": 52,
      "values": [
        "e",
        "s",
        "t"
      ]
    },
    "2": {
      "n": 9,
      "values": [
        "l",
        "d",
        "r",
        "i"
      ]
    },
    "Da": {
      "n": 2,
      "values": [
        "a",
        "m"
      ]
    },
    "t6": {
      "n": 12,
      "values": [
        "",
        "e",
        "ent",
        "n"
      ]
    },
    "x": {
      "n": 6,
      "values": [
        "f",
        "d"
      ]
    },
    "7x": {
      "n": 3,
      "values": [
        "",
        "s"
      ]
    }
  },
  "omitted_published_tokens": 205
}
```

All four exact normalized full quotations have zero occurrences in the inspected Catherine clean2 corpus and in the extracted Montaigne text. This excludes a direct exact-string hit in those files, not stylistic or n-gram leakage, textual variants, or an undiscovered historical source. The original LM *and* coverage dictionary are explicitly derived from Catherine’s own published letters. Model/dictionary agreement therefore does not constitute two independent validations. The Montaigne replication reduces that circularity.

For each phrase, counts below are candidate paths permitted by key_final.json and the unrestricted-unknown rule, before the LM chooses among them. Minimum edits are ordinary Levenshtein distance to the normalized exact quotation (j/y→i, v→u, accents/spaces removed), over every candidate path. No manuscript-error allowance is silently applied.

### reconciliation necessaire entre ces deux royaulmes

Start token (zero-based): 469. Paths: **38,016**; ambiguous occurrences: 8; minimum exact-quotation edits: **2**.

`p a 7 d m 4 # 2 T2 D th H d m qs b 7 a qf ^ H p b a m th p b 4 ae 3 r 3 Yb ch p d e ^ f m f sz b t6 3`

Token choices (in the same order):

`p={r} a={e} 7={c} d={o} m={n} 4={c} #={i} 2={l|d|r|i} T2={i} D={a} th={t} H={i} d={o} m={n} qs={n} b={e} 7={c} a={e} qf={s} ^={a} H={i} p={r} b={e} a={e} m={n} th={t} p={r} b={e} 4={c} ae={a|b|c|d|e|f|g|h|i|k|l|m|n|o|p|q|r|s|t|u|x|z} 3={e|s|t} r={d} 3={e|s|t} Yb={u} ch={x} p={r} d={o} e={i} ^={a} f={l|u} m={n} f={l|u} sz={m} b={e} t6={NULL|e|ent|n} 3={e|s|t}`

Nearest allowed reading: `reconciliationnecesaireentrecesdeuxroiaunlmes`.

Unfitted reviewer first-value reading (`?` unresolved): `reconcii?at?on?ece?a?reentrec?eme??roialnlse?e`.

### dexterite de son esperit

Start token (zero-based): 560. Paths: **54**; ambiguous occurrences: 4; minimum exact-quotation edits: **0**.

`gy a ch th b p # Bs 3 r b 3 d m a g tb 3 p # th`

Token choices (in the same order):

`gy={d} a={e} ch={x} th={t} b={e} p={r} #={i} Bs={t} 3={e|s|t} r={d} b={e} 3={e|s|t} d={o} m={n} a={e} g={s} tb={p|h} 3={e|s|t} p={r} #={i} th={t}`

Nearest allowed reading: `dexteritedesonesperit`.

Unfitted reviewer first-value reading (`?` unresolved): `?e?teritemeeonedperit`.

### pour le moins estre de la partie

Start token (zero-based): 143. Paths: **1**; ambiguous occurrences: 0; minimum exact-quotation edits: **3**.

`31 83 8 d # m g 30 p a r b 84 32 th e b`

Token choices (in the same order):

`31={pour} 83={le} 8={lui} d={o} #={i} m={n} g={s} 30={est} p={r} a={e} r={d} b={e} 84={la} 32={par} th={t} e={i} b={e}`

Nearest allowed reading: `pourleluioinsestredelapartie`.

Unfitted reviewer first-value reading (`?` unresolved): `pourleluioindestremelapartie`.

### faire son proufit de ce royaulme

Start token (zero-based): 744. Paths: **12**; ambiguous occurrences: 3; minimum exact-quotation edits: **3**.

`hb 3 d m Yx p n c N # 4t a r Z3 7 b p d e ^ Yb m f sz b`

Token choices (in the same order):

`hb={faire} 3={e|s|t} d={o} m={n} Yx={p} p={r} n={o} c={u} N={f} #={i} 4t={g} a={e} r={d} Z3={e|s} 7={c} b={e} p={r} d={o} e={i} ^={a} Yb={u} m={n} f={l|u} sz={m} b={e}`

Nearest allowed reading: `fairesonproufigedeceroiaunlme`.

Unfitted reviewer first-value reading (`?` unresolved): `faireeon?roufigemsceroia?nlse`.

The independent Montaigne whole-text beam recovers `dexteritedesonesperit` exactly and `reconciliationnecesaireentrecesdeux` followed by a corrupt kingdom word. Thus those cores are not solely a Catherine-corpus hallucination, although they still depend on the full-text-fitted key. “Dexterité” uses repeated 3 with different values e/s/e; confirming distinct handwritten shapes is essential. The published chart alone does not supply every fitted value in that phrase.

“Pour le moins…” is not produced even with the final flexibility: its span has only one output, `pourleluioinsestredelapartie`. The claim is an editorial repair of 8=luy to an m-like reading. A different glyph interpretation might justify it, but the reviewed key does not. “Faire son proufit…” similarly requires changing the fixed g at 4t and additional edits. Calling these exact plaintext overstates the evidence; calling every such repair an LM hallucination would also be inaccurate.

## Identification statistics

```json
{
  "top_letters": [
    "e",
    "s",
    "u",
    "i",
    "n",
    "t",
    "a",
    "r",
    "o",
    "l"
  ],
  "top_signs": [
    [
      "b",
      95,
      "e"
    ],
    [
      "m",
      61,
      "n"
    ],
    [
      "d",
      52,
      "o"
    ],
    [
      "3",
      52,
      "e"
    ],
    [
      "p",
      47,
      "r"
    ],
    [
      "th",
      40,
      "t"
    ],
    [
      "a",
      38,
      "e"
    ],
    [
      "r",
      36,
      "m"
    ],
    [
      "#",
      29,
      "i"
    ],
    [
      "tb",
      28,
      "p"
    ]
  ],
  "top10_hits": {
    "n": 20000,
    "mean": 6.4441,
    "sd": 1.2688479774976986,
    "max": 10,
    "min": 2,
    "real": 8,
    "z": 1.2262304291711907,
    "p": 0.2007399630018499
  },
  "numbers": {
    "8": {
      "n": 8,
      "chart": [
        "lui"
      ]
    },
    "30": {
      "n": 6,
      "chart": [
        "est"
      ]
    },
    "31": {
      "n": 2,
      "chart": [
        "pour"
      ]
    },
    "83": {
      "n": 3,
      "chart": [
        "le"
      ]
    },
    "84": {
      "n": 6,
      "chart": [
        "la"
      ]
    },
    "32": {
      "n": 2,
      "chart": [
        "par"
      ]
    },
    "6": {
      "n": 9,
      "chart": [
        "ie"
      ]
    },
    "40": {
      "n": 1,
      "chart": [
        "faict"
      ]
    },
    "93": {
      "n": 3,
      "chart": null
    },
    "80": {
      "n": 3,
      "chart": null
    },
    "82": {
      "n": 1,
      "chart": null
    },
    "34": {
      "n": 2,
      "chart": [
        "tant"
      ]
    },
    "51": {
      "n": 1,
      "chart": null
    },
    "37": {
      "n": 1,
      "chart": [
        "me"
      ]
    },
    "70": {
      "n": 2,
      "chart": [
        "toute"
      ]
    },
    "10": {
      "n": 2,
      "chart": [
        "dict"
      ]
    },
    "26": {
      "n": 1,
      "chart": [
        "bien"
      ]
    },
    "50": {
      "n": 1,
      "chart": [
        "que"
      ]
    }
  },
  "numeric_types": 18,
  "numeric_matches": 14,
  "numeric_occurrences": 54,
  "matched_numeric_occurrences": 46,
  "published_known_types": 51,
  "published_known_occurrences": 826
}
```

The frequency statistic selects the ten most frequent *mapped letter-sign types*, then counts first-value assignments in the Montaigne top ten letters. Randomization permutes the same multiset of values among the 31 mapped observed letter types; the actual complete list is determined in analyze.py. The exact type count is reported below. Result: 8/10, versus random mean 6.4441; one-sided p=0.20074 over 20,000 permutations. This is weak alone. It is not a valid measure to count “frequent-letter hits” without accounting for the many homophones assigned to frequent French letters.

Fourteen of 18 observed numeric-code types are present in the published chart, accounting for 46/54 numeric occurrences. Unmatched: 80, 82, 93 and 51. This inventory resemblance is suggestive but not a calibrated probability: contemporary keys and number allocation conventions would be needed for a defensible historical null. The added word-value permutation test is not significant under this LM. Broader graphic family identification is supported primarily by the unfitted sequence statistics and the source chart, conditional on glyph transcription.

## Specific code and inference weaknesses

1. controls.py assigns *each occurrence* of every unmapped token any of 22 letters. This freedom is omitted from the abbreviated claim. so is not merely a null: its list is e/que/null; t6 is null/e/ent/n.
2. The old beam is optimized on 6-gram total score plus priors, then reported with a 5-gram per-character score; the annealer uses 5-gram mean minus KL divergence and a null penalty. Comparing final −0.920 to refitted −1.33 is not a like-for-like statistic. Supplied controls.txt contains only the 30/12 permutation summaries; it does not contain the claimed −1.33 result. sa_ctrl.py reveals the differing objective.
3. Unfitted decoding silently deletes unknown glyphs, creating artificial adjacencies. Our barrier test preserves the positive signal, but the published method must disclose the deletion.
4. lattice.render and alignlat.py display clear-word nulls as uppercase literal words although norm_val deletes them for scoring. These displays can falsely suggest decoded content.
5. The raw and aligned outputs use different beam widths (48 versus 64), and therefore need not have the same path. Their reported scores differ accordingly. No single frozen, token-aligned canonical reading currently underlies every quotation.
6. Maximum dictionary segmentation permits arbitrary skipped letters and does not test syntax, meaning, word boundaries, or sign consistency. The original 71.9% is a corpus-dependent character-coverage statistic, not a fraction of text securely deciphered.
7. No penalty accounts for choosing candidate inventories, token splits/merges, null assumptions, key changes, corpus/model, or editorial text after examining the full artifact. A calibrated end-to-end null would repeat that selection process with equal budgets.
8. The catchword removal is plausible but supplied rather than independently checked against the manuscript. The historical novelty claim is a negative bibliographic assertion not established by these tests.

## Re-run

All created artifacts are in this review directory. Input snapshots and SHA-256 records are in input_snapshot/ and input_hashes.json. The late reading.md snapshot is v4; initial and final key/control hashes match, but reading.md changed. The tested key/transcription are additionally preserved in metadata.json. The language-model corpus and probabilities are entirely local to this directory.

```sh
cd /private/tmp/claude-501/-Users-feyseel-Projects-feyseel-nl/0f448bec-026f-44e9-a40a-c944b80dffc5/scratchpad/foix/review
python3 prepare.py
TMPDIR="$PWD" clang++ -O3 -std=c++17 audit.cpp -o audit
./audit baseline > baseline.tsv
./audit heldout > heldout.tsv
./audit stratified > stratified.tsv
./audit numbers > numbers.tsv
python3 reproduce.py
python3 analyze.py > analysis_output.txt
python3 write_report.py
```

prepare.py reads parent inputs; if they have changed, use the archived snapshot or restore the saved metadata/data files before rerunning. reproduce.py additionally reads ../corp/cond5.f32; analyze.py checks phrase leakage against ../corp/clean2.txt. Their hashes are recorded. Re-running the core C++ experiments from the saved lm.bin, *.dat and metadata files does not require access to parent source code.

The final report includes only computed numbers. No conclusion is drawn about the later v4 key or its asserted 1565 manuscript corroboration.
