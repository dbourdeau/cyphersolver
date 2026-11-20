# Timestamps

Three sets of stamps, all RFC 3161, from public time-stamping authorities (FreeTSA, DigiCert, Sectigo).

| subfolder | what is stamped | SHA-256 | times (GMT) |
|---|---|---|---|
| `numerals_v4/` | `numerals_v4.tsv`, the copy | `4f58bc562cdf30c36ca98f3ee865e9fcd7b9e2a2b1d614c8d27661c1e3728ae5` | freetsa.org Nov 20 05:54:46 2026 GMT; digicert Nov 20 05:54:47 2026 GMT; sectigo Nov 20 05:54:47 2026 GMT |
| `blind_readings/` | the two blind readers' answers, as received | in its `README.md` | in its `README.md` |
| `pr_folder/` | `MANIFEST.sha256`: the SHA-256 and path of every file of this folder outside `timestamps/pr_folder/` | in its `STAMP.txt` | in its `STAMP.txt` |

**What they show.** That the copy existed in this form when the first stamp was made; that each blind reader's answer existed as it stands here when it came; and that the whole folder existed when the last was made.

**What they do not show.** That the blind readers were blind: their task sheets are in `blind_readings/`, the images they were given are not. Nor who read which group, nor that no decode came before the copy. Those rest on the contributor's session logs and on his record chain, a hash-linked list of every reading, plan, run and ruling of this work; the pull request that brought this folder gives the chain's head.

The first reading of 19 Nov 2026 was time-stamped when it was made. Its receipts are with the contributor and will be added with the outcome of the test.
