# Mary Queen of Scots to John Hamilton, Archbishop of St Andrews, Bolton, 18 January 1569 (BL Add MS 33531 ff. 73–74; DECODE R8347) — NOTES

**Verdict: read at the time, calendared, and its key already published. Catalogue entry 84 ("... to unknown
recipient, Jan 1568") is resolved and removed.** Nothing in the cipher is unread except the code signs that the
contemporary decipherer also left as signs. This session identified the record and transcribed the decipherment in full
(`reading.md`; Bain gives only an abstract). Write-up `docs/hamilton1569.html`. Checked in one session on 2026-09-21.

## Identification

- DECODE R8347 leaves author, sender and recipient blank ("..."), dates the record January 1568, and gives the status
  "Partially decrypted", 4 pp.
- Bain, *Calendar of Scottish Papers* ii (1900), no. 966 (the number is used twice; this is the second 966), p. 604,
  margin "Add. MSS. 33,531, fol. 73": "Jan. 18. Mary to Archbishop of St. Andrews. 'Reverend fader and traist cousigne
  and counsalour' … Bowtoun. Signed: Your gud cusines and asuryd frinde, Marie R. 2 pp. Chiefly in cipher. (2) Decipher
  of same. 1½ pp. Indorsed: 'Recept xxiiij January.'" Bain footnotes that the "…" in "delivered in … hands" is "a
  symbol for Elizabeth", and the one after "the escheat ye crave for" is "a symbol". Found by grepping the archive.org
  text (`CalendarStatePapersMaryQueenOfScotsVol2`) for "33,531", as advised by [[throck1569]].
- Tomokiyo (cryptiana `mary.htm`, "Mary-Hamilton Cipher (1569)", "Mary to John Hamilton, Archbishop of St. Andrews,
  Bolton, 18 January 1569, f.73r-74v") reconstructs the alphabet. His key image is the record's DOC_ file
  (`DOC_8347_2024-Sep-18-20-52-36_42580.png`). He also finds the same cipher in Cotton Caligula B IX f. 315b (Mary to
  ?Hamilton, Bolton, 9 Sept 1568), printed in Labanoff ii p. 175.
- DECODE's "Jan 1568" is the Old Style year of the letter's own date ("Off Bowtoun the [xviij] of Januar 1568"),
  i.e. 18 January 1569 New Style. Mary was held at Bolton Castle; the recipient, John Hamilton, Archbishop of St
  Andrews, was leading her party in Scotland.

## The document

Four images (P1 = f. 74r, P2 = f. 73r, P3 = f. 74v, P4 = f. 73v), fetched with the shared DECODE cookie from
`decrypt-custom/filesrv` (the `decrypt-web/filesrv` path 404s). They are kept in the scratchpad, not the repository.

- f. 73r: a clear salutation in Mary's secretary's hand, three lines, then 36 lines of cipher.
- f. 73v: 26 more lines of cipher, then the clear close (the commission for Argyll, Eglinton, Cassillis and Boyd), with
  one cipher line glossed "als sall be necessarie", the date and the autograph "Zour gud Cusines and asuryd frinde /
  Marie R".
- ff. 74r–74v: the decipherment of the cipher body, 43 + 10 lines, in Scots, in a different hand, headed "35."
  (f. 73r is headed "34." and "Lre Cyphered from ye Q. with the decifer, bisc[hop of] St Andr."). Dorse endorsed
  "Recept [x]xiiij Januar".

## The cipher

Simple substitution with invented signs (word division not checked beyond the first line, where it looks kept), a sign for th/y (Tomokiyo: probably a thorn), word signs
for *and* and *to*, and a handful of code signs for persons and states. Tomokiyo's key checked on the opening of the
cipher body (f. 73r line 4): ϕf ∂ɼϕz qesqsϕf… = *it … bein proposit* (i ϕ, t f, b ∂, e ɼ, n z, p q, r e, o s), matching
the decipherment's first line "it had bein proposit to me".

## Signs left in the decipherment

The decipherer copied these through as signs. Readings are from context and Bain; none is certain.

- ⟨E⟩ "my sone suld be deliverit in ⟨E⟩ handis": Queen Elizabeth (Bain's footnote). Graded C.
- ⟨Ꝗ⟩ "spokin to me in ⟨Ꝗ⟩ name … to schaw hir": probably Elizabeth again (another homophone). M.
- ⟨¥⟩ after "the lord Lennox": probably a sign for Lennox's party or for Morton; M.
- ⟨B⟩ ⟨p⟩ ⟨sp⟩ "as to the secors of B p sp I hoip to get of thaym bayth": France and Spain (Bain's conjecture);
  later "to Fr and to Sp". C.
- ⟨Mn⟩, ⟨ʗ⟩, ⟨X⟩, ⟨n⟩, ⟨k⟩, ⟨m⟩, ⟨Ƒ⟩, ⟨Ɡ⟩: short signs, most at clause ends; ⟨ʗ⟩ behaves like a separator or
  null. Not resolved.

## Remaining gaps
- code signs Mn, ʗ, X, n, k, m, Ƒ, Ɡ, ¥ - blocker: no-key-material; the contemporary decipherer also left them as signs, each is short, and the context only narrows some (France/Spain, Elizabeth)

## Escalation
- [x] siblings: Add MS 33531 R8348 (Throckmorton 1569) uses a different cipher; Tomokiyo's Cotton Caligula B IX f. 315b letter uses this one (Labanoff ii p. 175), not on DECODE
- [x] clear-pages: ff. 74r-v are the decipherment, transcribed in full
- [x] known-keys: Tomokiyo's Mary-Hamilton key (DECODE DOC_ file) fits
- [x] print: Bain ii no. 966 (abstract only), Tomokiyo mary.htm
- [n/a] key-rebuild: the letter alphabet is complete; only word signs remain, too few occurrences to rebuild
- [n/a] retry: the whole body is read by the contemporary decipherment; nothing to regrade

## Related

- [targets/throck1569/](../throck1569/): Throckmorton to Moray, 20 July 1569, ff. 79–80 of the same volume.
- [targets/moray/NOTES.md](../moray/NOTES.md): the Add MS 33531 list and the unsolved Moray–Wood cipher.

## 14 Nov 2026: full-texts audit, the missing transcription

R8347 was listed without a transcription of the cipher (ff. 73r-v). In order: (1) the folder holds
only `reading.md`, the decipherment of the time; (2) the DECODE record (public API and record page) carries four
images and Tomokiyo's key image, no transcription; cryptiana `mary.htm` has the key image only; (3) the images
could not be fetched: DECODE serves the images of this record only to a signed-in session (an anonymous request to `decrypt-custom/filesrv` returned the `forbidden.png` placeholder, 17,947 bytes; the 200 px thumbnails are public and useless for signs). No DECODE session is available in this checkout and the images an earlier session fetched were git-ignored and are gone. So `transcription_missing` is recorded. What unblocks it: the images of ff. 73r-v through
a DECODE account; the signs can then be labelled from Tomokiyo's Mary-Hamilton key and the transcription checked by
decoding against `reading.md`. Nothing else changed.
