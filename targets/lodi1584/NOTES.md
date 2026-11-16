# Sir Francis Englefield to the Cardinal of Como, Madrid, 15 Nov 1584 (ASV Segr. Stato, Spagna 31, ff. 209-212; DECODE R119)

Status: no write-up

Catalogue no. 247 (DECODE refill, rule-scored class A, "Vescovo di Lodi (Spain) to The Secretariat, 1 Jan 1584").
Worked 21 Sept 2026.

Outcome: **read at the time; closed.** The ciphered passages carry a contemporary interlinear decipherment, and
the key is bound with the letter. Nothing is left to break. The new finding is who wrote it and when.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): `plaintext.txt` is the
contemporary decipherment of the cipher runs only; **every run reads** as Spanish without holes (reviewed B). The
clear text between the runs was not transcribed, so whole sentences and an English translation need it from the images.

## What the record is

DECODE R119 (4 images plus 2 attached documents, fetched with the session cookie; images git-ignored in `img/`)
is not a letter of the nuncio Taverna (Vescovo di Lodi). DECODE took the name and date from the volume heading
("Mons. Vescovo di Lodi, nuntio ... dal 1 gennaio 1584 - 16 march 1585"). It is a four-page Spanish letter,
stamped ff. 210 and 212 (old ink foliation 251-254); the key sheet is stamped f. 211 (old 253) and the address leaf, DOC_R119_D1354, is stamped 209. DECODE page order: P1 opening (210), P2 continuation, P3 postscript with the outer address, P4 close and signature (212).

- Addressed "All'Ill.mo et R.mo S.or ... il S.r Card.le di Como" (Tolomeo Gallio, Secretary of State), Roma.
- Signed with the cipher number **70**, which the key gives as "Fran.co Englefilol", i.e. **Sir Francis
  Englefield**, the English Catholic exile at the Spanish court. The docket reads "S.r Englefild ... 15 Novembre"
  and "84 / 17 9bre / Ingh.ri in Spagna / Avvisi diversi". The ciphered dateline reads "82 (Madrid) a los quinze
  de noviembre, año 1584".
- Content: Englefield thanks Como for a letter and for the cipher sent through the Bishop of Piacenza (Sega).
  After long waiting for help "from these parts" to bring England back to the Church, he finds the business
  deferred, now for one reason, now for another. He takes it that any intention of attempting something by force
  from Spain has cooled until the Flanders war is over, the Queen of England is dead or something else changes
  there. He asks the Pope to open the purse for the costs, and reports from Paris that the Earl of Shrewsbury has
  been relieved of guarding the Queen of Scots and that she has been put in the custody of three "most
  pestiferous Puritans" of Huntingdon's faction. He fears for her life, and warns that the delays add to the cost
  and difficulty of the reformation of England. He asks for a cardinal of the English nation, now that the see
  of Milan is vacant (Borromeo died 3 Nov 1584), and names Doctor William Allen ("69"). The postscript says that
  if the Pope has been moved by the objections Don Bernardino de Mendoza raised after his return from England
  against the execution of "la grande empresa", he should inform himself through Allen and Father Persons
  ("el padre Parsonio").
- Marginal notes in Italian by the Secretariat ("Ingl.si Catt.ci dimandano un Card.le della nat.e per capo della
  causa loro"; "Gulielmi Alani laudes"), and an Italian summary line at the head of f. 252r.

## Cipher

Key on f. 211r (DOC_R119_D284_211r.jpg): a simple substitution of Greek-like signs, with a few homophones (a =
q or y, e = ω or 6, i = υ or 7, o = τ or 3, u = φ or 4), and z/&/con signs. Twenty word signs follow (ora, al, ant,
assi, bien, buen, como, el, es, la, le, lo, muy, mas, no, por, para, pero, que, quan, su, yo), then a nomenclator
of names 50-94 (50 el Papa, 51 su Sanctidad, 52 el Rey de España, 53 su Mag., 56 la Reyna de Escocia, 57 la Reyna
de Ynglaterra, 64 el Card. de Como, 69 el Doctor Alano, 70 Fran.co Englefilol, 74 Yngalaterra, 79 Roma, 82 Madrid
...), nulls, a doubling sign, and symbols for señor, nuestro, cartas, escudos and so on. The key is DECODE's
"key attached" (it was cut out as DOC_R119_D284; DOC_R119_D1354 is the address leaf f. 209v).

Every cipher run on the four pages has a contemporary decipherment written letter by letter above it. Spot
checks against the key agree: χ ω = d e, 69 = Alano, 74 = Ingalaterra, 79 = Roma, 82 = Madrid, 51/52 = su
Sanctidad / el Rey. The one run with no gloss is a single sign group at the end of f. 210r line 4 ("no he querido
ϕ[...]", partly lost in the hole in the leaf). The gloss is "u", perhaps "usar", and it is left unread.

plaintext.txt holds the glossed runs (307 words, measured). The clear text was read from the images but not
transcribed in full.

## Prior art

- Read at the time (interlinear). Not in Knox, *Letters and Memorials of William Allen* (1882) (grep of the
  archive.org text: only Englefield→Allen 1581 and →Hesketh 1596). No edition was found on the web. It may be
  calendared or quoted in the Englefield or Allen literature (Loomie, *The Spanish Elizabethans*, 1963).
- DECODE metadata to correct: sender Englefield not the Vescovo di Lodi; receiver Cardinal of Como; date
  1584-11-15; place Madrid; status Decrypted (interlinear); cipher type simple substitution with nomenclator.

Removed from the catalogue 21 Sept 2026 (id 247).

## 14 Nov 2026: the cipher has no transcription, and why (audit section I, "no transcription file")

- In the folder: `plaintext.txt` is the contemporary interlinear decipherment, not the cipher. No file holds the figures.
- DECODE R119, public record page: four images (I880-I883) and two attached images (D284 `211r.jpg`, D1354), no text
  attachment. The file server gives a logged-out user a placeholder ("Insufficient permissions to see the full image").
- The Vatican archive does not publish Segr. Stato, Spagna 31 online. The `img/` folder named above is git-ignored and
  is not in this checkout.
- So the cipher could not be transcribed in this session. `outcome.texts[0].transcription_missing` says so and what
  unblocks it: the four images (DECODE login or the main checkout's `img/`). The cipher is in figures and the key sheet
  is f. 211, so a transcription made then can be checked by decoding against the interlinear decipherment.
