# Vetting, Daniel Bourdeau (2026-11-16)

**Ids.** This vetting was written against the ids 2931-2933 that the branch gave the sweep's rows. When the sweep was merged
into `research/leads.json` on current main (16 Nov 2026, after the merge of the Africa sweeps) the rows got fresh ids:
**2933 is now 2943** (Sachau 218), **2932 is now 2942** (Gotha), the vetted Sacromonte row **2930 is now 2941**, and row 1
(Gordon's note, **2931** below) was not merged at all: it is the same document as catalogue 2939 and `targets/gordonmudir1884`,
which main now holds, so it is excluded in `archive_sweep_2026-10/exclude.json`. `vetting.json` is keyed by the new ids and no
longer carries the 2931 note, which is kept below as written.

**2943's extent.** `vetting.json` for 2943 (and the promoted catalogue entry's `vetting.seen.extent`) still carries the vetting's
estimate of 120-160 signs, counted from the crops. Brice Dudout's count on 16 Nov 2026 (comment on PR #706, with Claude Opus 5.5) is
59 signs of 26 shapes in about 13 groups; the catalogue entry's status gives it. A promoted entry cannot be re-vetted through
`vet.py --apply`, so the extent field is left as vetted.

Run by Daniel Bourdeau with a Claude Code session (Claude Opus 5.5), 16 Nov 2026, following `research/VET.md`. Leads
from the Arabic sweep 2 of 16 Nov 2026 (`research/sweep_2026-11-16_arabic_2/`, parts B and C). Open issues and pull
requests searched for each id and for Gordon, Sachau and Gotha before starting.

## Leads

- **2933, Berlin Sachau 218 f. 231a: `open`.** Seen at native size (SBB IIIF, 2048 x 2853 px; image 467 = f. 231r
  in the METS): four underlined lines, roughly 30-35 word groups, of Syriac letter forms mixed with numeral-shaped and
  invented signs, joined like cursive Serto, some with red diacritic dots. No gloss or key on 230v, 231r or 231v.
  Sachau 1899 no. 188 quoted, no reading; DECODE, Tomokiyo, Lasry and literature searches found nothing. Key material
  to try (untested): the Syriac secret alphabets Sachau describes elsewhere (catalogue pp. 338, 552, 706, 717, 794, 803,
  807, 808) and the sibling Sachau 221 f. 20b. Plaintext language (Syriac or Karshuni) not judged. SBB dates the volume
  17XX. Access set to online.
- **2932, Gotha Pertsch no. 2507 (end leaf, "Notiz in Geheimschrift"): `unvetted`.** Leaf not seen. Pertsch vol. 4
  p. 373 re-read and confirmed. Shelfmark form Ms. orient. A 2507 still not confirmed.
- **2931, Durham SAD.250/1/550, Gordon to the Mudir of Dongola: `unvetted`.** The same leaf is lead 2873 and target
  `gordonmudir1884` in open pull request #591 (14 Nov 2026, not merged; its ids clash with main, where 2873 is a
  different lead), which vets it, promotes it and writes it up as attempted, not deciphered. Close this lead as a
  duplicate once #591 merges. The TNA question is settled: PRO 30/57/4/26 translates 4/27, a message from Major Rundle
  at Korosko dated [Sept 1884], and PRO 30/57/3/11-12 [Sept 1884] is Arabic script with a partial translation about the
  same loan. Neither is Gordon's note of 16 Muharram 1302 (Nov 1884), so no decipherment of SAD.250/1/550 is known.
  Key leads for the Gordon/Kitchener Arabic cipher (none digitised): PRO 30/57/4/26-27, 3/11-12 and 4/77-78 ("Please
  use Arabic cipher", 24-25 Aug 1884). I did not view the Durham image again, because the verdict does not depend on it.

## Routes

- Worked: SBB `content.staatsbibliothek-berlin.de` METS and IIIF full images (curl); archive.org djvu text (Sachau
  1899 vol. 2, Pertsch vol. 4); TNA Discovery API through `research/tna_discovery/tna.py`, plus
  `/API/records/v1/details/<id>` and `/API/records/v1/children/<id>` (searching by reference returns nothing, but
  searching by keyword finds the record id); cryptiana over https (Shift_JIS); K10plus SRU (the index names are
  `pica.xall`, `pica.xsgb` and so on: `pica.sgb` gives "Query feature unsupported").
- Blocked: dhb.thulb.uni-jena.de and collections.thulb.uni-jena.de redirect to a proof-of-work page
  (`rep-pow-challenge`), which I did not pass. The DDB API returned 403 (needs an API key). qalamos.net did not connect.
  K10plus has no record found for Ms. orient. A 2507.

## Left

- 2932: a person in a browser on the Gotha/Erfurt viewer, or a scan order to the Forschungsbibliothek Gotha for the
  two leaves at the end of the volume.
- 2931: close as a duplicate when #591 merges.
- 2943 (was 2933): compare the Sachau secret alphabets (pp. 338 ff.) and Sachau 221 f. 20b; decide whether the plaintext is
  Syriac or Karshuni.
