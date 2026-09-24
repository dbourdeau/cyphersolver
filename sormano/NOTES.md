# Sormano and de Vaulx to François I, Ferrara, February 1529

BnF français 3096, nos. 63, 65 and 66 (Gallica `btv1b9060015d`). The letters
concern Ferrara's defection from France before the Peace of Cambrai.

## Leaves and controls

| item | leaf / Gallica view | date | state |
|---|---|---|---|
| no. 62 | f. 113 / view 117 | 22 March 1529 | cipher with contemporary interlinear decipherment; key control |
| no. 63 | ff. 115–116 / views 119–121 | after 23 February 1529 | target; read as far as it goes, see `n63_reading.md`; final leaf is f. 123, bound out of order (sormano1529/NOTES.md), not read |
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

This target and `sormano1529/` cover the same three letters (nos. 63, 65, 66). This profile says class read, fraction
unknown; `sormano1529/profile.json` says read in part, 0.05. The two records should be reconciled into one outcome
the next time either is worked; not reclassified in the review, by decision.

## Glyph-level XML (24 Sept 2026, pilot for George Lasry)

`xml/no63.xml`, `xml/no65.xml`, `xml/no66.xml`, made by `python tools/transcription_xml.py sormano` from the
`n6x_transcription.md` files: one `<g>` per cipher glyph (3,131 / 3,888 / 1,249), in `<page>`, `<line>` and `<w>`,
with `cert="low"` wherever the Markdown has `{..}` or `(?)`, `type="null"` for (ɦ)/(ﬀ), `type="code"` for ◎ = DUCA,
and `<gap>` for unread stretches. The Markdown records decoded letters, not sign labels, so the XML has readings and
certainty but no sign identity. It has no coordinates either: no bounding boxes were stored.
