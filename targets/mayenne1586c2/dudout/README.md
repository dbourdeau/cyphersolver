Status: in progress (fr. 15573 f. 120 only: sign-by-sign image round on the lines flagged by the b21 re-read; 90.0% of letters read by the 95% rule, up from 88.3%; still under the bar. f. 385 not attempted here.) Next step: f. 385 sign round on views 752-753; values for the code signs E, 15, .u., 4d.

# fr. 15573 f. 120: sign-by-sign image round on r c15-c19, c24-c31, v c03-c05 (Brice Dudout, 12 Nov 2026)

Work by Claude Opus 5.5 for Brice Dudout. It builds entirely on Harumi-Matsuba's transcription and decode
(`../f120_harumi/`, CC BY 4.0), on Brett Burford's key (`../f385_burford/key-cipher2.json`), on Satoshi Tomokiyo's
Cipher-2 table, and on Daniel Bourdeau's b21 re-read (`../f120_harumi/f120_reading.md`, `f120_reread_log.md`), which
named the lines to check. Nothing here changes their files.

## What was done

1. **Image round.** Gallica btv1b90618780 views 246-247 at full resolution (openapi.bnf.fr IIIF, 4959 x 6438 and
   4975 x 6528), cut into line strips. The 16 lines the b21 log left open were re-read sign by sign against
   Harumi-Matsuba's transcription, with his sign names.
2. **Frozen before decoding.** The re-read transcription (`f120_transcription_reread.txt`, SHA-256
   `395c1995b8391fa50ea8e2ff4795e6910803463d441789d3913bfce3910f6066`) and the list of doubtful signs (frozen French
   original SHA-256 `804e5946bb851ed63f701e10a790850e8b968c5dcf9eb9edd967b57907f17f08`; English below) were hashed
   before any decoding with the key. `scripts/make_reread.py` applies the changes and asserts each old value.
3. **Decoded** with the target's key unchanged (`../f120_harumi/key.tsv`; `scripts/decode.py` ->
   `f120_decode_reread.txt`).
4. **One pre-registered measure** (below), frozen by SHA-256 before it was run.
5. **Reading** of the stretches, every letter put in one of four classes, counted with the 95% rule.

## Changes to the transcription (8, all on the 16 re-read lines)

| place | seen on the image | was | now |
|---|---|---|---|
| r c15 #21 | v with a bar below (v̲) | r | vbar (new name) |
| r c16 #9 | open 8-shaped g with a dot | g | g8 (new name) |
| r c16 #11 | same hooked g as #14 | f | g (same value s) |
| r c27 #1 | v̲, same form as r c15 #21 | r | vbar |
| r c28 #7 | barred ϖ with two humps | w (est) | w2 (il): "il m'est tombé" |
| r c30 #1 | flat-topped б | B (s) | 6b (f) |
| r c31 #2 | q with a crossed stem | 9 (d) | q+ (l): "spe[ci]alement" |
| v c05 #2 | "5", the same form as the S of "certain" later in the line | ls (r) | S (c): "au ser[v]ice" |

The other re-read lines (r c17-c19, c24-c26, c29; v c03-c04) agree with Harumi-Matsuba sign for sign.

**Doubtful signs (2-3 options each):** r c15 #21 and r c27 #1 vbar / r; r c16 #9 g8 / g; r c28 #7 w2 / w; r c28 #19
tt (les) / w2 (the form is the two-humped barred ϖ; "les" by sense); r c30 #1 6b / B; r c31 #2 q+ / 9; r c31 #6
curlo / delta / own sign (a δ with a small loop, before "inances"); r c24 #11, #18 dbar / a t-variant (same curled
form as "n'y en" in r c09, so kept dbar); v c03 last lambda / delta (no lower loop); v c05 #1 f / own sign (f with a
loop); a "2"-shaped stroke over the first sign of r c31 (probably the tail of the ʒ above). No blind planche was made.

## The measure (pre-registered, one run)

Portion: the 16 re-read lines, 453 tokens, 581 plaintext letters, decoded with the key unchanged (no new value).
Statistic M: share of tokens read by `targets/matignon1586c3/f276/scripts/measure.py`'s rule (run of >= 3 lexicon
words, >= 10 letters, fr-1600-letters, mincount 20). Controls: 200 permuted letter keys + 200 shuffles of the token
order. Criteria fixed in advance: (1) M above every control; (2) M(re-read) >= M(Harumi-Matsuba, same lines).
Script `scripts/measure_reread.py`, output `measure_result.txt`.

