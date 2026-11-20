# Checks

Credit: DECODE, the database of historical ciphers of the DECRYPT project, records R4033 to R4054. Florence, Archivio Niccolini di Camugliano, Fondo antico 214, inserto 1. No DECODE image is published.

Labels: "planted" is a number from a practice text with a key that I planted and hid from the solver. "Real" is a number from the real letters.

## 1. The main system: checks with no key

The main system is not checked against a key. The archive's key table serves the earlier system only: its alphabet holds 4% of the main system's tokens.

**The practice control (planted).** A practice text in the exact layout of the 13 letters of the read (8,590 digits), Italian letters of about 1600 under a planted key:

| Measure (planted) | Value | Bar set before the run |
| --- | ---: | ---: |
| Clean letter codes read right (hidden counts as not right) | .907 | .80 |
| Shown codes that are right | 1.000 | .90 |
| Starts on the best hill, of 100 | 36 | 3 |

**The language checks (real).** On the 13 letters, the Italian model scores the read above a shuffled text by .617 nats a digit, above Spanish by .554 and above Latin by .293.

**The two halves (real).** The letters of 1538 and of 1539 were each read alone, with 30 starts:

- 1538 (4,768 digits): 17 shown codes, all equal to the main key (2,356 of 2,356 tokens).
- 1539 (3,822 digits): 14 shown codes, all equal to the main key (1,634 of 1,634 tokens).

**R4049, held out (real).** Decoded with the frozen key and no further fit: .748 of its 321 codes show a letter in the frozen read. The decode gives .754: it also shows 2 codes that hold a doubtful digit. No language check ran on it.

**Names that fit outside sources.** The decode names people of these years: Bartolomeo Valori and his sons, Francesco Valori, Giulio the natural son of Duke Alessandro, Gian Francesco da Mantova, Stefano da P[al]estrina. The names come out of the decode of a key found from the cipher text alone. Some of them hold supplied letters, for example "[V]alori" in R4048.

**The printed affair.** The passage of R4054 fits the affair of Biagio della Campana, which L. A. Ferrai printed in 1882 (*Cosimo de' Medici duca di Firenze*, pp. 126 to 135 and the documents on pp. 276 to 285). The affair names Biagio Pesci, "speziale alla Campana", the sons of Baccio Valori, the fortress of Pisa, "la signora Maria" (Cosimo's mother), Giovan Francesco da Mantova and "il vescovo di Marzi". I looked up the affair after my page was public.

**Marks above the rows.** A rule fixed before any clear line was opened named four marks above cipher rows of R4039 and R4042. All four are pen strokes with no letters, so they cannot test the read.

## 2. R4054 against a printed sister letter

**What was compared.** Ferrai prints, in a footnote, the wording of a letter of Cosimo to Pirro Musefilo of 8 August 1539: *Cosimo de' Medici duca di Firenze* (1882), p. 136, note 1, to p. 137 (archive.org item `cosimodemedicid00ferrgoog`). It is a sister letter, not this letter. My R4054 is dated three days later. I compared the print with the section "The rows as read" of my public page of R4054, as it stood at 09:05 (UTC−5) on 19 November 2026.

**The order of events.**

1. 16 November 2026, 16:15 (UTC−5): the read of the main system fixed.
2. 19 November 2026, 09:05: the read public on my repository.
3. 19 November 2026, 15:31: the ledger's maintainer named Ferrai's footnote, on issue 802.
4. 19 November 2026, 15:53 and 15:56: the text of the print fixed from two readings of the page images, then the rule declared; the comparison ran once at 15:56.

So the check came after the read. The rule and the text of the print were fixed before the comparison opened my read. I changed no key, no row and no reading after it.

**The rule.** The print's letters and my read's letters are aligned as two letter streams, after fixed spelling rules (u = v; i = j = y; h does not count; doubled letters count once; "et" = "e"; Latin x = s, ct = tt, ti = zi before a vowel; m = n before p and b). A place that my read does not show counts as one letter that does not agree. The floor is the highest agreement of two texts that should not match: my read reversed, and a passage of my read outside the matched region of the same length.

**The verdict word, set before the run.** "supports" asks for coverage of at least .50, agreement of at least .60 and agreement at least .20 above the floor. "does not support" is agreement less than .10 above the floor. Every other case is "cannot tell".

