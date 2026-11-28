# hab123blank: notes

This is catalogue 3807: ciphered recipes on the last leaf of a recipe book in Wolfenbüttel.
- **Shelfmark:** Herzog August Bibliothek, Cod. Guelf. 123 Blank., f. 59v, scan 00120. The facing index of recipes is scan 00119.
- **Status:** read in part. The key K1 is **not validated**: the held-out measure failed (0.406 < 0.503; see prereg/RESULT.md).

## Prior work and credits

- **Catalogue:** Hans Butzmann, *Die Blankenburger Handschriften* (catalogue of the Herzog August Bibliothek), p. 131, as quoted in the HAB online catalogue.
  - He reports the cipher on the last verso and in some earlier recipes, without a reading.
  - He is credited for the identification of the cipher.
- **Pointer:** the catalogue entry 3807 (Codex vetting, 23 Nov 2026) supplied it. No mapping had been tested there.
- **Images:** Herzog August Bibliothek Wolfenbüttel, http://diglib.hab.de/mss/123-blank/start.htm?image=00120.
  - The images were studied from the HAB's full-resolution files (max/00119, max/00120), fetched on 27 Nov 2026.
  - The scan bears a CC BY-SA badge in its footer, but the licence was **not confirmed** on a HAB web page.
  - So **no image or derivative is included in this folder**.
- **Earlier decipherments:** none found. The checks covered DECODE, Tomokiyo's list, Lasry's inventory, the catalogue, the leads, and the open pull requests and issues.

## System

K1 is a simple substitution:
- **Vowels** move one place: a→b, e→f, i→k, o→p, u→x.
- **Consonants b to m** are numbered: b=1 (written like j), c=2, d=3, f=4, g=5, h=6, k=7, l=8, m=9. The value k=7 is attested only in *schlacken* (L31).
- **Other letters:** n→o, p→+ (a cross-shaped t), r→t (a tau-shaped t) or r, s→d, t→c (also e), q→q.
- **Word division:** words are divided, and the cipher alternates with clear Latin and German.
- **Unresolved signs:** the big z (rare, with contradictory values) and the 4-shaped q (= f in *perfecte*, not separated from q in the transcription) are left open.

## How the work was done

1. Two blind transcription passes were made by AI agents, with no key hypothesis: blind/PASS-A.txt and blind/PASS-B.txt.
2. A third agent arbitrated their 38 discrepancies on enlargements. That agent had not seen the key.
3. The key was built on lines L01–L18 only. Line L18 was decoded while the key was being built; it lies outside the held-out portion, and this is declared in the PREREG.
4. The freeze was posted on #1023, and then the single measure was run: it failed.
5. The reading by sense of the whole page comes after the measure: reading.md and reading.tsv.

All work was done by Claude Opus 5.5 agents run by Brice Dudout.
