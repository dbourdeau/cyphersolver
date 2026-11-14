# Starhemberg, Paris, 23 May 1758

**Substantially deciphered, with a complete proposed reading.** The German reconstruction and English translation cover the whole letter, including Farinelli’s statement to the recipient and Wall’s matching statement to the French ambassador. Remaining uncertainty concerns particular words, repairs and conventions, rather than large unread passages. An exact decipherment is not established: eleven conjectural digit repairs, four contextual readings of 99 as g, and several uncertain key alternatives remain explicit.

Read the [annotated edition](edition-2026-09-21/README.md) or the [side-by-side public page](https://aaymeloglu.github.io/unsolved-ciphers/starhemberg-reading.html).

Photographs supplied by Satoshi Tomokiyo with Alexandre Pillon’s permission on 21 September 2026 support a transcription of **1,726 digits in 21 physical lines**. Five digits are absent from the Cryptiana transcription. The photographs and DECODE key images are not redistributed. Source links, attribution, caveats and the German/English text are in the edition.

## Evidence and reproduction

The surviving 1752 Austrian Prima/Secunda key supplies the reading. Under [CONVENTIONS.md](../CONVENTIONS.md), the manuscript parse has **413 units: 398 H, 12 M, 3 I**; the proposed emended parse has **404 units: 378 H, 8 M, 18 I**. Counts include nulls and controls. Editorial word divisions, spelling and inflections are not separately authenticated by these grades. No statistical language model is used.

Run `python3 run_checks.py` from this folder to reproduce the historical controls and verify the current edition. Run `python3 edition-2026-09-21/build.py --check` to check the edition alone. The [transcription](edition-2026-09-21/manuscript-lines.json), [observed collation](edition-2026-09-21/collation.json), [repair ledger](edition-2026-09-21/emendations.json), [graded tokens](edition-2026-09-21/emended-tokens.json) and [physical alignment](edition-2026-09-21/alignment.tsv) separate source readings from proposed repairs.

## Research audits

The root-level ciphertext, keys, scripts and experimental outputs preserve the reproducible Cryptiana baseline and independent historical controls. They use 1,721 transcription digits and are not the manuscript edition. The [17–18 September audit](audit-2026-09-18.md) records that stage’s conclusions and failure log; the [current edition](edition-2026-09-21/README.md) states the supported reading and remaining research routes. Historical controls establish the cipher mechanics, not the truth of the proposed repairs.
