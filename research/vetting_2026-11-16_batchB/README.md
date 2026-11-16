# Vetting batch B, 16 Nov 2026 (wave 19)

Proposals only (`proposals.json`, built by `make.py`). `research/leads.json` and `catalogue.json` were not touched; nothing
was promoted or committed. All 10 vetting blocks pass `_check_catalogue.vetting_problems` on shape. The only remaining
problem is the expected one: a verdict other than open does not enter the catalogue.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2826 | read | high | BnF notice of fr. 3702 (cc501463): every cipher piece is "avec chiffre et dechiffrement", except no. 52 (f. 146, 24 Sept 1625). Not on Gallica. |
| 2827 | read | high | fr. 3673 (cc501246): all 28 cipher pieces are filed with their decipherment. Not on Gallica. |
| 2828 | read | high | fr. 3703 (cc50147b): all 18 are "avec dechiffrement". Nos. 22-23 read "chiffree avec chiffrement", probably a cataloguer's slip. Not on Gallica. |
| 2726 | **open** (rescoped) | medium | The lead's shelfmarks are wrong. The pieces are fr. 3541 (1603: catalogue 23 / breves1603) and **fr. 3654** nos. 6, 8, 11-19. Those are Marie de Medicis, Villeroy and Puysieulx to Breves, Nov 1611 - Nov 1613, catalogued "avec chiffre" with no decipherment. Not digitised. The Henri IV-Breves key is held (fr. 3462 f. 103). |
| 2744 | read | high | The shelfmarks are OCR errors for fr. 3828 / 3835 (lead 1577) and fr. 3825 no. 28. Avenel t. III (1858) prints all of them with the cipher explained in footnotes, from a key he rebuilt (CXXXV, CXLVI, CLIV, CLV, CLVIII, CLXVII, CXIX). |
| 2589 | read | high | The ACTApro title is Karl XI to Rutger von Ascheberg, 23-25 July 1676, "chiffriert, inklusive entschluesselte Abschrift", 4 leaves. |
| 2587 | partly_read | medium | Nr. 783 and 787 "nicht entziffert" are notes by Culeman and Vockerodt that the archivist could not read: handwriting, not cipher. Nr. 764 (Le Chambrier) is "chiffriert und entziffert"; Nr. 828 is catalogue 2494. Nr. 725/726/733 were not re-read. |
| 2618 | read | medium | The volumes are titled "Dechiffrements und Abschriften": Prussian decipherments and copies. |
| 2783 | read | high | TNA describes SP 87/2/49 and /51 as "Cipher with interlinear decodement". |
| 2814 | read | medium | The OeNB record says a German translation is filed with the cipher letter. |
| 1633, 1676, 1677 | none | - | Archivportal-D now serves an Anubis proof-of-work page to curl. The descriptions name a key ("Geheimschrift", "Chiffren"), not ciphertext. |
| 2417 | none | - | The only source is Tant's list, which does not say the letter is ciphered. archives-aube.fr needs JS and cookies. |
| 2692 | none | - | archives.hungaricana.hu returns 403 to curl. The quoted regest is cut short ("..."), so a noted decipherment cannot be ruled out. |

## Routes used
- **BnF Archives et manuscrits answers curl at `ark:/12148/cc<NNNNN><check>`.** The check character is the NOID checksum
  of the id without the NAAN (`am_probe.py`). For the Ancien fonds, cc ≈ fr. number + 46450 near fr. 3600-3700
  (fr. 3673 = cc50124, fr. 3702 = cc50146, fr. 3825 = cc50265, fr. 3654 = cc50106, fr. 3541 = cc49988).
  A digitised volume's notice carries a `gallica.bnf.fr/ark:/12148/btv1b...` link. None of the volumes here has one.
- The Omont OCR (archive.org `p1cataloguegnr02/03bibluoft_djvu.txt`) gives `(Anc. N.)` **at the end** of each entry, followed by
  the next heading. The Omont sweep seems to have paired items with the wrong heading. That explains fr. 3652 → 3654 and
  fr. 3826 → 3828, and probably fr. 3823 → 3825 and fr. 3855 → 3835. Other rows of `research/sweep_2026-11-14_omont_bnf` need the same check.
- Bot checks recorded, nothing solved:
  - portail.biblissima.fr and www.archivportal-d.de: Anubis proof-of-work.
  - gallica.bnf.fr SRU: Cloudflare 403.
  - archives.hungaricana.hu: 403.
  - archives-aube.fr: JS and cookies required.
  - ACTApro links for Nl Gruner Nr. 57/58: an empty shell, although other ACTApro records loaded.
- cryptiana unsolved.htm and GL.htm were fetched once each into `src/` (git-ignored).

## Record errors found
- 2726: fr. 3652 is the Antonio Perez volume and fr. 3339 holds copies on the Etats de Blois. Neither has a cipher piece.
- 2744: fr. 3826, 3823 and 3855 have no cipher items. The pieces are in fr. 3828, 3825 and 3835.
- 1577 (not in this batch): Avenel explains the cipher in every one of its letters checked, so its "partly_read" verdict is too weak.
- 2587: the "nicht entziffert" volumes Nr. 783 and 787 are not cipher.
- 2589: the recipient is Rutger von Ascheberg, and the file is 4 leaves.
