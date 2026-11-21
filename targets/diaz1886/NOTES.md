# Porfirio Díaz to Bernardo Reyes, ten cipher telegrams without a translation, 1885–86 (CEHM-Carso, Fondo DLI; catalogue 1460, part)

Status: in progress

**Transcribed, not read.** This folder holds the numerals of ten of the telegrams of catalogue 1460 and nothing else: no key and no decode. A key is being rebuilt from translated sister telegrams; it will be tested under a plan that was sealed and time-stamped on 20 Nov 2026, before any telegram here was decoded, and the result will be added here whichever way it falls (section 7).

Contributed by Jacob Houtrouw (`houtrouw`), with AI models working at his direction. Section 6 says what was used and who did what.

## 1. The unit
Catalogue 1460 is the cipher telegrams in General Bernardo Reyes's archive that the archive lists without a translation. Its row names them by shelfmark, from November 1885 to July 1909. This folder covers the first ten the row names: one of November 1885, one of July 1886 and eight of October 1886. By the archive's listing all ten are signed by Porfirio Díaz in México and addressed to Reyes.

The archive is the Centro de Estudios de Historia de México Carso (CEHM), Fondo DLI. The images are on its viewer; they are linked here and none is copied into the folder (section 2). The other telegrams of the row are not in this folder.

## 2. The telegrams
| Telegram | In the archive's listing | CEHM record | Hand | Images | Groups | Open | Read |
|---|---|---|---|---|---|---|---|
| DLI.2.397.1 | México, noviembre 26 de 1885 | 112727 | A | 1 | 44 | 1 | twice (44 of 44 groups the same) |
| DLI.4.771.1 | México, jul. 17 de 1886 | 114128 | A | 2 | 62 | 0 | once |
| DLI.5.907.1 | México, oct. 8 de 1886 | 114532 | B | 2 | 77 | 0 | once |
| DLI.5.909.1 | México, oct. 8 de 1886 | 114534 | B | 1 | 19 | 0 | once |
| DLI.5.910.1 | México, oct. 9 de 1886 | 114535 | C | 1 | 17 | 2 | twice (17 of 17 groups the same) |
| DLI.5.920.1 | México, oct. 13 de 1886 | 114545 | B | 1 | 19 | 4 | twice (18 of 19 groups the same) |
| DLI.5.921.1 | México, oct. 13 de 1886 | 114546 | B | 1 | 16 | 0 | once |
| DLI.5.924.1 | México, oct. 14 de 1886 | 114549 | C | 1 | 46 | 15 | twice (40 of 46 groups the same) |
| DLI.5.933.1 | México. oct. de 1886 | 114559 | C | 1 | 48 | 14 | twice (43 of 48 groups the same) |
| DLI.5.950.1 | México, oct. 26 de 1886 | 114603 | B | 1 | 12 | 4 | twice (11 of 12 groups the same) |
| all ten | | | | 12 | 360 | 40 | 186 groups twice, 174 once |

The address of each image, the time it was fetched and the SHA-256 of the file as it came are in `sources.tsv` and at the head of each transcription file. "Open": more than one reading of the group is on record.

## 3. How the numerals were copied
1. **A first reading** of all ten, on 19 Nov 2026, by an AI model (`claude-fable-5-2`) from the archive's images at full size. It was made in the session that was also studying translated sister telegrams, so it was not blind to the kind of system.
2. **A blind second reading** of six of the ten, on 19 and 20 Nov, by another AI model (`claude-opus-5-5`, as it named itself) in two separate chats. Each was given only cut images of the messages and a task sheet that asked for the digits by their shape; it was told nothing of the source or of the system. It read 186 groups: 173 with the same digits as the first reading, 13 with others.
3. **A comparison by script,** by a third session that audits the work. Its points on the copy are answered in versions 2 to 4 of the copy.
4. **The rule of the copy** (`numerals_v4.tsv`). Where the two readings give the same digits, that is the reading. Where they differ, the blind reading stands first, because it was made by shape alone, and the other is kept beside it. A reader's own second thoughts are kept too. A group with more than one reading on record is *open*: 40 of the 360 are. Nothing was chosen by eye, and nothing by what a reading might decode to.
5. **Four telegrams have one reading only** (DLI.4.771.1, DLI.5.907.1, DLI.5.909.1, DLI.5.921.1): 174 groups.

Three clerks' hands are told apart and called A, B and C here. Hand C is the least firm: on DLI.5.924.1 the two readings differ at 6 of 46 groups.

The transcription files give the message only, line by line: the words in clear as written, and each group by the reading that stands first. `~` follows a group with a small stroke above it, and `?` a group that is open. `open_groups.tsv` lists every open group with its other readings, and every place where the two readings differ on a stroke or on the mark after a group.

