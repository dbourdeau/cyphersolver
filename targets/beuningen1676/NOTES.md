# Coenraad van Beuningen to Gaspar Fagel, 23 May/2 June 1676

Status: read in part; **key recovered based on adjacent plaintext**. No earlier reading of
this letter was found in the sources checked, and it has no contemporary decipherment. The extent is **PARTIAL**: the
reading does not meet the repository's bar unconditionally.
Decipherment by **Feyseel Nur (with Claude and Codex)**; added 5 October 2026.

## Document and key

Coenraad van Beuningen, Dutch envoy in London, wrote to Gaspar Fagel from
Westminster on 23 May/2 June 1676. Nationaal Archief **3.01.18, inv. 249,
scans 131–132** holds the letter: 131R, 132L and 132R. There are **278 cipher
tokens** among clear Dutch passages. A braced spelling counts as one token;
clear text, insertion brackets and superscript endings add no tokens.

The key was rebuilt from the clerks' interlinear glosses of sibling letters in
**inv. 248 (1675), 249 (1676) and 250 (1677)**. Thirty transcription TSVs are in
`transcription/tx/`. Some glosses are in a later hand, identified in
`evidence/ext2/hits.tsv`; they are not all contemporary clerk evidence.
The June letter itself has no contemporary decipherment. The historical
parallels below corroborate its subject, rather than provide its plaintext.

The system combines a homophonic letter table, colon-marked common words and
letter-prefixed numbers for an alphabetical Dutch nomenclator. Superscripts
add endings; a hyphen marks a compound prefix. Long s is transcribed `s`, not
`f`. The digit correction `z108` → `z103` is recorded in
`evidence/ext/digit_checks.tsv` and applied to the June transcription.

## Reading

`reading.txt` keeps the line labels, clear passages and deciphered stretches.
Question marks mark inferred readings; square brackets retain unresolved text
or an editorial explanation. Spacing and grammatical expansions are editorial.

> … op 't Subject van 't MY aen-gebracht dessein op den BRIEL ende HELLEVOET …

The French *dessein* concerns Den Briel and Hellevoetsluis. Du Plat and two
Frenchmen are to cross to Bruges to hire, or buy, bylanders. Du Plat has obtained
a pass for **Thomas Straught** and a party of men; the number of men is uncertain.
The English soldiers are to remain unaware of the plan until they cannot turn
back. Van Beuningen distrusts the informer. He pays an uncertain sum through a
burgher who must refund it if the information proves false.

> Du PLATT heeft ondertusschen EEN pas voor EENEN THOMAS STRAUGHT … afgehaelt …

He recommends secrecy and considers asking Brussels to arrest Du Plat with
the two Frenchmen at Bruges. Amsterdam rumours already concern orders against
the plan and the possible detention of the fleet under Bastiaensz.

The States General's secret resolution of **26 May 1676** summarises Van
Beuningen's cipher letter of **19 May**, an earlier letter. *Calendar of State
Papers Domestic, 1676–7*, **SP 29/381 no. 168**, mentions “Capt. Plat ... against
whom the States have published a placart”. This supports the historical setting;
it does not independently settle the June codes or the informer's truthfulness.

## Corrections and uncertainties

| Code | Reading and evidence |
|---|---|
| o177 | **ondertusschen**, not *onder anderen*: inv. 248 scan 313R has the same `54: o177` construction. |
| n155 | **genomen**, hence `74:-n155` = **op-genomen**; inv. 250 scan 305L has a later-hand *genoomen*. Excluding that hand removes one token from strict coverage. |
| z108 → z103 | **Zee**, after the digit correction; twice glossed on inv. 249 scan 142R. |
| b386 | **brengen**; the 272L *bylegginge* attribution was a misread. |
| m161 | **mede** is attested in inv. 248 and 250, but “mede proeven … als woorden ende parolen” remains awkward. Attestation does not repair the syntax. |
| g121 | The retained **gemelte** is I. The glossed alternative **selve** is M; it is a different word, not evidence for *gemelte*. “Den selven” would be editorial inflection. |
| v274 | June **vernemen** is I and conflicts with **verwondert** on inv. 250 scan 103R. Neither reading resolves both passages. |
| t218 | The sum paid is uncertain. *Tweehondert* is an I proposal; hundreds elsewhere are written as a number plus `h165` **hondert**. |
| 63: | Two M-quality *men* glosses do not erase the conflicting *can* gloss. |

