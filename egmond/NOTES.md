# Charles of Egmond, BnF français 3015 no. 8

Status: read, with minor uncertainties retained. Already solved by George Lasry in 2023 (key on cryptiana GL.htm §2; he pointed this out on 21 Sept 2026): this reading is an independent re-solution, not a first reading.

Lasry review (25 Sept 2026): not a first break, so left out of the ciphertext-only list sent to Klaus Schmeh (profile outcome.first_break = false).

## 20 September 2026: source location

The active goal is to solve the letter, including the ciphered address. A provisional French reading and inferred key now exist; see the checkpoint below. The preceding turn concerned a
different target (Throckmorton) and supplies no cryptanalytic evidence here.

The BnF catalogue https://archivesetmanuscrits.bnf.fr/ark:/12148/cc49473n
locates item 8 at folio 16: "Lettre, en chiffre, de « CHARLES », duc DE
GUELDRES, avec une adresse en chiffre." Its component is
FRBNFEAD000049473_d0e176. The proposed 1520s date is not yet verified from
the document. The volume's French language metadata does not establish the
cipher's plaintext language.

Images retrieved from Gallica IIIF, identifier btv1b9060086g:

- View 27: folio 16, main letter, sixteen cipher lines (the last short),
  clear closing and CHARLES signature; later heading M. de Gueldres.
- View 28: mounted ciphered address, three lines.
- View 10 is folio 5; view 32 is folio 19. Do not infer a uniform
  two-views-per-folio mapping. Other downloaded neighbouring views remain
  contextual and have not been established as belonging to this letter.

Source URLs use
https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060086g/f27/full/3000,/0/native.jpg
and the corresponding f28 path (currently 1600 pixels wide).
The manifest and catalogue HTML are cached under sources/; source images and
analysis crops are under images/, excluded from git.

The body uses recurring graphic signs, with apparent spaces, double and
triple strokes, loops and cross forms. The alphabet size and length are not
yet counted: neither visual similarities nor spaces have been treated as
proven token boundaries. The clear closing appears French and supports
testing French first, but does not prove the enciphered language. No crib
has been imposed and no plaintext is claimed.

Next: transcribe body and address with stable glyph labels, distinguish
similar forms against the high-resolution image, count tokens and repeats,
then test substitution hypotheses. Full solution remains required.

## DECODE and contextual checks

The user reminded us of the existing DECODE cookie. Confirmed the file exists
and used it for a direct request to DECODE's RecordsList (154934 bytes), cached
privately. Cookie contents were neither printed nor copied. The locally harvested
record list and all three detailed views JSONL files contain no match for Egmond,
Guelders/Gueldres, Gelre/Geldern or the target shelfmark. Record ID 3015 is an
unrelated British Library letter, not BnF français 3015. This negative check is
limited to the cached metadata and is not proof that DECODE lacks the item.

The BnF description of item 12 identifies another Charles letter in this same
volume, to the grand maître, dated Arnhem 3 April 1537. This is a useful
comparison candidate for handwriting and address formulae, not a date or
recipient assignment for the ciphered item 8. General web searches yielded no
identified decipherment or key for item 8.

## First transcription probe

`opening_provisional.txt` contains a rough shape-label transcription of the
first three body lines. Labels are visual mnemonics, not plaintext. In particular,
cross/4 shapes, zigzags and loop shapes may have been conflated, and paired
`dd`/`ee` strokes may represent one sign rather than two. It is not a reliable
full ciphertext and must not be used to claim an alphabet size or corpus length.
`opening_tokens_provisional.txt` makes the individual provisional labels explicit
for the measurement tool.

`probe.py` tests a bijective substitution with the repository's existing
24-character period-French conditional five-gram model, twelve reproducible seeds
of 40000 proposals each. Separate-stroke, joined-dd, joined-ee and joined-both
variants produced no readable French. Their raw scores are not comparable as
evidence for segmentation because the lengths differ. The preceding many-to-one
probe collapsed to repeated letters, exposing a limitation of this conditional
scorer; that output is not a reading. Missing numba/model dependencies and an
initial alphabet-dimension mismatch were corrected before the bijective runs.

These unsuccessful probes do not exclude a simple substitution. The next step
is to correct the transcription from glyph crops and cross-occurrence comparison,
not to treat the best-scoring gibberish as a decipherment. French remains only
the first language hypothesis.

## Comparison leaf, solver control and indexed glyphs

Gallica views 39 and 40 are the separate clear letter at folio 24 and its
address. The body opens "Monsr mon bon Cousin" and discusses the bearer,
an ambassador, seeking support for the writer's affairs. Its address reads
"A Monsr mon bon Cousin Monseigneur Le grant Maistre" (abbreviations
expanded here). Its date is Arnhem, 3 April 1537, matching catalogue item 12.
These are contextual formulae, not decipherments of item 8, and the body
does not provide an independently matched clear copy of item 8.

