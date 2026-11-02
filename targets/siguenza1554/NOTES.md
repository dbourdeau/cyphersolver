# siguenza1554: Pedro Pacheco, cardinal of Sigüenza, to Antoine Perrenot de Granvelle, bishop of Arras, Naples, April-June 1554 (BNE MSS/20214/61/1-6)

Catalogue #855. Contributed by Michael Brackx; the work was done with Claude Code under his direction, 2 Nov 2026.

The catalogue row says "No decipherment mentioned". In fact every cipher passage found in the letters carries a
decipherment written at the time, between the lines or in the margin. Those decipherments are transcribed here as
the reading. The cipher itself (887 signs in five letters) is transcribed sign by sign. The key, a syllabary of
consonant signs with vowel marks, is rebuilt from the alignment of cipher and decipherment, and the decoder,
applying it, gives the same syllables over most of the text. Every passage reads, from its decipherment, and the key
gives a value to 98% of the cipher tokens (873 of 887), so the target is read. The key is partial: 85 tokens print
two values, four more signs are ambiguous but decoded with one value (look-alike signs; `key_1554.md`), and 11 rare
sign types have none (see Remaining gaps). Pacheco's letters of January-March 1554 in the Real Biblioteca, Madrid,
use the same key; their cipher (626 signs in four letters) is transcribed in `siblings/rb2251/` and confirms and
extends the key (see Siblings).

Sign names in backquotes (`ꝗ`, `ꝺ̶`, `ʒ` …) are conventional Unicode look-alikes for the cipher signs; their values
are in `key_1554.md`. Letters and numbers like A1, B2, C3 are the line labels of the transcription files.

## The letters

BNE Digital bdh0000172763, "Cartas del Cardenal de Sigüenza al Cardenal Granvela", MSS/20214/61/1-6, 13 leaves. The
BNE record names the writer: Pedro Pacheco y Guevara (1488-1560), cardinal of Sigüenza, viceroy of Naples
1553-1555. The address leaves (61/3 to 61/6) read "Al muy Ill.e y R.mo señor el S.or obispo de Arras, del consejo
secreto de Su Mag.d": Antoine Perrenot de Granvelle, then bishop of Arras and Charles V's minister (cardinal only from 1561).
The record also cites M. Van Durme, "Notes sur la correspondance de Granvelle conservée à Madrid", *Bulletin de
la Commission Royale d'Histoire* 121 (1956); that article was not seen. No edition or study of the cipher was found.

| doc | shelfmark | date | cipher | decipherment of the time |
|---|---|---|---|---|
| d1 | MSS/20214/61/1 | Naples, 4 Apr 1554 | 12 lines, 193 signs | interlinear (A, R, P), margin (B) |
| d2 | MSS/20214/61/2 | Naples, 9 May 1554 | 5 lines, 43 signs | margin |
| d3 | MSS/20214/61/3 | Naples, 15 May 1554 | 22 lines, 337 signs | margin (f. 1r: faint on image 1, legible on image 2, a second photograph; inner spread) |
| d4 | MSS/20214/61/4 | Naples, 24 May 1554 | 21 lines, 292 signs | margin (I, J, K, L), interlinear (N) |
| d6 | MSS/20214/61/6 | Naples, 11 June 1554 | 2 lines, 22 signs | interlinear |

