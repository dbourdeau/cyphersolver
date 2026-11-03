# Taiwan Government-General telegrams, 1901: kana substitution key (table A) reconstructed from the contemporary translations

Status: in progress (key reconstructed from contemporary translations; validated on Taipei drafts only, fails on telegrams received from Tokyo). Next step: better images of the received forms and a fixed rule for the reading order of the grids, then a new frozen protocol.

Contributed by Brice Dudout (Europe chiffrée / Wenmi), 3-4 Nov 2026. Not in the catalogue. The work was done by AI
agents (Claude Opus 5.5, Anthropic) under rules set by Brice Dudout (frozen protocol, blind transcription by a
separate agent, one measurement).

**What this folder holds: the key only.** The telegrams were read at the time: each enciphered form is filed with its
contemporary translation (譯電), and the outgoing drafts (電報案) carry the cipher kana between the lines of the clear.
This is therefore an *existing* decipherment; the contribution is the reconstructed substitution table, its method and
its measured limits. The documents belong to the National Taiwan Historical Archives (國史館臺灣文獻館); no
transcription, translation, decryption or image of them is reproduced here (see `profile.json` `outcome.texts_withheld`).

## The system

- **Kana-to-kana monoalphabetic substitution** of Japanese written in katakana, in the telegraphic spelling of the
  period (long vowels and ヂ/ジ, ヅ/ズ as in Meiji kana usage). Numerals are written in clear (kanji) inside the
  cipher.
- **Almost reciprocal (対合 type)**: 20 base pairs x<->y (イヨ ンロ ウニ クコ トテ カチ ナノ スツ ミム セタ サソ キケ
  アリ ハヘ ルマ モメ エラ ホフ ヤユ ヌネ), ヒ a fixed point, and a few non-reciprocal entries (オ->シ, シ->ヲ, ワ->レ,
  レ->ヲ). Voiced kana mostly follow their base pair (デ<->ド, ズ<->ヅ, ゴ<->グ), with exceptions (ダ->デ).
- **Built on the 五十音 grid, not on the iroha**: 11 of the 20 pairs exchange two kana of the same 五十音 row (only the
  vowel changes: クコ, トテ, ナノ, ミム, サソ, キケ, ハヘ, モメ, ホフ, ヤユ, ヌネ), against 1.7 expected for a random
  involution (20,000 draws). No sum or difference of ranks on the iroha (44-48 kana) or on the 五十音 (45-46 kana)
  repeats more than 4-6 times out of 20 pairs: the table is not a reflection, a shift or a folded alphabet.

## The key

`key_1901A.tsv`: 72 entries, cipher kana -> plain kana (45 base kana and their voiced forms), each with its number of
attestations and contradictions in the construction set and a certainty grade: 44 certain (3 or more concordant
attestations), 7 probable, 21 conjectural (1 or 0 attestations, filled by reciprocity or the voicing rule). ヲ, ヱ and
ヰ never occur as cipher kana in the drafts and are left out.

## Method

1. **Protocol frozen first.** The hypotheses (kana substitution, two-kana code, mixed), the construction set, the
   score, the control and the thresholds were written down and frozen by SHA-256 before any key was computed. The
   pieces reserved for validation (vol. 00000680, items 021 and after) were not opened by the agent that built the
   key.
2. **Construction (lot 1).** Four outgoing drafts with interlinear cipher kana: 00000680010 (pp. 2 and 22-25),
   00000680013 (pp. 7-8), 00000680019 (p. 3), 00000680020 (p. 2). The clear of each draft was put into period kana
   and aligned with its cipher kana (global Needleman-Wunsch alignment); 765 aligned positions give the table.
   Reading corrections were kept in a separate file; the frozen transcriptions were not edited.
3. **Blind transcription (lot 2).** Another agent transcribed the reserved pieces (00000680021-046) without seeing the
   key, and put the contemporary translations into kana before any decryption was looked at.
4. **One measurement.** The frozen key was applied mechanically to the whole cipher text (non-kana signs removed;
   for an alternative reading [A|B], the first). Score = share of decrypted kana equal to the aligned expected kana
   (dakuten ignored), weighted by length. **Control: 200 random keys of the same form (random involutions on the same
   kana set, seed 1901); the best of the 200 is kept.**

## Validation (measured once, 4 Nov 2026)

| Set | Pieces | Kana | Key A | Best of 200 random keys | Pieces >= control + 0.25 | Verdict |
|---|---|---|---|---|---|---|
| Decisive: telegrams received at Taipei (lot 2), key on the whole text | 32 telegrams | 5,693 | **0.233** | 0.164 | 5 of 32 | **fails** (threshold >= 0.60 and >= control + 0.30) |
| same, key applied between the arcs ︵ ︶ only (informative) | 32 | 5,693 | 0.371 | 0.302 | 3 of 32 | - |
| same, kana between the arcs only (informative) | 26 | 2,139 | 0.453 | 0.323 | 5 of 26 | - |
| Secondary: Taipei send drafts (lot 2), blind | 11 drafts | 782 | **0.721** | 0.316 | 9 of 11 | **holds** (informative, not the pre-registered criterion) |

Reading: the table is right for the telegrams **sent from Taipei** (blind drafts never seen during construction: 0.72
against 0.32, four drafts at 0.87-1.00). It is **not validated** for the telegrams **received from Tokyo**.

### Key B (failed)

