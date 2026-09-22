# Beinecke Mellon MS 29, "Elias of Cortona", Lumen luminum, c. 1525 (DECODE R2877)

Status: attempted, open (closed from the evidence 22 Sept 2026). The cipher is about 234 letters on ff. 1v-2v and
a later copy on the front pastedown. It does not read under any simple system tested. Its statistics fit either a
private cipher of an unknown type or invented "secret names". No key, no clear copy and no printed decipherment
exist anywhere I could find.

## What the catalogue entry gets wrong

The catalogue entry (DECODE R2877, catalogue item "Elia da Cortona (1180-1253) (Venice?) to unknown recipient") gets
several things wrong:

- It is not a letter. It is an alchemical codex, the *Lumen luminum* ascribed to Frater Elias, with an Italian
  prologue. It was copied in North Italy (Venice?) about 1525. Elias of Cortona (d. 1253) is the pseudonymous
  author, not a sender, and there is no recipient.
- The cipher uses Latin letters plus three scribal signs (ʒ, a 7-shaped et-sign, a 9-shaped con-sign), not
  "graphic signs".
- The cipher is only on ff. 1v-2v and on the front pastedown, not throughout the codex. The 68 pages on DECODE are
  the whole book.

## Source

- Beinecke Rare Book and Manuscript Library, Mellon MS 29. Free IIIF images (public domain) are in Yale Digital
  Collections: https://collections.library.yale.edu/catalog/17388793 (manifest
  https://collections.library.yale.edu/manifests/17388793). The canvases used are: front pastedown 17388795, 1r
  17388796, 1v 17388797, 2r 17388798 and 2v 17388799.
- Catalogue: Beinecke pre-1600 manuscripts description of Mellon MS 29,
  online at https://pre1600ms.beinecke.library.yale.edu/docs/pre1600.mell029.htm. It notes the "hint of
  charlatanism" in a cryptic text with a cipher code and a pious ascription.
- DECODE R2877 holds the same 72 images (TH_IMG_R2877_I20381_P1-P72). It has no transcription and no key.
- Images downloaded to `img/` (git-ignored) at 2000 px, with full-resolution crops of the cipher lines.

## Where the cipher is

