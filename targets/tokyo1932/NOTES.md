# Tokyo, 1932: the Japanese Navy reads the State Department (American intercepts, January-September 1932)

Status: read in part (Japanese Navy's reading of 1932, measured by Brice Dudout, 28 Oct 2026: about 77 % of the words of 53 State Department telegrams recovered, 45-95 % by telegram, compared with the text printed in FRUS; the confidential passages were not read; no cipher groups survive in the file, so Daniel Bourdeau's 95% rule (certain / probable / restored / unresolved) cannot be applied to a reading of ours; the identification of the code as the Gray is a compatible hypothesis, not a proof).

Contributed by Brice Dudout (Europe chiffrée), 28-29 Oct 2026. Not in the catalogue: a historical codebreaking file, not an unsolved cipher. Published write-up: https://bdudout.github.io/europe-chiffree/en/ecoutes-japonaises-1932.html (site currently offline: the GitHub account is suspended; the write-up is committed and will reappear with it).

## What the documents are

Sixteen bundles filed among the records of the Navy Minister's secretariat for 1932 (公文備考 昭和7年 T 事件附属, "事件付属（米特情 極秘 号外 外）" (1)-(16), 海軍大臣官房記録), Military History Research Center, National Institute for Defense Studies, Tokyo, online through JACAR: Ref. C05022467800 to C05022469300. 796 images, about 850 messages (828 lines of inventory), 29 January - 28 September 1932, numbered 32 to 548 in the "米特情 極秘" series ("special intelligence, America, top secret") plus about 330 unnumbered ship-movement bulletins (号外).

