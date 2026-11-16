# Philip IV to the Marquis of Santa Cruz, governor of Milan, Madrid, 6 December 1630 (catalogue 725)

Status: read (Brice Dudout, 28 Oct 2026; Daniel's rule: 1,162 of 1,171 words read from the sense, 99.2%; key validated narrowly on a held-out letter, 0.752 of words / 0.857 of characters; a plain-text draft may survive at Simancas, not consulted).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Write-up prepared for
https://bdudout.github.io/europe-chiffree/en/documents.html#santacruz-1630 (not yet online: GitHub account suspended at the time of writing).

## Document

Archivo Histórico de la Nobleza, Toledo, SANTA CRUZ, C.50, D.213 (PARES 12877198, images 32–38).
6 December 1630; signed original, 7 pages, “sin descifrar”. Madrid → Milan.
Sender: Philip IV. Recipient: Álvaro de Bazán, 2nd Marquis of Santa Cruz, governor and captain general of the State of Milan.
PARES record and images: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/12877198. Images are not reproduced here.

October 1630: before besieged Casale, the French and Spanish armies are about to fight when a young papal envoy, Giulio Mazarini, rides between the lines and wrests an agreement. On 6 December Philip IV answers his governor of Milan, the Marquis of Santa Cruz, in cipher: he approves the agreement, which “restored the reputation” of a discredited Emperor, wants a peace concluded before March, orders a secret inquiry into the army’s unreadiness, insists that Casale and Mantua stay guarded by the Emperor and that the Milanese be fortified — “and above all do not spend a single real badly”.

## System

the royal cipher “A” of Philip IV’s letters to Santa Cruz (1629–1632), also used by the Infanta in Brussels: a homophonic syllabary (letter groups pan = ca, fan = que, sol = por…, numbers 1–99 for syllables and letters) and a nomenclator (numbers 100–260 and groups for names: 128 Emperador, 194 guerra, 222 Italia, tus paz, hon Piamonte…).

## Key and validation

- `key_K6A.tsv`: learnt by EM alignment on 14 contemporary cipher letters of Philip IV to Santa Cruz (1629-1632) with
  their contemporary decipherments ("Descifrado de D.x", same fonds), plus D.163/164 and D.175/176 (1629-1630) and the
  Infanta Isabella Clara Eugenia's cipher letter of 14 Feb 1631 (C.51, D.31) with its plain copy (D.32). Frozen (SHA-256).
- Validation on a letter never opened before (`validation/`): D.167 (29 Jan 1630) was transcribed and frozen after the
  key, then its contemporary decipherment was opened. Result: **0.752 of words, 0.857 of characters**, against a 99th
  percentile of 0.257 / 0.591 for 200 permuted-value control keys. The pre-registered criterion (0.75 words / 0.85
  characters) is met, narrowly. The previous key K5 (without the Infanta's letter), measured on the same letter outside
  the protocol, gives 0.743 / 0.857. Earlier held-out checks of K5: D.163 0.842 words, D.175 0.871, D.31 0.705.

## Reading

First published reading, to our knowledge; the original letter is marked “sin descifrar” and we know of no contemporary decipherment and no edition; a plain-text draft may survive at Simancas, not consulted (see the caveats). Rule applied: Daniel Bourdeau’s, 95% of the words read from the sense. Enciphered part: 1,171 words. Certain: 1,112 (95.0%). Probable {x}: 28 (2.4%). Restored from the sense [x]: 22 (1.9%). Unresolved ‹…›: 9 (0.8%). Words read from the sense: 1,162 / 1,171, 99.2%. Key validation on a held-out letter: 0.752 of the words, 0.857 of the characters (threshold 0.75 / 0.85, met narrowly).

Counts follow Daniel's rule (CONTRIBUTING.md): certain 1,112; probable {x} 28; restored from the sense [x] 22;
unresolved ‹…› 9. "Certain" means every syllable or code of the word has an attested value in the pairs; the choice
between homophones that the key does not separate well is made by the shape of the word. The mechanical decoding with
K6A (`decryption.txt`) leaves 56 of 2545 groups without a value.

Files: `transcription.txt`, `decryption.txt`, `reading.md` (Spanish), `translation.md` (English), `key_K6A.tsv`, `validation/`.

## Justification of the probable and restored words

- **{francés} ×2, {franceses} ×6.** Code 155, eight times. It occurs in no letter of Philip IV deciphered at the time, but the Infanta Isabella Clara Eugenia’s cipher letter to Santa Cruz (14 February 1631, same key) and its contemporary decipherment render it “franceses” (“que los franceses”). The context requires it everywhere: the army trying to relieve the citadel of Casale, the places held from the Duke of Savoy.
- **{Alemania} ×2.** Code 152, never seen in a pair. “encaminen las tropas a …”, “esta gente que hubiere de pasar a …”: the imperial troops are going home; no other name fits. “Alemania” is written fel (attested) elsewhere in the letter: the clerk had two forms.
- **{veinte}, {veintinueve}, o{ctub}re.** Date of the dispatch brought by Senator Vilani. The figures are hard-to-read literal numbers (the middle group ‹29› remains unresolved); the month is certain from the context (the Casale agreement dates from 26 October 1630). The PARES record speaks of the “suceso de 26 de octubre”: the exact date of Santa Cruz’s letters remains uncertain.
- **{gran} (cuidado).** Homophone attested only once in the pairs; “con gran cuidado y deseo” is a chancery formula.
- **me{dios}, vo{lve}r, enten{di}do, trin{che}ras, ad{vi}rtiendo, {fi}delidad.** One syllable of each word has a rare homophone (fewer than three occurrences in the pairs); the rest of the word is certain and only one Spanish form is possible (“los medios de paz”, “volver a tratar”, “teniendo entendido”, “las trincheras”, “advirtiendo que”, “jurado … fidelidad”).
- **{lo} ×2.** Homophone attested once; “procurar que lo que se pudiere ganar” and “que lo que se pudiere ganar”: the syntax requires the neuter article.
- **{fortificando}.** Word code seen only once in a pair, followed by “lo”: “se disponga fortificándolo con toda diligencia”; the end of the letter returns to the fortification of the Milanese.
- **{demostración}.** Code seen once; “obliga a una gran demostración” (an exemplary sanction) follows the report of the army’s shortcomings and precedes the order to investigate.
- **{ambas}.** Syllables with rare homophones; “que ambas plazas y la de Mantua” repeats “en ambas plazas”, written earlier with certain values.
- **{esos}, {pueda}, {conveniente}.** Homophones attested only once; “dentro de todos esos estados y feudos imperiales”, “que se pueda ver en los efectos”, “porque es conveniente que vos y el duque de Feria”: only one grammatical reading.
- **[despachos], [halló], [villa], [cuenta], [cuidado], [esto], [muchas], [se], [la], [y] ×3, pudiere[is].** Words left out by the clerk (no cipher group at that point) or abbreviated; restored from the construction: “hacer los despachos para la paz”, “la resistencia que allá halló en el mío”, “la villa y castillo de Casal” (against “la ciudadela”), “dio cuenta”, “poniendo en ello tal cuidado”, “asentado esto”, “de muchas maneras”, etc.
- **[gran] ×2.** Left out in “mirar con [gran] atención” and “es [cosa] de [gran] peso”; the same formula occurs elsewhere in the letter (“con gran secreto”, “con gran rigor”).
- **[cosa], [de hacer], re[novar la].** “es cosa de gran peso”, “la guerra que se ha de hacer”, “que no nos deje a renovar la guerra”: groups missing or truncated in the cipher; the sense is imposed.
- **[de Saboya].** Code 115 means “duque [de Saboya]” in the pair D.193↔D.194 (19 June 1630); here “Respondo al duque … a las cartas que me ha escrito”.
- **[concluido], [paz], [seguridad].** Word codes never seen in a pair (R02, N, bor), replaced by the only word the sentence admits: “como si no se hubiere concluido”, “ganar en la paz”, “mirar por la seguridad de ese Estado”. We count them as restored, not as read.
- **‹…› unresolved.** Nine words: ‹29› (in the date), ‹lor› ‹nat› (“dio cuenta aquí … el senador Vilani”), ‹dol› ×2, ‹dul› (the Infanta uses it for “quando” and “assi”, neither fits here), ‹mur›, ‹fri›, ‹28›. We propose nothing.

## Caveats

- Criterion met narrowly. The frozen key reads 0.752 of the words and 0.857 of the characters of the test letter, against a threshold of 0.75 / 0.85. The starting key (K5, without the Infanta’s letter), measured outside the protocol on the same letter, gives 0.743 / 0.857: the gain is marginal.
- A wrong PARES record. Image 6 of unit 12877137 bears the shelfmark D.168, which PARES describes as a cédula to the Marquis del Viso; it is in fact the contemporary decipherment of D.167 (“de que la república quería estar neutral…”), which served as our test letter.
- A possible plain-text draft, not consulted. The chancery usually kept the plain-text draft (minuta) of the King’s letters to the governors of Milan in the Estado, Milán bundles at Simancas (AGS, legajos c. 3338–3340 for 1630). These bundles are neither described item by item nor digitised; we do not know whether the draft of this letter survives. If it does, it will check the probable and restored words.

## Decrypt audit, 16 Nov 2026

The audit (`research/decrypt_audit/`) applied `key_K6A.tsv` to `transcription.txt` and compared the letters with
`reading.md`: 219 of 1,112 compared words depart from what the key gives, without a mark. A separate letter alignment
of the mechanical decrypt with `reading.md` (1,169 words) gives: 896 words as the key file gives them, 75 departing
and marked ({x}, [x], ‹x›), 57 departing by spelling only, 141 departing otherwise without a mark.

Causes, with one example each:

- Normalisation (C), stated. `reading.md` says "Spelling normalised": auer > haber (h added 38 times, u > b 20),
  exercito > ejército (9), azer > hacer (8), assi > así, quenta > cuenta. 57 words depart in this way only, and many of
  the 141 carry such a change too.
- Key file incomplete (A). `key_K6A.tsv` keeps one value per token, the commonest in the aligned pairs (columns n and
  total: `fer` de 121 of 183), and drops codes aligned fewer than twice. The reading uses other values, as the Reading
  section says ("the choice between homophones ... is made by the shape of the word"), and they are in no file of the
  folder: `fer` read do ("se na de r" printed "senador", 8 times), `X` read t ("r re gu as" printed "treguas", 8),
  `q` read b or d ("o s li ga ro n" printed "obligaron", 8), `P` "caso" printed "Casal" (7), `C` "como" printed
  "comi-", "comu-" (6), `J` "co" printed "ciudad" (2). Ten codes with no row in the key file are printed as words without
  a mark, about 19 words: 104 "despacho" (3; twice more inside "mira a despedir", decryption line 203), `xol` "fo-"
  (3), `tan` "-nar" (2), `fru` "diligencia" (2), `plo` "cuidado" (2), `hon` "Piamonte", 165 "-forme", `gli`
  "buenas", 205 "importancia", 122 "esto". The pairs the key was learnt from, and the working keys named in
  `validation/score.txt` (`working/K6A_frozen.tsv`), are not in the folder, so the statement that every such value is
  attested in the pairs cannot be checked here.
- Unmarked emendation (B). Abbreviations and letters supplied without a mark: "mi s r s" printed "ministros" (3),
  final letters added ("copia" > "copias", "veni" > "venir"), and decrypted letters left out ("que se os ‹fri› z e e n
  otra" printed "que se os ‹fri› en otro", decryption line 207). These are counted within the 141; they were not
  separated one by one from the second homophone values.
- Marked words and unresolved codes (D): 75 words, nothing wrong.

Changed: `key_K6A_additions.tsv` added and listed in `profile.json` `outcome.key_file` beside the frozen
`key_K6A.tsv`, which is untouched. It holds five values that files of this folder establish, each with its source:
`hon` = Piamonte and 155 = franceses (this file, System and Justification), and from the held-out pair
`validation/D167_cipher.txt` / `D168_plain.txt`: `X` = t (line 4, "neutral"), `fer` = do (line 11, "procurando"),
`fri` = di (line 10, "ellos dicen"). No value was taken from what the reading needs.

The pair gives `fri` = di, which bears on two places of D.213 that the reading leaves open or probable: decryption
line 93 "‹fri› do" under "enten{di}do", and line 207 "se os ‹fri› z e", which would be "se os dize". The reading was
not changed; this is for a decision.

Figures after: unchanged, 219 of 1,112, because the audit applies one value per token. Not checked: the images; the
141 words one by one (classified by pattern of replacement, not read singly); whether the transcription token 104 is
one sign.

Marked on 16 Nov 2026. The 141 words were checked one by one against the key output (`decryption.txt` lines and
both key files). `reading.md` now carries 122 new [x] marks in 119 words: codes with no row in the key printed as
words ([despacho] 4, [diligencia] 2, [cuidado] 2, ga[nar] 2, [fo]rtifica- 3, [importancia], con[forme], [buena]s,
[mira a despedir]), letters from a homophone value the key files do not hold (o[b]ligaron, a[d]virtiendo, Cas[a]l 7,
com[i]sario 4, c[iudad]ela 2, en[t]regar), and letters or words supplied ([minist]r[o]s 3, [necesidad] 3 where the key
gives "e ma ne ra", [ninguna], [provisiones], [andando], [pueda]). No letter of the text was changed. Not marked: 16
words that follow the second values `fer` = do and `X` = t now in `key_K6A_additions.tsv`; the 57 words that differ by
the stated spelling normalisation, with "acción", "u", "exacciones", "vuelvan"; and places where decrypted letters are
left out or reordered, which have no letter to mark ("no se a ue r" printed "no haberse", "franceses es ∅ a ga n"
printed "{franceses} hagan", "se os ‹fri› z e" printed "se os ‹fri›", "uuestra" after "traído", "intentos" printed
"intento", "se trata" printed "[se] ha de tratar"). Words the alignment did not flag were not re-read. Header changed:
`reading.md` Conventions line extended. `v2_score.py` on `reading.md`: hole rate 0.023 before, 0.115 after (each word
holding a bracket counts as a hole). On the page, the sentence "1,112 are certain ..." was reworded; its counts were
not recomputed.


Placement of the marks (same day): the reading is the contributor's (Brice Dudout), so `reading.md` was put back as he gave it, with corrected header lines, and the marked text is the companion file `reading_marked.md`. Where this section says the marks are in `reading.md`, read `reading_marked.md`.