# LOG b77 Olivazzi pass 2 (UTC 2026-11-11)
- 22:14 start. 22:16 2r/2v fetched full scale (4273x5487, 4261x5345; 1,024 px tiles; md5 in img/). Own scripts in scripts/ (fetch, linecrop, reg, diff). b70 dec.py/ledger.py/baseline.py/agree.py run unchanged with python3 -I.
- 22:20:30 FREEZE pass B: md5 c4cc509ac0bf5823f1944e56b4b9e0f9 (379 units: 2r 180, 2v 199).
- 22:20:36 opened KEY_K3.tsv (md5 65b083be69e3a4c6219c65566aee20fc) and dec.py. One decode, K3 unchanged. Default ledger 302/378 = 79.89% (before word-level overrides); strict with 34 overrides 268/378 = 70.90%.
- 22:22:15 opened b76 pass A tx (md5 b7dac699...). Line IDs normalised in a work copy only (L01 -> L1); b76 files untouched. Agreement and 27 loci: ADJUDICATION.md.
- Consensus tx md5 95845a8ebde2da401f4fd9fe65248ac2. First consensus run had a notation slip ("181[sup-al]" split on the hyphen into 2 ILL units; 278/378 = 73.54%); fixed to "181[sup]"; final 278/377 = 73.74%. Both runs recorded here.
- Baseline 5,000 shuffles seed 1725: 0/5000 >= real (consensus and pass B).
- Not opened at any time: b76 L1725 READING.md, work/, overrides; any other KEY file.
- crops/ holds a first set of line crops cut with a wrong pitch (superseded by crops2/). A cleanup rm was refused by the safety check; files left in place.
- Nothing sent or posted. Outbound: IIIF manifest + tiles (edl-jarvis.cultura.gov.it); timestamp hashes via stamp.sh.
