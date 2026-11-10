# Japanese Army numeric kana cipher, 1902–04 (JACAR, NIDS holdings)

**23 Oct 2026, re-read (REREAD_BRIEF, b24): C03020059400 read.** The JACAR item (23 frames, fetched as one PDF through
the viewer's `raw/` path) has the **filed translation** of the telegram on frame 0118: 「辛碇泊場司令部ニ要スル下士以下及器具材料ハ
門司補給廠支廠長ニ交付済。[…]ノ結了ハ支廠長ヨリ直接報告ノ筈」 (大臣宛 井上師団長). The 12 cipher pairs are the unit name
(Anchorage Command Shin), re-read on frame 0119: pair 5 ends in a glyph unlike the 九 above it (九 or a cursive 四), pair
7 is written 八八 where ジ needs 六八. Reading `texts/C03020059400_reading.md`, English `_en.md`; fraction_read 0.836
(61 of 73 pairs). Helper: `research/reading_audit/reread_b24_army.py`.

**22 Oct 2026, reading audit** (George Lasry's test): C09122911500 and C09123116600 read as sentences. C09122909900 is a twelve-kana noun phrase ("observation of the naval exercise"), *not prose*; C03020059400 is a twelve-kana phrase with two signs off the table whose sense (an anchorage command) is a guess: *decoded, not read*. Claim read -> read in part, 49 of 73 pairs in telegrams that read.

Contributed by Harumi-Matsuba (GitHub issue #58, 20 Oct 2026; repository
https://github.com/Harumi-Matsuba/kagigo1901-public, code MIT, documents and data CC BY 4.0). Checked here 21 Oct 2026.
Page: `docs/army1902.html`. Outside the LLM paper's scope (Japanese, not a European classical cipher); contributed.

## The cipher

Domestic telegrams of the Imperial Japanese Army in which two digits stand for one kana. A coordinate table:

| first digit | second digit (consonant column, reverse gojūon) |
|---|---|
| vowel row a 0, i 1, u 2, e 3, o 4; +5 for a voiced kana | a 9, ka 8, sa 7, ta 6, na 5, ha 4, ma 3, ya 2, ra 1, wa 0; voiced ga 9, za 8, da 7, ba 6 |

ン = 10; a final 80 is taken as an end mark (conjecture). カ = 08, シ = 17, ガ = 59, ブ = 76. The same table appears from
March 1902 (Osaka) to January 1904 (Kokura, Moji). Whether it is the Army's 鑰号 (Yakugō, 1900–04) used without its key,
or the numeric part of 特号 (Tokugō), is not settled (contributor's METHOD §6); not claimed here either.

## The telegrams (one table, four telegrams)

| JACAR | frame | date, route | pairs | reading | against |
|---|---|---|---|---|---|
| C09122911500 | 0110 (translation 0108) | 27 Mar 1902, Osaka: Chief of Staff Ōyama → Lt-Gen. Terauchi | 35 + 80 | ホンシヨクキキヨウマデホンブノジムハキクワンヨロシクトリハカラハレタシ (本職帰京迄本部ノ事務ハ貴官宜シク取計ハレタシ) | 35/35 |
| C09123116600 | 0026 (reply draft 0025) | 25 Jan 1904, Kokura → Maj.-Gen. Iguchi, General Staff | 13 | ヨヨウノカンコクチズダイヨ + clear サレタシ ヲハラ (要用ノ韓国地図貸与サレタシ) | no translation; reply draft sends maps of Korea |
| C09122909900 | 0079 (translation 0078) | 28 Mar 1902, Osaka: Ōyama → Maj.-Gen. Fukushima | 12 | カシグンエンシウケンガク (カイグン…, naval exercise observation) | 11/12: イ written 17 (シ), table 19 |
| C03020059400 | 0119 | Jan 1904, Div. commander Inoue → War Minister | 12 | シンテイハクゼウシレイブ (辛碇泊場司令部) | 12/12: pair 5 04 (ハ) per Tomokiyo 24 Oct 2026; ゼウ = 場 (issue #97) |

Not included: C09122806100 (18 Feb 1901, Hiroshima, Manabe → Tamura), 15 pairs in four runs that the 1902 table does
not read (the same ニ is 91 and 69). A different method, so by the one-key rule it is not part of this target; the
contributor's OPEN.md lists what was tried. Unread with this table. **10 Nov 2026:** decoded in part with the 1901
serial table (issue #371): テンシヨク, ンチワ, フクム, with 91 and 69 off that table; see `targets/army1901in/`.

## How the table was found (contributor)

From C09122909900's 12 pairs and the furigana of its outgoing draft C09122909800 (カイグン, エンシウ): ン = 10 three
times, the first digit mod 5 follows the vowel, ≥ 5 only for voiced kana, ア 9 カ 8 サ 7, so reverse gojūon columns.
Then C09122911500 (found afterwards) agreed on all 35 pairs; only the ba column (6) was fixed from its ブ = 76.
So the 35/35 is not wholly independent of the table: the table's shape was completed with it in view, though
only one column value came from it. **C09123116600 is the real test**: 13 pairs, found by searching the catalogue
for digit runs, no translation, and it reads as a request that fits the reply draft in the same file. Two spellings in
it are irregular (ヨヨウ for ヨウヨウ 要用, ダイヨ for タイヨ 貸与); the contributor takes them as the sender's.

Method category: key recovered based on adjacent plaintext (the outgoing draft's furigana and the filed
translations beside the cipher). Provenance contributed. AI-only work (Claude Opus 5.5 transcription and table;
Codex and Claude Sonnet blind second transcriptions, lowest agreements 97.2%, 100%, 84.6%, 87.5%); no human check.

## Checks made here (21 Oct 2026)

- `decode.py` written from the stated table only. All four telegrams decode as the contributor says (`decode_out.txt`):
  35/35, 11/12, 10/12, and ヨヨウノカンコクチズダイヨ.
- Permutation control (`python decode.py control`, seed 1902, row and column digits shuffled, 1,000 tables):
  C09122911500 max 16 against 35; C09122909900 max 6 against 11; C03020059400 max 6 against 10; none reaches the
  real score (`control_out.txt`). Matches the contributor's figures (max 16 for 0110).
- JACAR images fetched (C09122911500, C09123116600, C09122909900 PDFs). Every digit of frame 0110 and frame 0026 read
  here against the transcription, column by column (columns right to left, top to bottom): all agree. One glyph,
  column 3 row 10 of frame 0110, looks like 九 but is read 五 (45 = ノ in ホンブノ), as the contributor has it.
- **Discrepancy in the contributor's repository**: `data/transcription.txt` and `data/telegrams.tsv` give
  C09122911500 with 34 pairs (column 2 = 一八四二…, reading ホンシヨクキヨウ…, "34/34"), while README and READING.md
  give 35 pairs (一八一八四二…, キキヨウ = 帰京, 35/35). The image shows 一八一八 at the head of column 2, and 35 pairs + 80
  = 72 digits matches the form's count of 72 characters. READING.md is right; the two data files are stale (the
  JACAR catalogue's own transcription drops the 18, per READING.md). `ct_C09122911500.txt` here has 35 pairs.
- C09122909900 was not re-read here; C03020059400 re-read 23 Oct 2026 (b24).

## Verification 4, 23 Oct 2026

C09122911500 and C09123116600 pointed at `texts/readings.md`, the shared table of unspaced kana decodes, which the v4
sweep cannot score (Japanese, no word list). Each now has its own `texts/<id>_reading.md` and `_en.md`: the kana divided
into words with the kanji text under them (C09122911500 from its filed translation, frame 0108, 35/35 pairs;
C09123116600 with the sender's spellings ヨヨウ, ダイヨ kept). Judged as a reader: each is one complete, coherent
sentence with no hole. Both keep read, grade B. C03020059400 (its reading already written, 22-23 Oct) judged the same way: two sentences from the filed translation, one hole of three characters; keeps read.

## 25 Oct 2026: issue #97 (Harumi-Matsuba)

- C03020059400: pair 5 is 04 (ハ), as Tomokiyo reads the image (cryptiana meijiarmy2.htm, 24 Oct 2026); with ゼウ taken
  as a spelling of 場 the run is シンテイハクゼウシレイブ, 12/12 against the translation (11/12 with 09). The contributor keeps
  it a partial reading because the lowest independent second transcription agrees 87.5%.
- C09122911500: the contributor's digit list now has 35 pairs + 80 = 72 digits, the form we had already checked on the
  image (21 Oct 2026); `ct_C09122911500.txt` unchanged.
- C09122909900: Tomokiyo reads the 2nd pair 14 (ヒ, カヒグン) where every AI reading has 17; not イ (19) either way, so
  11/12 stands; recorded, transcription unchanged.

## Remaining gaps
- C09122909900 pair 2 (17 for イ) - blocker: needs-physical-access; the image shows 七, writer's or transmission error; binarised JBIG2 scan cannot settle the head of column 2 either
- C03020059400 three cramped characters of the translation (frame 0118) - blocker: illegible; re-read on the JACAR scan 23 Oct 2026. Pairs 5 and 7 settled 25 Oct 2026: pair 5 = 04 (ハ) on Tomokiyo's reading of the image, pair 7 八八 (ゼ) read as ゼウ = 場 (Harumi-Matsuba, issue #97); 12/12 against the translation

Closed (taken out of the open list, 23 Oct 2026): b24, 23 Oct 2026: C03020059400 decoded, not read (read with its filed translation, frame 0118)

## Escalation
- [x] siblings: the contributor viewed about 420 items (1,088 frames) of the 1901-02 telegram files and 235 items of the 1904 Daijiki; C09123116600 found by a catalogue search for digit runs
- [x] clear-pages: the filed translations (fr. 0108, 0078, the Daijiki text) and the outgoing draft C09122909800 used as cribs
- [x] known-keys: Cryptiana's 1874 and 1894 Army coordinate ciphers (iroha order) do not fit; the 1902 table does not read C09122806100
- [x] print: contributor's prior-work check (PRIOR_CHECK.md, 20 Oct 2026) found no earlier reading
- [x] key-rebuild: table complete for the observed values; unobserved cells inferred from the rule
- [x] retry: the discordant digits judged blind by Codex and Sonnet (4 runs); none overturned the first reading

## Files

- `ct_<JACAR>.txt`: the digit pairs per telegram (from READING.md; 0110 and 0026 checked on the images)
- `decode.py`, `decode_out.txt`, `control_out.txt`
- Images are not committed (JACAR PDFs fetched into the scratchpad); crops for the site: `docs/army1902_f0110.jpg`, `docs/army1902_f0026.jpg`
