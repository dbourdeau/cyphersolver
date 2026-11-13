# dallas1911: F. González Garza ("Olliphant") to F. I. Madero, 17 March 1911, in the "clave de Dallas"

Contributed by SeldomPhooey (issue #520, 13 Nov 2026; transcription, key rebuild, decoding, reading, translation and a
blind second reading by AI agents). Integrated 13 Nov 2026.

Status: in progress. Not written up: by the README read bar 67 of the 114 cipher words read as typed (58.8%); the
other 47 rest on values outside the period table, on emendations or on context alone, and they can still be tested
against other letters in the same key (see Remaining gaps), so the gaps are workable.

## Documents

- **Top copy:** Biblioteca Nacional de México (IIB-UNAM), Archivo Francisco I. Madero, **Ms.M/40**, 3 pp. typed;
  UNAM digital repository record 700 (images `https://repositorio.unam.mx/covers/700/<0|1|2>/500.png`, 500 px wide).
  The shelfmark comes from the BNM catalogue summary as reported by the contributor; the repository record carries
  none (not checked here).
- **Carbons:** CEHM-Carso, Fondo CMXV (Archivo Federico González Garza), **CMXV.14.1370.1**, 7 pp. (CEHM record
  8,907, "EL TEXTO INCLUYE PALABRAS EN CLAVE", no decipherment). Pp. 1-4 a later clean retyping headed "(COPIA)"
  (typing A); pp. 5-7 a carbon of an earlier typing with struck-out and retyped blocks (typing B). Images:
  `http://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/14/1370/1/CMXV.14.1370.1.000<1-7>.jpg` (plain http
  answers; the https host fails TLS verification, as in targets/duron1911).
- Heading (typing B, p. 5): "17 de Marzo 911 - Correo: Escudero. Clave: la de Dallas." Signed "Olliphant." The alias
  W. Olliphant = Federico González Garza is glossed in CMXV.18.1795.1 (per the contributor) and on CMXV.18.1770.2-4
  (targets/mexico1911). Addressed "Señor Presidente" (Madero, in Chihuahua after Casas Grandes, 6 March 1911).
- Spanish, 1,785 words in the reading (counted here from reading.md); 69 cipher runs, 114 cipher words, 681 bigrams
  (1,362 letters, `_check_profile.py --measure transcription.txt --letters`).

Not in the catalogue or leads: catalogue 1462 (the El Paso junta) lists CMXV.14.1354.1 and other telegrams, not
1370.1; `research/latam_mexico/cehm_hits.json` has the CEHM record of 1370.1 (8,907) and of 1395.1 (8,932) from the
Oct 2026 sweep, but neither went into candidates. So this enters as a new target folder.

## System and key

Each plain letter is two cipher letters. Three rows of first letters (h/y/ñ, j/p/v, l/q/t) share second-letter columns
(x u w i z k a e o), so the homophones of a letter differ in the first letter only. Accents are not written; ll is one
sign (yw). The key is the period "clave de Dallas", named on the letter itself. It was rebuilt by the contributor from
CEHM **CMXV.14.1395.1** (González Garza to Madero, El Paso, 21 March 1911, "Correo: Hon. Mason. Clave: la de Dallas",
record 8,932), whose period typed transcription (pp. 5-6) gives the plaintext of its cipher runs: 54 bigrams for 21
plain letters (key.tsv, source `table`). Values added for this letter (key.tsv): row structure je=l, tx=g, hk=h,
vz=j; consistent in context jw=b, ho/yo/ño=z, yu/ñu=x; single context values lz=k, jx=f, ti=y, bk=p; typed errors
hb, uo, js read u, n, s.

Not a duplicate key: the other Maderista keys in this repository are the Clave G.A. card (targets/mccarty1911, row
letters WZCTG/MVPKI), a turning grille (targets/nuevaclave1911), simple substitutions or swaps (mexico1911,
hernandez1911, duron1911) and, later, Clave Extra 3 (carranza1914 and siblings). One key, one entry: 1395.1 belongs
here as the key source; it was deciphered at the time.

## Prior art