All leaves 3r-37v were checked (3r-6v by me, 7r-37v by a page-scan agent, spot-checked). They are clear Latin
*Lumen luminum* text (Rasis' De aluminibus et salibus family, then the Rogiel palace passage), a Latin-Arabic
synonym list on f. 36r, and Italian recipes on ff. 36v-37v. There is no cipher on them, only ordinary ʒ and ℔
weight signs.

The Italian prologue (ff. 1r-2v, clear) frames the cipher. On f. 1r the "medicine" for sun and moon is hidden in
two figures (a star for Sol, a reversed-C-with-p for Luna). Five bodies make sun and moon: Saturn, Jupiter, Mars,
Venus, Mercury. On f. 1v the medicines, "ouer nomi deli spiriti che lauano purgano et mondificano li corpi", are
the twelve zodiac signs. Then come the two recipes, and on f. 2v a table of what each sign "se chiama".

1. **f. 1v ll. 17-19, the Sol recipe**: "Primo nel nome de dio piglierai: [cipher] Dapoi pista in mortaro et
   tritale in poluere minutissima et pesa et se remagnera cossa alcuna sara ℔ 1 agiongerai ʒ che dir onze de leone".
2. **f. 2r ll. 8-10, the Luna recipe**: "piglia i nomi del signor. [cipher, with the clear words *in* and *cioe*]
   dapoi pesta bē nel mortaro ... aggiongi ʒ iiii libre poluerizate et scorpio et tauro et gemini piglia ʒ cioe
   drama 1 ...".
3. **f. 2v, the zodiac table**: "Ariete se chiama srcon pggy", and so on for all twelve signs.
4. **Front pastedown, later hand (late 16th c.)**: a copy of the Luna recipe ("Se tu vorai far argento
   perfettissimo ... di al nome di iddio ylior lay girrt ...") and of the zodiac table ("Aries dicitur sagonpggy,
   taurus dicitur lagrla..."). It varies a great deal from ff. 2r-2v: "gnotrh" becomes "girrt h", "in ʒshukss"
   becomes "vshu Rs", and "set Vʒ Vs sn qrpt" becomes "sot aʒ vssugint". Between them is a clear gloss of the
   planet names (sol significa oro, luna argento, saturno piombo, iove stagnio, marte ferro, venere rame, mercurio
   argento vivo) and an astrological note on which signs are good, bad and middling. The copyist glossed the
   planets but left the cipher unread.

The transcription is in `transcription.txt` (with conventions) and `ciphertext.txt` (cipher only). It measures 234
letter signs. Agnieszka Rec (below) reads Cancer and Scorpio as "irgp∫hk∫cel" and "prk∫yq∫7gp". This confirms the
long s and the 7-sign, and shows that the q/g split is uncertain; the tests below were run both split and merged.

## Prior work

- Agnieszka Rec, "Ciphers and Secrecy Among the Alchemists: A Preliminary Report", *Societas Magica Newsletter* 31
  (Fall 2014), n. 8. She treats the f. 2v list as a code of codewords, quotes Scorpio and Cancer, and does not
  attempt it.
- Paolo Galiano (Simmetria Institute articles; ed. *Lumen luminum ad Fredericum imperatorem*, 2021) quotes the
  Italian prologue. No decipherment is known (the 2021 book was not seen).
- Tomokiyo's Cryptiana covers diplomatic ciphers, not alchemy. DECODE has status Non-decrypted.

## What was tested (22 Sept 2026)

Every test ran on the 234-letter transcription, scored with `lang` models (it-modern, it-cinquecento, la).

- **Statistics.** IC is 0.075 in the table and 0.075 in the recipe lists, which is language-like. But the two
  sections have different profiles: q is 17% of the table and under 2% of the lists; h is 3% of the table and 10%
  of the lists. Sukhotin's vowel algorithm finds q as the main "vowel" in the table and r in the lists.
- **Monoalphabetic, one-to-one** (`mono2.py`, `anneal.py`): Italian and Latin, with and without word division, q/g
  split and merged, table and lists together and apart. The best result is -4.0 to -4.8 per character, which is
  gibberish. Control: a synthetic 206-letter Italian ingredient list enciphered at random is recovered by the same
  solver at -2.6 (an ad hoc run with `mono2.py` on the synthetic text). A simple substitution of Italian would therefore have been found.
- **Homophonic, many-to-one** (`homo.py`): gibberish.
- **Caesar and progressive (Trithemius) shifts** per entry, over five alphabets (with ʒ=z and 7=&), steps
  0/±1/±2 (`prog.py`): nothing.
- **Vigenère** with periods 2-7, key restarted per entry or running, both directions (`vig.py`): nothing. The
  period-7 fits are overfitting.
- **Reversed words; odd or even letters as nulls**: nothing.
- **Alberti disk.** The cipher letters include k, y, x, h and an et-sign, and capitals (R, V) sit inside the runs.
  This is the shape of Alberti's movable ring with index capitals. Alberti's published ring was tried per segment
  (`alberti.py`), then an unknown ring with a separate offset per segment was annealed (`alberti_anneal.py`, 19
  segments). Nothing read, even with that much freedom.
- **Word-pattern solver** over a vocabulary of about 170 Italian substances, numbers and weights
  (`wordsolve.py`): no consistent key. The only fits are trivial ("con", "et", "di al").
- **Pattern check.** "pqyqpqsqst" (q in every even position) and "lrqrlr", "qrqr" are hard to produce from
  Italian or Latin substance names under any fixed substitution. Only "cristallo" even fits Ariete's pattern.
  Shapes like these are typical of invented pseudo-text.

## Reading of the evidence

1. The texts cannot be the zodiac names re-enciphered or plain Decknamen. The recipes use the zodiac names in
   clear ("onze de leone", "scorpio et tauro et gemini"), so the table must hide what the signs stand for.
2. If the table and lists are a real cipher, it is not simple substitution. It is either a private system (an
   Alberti-type ring with changes we cannot see, or a nomenclator of whole names) or a set of "barbarous names".
   The Beinecke catalogue's suspicion of charlatanism fits the second: the book is ascribed to Frater Elias, backdated to 1315,
   and bound under an IHS stamp.
3. With about 234 letters in 14 short units, a polyalphabetic or code system cannot be recovered without a clear
   copy.

## Remaining gaps

- the zodiac table on f. 2v (12 entries) - blocker: no-key-material; not a simple substitution, and no key or
  clear copy is known
- the Sol recipe list on f. 1v and the Luna recipe list on f. 2r - blocker: no-key-material; as above, and too
  short (about 115 letters) for a polyalphabetic attack
- the pastedown copy - blocker: no-key-material; a corrupted later copy of 2 and 3, adds nothing

## Escalation

- [x] siblings: every leaf of the codex checked (3r-37v); no other cipher, no key, no gloss; the pastedown copy is
  unglossed
- [x] clear-pages: the pastedown's clear gloss explains only the planets; no clear copy of the recipes
- [x] known-keys: Alberti's published ring tested; no other key known for alchemical texts ascribed to Elias
- [x] print: Beinecke catalogue, Rec 2014, Galiano's articles; no decipherment
- [x] key-rebuild: monoalphabetic, homophonic, progressive, Vigenère, Alberti-ring and word-pattern solvers;
  none reads
- [n/a] retry: there is no partial key to retry with
