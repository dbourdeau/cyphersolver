# stmauris1548 / dudout: four held-out tests of the key (O2-O5) and two blind shape sheets

Brice Dudout (with Claude), 23-25 Nov 2026. Supporting files for issue #977. Outside this folder only `../profile.json` changes: one
solution step per test and per sheet, failures included.

All four tests **failed** their preregistered bar. The two shape sheets are readings of sign shapes, not measurements:
they change no verdict.

## Key used

All four tests used **`key.tsv`**, the current table, not `key_frozen.tsv`. Our issue called it "the frozen key"; that
was wrong. `key_frozen.tsv` is the frozen table on main.

| file | SHA-256 | used |
|---|---|---|
| `../key.tsv` | `b9e69238cd30569c01b1566bc6548fb1d16a030c652ecca053c6a98b89d5e034` | yes, O2, O3, O4, O5 and both sheets (unchanged) |
| `../key_frozen.tsv` | `ec7396e1ceb0ae94adb8c54911f8bf129a6ab11980599b3aac63bb8f7ff89dfe` | no |

The PREREGs name it `../o2-2311/wainut-key.tsv`: that was our local copy of `key.tsv`, byte-identical (same SHA-256)
and checked against main at 9812a45218 (O2), b13dd55072 (O3) and b81c613843 (O4, O5). It is still identical on main at
4c2ca49a21. The copy is not repeated here; read `../o2-2311/wainut-key.tsv` as `../key.tsv`. Neither table was built
on the 1547 letter or on the 12 March 1548 letter. `input/SIGNS.md` in o3/o4/o5 is byte-identical to `../SIGNS.md`
(`678be0a4…`).

## Preregistrations (frozen before any transcription)

| test | portion | file | SHA-256 at freezing | frozen (CET) |
|---|---|---|---|---|
| O2 | 1547, c. 1r | `o2-2311/PREREG-O2.md` | `e85e333c352919aa97cc7a158432b0ac64313e8b46d9152d2f42277568b9dd1f` | 23 Nov 22:11:38 |
| O3 | 1547, cc. 1v-2r | `o3-2511/PREREG-O3.md` | `fd80c8234ba34c04c35a7752982475af690a250fb2be2919257b4af9dbf330cc` | 25 Nov 08:01 |
| O4 | 12 Mar 1548, cc. 5r-6r | `o4-2511/PREREG-O4.md` | `f95a74e4af6dde254bdfa17daa2e03134b7653ad706c9c3ae9a6f3a5b5a8ba7a` | 25 Nov 09:55:45 |
| O5 | 12 Mar 1548, cc. 6v-8r | `o5-2511/PREREG-O5.md` | `ebd2429ba2a12b92b530eaa7534d5543b899e74571289d16221bebb50a4df7e7` | 25 Nov 10:53:44 |

The preregistrations are byte-identical to the frozen files; the private disk paths they mention hold the Estense images, which are not shared. `shasum -a 256 -c` passes on every `.sha256` sidecar.

## Results

| test | transcription | measure (file) | result |
|---|---|---|---|
| O2 | one blind pass (27 rows, 602 tokens measured) | lexical coverage M 0.718 < 0.85; best of 200 controls 0.438, margin 0.280 < 0.30 (`MESURE-O2.txt`) | FAIL |
| O3 | passes A/B, agreement 0.961; 31 disputes arbitrated blind | M 0.784 < 0.85; controls max 0.391, margin 0.393 (`MESURE-O3.*`, `RESULTAT-O3.md`) | FAIL |
| O4 | passes A/B, agreement 0.926; 104 disputes arbitrated blind | M 0.780 < 0.85; controls max 0.415, margin 0.365, z 8.43 (`MESURE-O4.*`, `RESULTAT-O4.md`) | FAIL (0.85 bar only) |
| O5 | passes A/B, agreement 0.830; 250 disputes arbitrated blind | read by sense by two readers who saw only the decode: 0.850 and 0.826 < 0.95; restored 0.092 and 0.074 > 0.05; M 0.659, margin 0.251 < 0.30 (`MESURE-O5.*`, `VERDICT-O5.txt`, `RESULTAT-O5.md`) | FAIL |

`o4-2511/NOTE-MARGE-5r.md`: the clear note in the left margin of c. 5r (masked from the transcribers, read after O4 was
closed) is a period decipherment of 5r L01-L03; it matches the O4 decode word for word apart from spelling.

The RESULTAT, INTEGRATION and NOTE files are our working notes, in French.

