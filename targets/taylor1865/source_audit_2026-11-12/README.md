# Source audit: Taylor/Surget, January18 and April10–11,1865

This is a partial source-reading addendum. It promotes no complete reading, new key, or whole-text percentage. Original target ciphertext/key/profile files are unchanged. Local improvements with known keys supported by the images are **CONTENT** and **THE**; **SENT** depends on reading EIEX rather than FIEX (which gives TENT) and is open. Other glyphs and endings remain uncertain. The large original images and all prior February contributions are outside this payload.

## Evidence and review limits

`JANUARY_READERS.tsv` preserves two context-aware AI source readings of the13 final groups (54cipherletters) of January18, NARA chapterIIvolume10frame0056 MS107. `JANUARY.tsv` adds exact continuous positions and old/new fixed-key literal outputs. Both readers prefer ODYXXRO, yielding CONTENT with COMPLETEVICTORY at phase2. They disagree FMNA/FMNQ; both prefer NEFM despite its worse fit with proposed TROO. No word is repaired from context. Root reviewed the crop before opening proposed values, but the prior interpretation and cleartext context were not hidden from the whole investigation. This was not a blind experiment or human paleographical certification.

`APRIL_SOURCE_FIRST.md` was recorded before the author reopened the old April transcripts in this pass; its visible uncertainties and minor initial descriptive error are preserved. `APRIL_RECONCILIATION.md` records the root's image-only corroboration and disagreements. Root's April10 final groups GJS EX FVWJ JMNH agree with the author, confirming THE but leaving ST ORDS BLTO unread. The earlier EIEX→SENT is the author's source reading, not independently certified by root. Source first JMNH has four glyphs versus prior JMNCH5. Other earlier candidate letters are explicitly unverified comparison scaffolding, not a complete revised transcription.

The April11 source has unresolved SV/SJ, M/N, E/F and gutter/length questions. `APRIL_MECHANICAL.tsv` includes the three April10 comparisons and225 April11 standard-Vigenere literals (3 variants ×5 existing keys ×15 phases). No plaintext is accepted. The already-reported November9 broader convention search on the author's unchanged terminal candidate is prior work, not repeated or claimed here. These failures do not prove a different key/system or exclude missing letters. The check below reproduces arithmetic and records; it does not automatically judge English or certify a solve.

## Reproduce

From repository root, standard-library Python3 only:

```
python3 -I targets/taylor1865/source_audit_2026-11-12/check.py
```

To verify the original-image evidence, reacquire the3 public URLs recorded in `SOURCES.json`, save the files under the listed filenames in a directory outside the repository, and run:

```
python3 -I targets/taylor1865/source_audit_2026-11-12/check.py --images /absolute/path/to/originals
```

A reproducible optional downloader using only public URLs (no login or preview bypass):

```
python3 -I - targets/taylor1865/source_audit_2026-11-12/SOURCES.json /absolute/path/to/originals <<'PY'
import json,sys,urllib.request
from pathlib import Path
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
for row in json.loads(Path(sys.argv[1]).read_text())['assets']:
    target=out/row['path']
    if not target.exists(): urllib.request.urlretrieve(row['url'],target)
PY
```

If the archive changes bytes, record the new witness separately; do not silently update expected hashes. Files are JPEGs and exact originals were used. Optional viewing crops use original pixel coordinates `(left,top,right,bottom)` and simple grayscale/autocontrast; no generated or reconstructed marks:

|Frame|Crop|Box|
|---|---|---|
|v10-0056|January suffix|(3500,2200,6100,3100)|
|v11-0045|April10 telegram|(710,2230,3480,3350)|
|v11-0045|April10 ending|(720,2830,1770,3100)|
|v11-0046|April11 lower telegram|(720,2340,3510,4040)|
|v11-0046|April11 ending|(1650,3330,3470,3640)|

## Remaining witness work

The earlier investigation (12 November 2026) read Davis Papers volume11 p339 in the publisher-authorized Google Books preview; it cites the same NARA bookcopy (chapter2 volume10:107), and its printed opening agrees with the existing provisional reading. The image is kept locally, not committed. P340 was not acquired/read; do not treat the modern edition as an independent contemporary clear duplicate. [Official publisher](https://lsupress.org/9780807129098/the-papers-of-jefferson-davis/) offers the authorized ebook ISBN9780807158920. [Tulane's official guide](https://libguides.tulane.edu/c.php?g=528385&p=3612964) lists Davis microfilm2012-0192reel14 with incoming telegrams fromJanuary1,1865; the exactJanuary18 item has not been located. Both are concrete next access paths, not claims of an existing clear counterpart. No purchase, contact, or order was made in this audit.
