# Ottobon–Mocenigo, 27 April 1589: substantial decipherment

**Grades** ([CONVENTIONS.md](../CONVENTIONS.md)): of 1,585 group slots, 1,537 H (looked up in Ziffra prima), 48 M (alternative labels, unread signs, or absent from the key excerpt); 54 bracketed supplied readings (I) in the line readings. `python3 decode.py --check` prints the counts and [TRANSCRIPTION.md](TRANSCRIPTION.md) carries them per line.

**The surviving Venetian key “Ziffra prima” (DECODE R1789) reads the seven cipher pages in BNE Mss/994, ff.35r–38r (DECODE R2252).** The covering dispatch is dated 27 April 1589; its enclosed reply to Gerolamo Gondi, ambassador of France, is dated 24 April. Both texts are substantially readable. Some handwriting, binding losses, and apparent encoding errors remain unresolved.

Gondi asks Venice for assistance and a closer alliance, with discussion of recovering Saluzzo. Venice cannot provide the requested immediate aid and promises renewed intercession with the pope. The covering dispatch instructs Mocenigo how to explain that answer and separately reports intercepted correspondence.

**The letter was broken once before.** The volume’s title page, f.34r, in a Spanish archival hand, reads: *Carta en cifra de Venecia. Que dio en Turín la Señora Infanta Doña Catalina por orden del Duque de Saboya a Luis Valle de la Cerda, que declaró; y no tiene contracifra ni declaración por haverse perdido.* The dispatch was intercepted in Savoy, whose duke had just seized Saluzzo, handed by the Infanta Catalina Micaela to Philip II’s cipher secretary Luis Valle de la Cerda (c.1559–1607), and deciphered by him without the key; his working was later lost. The reading here recovers, with the surviving Venetian key, what he recovered without it. See [Navarro Bonilla and Hernández, *Geheime Post* (2015)](https://researchportal.uc3m.es/display/act462541) on Valle de la Cerda.

[Italian text and English translations](READING.md) · [Ciphertext, literal decoding, and line readings](TRANSCRIPTION.md) · [Sources and page locations](SOURCES.md)

## How to verify the key match

The manuscript uses letters with superscript numbers: `d15` means **d¹⁵**, one cipher group. Groups encode letters, syllables, words, titles, numerals, or nulls. Our [key excerpt](key.json) contains the entries used or explicitly considered in the transcription. It is transcribed from the separate archival key, **ASVe B4 Reg.16 f.64, “Ziffra prima,” [DECODE R1789](https://de-crypt.org/decrypt-web/RecordsView/1789)**.

These short passages provide convenient checks against the [public BNE images](https://bnedigital.bne.es/bd/es/viewer?id=91753d62-e2f8-4fcc-8947-9e56a53af1b5&page=30):

| Location | Cipher groups | Literal key values |
|---|---|---|
| f.37r1, opening date | `d43 g57 a92 d41 d53 d50 g61 d53 d14 f64` | `1 5 8 9 a 2 4 a pri l` |
| f.35v9, proposed league | `c56 g7 f66 f19 d2 g99 c74 c29` | `in qualche u ni one di le ga` |
| f.35v13, response transition | `g6 h16 d15 d10 g38 f63 a96 a48 h1 d55 g98 h3 f20` | `qual sua pro po sta i s cu sa n do si no` |

The last passage reads **“[Alla] qual sua proposta, iscusandosi no[i]”**. *Alla* is supplied at the end of preceding line12; the final *i* is supplied at the end of line13. Both places are obscured by the binding. The [comparison sheet](evidence/transition.png) places the visible groups beside other occurrences in the same manuscript; [crop coordinates and image hashes](evidence/transition.json) identify the public source pixels.

Important key readings are **d2=one**, **g7=qualche**, **a47=cusi** (encoder *cosi*), **c89=mente**, **g20=rece**, and **g48=scriue**. Ordinary **d32=present**, **d52=zz**, and **d62=l** retain their separate values. These are readings of the archival tables; no dispatch-specific replacement key is needed.

## Reproduce the literal decoding

Python 3, standard library only. From this folder:

```sh
python3 decode.py --tokens 'c56 g7 f66 f19 d2 g99 c74 c29'
python3 decode.py --folio 35v --line 13
python3 decode.py --check
```

The check verifies all **118 rows** against fixed-key lookup and the committed transcription. It does not verify the handwriting. [transcription.json](transcription.json) keeps each cipher row, its literal output, and the editorial reading separate. `{a84/a94}` means alternative labels; `?` marks unread material, sometimes more than one sign. Square brackets in the reading mark doubt or supplied text. Unmarked labels can still be mistaken. The transcriptions are context-assisted, with repeated-sign comparisons by native Codex agents; this was not a blind validation.

## What remains uncertain

- Short connections and endings on f.35v, including **col[…]** at line 19; several signs disappear under the binding.
- Two blotted groups before **benissimo** on f.36r8, and the ending after **di nostra** on f.36v6.
- Specific label disputes: f.35r3 **a84/a94**, f.35v20 **a92/a94**, and f.38r9 **f63/f67**.
- Literal **recessimo**, **[po]tergo**, **soletione**, **giussima**, and **crirtissimo** require interpretation or repair. The reading edition identifies those repairs explicitly. In particular, *sole[va]tione* supplies an unobserved **va**.

A possible registered copy would be worth checking in **ASVe, Senato, Deliberazioni, Secreti, register 87**, around late April 1589. The precise letter and folio have not been found; the [official catalog entry](https://asve.arianna4.cloud/patrimonio/19dba575-2ea7-495c-83d9-2e09693bfc87) has no attached scans. Romanin, *Storia documentata di Venezia* VI, p.409, summarising the registers, reports Venice's 1589 answer to Henri III in the same terms as the deciphered reply (no aid for now, because of Spanish movements in Italy; good offices with Sixtus V) and cites Secreta, 3 June 1589, which confirms the series. [Source details](SOURCES.md#possible-plaintext-witness).

Prepared 16 September 2026 with native Codex agents; independently reviewed the same day (key spot-checks on the public scans, clear-hand *ult[im]e* for *altre* on f.36r, three bracketed gutter restorations on f.35v, the address offset on f.38r, and the f.34r provenance note). A page-by-page reading with the BNE page images, Italian, and English is in this folder as [reading.pdf](reading.pdf) and [reading.html](reading.html) (images in `pages/`, credit Biblioteca Nacional de España, CC BY 4.0); the same page is online at [aaymeloglu.github.io/unsolved-ciphers](https://aaymeloglu.github.io/unsolved-ciphers/ottobon-reading.html). No publication-priority claim. DECODE sources were accessed with the project's permission; their images are not redistributed. The comparison sheet uses independently acquired public BNE reproductions, credited to the Biblioteca Nacional de España.
