# Matthias Corvinus to Ercole I d'Este, Pozsony, 1 June 1482 (DECODE R1156)

Status: read. Already in print; checked here against the glyphs, and four garbled passages in the printed text corrected.

- **Shelfmark.** Modena, Archivio di Stato, Cancelleria, Carteggio principi esteri (CPE) 1622, b. 1/3, nos. 2, 2a.
  DECODE R1156 ("Partially decrypted", 1 p., graphic signs, images need a login). Two images: I5815 is the letter,
  I5816 the verso with the address and the red seal. Images are in `img/`, git-ignored because the archive
  holds the rights.
- **Sender, recipient.** King Matthias (Hunyadi Mátyás) to Duke Ercole I of Ferrara, his brother-in-law (Eleonora of
  Aragon, Ercole's wife, was sister to Queen Beatrix). The letter was written five weeks after Venice had opened the
  War of Ferrara (May 1482). Matthias was fighting Frederick III at the same time.
- **Language.** Latin. The cipher runs are Latin too, not Italian as DECODE has it.

## Prior art: printed in 1877 and 1895

Fraknói Vilmos, *Mátyás király levelei. Külügyi osztály* II (Budapest 1895), no. 131, pp. 232–233
(`fraknoi_v2.pdf`, from MEK 07105, `fraknoi_v2.txt` for search). He prints the whole letter from the Modena
original ("Eredetije, mely részben titkos jelekkel van írva", i.e. "the original, partly written in secret signs"),
after *Magyar diplomácziai emlékek Mátyás király korából* III (1877), no. 14. So the cipher was read in the 19th century.
DECODE's "partially decrypted" means only that nobody has entered a transcription.

The printed text has "(így)" (sic) at three places and runs into nonsense at the end ("Speramus nos eos nostris contra
dispositiones ut meliori postea modo possemus (így)"). It prints the last sentence only as a "contemporary regest at the
end of the letter": "Rex Hungarie scripsit regi Ferdinando, quomodo possent diverti Veneti et confundere eos et cum
paucis pecuniis". The verso (I5816) has only the address and the seal. Either that decipherment is on leaf 2a, which
DECODE did not image, or it is the letter's own last line, which is half in cipher.

## The cipher

Letter-for-letter substitution with homophones for the common letters, plus a few nomenclator signs for names. The
signs are invented shapes, some borrowed from Latin letters and numerals (5, 4, 9, 2, 3, 7, 8, reversed C, L, T, ⊥,
Ŧ, Π, Λ, ⊏, ⊐, ∃, ∅). About 15 runs of cipher are set into clear Latin, roughly 330 signs in all. Doubled letters are
written as a sign between dots (·ıı· = tt).

Working key, from runs aligned with the printed text and checked on at least two words each:

| letter | signs (as they look) |
|---|---|
| a | 8, V |
| b | d |
| c | reversed C (Ͻ/⊃) |
| d | 2 (in *dispositu-ros*, *diverti*), ᑐ |
| e | 5, 4, 9, ς |
| f | ϵ (one instance, *confundere*) |
| g | ᒪ (hooked L) |
| h | 6 |
| i | 2, 3, ∅ |
| l | σ / Ω, ᒧ |
| m | ⊐, ᑐ |
| n | ⊏, ϲ |
| o | 7, Π, Λ, + |
| p | ⊔ |
| q | = |
| r | Ŧ |
| s | L, Γ, S |
| t | ⊥, + |
| u / v | ⊤, ∃ |
| tt | ·ıı· |

Nomenclator signs: ⅋ (a looped "&") = *Veneti / Venetorum*; ⊠ (a crossed square) = *regi Ferdinando*;
ꝗ (a q with looped tail) = *Rex Hungarie*, i.e. Matthias himself (the printed text expands it this way).
Some signs do double duty (+ as o, t and e; 2 as i and d), so the key is not a clean one-to-one table.
The sample is too short to split them.

## The cipher runs, read

Line by line, clear text in roman, cipher runs in [brackets] with the reading:

1. … statim cum domina regina consorte nostra statuimus [mittere] in [subsidium] [vestrum] [quingentos]
2. [equites] inter [quos] essent [centum] [usarones], idest [homines] levis [armatu-]
3. [-re], qui plus [ceteris] **[valent]**. Sed cum examinaremus cum domina regina ⟨2 signs⟩ et
4. [aliis] nostris per [quam] [viam] possemus [eos] [mittere], non invenimus aliquam [tutam] …
5. … Scripsimus … [modum] quo [tuto] modo possent. Libenter [mitteremus] …
6. In crastinum hinc recedet [Mager] [Balas] [capitaneus] [noster] cum **[pluribus] [gentibus]**, iturus in
   [Croatiam] versus [confinia] [⅋ = Venetorum], ubi [plures] etiam [congregabit]; et quotienscunque inventa erit
   [tuta] [transeundi] [via], statim significet(ur?) [ꝗ] et illic faciet [ꝗ] **[venient]**.
7. **Speramus cito nos [res] [nostras] ita [disposituros], ut meliori postea modo [vos] [iuvare] possemus.**
8. **[ꝗ = Rex Hungarie] [scripsit] [⊠ = regi Ferdinando] quo(modo) possent [diverti] [⅋ = Veneti] et [confundere]
   [eos] et cum paucis [pecuniis].** Dat. Posonii, p° Junii 1482.

## What is new here (corrections to Fraknói no. 131)

1. "qui plus ceteris **valoris** (így)" → the cipher spells v-a-l-e-n-t: **qui plus ceteris valent** ("who are worth
   more than the rest"), said of the hundred hussars.
2. "cum pluribus **servis**" → g-e-n-t-i-b-u-s: **cum pluribus gentibus**, i.e. Balázs Magyar leaves with a large force,
   not with servants.
3. "Speramus nos eos nostris contra dispositiones ut meliori postea modo possemus (így)" → **Speramus cito nos res nostras
   ita disposituros, ut meliori postea modo vos iuvare possemus**: "we hope soon to have our own affairs so arranged that
   we can then help you better". The printed text lost *cito*, misread r-e-s and n-o-s-t-r-a-s, rebuilt
   d-i-s-p-o-s-i-t-u-r-o-s as "contra dispositiones", and dropped v-o-s i-u-v-a-r-e altogether.
4. The "contemporary regest" is the letter's own last sentence, half in cipher: [Rex Hungarie] scripsit [regi Ferdinando]
   quomodo possent diverti [Veneti] et confundere eos et cum paucis pecuniis. (The printed regest words are right.
   The point is where the words come from.)

Uncertain: "illic faciet ꝗ venient". The printed text has "convenire". The glyphs read ꝗ + v-e-n-i-e-n-t, so ꝗ may
here stand for *quod* or *con-*. The clear verb before the first ꝗ looks like *sufficietur*, which the printed text
gives as *significet*. Neither point changes the sense: Balázs is to tell the king as soon as a safe road is found,
and the troops are to meet there.

## Open point (14 Nov 2026): three values against the key rebuilt for beatrice1482

Brice Dudout (PR #620) rebuilt the key of the queen's letters of 31 May and 8 June 1482 to Eleonora
(`targets/beatrice1482/vestigia/`) from their clear copies of the time. It is this alphabet: sixteen letter values
are the same (a 8/V, b d, c reversed C, h 6, i 3, l σ, m ⊐, n ⊏/ϲ, o 7/Π/Λ, p ⊔, q =, r Ŧ, s L, t ⊥, u ⊤, tt ·ıı·)
and both have a looped q-sign for the King of Hungary, seventeen shared values in all. Three values differ:

| letter | here (R1156) | beatrice1482 (R1140, R1141) |
|---|---|---|
| d | 2 (*disposituros*, *diverti*), ᑐ | 9 (33 places in R1140; held out on R1141) |
| g | hooked L | 2 (10 places in R1140: *grande*, *liga*) |
| e | 5, 4, 9, ς | one ϟ/5-like sign |

On the 648 signs of R1141, which the beatrice key was not built on, 9 = d and 2 = g give 0.900 of the characters of
the printed text; 9 = e with 2 = d gives 0.833 and with 2 = i 0.843 (integration check of PR #620). So for the
queen's letters 9 = d and 2 = g hold. For R1156 it cannot be settled from this folder: no sign-by-sign
transcription was kept, the images are git-ignored and behind the DECODE login, and the table above was drawn from
about 330 signs, with "2 as i and d" already noted as doing double duty. The likely explanation, not checked, is
labelling: the sign called 2 in *disposituros* and *diverti* may be the 9-shape, and the 9 read as *e* may be a
form of the 5-like sign. **The key above is left as it was.** To settle: re-read the d, e and g places of R1156
on the image against the beatrice sign inventory (`targets/beatrice1482/vestigia/sign_inventory.md`).

Seventeen shared values, the same court, the same week and the same household at Ferrara make this one key with
beatrice1482. The two targets are cross-referenced and **not folded**; the fold under the one-key rule is left to
the owner.

## Files

- `decode/rec1156.htm`, `decode/view1156.json`: DECODE record and metadata (jwt.txt git-ignored).
- `fraknoi_v2.pdf` / `.txt`: Fraknói vol. 2 (git-ignored, 29 MB; MEK 07105).
- `img/`: DECODE images and working crops (git-ignored).
