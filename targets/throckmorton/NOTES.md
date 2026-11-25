# Throckmorton: BL Add MS 4136, twenty DECODE records

Status: in progress — published counterparts found; archived key verified on two samples

## Result, 20 September 2026

See [RESULT.md](RESULT.md) for the evidence and limitations, and
[CONCORDANCE.md](CONCORDANCE.md) for the twenty-record source concordance.
The first complete numbered extract on R9220 reads **all be it i be revoked or
the warr breake** with R9262's third cipher; Forbes I (1740), p.355 agrees.
R9230's opening gives **orleans or burges**, matching Forbes II (1741), p.12.
These checks cover 27 and 15 tokens respectively, with replayable JSON.

The downloaded target material has 54 image references but 39 unique JPEGs;
four nearby key records add 17 images. Full hashes and record mappings are in
`verified_inventory.json`. Most of the twenty edition matches have not received
a complete token alignment. R9255 is composite, and its other writers remain
outside the verified Throckmorton match. This is a prior-solution finding, not
twenty new decryptions. R2988's marginal cipher and R2989's John Wod material
remain separate, unresolved targets.

The working profile has been brought up to date from the existing dossier;
the starting log below is preserved as a record of the initial state.

## 2026-09-20: starting evidence

Objective supplied by the user: investigate twenty records R9220–R9255 attributed to
Throckmorton, retrieve images and related keys, and compare published decipherments.
The range is not consecutive: other correspondents occur between these records.
`records.json` preserves the locally harvested metadata for this manuscript, including
adjacent records for context. Catalogue dates are not yet normalized or verified.

The local copy `../../unsolved.htm`, under Nicholas Throckmorton, explicitly says Tomokiyo
reconstructed three ciphers. Its two unresolved cases are R2988 (marginal ciphertext)
and R2989 (John Wod, 1568), outside this twenty-record set. The supplied objective's
remark on two-digit superscripts belongs to the preceding Serno Gilino section and
must not be treated as evidence about Throckmorton.

DECODE pages failed in the web tool. The user pointed out an existing DECODE cookie;
located the repository's git-ignored cookie file and existing download convention.
No ciphertext image has yet been read; no plaintext is claimed.

## Access, corpus and provenance (later in the same session)

The cookie worked after the sandbox network restriction was escalated. Downloaded
all 54 image files attached to the twenty target records. SHA-256 comparison gives
**39 unique images**, not 54 independent pages. `image_manifest.json` records the
duplicate groups. R9220 and R9221 are byte-identical; many later records share their
boundary leaf with the next record. Images remain local and git-ignored.

Retrieved all four key records mentioned in the objective: R9262 (11 images), R9260
(3 images despite a two-page metadata count), R9261 (2), R9257 (1). R9262 is headed
"Sir Nicholas Throckmorton's third cipher". R9260 contains the first and second;
the other records concern other correspondents and are not four alternative
Throckmorton keys.

The British Library's own catalogue identifies this volume as **Forbes Papers V**,
with tracings or facsimiles on ff.1–171 and keys later in the volume:
https://searcharchives.bl.uk/catalog/040-002109587 . These are not to be described
as twenty newly discovered autograph originals. Nor has the dating or authorship
of the archived reconstructed key been independently established here.

## Verified short control

`control.json` transcribes 27 cipher tokens in f.110 extract (6), including two
nulls. `decode_control.py` applies values from the archived third cipher and emits:

> all be it i be revoked or the warr breake

Grade H: values read from the primary key source; the contextual u/v choice and
word spacing are editorial. The source is the continuation of the 7 March letter
to Cecil, on a leaf which also includes the 8 and 9 March letters. Forbes I (1740),
p.355 independently prints the corresponding clause. The initial visual reading
"wars" was wrong: the last numeric sign is another r homophone, giving "warr".
This correction is retained in the control's provenance. The 27-token count was
measured with `docs/_check_profile.py --measure targets/throckmorton/control_tokens.txt`.
It is a control length, **not the length of R9220 or of the corpus**.

The August 5, 1562 leaf f.133, extract (1), contains the spelling ORLEANS OR BURGES
and place codes matching the passage about forces being applied against Rouen,
Newhaven and Dieppe. Compare Forbes II, the August 5 letter (pp.28–35), and CSP V
no.425 paragraph 11. CSP no.426 explicitly records a separate decipherment.
The two short controls now have machine-readable token transcriptions, totaling
42 tokens; neither constitutes a full-record transcription.

## Published counterparts and source distinctions

`CONCORDANCE.md` / `concordance.json` map all twenty records to candidate published
counterparts, using manuscript dates, addressees and the checks stated per row.
`PUBLISHED_REFERENCE_TEXTS.md` supplies the historical Calendar entries, labelled
as copied reference texts rather than new decipherments. The Calendar is often an
abridgment and cannot be silently substituted for a diplomatic transcription.
Forbes I and II OCR are cached locally under `sources/`; exact pages should be
checked against print images before quoting uncertain OCR spellings.

The direct HTTP downloads succeeded where the web tool failed. `fetch_public.py`
sends no cookie; the DECODE cookie is only sent to de-crypt.org by `fetch_sources.py`.

Tomokiyo's `elizabeth.htm` explicitly describes three reconstructed ciphers and
locates the archived keys (November 2024 update). His still-unidentified items are
R2988's margin and R2989's John Wod text, outside this twenty-record group. The
catalogue incorrectly imported his unrelated superscript comment into this group.

R9255 is composite: Thomas Smith on f.169; Throckmorton to the Queen, Essone,
22 November 1562 on ff.169–170; Mr Somer to Cecil, Bonneval, February 1562/3 on
ff.170–171; Randolph to Cecil, Edinburgh, February 1560/1 on f.171. Thus Edinburgh
is not evidence that this Throckmorton series originated there, and "Lomer" in the
metadata appears to be Somer. The Throckmorton portion corresponds to CSP V
no.1099; no.1100 explicitly records the deciphered copy. The non-Throckmorton
portions are not yet decoded in this session.

## What remains

This is a successful archive-key control and a source concordance, **not a complete
decryption of twenty records**. Most concordance rows are date/addressee matches;
the full ciphertext has not been checked token by token. No corpus fraction-read
is claimed. Next: transcribe the complete third key, align the numbered extracts
against Forbes and the Calendar, flag omissions and mismatches, and handle the
additional Smith/Somer/Randolph portions under their own keys. Keep the catalogue
entry open while that full audit remains unfinished. No new cryptanalytic break
or previously unknown historical content is claimed.

## 14 Nov 2026: full-texts audit, the missing transcription

Eighteen records were listed without a transcription (R9221-R9229, R9231-R9234, R9242-R9245,
R9255). In order: (1) the folder has token files only for one extract each of R9220 and R9230
(`control_tokens.txt`, `control_9230_tokens.txt`); (2) each DECODE record (public API and record page, fetched
today one at a time) carries images only, no transcription or document; cryptiana `elizabeth.htm` gives the key
reconstructions as images, no transcription; (3) the images could not be fetched: DECODE serves the images of this record only to a signed-in session (an anonymous request to `decrypt-custom/filesrv` returned the `forbidden.png` placeholder, 17,947 bytes; the 200 px thumbnails are public and useless for signs). No DECODE session is available in this checkout and the images an earlier session fetched were git-ignored and are gone. So `transcription_missing` is
recorded on the 18 entries. What unblocks it: the images through a DECODE account, then a transcription against a
sign inventory for Throckmorton's ciphers (DECODE R9260 and R9262), checked by decoding against Forbes's text.
Nothing else changed.
