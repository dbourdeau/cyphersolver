# AGAD 131: a letter from Wilno, 11 July 1757, on subsidies and the Strutyński affair

A letter in clear Polish and French cipher, to a patron in the Branicki circle. It asks for protection and subsidies for the Lithuanian Tribunal. It also reports the killing of a Ciechanowiecki at the Brasław dietine, and how Count Apraksin shields the killer.

- **Where:** AGAD Warsaw, fonds 338, reference code 1/338/0/1/131.
- **Scans:** https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/28223838
- **Ledger:** catalogue 1580 at https://github.com/dbourdeau/cyphersolver lists this letter among letters partly in cipher. It gives no reading of it.

## What it says

- The Castellan of Brest [?Abramowicz] and Count Pociej, Strażnik of Lithuania, ask His Excellency [?Branicki], Grand General of the Crown, for protection and a subsidy for the coming Tribunal.
- Beyond the French subsidy, the Prince Grand General of Lithuania gave a thousand ducats. Their borrowing reached two hundred thousand francs.
- The Castellan asks support for a memorial of the Castellan's nephew Ciechanowiecki, Starost of Opsa. It is to go to the French ambassador, the Count de L'Hôpital.
- Strutyński, Starost of Szakinów, had a Ciechanowiecki killed at the Brasław dietine. Strutyński then fled. The text seems to say that he went to the Russian army, but that part is still doubtful. Field Marshal Apraksin stopped the Tribunal's case.
- Rumours follow: a crime at [?St Petersburg] about 1730, and a betrayal of King Stanisław at [?Danzig].
- In clear Polish: a secretary, perhaps Bouwen, did not write by this post. His name and title are still doubtful.

Read it: [Polish and French](reading.md), [English](translation.md).

## The cipher

The key of letter 446, with no change: a reciprocal alphabet of 12 pairs, plus a number code. Bespoke count matching based on French next-letter counts, run on this letter alone, gives the same key for 97.7% of letter tokens.

The numbers agree with the published table of the 446 key. The value 580 is Pétersbourg. The proposed values 185=Branicki and 275=Dantzig remain conjectures. The group 190 stays open.

## Checks

- **Score:** the key scores -2.74 nats per letter under a French model. Three shuffled controls score -3.42 to -3.50.
- **Blind read:** a reader with no context named the cipher text French and three controls noise. It translated about 75% of the clauses.
- **Print:** Konopczyński (1909, p. 216) and Matuszewicz's memoirs (vol. II, p. 237; vol. III, pp. 84 and 136) tell the Strutyński affair: the killing at the Brasław dietine, Apraksin's protection and the later suit.
- **The writer:** letter 1398, also of summer 1757, ends with the same memorial, the Castellan of Brest and the Count de L'Hôpital. Its writer signs "Matusewic", and the memoirs put Matuszewicz in Wilno in early July 1757. So I infer the same writer here. This letter ends "manu notus" and gives no name.

## Status: read in part

The reading remains partial. Ordinary wording and syntax still have gaps.

The memorial now reads “est tenoris sequentis”. Strutyński came armed to Brasław with the intent to kill. He fled because he did not trust the courts. The decrees concern his disorders. The final passage asks for the tables to be kept and refers to the council of war. The clear closing reads “obligowany sługa”.

Open items:

- 190 stays unread. 185=Branicki and 275=Dantzig remain conjectures.
- Pińsk, Szkultyn, Königsberg and Bruwen/Bouwen need confirmation. Abramowicz and Matuszewicz remain inferred identities.
- “Autres”, “Ce pourquoi”, “par de”, “massacre”, “cris/crimes”, “d'être entré”, “tous” and “marque” stay doubtful.
- Three cipher signs remain unread. One precedes “de Russie”. Two occur in the proposed “réponse”.
- The secretary's title, the closing extra M, “sous/soûl” and the final paragraph's subject stay open. The clear Polish remains a working reading.

The reading is with the cipher ledger as issue #331, as a partial solution: https://github.com/dbourdeau/cyphersolver/issues/331

## Earlier work

As far as I checked, nobody has read this letter. That is not proof that nobody has.

**Checked:**

- the ledger, live on 7 November 2026;
- the card and the five scans of the unit;
- a text comparison with letters 446, 1398, 1399 and 1400, which share titles but no passage.

**Not checked:**

- unit 83 (Beck, 1757) and the rest of the fonds, unit by unit;
- key sheet 1196;
- the Radziwiłł and Branicki papers in other archives.

Matuszewicz's memoirs tell the same events, but they do not give this letter on the cited pages.

## Files

- `reading.md`: the letter in Polish and French
- `translation.md`: the letter in English
- `transcription.txt`: the signs and the clear parts, line by line
- `decryption.txt`: the decryption, line by line
- `key.tsv`: the key

© 2026 Prabal Gupta. First published here, 7 November 2026. Released under CC BY 4.0: reuse it, and credit me.
