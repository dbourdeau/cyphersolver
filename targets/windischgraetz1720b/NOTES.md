# Charles VI → Count Leopold Viktorin Windischgrätz, 1720–22, in the Emperor's private key R5018 — **read in part**

Status: read in part (since 16 Nov 2026: No. 2 is under the read bar on its cipher words, 9 of 10; Nos. 3 and 6 read). Three letters of the Emperor to his envoy, Nos. 2, 3 and 6 of the family register: R5021 and R5022
(13 Apr 1720, autograph and copy), R5023 (24 Jul 1720, copy only) and R5024 (11 Apr 1722, copy only). Every cipher
passage reads directly from the private key R5018, which survives in the same family archive: 192 of 192 cipher
signs (`dec_R5018_letters.md`).

Split on 14 Oct 2026 from `windischgraetz1720` under the one-key rule (George Lasry, 14 Oct 2026). Until then these
letters were filed with No. 1 (3 Feb 1720, R5019/R5020), which is in the Court Chancellery nomenclator R5017 and
announces this key: [`targets/windischgraetz1720/`](../windischgraetz1720/NOTES.md) (a different cipher, with its own
page). The work below was done in the windischgraetz1720 session of 19 Sept 2026 and is carried over from its NOTES;
`key5018.md` and `dec_R5018_letters.md` moved here on 14 Oct 2026. Images (git-ignored) stay in the main checkout's
`targets/windischgraetz1720/decode/`, and the glyph crops in its `key5018_glyphs/`.

Work date: 2026-09-19. Catalogue item 69 (removed when the four letters were read).

Holder: Státní oblastní archiv v Plzni, pracoviště Klášter u Nepomuka, Rodinný archiv Windischgrätzů. Autograph of
No. 2 in inv. 694, karton 5; the fair copies in inv. 5, book 5 (a register of the Emperor's letters, one "No." per
letter, pp. 404–416). The key is in the key collection, karton 164, inv. 1403, sign. 103 (DECODE R5018).

## Prior work

Jakub Mírka, "Raně novověká šifrovaná korespondence ve fondech šlechtických rodinných archivů SOA v Plzni",
*Západočeské archivy* 2012, pp. 44–72, reprinted in *Crypto-World* 3–4/2013, describes the key change announced on
3 Feb 1720 and says the later letters are in the new key and that it survives (n. 40–41). He prints no decryption,
and none was found elsewhere (web search, 19 Sept 2026).

## The key

**R5018** is the new private key, on one sheet. Each of 24 letters has a number from 10 to 38 and a graphic sign;
the vowels have a second number. There are about 300 codes (39–210 and two-letter groups such as ab, fb, zi) and the
nulls 3 4 5 6 7 9. Transcribed in `key5018.md`. The docket on the back reads "Ziffern mit J[hr]: K[ayserlichen]
M[ajestät] …".

Corrections found by using the key: the copyist's signs drift. The q-with-crossbars sign serves D and once N, and p
with one crossbar serves both Z and G. Each is settled by the surrounding numbered letters.

## Letters and contents

| No. | date | DECODE | cipher passages | substance of the cipher |
|---|---|---|---|---|
| 2 | Vienna, 13 Apr 1720 | R5021 (autograph), R5022 (copy pp. 404–407) | 2 | Whether [Spain] **and Orleans** will come to terms with one another again. How one could **free oneself entirely from the burden of the Barrier** |
| 3 | Vienna, 24 Jul 1720 | R5023 (copy pp. 407–409) | 3 | **Beretti Landi** (the Spanish envoy at The Hague) proposed, in the name of his court, **a marriage between one or other of the Emperor's children and Anjou's sons**. Charles will stay on good terms with that court, but **"both are so small"** that nothing is to be made known yet |
| 6 | Vienna, 11 Apr 1722 | R5024 (copy pp. 414–416) | 4 | Windischgrätz's talks **with Beretti about a marriage between Spain and the Emperor's house**. Beretti is **"embittered against me and Austria"**, but it is not bad to make use of him and to show him every consideration *in utili et honorifico* |

No. 3 is an early trace of the Austro-Spanish marriage scheme that came back in the 1725 Treaty of Vienna. The
Emperor's eldest child, Maria Theresa, was then three. No. 6 opens in clear text with the Emperor's grief at the death
of his Oberststallmeister and favourite, presumably Count Michael Johann Althann (d. March 1722).

Not on DECODE: Nos. 4 and 5 (book pp. 409–414) and No. 7 (p. 417 on). R5023's first image repeats pp. 406–407.

## Files

- `key5018.md`: the key transcribed (alphabet grid and nomenclature).
- `dec_R5018_letters.md`: the three letters' cipher passages, sign by sign, with their readings.

Open: the clear text of Nos. 2, 3 and 6 is only summarised around the cipher passages.

**23 Oct 2026, verification 5 (plain bar; research/reading_audit/VERIFY5_BRIEF.md)**: the letters are German (not English): explicit-hole bar. The passages of Nos. 2, 3 and 6 in their quoted clear context: explicit 1.0 each. Rescored with research/reading_audit/v2_score.py (plain word-list share and explicit-hole share); both figures are in each entry's reading_review note. Keeps read.


## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher only. The readings mark the cipher in
⟦ ⟧ and quote clear words around it, so the cipher was taken as the ⟦ ⟧ spans; holes counted by words.

- No. 2: 0.964 (whole excerpt, clear included, not the measure) -> **0.900** (9 of 10 cipher words; versten[den]
  supplies letters the copy's cipher does not have). Read -> **read in part**.
- No. 3: 0.972 -> **0.963** (26 of 27; the word pieces "er" and "en" at the joins with the clear counted as words).
  Pr[o]posi[t]ion is one word and one hole (the old figure counted it twice). Stays read.
- No. 6: 1.0 (18 of 18), stays read.

The target moves from read to **read in part**, because one of its three letters is under the bar. Over all three
letters: 53 of 55 cipher words (0.964). By signs, all 192 are read: neither hole is an unread sign. Both are letters
the reading supplies.

## Remaining gaps

- No. 2, "versten[den]": letters the writer left out of the cipher (it ends VERSTEN before the clear "werden") - blocker: needs-physical-access; every sign that is there is read, and the missing letters cannot be recovered from any file here. The checker offers no blocker type for letters left out; this is the nearest.
- No. 3, "Pr[o]posi[t]ion": two letters written with the wrong sign (P for O, Z for T). The word is certain - blocker: needs-physical-access; the wrong signs are what the copy has, and no file here can change them (No. 3 survives only in the register copy). The checker offers no better type. One hole; the letter stays read.

## Escalation

- [x] siblings: No. 1 (3 Feb 1720, R5019/R5020, Chancellery key R5017, `../windischgraetz1720`) read; Nos. 4, 5 and 7 of the register are not on DECODE
- [x] clear-pages: the clear text around each passage used for the sense
- [x] known-keys: the Emperor's private key R5018, which survives in the same archive, applied to every sign
- [x] print: Mírka 2012 describes the key and letters without a decryption; none found elsewhere (web search, 19 Sept 2026)
- [n/a] key-rebuild: the period key survives and gives every sign; the two holes are not unread signs
- [x] retry: the copyist's drifting signs (D/N, Z/G) settled by the numbered letters around them; nothing in the cipher is left unread
