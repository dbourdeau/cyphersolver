# Vande Perre correspondence: expanded evidence audit

Research date: 19 September 2026. The published alphabet is convincing, but neither the
complete correspondence nor the two damaged readings has been exhausted. The strongest
new result is a specifically catalogued, unprinted cipher letter from the same sender to
the same recipient. Its digits have not been seen, so use of the published key is unproved.

## Newly identified manuscript evidence

1. **Bodleian MS. Rawl. A.7, old p.47: 17 October 1653, Van de Perre to Bruyne.**
   [Modern item record](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820123).
   Macray, *Catalogi*, part V fasc. I (1862), col.12, item 4, explicitly describes a copy
   partly in Dutch and partly in cipher, among the exceptions not printed by Birch.
   The actual catalogue scan was read independently: [scan n13](https://archive.org/details/CatalogiCodicumManuscriptorumBiblioth/page/n13/mode/1up),
   retained as `sources/macray-n13.jpg`. This confirms another cipher witness, not another
   decipherment and not yet another same-key letter. The catalogue does not state the date's calendar style.
2. **A.6 old p.195**, undated Dutch extract from Van de Perre to Bruyne:
   [item record](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820091),
   Macray col.11 item 10. **A.8 old p.88**, Dutch extract to Bruyne, 7 November:
   [item record](https://archives.bodleian.ox.ac.uk/repositories/2/archival_objects/820134),
   Macray col.13 item 2. These are precise parallel-language leads; no matching passage or
   cipher has been verified in them.
3. **Zeeuws Archief, access 2, inventory 3188**, J. de Brune, incoming letters 1652–1658,
   one folder. [Permanent record](https://hdl.handle.net/21.12113/7EE8C3AD46AB40FC882D10532E14648A).
   Verified in the current full EAD, under subseries 1.5.2.08 (J. de Brune, secretary 1644–49,
   pensionary 1649–58). The old 1922 reference is therefore still usable. The catalogue
   does not enumerate senders or prove that these specific letters or their key survive.
   The [IIIF manifest](https://proxy.archieven.nl/iiif/239/7EE8C3AD46AB40FC882D10532E14648A)
   has an empty `items` array; no manuscript images were obtained.
4. **Zeeuws Archief 2, inventory 3101.1**, England correspondence 1652–1656:
   [permanent record](https://hdl.handle.net/21.12113/22565F7402054D48A6003DDC0EFA75F3).
   Its scope note explicitly includes copies sent to the Gecommitteerde Raden by the
   three surviving envoys after Van de Perre's death in 1653. This ties the bundle to the
   actual embassy, but does not prove that private De Brune letters or cipher materials
   occur there. Its manifest also exposes no image canvases.

The Bodleian series description says its detailed catalogue generally lists items omitted
from Birch; foreign correspondence can survive in original-language copies and translations,
with only the translations often printed. Thus absence of a letter-level search result does
not imply a missing manuscript. No target manuscript was visually inspected. See the
[full Bodleian search report](../further-review/manuscript-search-aside.md).

## One further printed code candidate, in the reverse correspondence

Birch I, **p.552**, De Bruyne to Van de Perre, Middelburg 31 October 1653 NS, includes
`met 118` at the end of one line, followed by a retained Dutch phrase on the next.
The number 118 is clearly printed in the [page scan](https://archive.org/details/collectionofstat01thur/page/n581/mode/1up),
saved as `sources/thurloe-p552.jpg`. The marginal manuscript reference is **Vol.VII p.211**.

This is an additional unexplained number in the same exchange, likely a code group. There
is no gloss establishing its meaning. A single three-digit group cannot demonstrate which
key was used. It is recorded separately in `additional-witnesses.json`; it is not silently
added to the 20-run/322-group outbound inventory or mapped to a guessed person/country.
The nearby De Witt letter has 388 and 390; those must not be imported into this codebook
merely because they appear on the same printed page.

## The key-dispatch trail

Birch's dated letters give a focused place to search for an enclosure:

- 29 August, p.431 (MS vol.V p.226): Van de Perre says a cipher will arrive by a third hand.
- 5 September, p.442 (MS vol.V p.293): he says he sent a character with his preceding letter.
- 27 September: De Bruyne's acknowledgement is inferable from the 3 October reply;
  Macray independently catalogues a translated note from De Bruyne to Van de Perre on
  that date, **A.6 p.293**, col.11 item 24. Its text/enclosures were not inspected.
- 3 October, p.500 (MS vol.VI p.355): Van de Perre acknowledges safe receipt and asks him
  to examine the seal for tampering.
- 11 October, p.525 (MS vol.VII p.14): De Bruyne refers to the latest letter in cipher,
  criticizing the small amount of information it conveyed. This confirms actual use
  by the correspondents but supplies no alphabet.

An actual key has not been located. The dispatch does not establish whether an alphabet,
code list, or both was enclosed, or whether the 29 August passage used an earlier key.

## A necessary source-reference warning

The retained scan of Birch p.522 unmistakably prints **Vol.X p.471**. Both Macray and the
modern catalogue describe A.10 mainly as December 1653–February 1654. Macray places other
10 October 1653 letters at **A.6 pp.463 and 474**, which bracket 471. Therefore **A.6 p.471 is a
plausible alternative location**, not a verified correction. An image enquiry should give
both the literal Birch reference and this discrepancy. Do not simply order A.10 p.471 or
silently substitute A.6. Old pagination also needs conversion to current foliation.

## Printed-source coverage and negative results

- **Birch I,1742:** full-volume OCR searched for sender/recipient variants and numeric runs;
  the four reverse letters on pp.525,552,561,600 were read. The numerical screen found
  eight candidate runs with at least 12 groups and at least 85% coverage by the proposed
  alphabet; all relevant matches are already-known outbound passages. One match was
  ordinary article numbering, not a cipher. OCR breaks up some known runs, so this is
  explicitly a discovery screen, not proof of a complete page-by-page inventory.
  Code 118 was found by reading the reverse correspondence, not that numeric heuristic.
- **Colenbrander 1919, Bescheiden…zeeoorlogen I:** retrieved 152 OCR pages: the entire
  first-war section pp.1–94 (including page 62 b), prefatory pages, and pp.607–620.
  Searched all for Perre/Brune/Bruyne/cipher terms and inspected relevant hits, source
  notes and concluding first-war documents. No parallel text for the damaged October
  or November phrases was identified. The first-war documents actually end with
 12 September 1653. The two added Thurloe letters (nos.54–55, pp.85–86) are anonymous
  intelligence to Thurloe, not Van de Perre's letters to De Brune.
  Source: https://resources.huygens.knaw.nl/retroboeken/zeeoorlogen/1/1 .
  `sources/colenbrander-manifest.json` records exact URLs, byte counts and SHA256 hashes.
- **Gardiner/Atkinson, First Dutch War V–VI:** downloaded both public OCR volumes,
  searched correspondence/cipher terms and checked the series index in VI. The indexed
  De Bruyne letter is no.1240, VI p.72,23 September, explicitly reprinted from Birch I p.484;
  it is not an independent text of the damaged passages. No relevant alternative text
  was identified. Sources: https://archive.org/details/letterspapersrel05gard and
  https://archive.org/details/letterspapersrel06gard . This is a targeted search/index
  inspection, not a claim to have read every page of both volumes.
- **1725 embassy Verbael**, Google Books 545Vf-pifTMC: catalogue/viewer metadata and a
  positive in-book search for Perre were available. Search snippets include p.245's
  passport for the body of Paul van de Perre. Brune, Bruyne and fundament gave no search
  results; later queries returned 429, and normal browser access reached a verification
  page. The attempted EPUB was challenge HTML, not a book. This remains **incompletely
  inspected**, not a checked negative. Internet Archive catalogue searches for the title
  and author variants found no alternate full scan. The contemporary embassy journal
  remains a secondary priority behind the precisely identified cipher manuscript.
- **Macray catalogue:** complete OCR searched for Perre/Bruyne/cipher/key. The only
  specifically described extra Van de Perre cipher letter found is A.7 p.47. Two keys
  at A.33 pp.748 and 752 are late 1655; the first belongs to someone calling himself Archer.
  No evidence connects either to Van de Perre. They are low-priority, not a discovered key.
- **Digital Bodleian:** catalogue search found neither the requested source volumes nor
  target manuscript images; see the detailed report for exact queries/results/limitations.

Birch's own index calls the envoy **Paulus Vande Perre**. The NNBW biography also identifies the envoy as Paulus.

The [Zeeland search report](zeeuws-search-aside.md) records the complete inventory keyword
search, working catalogue links and the limits of the 2025 digitization programme. No
explicitly catalogued cipher key was found in inventory 2. The older DBNL reference is
on PDF page 197 (one-based), under 1922-01.

## What remains unresolved

The new evidence does not repair `diemnicvndament`, `ote`, the n/u ambiguity, or the
mechanism behind joined numbers. The earlier p.523 extension remains valid. Exact wording
and conjectural spelling are kept apart in the [earlier review](../further-review/README.md).

The best next step is images of **A.7 p.47**, then the two damaged passages and their Dutch
witnesses, followed by the two Zeeland bundles. A concrete retrieval specification is in
[ARCHIVAL-TARGETS.md](ARCHIVAL-TARGETS.md). No archive correspondence or orders were sent.
The repository reading incorporates the p. 523 runs; this audit records the wider search and its limits.

## Statistical-control audit

The discovery-corpus control reported z = 5.2 on 308 groups. Its caller mapped non-S
symbols to `#`, but did not pass them as fixed: the shared helper therefore shuffled these
single-character boundary values among letters. The current caller explicitly holds every
non-S symbol fixed. It also retains the helper's fixed multi-letter `ij` and `ee` values.
On the 322-group corpus the conditional comparison gives z = 18.0, p = 0.001 (1,000
shuffles, seed 0). This change of null makes the two z-scores non-comparable. Neither is a
search-adjusted significance test, a probability that the key is right, or evidence fixing
the damaged fragments. See `control-result.txt` and `../verify.py`.

The retained source manifests identify remote-only OCR files by URL and hash; large full
volumes are not duplicated here. `sources/zeeuws-inventory-excerpts.xml` contains the two
item entries extracted from the official EAD identified in `source-manifest.json`.
