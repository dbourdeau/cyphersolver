# Charles IX to Philibert du Croc — DECODE R2789

Status: resolved — found already solved by George Lasry (25 May 2022); DECODE's “Non-decrypted” label is stale.

## Identification and date

DECODE R2789 reproduces the two-page cipher letter printed as document XLIII in Paul Destray, *Philibert Du Croc : un diplomate français du XVIe siècle* (1924), p. 80 and the two following facsimile leaves. Destray heads it `S. l. n. d.`: without place or date. The address is to du Croc as Charles IX's ambassador in Scotland. Cryptiana dates it cautiously to one of his Scottish missions, 1565–67 or 1572. The catalogue's “1 Jan 1550” is a metadata artefact: Charles IX was born only on 27 June 1550.

The authenticated DECODE scans (`CharlesIXToPhilibertDuCroc1.png` and `CharlesIXToPhilibertDuCroc2.png`) were checked against Gallica canvases 88–89. They are the same recto and verso reproduced by Destray: cipher throughout, signed Charles, with a ciphered postscript and Pinart's countersignature.

## Prior solution

Satoshi Tomokiyo's Cryptiana page `GL.htm`, updated 25 May 2022, publishes George Lasry's red plaintext overlay on both pages and identifies the system as Charles IX's nomenclator for du Croc. The overlay is not complete: several groups are printed as question marks and a few readings are hidden by signs or are hard to distinguish at the available resolution. The diplomatic reading in `READING.md` therefore preserves gaps instead of silently completing them.

## Substance

Charles tells du Croc to use his judgment in Scotland and follow his instructions for the country's peace. Above all, the King's nephew is to be well brought up, to retain the traditional Scottish attachment to France, and not to marry or conclude a marriage before Charles has been informed and can send his intention. The postscript directs du Croc to prevent the English from gaining any foothold in Scotland and to make the Scots understand that France seeks their preservation.

“Mon nepveu” is the young James VI. The letter belongs to the politics of his minority, but the surviving evidence does not choose securely between du Croc's 1565–67 and 1572 missions.

## What remains open

- the original date and place;
- the exact archive cote within the Archives départementales de la Nièvre, fonds du Bourg de Bozas (Destray does not give it);
- a person's check of the sign transcription made on 14 Nov 2026 (`R2789_transcription.txt`, see the last section), and a complete sign-to-plaintext key;
- the handful of groups and phrases Lasry's overlay leaves as `????` or that remain visually uncertain.

## Sources

- DECODE R2789, <https://de-crypt.org/decrypt-web/RecordsView/2789>.
- Paul Destray, *Philibert Du Croc* (Paris, 1924), document XLIII, p. 80 and facsimiles, <https://gallica.bnf.fr/ark:/12148/bpt6k932364m/f86.item>.
- Satoshi Tomokiyo, “George Lasry's Solutions of Unsolved Ciphers,” section “Charles IX to Philibert du Croc (1565–1567 or 1572),” with George Lasry's overlays, <http://cryptiana.web.fc2.com/code/GL.htm>.


## 14 Nov 2026: the cipher signs transcribed

The audit asked for the transcription of the cipher as written. Checked first: nothing in the folder; the DECODE
R2789 record (public API and record page) carries the two images and no transcription or document; cryptiana
`GL.htm` carries George Lasry's key table (`GL/GL_CharlesIX.png`) and his overlays as images only.

Both images are public, so the signs were transcribed here from Destray's facsimile on Gallica
(`openapi.bnf.fr/iiif/image/v3/ark:/12148/bpt6k932364m/f88` and `f89`, full size, 3330 x 4796 px; the DECODE scans
are the same pages at 614 and 707 px).

- `R2789_transcription.txt`: 42 lines (recto r01-r27, the postscript line rPS, verso v01-v14), 1622 signs with 78
  distinct labels, and 34 vertical strokes (1656 tokens on `_check_profile.py --measure --drop-first`); 47 signs
  marked `?`. Each sign is written with a label from Lasry's key table (`E1`, `N3`, `VOUS`, `U4` ...).
- It is a single AI transcription, not checked by a person. Some signs of the key look alike in the facsimile
  (D1/O3, P1/F1/N2, E2/QUE, V4/LL/POUR, B1/S1, E3 and the stroke); these were labelled by what makes sense in the
  line, so those labels do not test the plaintext. The ticks above and below the line are not recorded.
- `R2789_decode.txt`: the labels replaced by their letters and words. It agrees with Lasry's overlay on every line.
  In several places where `READING.md` has `[…]` (it was copied from the overlay image at 624 px) the decode shows
  the word sign or the letters, for example r01 `JE SCAI QUE VOUS CONGNOISSES [TRES] BIEN L HVMEVR DE CEVLX A`
  against `JE SCAIS […] CONGNOISSES […] BIEN L'HOMME […] CEULX A`, and r18 `QV IL N EN SERA RIEN CONCLVD QUE JE N EN
  SOIS PREMIE-` against `QV'IL NE SE MARIE […] QVE JE M'EN SOIS PREMIE-`.

Not done: `R2789_reading.md` and `R2789_en.md` were not redone from the decode, so `read_share` stays 0.928 and the
state stays "read in part". Redoing them from `R2789_decode.txt` (after a person has checked the doubtful signs) is
the next step and would probably close most of the gaps. Still unvalued: the nine signs Lasry lists as unknown
(U1-U9: r05, r07, r20, v08, v12, v14) and the word signs he queries (TRES, ESC, ROY, JACQUES).