The twelve residual I tokens are **c324, d210, e274, o211, p113, p122, s254,
t218, v111, v274, w141 and w204**. They propose, respectively, *consteren*,
*dertigh*, *engrosseren*, *onderrechten*, *parolen*, *participant*, *soecken*,
*tweehondert*, *vaertuyg*, *vernemen*, *geweten* and *woorden*. Each occurs once.
With *gemelte* retained, **g121 is an additional I token**. **s439** is unread,
in the **sup-** range; *sweeren* is not retained as a candidate.

Repository grades mean H = primary-key support, C = known-plaintext support,
M = uncertain, I = inferred. The historical key tables instead use H for a
sibling gloss and C for partly contextual spelling. Those bands are retained
as evidence history, not presented as repository-grade totals. There is no
primary key sheet here. `key/corrections.tsv` records the reviewed values;
`scripts/decode.py` applies them without overwriting the original tables.

## Measurement and controls

The Codex re-measure in `codex_review/review2.md` gives:

| Scenario | Strict H+C+M |
|---|---:|
| All gloss sources and our *gemelte* | **264/278 (94.96%)** |
| Excluding later-hand glosses, retaining *gemelte* | **263/278 (94.60%)** |
| Only if g121 is read as the glossed *selve* and the later-hand *genomen* is accepted | **265/278 (95.32%)** |

**Same-code direct gloss support is 241/278 (86.7%).** These are the review's
support measures, not a measured claim that 95% reads as coherent Dutch.
The twelve I tokens and s439 remain even in the conditional scenario, partly
clustered. The awkward *mede* clause and v274 conflict also remain.

The earlier blind-test accounting is corrected to **M 10/10, I 3/6** (one near
match and two misses among the I predictions). The key is **not cleanly blind**:
files already cite scan-128 glosses and `s250` was subsequently revised to `s258`.
`evidence/blind_test.tsv` preserves the comparison; the reviews explain its limits.

The shuffle control finds **93%** of spelled words of four or more letters Dutch,
against **1.2%** mean over **1,000 shuffled keys**, maximum **11.6%**. It tests
the spelling layer and includes a fixed list of names and historical spellings.
It does not validate inferred nomenclator values, syntax or sums. The recorded
result is retained; the word list is not included and the control has not been
rerun for this addition.

`evidence/ext2/RESULT.md` records an earlier upgrade claim. The second Codex
review supersedes its unconditional 265/278 and H claims. Both reviews are
preserved verbatim, including the first review's earlier counts and judgments.

## 23 Oct 2026: verification 3 (explicit-hole score)

The v3 sweep scored `reading.txt` as German (the text entry had no language; 0.528 explicit-hole), a false alarm. As
Dutch, with the line labels and the closing editorial-note lines cut, the body scores 0.872 explicit-hole (41/47
sentences, hole rate 0.048); plain 0.0 because the Dutch word list is modern and does not know 1676 spelling. The
entry now carries `language: nl` and `reading: june1676_reading.md` (the same text without line labels and notes) and keeps read.

## Read share over cipher words only (16 Nov 2026)

README Conventions now measure the read bar over the words written in cipher only. The reading puts spelled cipher
words in UPPER CASE but leaves code readings in lower case, like the clear text, so case does not separate them. Each
line of `reading.txt` was therefore aligned to its line in `transcription/june1676_tx.txt`, where the clear text is
between ~tildes~. The reading words that match the clear segments are clear, and the rest are cipher
(`research/reading_audit/r23_beuningen_split.py`, run from this folder). The clerk's interlinear insertions are text,
not holes. By the contributor's record:

- cipher words: 274 read; 3 unread (s439 `[...]`; t218 `[t218: som onzeker; tweehondert?]`; BR[U]GGE, a supplied
  letter); 12 inferred words marked (?), the twelve I tokens of Remaining gaps
- read share over cipher words: **0.946** (was 0.956, scored on `june1676_reading.md` whole, where the lower-case
  insertions `[ins ...]` and the struck-through note were counted as holes)
- whole letter with the clear text, not the measure: 0.973 on the same rules

The letter goes from read to read in part. The target was already read in part, and the token measure (264/278,
94.96%) is unchanged. Remaining gaps are unchanged.

## Remaining gaps
- Twelve residual I tokens (c324, d210, e274, o211, p113, p122, s254, t218, v111, v274, w141, w204), plus g121 when gemelte is retained, and unread s439 - blocker: no-key-material; context and alphabetical position do not establish these readings, and s439 lies in the sup- range
- Unglossed siblings: inv. 249 (1676) scans 118, 218–219; inv. 250 (1677) scan 86; inv. 248 (1675) scans 190, 238–239 - blocker: no-key-material; inventoried and still workable with the reconstructed key, without a complete reading claimed here

