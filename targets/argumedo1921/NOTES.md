# argumedo1921: Argumedo's letters to Félix Díaz, 5 and 20 October 1921 (catalogue 1445)

Status: read in part (Brice Dudout, with AI agents, 25 Nov 2026; the 25 cipher runs Narváez did not print: 32 words, 25 read as the key gives them, 7 marked encipherer slips, none unread; no person has checked the reading yet).

This target **completes Narváez's reading**; it is not a new break. Roberto Narváez broke the system and printed the
table (Documenta & Instrumenta 13, 2015, p. 122), and printed the clear of 10 runs. He wrote that the table reads the
rest but did not print it: he cut DCXXI.3.244.1 with "[...]" and gave the four f. 2 runs of DCXXI.3.250.2 in cipher
only. This target reads those 25 runs with his key, unchanged, in the way PR #941 (wellington1922, Andrew Beling)
completes his reading of the Wellington letter.

## Documents

- CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo DCXXI Archivo de Félix Díaz:
  - **DCXXI.3.244.1**: Cristóbal Mateo Argumedo ("Don Mateo", signature in cipher), Mexico City, "Octubre 5 de 1921",
    to "Señor Gral. Díaz" (in cipher). Typed, 2 ff.; received stamp "DEC 31 ANS'D".
  - **DCXXI.3.250.2**: the same, "Oct 20/21", signed "Argumedo" in cipher. **Handwritten** in ink, 2 ff.; Narváez
    describes it as typed, but the images show a pen hand. Pencil letters above some groups of f. 1 and a pencil
    "C. M. Argumedo" under the signature are in a later hand of unknown date; they are not used.
- Plain Spanish with names and key words in two-digit pairs (25 cipher runs not printed by Narváez, 10 printed).
- Images: the CEHM-Carso public viewer, same path pattern as #941:
  `http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/3/244/1/DCXXI.3.244.1.000{1,2}.jpg` and
  `http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/3/250/2/DCXXI.3.250.2.000{1,2}.jpg`
  (fetched with curl on 25 Nov 2026, no sign-in; .0003 does not exist for either). The CEHM site says "Todos los
  Derechos Reservados" and publishes no terms of use, so **no image is committed here**: the images are linked only.
- AI analysis was not raised with the archive; the project's method was not presented to it at the time.

## System and key

A table of two-digit numbers for the 27-letter Spanish alphabet (A=34, B=35, C=36, D=37, E=01, F=02 ... N=10, Ñ=11,
O=12 ... Z=23), used only for names and key words inside a letter in clear. Codes 24-33 do not occur in these two
letters. `key.tsv` is Narváez's table copied as printed and frozen by SHA-256 before the transcription (the working
file and the hash are kept by the contributor; the SHA is quoted in the header of `key.tsv`). No key was searched for:
the key is Narváez's, and only the reading of the runs he did not print is new.

## Control

The ten runs whose clear Narváez prints (pp. 120-122) are the control (`control_narvaez2015.tsv`, written before the
decoding): the frozen key gives **88 of 89 letters (0.989)**. The one miss is the writer's: PELIGRO is enciphered
13-01-08-05-03-15-10, ending in N; Narváez corrects it silently. No test against null keys was run: the key is a
printed one, applied unchanged, not built from these letters.

## Reading

`scripts/decrypt.py` writes `decryption_DCXXI.3.244.1.txt` and `decryption_DCXXI.3.250.2.txt` (the unedited output of
the key) and prints the control. `reading_<doc>.md` gives the marked runs and each run in its clear Spanish sentence;
`translation_<doc>.md` the English. `scripts/check_marks.py` checks that every departure from the decryption is marked
and counts the words: passes.

New runs (not printed by Narváez): **25 runs, 32 cipher words: 25 read as the key gives them, 7 marked, 0 supplied,
0 unread.** The 7 marked words are one-code slips by the writer or an overstrike: BEN{E/I}TEZ twice and D{E/I}AZ
(01 for 05), {D/A}LFREDO (37 for 34, the same slip as Narváez's "Pdncho", written "Pancho" in clear in the 5 October
letter), FELI{Z/X} (23 for 21, or the writer's spelling), A{?/G}UA PRIETA (an overstrike of 06 and 03; 03 gives
Agua Prieta) and a stray "{H}" (04) before HEREDIA. The new cipher portion is short, about 205 letters.

