# Sign transcription rules (Selvatico -> Riva, numeric cipher)

Transcribe signs only. Do not decode, do not guess plaintext, do not let any interlinear
writing or expected sense change a number. Work from full-size crops.

- One output line per manuscript line, prefixed with a line id: `21r.L05:`.
- Number groups separated by single spaces, in manuscript order.
- Marks on a group (record exactly what you see):
  - underline below the group: suffix `_`   e.g. `61_`
  - dot or small stroke/accent above: suffix `'`   e.g. `60'`
  - small numeral written above the group: suffix `^n`   e.g. `188^3`
  - a curl or hook written immediately before the number (looks like `c` or `(`): prefix `c`   e.g. `c13`
  - period or colon after a group: keep it, e.g. `287.`
- Uncertain digit: `?` after the group, e.g. `52?`; two possible readings: `52|72`; illegible: `#`.
- Clear (plain) words between groups: put them in braces, short is fine: `{ma fanno nello stesso tempo temere}`.
- Interlinear decipherments (words written above the numbers) are NOT transcribed in the cipher pass.
- Digit shapes in this hand: 3 often looks like `B`, 5 like `s`, 2 like a `z`/`r`, 9 with a long tail
  like `g`, 7 can resemble 2 (look for the straight top bar and the descending stroke), 8 like `&`/`ss`.
  Decide each digit from the shape; mark `?` when unsure rather than choosing by sense.