Each copy is typed in English under the copied American heading (sender, addressee, number, word count, date, Tokyo time), with a handwritten Japanese title and distribution stamps (the round seal 中杉 of Commander Nakasugi Hisajirō, head of the Naval General Staff's cryptanalytic annex, according to Kotani). **No cipher groups are copied**: only the recovered clear text, with missing words left blank ("____") or reduced to their first letters ("co...."), and working notes such as 以下未解読暗号 ("what follows: code not deciphered") or 次ニ四十五語 未解讀暗號 ("there follow forty-five words in code not deciphered"). About 70 % of the lines are US Navy traffic (Asiatic Fleet, Cavite, Yangtze Patrol, 4th Marines), 25 % State Department (Peiping legation, Shanghai and Nanking consulates, Tokyo embassy), 3 % War Department. Most State Department telegrams from China went over Navy radio and were intercepted (Tokyo, about forty at Hiratsuka); cables of the Tokyo embassy carry Japanese telegraph marks (D.C., G.H., G.N.) and probably came from the telegraph administration. The JACAR images are "all rights reserved" and are not included.

## What we did

- Inventoried all sixteen bundles (inventory/, four batches a-d, working notes in French: JACAR item and image, 米特情 number, date and time, sender, addressee, series, code mark, length, unread parts, summary).
- Transcribed bundles (1)-(8) image by image (transcriptions/, English text of the copies with French working notes on stamps, seals and handwriting; bundles (9)-(16) are inventoried but not transcribed in full).
- Found the FRUS text of 53 State Department telegrams copied by the Japanese and compared them word by word (frus_pairs.md; gaps/ lists every blank, truncation and wrong word against the FRUS text, French working notes).
- Tested whether the errors betray a one-part (alphabetical) code (stats_initials.py, initials_pairs.tsv) and mapped what the Japanese code book contained (reconstructed_book.tsv).

## Results

- **What Tokyo read.** Word for word the Japanese copy renders on average about 77 % of the FRUS text (45 % to 95 % by telegram). The four batches were measured somewhat differently (sense recovered, identical words, manual count), so the figure is an order of magnitude. Structure, figures, dates and common names are nearly always right; losses fall on small, rare or abstract words and unusual proper names. Wrong values persist for months: *believe* is rendered "calculate" from March to September, *his* "trusty", *question* "realization".
- **Confidential passages not read.** In six telegrams the unread part begins at a paragraph break and covers exactly the most sensitive matter: Forbes, Tokyo, 1 Feb (the only paragraph FRUS paraphrases is blank in the Japanese copy); Johnson, Peiping, 12 July ("(28 words Enciphered)", "(251 words Enciphered)"); Grew, Tokyo, 2 Sept, no. 223 (45 words, the Vice Minister's confidence, "Please do not use his name in this connection."); Johnson, 7 Sept, no. 1078 on the Lytton report (only the first paragraph read, 以下未解読暗号 over the nine paragraphs of political analysis). Hypothesis: an ordinary code largely read, and an enciphered confidential code for sensitive matter.
- **A one-part code.** Wrong readings share the initial of the true word in 63 of 137 cases (46 %) against 6.3 % when the FRUS words are shuffled (10,000 draws); truncations have the right initial in 95 of 119 (80 %) against 6.1 %; p < 1e-4 for both, and in each of the four batches. Wrong words are alphabetical neighbours (*functioning* -> "fundamental", *admission* -> "admonition", *million* -> "military"): median alphabetical distance 0.10 against 0.30 for controls, replicated on the held-out batch d. The protocol was written before the calculation. Compatible with the Gray code (the State Department's ordinary one-part code since 1918, used without superencipherment; Kotani credits Nakasugi's office with solving it); not a proof, since neither groups nor a Gray copy are available.
- **The Japanese code book.** Of 1,972 distinct FRUS words: 1,107 always read right, 357 sometimes, 270 only replaced by another word, 181 never read (blank or initials), 57 only omitted (reconstructed_book.tsv). The errors are spread over the whole alphabet (a model predicting error zones fails on batch d: AUC 0.53 / 0.58 < 0.60 threshold).
- **US Navy.** The Asiatic Fleet traffic was mostly in clear. Sixteen dispatches of late January - 12 March 1932 carry an office-number group "00" (reserved for code dispatches by the Communication Instructions 1929) followed by a five-letter group, copied as such before a clear text: very probably the naval code indicator, so coded Navy dispatches were probably read as early as February 1932 (to be confirmed on the originals).
- **Where the Japanese copy corrects FRUS.** Cunningham, Shanghai, 9 Feb (III d288): FRUS "Rear Admiral Shimottowa [Shiozawa?]", Japanese copy "Shiozawa"; Peiping no. 328, 11 Mar (III d605): "the Japanese [forces?]" vs "the Japanese gendarmes"; Shanghai no. 222, 6 May (IV d3): "about 24,000 men of the 3d Division" vs "about 2400 men of the 14th division" (probably right); Nanking quoted in Peiping no. 500 (IV d541): dated 2 May in FRUS although quoting a note of 4 May, 5 May in the Japanese copy. The reverse also occurs (a negative lost, Chinese read "Japanese").

## Count by the 95% rule

Not applicable as a count of our own reading: the file contains no cipher groups, only the Japanese recovered clear text, and the code was not reconstructed by us. The measured quantity is the Japanese reading rate against FRUS (about 77 % of the words of 53 telegrams; see frus_pairs.md for each telegram and its method of measurement).

## Remaining gaps

- Confidential passages (e.g. Grew no. 223, last 45 words; Johnson no. 1078, paras. 2-10; Johnson 12 July, 28 + 251 words "Enciphered") - blocker: no-key-material; not read by the Japanese in 1932, and no cipher groups were copied, so nothing can be read from the file; the American text is known from FRUS.
- Code identification (Gray or another one-part code) - blocker: needs-physical-access; the NARA RG 59 file copies with their code groups are needed.
- Bundles (9)-(16) transcribed only as an inventory - blocker: needs-physical-access; the inventory lists every message and the comparison with FRUS covers them (gaps files), but a full transcription needs the JACAR images, which cannot be redistributed.

## Escalation

- [x] siblings: all sixteen bundles of the series opened; JACAR searched for other 米特情 / 英特情 years (none found apart from one 英特情 of 1937).
- [n/a] clear-pages: the copies are themselves the Japanese clear text; there is no cipher to match against a clear page.
- [n/a] known-keys: no cipher groups survive in the file, so no key can be tried.
- [x] print: FRUS 1932 vol. III-IV and Japan 1931-1941 vol. I searched; 53 telegrams found and compared.
- [n/a] key-rebuild: no groups to rebuild a key from; the Japanese code book is mapped through its errors instead (reconstructed_book.tsv).
- [n/a] retry: nothing of ours to retry; the unread parts are unread in the 1932 copies themselves.

## Files

- `frus_pairs.md`: the 53 compared telegrams (米特情 number, JACAR item and image, telegram, FRUS document, NARA decimal file, rate).
- `initials_pairs.tsv`, `stats_initials.py`: the one-part-code test (`python stats_initials.py` reproduces 63/137 and 95/119).
- `reconstructed_book.tsv`: every FRUS word of the compared telegrams and how the Japanese rendered it.
- `inventory/inventory_{a,b,c,d}.tsv`: the inventory of the sixteen bundles (French working notes).
- `transcriptions/C05022467800.md` ... `C05022468500.md`: image-by-image transcription of bundles (1)-(8) (English text, French notes).
- `gaps/gaps_vs_frus_{a,b,c,d}.tsv`: every unread or wrongly read group against FRUS (French notes).

## Caveats

- No cipher groups in the documents: the code identification (Gray) remains a compatible hypothesis. The State Department file copies (NARA RG 59, decimal files listed in frus_pairs.md) would settle it.
- Reading rates measured somewhat differently from batch to batch; "about 77 %" is an order of magnitude.
- The Japanese marks A.C., A.G., A.O., D.C., G.H. are not explained.
- What is said of Nakasugi's office rests on Kotani (read through a review) and the Japanese Wikipedia; Kotani's pages and Moriyama's articles of 2004 and 2007 not yet read directly.
- Working notes in inventory/, transcriptions/ and gaps/ are in French; NOTES.md, frus_pairs.md and the TSV headers are in English.

## Prior work

Kotani writes in one sentence that Nakasugi's office read the Shanghai consulate general's telegrams to the State Department during the Shanghai Incident and credits it with solving the Gray code; according to Moriyama Atsushi, in 1941 Japan read most State Department telegrams except the strip cipher. We found no publication that uses these sixteen bundles or compares them with FRUS (search of 28 Oct 2026, Japanese and English).

## Sources

- JACAR (jacar.go.jp), Ref. C05022467800 to C05022469300; copy of Grew no. 223: C05022469300, stamped images 0766-0767; Johnson no. 1078: same item, image 0777. Images not reproduced.
- Foreign Relations of the United States, 1932, vol. III (The Far Eastern Crisis) and vol. IV (The Far East); Japan, 1931-1941, vol. I (Office of the Historian, history.state.gov).
- Navy Department, Communication Instructions 1929, Part IV, arts. 3016-3023 (navy-radio.com).
- 小谷賢 (Kotani Ken), 『日本軍のインテリジェンス』, Kōdansha, 2007, ch. 3; English ed. Japanese Intelligence in World War II, Osprey, 2009. 森山優 (Moriyama Atsushi), "戦前期における日本の暗号解読能力に関する基礎研究", 国際関係・比較文化研究 3-1, 2004. Japanese Wikipedia, "中杉久治郎" (accessed 28 Oct 2026).

## Credits

Brice Dudout (dossier, choice of the material, rules: protocols written before calculation, held-out batch), with Claude (Anthropic) agents for inventory, transcription, comparison and write-up. American texts from FRUS (US government, public domain).
