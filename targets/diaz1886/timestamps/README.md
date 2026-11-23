# Timestamps

Six sets of stamps, all RFC 3161, from public time-stamping authorities (FreeTSA, DigiCert, Sectigo).

| subfolder | what is stamped | SHA-256 | times (GMT) |
|---|---|---|---|
| `numerals_v4/` | `numerals_v4.tsv`, the copy | `4f58bc562cdf30c36ca98f3ee865e9fcd7b9e2a2b1d614c8d27661c1e3728ae5` | freetsa.org Nov 20 05:54:46 2026 GMT; digicert Nov 20 05:54:47 2026 GMT; sectigo Nov 20 05:54:47 2026 GMT |
| `plan/` | the plan of the test of `NOTES.md`, section 7, as sealed | `2e84dbbd3a74f764e58d79be2a717503c15d4201c38aa0acd7c81c67395ae89a` | freetsa.org Nov 20 21:19:40 2026 GMT; digicert Nov 20 21:19:40 2026 GMT; sectigo Nov 20 21:19:40 2026 GMT |
| `results/` | the results note of the test of `NOTES.md`, section 7 | `68c3f4ec92f4b4c53e0031edd02dd8b01bbae700e4a068702556959d2c94357e` | freetsa.org Nov 22 17:56:34 2026 GMT; digicert Nov 22 17:56:34 2026 GMT; sectigo Nov 22 17:56:34 2026 GMT |
| `first_reading/` | the first reading's note of 19 Nov 2026, `NOTES.md`, section 3 | `5189f57c202aa7edae0ec9c967934e6a0ca7d872b63b662d34e0f0727904410d` | freetsa.org Nov 19 02:01:50 2026 GMT; digicert Nov 19 02:01:50 2026 GMT; sectigo Nov 19 02:01:50 2026 GMT |
| `blind_readings/` | the two blind readers' answers, as received | in its `README.md` | in its `README.md` |
| `pr_folder/` | `MANIFEST.sha256`: the SHA-256 and path of every file of this folder outside `timestamps/pr_folder/` | in its `STAMP.txt` | in its `STAMP.txt` |

**What they show.** That the copy existed in this form when the first stamp was made; that the plan existed as it stands here when it was stamped; that the results note and the first reading's note existed as they stand here when each was stamped; that each blind reader's answer existed as it stands here when it came; and that the whole folder existed when the last was made.

**What they do not show.** That the blind readers were blind: their task sheets are in `blind_readings/`, the images they were given are not. Nor who read which group, nor that no decode came before the copy or before the plan, nor that the results note's figures are right. Those rest on the contributor's session logs and on his record chain, a hash-linked list of every reading, plan, run and ruling of this work; the pull request that brought this folder gives the chain's head.

The first reading of 19 Nov 2026 was time-stamped when it was made. Its note and receipts are in `first_reading/`, and the note's SHA-256 is also in `NOTES.md`, section 3.