Per letter, over all its cipher words (control runs included, README rule of 16 Nov 2026):
- DCXXI.3.244.1: 38 cipher words, 31 read, 7 marked: read share 0.816, **read in part**.
- DCXXI.3.250.2: 12 cipher words, 10 read, 2 marked (both in Narváez's control runs: PELIGR{N/O}, P{D/A}NCHO):
  read share 0.833; **read by the short-text floor** (fewer than 40 cipher words, 2 holes).

The one-digit rule of 14 Nov 2026 is not applied: Narváez's table is a reconstruction, not a surviving key of the
period, so the slips are counted as holes.

What the cipher hides. A Michoacán landowner's son, Alfredo Gutiérrez, offers through Argumedo his father's whole
hacienda and a guerrilla of 80 to 100 men his father has armed, and asks for a *nombramiento* to win over the peons of
the district of Panindícuaro. Agents named: Gral. Benítez (probably the Gral. Vicente Benítez of Narváez's control runs),
Heredia, Mata, Montaño, Lic. Mena, Lic. P., "Don Miguel". The 20 October letter closes the loop: the document asked of
Don Miguel "for the person of Panindícuaro" was granted "with the rank of colonel". The 5 October letter also calls
Obregón's government the "reigning horde" and its men the "Agua Prieta mob".

## Prior art

- Narváez, R., "Sobre algunos criptosistemas mexicanos de principios del siglo XX", Documenta & Instrumenta 13 (2015),
  pp. 107-132 (https://revistas.ucm.es/index.php/DOCU/article/view/49742), pp. 117-122: the system, the table and the
  clear of the 10 control runs. The 25 runs read here are not printed there.
- Narváez's book *Criptografía diplomática, política y militar en México (1813-1926)* (Mexico, 2019), cited in #941
  for the Wellington letter, was not consulted for these two letters: it may print more of them.
- This repository (25 Nov 2026): no target, PR or issue on Argumedo; catalogue 1445 cites the two letters as broken by
  Narváez, without a target. Family: duhart1921 (#511) and sanchez1922 (#512), both WAINUT; wellington1922 (#941,
  Andrew Beling, open at the time of writing).

## Transcription doubts

- A04 pair 2 (3.244.1 f. 1, "turba de 34-0?-...") - read: 03, a 0 with 6 and 3 typed over each other; checked: image, decode; 03 gives AGUAPRIETA, 06 (Narváez's figure) gives AJUAPRIETA; kept as "0?" in the transcription, marked in the reading.
- A06 pairs 5 and 11-12 (3.244.1 f. 1) - read: 10, 17, 17 typed "L0", "L7"; checked: image, decode, transcription (Narváez prints "Benit-L7-ez").
- A10 (3.244.1 f. 1, "El Señor 04:04-01-...") - read: 04 then HEREDIA; checked: image, decode; H. may be an initial or a repeated keystroke; marked {H}.
- A15 (3.244.1 f. 1) - read: 10-17 typed "1017"; checked: image, decode (MONTAÑO).
- A26 (3.244.1 f. 2) - read: 10 overstruck; checked: image, decode, transcription (Narváez: Don Mateo).
- B02 last pair (3.250.2 f. 1) - read: 10; checked: image, decode, transcription (Narváez prints the clear "peligro"); a writer's slip.
- B08 pair 1 (3.250.2 f. 2) - read: 36, rewritten over another figure; checked: image, decode (CORONEL).

## Remaining gaps

- The seven marked words of the new runs (AGUA, BENÍTEZ twice, H., ALFREDO, DÍAZ, FÉLIX) - blocker: illegible; the
  writer's signs are wrong by one code or overstruck, so the key does not give them as written; each is read by the
  sense and listed above.

## Limits of the check (not gaps in the reading)

- No person has checked the transcription or the reading against the images; the reading review is the solving model's own.
- Narváez's 2019 book was not consulted: it may print more of these two letters.

## Escalation

- [x] siblings: catalogue 1445 (duhart1921, sanchez1922, wellington1922). Next candidate: Amaya, Havana, DCXXI.3.242.1,
  "two-digit numbers with pencil letters", not tested with this table.
- [x] clear-pages: the clear text around every run agrees with the reading; the second letter answers the first.
- [x] known-keys: Narváez's table applied unchanged.
- [x] print: Narváez 2015 read for these letters (the clear of 10 runs, none of the 25 read here); his 2019 book not consulted (see Limits).
- [x] retry: every marked word looked at again on the image and against the decode; the slips stand as listed.
- [n/a] key-rebuild: the table is complete for these letters.

## Credits

Brice Dudout, with AI agents (transcription, decoding and reading by Claude, claude-opus-5-5; no person has yet checked
the reading). Key, system and the earlier partial reading: Roberto Narváez (2015). Images: CEHM-Carso (Centro de
Estudios de Historia de México, Fundación Carlos Slim). Family and viewer path: #511 and #512 (WAINUT), #941 (Andrew
Beling).
