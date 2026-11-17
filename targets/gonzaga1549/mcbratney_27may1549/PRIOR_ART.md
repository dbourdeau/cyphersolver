# Prior art: Charles V to Ferrante Gonzaga, Brussels, 27 May 1549

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Karl V sfasc. III. Cipher letter cc. 31-36 (Lodovico record
bbdff1f6-f75f-44e1-b9d0-c66a83a9a7a9, 12 canvases); contemporary decipherment cc. 12-15 (record 968f7688-4b71-44f2-9954-737adabf92c3,
8 canvases, text on 12r-14v). Prior art searched before any decode (Track B rule). Searches of 15 Nov 2026 05:05-05:30 UTC are
r2_estense2's (copied here with its sources); the rows marked cv1549 were run by this session, 15 Nov 2026 06:30-06:35 UTC.

## Verdict
**RISK (one open item): Bertomeu Masiá 2009 not checked.** No published reading of this letter was found anywhere searched.
The plaintext itself is not new: the chancery's own decipherment is in the same file (cc. 12-15), so nothing here is a first
break. The open question is only whether a modern edition prints the letter or its decipherment.

## Searched
| Source | Route / query, date | Result |
|---|---|---|
| Cyphersolver upstream main, `targets/gonzaga1549/NOTES.md` (dbourdeau) | raw.githubusercontent.com, cv1549, 15 Nov 2026 | 416 lines (md5 89b9b50df80c1bda6016adb415d40f77, `ref/NOTES.md`). No mention of 27 May 1549, cc. 31-36, cc. 12-15 or either uuid. Worked letters: 13 May, 14 Nov, 20 Nov, 23 Dec, 30 Sep 1549 and Philip's letters. The GitHub API for dbourdeau/cyphersolver was not reachable from this session (403), so the commit id was not recorded [sourced] |
| same, `targets/gonzaga1549/wainut/NOTES_ferrante1549.md` | raw GET, cv1549, 15 Nov 2026 | md5 5c5778c18c78f8361209009df37463a6. WAINUT's twelve transcribed letters list Charles 13 May, 14 Nov, 20 Nov, 30 Sep 1549 and Philip's; "Not started: Charles 15 Jul and 23 Dec 1549, 1 Jul 1552, 11 Aug 1542". 27 May 1549 not mentioned [sourced] |
| Cyphersolver fork main (mmcbratney), same folder | r2_estense2, 15 Nov | NOTES 237 lines; both uuids only in `labels.json` (cc. 31-36 = 12 canvases, cc. 12-15 = 8) [sourced] |
| Cyphersolver `research/leads.json` | grep Gonzaga + 1549 (r2_estense2) | Leads 2158 (Lodron to Gonzaga, Dec 1549) and 2163 (Capilupi 1545); nothing for this letter [sourced] |
| DECODE (de-crypt.org) | live search not reachable by plain GET; harvest snapshot in the clone (batch_1-8, out_1-4, records_current), r2_estense2 | No Estense/Campori record, no Charles V-Gonzaga 1549 record. The harvest covers non- and partly-decrypted records only [measured] |
| Tomokiyo, Cryptiana `code/spanish2.htm` | plain GET, r2_estense2 | Imperial Cipher of 1544-1554: "Bertomeu Masiá (2009) reconstructed a more complete version of this cipher. The cipher was used by Charles V, Prince Philip, ... Ferrante Gonzaga ... around 1547-1550 (p.151) in the context of the issue of Piacenza"; "Ferrante Gonzaga's two letters reproduced in the book use only one [series]". No mention of Modena, Estense, Campori or 27 May 1549 [sourced] |
| Tomokiyo blog (three posts on Granvelle/Renard/Saint-Mauris and vowel-indicator ciphers) | r2_estense2 | None names Gonzaga, Modena or this letter [sourced] |
| Lasry | web search "Lasry Charles V cipher Ferrante Gonzaga 1549" and variants, r2_estense2 | Hits: the 2022 Charles V to Saint-Mauris decipherment and 2023 syllabary work. Nothing on this letter [search titles only] |
| Editions | web search "Carlos V Ferrante Gonzaga 27 de mayo de 1549 Bruselas carta"; "carteggio Ferrante Gonzaga Carlo V 1549 ... Piacenza maggio 1549", r2_estense2 | No edition or calendar entry of this letter in result titles [unverified negative] |

## Not checked (for Malcolm's prior-art sheet: needs a library or a signed-in reader)
1. **María José Bertomeu Masiá, *La guerra secreta de Carlos V contra el Papa. La cuestión de Parma y Piacenza en la correspondencia del cardenal Granvela*, Valencia 2009, ISBN 978-84-370-7398-9, esp. p. 151 and the two Gonzaga letters it reproduces.** Whether one of them is this letter, or whether it prints the decipherment: NOT CHECKED. **RISK.**
2. *Corpus documental de Carlos V*, vol. III (1548-1554): whether it prints this letter or its Simancas minute.
3. HathiTrust / Google Books full text: "xxvij de Mayo" 1549 Gonzaga; "bullicios y aparejos que franceses hazen"; "insolencias que todavia continuan con nuestros vassallos".
4. Simancas, Estado (the minute of this letter; the clear opening suggests a register copy may exist).
