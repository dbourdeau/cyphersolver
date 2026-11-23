# Plan as frozen before decoding (copied unchanged from the work file PLAN_wellington_313.md, 23 Nov 2026)
# SHA-256 of the frozen file: e02991a7b0cdced98fe8f1429731b46a744454618c57ab42df19c38b94aa30bf

# Plan: decode the unread cipher runs of the Wellington letter (CEHM-Carso DCXXI.6.588.1, folios 2-3) with Narváez's key 313

Written 23 Nov 2026 by an AI agent (Opus 5.5) before any decoding of these runs.

Key (Narváez 2015 pp. 125-126; 2019 pp. 367-368, cited, not copied for any repository): Gronsfeld-type shift over the
27-letter alphabet A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z, cipher = plain + 3, +1, +3, repeating;
plain = cipher - 3, -1, -3, ...; the cycle starts with 3 at the first letter of each run (as in Narváez's own worked runs
"Republica" and "Contingentes de partida..."). Frozen; no other key or phase.
Line breaks ("/") inside a run: primary decode continues the cycle across the break. Pre-declared fallback: if the
part after the break gives no Spanish under the primary, it is decoded once as a new run (cycle restarting), and
counted under the label "restart at line break".
Text decoded: pass 1 (pass1_wellington.txt); letters where the blind pass 2 differs are counted as unsure.
Controls: 1,000 random 3-digit keys (digits 0-9, random.seed(20261123)) on the concatenated runs, mean log bigram
probability per letter (Spanish model from the Epistolario t. II clear text).
Pass mark: (1) key 313 scores above every control; (2) by eye, at least 60% of runs give Spanish words.
Counting: per run, words verbatim from the key / words with a marked repair (one or two letters, slip shown) / holes.
A run is "read" only if every word in it is verbatim or repaired and the words build a phrase in the clear sentence.

---

## What was decided after the plan (23 Nov 2026)

- Order: the plan, its hash, the decoding script and its output were written within nine seconds (00:37:33-00:37:42
  EST, file times). Nothing on disk proves the plan came first; it matters little, as the key, alphabet and phase rule
  are Narváez's published ones and only the line-break handling was a choice.
- The plan was run once on the first transcription: mean score -2.505; 999 of 1,000 random keys lower; the one equal
  control was 3-1-3 itself, drawn by chance (index 122); the best other key, 3-1-7, -3.664.
- After the blind second transcription three signs were changed, each checked on the image (NOTES.md, Transcription
  doubts): f3.02 sign 2 (overtyped; F chosen with the decode; TENEMOS counted as a hole), f3.04 sign 5 (S typed over B),
  f3.07 sign 9 (P; pass 1 had read the watermark's C). Words holding a sign on which the passes differ are holes, as the
  plan says (PARECER, EN, DOCUMENTOS, TESORERO).
- After the independent review the decoder was fixed so that an unsure sign ("?") keeps its place in the key cycle;
  the first decoder had skipped it. This turned ATINAS ORIENTACIÓN (f2.19) from read to a hole (NOTES.md).
- With the final transcription, `scripts/control.py` gives key 313 -2.444; best other key 3-1-7, -3.617
  (`control_313.txt`).
- The plan's line-break fallback is not used in the counts. Readings that need a shift in the key cycle were found
  after the run by the reviewer and are reported post hoc under their own rule (NOTES.md), not counted.
- Counting follows the repository's strict rule (a repaired or doubtful word is a hole), stricter than the plan's
  "verbatim / repaired / holes", and estimates the words hidden by each unread stretch: 247 clean of an estimated 296
  word places (0.834); 275 places if each stretch counts as one word.

## Added 23 Nov 2026 (after the third transcription)

A second plan (SHA-256 c17933f51479fbe15089478113b062a85e628ba9626d4709fd522569440ba5c7, kept in the contributor's
work folder with its scripts and outputs) froze a restart rule for the key cycle before running it on stretches it had
not been seen on: the cycle may restart (shift 3) at the first letter of a word, once per unread stretch, or a run
may continue the previous run's cycle across punctuation; 1,000 shuffles of each stretch as controls; pass at 80% of
letters in words and above the controls' 99th percentile. Result: f3.07's tail (8 letters) and f3.22's tail (4) are too
short and missed; f3.20's end needs a skip inside PROPIA, outside the rule, a miss. The counts are unchanged by it.
