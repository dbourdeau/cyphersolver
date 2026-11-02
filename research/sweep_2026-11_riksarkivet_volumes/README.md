# Riksarkivet digitised volumes (Diplomatica), 2 Nov 2026

Source key `riksarkivet_volumes`. Goal: find digitised envoy volumes with number cipher that is not glossed. **5 rows**
in `candidates.json` (built by `make_candidates.py`), well short of the 60 asked for. Not padded.

## Method

1. NAD API `https://data.riksarkivet.se/api/records?text=<caption>&only_digitised_materials=true&max=100` (send
   `User-Agent: curl/8.0`; the parameter is snake_case, the camelCase `onlyDigitisedMaterials` is ignored). 44 generic volume
   captions ("Brev till Kungl. Maj:t", "Depescher", "Koncept", "Envoyen" ...) gave 457 digitised units in Diplomatica,
   Stedingk, Barthelemy, Ericsberg, De la Gardie, Tessin, Reuterholm and other fonds. Diplomatica proper: Turcica 59,
   Polonica 32, Muscovitica 20, Gallica 11, Hollandica 8, Italica 5, Anglica 3, others fewer. Only a subset of Diplomatica
   volumes is digitised.
2. Per unit: `data.riksarkivet.se/archive/<id>.jsonld` for the IIIF manifest id, then the manifest for the image count.
   186 selected units resolved (`info.json` in the session scratchpad, not kept).
3. Contact sheet per volume (24-36 images sampled evenly, 330 px each), viewed by eye. About one request a second to
   lbiiif, one every 2.2 s to data.riksarkivet.se. Only 15 volumes were sheeted before the sweep stopped.
4. `known.py` run on Funck, Hopken, Dorffler, Wachschlager and the shelfmarks: no hits.

## Findings

- **Confirmed cipher, five volumes**: Turcica 6/13 (Funck 1711-13), 9/20 and 9/21 (Hopken and Carlson 1734-41, the densest),
  Polonica 19/100 and 19/102 (Dorffler 1680-89). The catalogue never says "cipher" for any of them, which is why the
  title/note searches of the October sweep (`research/riksarkivet`, `research/scandinavia`) missed them.
- **Sheeted, no cipher seen**: Tatarica 4/1 and 4/2, Transsylvanica 5/2 (image 35 doubtful), Polonica 19/101, 19/103, 22/109,
  Courtin 1657-60 (Gallica 11/14).
- Dense dark text blocks on a thumbnail are not a safe sign of cipher: Polonica 19/103 image 267 and 22/109 image 48 were
  checked at full size and are clear Latin and German. Only visible number rows count.

## What blocked

- **No full-text route.** `transcribed_text=` (HTR search; needs `only_digitised_materials=true`) covers court and mining
  records only. Diplomatica has no HTR: Courtin, Mazarin, Strasburgk, Dorffler return nothing from it.
- **No bot check**, no Chrome needed.
- **Scale.** A Diplomatica volume is 300-1,000 two-page images; a 1-in-12 sample catches only cipher-heavy volumes, and I
  could not screen by script (no OCR on this machine).

## Not reached

About 170 of the 186 selected digitised units, in particular: Polonica 12/60-62 (Dorffler 1667-72, 785-1,065 images),
22/108-110 and 20/105-106 (Wachschlager), II/2/247, II/3/248-249 (Pels, Kock); Hollandica 5/7 (Camerarius 1626-30) and
Grotius's 7/8; Gallica 24/54 (Bonde 1674-78); Muscovitica 36/82, 45/115, 47/118, 55 (Cederhielm), Cosacica 1a; Italica 5/4-6
(Piranesi 1782-1800); Turcica 6/9, 6/11 (Funck), 4/5-6, 8/17-19 (Neugebauer, Grotthuss), 9/29 (Beskickningshandlingar);
Maroccana and Tunisica consular volumes; the Stedingk (104 units) and Barthelemy (91) fonds; De la Gardie, Tessin, Reuterholm.
The unreached Turcica and Polonica volumes of the same envoys are the best next pass: cipher is regular there. Oxenstiernska
samlingen returned no digitised volumes through these captions. Rigsarkivet TKUA was not tried here (see `research/scandinavia`).
