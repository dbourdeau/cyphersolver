# Juan de Eraso to Philip IV, Genoa, 18 January 1643 (catalogue 755, item EST,LEG,3598,44)

Status: read (Brice Dudout, 28 Oct 2026; 135 of 137 words read in their sense, 115 certain, 4 probable, 16 restored, 2 unresolved; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Write-up prepared for:
https://bdudout.github.io/europe-chiffree/en/documents.html#genes-1643

## Document

Archivo General de Simancas, Estado, legajo 3598, no. 44 (EST,LEG,3598,44; PARES 3555178), image 1. The plain-text original (no. 42, ff. 151–152) is not online: the PARES record for no. 42 shows the images of no. 41 by mistake.
18 January 1643; signed duplicate (“Dupp.do”). Genoa → Madrid.
Sender: Juan de Eraso, Spanish ambassador at Genoa. Recipient: Philip IV.
PARES record and images: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3555178. Images are not reproduced here.

January 1643: Tortona has just been retaken, the war with France weighs on the Milanese, and Madrid is pressing the Italian princes bound to Spain to send troops. The ambassador at Genoa, Juan de Eraso, has forwarded the King’s letter to Grand Duke Ferdinand II de’ Medici. The answer comes back: the Grand Duke refers the matter to his resident in Madrid. Eraso tells the King, in cipher, that this is a way of playing for time.

## Scope within entry 755

The 1638 letters are in targets/genes1638. Of the ten cipher items of 1643-1651, nine have their contemporary plain text
in the same bundle (3598,15/14 and 41/40; 3600,43/45, 166/165, 182/181, 199/200 (word-by-word descifrado); 3602,56/55;
3637,33/12 and 39/14): existing decipherments. **3598,44 is the only one whose plain text is not online**: its original
(3598,42, ff. 151-152) exists, but the PARES record for no. 42 carries the images of no. 41. That is the reading contributed here.
The 1645 letters use the Rome 1644-45 family of keys; 1647 and 1650-51 are other systems.

## System

the 1643 cipher of the Genoa embassy (a different table from that of 1638): syllabic series of five numbers (27 fa, 32 ta, 37 as, 42 na, 47 ja, 52 al, 57 da, 62 an), disguised bigrams (ax = la, at = sa, ha = ma, am = ya), trigrams (sal = ra, gan = ca, tes = ve, las = tra), single letters (ℓ = a, c = n, v = e) and code (270 = Vuestra Majestad, 223 = república, 180 = Francia).

## Key and validation

`key_K4b.tsv`. Learned on the pairs 3598,38/37 and 41/40 (cipher / plain original) by an EM alignment seeded with a partial
key, frozen (SHA-256) before each test. First held-out test 3598,15 vs 14: 0.816 of characters / 0.750 of words, below the
criterion fixed in advance (>= 0.85 / >= 0.75); reported. Main test, designated before either piece was seen:
3598,291 p. 1 (`validation/291_cipher.txt`, 22 lines, frozen before the plain original was opened) against 3598,290
(`validation/290_plain.txt`): **0.881 of characters, 0.834 of words**; 200 permuted-value control keys: 99th percentile
0.298 / 0.121. Criterion met.

## Reading

First published decipherment, to our knowledge (the contemporary plain text is not digitised; no edition found). Rule applied: Daniel Bourdeau’s, 95% of the words read from the sense. Cipher part: 137 words; certain 115 (83.9%), probable {x} 4 (2.9%), restored from the sense [x] 16 (11.7%), unresolved ‹…› 2 (1.5%); read from the sense: 135/137 = 98.5%.

Files: `transcription.txt`, `decryption.txt` (each line and its token values), `reading.md` (Spanish), `translation.md` (English).

## Notes

- The Grand Duke’s letter. The next item in the bundle (3598,43, PARES 3555166) is the “copy” announced here: Ferdinand II’s letter to Eraso in Italian, Florence, 1 January 1643. He refers to the good offices of his ambassador and recalls that he must provide for “la conservatione de’ miei stati”.
- [carta] (pis) and [Milán] (ble). These two groups were missing from the training key. They occur in the validation letter 3598,291, whose plain copy 3598,290 reads “por cartas del marqués de Velada” and “en el Estado de Milán”.
- {Duque} (130). “Gran” is spelled out (1 salc = g-ran); code 130 follows it and precedes “de Toscana” three times. The title imposes “Duque”, but the code is attested nowhere else, so we mark it as probable.
- [para que] (hec, three times). This code group introduces three subjunctive clauses: “… acudiese”, “… trate de esta materia”, “… llegue”. Only “para que” fits all three.
- [con que] (213), [órdenes] (tun), [España] (166), [respuesta] (224), [cuenta] (214). These are word codes with no other attestation, restored from the syntax and from the formulas of the correspondence: “dar cuenta a V. M.”, “aguardar respuesta”, “remitir el negocio a España”. For 166, “Madrid” or “la corte” would give the same sense.
- [gozará]. The key gives g-u-o-ca-ra letter by letter; this is the verb that “del beneficio del tiempo” calls for.
- ‹149› and ‹210›. Codes not attested elsewhere. 149 comes before “residente” (a title or rank of the resident). 210 stands between “llegue” and “antes este aviso” (perhaps “a manos de V. M.”). We leave them unresolved.

## Remaining gaps

- Codes 149 (before "residente") and 210 (between "llegue" and "antes este aviso") occur only here.
- A reproduction of the plain original 3598,42 (not online) would check the restored code words.