## Files

Each test folder holds, where they exist: `PREREG-*.md` (+ `.sha256`), `input/` (briefs and shape lists given to the
transcribers), `passe-A/` and `passe-B/` (blind passes, each with its `.sha256`), `COMPARAISON-AB.txt` (A/B agreement),
`ARBITRAGE/` (`disputes.json`, `CANDIDATS-DESCRIPTIONS.md`, `ARBITRAGE.tsv`: the blind arbitration, shapes only), the
merged transcription (`*_merged.txt` + `.sha256`; O4/O5 also `*_merged_named.txt` after the namespace step),
`MESURE-*.txt/.json`, `RESULTAT-*.md` and `tools/` (merge, compare, measure, naming step). `o2-2311/measure_o2.py` is
the measure of O2 and O3. O5 adds `BRIEF-LECTURE-O5.md`, `lecture-input/DECODE-O5.txt` (the only thing the readers saw),
`lecture-L1/` and `lecture-L2/` (`LECTURE.txt`, the reading; `JUSTIFICATIONS.tsv`, the justification sheet;
`L1.json`/`L2.json`, the checker's word classes), `ACCORD-L1L2.json` and `VERDICT-O5.txt`.

Left out: page images, line crops, arbitration boxes, sheet thumbnails and sheet HTML (they hold Estense crops), the crop
scripts and crop hash lists (`make_crops*.py`, `CROPS.sha256`), and our copies of WAINUT's own files.

## Shape sheets of 25 Nov (reading only, not a measurement)

Two blind shape sheets were shown to Brice. For each, the selection rule was hashed before any thumbnail was made, and
the sheet carried hidden controls.

| sheet | rule (SHA-256) | answers exported (SHA-256) | controls |
|---|---|---|---|
| `planche-2511/` stmauris1548-2511 | `REGLE-SELECTION.md` `91feba56…` (`.sha256`) | `reponses/reponses-stmauris1548-2511.json` `8956a94b…` | K2 `O`, K3 `x` passed; K1 `w` missed, waived as a construction fault (its twin "∞" was among the options) |
| `planche-2511b/` stmauris1548-2511b | `REGLE-SELECTION.md` `1fe966ee…` (`.sha256`), `AVENANT-1.md` before sending | `reponses/reponses-stmauris1548-2511b.json` `2210b6b6…` | K1 `x`, K2 `d`, K3 `O` passed |

- `CLE-OPTIONS-*.json`: the sheet key reduced to the option order (which shape is behind each "forme N", and the
  expected answer of each control), extracted from the private key file, whose SHA-256 it gives (`cede47b5…`,
  `7697ebc5…`). Crop names, boxes and example places are left out.
- The exported answers are kept byte for byte, with Brice's shape remarks, so their hashes check.
  `planche-2511b/reponses/REMARQUE-CHAT.txt` is a shape remark he made outside the export.
- `integration/`: what each sheet changed, applied to copies of the O5 transcription and readings (`recompte_*.py`,
  `*.json`, `LECTURE-*`, `DECODE-O5-avec-planche(s).txt`, `transcription_*_avec-planche(s).txt`). The scripts read the
  private key file, which is not here. In this copy of `INTEGRATION-2511.md` one personal aside in a quoted message is cut
  (`[…]`).
- `SIGNS-ajout-2511.md`: the shape-list additions for a future preregistration on another letter: `w` also
  drawn as two rings side by side with a short stem and no bar ("∞"); `vt` also drawn as "ox"; `N4` also a small closed
  loop in v or D with a lead-in stroke. The frozen SIGNS.md copies are not edited.

Outcome of the sheets: the 95 "∞" tokens are `w` (o by the key), the 45 "ox" tokens stay `vt` (s), the 22 looped tokens
are `N4` (m); "Piemont" (6v L15) reads "poemont" and stays unresolved. With the key unchanged, unknown letters in the O5
decode fall from 215 to 98; sure words rise from 193 to 266 (L1) and 201 to 271 (L2); restored words fall to 3.4 % and
2.6 %; share read 0.850 and 0.824. O5 stays FAIL.

## Checking

`SHA256SUMS` lists every file in this folder except itself (`shasum -a 256 -c SHA256SUMS` from this folder).

Images: Biblioteca Estense Universitaria, Modena (IIIF, CC BY-NC-SA), used for private study only; none are here.
AI agents (Claude) made the crops, transcriptions, arbitration and readings; Brice Dudout answered the shape sheets and
reviewed the results.