A second key was built for the received telegrams (separate frozen protocol; table A re-learned on the received forms
plus a two-state clear/cipher decoder with a kana language model, since the received telegrams mix clear kana and
enciphered passages). Re-learning kept table A's value for 59 of 79 symbols: the received telegrams do not use another
table, nor the inverse of A. On a new reserve of 9 received telegrams (vol. 00000703, Oct-Nov 1901, transcribed
blind), key B **fails**: **0.206 against a control of 0.228**, 1 of 9 telegrams >= control + 0.10 (threshold >= 0.45,
>= control + 0.15). Drafts of that reserve: 0.167 against 0.222.

## Limits

- **Image resolution.** The online images are about 65-70 dpi (about 570 x 760 px per form); the cursive received
  forms are read at about 55-70 % (40-85 % on the reserve). Even a perfect key cannot score above that.
- **Clear and cipher mixed.** In the received telegrams many passages are plain kana; applying the key everywhere
  destroys them, which explains much of the decisive failure. The arcs ︵ ︶ mark enciphered passages but are not
  transcribed reliably.
- **Grid order.** Some hands write the kana in grids (columns of ten); the reading order could not be fixed
  mechanically.
- **Conjectural entries.** 21 of 72 entries rest on 1 or 0 attestations; ミ is ambiguous (ム x11, but オ x8 and ヲ x3).
- The table is a reconstruction from the 1901 drafts; the original cipher table of the Government-General (秘書課) was
  not found in the file.

## Prior work

- **The type is known and published.** Reciprocal kana tables (対合) of the Finance and Home Ministries (1875, 1876, rev.
  1880), the Justice Ministry, the police (警視局), the Army (22 tables, 1877) and the Genrōin, 1874-1882, are described
  by 長田順行 (1989), 佐々木隆 (1995) and 大野哲弥 (2009, 2012), summarised by Satoshi Tomokiyo on Cryptiana.
- **Table A itself: not found in the published tables available online.** Fifteen tables or families of tables were
  compared (both directions, base kana only). The closest is the Foreign Ministry (外務省) kana table of 9 May 1902
  (JACAR B13080285600), with **3 entries in common out of 45** (chance level); it is not reciprocal, and it was sent to
  the Taiwan Government-General only in June 1904 (JACAR B13080285400 p. 60), after these telegrams. The others (外務省
  1907 partial; 捕獲審検所 1904; Finance Minister's cipher disk 1879 and the Ōtsu tables; Army 1877; 通信局長 cipher
  disk 1901; Cabinet 1924 and 1934; state funeral 1926; Korea Government-General 1934; Sendai 1924) share 0 to 4
  entries.
- **Not verifiable online:** the ministerial tables of 1875-1896 printed only in 長田 1989 and 佐々木 1995 (tables 1-6
  and 12-14) and 大野 2012. The 五十音-ordered reciprocal table of the Home Ministry of 1876 is the most plausible
  relative. These books should be checked before any claim of novelty.
- Daniel Bourdeau's catalogue (822 entries, 3 Nov 2026) has no Taiwan entry and no kana substitution of this kind.
  Taiwan 1874 (JACAR, 処蕃始末) is already published (Tomokiyo; 大野 2009).

## References

- Satoshi Tomokiyo, Cryptiana: 「明治日本の暗号いろいろ」 <https://cryptiana.web.fc2.com/code/meijijapan.htm>; also
  meijijapan2.htm, meijiarmy.htm, meijinavy.htm, jcipherdisk.htm (consulted 3 Nov 2026).
- 長田順行 『西南の役と暗号』 朝日文庫, 1989 (pp. 130-146, 173).
- 佐々木隆 「明治前中期の政府暗号」 『メディア史研究』 3, 1995, pp. 114-130.
- 大野哲弥 「西南戦争時の政府暗号補論」 『情報化社会・メディア研究』 9, 2012, pp. 59-66; and vol. 6, 2009.
- National Diet Library, 「これが明治の暗号盤」 <https://www.ndl.go.jp/modern/column/02.html>.
- JACAR B13080285600 and B13080285400 (Foreign Ministry kana table of 1902 and its distribution).

## Sources (pieces used; National Taiwan Historical Archives, 國史館臺灣文獻館, 臺灣總督府檔案)

Vol. 00000680 (臺灣總督府公文類纂, 明治34年 永久保存追加 第20卷 官規官職) and vol. 00000703 (進退追加 第21卷).
Telegrams between Taipei and Tokyo, Sept-Nov 1901.

| Role | 典藏號 | Dates |
|---|---|---|
| Construction (send drafts with interlinear cipher) | 00000680010, 00000680013, 00000680019, 00000680020 | 8-18 Sept 1901 |
| Validation, decisive (received telegrams) and secondary (send drafts) | 00000680021, 022, 024-036, 038-044, 046 | 18 Sept - 9 Nov 1901 |
| Key B reserve (received telegrams and drafts) | 00000703007 (with its translation in 00000703008), 009, 010, 012, 013, 015, 022, 043 | 3 Oct - 11 Nov 1901 |

## Remaining gaps

- Received telegrams (Tokyo -> Taipei): no validated key. Blocker: illegible (low-resolution online images of cursive
  forms); the clear/cipher boundary and the grid order are not established.
- 21 conjectural entries of table A (rare kana and voiced forms).
- Prior art: the 1875-1896 ministerial tables in print (長田 1989, 佐々木 1995, 大野 2012) not yet compared.
