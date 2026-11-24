# William Cecil to Sir Ralph Sadler and Sir James Croft, 11 Sep and 30 Oct 1559 (BL Add MS 33591, DECODE R4847, R4860) — NOTES

Status: no write-up

**Verdict: closed, already in print.** Both letters are printed in full in Arthur Clifford (ed.), *The State Papers
and Letters of Sir Ralph Sadler* (Edinburgh, 1809), vol. I: R4847 is no. XXXVI (p. 437), R4860 is no. XCVII
(pp. 526-527). Clifford prints the one ciphered phrase already deciphered. Nothing new is added here, so catalogue
entry 85 is removed and there is no site page. Session 2026-09-21.

## Sources

- DECODE R4847 (4 images: f. 102r letter, f. 102v blank, the address leaf, f. 103 blank) and R4860 (2 images:
  f. 248r letter, f. 248v address), fetched with the shared cookie into the git-ignored `img/`.
- DECODE R4851, the "key" record from the same series (Add MS 33591 ff. 166-167, dated "1554" on DECODE): a
  letter-and-symbol nomenclator endorsed **"Rand. Ciphre. Aug. 31 1559"**, i.e. Thomas Randolph's cipher. It has
  England, Scotland, Berwick, the Queen of Scots, Arran's family (Hamilton, Chatelherault), Sadler, Randolph, Knox,
  and so on. It contains no ② sign and does not cover the 11 Sept letter.
- Clifford 1809 vol. I, archive.org `statepapers01sadl` (djvu text).

## The documents

**R4847, 11 Sept 1559, Cecil at his house near Stamford → Sadler and Croft at Berwick.** In clear except for one
phrase. Cecil writes: "Ye wryte nothing to me of the recept of a new ciphre, which I lately sent to you, wherein this
I wryte." Then comes the ciphered sentence **"② borrowed of me at his being at London + H oo"**. The rest follows in
clear ("which he promised should be payed to you Mr Sadler for me …"). Clifford (p. 437, where his italics mark the cipher
deciphered "by another hand") gives: "**Therle of Arrayn** borrowed of me at his being at London **200 crowns**".
So ② = the Earl of Arran and "+ H oo" = 200 crowns. "oo" is probably the hundreds sign (compare "cc" = Baron and
"ccc" = Earl in Randolph's table), and "+" or "H" stands for 2 and for crowns. The cipher is the "new ciphre" that Cecil had just
sent, not Randolph's. Only these two groups are in cipher, so the new cipher cannot be rebuilt from this letter.
"Mons. de Beaufort" in the clear text is Arran's alias ("ye knowe what erle I meane").

**R4860, 30 Oct 1559, London, "at midnight" → Sadler and Croft.** Entirely in clear. There is no cipher on either page.
DECODE's "Non-decrypted, graphic signs, numerical" describes the series, not this letter.

## Contamination

The reading existed in print from 1809 and was found by a web search in this session, after the images had been
examined. The only step taken before the search was a tentative identification of ② as Arran from context:
Arran passed secretly through London to Cecil in late August 1559.

## 14 Nov 2026: full-texts audit, the missing transcription

R4860 was listed without a transcription. Checked the folder, the DECODE public API record
(`decrypt-web/api/view/Records/4860`) and the record page: no transcription anywhere, and none is possible, because
the letter has no cipher (see "The documents" above). `outcome.texts` now says so in `transcription_missing`. The
images could not be looked at again: DECODE serves the images of this record only to a signed-in session (an anonymous request to `decrypt-custom/filesrv` returned the `forbidden.png` placeholder, 17,947 bytes; the 200 px thumbnails are public and useless for signs). No DECODE session is available in this checkout and the images an earlier session fetched were git-ignored and are gone. R4847 is unchanged (`transcription.txt`).
