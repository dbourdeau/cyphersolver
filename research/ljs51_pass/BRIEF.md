# LJS 51 page-by-page pass: agent brief

Volume: Penn LJS 51, a Mamluk secretary's book of cipher verses exchanged with colleagues (text c. 1330-1370, copy 15th c.).
Layout: 13 long lines of Arabic naskh; each cipher is a block of 2-12 lines of invented signs separated by a dotted
vertical stroke; after it the compiler writes "fa-halaltuhu ... wa-huwa" (I solved it, and it is) and gives the plaintext
verses; some blocks have small red Arabic letters over the signs (a gloss).

Images: C:\Users\dbour\cypher\output\ljs51\web\0084_NNNN_web.jpg (1422 x 1800). Image 0084_0006 = f. 1r, 0007 = f. 1v,
... folio = (NNNN-6)//2+1, side r for even (NNNN-6), v for odd. Last text page 0217 = f. 106v. View each image with the
Read tool. If a passage is too small, crop/zoom with Python PIL into
C:\Users\dbour\cypher\output\ljs51\crops\ (git-ignored working folder; create it) and view the crop.

For EVERY page write one JSON object (one line) appended to your output file as soon as the page is done (never batch at
the end). Fields:
 image, folio, 
 contents: ordered list of segments on the page, each {kind: "arabic_text"|"cipher"|"plaintext"|"heading"|"marginal"|"blank",
   lines: [first line, last line] counted on the page, text: Arabic transcription (for arabic_text/plaintext/heading/marginal;
   use [?] for unreadable words, never invent), 
   for cipher: n_lines, signs_per_line: [..], approx_signs, word_groups (count of dividers+1 if you can), red_gloss: true/false,
   gloss_letters: Arabic letters if red letters are present, direction_remark }
 correspondents: names in "wa-kataba li X" / "katabtu lahu" with Arabic as written + transliteration
 technique_remarks: what the compiler says about the trick (lam-alif as one sign, dropped or null letters, direction, which
   letters fell first, how many alphabets, a named authority) - Arabic phrase + one-line English gloss
 plaintext_for: if a plaintext passage answers a cipher block, say which one (e.g. "block on this page", "block on previous page ff. Nr")
 cipher_without_plaintext: true if a cipher block has no plaintext following it anywhere in the pages you saw
 certainty: high|medium|low and a note on any damage, worm holes, cut-off text.
Be literal and honest: say "not read" for anything you could not read. Do not paraphrase from memory what an Arabic
cipher letter plaintext "should" be.