## Escalation
- [x] siblings: inv. 248–250 inventoried in evidence/inv_notes.txt; thirty glossed transcription files compared; the unglossed siblings above remain workable
- [x] clear-pages: the inventory distinguishes glossed and unglossed letters; no contemporary decipherment accompanies the June letter
- [n/a] known-keys: no primary key sheet is identified in these records; the working key comes from the sibling glosses
- [x] print: the 26 May secret resolution and CSPD SP 29/381 no. 168 corroborate the subject; neither is a decipherment of this letter
- [x] key-rebuild: May, November and cross-year glosses extend the three tables; later hands and conflicting readings remain distinguished
- [x] retry: the second Codex review re-tokenizes 278 positions and compares three strict scenarios; unresolved codes and sense remain explicit

## Sources and reproduction

- Nationaal Archief [3.01.18 inv. 249](https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/249), scans 131–132; gloss sources also in [inv. 248](https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/248) and [inv. 250](https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/250). Individual scan and line references are in transcription/tx/ and evidence/ext2/hits.tsv.
- States General, secret resolution, 26 May 1676, summary of the cipher letter of 19 May.
- *Calendar of State Papers Domestic, 1676–7*, SP 29/381 no. 168, Capt. Plat and the States' placard.
- Lead image: **Nationaal Archief, 3.01.18, inv. 249, scan 131 (CC0)**.

Run from the repository root:

```
python3 targets/beuningen1676/scripts/measure.py
python3 targets/beuningen1676/scripts/decode.py
python3 targets/beuningen1676/scripts/decode.py --exclude-later
python3 targets/beuningen1676/scripts/decode.py --selve
python3 docs/_check_profile.py --measure targets/beuningen1676/transcription/june1676_tokens.txt
python3 docs/_check_profile.py beuningen1676
python3 docs/_check_writeup.py beuningen1676
python3.14 targets/beuningen1676/scripts/build_site.py
```

The optional control requires `BEUNINGEN_OPENTAAL=/path/to/opentaal.txt` when
running `scripts/control.py`. No dictionary or manuscript images other than
the lead crop are included. No DECODE record is identified for this letter.
No verified correspondent portrait is available among the existing site assets.

## Contribution by WAINUT (21 Oct 2026)

