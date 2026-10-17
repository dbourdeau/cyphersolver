# Siena 20 and 23 — DECODE R4808 and R4811

Status: **read in part; key recovered from ciphertext-only**. Contributed by George Lasry. Transcribed with CTTS, then solved by GPT-6 Astra.

## Editions and summary

| Document | Readable Italian | English | Date and proposed correspondents |
|---|---|---|---|
| No. 23 / R4811 / Letter 1 | [Reading](R4811_reading.txt) | [Translation](R4811_translation.txt) | Two royal memoranda, probably Ladislaus’s orders; Iacobo Spinelo and Francisco Gactule named. Before the 4 May deadline; spring 1413 proposed. |
| No. 20 / R4808 / Letter 2 | [Reading](R4808_reading.txt) | [Translation](R4808_translation.txt) | Perugia, 30 March, year absent; Muzio Attendolo Sforza to Ladislaus proposed. |

[Summary and historical background](SUMMARY.html) · [Visual key](visual_key.html) · [Working key](key.txt) · [Five-line mechanical excerpt](excerpt.txt).

The readings follow the current `edited/4808_edits.txt` and `edited/4811_edits.txt`, copied as `R4808_edited_lines.txt` and `R4811_edited_lines.txt`. Only physical line-break hyphens are joined and paragraphs added; all current words, uncertainty brackets and CLEAR1–CLEAR4 passages are retained. These are edited readable texts, not a newly generated complete mechanical decoding. English translations have been revised to follow these readings. Source inputs and publication inputs have SHA-256 manifests. No source-project file was changed in preparing this contribution.

The latest reading has **docento cavali (two hundred horses)**, **Ecclesia**, **però che**, and the unresolved **[Eucebio?]**. `fat = [Paolo Orsini?]` and `o+ = [Sforza?]` remain hypotheses. `e` appears eight times and is retained as `[Name6?]`, a person-reference or possibly pronoun, not silently deleted. `# = [Tartaglia?]` is tentative despite the certain alphabetic heading *ad Tartaliam*. In the English version the unresolved `dessut` clause is explicitly marked; its syntax is not claimed resolved. The phrase *rompere a la scorta* permits more than one interpretation.

## Cryptanalysis

The key was recovered from ciphertext patterns and original cleartext framing; no interlinear/marginal decipherment or matching archive key was used. Later historical sources propose identities and a date; they did not supply the alphabet or a plaintext copy. Original clear-script passages are transcribed as CLEAR1–CLEAR4 and must not be confused with a decipherment of the encrypted lines.

The system is **graphical homophonic substitution with letter groups, one common-word sign, a small nomenclator of names/references, and provisional nulls**. The current transcription has **4,254 ciphertext elements in two documents**: R4808 1,045 in 16 rows, R4811 3,209 in 54 rows. Eleven of 4,265 selections are punctuation or clear-script blocks and are excluded. There are **59 observed classes**: 34 single-letter signs, six multi-letter signs (CI, ET, FF, RE, RR, SS), seven unresolved/proposed name-reference signs, eleven provisional null classes (188 occurrences), and one erased class (two occurrences). An unused `n = ?` mapping is retained in the working key, but not counted as an observed class.

The alphabet has 19 values, with up to four homophones for A/I, three for E/O and U/V, and two for other consonants. The seven reference signs have 41 occurrences: `#` 9, `fat` 8, `o+` 7, `ovo` 7, `Fom` 1, `ta` 1, `e` 8. Three have tentative historical names; four remain placeholders. Thus all seven remain unresolved at the identity level. Assignment coverage excludes hypotheses, erasures and provisional nulls: **4,023 / 4,066 = 98.94%**. This is not a percentage of coherent prose or a claim of full decipherment.

## Mechanical verification — exactly five lines

Only **R4811 CTTS physical lines 6–10** are mechanically decoded. The 322 selected signs produce 328 literal letters after omission of provisional nulls. V represents u/v. There are no letter substitutions, inserted letters, spelling corrections or filled gaps. Physical boundaries split *personalmente* at the start and *Tronto* at the end. The joined output is an exact substring of the normalized current readable edition.

`build.py` regenerates counts, token counting files, the visual key, the five-line excerpt, its token alignment, and the reveal data. `validation.tsv` contains this excerpt only. Any language-model test applies only to these deliberately selected five lines, not both full editions or all key assignments.

## Historical research