| | M |
|---|---|
| re-read transcription | 409/453 = 0.903 |
| Harumi-Matsuba transcription | 412/453 = 0.909 |
| 200 permuted keys | median 0.124, max 0.428 |
| 200 shuffled texts | median 0.550, max 0.695 |

(1) holds (0 of 400 controls reach 0.903, p = 1/401). (2) does not (three tokens fewer): the pre-registered criterion
**failed**. The eight corrections are reported as not shown by the measure: they rest on the sign forms, not on a score. The measure
cannot see the gains below, which are word-level ("il m'est", "alement", "ser-ice"), not lexicon runs.

## The reading, counted with the 95% rule

Notation (`f120_reading_reread_annotated.txt`): plain = sure; {x} = probable; [x] = restored (holes); [?x] = unresolved
(holes; x = the decode letters, ___ = a code sign with no value, counted 3 letters). The "before" file is the b21
reading word for word, with the holes of the re-read stretches filled with their decode letters
(`f120_reading_before_annotated.txt`); outside those stretches both files are the b21 text. `scripts/count95.py`.

| | sure | probable | restored | unresolved | total | read (sure + probable) |
|---|---|---|---|---|---|---|
| whole letter, before (b21) | 1,307 | 0 | 45 | 129 | 1,481 | 88.3% |
| whole letter, after | 1,335 | 9 | 62 | 87 | 1,493 | **90.0%** |
| re-read stretches, before | 381 | 0 | 4 | 85 | 470 | 81.1% |
| re-read stretches, after | 409 | 9 | 21 | 43 | 482 | 86.7% |

`docs/_check_reading.py` on the same footing (the reading pointed at in turn): b21 `f120_harumi/f120_reading.md`
0.467 (21/45 sentences, holes 0.193); this re-read `f120_reading_reread.md` 0.564 (22/39 sentences, holes 0.152);
still "marginal". `profile.json` keeps the b21 reading as the document's reading; the maintainer may switch it.

What changes in the sentences (the decode letters, now divided):

- r c15-c19: "... que [E] est tout resolu, quelque [comme]ndement et coniuration que vous [luy] puissies faire de
  s'en aler, et partir si [tost] qu'il saura ce que doivent devenir les estrangers". b21 had an extra "que" the figures
  do not give, "s[?] puis [?…]" and "[?s'en]": "puissies" and "s'en" are carried letter for letter. Restored:
  vbar = comme (two places, see below), g8 = luy, Om = tost (one place each, from context).
- r c27-c31: "mais nous somes {comme} un corps si debile qui ne peut afaire profit de [n 15]. Il m'est tombé entre
  {les} mains une [.u.] du secretaire La Marsiliere, qui nous [?le fort] particulierement des afaires de [4d],
  spe[ci]alement des [f]inances, et semble qu'ils facent plus de fondement ...". vbar = comme fits both its places
  (here and "commendement" in r c15), so "comme" is counted probable here, restored in r c15. "qui nous le sort" of b21
  rested on B = s; the sign is the б (6b, f), and "le fort" has no verb, so it is now unresolved.
- v c03-c05: "... remise pour u[n] temps. L'on ne sauroit com{p}rendre l[e] tort que la rupture de ceste armée faict
  au ser[v]ice du [Roy]. Car [c']est certain que si ele subsistoit encore six sepmaines ...". The ℓ-sign (Lp) is
  read p here (Tomokiyo's table has this form at p; Harumi-Matsuba inferred i elsewhere), counted probable. I (u in
  the key) before "Car" is restored as "Roy" from context only.

English of the changed passages: "And moreover [E] is quite resolved, whatever command and entreaty you may make to
him, to go away and leave as soon as he knows what is to become of the foreigners ... but we are like a body so weak
that it cannot make use of [...]. There has fallen into my hands a [...] of the secretary La Marsilière, which [...]
very particularly about the affairs of [...], especially the finances, and it seems they put more trust in [...]
poverty than in the coming of their foreigners, which he says has been put off for a time. One cannot understand the
harm that the break-up of this army does to the service of the [King]."

## Still open on f. 120

- r c24 "si je irai, [?s'ay en dray] ce que l'on m'en dira": the signs are as transcribed (the curled ǂ is the dbar
  of "n'y en", r c09); no sense found.
- r c25-c26 "les deputés de l'armée qui [?suie(a|n)ent apler] et font [?ts] ofres".
- Code signs with no value: E (r c15), 15 (r c28), .u. (r c29), 4d (r c30), and those already listed in NOTES.
- The value hypotheses vbar = comme, g8 = luy, Om = tost, I = Roy, Lp = p rest on this letter only; they are not
  added to the key.