61/5 (Naples, 2 June 1554) has no cipher. Every image of the six letters was viewed; the cipher pages at full size.
The address leaves (61/3, 61/4, 61/5, 61/6) name the recipient only ("Al muy Ill.e y R.mo señor el S.or obispo de
Arras, del consejo secreto de Su Mag.d"), with no place. So `profile.json` gives no `places` for the atlas: where
Granvelle received the letters (probably Brussels, with the emperor) is not on the documents.

## Sources

BNE Digital (images CC BY 4.0, Biblioteca Nacional de España). The "high" PDF of each letter holds one JPEG per
page or spread, about 1050 x 1400 px a page. The JPEGs were taken out of the PDF and cropped. The lines were read on
crops at 2-4.5x. Some crops follow the slope of the line (61/2). Others are side-by-side galleries of one sign (61/3).

BNE Digital blocks a client that requests many records quickly: fetch one record at a time. A plain download of
the PDF URL returns an HTML page; the PDF loads in the viewer page.

## The system

The cipher is a syllabary of the Spanish chancery type (`key_1554.md`). Its signs fall into four kinds:

- **A consonant sign with a vowel mark.** A tail marks *a* (`∇ꝶ` *ha*, `bꝶ` *fa*, `∂ꝶ` *la*). A bar through the
  sign, or bars on both sides, marks *e* (`ꝺ̶` *te*, `─x─` *de*). A dot above or a bar before marks *i* (`q̇` *di*,
  `─ꝺ` *ti*). The plain sign is *o* (`∂` *lo*, `x` *do*). A small circle marks *u* (`f°` *pu*, `8°` *cu*, `5°`
  *bu*). This is a model that fits most signs, not a table found in the source.
- **Signs for a syllable or a short word:** `c` *que*, `o-o` *no*, `ʒ` *yo*, `A` *po*, `◻` *tra*, `ẋ` *pli*,
  `ꝗſ` *qua*.
- **Single letters:** `tt` *e*, `Ω`/`oʒ` *n*, `h` *r*, `b`/`t`/`ȯ` *s*, `M` *a*, `4` *y*.
- **Code groups:** `3z` *dinero*, `43` *ducado*, with a plural `43b` *ducados*; `gua` *armada*, `troꝶ` *guerra*,
  `si` *amigos*, `ụʒ` *Sena* (Siena), `ros` and `ιos` *su Mag.d*; a sign shaped like the clear word "de" stands for
  *aqui*. Most are seen once, at the place where the decipherment has the word.

Dots set off groups; they are not word dividers. The transcription has 138 kinds of sign. Many are a base sign
with a mark, and a few are probably one sign transcribed in two ways.

## How it was read

1. Every cipher passage was located and its decipherment of the time transcribed: interlinear words or a running
   text in the margin.
2. The cipher of each passage was transcribed sign by sign and aligned with its decipherment, at first by letters
   (failed: too few signs for the letters), then by syllables (worked). Letter 2 aligned first, sign for sign
   with nothing left over (*yo me hallo confuso en hallarme en este tienpo tan falto de dinero*). From it came the
   consonant-plus-vowel structure.
3. The key grew letter by letter (1, 2, 3, 4, 6). The independent checks are the repetitions across letters, where
   the same signs stand for the same words: *halla*/*hallo*/*hallarme* (letters 2, 3), *podello* (1, 3), *dinero*
   `3z` (2, 3), *es verdad* `tt b ꝗ̶ h ꝓ 5` (3, 4), *necessidad* `oo . u . ꝺ̵ x ꝶ` (3, 4, three times),
   *estrangera* `tt b . ◻ oʒ` (1, 2), *de donde* `q . ʒ Ω ꝺ̶` (letter 1, twice), *tienpo* (1, 2).
4. Signs read as one thing in one letter and another elsewhere were cropped side by side at 3-4.5x. Splits found
   this way: `ꝗ̶` *ve* against plain `ꝗ` *vo*; `∂ꝶ` *la* against `∃ꝶ` *sa*; `aꝶ̶` *ll* against `aꝶ` *ra*; `Ω`
   *n* against `ꝺ`. Letter 1 was then read again at full size, which removed most of its first-pass conflicts.
5. The tokens left without a value were aligned one by one with their decipherments; 39 of 56 took a value,
   several as the vowel-mark model predicts (`ɓ` *fo* beside `bꝶ` *fa* and `b°` *fu*; `─ꝗ─` *ve*; plain `∇` *ho*;
   plain `n` *g* beside `n̄ꝶ` *ga*; `r°` *du*), the rest as code groups.
6. The signs still read two ways were compared again side by side across letters: the *yo* sign (a large Ʒ) and
   a small hooked z, `ɀ` *do* (*donde* twice, *acabado*, *donativo*, *haviendo*, *ducados*), are two signs, the
   *d* base of `ɀꝶ` *da*; plain `ꝺ` is *l* in 22 of its 31 places; `x` (*i*/*y*) and `ꝯ` (*(h)a*) are one value
   each; the `ı` of A2 is a comma. D6 was read again in full (*en sus tramas y intelligencias*). Two-valued
   tokens fell from 126 to 62 (they rose to 85 again at step 7, when plain `ꝗ` was given two values, *que/vo*).
7. Pacheco's letters in the Real Biblioteca (II/2251) were found to use the same key and transcribed (see
   Siblings). Their decipherments confirmed values met once in the BNE letters and showed that plain `ꝗ`, as transcribed,
   covers a *que* sign as well as the *v* sign.
8. `dec1554.py` decodes each transcription with the key, without hand corrections
   (`decryption/dN_decode.txt`). Where a sign keeps two values it prints both (`te/de`).

How far the decode gives the decipherment's syllables, by passage:

| passage | agreement |
|---|---|
| d2 C1-C3 (*yo me hallo … tan falto de dinero*) | full |
| d3 D1, d4 N3 (*es verdad*) | full |
| d1 R1 (*acabado*) | full |
| d1 A2, B1-B3, R2-R4, P1-P2 | most |
| d3 E1-E3, F1-F2, G1, G3, H1-H6 | most |
| d4 L1-L2 | most |
| d1 A1, A3; d3 D2-D6, F3-F4, G2; d4 I, J, K, N1-N2, N4-N5; d6 X1-X2 | in part |

A person checked one passage against the image without AI help: Michael Brackx, 2 Nov 2026, letter 2 lines C1-C3
(*yo me hallo confuso … tan falto de dinero*) and the margin beside them. He counted the signs strip by strip (5, 10,
10, 7, as transcribed), compared the repeated signs of *hallo*/*hallarme* and *me*, and read the margin. Result:
confirmed (`profile.json` `outcome.human_check`). He also noted that the *a* tail of `∇ꝶ` is f-like (ſ); see
`key_1554.md`, Note on the a-tail.

This agreement is not an independent proof: the key was rebuilt from the same decipherments. The repetitions
across letters, listed in step 3, are the independent evidence. The reading itself is the decipherment of the
time, transcribed.

## Reading

`decryption/dN_reading.md`, with English in `decryption/dN_en.md`. Clear words of the letter are in parentheses, for
sense; "…" marks clear text left out; `[…]` marks words not read. Each paragraph is one passage, in the order of the
transcription: d1 A1-A3, B1-B3, R1-R4, P1-P2; d2 C1-C5; d3 D1-D3, D4-D6, E1-E3, F1-G3, H1-H6; d4 I1-I4, N1-N5,
J1-J6, K1-K4, L1-L2; d6 X1-X2.

Content. Through April-June 1554 the viceroy writes from Naples to Granvelle about money and troops:
- d1: the donative, whether the enemy fleet (French or Turkish) will come, the need for foreign troops because the
  people of the kingdom cannot be trusted, and the lack of means;
- d2: he is at a loss, so short of money, and above all without foreign troops;
- d3: the Prince of Salerno (Ferrante Sanseverino, in the French service) is still at Castro and wants to come to
  Sermoneta ("Salmoneta") to pursue his plots more easily; no buyers can be found for the crown's annuities: only
  2,500 ducats have been sold at ten per cent redeemable; he would sell up to 25,000 ducats at that price if
  buyers could be found;
- d4: things are getting tighter, if the Venetian ambassador's news is true; 70,000 ducats a month will go on the
  war of Siena and the kingdom; the excesses of the troops; "lo de Ingalaterra";
- d6: it cannot be borne unless the emperor provides.

Siena was besieged by the imperial and Florentine forces from January 1554. "Lo de Ingalaterra" is probably the
marriage of Prince Philip and Mary Tudor (July 1554).

## Siblings: Real Biblioteca II/2251

Pacheco's letters to Granvelle of 5 and 17 January, February and 30 March 1554 in the Real Biblioteca (II/2251,
ff. 22-24, 72-73, 110, 243-244; IIIF images about 2700 px wide) carry cipher in the same key, with decipherments of
the time in the margin or between the lines. The H15Corpus (GRANVELA-H-0032, 0033, 0036, 0044) transcribes these
letters and their decipherments, and marks the cipher only as "[mensaje cifrado]". The cipher is transcribed here sign
by sign (`siblings/rb2251/`, with its own readme). These letters are not documents of this target; they serve as
evidence for the key:

- Before they were read, the key built from the BNE letters gave a value to 86% of the 590 signs first transcribed,
  and the decodes followed the decipherments over long runs (*fue su costumbre y es y sera mientras*; *hasta que el
  matrimonio*; *que venga seguro y*).
- Values met once in the BNE letters recur where the decipherment needs them: `ụʒ` *Sena*, `ιos` *su Mag.d* (four
  more times), `de` *aqui*. The split of `ʒ` *yo* and `ɀ` *do* holds.
- Signs the vowel-mark model predicts appear where the decipherment needs them: `ꝺ°` *tu*, `-d` *mi*, `dꝶ` *ma*,
  `◻̇` *tri*, `fꝶ` *pa*, `nꝶ` *ga*.
- Plain `ꝗ`, as transcribed, reads *que* in some places (*y que ninguno*, *y que no*, *porque*, *que venga*) and *r*,
  *vo* or *lo* in others. Side by side on the sibling images, the *v* syllables turn out to be mostly the barred `ꝗ̶`,
  a sign of its own; but the plain two-storey `ꝗ` has the same shape where it reads *que* and where it reads *r* (both
  in H32a), and a small 9-like q (*lo*) was also written `ꝗ`. The values are not separable by shape at this
  resolution.
- New code groups: `ιoz` *su Santidad* (against `ιos` *su Mag.d*), `42` *duque*, `36` *(el) duque de Florencia*,
  `iz` *cardenal*, `ꝗz` *Ingalaterra*.

With these values the key gives a value to 97% of the sibling signs (608 of 626). The H15Corpus lists the letter of
30 March 1554 (GRANVELA-H-0044) under 1556; its date is on f. 244v. The decipherments in the sibling files follow
the H15Corpus transcriptions, checked on the images; the H15Corpus states no licence, and its citation form is
given in `siblings/rb2251/readme.md`.

## Remaining gaps

- Look-alike signs: `ꝺ̶` (*te*/*de*/*re*), `ụ` (*c* with an unseen vowel), `ꝸ` (*re*/*co*/*a*), `ꝺ̵` (*se*/*si*), plain `ꝗ` (*que*, *r*, *vo*, *lo*; not separable by shape), and `ʒ` in five places of letters 3-4 that want *do* (probably `ɀ`) keep two values: 85 tokens - blocker: illegible; at 12-15 px a sign the BNE scan does not separate the forms, and it is the only image; a side-by-side comparison on the sharper sibling images did not separate plain `ꝗ` (see Siblings)
- 11 sign types (14 tokens) without a value (`f`, `ffoꝶ`, `f̈`, `m`, `ova`, `°`, `ŧ`, `ʳ`, `⊳`, `ꝗ̈`, `ꝶ̃`) - blocker: too-short; each is met once or twice where the alignment does not fix a value (`°` may be a null)
- Code groups seen once (`gua` armada, `troꝶ` guerra, `si` amigos, `ros` su Mag.d; in the siblings `iz` cardenal, `ꝗz` Ingalaterra, `5ı` españoles, `ge` alemanes) and the sibling number `25` (*(ca)vallos*) - blocker: too-short; each valued from the decipherment at its one place
- d4 J1-J6, K1-K4, single signs read at 2-2.6x - blocker: illegible; the margin text is clear, the scan limits the cipher
- d4 N1-N5, the interlinear notes transcribed only roughly (*las ven[…]*, *otro[…]* in L1) - blocker: illegible
- The key's structure (consonant sign plus vowel mark) is inferred; several signs do not follow it - blocker: too-short; most signs occur once or twice

## Escalation

- [x] siblings: all six letters of MSS/20214/61 viewed; five carry cipher, all with decipherments of the time.
  Pacheco's thirteen letters of 1554-1555 in the Real Biblioteca, Madrid (II/2251; H15Corpus GRANVELA-H-0032 to
  0044) viewed: four carry cipher in the same key, with decipherments of the time, and are transcribed in
  `siblings/rb2251/` (37 lines, 626 signs). The volume also holds a letter of the viceroy of Sicily almost wholly in
  cipher (f. 182r), another correspondence, not worked. Pacheco's other letters to Granvelle in the Real Biblioteca
  (II/2322, II/2325, II/2258; Rome 1552-1553) are not checked
- [x] clear-pages: the decipherments of the time are on the same pages (interlinear and margin); 61/3 f. 1r has a second photograph with the margin legible
- [x] known-keys: Tomokiyo's list of Spanish ciphers (cached upstream in `targets/vasto1527/prior/spanish2C_now.htm`)
  searched: no Pacheco or Sigüenza key (its "Cardinal Pacheco" is Francisco Pacheco, a 1566 cipher). Pich-Ponce's
  PP1-PP3 (Granvelle-Renard, Saint-Mauris) are other ciphers. The structure (base sign plus vowel marks,
  letter-word codes such as `o-o`) is that of Charles V's syllabic ciphers, as is the Imperial Cipher of 1544-1554
  of `vargas1552`, whose short-word codes (`s-o` *el*, `x-o` *del*, `n-o` *al*) have the same shape. No code group
  is shared among the few known, and that key's full table (Meister 1906, Bertomeu Masiá 2009) is not in the
  repository, so the identity is not tested
- [x] print: web search (2 Nov 2026): no edition or study of these letters' cipher. Martín Aizpuru, *Onomázein*
  (2025), studies forty letters of Pacheco and Bolea to Granvelle (1551-1557), but those are in the Real Biblioteca
  (Granvela collection, H15Corpus), not the BNE, and her study is linguistic. Bucuré, *Estudios Románicos* 34
  (2025), studies the Naples cipher of 1547 (Pedro de Toledo), not compared. Van Durme 1956, cited by the BNE
  record, not seen
- [x] key-rebuild: syllabary rebuilt from the alignment with the decipherments
- [x] retry: letter 1 re-read at full size after the key was built from letters 2-4; look-alikes compared side by side

## Next steps (ranked)

1. Ask BNE for better images of the cipher pages, to separate the look-alike signs.
2. Check Pacheco's Rome letters of 1552-1553 in the Real Biblioteca (II/2322, II/2325, II/2258) for cipher in
   this key, for second occurrences of the code groups seen once.
3. Compare Bucuré 2025 (Naples, 1547) and the Imperial Cipher of 1544-1554 tables for a match.
4. See Van Durme 1956 for a printed text or key.

## Files

- `transcription/dN_transcription.md`: the cipher lines (label, decipherment of the time, signs).
- `key_1554.md`: the key, each value graded by evidence.
- `dec1554.py`: the decoder (`python3 dec1554.py transcription/d1_transcription.md`).
- `decryption/dN_decode.txt`: decoder output.
- `decryption/dN_reading.md`, `decryption/dN_en.md`: reading and English.
- `siblings/rb2251/`: the Real Biblioteca sibling letters: transcriptions, decodes, readme.

## Checker output (2 Nov 2026)

- `docs/_check_profile.py siguenza1554`: valid (4 unknown fields: nomenclator size, nulls, key order).
- `docs/_check_reading.py siguenza1554`: clean share 0.71 over the five readings (d2 1.0, d3 and d4 0.73, d1
  0.67, d6 0.0 on its single sentence). The weak sentences fail on period spellings the word list does not know
  (*podello*, *havello*, *cumplillo*, *fuesse*); the readings have only two explicit holes. All five translated.
- `docs/_validate.py siguenza1554 --na`: not applicable (syllabary, about 6 tokens per sign type, signs with two
  values).
- `docs/_check_writeup.py siguenza1554`: INCOMPLETE. Missing: the docs/ write-up surfaces (page, PAGES and IMAGES
  entries, README row, portrait, snip, reveal, keys.json), which are for the maintainer on merge, and the
  `reading_review` of each document, which is for the reviewer. "read" meets the read bar (98% of cipher tokens
  valued).
