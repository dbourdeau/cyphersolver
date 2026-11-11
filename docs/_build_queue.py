"""RETIRED 17 Sept 2026: the priority queue was removed from index.html (replaced by the catalogue section and CATALOGUE.md).
Kept for the structured data. Running it now does nothing.

Generate the priority queue section of docs/index.html from structured data.

The queue had drifted into a 31-row table in which items already attempted, items blocked at source,
and things that are not ciphers at all were interleaved with live targets at ranks 1 to 14. The ranks
had stopped meaning anything. This rebuilds it as three honest tiers, and emits a filterable list
rather than a table, because the reasoning column had become prose crammed into a cell.

Run:  python _build_queue.py    (rewrites the section in index.html between the queue and blocked anchors)
"""

CRYPTIANA = 'https://cryptiana.web.fc2.com/code/unsolved.htm'
T50 = 'https://scienceblogs.de/klausis-krypto-kolumne/the-top-50-unsolved-encrypted-messages/'
ELONKA = 'https://elonka.com/UnsolvedCodes.html'
GH = 'https://github.com/dbourdeau/cyphersolver/blob/main/'

# tier, name, date, href, badge, odds, oddsclass, effort, why
LIVE = [
    ("Blancmesnil to Nevers; Cocquet to Mangot; Joyeuse to Villars", "1580s&ndash;1616",
     "https://cryptiana.web.fc2.com/code/unsolved.htm", "", "low", "lo", "low",
     "Three short enciphered passages in volumes Gallica now serves over IIIF: BnF fr. 3633 f. 24, Clairambault 369 f. 316 and 500 de Colbert 33 f. 539. "
     "Each is too short to solve alone, but Tomokiyo's Nevers and Louis XIII articles print sibling keys for the same correspondents, so the test is "
     "key matching, an hour each. Not yet attempted."),


    ("DECODE R2179 (1644) and Starhemberg (1758), undelimited digit streams", "1644, 1758",
     "https://cryptiana.web.fc2.com/code/variable2.htm", "", "low", "lo", "high",
     "The two Austrian items left in Tomokiyo's article now that R2159 (Lucca) and R1408 (Warsaw) are read. Neither has token boundaries, so segmentation "
     "comes before substitution, which is the Vatican Part 5 problem again at a fraction of the length. The Lucca and Warsaw annealers apply once the "
     "stream is cut; the segmentation tools from the Vatican work are the first step. Not yet attempted."),

    ("Japanese telegram decoded by Yardley", "c.1920",
     "https://cryptiana.web.fc2.com/code/yardley.htm", "", "partial", "lo", "not started",
     "Yardley printed the plaintext, so the scheme is attackable, but Japanese diplomatic traffic of 1920 ran on codebooks. One message can only "
     "recover the entries it happens to use, so a complete answer is ruled out by construction."),
]

