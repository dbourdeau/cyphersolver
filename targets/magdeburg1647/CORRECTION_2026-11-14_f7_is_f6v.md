# Correction, 14 Nov 2026: our "f.7" is fol. 6 verso

**Our error.** In this folder (PR #524 and the R3 and blind4_b198 additions), the slip labelled **f.7** (frame 11, left page) is **not a separate slip**. It is the **verso of the slip foliated 6**: the second page of the same dispatch, "ad Diarium No. 32".

## Evidence [measured]
LASA A 1 Nr. 530, frames 10, 11 and 12. Each frame was fetched once by plain GET from `https://recherche.landesarchiv.sachsen-anhalt.de/images//A_1/Nr_530/max/A_1__Nr_530__NNNN.jpg` on 13 Nov 2026 at 23:11:56 UTC.

| Frame | md5 of image | What it shows |
|---|---|---|
| 10 | d355c2fc9424049551ae0d30d83d18b7 | f.6 recto |
| 11 | 71ca7037d62165d7b41ff2adc5cce7a5 | left page: the cipher we called "f.7" = **f.6 verso**; right page: foliated **7**, blank |
| 12 | 8fad95161d74cde1eefb1a8d7b882754 | left page: f.7 verso, endorsed "1647 ad Diarium No. 32" |

Two things agree with this:
- Our own Nr. 529 match: frame 882, left page, fol. 807v continues the draft of No. 32 (see `PRIOR_ART.md`).
- Perplexity's independent frame sweep made the same point first. We checked it on the images before accepting it.

## What changes
- **Labels only.** Read every "f.7" in this folder (file names, NOTES, ledgers, readings, translations, controls) as **f.6v**.
- **File names are deliberately left unchanged.** They are inside frozen manifests and RFC 3161 tokens, and renaming them would break the hash chain.
- **Slip count.** The open set is **four distinct slips plus f.6v** (f.5, f.6r-v, f.101, f.102, f.104, f.204), not "five slips".
- **The b160 held-out test of KEY_v2 on "f.7" was weaker than described.** It held out another page of the same dispatch as f.6r, not a separate letter. The key confirmation does not depend on it: the Catalogus, the glossed postscript, the frame 168 worksheet and the enciphered Nr. 529 drafts each confirm the key independently.
- **No figure changes.** Every count stays as filed.

## Also new since #524 (prior art, f.204)
f.204 ("Annotata ad Num. 40", frame 233) lies inside the frames 226-259 Annotationes run that we linked to the margin notes of the Nr. 529 diary. Diary No. 40 was outside the ranges we searched. f.204 prior art is therefore **not cleared**. We are checking Nr. 529 No. 40, the Nr. 545 fair copy and Nr. 546, and will report in a follow-up.
