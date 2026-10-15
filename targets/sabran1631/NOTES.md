# Louis XIII to Melchior de Sabran, Dijon, 28 March 1631 — BnF Baluze 155 f. 79–80 (DECODE R2748) — NOTES

Split on 14 Oct 2026 from `louis1615` under the one-key rule (George Lasry, 14 Oct 2026). The old entry (catalogue
191) grouped this letter with two letters of 1615 and 1617 to Brûlart de Léon because DECODE lists all three with
Louis XIII as author. Those two are in the Brûlart de Léon cipher of 1615–18, a different cipher, with their own
entry: [`targets/brulart1615/`](../brulart1615/NOTES.md), page `brulart1615.html`. The old slug `louis1615` is a
stub page pointing to both.

**Outcome: read from existing decipherment.** George Lasry solved the cipher of this letter in 2022; his key and his
decipherment (overlaid on the f. 79 image) are on Satoshi Tomokiyo's cryptiana page "George Lasry's solutions"
(GL.htm, "Melchior de Sabran (1631)"). Nothing about the text is added here, and his key was not re-applied to a
transcription in this project. Session 2026-09-21; split and written up 2026-10-14.

## The letter

- DECODE R2748 ("BnF_Baluze155_f79", uploader Tomokiyo, status Non-decrypted when fetched): BnF Baluze 155 f. 79–80,
  4 images (Gallica scans). Louis XIII, countersigned Bouthillier, at Dijon, 28 March 1631, to Melchior de Sabran,
  French resident in Genoa (1630–1637). f. 79r: a clear letter with two cipher paragraphs, about 20 lines in all, of
  lower-case letters, two-digit numbers and signs; f. 80 is blank. The images are git-ignored in the main checkout,
  `C:\Users\dbour\cypher\targets\louis1615\decode\` (`IMG_R2748_I17139_P1.png` … `P4`, reduced copies `p1s.jpg` …).
- The clear text: the King has seen Sabran's despatch of 16 February, and will answer the two main points.
- Lasry's overlay shows the cipher mixes single letters, syllables (`tion`), words (`vous`, `que`, `par`, `bon`,
  `prince`) and a doubling sign. The first passage concerns the Prince of Monaco; the second says the King did not
  think it right to take up the conditions proposed, but wants Sabran to keep the prince in his devotion to the
  crown and assure him of the King's goodwill and protection. (Summary from Lasry's overlay, not re-checked here.)
- Lasry also found the same cipher in Sabran's own letters to Bouthillier, BnF fr. 4134 (1633) and fr. 4135 (1635)
  (Tomokiyo, louisxiii.htm). Those letters were not opened here.

## Sources

- Tomokiyo, "George Lasry's solutions", https://cryptiana.web.fc2.com/code/GL.htm, "Melchior de Sabran (1631)":
  key and decipherment as images (`GL/BnF_fr4134.jpg`, `GL/BnF_fr4134_decipher.png`, `GL/BnF_fr4134_decipher2.png`).
  Copies of GL.htm and louisxiii.htm are in the main checkout's `targets/louis1615/` (git-ignored).
- Tomokiyo, "French Ciphers during the Reign of Louis XIII", https://cryptiana.web.fc2.com/code/louisxiii.htm,
  "Louis XIII-Sabran Cipher (1631)".

## What was done

1. 21 Sept 2026: fetched the DECODE record view and the four R2748 images with the shared cookie.
2. 21 Sept 2026: fetched louisxiii.htm and GL.htm; both state Lasry's solution. The entry was closed without
   applying the key.
3. 14 Oct 2026: split from louis1615; Lasry's three GL.htm images fetched to read what the overlay says for the
   page summary.

## Still open (here)

Not a gap in the text, which Lasry deciphered in full: this project made no transcription of f. 79r and did not
apply his key, so it has no sign-level check of its own and no replay. The sibling letters in fr. 4134 and fr. 4135
were not opened.

## Escalation (record)

- [x] siblings: fr. 4134 and fr. 4135 identified from Tomokiyo (same cipher, per Lasry); Baluze 155's other cipher
  (Servien–Sabran 1632) is a different cipher, solved by Tomokiyo
- [x] clear-pages: f. 80 is blank; no decipherment on the record
- [x] known-keys: Lasry's key (GL.htm) is the key of this letter
- [x] print: louisxiii.htm and GL.htm checked
- [n/a] key-rebuild: the text is already deciphered by Lasry; nothing to rebuild
- [n/a] retry: no reading of our own to retry

## Assumptions for George's review

- Credit: George is credited with the prior solution of this letter only (R2748), from Tomokiyo's GL.htm entry
  "Melchior de Sabran (1631)", which shows his key and decipherment. He is not credited on the 1615–17 Brûlart
  letters (brulart1615), which Tomokiyo read with his own reconstruction.
- The page's summary of what the cipher says comes from his overlay on GL.htm, read by eye; his decipherment is
  assumed complete and was not re-checked sign by sign.
- That fr. 4134 / fr. 4135 use the same key is his finding as reported by Tomokiyo; it was not tested here.