ATTEMPTED = [
    ("Antoine de Bordeaux to Brienne, London, 30 May 1653", "1653",
     GH + "targets/bordeaux/NOTES.md", "", "not solved, design identified", "lo",
     "A Thurloe intercept, BL Add MS 4200 f. 88, <b>810 tokens over 156 symbols</b> in Tomokiyo's transcription: graphic signs, plain numbers and three "
     "diacritic series. <b>Attempted 16 September 2026.</b> Identified as a cipher of the Brienne office's 1651&ndash;54 family, in which consecutive numbers "
     "run through the syllabary in alphabetical order across the diacritic series, as in Lasry's 1654 Mazarin&ndash;Bordeaux key. A solver with that "
     "order as a hard prior reads matched 810-token controls to 99&nbsp;%, and the letter never leaves the failed-seed band over 21 seeds; the rival "
     "reading of the symbol classes is unsolvable even on its own control. The control that explains it: misreading one diacritic in ten already "
     "drops the solver to 52&nbsp;% and 9&nbsp;% on two seeds, and Tomokiyo's copy is provisional. The plaintext is not in print (Birch, Guizot checked). "
     "Ways in: the DECODE images of R8390 to fix the diacritics, the 1653 English key for &ldquo;Mr. Bordeaux&rdquo; in BL Add MS 32263 f. 1 (R7537), or "
     "the letter-book at the BnF. The companion item, Mazarin to Bordeaux of 22 June 1654, was solved by George Lasry in February 2025 and is closed. "
     "<a href=\"" + GH + "targets/bordeaux/NOTES.md\">Notes &rarr;</a>"),

    ("Armstrong to Madison, 20 February 1808: the contest solution does not hold", "1808",
     "armstrong.html", "", "adjudicated", "md",
     "A different code from the postscript solved on this site: 369 groups running to 1900, plus shorthand-like symbol passages. <b>Adjudicated "
     "16 September 2026.</b> The AFIO contest solution of May 2025 rests on a 56-entry key. Scored against the letter, that key covers 36&nbsp;% of the "
     "groups, leaves 93 of its own 133 mapped occurrences unread, and uses five numbers that do not occur in the letter at all. Built by the same "
     "procedure on a shuffled ciphertext, 500 random keys fit the claimed sentence with all 60 words in order and account for more of the text than the "
     "AFIO key does. Madison wrote in May 1808 that no such cipher was in the office, and every pencil decode on roll 13 is THE&nbsp;=&nbsp;972, so the "
     "frames cannot supply it either. The claim does not hold; the letter stays unsolved and needs the key Armstrong actually used. "
     "<a href=\"" + GH + "targets/armstrong/NOTES.md\">Notes &rarr;</a>"),

    ("Lodovico Birago to the Duke of Nevers, the numerical paragraph", "1571",
     GH + "targets/birago/NOTES.md", "", "not solved, structure fixed", "lo",
     "BnF fr. 3251 f. 119, a letter of 13 November 1571 in Italian; one paragraph is in a figure cipher unlike Birago's other letters. <b>Attempted "
     "16 September 2026, four sessions.</b> The page was fetched from Gallica and re-read glyph by glyph: 483 digits, sixteen carrying a dot, bar or "
     "cross, nine wavy signs inline, six null letters. Every variable-length design was excluded with scans that recover the true rule on matched "
     "controls. What fits is the design of the Nevers Italian keys of 1588&ndash;89: two-digit letters with heavy vowel homophony, marked figures of one or "
     "two digits for names, nulls anywhere; 75 pairings satisfy it, all giving 228 letter tokens over 62 symbols. At that homophony and length the "
     "annealer cannot read its own controls (14&nbsp;% after 120 restarts), a word-level objective ranks the truth first but the search still fails, "
     "four-million-step anneals do no better, and the target scores in the same band, so the limit is the method. Also excluded: a Lucca-type "
     "polyphonic single-figure design, with a method that reads its control three times out of three; structured homophony rules; a syllabic "
     "alphabet. A sweep of the volume's 118 openings finds no second letter in the cipher. The Nevers key of 1574 (fr. 3315) is a symbol alphabet with a "
     "figure nomenclature 8&ndash;62, recorded as a gloss. Needs a sibling letter or one fixed code group. "
     "<a href=\"" + GH + "targets/birago/NOTES.md\">Notes &rarr;</a>"),

    ("Louis XIV to the Duke of Chaulnes in Rome, 10 July 1690", "1690",
     GH + "targets/chaulnes/NOTES.md", "", "not solved, design fixed", "lo",
     "<b>Attempted 16 September 2026.</b> The ciphertext verified from the page images, two transcription fixes: <b>300 groups, 116 distinct</b>. The "
     "step-10 chains give the design, a one-part Croissy table of ten columns running to at least 535. That is the whole result, because 300 groups do "
     "not determine a 116-entry nomenclator: the annealer recovers 4&ndash;12&nbsp;% of a matched control and wrong keys score within noise of the true one. "
     "No printed plaintext found; G&eacute;rin's 1877 article does not quote the letter. Needs the minute in Affaires &eacute;trang&egrave;res, "
     "Correspondance politique Rome 331&ndash;332, or a second letter in the code. "
     "<a href=\"" + GH + "targets/chaulnes/NOTES.md\">Notes &rarr;</a>"),

    ("Catherine de M&eacute;dicis to Philibert du Croc, 27 April 1567", "1567",
     GH + "targets/ducroc/NOTES.md", "", "below threshold", "lo",
     "Printed with a facsimile in Destray's 1924 life of du Croc; the plate fetched here from Gallica over IIIF and transcribed: about <b>147 symbols, "
     "40 distinct</b>, French, with sparse dots. <b>Attempted 16 September 2026.</b> A matched control, du Croc's own despatch of the same year "
     "enciphered with a 40-symbol key on the target's profile, is recovered at only 28&ndash;41&nbsp;% over six seeds, so a ciphertext-only attack at this "
     "length is below the solver's threshold and no reading is claimed. Lasry's key for the Charles IX letter in the same book is a different symbol "
     "set. What would move it: cribs from Catherine's and du Croc's other letters of April 1567, or the dots and ticks proving to be word separators, "
     "which would make it the Forster kind. The transcription needs a second reader. "
     "<a href=\"" + GH + "targets/ducroc/NOTES.md\">Notes &rarr;</a>"),

    ("Telegram from Switzerland, “BLUME SALAMANCA”", "1937",
     "https://github.com/dbourdeau/cyphersolver/blob/main/targets/blume/NOTES.md", "", "attempted, not solved", "lo",
     "Zurich to London and on to Spain, 8 January 1937, from the firm of Werner Oswald, who had close ties to Franco's side. <b>Attempted "
     "September 2026.</b> The first telegram is transcribed from Schmeh's photograph, 123 groups, and checks against the 125 words on the form. "
     "It is a <b>transposition</b> (index of coincidence 0.070, no bigram structure of its own) of what the letter counts say is telegraphic "
     "Spanish: two <i>q</i> in 615 letters, too many <i>p</i>, <i>t</i> and <i>x</i>, six <i>k</i> and <i>x</i> together, the profile of "
     "spelled figures and trade words rather than prose. A <b>lag scan</b> (planted controls light up at z 11&ndash;22; the telegram never "
     "passes 3.3) excludes every single columnar transposition and every reversed-direction double columnar at once. <b>Exhaustive "
     "enumeration of the second key</b>, proven on plants from 19 &times; 8 to 41 &times; 8 and 30 &times; 10 where the true key ranked first "
     "every time, excludes forward double columnar and both mixed conventions for every second key of ten or fewer letters with a first "
     "width up to 41. Local search on longer second keys fails on plants at this length, and the reason is measured: one wrong swap already "
     "costs half the signal, five make the key indistinguishable from random. What remains is the German-practice region, two keys of "
     "15&ndash;25 letters, and a single 615-letter message there is beyond published ciphertext-only attacks. Needs the second telegram, "
     "same day and same firm, or a crib such as <i>pesetas</i> or the firm's name."),

    ("Sir Richard Forster, 13 May 1644 (Val-d'Oise 68.H.8)", "1644",
     "https://github.com/dbourdeau/cyphersolver/blob/main/targets/forster/NOTES.md", "", "already read by others", "md",
     "<b>Found already read, September 2026.</b> The passage was deciphered by George Lasry after Britland's 2013 article, independently by Norbert "
     "Biermann, and again by Robert Pitt (GitHub, 14 September 2026), whose key is public; Tomokiyo's page still lists it as unsolved. It is <b>207 tokens in 37 "
     "comma-separated words over 34 symbols</b>, not 134 over 24 as the queue said, and the key is a mixed homophonic alphabet, not a regular Stuart key. The text is "
     "spiritual counsel: no scruple about failing God, take the ways of prudence to preserve your life for a greater sacrifice in the service of your brethren. "
     "Verified here: z&nbsp;=&nbsp;8.8 against 20,000 permuted keys, and 31 of 34 symbols recovered blind from the ciphertext once the word edges are used and the "
     "French model writes <i>u</i> for <i>v</i> and <i>i</i> for <i>j</i>; six matched 207-letter controls read at 98&ndash;100%. Without that normalisation the controls "
     "pass and the letter fails, which is the useful lesson. Four slips and two single-occurrence words need the manuscript. "
     "<a href=\"https://github.com/dbourdeau/cyphersolver/blob/main/targets/forster/NOTES.md\">Notes &rarr;</a>"),

    ("Charles I and Nicholas to Boswell, TNA SP 84/157 ff. 217 and 219", "1643",
     "https://github.com/dbourdeau/cyphersolver/tree/main/targets/boswell", "", "read in substance", "md",
     "<b>Attempted September 2026; alphabet solved, text read.</b> The alphabet was found by Robert Pitt days earlier (GitHub, 14 September 2026): a "
     "24-letter row, odd then even positions of the alphabet, repeated four times over 20&ndash;115, with supplementary homophones 116&ndash;159 in "
     "alphabetical blocks and nulls 0&ndash;19. Verified here: z&nbsp;=&nbsp;9.6 against 20,000 permuted rows, none as good. Added here: the four graphic "
     "signs are word-signs the clerk introduced inside the spelled word (good, Cousin, Master, us), which closes the passages Pitt left open; the King's "
     "&ldquo;Sir&rdquo; is the Duke of Courland's envoy at The Hague, and the letter sends him the &ldquo;re-credentials&rdquo; Simpson printed in 1893 "
     "from Mitau with a cipher line in the same key; Nicholas's covering letter asks Boswell to hinder the Dutch embassy of 1644. The King had heard nothing from the Duke but "
     "the invitation to the funerals of the two Dukes; he asks for muskets, match and powder to Weymouth, Dartmouth, Exeter or Falmouth, and knows not whether his answer "
     "arrived. A dozen single-occurrence word codes and a table of transcription slips remain; the folios would settle them. "
     "<a href=\"https://github.com/dbourdeau/cyphersolver/blob/main/targets/boswell/NOTES.md\">Notes &rarr;</a>"),

    ("Feuqui&egrave;res to Catinat, Pignerol, 25 January 1691", "1691",
     "feuquieres.html", "", "read (586 of 601 tokens)", "hi",
     "<b>Read, September 2026.</b> The 1819 <i>M&eacute;moires de Catinat</i> print the 418 groups; collated with the Munich page images. The code is the "
     "<i>petit chiffre</i> of the Pignerol governors, the 367-group companion of Bazeries&rsquo; Grand Chiffre de 1691 (his table transcribed from Gallica and "
     "verified on four despatches of 1690&ndash;91). A second letter in the same code, Louvois to d&rsquo;Herleville of 6 September 1690, sits in vol. I of the "
     "same edition with its contemporary translation, found by searching the OCR of all three volumes; the two letters share 72 groups. Exact aligners and "
     "annealers all failed (the translation paraphrases; <i>u</i>/<i>v</i>, <i>i</i>/<i>j</i> are one letter); one 31-group stretch where a single segmentation "
     "makes every repeated group agree, carried between the two letters by hand, reads the rest: 167 of 179 groups. Feuqui&egrave;res has Catinat&rsquo;s letter "
     "of the 24th at ten in the morning, is ready, cannot see how to pass the eighty horse to Saint-Ambroise, names the two roads into Avigliana and will keep the "
     "dragoons from escaping. Twelve singleton groups remain. <a href=\"feuquieres.html\">Write-up &rarr;</a>"),

    ("ADFGVX residue of the Eastern Front", "1918", "adfgvx.html", "top 50",
     "9 solved, 3 partial, 10 open", "md",
     "Not unbroken ciphers: Lasry and colleagues published the keys, and the twenty-two are mutilated transmissions. <b>Second session, "
     "September 2026.</b> The 2017 comment thread, read in full, had already solved nine and partly read three, by Norbert's rule of two block "
     "edits of up to five letters; Lasry's unpublished <b>sixteenth key</b> (CHI, 13 November) is rebuilt here and added to the fifteen. The table "
     "nobody published is now in the notes. Norbert's method, reimplemented with a German quadgram model, re-derives seven of the solved pages "
     "blind. On the ten never read (73, 152, 153 twice, 158, 170, 176b, 189, 198, 217) it finds nothing with any key, the CHI key fails on the two "
     "page-153 messages, and a key-free transposition attack fails its own 224-letter planted control. They need the Childs originals or a key "
     "that was never in the corpus. <a href=\"adfgvx.html\">Full write-up &rarr;</a>"),

    ("Huang Xing telegram, the scheme corrected from the frames", "1916", "huangxing.html", "", "scheme found, corrected", "md",
     "<b>Second session.</b> Frame 0247 read at 500 dpi gives a 46-character plaintext, and one superfluous kana at position 106 turns out to have "
     "hidden the repeats: with it dropped, &#34892; three times, &#36895; twice and &#38651; twice are <b>identical kana triples</b>. So the code is "
     "deterministic and the vowel is not a free homophone, which overturns the first reading; the seven row collisions are different characters. A "
     "row-to-digit permutation test against telegraph-code order is at chance. 42 codebook entries recovered; the kana-to-digit table needs a second "
     "telegram. <a href=\"huangxing.html\">Write-up, corrected &rarr;</a>"),

    ("Regent Moray to John Wood, the Scottish ambassador in London", "1568",
     "https://github.com/dbourdeau/cyphersolver/blob/main/targets/moray/NOTES.md", "", "undetermined", "lo",
     "BL Add MS 32091 f.213, 13 July 1568, <b>134 groups over 32 symbols</b> in Tomokiyo's transcription. The Catalogue of Additions says "
     "what the letter does: refuses Wood's recall and sends Border news. <b>Attempted September 2026.</b> A 5-gram Scots annealer, built from "
     "the <i>Diurnal of Occurrents</i>, the Privy Council register and Pitscottie, reads <b>five of six planted 134-letter controls</b> of the "
     "same symbol profile at 93&ndash;98%; on the letter it returns gibberish, scoring below every solved control, and English, French and "
     "Latin models do no better. No symbol behaves as a null or a word separator, Tomokiyo's variants are distinct symbols, twenty dragged "
     "cribs (the quene, Lethingtoun, Herreis&hellip;) are all rejected, and a word-code mask has no power at this length. Thirteen per cent of "
     "genuine Scots passages score below the solver's false optimum, and Border news is names, so the result is undetermined, not excluded. "
     "Needs the page, offline since the BL cyber-attack, or a second letter in the cipher."),

    ("Two anonymous letters to English Catholics in France, SP53/16 nos. 78 and 79", "1585?",
     "https://github.com/dbourdeau/cyphersolver/blob/main/targets/sp53/NOTES.md", "", "undetermined", "lo",
     "One to Mr Tempest, a priest in Paris, one to Dr Barret, president of the Rheims seminary, both endorsed by Phelippes and never read: "
     "<b>507 and 644 groups, 132 and 102 symbols</b> in Tomokiyo's glyph-label transcription. <b>Attempted September 2026, three sessions.</b> "
     "The first two closed the pair because the homophonic annealer failed its own planted controls; the third showed that was the annealer. "
     "A numba pipeline with a hot schedule, 168 parallel restarts and a reheat stage now reads <b>planted English and French controls of 507 groups "
     "and 130 symbols letter-perfect</b>, and a 507-group control carrying 24 word-signs. Under it no. 78 shows <b>no language basin in English, "
     "French, Latin, Italian or Spanish</b>, with or without word-signs: it scores where a failed control scores, and the reheat that finishes a "
     "control moves it nowhere. No. 79 sits at random-text level with base labels or with Tomokiyo's variants kept apart, although its symbol ratio "
     "is the easier one. Pooling the two letters scores worse than either alone, so the earlier same-key claim is withdrawn. A planted control with "
     "8&thinsp;% nulls plus word-signs is <i>not</i> read at this length, so a null-heavy design, a heavy nomenclator, a syllabary or merged glyph "
     "labels remain open and all need the page images. Calendar viii is full view on HathiTrust but refuses scripts. The &ldquo;Spanish spy&rdquo; "
     "slip SP 53/22 f. 52 (84 tokens, 22 symbols) stays below unicity. Needs the page images and the SP 53/22 keys, f. 53 first."),

    ("Catokwacopa, line 29 in Latin", "1875", "https://github.com/dbourdeau/cyphersolver/blob/main/targets/catokwacopa/NOTES.md", "top 50", "undetermined", "lo",
     "<b>Second session.</b> The exact-interleaving search rerun with a Latin vocabulary from 43 Latin Library texts. Control: line 17 returns QUI FIT "
     "first, ahead of <i>qui fuit</i>. Line 29 (<i>ereflodbr / rileohmae</i>) is junk in Latin as in English, three or four words at best; "
     "RELIGIONEM CONFIRMARE stays at eleven edits. The line is undetermined in both languages, and the Oxford reading is otherwise as audited before."),

    ("Sun Yat-sen telegram, the tail", "1916", "sunyatsen.html", "", "garble confirmed", "lo",
     "<b>Second session.</b> The received-message form re-fetched from JACAR and its second sheet read at 600 dpi: <i>xopavajejo ropezpo / ngobunibai "
     "tanaka</i>, every letter as Tomokiyo transcribed it. The garble after &#36820; is the operator's, not the transcriber's, and the three lost "
     "codes stay lost."),

    ("Armstrong: the roll 13 residue", "1808", "armstrong.html", "", "one group upgraded", "md",
     "<b>Second session.</b> The microfilm frames were re-fetched through the catalogue proxy. Frame 0190, a fully pencilled despatch of 20 July 1806 "
     "(&ldquo;a peace was signed last night between Russia and France&rdquo;), gives <b>1320 = like</b> as a reading from source, so the last clause "
     "of the postscript no longer rests on inference for that group; it also adds <i>last, night, about, look</i>. Thirty-nine more frames are down "
     "and unread. The 20 February 1808 letter is a different code and is adjudicated separately above."),

    ("Urquhart octastich", "17th c.", "https://github.com/dbourdeau/cyphersolver/blob/main/targets/urquhart/NOTES.md", "top 50", "book-cipher shape", "lo",
     "<b>Second session.</b> Measured: 272 numbers, 82 distinct, maximum 201, index of coincidence 0.021, forty per cent of values ten or less, "
     "and 31 of the distich's 32 values recur, so the two poems are one system with the shape of a word-index book cipher. Not attackable without "
     "the key text, and nobody has said where the octastich was printed."),

    ("Roosevelt cryptogram, number block", "1935", "roosevelt.html", "top 50", "explained, not a cipher", "lo",
     "Three lines of digits above the &ldquo;bite a lemon&rdquo; letter Friedman read in 1935. <b>Attempted 16 September 2026.</b> Read at glyph level "
     "from the 300 ppi Internet Archive scan of <i>The Friedman Legacy</i>, the block is a permutation of 1 to 52, each value once, with eighteen zeros "
     "in groups of six and three, as Thomas Ernst claimed in 2017. It is not a random permutation: rank correlation +0.39, a run 39 40 41 42, and "
     "sixteen rising chains where a fair shuffle gives 26, the marks of a list written by hand; a riffled deck fits worse. The ordered-key cipher "
     "readings that can be tested reach &minus;2.6 nats per letter with junk while seven of eight matched 52-letter controls are read at 88&ndash;100%. "
     "Unordered keys are untestable and indistinguishable from a doodle. <a href=\"roosevelt.html\">Full write-up &rarr;</a>"),

    ("Copenhagen cryptogram", "c.1950s", "copenhagen.html", "top 50", "not a simple substitution", "lo",
     "Three lines found behind an 1835 portrait of a Danish general, 107 characters. <b>Attempted September 2026.</b> Transcribed twice (20 and "
     "25 symbols), attacked in ten languages under six reading conventions and a word-separator hypothesis with a 5-gram annealer and dictionary "
     "re-ranking, then confirmed with 300 restarts. Nothing readable: best &minus;2.7 nats per letter, while matched controls of the same length "
     "in Danish, German, English, Latin and Swedish are recovered at 96&ndash;100% and &minus;1.4 to &minus;2.1. Either not a simple substitution "
     "of those languages, or both readings share an error only the original slip could fix. <a href=\"copenhagen.html\">Full write-up &rarr;</a>"),

    ("Scorpion letters", "1991", "scorpion.html", "top 50", "below unicity distance", "lo",
     "Two Zodiac-style cryptograms, 70 symbols with 53 distinct and 180 with 145 distinct. <b>Attempted September 2026.</b> Every S5 repeat falls "
     "at a multiple of 16; S1 shows a weak period-5 signal (p = 0.04). Both carry more key information than the English text has redundancy "
     "(249 vs 224 bits, 682 vs 576), and matched controls return fluent English at 3&ndash;13% letter accuracy, so no ciphertext-only solution can "
     "be verified. A claimed 2018 solution is consistent with the repeats but scores worse than the controls' false solutions. Needs S2&ndash;S4. "
     "<a href=\"scorpion.html\">Full write-up &rarr;</a>"),

    ("Abwehr agent Koehler's messages, New York to Berlin", "1944",
     "https://scienceblogs.de/klausis-krypto-kolumne/2017/02/19/the-top-50-unsolved-encrypted-messages-47-encrypted-messages-of-a-nazi-spy/",
     "top 50", "skipped: intractable", "lo",
     "Five messages, 924 letters, from the Dutch double agent Walter Koehler. <b>Attempted September 2026.</b> Every tractable class is excluded "
     "against controls: substitution and transposition by the index of coincidence; Vigen&egrave;re, Beaufort and autokey at every period in "
     "German, English and Dutch; a running key from book text, which would show in the letter counts (true cases gain at least 7.5 nats, these "
     "score below uniform); and <b>any Enigma</b>, because the counts are too uneven for machine output (&chi;&sup2; 57.9, p = 0.0003). What "
     "survives is a book key through a mixed alphabet table, the documented prayer-book system, or a hand one-time pad. Neither falls without "
     "the book or the FBI's plaintexts. The attempt also corrects one letter of the circulating text."),

    ("Censorship manual steganograms", "WW2",
     "https://scienceblogs.de/klausis-krypto-kolumne/2017/05/03/the-top-50-unsolved-encrypted-messages-33-the-censorship-manual-steganograms/",
     "top 50", "image resolution", "lo",
     "A British censorship manual (TNA KV 2/2424) gives the plaintext of a map and a fashion drawing but not the readings. <b>Attempted "
     "September 2026.</b> The one published fragment (AATHUT &rarr; LLESFE, <i>alles fertig</i>) fixes the map's shift direction, and the "
     "exact dot-dash sequence any German wording would leave is now computed, so a reading can be checked mark by mark. The tram bands "
     "themselves are ordinary map fill; the Morse is pen marks beside them, and those are 0.1&ndash;0.3&nbsp;mm &mdash; 2&ndash;5 pixels in "
     "the best public photograph, where dots and dashes merge. Needs a 1,200&nbsp;dpi scan of pp. 14 and 17. The manual's &ldquo;French "
     "shorthand&rdquo; points to Duploy&eacute; for the signature."),

    ("Debosnys cryptograms", "1882–83", "debosnys.html", "top 50", "attempted, not solved", "lo",
     "About 1,200 glyphs in an invented script, left by a man hanged in 1883. Three passages transcribed here, 969 glyphs. The cipher poem is "
     "<b>rhyming couplets</b> &mdash; the last glyph matches within 9 of 10 couplets and across none of the boundaries &mdash; and line length and "
     "rhyme both point to a <b>French syllabary</b>. Every crib that could be tested failed against controls that would have found a hit: the poem "
     "on the same page, 7,821 couplet windows of French verse, Delille's <i>Aeneid</i>, Moore. The corpus sits at its unicity distance and a "
     "planted syllabary of the same length recovers 0%, so it falls only to a crib from his papers. <a href=\"debosnys.html\">Full write-up &rarr;</a>"),

    ("Vatican Challenge, Part 5 — Farnese to Poggio", "1542",
     "vatican.html", "", "family identified", "md",
     "Identified as a polyphonic-syllabic cipher of the kind <b>Antonio Elio</b> built for Paul III's chancery — the chancery that sent this letter. "
     "Six sessions: the Meister keys verified from the page scans and excluded on structure, the letter dated from its own cleartext (15 April 1542), "
     "the sibling and relative records located in DECODE, and a unit-level attack (segmentation by EM, then annealing) shown by a matched control to "
     "fail on the segmentation step. Still unread; needs the 400 dpi images behind the DECODE login, the key in Chigi M II 49, or the clear register copy."),

    ("D’Agapeyeff cipher", "1939", ELONKA, "famous", "diagnosed", "lo",
     "196 digit pairs, and the author admitted he had forgotten his own method. Five independent lines — frequency against the author's own worked "
     "control, no transposition signal, no periodicity, repetition far below language, and the book's own null rule swept — all say near-uniform "
     "random. Consistent with a botched encipherment rather than a lost key."),

    ("Maltravers to Ormonde — read", "1634–35", "ormonde.html", "", "solved", "hi",
     "The alphabet is recovered and every spelled word reads. <b>Second session:</b> the nomenclator checked against Wentworth's own dispatches in "
     "Knowler's <i>Strafforde's Letters</i> (1739) — the King refusing to see Kildare, and the 22 December 1634 dispatch moving Ormonde for the "
     "Council in exchange for Sir Piers Crosby, with Coke's marginal answer that the warrant is enclosed. Seven of nine codes fixed; the two "
     "parties in &ldquo;what [185] hath written unto [149] concerning Crosby&rdquo; would need the key sheet."),

    ("Kaliningrad bottle post", "found 2015",
     "https://scienceblogs.de/klausis-krypto-kolumne/2017/10/17/the-top-50-unsolved-encrypted-messages-19-the-kalinigrad-bottle-post/",
     "top 50", "transcription", "lo",
     "The blocker is transcription, not cryptanalysis: it exists only as two photographs and nobody has ever published the character string. "
     "Attempted and abandoned honestly — cursive n, u, v and w are barely separable and the verso bleeds through. Two observations stand: the "
     "primed consonants are exactly the Russian palatalisation set, and the text carries dotted initialism groups that would be the natural home "
     "for Bible citations under the outstanding Synodal-Bible claim."),

    ("Colbert passages, Thurloe intercepts, D’Estaing, Le Tellier", "1653–1779",
     CRYPTIANA, "", "too short", "lo",
     "Four separate items that fail the same way. Each is a short passage — sixteen to two hundred and seventeen groups — with every known period "
     "key already tested and failing, and hill-climbing yielding fragments only. None is long enough to solve unconstrained, and the originals are "
     "not digitised."),
]

