# bongars1597: Jacques Bongars, two letters of 26 Jan 1597 from Strasbourg (Burgerbibliothek Bern, Cod. B 149 (A) 451-452), names in nomenclator

Status: read in part (Brice Dudout, 11 Nov 2026, transcription and context reading; integration check the same day: cipher table matched, BnF fr. 7131 f. 548. Of 9 cipher groups, 4 are given by the table, 2 are proposed from context only, 3 are open; the clear French of both letters is read.)

Contributed by Brice Dudout (Europe chiffrée), with a Claude Opus 5.5 agent (pull request #396). Lead 2453, found in Daniel Bourdeau's Swiss
cantonal sweep (Burgerbibliothek scopeArchiv, Nov 2026) and closed on 9 Nov 2026 as "not_cipher" (clear letter-book copy
with about 6 nomenclator groups for names). We agree with that description; this target only supplies what the vetting left
aside: a full transcription of both leaves, the groups noted as written, and the names recovered from context where the
context allows it. If Daniel prefers to keep the lead closed, this folder can stay as a pointer.

## Documents

Burgerbibliothek Bern, Cod. B 149 (A), Bongars's letter-book (copies in one secretary hand, not the sent letters):
- 451, f. 360r (old foliation 429): Bongars to an unknown correspondent, Strasbourg, 26 Jan 1597. https://katalog.burgerbib.ch/detail.aspx?ID=201730
- 452, f. 360v: Bongars to an unknown correspondent (perhaps a second addressee), same place and date. https://katalog.burgerbib.ch/detail.aspx?ID=201731

Catalogue: "Personenangaben verschlüsselt"; rights "Gemeinfrei" (public domain). Credit: Burgerbibliothek Bern, Cod. B 149 (A)
451-452. No image is included here (CONTRIBUTING); the leaves are public at the links above.

## System

A small nomenclator for names only, inside clear French: 9 groups, each used once (the barred 4 occurs twice, alone in G5
and at the head of G7). Kinds: multi-figure numbers with marks above the figures (G1: tilde, strokes and a hook), figures
(G3 "12", G7 "199877"), and single signs (#, X, -o-, barred 4, 5 capped by a bar, barred Z). Cryptiana's catalogue of
Bongars ciphers in BnF fr. 7125-7132 (http://cryptiana.web.fc2.com/code/bongars.htm) lists a "Bongars' Cipher (1594-1603)"
(fr. 7129 f. 241) and figure ciphers with tilde or accents (f. 262, 548); one of these is the likely table, but none was seen
here, so no figure value is claimed.

## Method and honesty note

Identification by context only (grammar, names written in clear in the same letters, and the history of January 1597: Ancel's
tour of the German princes after his credentials of 16 Aug 1596, the 1596 league with England and the States, the Strasbourg
bishopric quarrel). A pre-registration fixed the levels (sure / probable / restored / unresolved) before the identifications.
There is no enciphered text to decode, so no shuffled-key test applies and none is reported; nothing here is a measured key.

| group | as written | proposal | level |
|---|---|---|---|
| G1 | 2~85 2'1'6^ | a person out of favour with a princely house | unresolved |
| G2 | # with four dots | a prince or house | unresolved |
| G3 | 12 ·sig(?) | les Estats (States General) | probable |
| G4 | X with a dot | the Spaniard / King of Spain | probable |
| G5 | barred 4 | a power that "could serve greatly" | unresolved |
| G6 | -o- | Queen Elizabeth | probable |
| G7 | 4 199877 | a German prince; candidate the Administrator of Magdeburg | unresolved (one candidate) |
| G8 | 5 capped by a bar | Cardinal Charles de Lorraine (other party at Strasbourg) | restored |
| G9 | barred Z | House of Austria / the Emperor | restored |

Reasons for each are in `names.tsv`. Main sources for the context: A. Anquez, *Henri IV et l'Allemagne d'après les mémoires
et la correspondance de Jacques Bongars* (Paris 1887), p. 45-47 (Ancel's tour; Lincoln at Kassel; Spanish garrisons in
Westphalia).

## Prior art

- Daniel's lead 2453 and vetting v16 (9 Nov 2026): no reading, closed "not_cipher".
- Anquez 1887 cites many Cod. B 149 items (nos 18 ... 499) but, in the OCR searched, not nos 451-452 nor a letter of 26 Jan 1597.
- *Epistolae Bongarsianae* (1647) and the French *Lettres* (1668, 1681, 1695) are the Latin letters to Camerarius and others, not these French letter-book copies. Not checked page by page.
- Not checked: R. Kohlndorfer-Fries, *Diplomatie und Gelehrtenrepublik* (2009, which lists over 300 Bongars letters); Hagen's Bern catalogue (1875).
- Web searches (11 Nov 2026) for this letter and for a Bongars nomenclator found only the Cryptiana catalogue above.

## Files

`transcription.txt` (diplomatic), `reading.md` (sentences), `translation.md` (English), `names.tsv` (the groups and reasons).
Added at integration: `decryption.txt` (the transcription with each group replaced by its value) and `key_fr7131_f548.tsv`
(the entries of the cipher table used here).

## Gaps (as sent by the contributor; superseded by Remaining gaps below)

The four open groups need the period table (BnF fr. 7129/7131) or the received originals. The addressee is unknown; f. 360v
("les Princes que nous avons veu ensemble", "l'affaire que vous traitez") may be addressed to Ancel himself, which f. 360r
(Ancel in the third person) is not. One reader (an agent) on 200 dpi greyscale images; no human palaeographic check.

## Integration check (11 Nov 2026)

Done by the project when pull request #396 was merged. What the contributor sent is kept above as sent; where this section
differs, this section holds.

**What reproduced.** Both leaves were fetched again from the Burgerbibliothek catalogue and the transcription was read
against them line by line: the clear French stands. The nine groups are where the transcription puts them (6 on f. 360r,
3 on f. 360v). Hagen's catalogue of 1875 was checked (Internet Archive, `CatalogusCodicumBernHagen`): it lists "451, Nescio
cui. Strasb. 26 Janvier 1597" and "452, Item" with no edition, where its neighbours 450 and 447 name one, so no printed
text of these two letters is recorded there.

**What did not.**
- Image size. The notes said "200 dpi greyscale". The catalogue serves each leaf at 658 x 895 px
  (`getimage.aspx?VEID=201730&DEID=10&SQNZNR=1&SIZE=100`); `SIZE=400` returns 2632 x 3580 px, but it is an enlargement
  of the same picture. The marks over the figures are at the limit of what can be seen.
- Word count. The notes said "about 690 words in clear". Counting the transcription gives 513 (238 + 275).
- "None [of Bongars's tables] was seen here." They can be seen: BnF fr. 7131 is on Gallica (ark:/12148/btv1b10509420g,
  through `openapi.bnf.fr`; gallica.bnf.fr answers 403 to scripts), and Cryptiana shows two of the leaves. The tables
  were opened in this check (next paragraph).

**The cipher table: BnF fr. 7131 f. 548r-v** (Cryptiana no. 29; Gallica views 1106-1107). Tables tried:
- f. 255v (Cryptiana no. 23, the clean copy of the 1594 cipher no. 17; view 522): signs for names. X with a dot is
  "Marquis d'Anspach", a 4-shaped sign is "Schonberg", a cross-topped h is "Mr de Bouillon", # is "Pais bas". These give
  no sense in the two letters (Hesse fearing that Ansbach comes too close; the morsel falling to nobody listed). Ruled out.
- f. 262r (no. 28, view 533): letters as single digits with a stroke, names as 21-76 under a tilde. Its name list
  (Padre Paulo, Padre Fulgentio, Diodati, Archduke Matthias) looks later than 1597 (not checked), and G7 gives no word with it. Ruled out.
- f. 548r-v (no. 29): letters as single digits with five kinds of mark (bar a-d, grave e-h, acute i-n, circumflex and
  tilde o-t, breve u-z), syllables 10-99 (ba 10 ... zu 99), "Doubles" (br = 4 with a cross-stroke), about 200 signs for
  common words, and names: French court, English court (Essex, Cecil, Norris, Buckhurst, Cobham), princes. It fits:
  - G4, X: "Roy d'Espagne". The contributor's context reading, made without the table, was "the Spaniard".
  - G9, Z: "L'Empereur". The contributor's context reading was "the House of Austria / the Emperor".
  - G8, a cross over an S-shaped tail: "Administrateur de Magdebourg". The contributor had restored "Cardinal de
    Lorraine"; the table gives "De Lorraine" the letter a and has no such sign for a cardinal. With Magdeburg the
    doubtful word before it reads "deputé": the envoy leaves the game "au deputé de l'Administrateur de Magdebourg".
    (The Administrator of Magdeburg was the father of the Brandenburg candidate for the see of Strasbourg. This
    background is not from the sources in this folder and was not checked here.)
  - G7, a spelled name: 4 with a cross-stroke = br, 1 with a breve = u, 9 with a stroke = n, 9 with a breve = z,
    87 = vi, 7 with a bar = c: "Brunzvic", Brunswick. The contributor's candidate was the Administrator of Magdeburg.
    It agrees with f. 360r, where Bongars writes in clear that "le Duc de Brunswic les estime" (the States), and here
    that "Messieurs les Estats ont du credit pres de luy".
  Two of the contributor's context readings could be tested against the table and both agree (G4, G9); one is
  contradicted (G8); one candidate is replaced (G7). That agreement, between readings made blind and a table found
  afterwards, is the evidence that this is the table. It is four groups, read on a small image: no shuffled-key control
  is possible on so little, and none is claimed.
- Not confirmed by the table: G3 (context: les Estats; the table's sign for "Les Estats" is h-shaped, the leaf has "12"
  and a small sign) and G6 (context: Queen Elizabeth; the table's sign for "Rne d'Angleterre" is a long s, the leaf has a
  stroke with a loop, nearer the table's "Cte d'Essex", a stroke with three loops; the feminine "elle" and "ses
  serviteurs et sujets" keep the Queen). Both stay grade I.
- Open: G1 (a figure under a tilde and digits with marks: the spelled part of the table, marks not legible), G2 (a
  double cross with dots; nearest table sign "Comte Palatin", a barred cross with dots) and G5 (a small 4 with a bar;
  nearest table signs "Madame soeur du Roy", a 4 with a cross-stroke, or the letter b). Candidates only, grade M.

**Grades** (README Conventions): G4, G7, G8, G9 are H (from a primary key source), with the caveat of the image; G3, G6
are I (context); the candidates for G2, G5 are M; G1 is unread.

**Outcome.** Method: read after matching with key from external sources (a table in Bongars's papers in Paris, not tied
to this Bern letter-book, found here to fit). Extent: partial. f. 360v has its three groups from the table; f. 360r has
one of six. The read bar is counted on cipher tokens: 4 of 9 from the key, so "read in part". Provenance: mixed (the
contributor's transcription and context readings; the project's key match). Lead 2453 was closed "not_cipher"; that
verdict is corrected to "partly_read": the leaves carry a real, if small, cipher (letters, syllables and name signs).

Prior reading: none found (Hagen 1875 no edition; Anquez 1887 OCR, contributor; web, contributor). The table itself is
described by S. Tomokiyo (Cryptiana, "Catalogue of Ciphers Related to Jacques Bongars in BnF fr.7125-7132", no. 29),
who does not connect it with the Bern letter-book.

## Remaining gaps
- G1 (f. 360r line 1: a figure under a tilde, then digits with marks) - blocker: illegible; the marks that tell the letters apart cannot be read on the 658 x 895 px catalogue image, the only one online
- G2 (f. 360r line 2, double cross with dots) and G5 (f. 360r line 16, 4 with a bar) - blocker: illegible; each occurs once and at this image size is not told apart from two or three table signs (candidates: Comte Palatin; Madame soeur du Roy)
- G3 (les Estats?) and G6 (Queen Elizabeth?), from context only - blocker: illegible; the leaf signs do not match the table's signs for those names at this image size, a larger scan from the Burgerbibliothek would settle them
- three doubtful words of the clear text (deputé, ma/sa, Firx) and the verb "l'apprecie" - blocker: illegible; same image
- R. Kohlndorfer-Fries, Diplomatie und Gelehrtenrepublik (2009), not checked for a calendar entry of these two letters - blocker: needs-physical-access; a printed book with no online text
- the common-word signs of fr. 7131 f. 548 (about 200) are not transcribed - blocker: no-key-material; the two letters use none of them, so nothing here tests them

## Escalation
- [x] siblings: Hagen 1875 lists the neighbours 447-454 of Cod. B 149 (A); the catalogue flags only 451 and 452 as having coded names (lead vetting, 9 Nov 2026); no other leaf opened
- [x] clear-pages: none; a letter-book copy, no decipherment on or with the leaves (both images read again)
- [x] known-keys: BnF fr. 7131 f. 255v (no. 23), f. 262r (no. 28) and f. 548r-v (no. 29) opened on Gallica; f. 548 fits (4 groups), the other two ruled out
- [x] print: Hagen 1875 (no edition named for 451-452); Anquez 1887 and web by the contributor: nothing
- [n/a] key-rebuild: the table exists and is complete; nine groups, each used once, give nothing to extend it from
- [x] retry: all nine groups compared again with f. 548 after the match; G1, G2, G5 stay open, G3 and G6 stay context-only
