# Timestamps

All stamps here are RFC 3161, from public time-stamping authorities (FreeTSA, DigiCert, Sectigo).

**Beside the files.** Most files of this folder carry their stamps beside them, made when the file was made: the request (`.tsq`) and one receipt (`.tsr`) from each authority.
- Some files carry none: the two READMEs, the plan's dated correction, and the strip's second reading's task sheet, recount and recount script. The manifest below covers them.
- The second reader's table and the note that counts it carry DigiCert's and Sectigo's only, as FreeTSA could not be reached that day.

**`pr_folder/`.** `MANIFEST.sha256` gives the SHA-256 and path of every file of this folder outside `timestamps/pr_folder/`. Its receipts and `STAMP.txt` are beside it.

**What they show:**
- that each stamped file existed in this form when it was stamped;
- in particular, that the plan existed as sealed at 18:38:11 GMT on 17 Nov 2026, before the first results file (18:59:47 GMT);
- that the blind readings existed before the plan;
- that the whole folder existed when the manifest was stamped.

**What they do not show:**
- that no run came before the plan;
- that the readers were blind;
- that the checking session kept frame 42 from the solving session.

Those rest on the contributor's session logs and on his record chain, whose head the pull request gives.

**To check a file's stamp:**
- DigiCert and Sectigo: `openssl ts -verify -data FILE -in FILE.<authority>.tsr -CAfile <a bundle of public root certificates>`.
- FreeTSA: the same, with `-CAfile` and `-untrusted` set to FreeTSA's own root and signing certificates, as its site publishes them.
