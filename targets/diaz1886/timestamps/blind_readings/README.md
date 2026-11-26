# The blind readings, as received

The two second readings of the numerals, each made by an AI model in a chat of its own from cut images and a task sheet, as the answers came back. Nothing in them was changed. The task sheets are here too; the cut images are not, because no image of the archive is committed.

| file | what | SHA-256 | stamped (GMT) |
|---|---|---|---|
| `BLINDREAD_numerals_1460_table_as_received_2026-11-19_1822Z.txt` | the first blind reading, 19 Nov 2026 | `a5c25c1eff3a8194761d5960236c615db830b18ed3fd97479e644d71aaa9b2bb` | digicert Nov 19 18:22:07 2026 GMT; sectigo Nov 19 18:22:10 2026 GMT |
| `TASK_blind_second_reading_numerals_v1_2026-11-19_0207Z.md` | the task sheet its reader was given | `030218d2d1ca21b68da8195b9fbdfc4a89672b4a091dc0d60044d8cc0cdc0eaf` | |
| `BLINDREAD2_numerals_1460_M1M2_table_as_received_2026-11-20_0228Z.txt` | the second blind reading, 20 Nov 2026 | `372136048bca365fcae20779425c3890929de0de664d4b2bb699034b360135ff` | digicert Nov 20 02:29:33 2026 GMT; sectigo Nov 20 02:29:33 2026 GMT |
| `TASK_blind_second_reading_numerals_v2_2026-11-19_2319Z.md` | the task sheet its reader was given | `4c17b803de87f6f0844f5916c770914cd783f4f79fd518344d466a1687330120` | |

**Which label is which telegram** (from `numerals_v4.tsv`, columns `sample` and `sample2`):

| label | telegram |
|---|---|
| S1 | DLI.2.397.1 |
| S2 | DLI.5.920.1 |
| S3 | DLI.5.933.1 |
| S4 | DLI.5.950.1 |
| M1 | DLI.5.924.1 |
| M2 | DLI.5.910.1 |

The stamps on the two answers are the auditing session's, from two authorities (DigiCert, Sectigo), made when each answer came. Verify one with: `openssl ts -verify -data <file> -in <file>.timestamp.<authority>.com.tsr -CAfile <a bundle of public root certificates>`.

**To count the agreement yourself:** `numerals_v4.tsv` sets each group of the first reading beside the blind reader's token for it; the tokens are the ones in these files, line by line.
