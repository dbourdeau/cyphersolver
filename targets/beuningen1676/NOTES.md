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

## Remaining gaps
- Twelve residual I tokens (c324, d210, e274, o211, p113, p122, s254, t218, v111, v274, w141, w204), plus g121 when gemelte is retained, and unread s439 - blocker: open-codes; context and alphabetical position do not establish these readings, and s439 lies in the sup- range
- Unglossed siblings: inv. 249 (1676) scans 118, 218–219; inv. 250 (1677) scan 86; inv. 248 (1675) scans 190, 238–239 - blocker: open-codes; inventoried and still workable with the reconstructed key, without a complete reading claimed here

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
