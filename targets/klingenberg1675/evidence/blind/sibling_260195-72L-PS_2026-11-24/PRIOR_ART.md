# kling72: prior art (24 Nov 2026, before any transcription)

Passage: Conrad Biermann to Christoph (Estats Rath) Klingenberg, P.S. of the draft of late July 1675, Rigsarkivet unit 260195
images 72L-72R (api id 48574280, one spread). The body of the same draft (68R-72L) is filed upstream; this P.S. is not.

| source | what was checked | result |
|---|---|---|
| cyphersolver upstream main 8b75e65ac, targets/klingenberg1675/NOTES.md l.77, l.158 | the P.S. in the parked list | "Ten passages parked by the first reader (59R-60L, 70R, 254R, 263L, 274R, 72L-72R P.S., ...)"; "Logged figures (files not sent): ... 72L-72R P.S. 33/51" |
| same, NOTES_addition_2026-11-13.md l.113 | parked note | "260195 72L-72R P.S. (33/51 = 64.71% with the stray 'r' as E)" |
| same, evidence/first_reader/b165_PARKED.tsv row 11 | first reader's own log | "tx md5 00778ac5 frozen 14:50:53; strict 34/51 = 66.67% but one S unit is a stray 'r' (not a word): honest 33/51 = 64.71% < 65%; shuffle 0/5000 both seeds; PARKED on the 65% line" |
| same, evidence/first_reader/b165_LOG.md l.21 | token count | "FROZEN ... tx/kl_195_72ps_tx.txt md5 00778ac5a6e602b996c58305ecd68c4f ... (P.S. 122 tokens)" |
| same, NOTES.md l.160 | print | Aarsberetninger fra det Kongelige Geheimearchiv VI pp. 117-126 and Historisk Tidsskrift 5. R. IV pp. 446-450 "print the policy the letters carry", not their wording |
| open PRs | /tmp/openpr_files.txt (79 PRs with a refs/pull/N/merge ref, listed 24 Nov 2026 08:07Z) | none touches targets/klingenberg1675 |
| decode_updates/queue.json | DECODE | "No DECODE record: the Biermann copybook 1675 and its Koncepter unit are not on DECODE" |
| research/leads.json, catalogue.json | | the volume is target klingenberg1675 (ours, PR #455); no separate entry for the P.S. |

Verdict: no published reading of this P.S. anywhere. The only earlier decode is our own first reader's (b165, 12 Nov 2026,
not blind, transcription never sent upstream), which logged 33/51 = 64.71% strict and 0/5,000 shuffles, and parked it.
This is a re-test of OUR OWN key on a passage it nearly passed: a pass would be a blind confirmation, not a first reading.

Contamination: the packet builder (this sub-session) read the PARKED row, which names the P.S. topics in four words. None of
it is in packet/. The blind reader must not see the repo (PROMPT.txt rule 1); the judge sees only judge/BRIEF.txt and
judge/decode.txt.

Key: ours. key_frozen/ = byte copies of upstream main 8b75e65ac targets/klingenberg1675/key.tsv, maps/words_v4.json,
maps/table_M3.json (sha256 identical to the 16 Nov freeze used for 41R, 134R and 253R).
