# LJS 51: plaintext transcription from the master TIFFs, keyed to cipher chains

Project C:\Users\dbour\cypher (Windows; python 3.12 with numpy/scipy/cv2/PIL; set PYTHONUTF8=1). Read
research\ljs51_pass\BRIEF.md (what the book is) and targets\ljs51corpus\pilot_report.md (what the pilot learned).

Inputs per page:
- master TIFF output\ljs51\master\0084_NNNN.tif (2339 x 2959); image = 6+2*(folio-1) for r, +1 for v (folio = (N-6)//2+1);
- page-pass record in research\ljs51_pass\pages_merged.json (field `n` = image number): ROUGH model reading of the 1422-px JPEG,
  with known errors (line numbers, counts). Use it as a draft only, correct it on the master.
- sign segmentation: `cd targets\ljs51corpus; python segment.py <N>` gives each line's kind (cipher/arabic) and the sign count
  per cipher line (about +-1 per line); `--overlay` writes an overlay to output\ljs51\crops\. Run it for each of your pages.

For EVERY cipher chain that starts on your pages (a chain = a cipher block, joined across a page turn when it runs on, e.g.
last lines of f. 12v and first lines of f. 13r) write ONE JSON line to your output file, as soon as the chain is done:
 chain_id: "<folio><r|v>.<first line>" of its start, e.g. "9r.7"
 pages: [{image, folio, lines:[first,last]}...]
 signs_per_line: from segment.py per line (list), signs_total, dividers_total (word groups = dividers+1)
 style: one short description of the sign style (invented glyphs / numerals / Arabic-letter-like / tree / dots ...)
 red_gloss: true/false; if true transcribe the red letters per line right to left in gloss_letters, 'not read' where unsure
 technique_note: what the compiler says about THIS cipher (Arabic phrase + English), if anything
 plaintext: {text: Arabic exactly as written on the master (no vowel marks, [?] for doubtful words, never invent),
             folio_lines: where it is, certainty: high|medium|low, source: "master"}
 plaintext_letters: count of Arabic letters in the plaintext (alif-lam as 2, lam-alif ligature counted as 2 letters; give also
             plaintext_words)
 fit_check: signs_total vs plaintext_letters vs word groups vs plaintext_words. Say 'fits' (equal within 2), 'signs > letters'
            (ratio), 'signs < letters', and a short hypothesis for any mismatch (plaintext only half given, nulls, a dropped letter,
            two signs per letter, plaintext is a recombination of verses, damaged, other). Do NOT force a fit.
 answered: yes | partial | no, and 'no' means you looked on the same page, the next page and the margins.
 notes: damage, show-through, anything odd.
Also for every plaintext passage that answers NO cipher (verse quoted in prose), do not transcribe it; only chains matter.
Be literal. If the Arabic is illegible, say 'not read'. Do not touch any other repo file. Reply with a 6-line summary: pages and
chains done, how many fit, how many mismatch (list the chain_ids), red-gloss chains, unanswered chains, anything not read.