| Measure | My read | Floor: my read reversed | Floor: a passage that does not match |
| --- | ---: | ---: | ---: |
| Print letters counted | 666 | 666 | 666 |
| Letters shown | 417 | 425 | 370 |
| Letters that agree | 279 | 182 | 191 |
| Letter agreement | **.669** | .428 | **.516** |
| Letter coverage | .626 | .638 | .556 |
| Print words counted | 150 | 150 | 150 |
| Words shown | 127 | 131 | 129 |
| Words that agree | 19 | 2 | 4 |

**The verdict: cannot tell.** The agreement is .669 against a floor of .516: a margin of .153, under the .20 that "supports" asks.

- This is not a key accuracy. It is the share of aligned letters that agree with a printed sister letter.
- The print span matched the opening 42% of my read of R4054.
- Where the print has "per li otto di balia era stato", my rows read `persiot·odibaliaerastato`: "per si ot·o di balia era stato". The print's letter before "otto" is doubtful (l or i) and stays out of the counts. One code of "otto" is hidden in my read. My reading on the record page gives "per sent[enza] di Balia" at that place. I changed neither.
- The rows also read `dibartolomeoualori`, where the print has "di Bartolomeo Valori".

**What this check does not show.**

- The print is a letter to another man, so some differences are real differences of wording. The check cannot tell them from misread letters.
- The print is Ferrai's transcription of 1882. Nobody here checked it against the archive.
- Two readings of the print agree except at one letter, which stays out of every count. A misreading that both share is possible.
- The check does not test my transcription of the cipher rows.

## 3. The earlier system: my blind read against the archive's key table

Before I used the table, I read the five letters of the earlier system from the cipher text alone. That read was fixed on 16 November 2026 at 22:09 (UTC−5). On 17 November at 19:33 I compared it with my reading of the archive's table (DECODE record R4033). The comparison ran once, by a rule fixed before it.

| Measure (real) | Value |
| --- | ---: |
| Shown codes of the blind read: types; tokens | 17; 1,558 |
| Agree with the table: types; tokens | 16; 1,488 |
| Disagree with the table | 0 |
| Not in the table: types; tokens | 1; 70 |
| Precision of record, tokens (a code not in the table counts as wrong) | .955 |
| Floor: mean; 95th percentile | .071; .217 |
| The word | supports |

- The practice controls of the earlier system missed their bar: .725 and .768 of the clean letter codes against .80, with every shown code right. So this blind read is a partial read.
- An earlier, smaller check against two clear lines above rows of R4034 gave "does not support" (10 of 32 letters against a floor of 15). One of the two lines turned out to be a described pen stroke, not writing. The other line alone is too short for a result.
- The table is my reading of the table's images, read twice. An error that both readings share stays in it.

## 4. The decode and the frozen read

The decode on each record page is the key applied to the codes of the cut. The frozen read (`key/frozen-read.md`) is the read as it stands on my public pages. They differ in two ways:

- **Doubtful digits.** The frozen read hides each code that holds a doubtful digit (114 code tokens in the 14 letters). The decode shows the key's value for these codes in `⟨ ⟩`.
- **Seven places.** At 7 places the frozen read shows the value of a two-digit code (26 = i; once 25 = a) on both codes of its cut, code 2 and code 6 (once code 5). The key gives "o" and a hidden code. The places: R4042 image 2, C01; R4044 image 1, C01; R4045 image 1, C03; R4048 image 3, C01 and C02 (2 places); R4052 image 3, C04. I left the frozen read as it is.
- **Token counts.** The cut of the 13 letters of the read has 4,730 code tokens. My public page gives 4,726, and the count column of `key/key-main.tsv` sums to 4,719. I did not find the cause of these differences.
- **The earlier decode.** The decode of the five earlier letters is the table applied to the codes of the cut. An older decode of them, on my public pages, leaves out the table's sign & at 21 places. The decode here gives it.
- **Bars.** My rows of R4034 mark 12 digits under a bar. The grade of the earlier blind read speaks of 14 barred code tokens (16 digits) in R4034. I did not settle this difference.

## 5. What is not checked

- No key checks the main system.
- The readings supply letters and words. They mark most supplied letters with brackets, but not all of them. The decode is the reference.
