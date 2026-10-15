# Sormano and de Vaulx to François I, Ferrara, February 1529

BnF français 3096, nos. 63, 65 and 66 (Gallica `btv1b9060015d`). The letters
concern Ferrara's defection from France before the Peace of Cambrai.

**One entry for one cipher (merged 14 Oct 2026, one-key rule).** The same three letters in the same key were also
the target `sormano1529`, Arya Sanketbhai Patel's work (PR #2, 18 Sept 2026), with its own profile, page and
outcome (read in part, 0.05, against this folder's "read"). They are now one entry: this folder, this profile and
`docs/sormano.html`. His folder moved to `targets/sormano/arya/` unchanged (NOTES, scripts, `key_lasry.tsv`,
`ct/`, `src/`), and `docs/sormano1529.html` is a stub pointing here. What his work adds is credited to him in the
profile and on the page: the third sheet of no. 63 (f. 123, numbered "3", dated *penultimo de Febraro* = 27 Feb
1529, signed Sormano and Joachin), the identification of "Ioachin" as Gian Gioacchino de Passano, seigneur de Vaux,
no. 64 having no cipher, the "de Venetiani" gloss on f. 116v, the f. 124 margin crib, an independent derivation of
22 key values (20 agree with Lasry's table) and the record of eight failed ciphertext-only methods on the microfilm.
The reconciled outcome is below (## Outcome, reconciled).

## Leaves and controls

| item | leaf / Gallica view | date | state |
|---|---|---|---|
| no. 62 | f. 113 / view 117 | 22 March 1529 | cipher with contemporary interlinear decipherment; key control |
| no. 63 | ff. 115–116, 123 / views 119–121, 127 | 27 February 1529 (*penultimo*, on f. 123r) | target; ff. 115–116 read in patches, see `n63_reading.md`; the third sheet f. 123r, bound out of order (arya/NOTES.md §1), read 14 Oct 2026, see `n63_f123r_reading.md` |
| no. 65 | ff. 119–120 / views 123–124 | 23 February 1529 | target; read, see `n65_reading.md` / `n65_transcription.md` |
| no. 66 | ff. 121–122 / views 125–127 | 23 February 1529 | target; docketed `duplicata`; read, see `n66_reading.md` |
| no. 67 | f. 124 | 1529 | Sormano's `Doppio`, cipher with decipherment; second control |

## What nos. 65 and 66 are

**No. 66 is docketed `duplicata` and is the duplicate of no. 65.** No. 63 opens
*"Il xxIII del p[rese]nte per n[ost]re **duplicate l[ette]re** a v[ost]ra M[aes]ta
al lungo scriuessimo ciò che haueuamo negociato con questo S[ignor] Duca"* —
that is, nos. 65 and 66 are the pair sent on 23 February, and no. 63 is the
follow-up written a few days later. Both bear *Da Ferrara alli 23 Febraro 1529*.

The two are **independently drafted, not literal copies, and — decisively —
they encipher different passages.** Where no. 65 puts a sentence in cipher,
no. 66 very often writes it out in clear, and the reverse. The pair is
therefore its own crib: aligning them recovers most of the text without
decipherment at all, and checks the decipherment where it is needed.

Worked example, the same moment in the audience:

| no. 65, f. 119r L5 (cipher, deciphered) | no. 66, f. 121r L6–7 (clear) |
|---|---|
| *maiesta, fato la reuerentia a madama Rainea et al signor don Hercole* | *fatta che hebbimo la reuerentia a Madama Rainea et al s[ignor] Don Hercole* |
| *…conforto… suadesimo… instantemente esortasimo et pregasimo sua signoria…* | *suadessemo confortassemo et instantementi essortassemo et pregassemo…* |

This is an independent confirmation of the decipherment: the plaintext read out
of no. 65's cipher is the text no. 66 writes in the clear hand.

## Cipher and key

One continuous homophonic substitution alphabet, special signs for `cc` and
`ll`, no transposition. George Lasry reconstructed the key in 2023 (Tomokiyo,
Cryptiana); `key_lasry3.png` is the published table and `KEY.md` the local
transcription. The hand and symbol repertoire of nos. 63, 65 and 66 are the
same as the control no. 62, so the key applies to all three — the "verify
first" step is satisfied.

Three corrections were established on the leaves and are recorded in `KEY.md`:
the fourth `e` homophone is a **crossbarred long-s** (not `f`; `f` is the
double `ſſ`); there is a **null**, a tall looped sign absent from Lasry's
table; and the **large double circle `◎` is a nomenclator for DUCA**, distinct
from the dotted circle `⊙`, which is an ordinary `i`. The first two are proved
against the glossed ground truth on f. 113r; the third resolves every context
in which the sign occurs (`con questo ◎`, `fusimo col deto ◎`, `andai dal
deto ◎`).

## Codicological note

No. 63 breaks off in mid-sentence at the foot of f. 116v (*"difficilmente
crederemo …"*). The facing leaf f. 117 is a different paper in another hand and
wholly unciphered, so the continuation of no. 63 is not there; the end of the
letter, and its date, still have to be located. `pages.json` covers only the
four sides ff. 115r–116v for no. 63.

**Superseded (14 Oct 2026):** the end is f. 123r, bound out of order after the duplicate, numbered "3" at the
foot and dated *penultimo de Febraro* 1529 (found by Patel, `arya/NOTES.md` §1); its cipher is read in
`n63_f123r_reading.md`. The image is canvas 127 (`raw/full127.jpg` in the main checkout, right half).

## Files

`n65_transcription.md` / `n66_transcription.md` — line-by-line transcriptions.
`n65_reading.md` / `n66_reading.md` — continuous readings. The no. 65
transcription and the no. 65 reading were made independently and in parallel;
they agree on the substantive lines and on the null and the `◎` nomenclator,
which is worth more than either alone. `FINDINGS.md` — results and how each
was proved. `AGENT_BRIEF.md` — crop route and output conventions.
Tooling: `extract.py` (glyph inventory), `cluster.py` (k=340, deterministic, so
`labels.py` survives a rebuild), `wstrip.py` / `gmont.py` / `chunk.py`
(reading images at three magnifications), `classify.py` + `pdec.py` (a ~77%
k-NN draft, a scaffold only), `tmatch.py` (find one glyph everywhere in
context — this is what exposed the null). Raw Gallica pages are not tracked.

## Next step

No. 65 is transcribed throughout; its remaining uncertain patches (chiefly
f. 119v L25–37 and f. 120r L01–L19) should be settled against no. 66, where
much of that matter stands in clear. Then no. 63, the longest and most heavily
enciphered of the three, including its final leaf f. 123 (found in the sormano1529 work, bound out of order).

## Outcome disagreement with sormano1529 (22 Sept 2026, site review)

This target and `targets/sormano1529/` cover the same three letters (nos. 63, 65, 66). This profile says class read, fraction
unknown; `targets/sormano1529/profile.json` says read in part, 0.05. The two records should be reconciled into one outcome
the next time either is worked; not reclassified in the review, by decision.

**Resolved 14 Oct 2026:** merged into this entry; see the head of this file and ## Outcome, reconciled.

## Glyph-level XML (24 Sept 2026, pilot for George Lasry)

`xml/no63.xml`, `xml/no65.xml`, `xml/no66.xml`, made by `python tools/transcription_xml.py sormano` from the
`n6x_transcription.md` files: one `<g>` per cipher glyph (3,131 / 3,888 / 1,249), in `<page>`, `<line>` and `<w>`,
with `cert="low"` wherever the Markdown has `{..}` or `(?)`, `type="null"` for (ɦ)/(ﬀ), `type="code"` for ◎ = DUCA,
and `<gap>` for unread stretches. The Markdown records decoded letters, not sign labels, so the XML has readings and
certainty but no sign identity. It has no coordinates either: no bounding boxes were stored.

## Outcome, reconciled (14 Oct 2026)

The two old profiles disagreed (this one "read", fraction unknown; sormano1529 "read in part", 0.05 estimated).
From the evidence in both folders, judged per document:

- **No. 65** (ff. 119–120): read. Transcribed throughout (`n65_transcription.md`, 3,888 glyphs in `xml/no65.xml`,
  205 marked low-certainty, no unread stretch); about a dozen words stay (?) or in braces (foot of f. 119r, foot
  of f. 119v, f. 120r run).
- **No. 66** (ff. 121–122): read; 1,249 glyphs in `xml/no66.xml`, 12 short unread stretches; the clear twin of
  no. 65 controls most of it.
- **No. 63** (ff. 115–116, 123): read in part. On ff. 115–116 the clear text and the shorter cipher runs are read
  but the long runs of ff. 115v–116r only in patches (252 unread stretches in `xml/no63.xml`; their length was not
  recorded, so no token fraction can be measured). The third sheet f. 123r, found by Patel, was deciphered on
  14 Oct 2026 with the same key (`n63_f123r_reading.md`): about 386 of 389 cipher glyphs give Italian, three signs
  before *ricaduto* do not. It ends the letter on Naples and the captaincy, and its postscript reports letters from
  Rome of the 18th: the Pope has relapsed, *sensa speransa di salute*, and the French cardinals should make ready
  for a conclave (Clement VII's illness of early 1529).

So the entry is **read in part** (no. 63 is not read in full), method read with known key (Lasry's key for the
volume, verified on the glossed no. 62 and on no. 67). `fraction_read` stays unknown: the transcriptions record
decoded letters with unread stretches of unrecorded length, not sign counts. Patel's 0.05 was an estimate made
before the transcription here existed.

Point to recheck: on f. 123r the crossbarred long-s behaves as a null three times (*q(f)uello*, *qu(f)elli*,
*pa(f)pa*), where KEY.md, from the f. 113r gloss, makes it a fourth *e*. The f. 123r reading drops it; KEY.md is
not changed until the sign is compared on the two leaves.

## Remaining gaps
- no. 63 ff. 115v-116r, long cipher runs read only in patches (252 unread stretches) - blocker: illegible; 44-60 px signs on the microfilm (MF 31394) whose i/o and other homophone forms differ by less than the film records (arya/NOTES.md 5b); segmentation merges and splits signs in runs with no clear word to anchor them; a new capture of the original would settle them
- no. 65, about a dozen words marked (?) or in braces (foot of f. 119r, foot of f. 119v, f. 120r) - blocker: illegible; same cause, the glyph strings are kept in n65_transcription.md
- no. 63 f. 123r, three signs before "ricaduto" (V 7 4 = a e i, no word) - blocker: illegible; read as written they give no word, and context alone is not used to fill them

## Escalation
- [x] siblings: nos. 62 and 67 (glossed) used as key controls; nos. 65/66 crib each other; no. 64 has no cipher; f. 123 found to be no. 63's third sheet (Patel) and deciphered
- [x] clear-pages: interlinear decipherment f. 113 and marginal decipherment f. 124 aligned; f. 116v "de Venetiani" gloss noted
- [x] known-keys: Lasry's 2023 key (Tomokiyo, francis.htm) applied; the Langeac-Passano Venice cipher of fr. 3000 f. 74 compared and is a different cipher
- [x] print: Molini, Documenti di storia italiana II, does not print nos. 63, 65, 66 (Patel); Tomokiyo lists them without decipherment; fr. 2974 f. 94 (Molini's printed decipherment of Sormano's 13 April letter) not digitised, and no longer needed for the key
- [x] key-rebuild: the null, the duca sign and four letter forms added to Lasry's table (KEY.md); Patel's independent 22 values agree on 20
- [n/a] retry: the open stretches are limited by the image, not by the key; running them again with the same key gives nothing new until a better capture of the leaves exists