`validate_probe.py` supplies a constructed 180-letter French positive control
with a reproducible random substitution. The same solver recovered all letters
exactly (`synthetic_control_validation.json`). Its text is synthetic and is
explicitly not the Egmond plaintext. This supports the basic solver implementation
but cannot validate the manuscript transcription or exclude other cipher systems.
A reversed-text French probe also failed to produce readable text.

`glyph_sheet.py` creates an indexed contact sheet of connected ink components
for the first line, with bounding boxes preserved in `line1_components.json`.
There are 69 components, not 69 established tokens: ascenders from the next line
intrude, some components join neighbours, and small strokes are split off. This
is a visual-audit aid, not an OCR transcript. The sheet suggests a possible
distinction between the two shapes provisionally labelled `ee` (a c-like and
an e-like form). Testing the `ce` distinction everywhere in the provisional
opening still yielded no readable French; this global replacement remains a
hypothesis, not a confirmed correction.

The next transcription pass must distinguish single and double crosses, open
and angular 4-like forms, c/e-like forms, and zigzag variants on each occurrence.
Neither the cipher language nor addressee, date, alphabet or plaintext is yet
established. The goal remains open.

## Address transcription and broader probes

`address_provisional.txt` and `address_glyphs.json` record the three-line address
with explicit shape descriptions, independently of the opening transcript.
The measured provisional sequence has 56 tokens and 20 labels. This is a
measurement of the transcription, not an established original alphabet size.
The descender of the first-line initial cross overlaps the next line; it must
not be counted again as a separate second-line character. Paired arches and
quavers remain uncertain as single versus compound signs.

`opening_revision2.txt` distinguishes simple pluses from angular 4-like forms,
top-bar corners from side-bar T forms, and c-like from e-like forms, where the
image appears to justify doing so. It remains provisional. French probes on
both separate and compound-stroke readings did not recover readable text.
The independent address likewise did not produce a coherent reading in its
separate or compound-stroke tests. German and Italian models on the original
three-line draft also failed. These are failed hypotheses under uncertain
transcriptions, not exclusions of languages or cipher families.

The probe now accepts language and input-file arguments and records both in
its JSON outputs. Models: the existing period-French 24-letter table;
`kurtz1639/de_early5.npy` with the early German alphabet; and
`pallotto1629/it_clean5.npy` with the alphabet in its JSON metadata. Their
scores must not be compared across languages as calibrated probabilities.

## Literature search follow-up

Searches in French, Dutch and German yielded no identified key or decipherment
of this letter. A concrete bibliographic lead is Gerard Kalsbeek, *De
betrekkingen tusschen Frankrijk en Gelre tijdens Karel van Egmond* (Wageningen,
1932). No digital copy was located in these searches; its contents have not
been inspected and no claim about the target is attributed to it.

Downloaded https://sup.sorbonne-universite.fr/commerce-file/3950/download
to `sources/diplomatic_letters.pdf` and extracted it to a private text cache.
It is Gilles Docquier's chapter on political correspondence between Maximilian
and Margaret of Austria. It cites Kalsbeek and discusses the Guelders conflict,
but the extracted chapter contains neither `3015` nor `chiffr`. It has supplied
context and the bibliographic lead, not a key or matching plaintext.

## Six-line transcription and null hypothesis

Extended the draft through body lines 4–6, retaining source crops and a shape
legend in `body_glyphs_provisional.json`. The combined file
`body_six_lines_provisional.txt` measures **343 provisional tokens, 22 labels**
with `_check_profile.py --measure`. These remain transcription statistics, not
verified document statistics. `W`, the broad backward-five form, is newly
distinguished; earlier lines may have conflated it with other zigzags and need
another occurrence-level check. Line 7's supralinear insertion is not yet included.

Tested the explicit hypotheses that paired D strokes, or both D pairs and CE
pairs, are nulls. Tested both the revised opening and six-line draft, without
obtaining sustained readable text. Null-removal scores cannot be compared
directly with the unshortened sequences as evidence of correctness.

Added an optional many-to-one substitution probe, with a letter-distribution
penalty to discourage the earlier repeated-letter collapse. The prior is the
average next-letter distribution of the existing language model, not a measured
plaintext distribution for this letter. Tested the six-line compound-stroke
variant with this option. It produced French-looking fragments but no coherent
sentence or stable independent validation. None of its generated text is accepted
as a reading, key, or historical claim. All runs completed; no solver is pending.

The enlarged draft improves coverage but does not settle glyph identities. Next
work should align occurrences and extend the remaining ten lines and insertion,
then use the address and body jointly under consistent glyph labels. Repeating
short probes on unchanged drafts will not resolve the present uncertainty.


## French-reading checkpoint (unfinished)

Extended the provisional transcript to all sixteen main lines (804 shape labels,
23 distinct labels; not verified cipher-token counts). The supralinear insertion
on line 7 remains untranscribed. Full-text probes with compound DD/CE signs led
to sustained French fragments. Interpreting F, O and X as nulls yields the opening
`mon cousin`; DD represents s and CE represents r in the working hypothesis.
`candidate_key.json` and `decode_candidate.py` reproduce the raw candidate in
`candidate_reading.txt`, without silently repairing it from expected prose.