## 4. What the numerals show (`groups_output.txt`)
Counts only. This folder gives no value of its own for any group; section 5 names one value that is in print.
- **360 groups** among 169 words in clear: 128 of four figures, 200 of three, and 32 low numbers of one or two figures.
- **Two signs.** A small mark read `cs` stands 25 times, each time directly after a low number; it may be `es`, and the copies cannot tell. A mark read `q'` stands 52 times, in 26 pairs.
- **194 distinct groups of three or four figures;** 52 of them stand in more than one telegram.
- The three-figure groups run from 100 to 925, the four-figure groups from 1054 to 7626.

## 5. Prior work
What was looked for is a reading of any of these telegrams, or a key to their code. None was found in what was opened. That is a statement about what was opened.
- **The ledger.** `targets/reyes1886` treats another system of the same archive and leaves this one alone. Its notes say of their own system: 'Not the "clave del Sr. Presidente" (four-digit code with three-digit groups)', a description that fits the telegrams here; and of three leaves of the archive: "are in that system and were not used". The repository was read at commit `da849afb` on 20 Nov 2026: it has no folder on catalogue 1460 or on this code. Its issues and pull requests were searched through GitHub's public API on 19 Nov and again on 20 Nov 2026: 18 searches between 16:32:18 and 21:11:59 GMT, for 1460, Díaz, Diaz, Porfirio, Reyes, Presidente, CEHM, diaz1885, Carso and diaz1886, with the list of open pull requests and of everything updated since 19 Nov. The search for 1460 returns four items: the invitation thread #542, on which this entry was claimed; #806, which recorded the claim, a mark the maintainer calls "a notice against double work, not a hold"; and two in which the number is something else. Apart from those no item names catalogue 1460. The items that name Díaz or Reyes are, by their titles, on other entries of the catalogue and on other archives; their texts were searched for these words and not read through.
- **In print, read in part:** Ángel Ángel and Morales-Luna, *Revista Digital Universitaria* 9:3 (2008). Its section on Díaz was read whole by the session that is rebuilding the key, on 19 Nov; the rest of the article was not read line by line. That section prints letter tables for other correspondents of Díaz, and it says that in some of his systems "se reemplazaba cada palabra por un número", with three examples from "el sistema empleado por Díaz y Diego Redo". **One of the three, 6355, which the article gives as QUE, stands on DLI.5.909.1, line 2.** That is a published value for one of these groups, from another correspondent's code. Whether it holds in the code with Reyes is not tested here. As read here the article prints no table of such a code, and it does not name Reyes.
- **In print, searched by the auditing session and not opened by the session that copied the numerals and is rebuilding the key:** Leonardo Ríos Vázquez's master's thesis (Universidad Autónoma de Querétaro, 2023) and his article in *Estudios de Historia Moderna y Contemporánea de México* 68 (2024), both of which use the telegrams between Díaz and Reyes. The auditing session took the whole text of each and searched it for every passage on ciphers, keys and code numbers and for every citation of this correspondence in 1885 and 1886. By its account neither prints a table or a list of code numbers, and neither quotes a telegram of Díaz to Reyes on the day of a telegram here. The thesis does quote messages of Reyes to Díaz of October 1886, and for that reason it stays closed to the session that is rebuilding the key.
- **Opened by Jacob Houtrouw and the auditing session,** by his report of 19 Nov 2026: the bibliography page of Morales Luna and Ángel Ángel, "Criptografía en la presidencia de Porfirio Díaz", *Ciencia y Desarrollo*, May 2008, read by the auditing session; the same authors' slides, "Criptografía usada en la Revolución Mexicana" (Morelia, 19 September 2008); Narváez in *Historia Mexicana*, 2015, read by the auditing session from his copy; and López-Portillo y Rojas, *Elevación y caída de Porfirio Díaz* (1921), searched by the auditing session. By the report none of them prints a key between Díaz and Reyes or the clear text of a telegram of 1885 or 1886. The session that copied the numerals did not check them.
- **In print, not read by anyone here, five works:** Roberto R. Narváez, *Criptografía diplomática, política y militar en México (1813-1926)* (2019), known only by a review, which by the auditor's account names neither Reyes nor a telegram of Díaz to him; a report of 2007 by Ángel Ángel and Morales-Luna and their paper in *Cryptologia* 33:2 (2009), which by the auditor's account are behind payment and are the likeliest to print a key of Díaz's; pages 3 and 4 of the *Ciencia y Desarrollo* article of May 2008, whose site fails and of which no other copy was found online; and Galende 2000, "Sistemas criptográficos empleados en Hispanoamérica", *Revista Complutense de Historia de América* 26.
- **Not searched:** Díaz's own archive (Colección Porfirio Díaz, Universidad Iberoamericana), which may hold the clear drafts; and the Fondo Rafael Chousal, Archivo Histórico de la UNAM, whose printed inventory (Salinas 1998) is unopened. By the 2008 article Chousal, Díaz's private secretary, chose the methods, and by Jacob Houtrouw's report he issued and kept the keys.
- **Closed on purpose.** The session that is rebuilding the key keeps a list of sources that may hold the plain text of these telegrams (the archive's record of each, its neighbours on the shelf, Reyes's answers, the works above, and this repository's own sweep of the archive, the folder `research/latam_mexico`) and does not open them until its decode is time-stamped. The auditing session searched that folder for the ten shelfmarks: by its account its listing names all ten, as records of the archive's listing, and its candidates file names three; neither holds a reading or a key. Two slips are on record, both of 19 Nov 2026 and both bearing on DLI.5.950.1. The session saw once, at reduced size, a pencil draft by Reyes to the President of 23 or 25 October, which lies on the second image of a translated telegram it was using for the tables. DLI.5.950.1 may be the answer to that draft, so the session is no longer blind to a likely subject of it, nor to two names that could be spelled in it. And a search of this repository printed the beginning of the archive's line for the leaf that stands before DLI.5.950.1 on the shelf, and for one three leaves after it. Neither slip showed a cipher group or a translation. DLI.5.950.1 is out of the scored test, and a decode of it will be marked not blind. DLI.5.933.1 has a month and no day in the archive's listing: if it is of 20 to 22 October, the draft lies within three days after it too.

## 6. What was used, and who did what
- **Jacob Houtrouw** chose the target, ruled on its scope and on each rule of the work, ran the blind readers' chats, and sends this.
- **AI models, at his direction.** `claude-fable-5-2` copied the numerals and wrote the scripts and these notes. `claude-opus-5-5`, as it named itself, made the blind second readings and, in a separate auditing session, compared the readings and checked the copy. The session that wrote these notes ran on `claude-opus-5-5` from 21:07 GMT on 20 Nov 2026, by its log; on that model it made their last changes, sealed the plan of section 7 and opened the pull request.
- **Tools:** the Python script in `scripts/`; RFC 3161 time stamps from FreeTSA, DigiCert and Sectigo (`timestamps/`).
- **No person has yet checked a passage against the images without AI help.**

## 7. What is in progress
A first test of a key rebuilt from translated sister telegrams. The method is the one that the row of this catalogue proposes: "a key can be rebuilt from translated pairs". Its plan was sealed on 20 Nov 2026, before any telegram of this folder was decoded: SHA-256 `2e84dbbd3a74f764e58d79be2a717503c15d4201c38aa0acd7c81c67395ae89a`, time-stamped at 21:19:40 GMT by FreeTSA, DigiCert and Sectigo. In outline: tables are built from translated telegrams of the same months and frozen; they are tested on other translated telegrams, held back and cut above their translations by the auditing session and copied by a reader who knows no table; then the telegrams of this folder are decoded once by the frozen tables. A miss will be printed as fully as a hit. The plan, its receipts and the outcome will be added to this folder.

The catalogue entry is marked as being worked on by Jacob Houtrouw from 19 Nov to 3 Dec 2026.

## Remaining gaps
- **All 360 groups** of the ten telegrams are without a value in this folder.
- **40 groups are open,** and 174 rest on one reading.
- **The other telegrams of catalogue 1460** are not copied.
- **Two signs are not understood here:** `cs` after a low number, and `q'`.

## Escalation
1. The sealed test of the rebuilt key (section 7).
2. A second blind reading of the four telegrams read once.
3. The five works of section 5 that nobody here has read, by someone with access to them; by the auditing session's account the 2007 report and *Cryptologia* 33:2 are the likeliest to print a key.
4. Díaz's own archive, for clear drafts under the same dates, and the Fondo Rafael Chousal, through its printed inventory, for a key.
5. A person's check of a passage against the images.

## Files
- `numerals_v4.tsv`: the copy, one row a token, with both readings, every other reading and the status of each group. The three columns `p_first`, `p_other` and `p_dropped` give the reading that stands first, the first of the other readings, and a pass in which an open group has no reading. Where a note in it speaks of "the desk", that is the auditing session.
- `<telegram>_transcription.txt`, ten files: the message line by line, written from the copy by the script.
- `open_groups.tsv`: the open groups, and the strokes and marks on which the readings differ.
- `sources.tsv`: for each telegram, what the archive's listing says of it, and each image's address, time of fetching, size and SHA-256.
- `groups_output.txt`: the counts of section 4.
- `scripts/make_data_files.py`: writes the transcription files, `open_groups.tsv` and `groups_output.txt` from `numerals_v4.tsv` and `sources.tsv`.
- `timestamps/`: the time stamps on the copy and on this folder; the blind readers' answers as received, with their stamps and task sheets; and what all of that shows.