<p><strong>Two documents, one cipher; proposed spring 1413 setting.</strong> Siena Concistoro 2308, fasc. 2, no. 20 (DECODE R4808) is a captain’s complaint addressed to a king from Perugia on 30 March, without a written year. No. 23 (R4811) contains two royal memoranda for Iacobo Spinelo and Francisco Gactule. Its 4 May date is an arrival deadline, not an issue date. The best current historical hypothesis is Ladislaus of Naples’s campaign of spring 1413, with the memoranda probably written before 4 May. The year and correspondents remain inferred.</p>
<p><strong>Contents.</strong> The letter’s writer says an enemy has taken fully 200 horses and threatens retaliation despite the risk of royal punishment, while promising not to harm the Church’s lands, people or livestock. The first memorandum coordinates the guarding of passes near Ascoli, the Tronto, Arquata and Montemonaco to contain a hostile captain in the Marche, with intelligence gathering and limited, secret cooperation with the Malatesta. It also orders the recovery of castles using 140 lances. The second arranges a royal muster at “Maccione de le Rose”, a payment of 1,000 ducats, and a promise under seal.</p>
<p><strong>Why 1413.</strong> The Fermo chronicle describes an unusually close parallel in April 1413: forces at Forca di Presta and Sforza’s troops around Caldarola and Sarnano were placed to prevent Paolo Orsini from leaving the Marche at the King of Naples’s request. Orsini’s departure and pursuit are recorded on 10 May. This supports the campaign setting and <code>fat = [Paolo Orsini?]</code>, but supplies no verbatim decipherment. [<a href="https://archive.org/stream/bub_gb_i1rhdgfMJrYC/bub_gb_i1rhdgfMJrYC_djvu.txt">Cronache della città di Fermo, printed pp. 39–40</a>]</p>
<p><strong>Probable participants.</strong> Minuti recounts Sforza’s grievance against Orsini, his service to Ladislaus, and his return to Perugia in February 1413 before pursuing Orsini in the Marche. This makes Muzio Attendolo Sforza a plausible writer of no. 20, although its subscription remains unread. Rodolfo is probably Rodolfo III da Varano; “messer Ludovico” probably Ludovico Migliorati. These contextual proposals do not replace the names actually recovered. [<a href="https://archive.org/stream/MiscellaneaDiStoriaItaliana7/Miscellanea_di_Storia_Italiana_7_djvu.txt">Minuti, Vita di Muzzo Attendolo Sforza, pp. 163–169</a>]</p>
<p><strong>Key comparison and dating safeguard.</strong> Meister’s printed Viviani nomenclator, dated 25 July 1412, has a circle-and-cross Sforza sign comparable to <code>o+</code>. This supports <code>[Sforza?]</code>; the Lucca alphabets differ, so they are not the recovered key. Meister’s 1421 date belongs explicitly to Siena piece no. 1, not nos. 20 or 23. The local “Siena1421” name therefore cannot date this pair. [<a href="https://nbn-resolving.org/urn:nbn:de:hbz:6:1-143638">Meister, Die Anfänge der modernen diplomatischen Geheimschrift (1902), pp. 51, 55–57</a>]</p>
<p><strong>Place and remaining limits.</strong> “Maccione de le Rose” probably denotes the Mazzone delle Rose muster ground. Later royal records independently attest a camp there, including near Ponte Annecchino in 1450; they support the place identification, not the date of these letters. [<a href="https://www.accademiapontaniana.it/wp-content/uploads/2018/03/REGISTRO-9.3.2018.pdf#page=278">I registri privilegiorum di Alfonso il Magnanimo, register 2905, nos. 11–16; register 2914, no. 27</a>]</p>
<p>The supplied research report surveys 44 key records, 43 with images, and reports no matching key; R4783 could not be inspected. It also reports no external copy of these plaintexts. These are bounded search results. The heading certainly names Tartaglia, but <code># = [Tartaglia?]</code> remains tentative: <code>#</code> and the repeated <code>e = [Name6?]</code> may name different people. Name3–Name6, the place [Eucebio?], one difficult clause and the subscription remain unresolved. No priority or “oldest deciphered cipher” claim is made.</p>

## Remaining gaps

- `#`, `fat`, `o+`, `ovo`, `Fom`, `ta`, `e` and historical identities/year — blocker: open-codes. Three name hypotheses remain tentative; Name3–Name6 have no secure identification, and `e` could be a pronoun. The proposed writer and 1413 date are historical inferences.
- Erased selections, `dessut`, `[essereme?]`, `[Eucebio?]`, `[prout?]`, the closing abbreviation and subscription — blocker: illegible. The current readable editions retain unresolved text and editorial restorations; five-line agreement does not settle these passages.
- Nulls, compound segmentation and editorial emendations — blocker: open-codes. Occurrence-level manuscript checks remain necessary; a nearly complete alphabetic assignment is not a completely verified reading.

## Escalation

This publishes the contributor’s current edited result; it does not declare further research exhausted.

- [x] siblings: the supplied report describes review of the 25 photographed fascicle pieces and finds no further document in this cipher. Nos. 6/24 are a different system.
- [x] clear-pages: original clear passages are retained as CLEAR1–CLEAR4. No interlinear or marginal decipherment was used.
- [x] known-keys: the supplied report surveys 44 records, 43 with images; R4783 remains unavailable. No matching key reported. Meister’s Lucca comparison was independently checked here and is a different key.
- [x] print: independently checked the Fermo and Minuti parallels, Meister’s inventory and 1412 nomenclator, and later Mazzone camp attestations. No exact external plaintext established.
- [x] key-rebuild: imported the current reviewed key and edited files; refreshed all glyph samples and counted the new classes. Source mappings were not altered for publication.
- [x] retry: reapplied the current key to exactly five physical lines and verified literal agreement with the current edition. The remaining editorial gaps are disclosed above.

## Sources and credit

George Lasry supplied the images, CTTS material and successive Italian readings, directed the work, and confirms: **transcribed with CTTS, then solved by GPT-6 Astra**. Codex prepared this contribution, revised the English translations to match the latest Italian edition, checked the five-line excerpt and selected historical sources, and regenerated the visual key.

- [DECODE R4808](https://de-crypt.org/decrypt-web/RecordsView/4808) and [R4811](https://de-crypt.org/decrypt-web/RecordsView/4811): Archivio di Stato di Siena, Concistoro 2308 fasc. 2 nos. 20 and 23.
- User-supplied research report: *Siena Concistoro 2308 keys and sources.md*, 17 October 2026 source snapshot. Its broad survey is attributed, not represented as independently repeated in full. Primary sources are linked in the historical section.
- [Earlier collection survey](../siena1421/NOTES.md), for the preceding attempts and other cipher systems.

DECODE updates are queued as **Partially**, not sent. No inferred year or sender is entered as established metadata. No oldest/first decipherment claim is made.