The contributor searched this repository, Narváez 2011 (Documenta & Instrumenta 9), the CEHM and BNM catalogues and
HathiTrust full text of Fabela, *Documentos históricos* vols. 5-9 (no hit for Caracristi or Olliphant), and found no
print or decode of this letter. Not read: Narváez 2019 (*Criptografía diplomática, política y militar en México*) and
González Garza 1936 (*La Revolución Mexicana: mi contribución político-literaria*). Parallels in clear: CEHM
CMXV.14.1351.1 (González Garza to F. Vázquez Gómez, 12 March 1911: the Caracristi-Knox "15,000 Japanese" story) and
CMXV.14.1383.1-2 (19 March 1911, Escudero with about fifty men; checked here on the image: a telegram to "John
McCarty" with a pencil decode "cincuenta hombres", in a different key). Repository check here (13 Nov 2026): no target,
catalogue entry or lead names 1370.1, 1395.1, Caracristi or the clave de Dallas.

## Integration check (13 Nov 2026)

Issue #520 only; the two attachments (transcription.txt, decryption.txt) answer 403 to this sandbox, so the contributor's
clear-text transcription as typed and the per-run reasons for each emendation were not read. The issue body carries
the 54-bigram table, every cipher run as typed, the raw decode, the reading, the full Spanish and English texts and the
counts, which is enough to reproduce.

1. **Own decoder** (scripts/decode.py over key.tsv, written from the issue's table): all 69 raw decodes identical to
   the issue's column, 681 bigrams, 0 differences.
2. **Images.** CEHM 1370.1 pp. 2, 5 and 6 fetched (plain http) and compared run by run: runs 1-26 on typing B p. 5
   (about 220 bigrams) and runs 39-51 on typing B p. 6 and typing A p. 2 agree with the issue's cipher. One variant:
   run 43 word 2 ends -lk (r) in typing A and -lw (e) in typing B; the issue follows typing A (MILITAR), which reads.
   BNM 500 px images fetched; too small to read the cipher letter by letter, not compared.
3. **Key source.** CEHM 1395.1 pp. 1 and 5 fetched: p. 5 is the typed transcription ("Correo: Hon. Mason. Clave: la de
   Dallas"; "Tengo vehementes sospechas que este correo enseña a Caracristi ..."); spot-check of the first cipher line
   of p. 1 against it: lwjoyztw = este, tuhaqktklwña = correo, twlo = en, volwjiyx = seña, ...qulkyivohzyi = caracristi
   (its first bigram tw for tu, the same u/w slip as in 1370.1). The table is consistent where checked; the full
   1395.1 alignment was not redone here.
4. **Count (README read bar, cipher words).** Own count from the issue's reading: 114 cipher words, 67 sure (every
   bigram in the 1395.1 table, no emendation, no mark) = **58.8%**, the contributor's own cipher-word figure. The
   contributor's headline, 97.4% (1,738 of 1,785 words of the whole letter, clear text counted as read; 99.9% with
   the probable words), is theirs and counts the clear text; the bar counts cipher tokens. Class: read in part.
5. **The reading reads.** The Spanish reads as continuous sentences and matches the English; the context values
   (BATALLA, SUBALTERNOS, BENEVOLENCIA, FUERZAS, EXPEDICIÓN) make sense at every occurrence, and the parallels in
   1351.1 and 1383.1-2 support KNOX, NIPONES and CINCUENTA. That is support, not proof: 17 words stay `[?...]`.
6. **Sibling search, started here.** CMXV.14.1352.1 (Douglas, 13 March 1911, to Olliphant, "palabras en clave y
   descifradas") and 1383.1-2 were opened: both use other systems, not the clave de Dallas.
7. Blind second reading: by the contributor's record, a second AI agent of the same family, without the first reading,
   agreed on 99.5% of cipher letters (1,355 of about 1,360). Not model-independent; not re-run here.

## Remaining gaps

One line per open piece, with its blocker type.

- 46 cipher words resting on values outside the 1395.1 table, on emendations or on context - blocker: not-attempted; 17
  marked `[?...]` (DECLARACIÓN, PELIGROSA, HIZO, COLONOS, MÉXICO, ATACAR, AMERICANOS, NUESTROS, DISCIPLINA, EXIGE,
  RIGUROSO, MAYOR, PELIGRO, MÁS, OPERACIONES, OBEDIENCIA, JUNTARA), 8 other emended words (CARTA, CRISTI twice, NIPONES
  twice, COMPLACENCIAS, CAMPO, CINCUENTA) and 21 unmarked words that need a value outside the table (je, tx, jw,
  ho/yo/ño, yu/ñu, lz, jx: e.g. MIL, LE, AL, ORIGINAL, BATALLA, FUERZAS, KNOX). Workable: further "clave de Dallas"
  letters with period decodes (CEHM CMXV catalogue, the 1795.1 list of decipherments) would test these values.
- REMESA MAU[...] - blocker: illegible; the run ends after three letters (leyxhe = m a u), with nothing further on either
  typing, per the contributor.
- The contributor's attachments (clear text as typed, reasons for each emendation) - blocker: no-key-material; the
  GitHub attachments are refused to this sandbox (403); to be added to the folder.
- Narváez 2019 and González Garza 1936, not read for a prior decode - blocker: needs-physical-access.

## Escalation

- [x] siblings: CMXV.14.1395.1 (same key, the key source) opened; 1352.1 and 1383.1-2 opened, both in other systems; a
  catalogue-wide search for "Clave: la de Dallas" not yet done
- [x] clear-pages: the letter's clear text and the clear parallels 1351.1 and 1383.1-2 (pencil decode) checked; none is
  a decipherment of these runs
- [ ] known-keys: the other Maderista keys of this repository (Clave G.A., grille, swaps, shifts) differ in form; the
  21 keys of CMXV.16.1557.1 not compared with the Dallas table
- [ ] print: Fabela vols. 5-9 searched by the contributor (HathiTrust full text); Narváez 2019 and González Garza 1936 not seen
- [ ] key-rebuild: 17 values added from row structure and context; not tested on further text in the key
- [ ] retry: the 46 words not retried, waiting on further period pairs