The address provisionally reads “A mon bon cousin, Monsieur le grant maistre de
France”. This requires occurrence-level corrections to the old shape labels:
m/n zigzags were conflated, the b/f forms differ, and an apparent extra sign is
part of a neighbouring glyph. Its ending appears to contain nulls. This is an
inferred cross-check, not an independently supplied plaintext or archived key.

Body fragments include `vous communiquer`, `et le croire` and final `iuillet`.
The apparent Arnhem/July date remains provisional; no year or named recipient
has been established. Values are inferred (I), with uncertain glyph readings (M).
Do not treat the uncorrected candidate as a diplomatic edition or a solved target.
Remaining work: audit each glyph against the images, distinguish rounded nulls
from angular a, repair m/n and cross forms, transcribe the insertion, and verify
the full body and address. The goal remains in progress.

The existing private DECODE cookie was used for catalogue access; it is not part
of this checkpoint. Cached catalogue searches supplied no matching Egmond key
or plaintext. Sources and images remain ignored.


## Occurrence-level image audit: address and seven body lines

`address_audited.json` now separates seven/b from corner/f, long m from short n,
and compound signs from adjacent nulls. `decode_audited.py` gives exactly:

    amonboncousin
    monsieurlegrantmaistre
    defrance

Word division: A mon bon cousin / Monsieur le grant maistre / de France.
The address is inferred from the manuscript and working key, not an independent
known-plaintext control. No personal name is enciphered in this reading.

The same replay script uses `body_revision3.txt` and `audited_key.json`.
`body_audit.json` records which lines were inspected: 1, 2, 3, 9, 13, 14, 16.
Other lines are explicitly marked DRAFT, even where they resemble French.
Opening changes recover `aduerti que donnes faueur`, `possible au bien de mes
affaires`, and `vous ai bien ... prier voulloir`. The raw forms `sueis` and
`uouellu` remain; they have not been silently respelled. The closing now gives
`ce scet nostre seigneur auquel apres / mestre recommande a vostre bonne grace
prie`. Plain plus/g differs from angular four/u; the h-like sign is provisionally
null. This resolves several errors independently of adding expected letters.

The date crop still leaves the complex sign after `di` uncertain. An eighteenth-
of-July interpretation remains a hypothesis, not a verified date. The place-name
also needs its own glyph audit. Nine main lines and the supralinear insertion
remain unaudited. The target is still in progress.


## Full candidate reading, including both insertions

Audited the remaining main lines and retrieved the native 4351 x 6122 scan.
Direct Python requests were unavailable; urllib received HTTP 403; curl with a
browser user agent succeeded. The native scan confirms the second insertion
DD V (`sa`) above line 15. The line-7 insertion reads `entenderes`. Reinterpreting
the disputed line-7 sign cluster as `guerre`, not `ouverture`, resolves the king's
commands / entry into war passage. The ambassador is `le commandeur de sainct
Iehan`; no personal name is supplied. The address names the grand master of
France. The closing place is Arnhem and the date `dih[u]itieme de iuillet`,
apparently 18 July, with the blotted u marked M. No year is encoded there.

READING.md gives all sixteen lines, insertions, clear closing and address, with
an English sense translation and explicit residual ambiguities. The word-divided
lines were checked against the raw token replay. `body_complete_tokens.txt`
measures 726 tokens and 27 labels with the standard checker; aliases and the
blotted instance mean this is not a historical alphabet count. Full consistency
review and site write-up remain pending. Target status remains in progress.

Searches using Gueldres/commandeur/grand maistre and Arnhem/18 juillet did not
identify a matching edition, a verified year, or the ambassador's name. No new
external plaintext has been used.


## Final reading and publication review

The body (16 main lines plus two insertions), address (three lines), clear closing
and signature are all accounted for. Native-resolution crops were inspected for
the anomalous forms. The cross in lextreme has a bar extending left from the stem,
distinct from the plain cross used for g; x still has only one occurrence and is
graded M. The blotted date u remains M. These are disclosed local uncertainties,
not unresolved passages. No independent clear copy or key has been found; no
claim of 100% letter accuracy or proven priority is made.

The corrected body has 726 labelled signs and the address 48, measured from the
replay files. The 27 body label names include u variants and a special label for
the blotted u; they are not a claim of 27 distinct historical glyphs. The original
catalogue's 1520s attribution is not substantiated by the recovered date. The
reading gives Arnhem, apparently 18 July, without a year. Recipient and ambassador
are identified only by the titles actually in the cipher.

The write-up surfaces pass docs/_check_writeup.py egmond; the profile validates. The local page was inspected in the browser, including the full reading table. The decoder confirms edition-to-token fidelity and both insertion anchors. These software checks do not establish an independent historical control.