NOTCIPHER = [
    ("Voynich manuscript", "c.1420", "voynich.html", "famous",
     "<b>Adjudicated September 2026</b>, not deciphered. Six computational tests on the transliteration against eleven languages and implemented hoax "
     "generators, each re-run adversarially, plus five literature sweeps. A plain or simply enciphered European language is excluded on transliteration-"
     "robust entropy (h2 2.2&ndash;2.9 bits against a 3.3 floor); Rugg's grille and free-edit self-citation are disfavoured; a verbose or slot-template "
     "encoding and a structured meaningless text are left roughly even, with the tests that would separate them. <a href=\"voynich.html\">Full write-up &rarr;</a>"),
    ("Kryptos, passage K4", "1990", ELONKA, "famous",
     "97 characters. The plaintext was recovered from Sanborn's own papers in 2025 — explicitly not a cryptographic solve — and the archive sold at "
     "auction for $962,500. The method remains unbroken and the plaintext unpublished."),
    ("Zodiac Z13 and Z32", "1970", ELONKA, "famous",
     "Z408 fell in 1969 and Z340 in December 2020. What is left is thirteen and thirty-two symbols, far too short for any answer to be verifiable."),
    ("Dorabella cipher", "1897", ELONKA, "famous",
     "Eighty-seven characters. Wase's 2023 statistical study finds it unlikely to be monoalphabetic English or Latin at all, which undercuts most of "
     "the century of proposed solutions at the root."),
    ("WWII pigeon cipher, Bletchingley", "1942?", ELONKA, "famous",
     "135 letters. GCHQ's position is that without the codebook the message cannot be decrypted, nor any claimed solution verified."),
    ("Enigma message of 10 January 1945", "1945", CRYPTIANA, "",
     "A single message, and compute-bound. The comparable unsolved M4 messages fell only to distributed computing."),
    ("Lüderitz consular telegram", "1911", CRYPTIANA, "",
     "A five-figure codebook. One message recovers nothing without the book."),
    ("Phaistos disc, Linear A, Indus script, Rongorongo and the rest", "c.2600 BC – c.1800 BC", ELONKA, "famous",
     "Undeciphered writing systems, not concealed messages. These are problems for linguistics, and several may not encode language at all. "
     "Meroitic can be read aloud without being understood, which is the clearest illustration of the difference."),
]


