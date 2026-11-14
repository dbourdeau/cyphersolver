# Frozen-key test on the Sorel letter (13 Nov 2026)

Files kept as run in the workspace (`output/pcc_jr_2026-11-13/`):

- `TEST_PLAN.md`: written before the run. Its key path `key/armylist_titlepage_1778.txt` is `../../key/` here, the
  same bytes (sha256 07e09b45..., frozen for this folder on 12 Nov 2026, before this letter was looked at). It says
  63 crib cells; `key_work.json` holds 56 distinct cells (the count in the plan was a slip).
- `key_work.json`: cell values solved from the clear words and word patterns of p. 227 before the key file was opened.
- `transcription_reading.txt`: the p. 227 transcription as tested (= `../transcription_pcc51v2p227.txt` plus one
  override: the box `.29 .14 .17 .9` read in line 18).
- `run_test.py`, `parse.py`: the test as run (`python run_test.py <key> transcription_reading.txt key_work.json`);
  the word measure uses `/usr/share/dict/words` of the machine it ran on (macOS). `test_result.txt` is its output.
- `make_alignment.py` writes `../alignment.tsv`.

`../../verify.py` section 5 re-checks the hashes, the crib agreement, the controls (agreement only, no word list) and
the alignment.
