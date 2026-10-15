# Castelcicala to Naples, two undated letters in a second code (ASNa Esteri 2337, DECODE R9586, R9588)

Status: in progress (transcribed 21 Sept 2026, not attacked; the pencil glosses are an untried crib). Written up in docs/r9586.html as attempted, not solved.

Split on 14 Oct 2026 from `castelcicala1816` under the one-key rule (George Lasry, 14 Oct 2026): one entry per key.
The old entry included these two letters because they share the sender, the busta and the catalogue items (166 and
167) with Castelcicala's despatches in the Segreteria di Stato code, but they are in another code. The Segreteria di
Stato code is a different cipher, with its own page ([`targets/castelcicala1816/`](../castelcicala1816/),
docs/castelcicala1816.html). Shared material stays there: the DECODE metadata (`decode/`) and the images (`img/`,
git-ignored, not public domain; main checkout `targets/castelcicala1816/img/IMG_R9586_*`).

Catalogue items 166 (R9588) and 167 (R9586) were restored on 14 Oct 2026, narrowed to these records, as
"attempted, open".

## The letters

- **R9586** (ASNa, Ministero degli affari esteri, busta 2337; catalogue 167): three pages, no number, address or date
  visible; signed "Castelcicala". 537 groups (`cipher/R9586.txt`), 240 distinct.
- **R9588** (same busta; catalogue 166): two pages, no number, Eccellenza or date; signed "Il Principe di
  Castelcicala"; the top four lines of p. 2 photographed blurred. 432 groups (`cipher/R9588.txt`), 220 distinct.

## The code

Numeric groups mostly 100–1100, plus a few 1405, 1415, 1657, 1697, 1698, 1858, 1930, 1952; dots between groups.
Frequent: 224, 1043, 1698, 294, 784, 319 (R9586); 294, 319, 1043, 269, 287, 456, 697, 101 (R9588). Many groups carry
short overbars, not all transcribed. Almost none of the 1400–2450 groups that dominate the Segreteria di Stato code;
the two letters share their frequent groups with each other, so they are one system. 344 distinct groups over both.

**Pencil glosses.** Sparse and faint syllabic glosses over a few runs, transcribed as `P:` lines in
`transcripts/R9586.txt` and `transcripts/R9588.txt`: e.g. R9586 p. 2 "se dell … cam bia … an … cut … ver", "ba li , che
non effett in o la sol tan za", "tta con … si … ri … chi … ed ella", "ei di san"; R9588 "tal … in che stato". They are
a possible crib, not yet aligned with the groups.

## Log

- 2026-09-21: transcribed with the rest of busta 2337; found to be in a different code; set aside.
- 2026-10-14: split from `castelcicala1816`.

## Remaining gaps

- R9586 and R9588 (different code, values 100-1100) - blocker: not-attempted; faint pencil syllabic glosses noted but not aligned; no key

## Escalation

- [ ] siblings: not done beyond the busta 2337 sweep of castelcicala1816 (no other letter in this code found there)
- [ ] clear-pages: the pencil glosses are the only clear text; not aligned
- [ ] known-keys: not done - the Segreteria di Stato key.tsv does not fit (other value range); no other key tried
- [ ] print: not done
- [ ] key-rebuild: not done - align the pencil glosses with their groups, then extend by repeats
- [ ] retry: not done