def badge(b):
    return ' <span class="fam">%s</span>' % b if b else ''


def target(rank, name, date, href, b, odds, oc, eff, why, cls=''):
    r = '<span class="tg-rank">%s</span>' % rank if rank else '<span class="tg-rank tg-dash">·</span>'
    link = '<a href="%s">%s</a>' % (href, name) if href else name
    meta = '<span class="odds %s">%s</span>' % (oc, odds)
    if eff:
        meta += '<span class="eff">%s</span>' % (eff + ' effort' if eff in ('low', 'medium', 'high') else eff)
    return ('<article class="tg %s">\n  <div class="tg-l">%s</div>\n  <div class="tg-b">\n'
            '    <h3>%s<span class="tg-date">%s</span>%s</h3>\n'
            '    <div class="tg-meta">%s</div>\n    <p>%s</p>\n  </div>\n</article>\n'
            % (cls, r, link, date, badge(b), meta, why))


def build():
    out = []
    out.append('<h2 id="queue"><span class="num">02</span> Priority queue</h2>\n')
    out.append('<p>Everything open, from all three source lists, on one scale. <b>Odds</b> is the estimated chance of a full reading; '
               '<b>effort</b> is the work needed to find out. A cheap decisive test outranks an expensive long shot, so a coin-flip that '
               'resolves in an hour sits above a one-in-four that costs a week. Badged entries come from '
               '<a href="%s">Elonka Dunin\'s famous unsolved codes</a> and <a href="%s">Schmeh\'s Top 50</a>.</p>\n' % (ELONKA, T50))
    out.append('<div class="qfilter" role="group" aria-label="Filter the queue">\n'
               '  <button class="qf on" data-f="all">All <span>%d</span></button>\n'
               '  <button class="qf" data-f="live">Worth continuing <span>%d</span></button>\n'
               '  <button class="qf" data-f="done">Attempted <span>%d</span></button>\n'
               '  <button class="qf" data-f="no">Not a cipher <span>%d</span></button>\n'
               '</div>\n' % (len(LIVE) + len(ATTEMPTED) + len(NOTCIPHER), len(LIVE), len(ATTEMPTED), len(NOTCIPHER)))

    out.append('<h3 class="tier" data-t="live">Worth continuing <small>no archive access needed; ranked by odds against effort, the next step named in each</small></h3>\n')
    for i, t in enumerate(LIVE, 1):
        name, date, href, b, odds, oc, eff, why = t
        out.append(target(i, name, date, href, b, odds, oc, eff, why, 'live'))

    out.append('<h3 class="tier" data-t="done">Attempted &mdash; findings recorded <small>what was established, and what is left</small></h3>\n')
    for name, date, href, b, odds, oc, why in ATTEMPTED:
        out.append(target(None, name, date, href, b, odds, oc, '', why, 'done'))

    out.append('<h3 class="tier" data-t="no">Open, but not settleable by cryptanalysis <small>listed, not ranked</small></h3>\n')
    for name, date, href, b, why in NOTCIPHER:
        out.append(target(None, name, date, href, b, 'not tractable', 'no', '', why, 'no'))
    return ''.join(out)


def main():
    p = 'index.html'
    s = open(p, encoding='utf-8').read()
    if '<h2 id="queue">' not in s:
        print('queue section retired; nothing to do'); return
    i = s.index('<h2 id="queue">')
    j = s.index('<h2 id="blocked">')
    s = s[:i] + build() + '\n' + s[j:]
    open(p, 'w', encoding='utf-8').write(s)
    print('queue rebuilt: %d live, %d attempted, %d not-a-cipher' % (len(LIVE), len(ATTEMPTED), len(NOTCIPHER)))


if __name__ == '__main__':
    main()