WAINUT (a Dutch AI company, https://github.com/WAINUTAI) applied the key of this folder to the unglossed siblings
listed under Remaining gaps: inv. 248 scans 190 and 238–239, inv. 249 scans 118 and 218–219, and inv. 250 scan 86.
The key, the glosses and the June reading are this folder's, and nothing above is changed. This section adds transcriptions
and decodes of those pages, a calibration on scan 131R, a shuffle control, and a few letter numbers that
`key/key_letters.tsv` lacks. The files are in `wainut/`. No complete reading of any page is claimed.

**How the work was done.** The number groups were transcribed from crops of the NA scans by Google Gemini
(gemini-4-argon), in the token convention of `transcription/june1676_tx.txt`. Decoding, controls and analysis were
done with AI language-model agents. On every page for which a reading is given below, the cipher tokens were checked
by eye on the NA scans in two separate passes. The 15 resulting corrections are listed with their basis in
`wainut/corrections.tsv` and are applied in `wainut/transcription/`. The clear text in those files is the model's
transcription and was not proofread in full. Inv. 249 scan 219 was not checked by eye.

**Keys.** Key A is `key/key_letters.tsv`, `key/key_words.tsv` and `key/key_codes.tsv` with `key/corrections.tsv`,
as `scripts/decode.py` applies them: 76 letter numbers, 39 colon words, 62 codes. Key B adds every code and
colon-word gloss in `transcription/tx/*.tsv` (tokconf H or M) and `evidence/ext2/hits.tsv`. Where glosses differ,
the most frequent wins (H counts twice), and key A wins where both have a value. That gives 51 colon words and 432
codes. Key B contains no value of ours: it is this folder's gloss transcriptions, used as a key. None of the pages
below is among the gloss sources. Some key-B values used below rest on a single witness: g120 *geen* (249 scan 121R,
M), t178 *treden* (248 scan 313L, M), s105 *salveren* (249 scan 165L, M), c302 *conquesten* (249 scan 279L, H), and
v204 *vergaderen* and v493 *voorslagh* (only 250 scans 304R–305L, the later hand).

**Calibration on 249 scan 131R.** Of the 109 cipher tokens of 131R in `june1676_tx.txt`, the model transcription
has 101 identical (92.7%). The differences are three wrong digits (b387 as b389; 81 as 82 and 47 as 42 in one
group) and four grouping slips. With key A, 101 of the 109 decoded tokens are identical. Key B decodes 107 of the
model's 108 tokens, and the text agrees with the reading above apart from those slips.

**Coverage and control.** Coverage counts the cipher tokens that the key decodes completely. Control T scores the
key-B decoded runs by their mean log-probability per character under a character 5-gram trained only on clear text
(the clear passages of these pages and of `june1676_tx.txt`, and the glosses in `transcription/tx`). The real key B
is compared with 200 keys whose values are shuffled within each table (seed 1675). The columns count the shuffles
that score as high as the real key: whole key; colon words and codes only (letter table kept); letter table only.

| NA 3.01.18 | letter | key A | key B | T: whole key | codes only | letters only |
|---|---|---:|---:|---:|---:|---:|
| 249 scan 131R (calibration) | 23 May/2 June 1676 | 107/108 | 107/108 | 0/200 | 35/200 | 0/200 |
| 248 scan 190R | 4/14 June 1675, clerk copy | 25/34 | 27/34 | 0/200 | 13/200 | 0/200 |
| 248 scan 238R, last three lines | 10/20 Aug 1675, clerk copy | 11/19 | 15/19 | 1/200 | 50/200 | 0/200 |
| 248 scan 239L | same letter | 70/119 | 97/119 | 0/200 | 0/200 | 0/200 |
| 249 scan 118R | 12/22 May 1676, autograph | 1/3 | 1/3 (2 partly) | too short | | |
| 249 scan 218R | 9 Oct 1676, autograph | 9/23 | 18/23 | 0/200 | 4/200 | 0/200 |
| 249 scan 219L | same letter, end | 1/6 | 1/6 | 94/200 | 104/200 | 200/200 |
| 250 scan 86L, top | 20/30 Mar 1677, clerk copy | 6/12 | 9/12 | 0/200 | 2/200 | 3/200 |

The codes-only column is weak even on 131R (35/200), where the reading is established: a model trained on glosses
gives any shuffled Dutch word a fair score. It therefore says little about the nomenclator values. The evidence for
those is that they are glosses of the same codes in sibling letters.

**Readings.** CAPITALS come from the key (key B), `[x123]` and `[NN:]` are codes that key B lacks, `?` is a letter
number not in `key_letters.tsv`. Superscript endings are left out. Clear text is the model's transcription. The
English gists are our interpretation across the gaps.

- **248 scans 238R–239L, Sondley near Windsor, 10/20 Aug 1675.**
  > ende de wyle ik seide DAT DAER IN HAER HO: MO: NIETS [v270] soo [l119] DE FRANSCHE [i216] OP HET [b160] VAN
  > CONQUESTEN IN DESE OORLOGH GEDAEN en … SOO VRAEGHDE MY SYNE MAYT OF HAER HO: MO: SOUDEN [w182] [a363] EEN VREDE
  > MET EEN GENERALE RESTITUTIE VAN ALLE het GEOC?UPE?RDE IN DEN OORLOGH daer op ik geantwoordt heb, dat DAER TOE
  > GEEN RESOLUTIE [91:] NOG? BY DEN STAET VOOR A? GENOMEN ??NDE maer DAT HAER HO: MO: IN ALLE [g200] GEEN VREDE
  > KONDE MAECKEN ten zij HAERE GEALLIEERDEN IN DEN STAET in de welke SY SYN GEWEEST VOOR DEN OORLOGH SOUDEN WESEN
  > [h149] ENDE DAT INDIEN SYNE MAYT DE [p266] VAN EEN GENERALE RESTITUTIE BY VRANCKRYCK ??NDE UYT [w159] HET E?N
  > GROOTE PAS TOT DE VREDE scheen TE SULLEN SYN … ENDE TE [w154] DAT DEN OORLOGH OP DIE UOET [66:] [t124] WERDEN
  > soo DAT de REPUGNANT?E DIE DESE VOORSLAGH VOOR DESE in de GEEST VANDE CO: heeft gevonden DOOR DE [v153] sedert
  > IN de SAECKEN VOOR [v110] ?T [s418] VANDE [w121] OP FRONTIEREN VAN DUYTSLANDT scheint eenigermate opgeheven

  Gist: Charles II asked whether the States would [accept] a peace with a general restitution of everything
  occupied in the war. Van Beuningen answered that no resolution had yet been taken, but that the States could make
  no peace unless their allies were restored to their pre-war state; if the King obtained a general restitution
  from France, that would be a great step towards peace. The King's earlier repugnance to the proposal seemed
  somewhat removed since [events] on the German frontiers. On 239L the whole-key and the codes-only shuffles both
  give 0/200.
- **248 scan 190R, 4/14 June 1675.**
  > MAER DAT MEN sich NIET MOST ILATTEREN DAT sijn Majt. soo LANGE de FRANSCHE [c104] [r173] SOUDEN SYN SIGH DAER
  > OVER IN OORLOGH SOUDEN ?NLATEN TEGENS [d219] dewijle SYN EER NOGH DEN [f114] [g140] VAN SAECKEN HEM [s426] NIET
  > TOELIETEN

  Gist: one should not flatter oneself that the King would go to war against the French over the Spanish
  Netherlands, since neither his honour nor the [...] of [his] affairs would allow it. ILATTEREN is *flatteren* if
  the first number is 42 (f), as the scan may allow; the transcription keeps 12. d219 is uncertain in its last
  digit (d214 is *deselve*).
- **249 scan 218R, 9 Oct 1676.**
  > aen des Coninghs [g169] OM UAN NUW AF te TRACTEREN over de [a312] met HAER HO: MO: hebbende de Heer Williamson
  > mij gesegt dat hij geloofde, men soude met WERCK kunnen TREDEN als ik LAST SAL HEBBEN ende is apparent dat de
  > [v452] van die SAECKE sal helpen [f105] [s357] RESOLUTIE van den RUPTURE met VRANCKRYCK … gedaghten sijn SYN
  > PARLEMENT te VERGADEREN

  Gist: Williamson said work could start once Van Beuningen had instructions; the matter would help towards a
  resolution for a rupture with France; the King intends to convene Parliament. TREDEN and VERGADEREN rest on
  single witnesses (above).
- **250 scan 86L, 20/30 Mar 1677.**
  > nodigh was DAT HAER HO: MO: OP EAN [r173] VOET DAER OVER met [s489] [c240] … om de SPAENSCHE NEDERL. te SALVEREN

  Gist: to speed the peace the States would have to [come to terms] on a [...] footing; the King would then do his
  best to save the Spanish Netherlands. `{10,4,65}` gives *ean* because 4 = a in the table; the sense wants *een*.
  r173 is also open on 190R.
- **249 scan 118R, 12/22 May 1676.** "van de DESSEYN op de BRI?L ende HELLEUO?T": the plan against Den Briel and
  Hellevoetsluis of the June letter. The third number of the Briel group is overwritten and uncertain.
- **249 scan 219L.** One of six tokens decodes and the control shows no signal (94/200). We could not decode it
  with this key.

**Open codes** (not in key B; `wainut/check.py` section 6): 190R c104, r173, d219, f114, g140, s426; 238R v270,
l119, i216, b160; 239L w182, a363, 91:, g200, h149, p266, w159, w154, 66:, t124, v153, v110, s418, w121; 218R
g169, a312, v452, f105, s357; 86L r173, s489, c240; 219L v517, c344, z1, v531, k143.

**Letter numbers not in `key_letters.tsv`** (proposals for you to judge; not used in the decodes above):

| number | value | where (eye-checked pages) | fits the slot order of the table |
|---|---|---|---|
| 8 | e | 239L *geoccupeerde*, *een*; 118R *Briel*, *Hellevoet* | yes (e = 6–10) |
| 13 | i | 190R *inlaten*; 239L *repugnantie* | yes (i = 11–15) |
| 35 | c | 239L *geoccupeerde* | yes (c = 32–33) |
| 43 | f | 239L *vooraf genomen*; also `{43,86}` before s418, unclear | yes (f = 42) |
| 52 | h | 239L *nogh* | yes (h = 49–51) |
| 54, 16, 17 | s, y? | 239L `{54,16,70,37,10}` and `{54,17,69,38,7}`, context *synde* | no: 54 sits between h and k; left open |

**What this does not settle.** On the six pages with readings, 43 of 210 cipher tokens (20.5%) are not fully
decoded by key B, and the gists bridge them by interpretation. We did not check printed editions, or whether Van Beuningen sent parallel letters
to the Griffier (NA 1.01.02). The profile, grades and Remaining gaps above are left for you to update if you
adopt any of this.

Reproduce from the repository root (standard library only; it rewrites `wainut/readings/`):

```
python3 targets/beuningen1676/wainut/check.py
```

Scans: Nationaal Archief 3.01.18 [inv. 248](https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/248)
scans 190, 238, 239; [inv. 249](https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/249) scans 118,
131, 218, 219; [inv. 250](https://www.nationaalarchief.nl/onderzoeken/archief/3.01.18/invnr/250) scan 86. No images
are included.
