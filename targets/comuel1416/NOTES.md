# Pedro Comuel to Francesc Climent, 27 Jun 1416 (Puig y Puig 1920, app. CXXXV)

Status: found already read (Puig y Puig 1920); the cipher itself is not imaged and its key is not known.
**22 Oct 2026, reading audit:** nothing of the letter is in the repository (the Google Books link returns 403 to scripts), so the entry is *decoded, not read* in profile.json; class already solved is kept because the text is in print (Puig 1920).
**23 Oct 2026, re-read (b26):** the Google Books `jscmd=click3` endpoint still serves signed page images of Puig 1920, so his text (p. 578 (the letter ends there; p. 579 is the next item); ACB "Documentos inéditos del obispo Çapera" no. 670) is now transcribed as printed, italics marking his decipherment (85 of 401 words): [`texts/comuel1416_reading.md`](texts/comuel1416_reading.md), English [`texts/comuel1416_en.md`](texts/comuel1416_en.md), log [`texts/comuel1416_reread_log.md`](texts/comuel1416_reread_log.md). Scored 0.25 plain, 1.00 explicit holes (the classical Latin word list does not know the abbreviations and medieval spellings); the sentences hold. profile.json: read (grade A).


Split on 14 Oct 2026 from `benedict1399` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter was
filed with Benedict XIII's own cipher letters to Climent because Puig printed them together. Benedict's key was rebuilt
on the one facsimile page of his letter of 22 June 1400 (doc. 1068); nothing shows that this letter, from another
sender, used the same key (Puig writes of "la clave o claves" he recovered). So it is an entry of its own, with no
claim about its key. Benedict XIII's letters are [`targets/benedict1399/`](../benedict1399/NOTES.md) (a different or
unverified cipher, with its own page). The other letters of his circle split off the same day, each its own entry for
the same reason: [`targets/santacruz1399/`](../santacruz1399/NOTES.md), [`targets/jafet1400/`](../jafet1400/NOTES.md), [`targets/exea1408/`](../exea1408/NOTES.md), [`targets/comuel1415/`](../comuel1415/NOTES.md); and the 1398 line in an unknown key, [`targets/vico1398/`](../vico1398/NOTES.md).

The work below was done in the benedict1399 sessions of 23 Sept 2026 and is carried over from its NOTES (section 3).

## The document

- Arxiu Capitular de Barcelona, the Schism papers Francesc Climent (Çapera) left to the chapter (Çapera papers, document number not given by Puig);
  today the paper part of the series Cisma d'Occident. Not digitised. Some of these papers were not returned after
  Puig studied them at home in 1920-30 (archivist Josep Mas, quoted by Baucells 1978).
- Pedro Comuel to Francesc Climent, 27 Jun 1416; printed by Sebastián Puig y Puig, *Pedro de Luna, último papa de Aviñón*
  (Barcelona 1920), appendix CXXXV, p. 578 (the letter ends there; p. 579 is the next item), with the deciphered passages in italics (p. 466 n. 2).
- Deciphered words printed: ~ 85 (estimate from printed lines). His coming to Aragon; note 2 cites another Comuel letter, doc. 661, not printed.

Puig's note 2 to this letter cites another letter of Comuel, doc. 661, which he does not print (a lead in the ACB).

## What was done here (23 Sept 2026)

- Puig's book found in full view on Google Books (CuOlkxWnk-EC); in-volume search for cifra/clave/descifr; the
  appendix pages of every cipher item fetched and checked for gaps (benedict1399 NOTES, section 1 and 3).
- No image of this letter exists: Puig's only cipher facsimile (p. 475) is of Benedict XIII's letter of 22 June 1400.
  The key was therefore not checked on this letter.

## Remaining gaps
- The ciphertext itself (no image, not transcribed) - blocker: needs-physical-access; the reading is Puig's, complete as printed (he marks nothing as unread); the cipher and its key could be checked only on the ACB original
- ~~Puig's printed text, not in the repository~~ closed 23 Oct 2026: transcribed from the Google Books page images (texts/comuel1416_reading.md)

## Escalation
- [x] siblings: Puig's appendix index (pp. 623-627) and a full-text search for cifra/cifrada/cifrado/clave read; every cipher item listed in benedict1399 NOTES section 3
- [n/a] clear-pages: no image of the letter; Puig's p. 466 n. 2 says the key came from Climent's lines on docs. 1063, 461, 463 (Benedict's letters), not from this one
- [n/a] known-keys: Benedict XIII's key (benedict1399/key.md) could be tried only on ciphertext, and this letter's ciphertext is not imaged or printed
- [x] print: Puig 1920 (this reading, transcribed 23 Oct 2026 in texts/); Meister 1906; Baucells 1978 (parchments only)
- [n/a] key-rebuild: no ciphertext in hand
- [n/a] retry: nothing to retry without the ciphertext

## Assumptions for George's review
- This letter is split from Benedict XIII's because its key is not shown to be his; it is not shown to differ either.
  If the ACB original shows Benedict's sign alphabet, it belongs back in benedict1399.

## 14 Nov 2026, full-texts audit: no transcription of the cipher

The audit asks for the cipher as written beside the decipherment. Looked in order: (1) the folder holds only Puig's printed text (`texts/`), no cipher; (2) the folder names no DECODE record for this letter, and Puig 1920 (appendix CXXXV, p. 578) prints the deciphered words in italics, not the signs; (3) no image of the letter is reachable (ACB, not digitised; Puig's only cipher facsimile, p. 475, is of Benedict XIII's letter of 22 June 1400). So `outcome.texts` now carries `transcription_missing` with that reason. Nothing else changed: class, method and the reading are as before. Unblocked only by an image or an on-site transcription of the ACB original (same blocker as in Remaining gaps).
