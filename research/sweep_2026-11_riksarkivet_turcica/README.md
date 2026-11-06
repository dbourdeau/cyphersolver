# Riksarkivet Diplomatica Turcica and Polonica, volume pass (5 Nov 2026)

Source key `riksarkivet_turcica`. Goal: finish the volume-level pass over every digitised Turcica and Polonica volume that the
two earlier Riksarkivet sweeps (`sweep_2026-11_riksarkivet_volumes`, `sweep_2026-11_D_east_north`) left unsheeted, above all
the 1709-14 Bender run that sweep D recorded as "no IIIF manifest". **5 rows** in `candidates.json` (`make_candidates.py`);
the per-volume record is `findings.md`.

## The route that was missing

The Bender run (Turcica I/4/5 to I/8/19 and III/96) and three Polonica volumes are digitised in a separate image series
(`40006060` to `40006085`, `40008933` to `40008936`). They have no IIIF link in the record's `.jsonld` any more, which is why
sweep D logged them as manifest-less.

1. The image-series id is in the **APE EAD**: `https://oai-pmh.riksarkivet.se/OAI/?verb=GetRecord&identifier=<ref>&metadataPrefix=oai_ape_ead`,
   element `<dao xlink:href=".../bildvisning/<id>">`. The `oai_ra_ead` form has no `<dao>`. Pass the reference code with its
   slashes unencoded (`requests` `params=` encodes them and the server then finds nothing).
2. `lbiiif.riksarkivet.se/arkis!<id>/manifest` and the images return **403 to scripts** unless the request carries
   `Referer: https://sok.riksarkivet.se/`. With that header they open with curl or `requests`; no cookie, no Chrome. The
   `Origin` header alone does not work. The R000xxxx series still opens without a Referer.
3. `rik_common.py` holds the helpers (`dao`, `count`, `img`); `build_units.py` writes `units.json` (100 volumes, 33,285
   images); `batch.py` / `rik_sheet.py` make 24-image contact sheets; `rik_pick.py` fetches chosen images at 900 px.
   About one request a second. The sheets themselves sat in the session scratchpad and are not kept.

HTR text: the viewer offers `download/current/text/...` but it returns 404 for these volumes, so there is still no
full-text route into Diplomatica.

## Result

75 volumes sheeted (every Turcica and Polonica volume with images that earlier sweeps had not sheeted), 24 images each, suspects
re-fetched at 900 px. Cipher seen in nine volumes, which make five rows:

| Row | Volumes | What is there |
|---|---|---|
| Poniatowski to Charles XII, 1710-14 | Turcica I/5/8 | French letters with number-cipher runs, French decipherment between the lines |
| Bender field-chancery code, 1710-14 | Turcica I/6/9, I/6/10, I/6/14, I/7/16 | one 2-3 digit code (Funck, Perman, von Müllern), interlinear Swedish/French decipherments; key material for catalogue **#1769** (Funck I/6/13, the same code unglossed) |
| Rålamb and Vellingk, Constantinople 1657 | Turcica I/2/2 | Swedish despatches, small-number code, interlinear decipherment |
| Cantersten, Poland 1648 | Polonica I/5/17 (drafts I/5/18) | Swedish despatches, small-number code, interlinear decipherment |
| Molinari, consul at Tunis, 1765-70 | Tunisica 7/2 | French letters in unbroken digit strings, **no decipherment seen**: the one ciphertext-only row |

The four glossed rows are class A: a key can be rebuilt from the pairs, and the Bender code then applies to #1769. The Funck
drafts (I/6/11, I/6/12) are clear and may give cribs for unglossed letters.

## Sheeted, no cipher seen

Listed volume by volume in `findings.md`: Neugebauer 1709-11 (I/4/5-7), Funck's drafts, Grotthuss 1714 (I/8/17-19), III/96 to
III/107, Höpken's report I/9/30, Heidenstam/Brentano I/13/74, Strasburgk 1634, Sternbach 1656-57 (5/3), the Algerian, Tunisian
and Tripolitan consular volumes (except Molinari), and on the Polish side the Lübeck commission 1651-53 (I/6/19-25), Pels, Kock,
Dörffler 1671-79 (I/12/61-62), Arenstorff 1669, Wachschlager 1694-1714 (I/20/104-105, I/22/108, I/26/130-131), von Storren
1697, Stanisław Leszczyński's letters (III/8/326) and the Polish memorials (III/9/328 A, B). A 24-image sample per volume only
catches volumes where cipher is common: "no cipher seen" is not "no cipher".

## Not reached

- Pages beyond the sample in the nine cipher volumes: each needs paging for a full list of cipher letters.
- The 1709-14 volumes' sister series outside Turcica (Kanslikollegium, Cosacica beyond sweep D's rows) and the Stedingk,
  Barthelemy, De la Gardie, Tessin and Reuterholm fonds named in the earlier sweep.
- Muscovitica, Gallica, Italica, Hollandica volumes: sweep D made sheets but never viewed them; they can now be rebuilt with
  `rik_sheet.py` (same Referer route if any are 4000xxxx).
- DECODE, Tomokiyo and Lasry were not searched for these rows; web search found no edition or decipherment.

## Vetting pass (5 Nov 2026, same day)

`vet.py` writes the vetting blocks; prior art (DECODE dump, cryptiana, Lasry, editions, literature) found no decipherment,
edition of the cipher letters or printed key for any of the five.

| Lead | Outcome | Why |
|---|---|---|
| 2258 Rålamb 1657 | **promoted** to catalogue | bare number runs on images 104 and 114 beside glossed letters (18, 22-23, 74, 77, 87-88) |
| 2257 Bender code | closed `read` | every passage seen is glossed; recorded as crib material on catalogue **#1769** (`vetting.key_held`) |
| 2256 Poniatowski | closed `partly_read` | glossed throughout except 10-15 tail lines; cipher in images 253-335, May-Oct 1712, plus a letter cipher "de Mr de Grothus" |
| 2259 Cantersten | closed `partly_read` | one glossed letter (images 9-11), a few bare rows |
| 2260 Molinari | **held** (`vetting.pending`) | 16-18 pages of bare digit cipher, but image 365 is marked "Dubbletten dechifferad" and Jerad's 2015 edition (unseen) may print the text |

Possible held keys, untested: DECODE R4201 (Chifferklaver låda II 82, 1657) and R4195 (1658) for Rålamb; R4160 and R4172
(1648) for Cantersten.
