# Telegram to Sun Yat-sen, Swatow → Tokyo, 3 April 1916 (JACAR B03050738800) — SOLVED

Cryptiana list item: "Telegram to Sun Yat-sen (1916)" (unsolved since 2021). The same entry
also lists the Huang Xing telegram (JACAR B03050731500; decoded text filed with it, scheme
unknown) — not attempted here (JACAR's archive host returns 403 to the browser tool).

## Verdict

**Solved.** The telegram is standard Chinese telegraph code (電報新編 numbering) passed
through a *systematic* code condenser of the same family as Yamada Junzaburō's two known
tables: 20 consonants in alphabetical order rotated to start at **l**, five vowel columns in
the order **e a i o u**, numbered column-major 01–99, 00 (so l‑e = 01 … k‑e = 20, l‑a = 21 …
k‑u = 00). No additive. 42 of ~44 characters read (港 restored 30 Sept 2026 from a Morse slip, M); the last
word, about two codes, is garbled in the received copy.

```
潮城由莫擎宇獨立。我軍亦光復汕頭。後莫率大隊來，令我退出鎮守府。
我軍力薄，暫由翼□支持。文慧返［港］……［last word garbled］         （田中）
```

"Chao[zhou] city has been declared independent by Mo Qingyu. Our army too has recovered
Swatow. Afterwards Mo came at the head of a large force and ordered us out of the garrison
headquarters. Our army is weak; for the present we are supported by 翼□. 文慧 returns …"

This matches the events exactly: Mo Qingyu (莫擎宇), regimental commander at Chaozhou, was
induced by Chen Jiongming, Lin Hu, He Haiming and the local revolutionaries to declare
against Yuan Shikai; he took Chaozhou city (潮城) on 27 March 1916 and wired Long Jiguang
"率師占領潮城，宣布獨立"; on 30 March the Swatow guard troops came over and Mo moved his
headquarters to Swatow — pushing Sun's own men (with whom the Japanese "Tanaka" was
serving) out of the 鎮守使署 they had seized. The telegram went to "Rosamonde Tokio" —
Soong Ching-ling's English name — i.e. to Sun's household, and was intercepted by the
Japanese Foreign Ministry, which could not read it (機密送第一號, 29 Apr 1916).

## The JACAR file (reel 1-0959, frames 0288–0298, MT 161752 1230–1247)

Read from the 11-page PDF supplied by the user (Gaimushō record 680675–680684).

| frame | content |
|---|---|
| 680675–6 | 機密送第○號, 29 Apr 1916, FM Ishii → Consul-General Segawa, Hankow: "孫逸仙ト電報往復ノ件". The Ministry has secretly obtained telegrams passing between Sun and a person at Hankow (the consulate's policeman Saitō); since mid-March they are in cipher. Who is he, why? Decode if possible. Five telegrams attached. |
| 680677–9 | The five telegrams, Tokyo → "Saito, Japanese Consulate, Hankow", 13–24 Apr 1916, four-digit groups (one five-digit) — the +111 additive code Tomokiyo has already read. |
| 680680–1 | 機密送第一號, 29 Apr 1916, Ishii → 田中事務代理 (Tanaka, acting consul, **Swatow**): "孫逸仙宛電報ニ関スル件". A telegram from a "Tanaka" at Swatow to Sun has been obtained; it is in cipher, ten letters to a word; who is this man, why does he write to Sun, is he misusing the consul's name? Investigate secretly and if possible decode. |
| 680682 | **The telegram** (received-message form). From Swatow, No. 1507, 22 words, 3/4/16 6.05 pm, received Tokio 6.05 pm. Address: **Rosamonde Tokio**. |
| 680683–4 | 政機密第二八號, 11 May 1916, Segawa (Hankow) → Ishii. Reports the *new* scheme of Sun's telegram of 10 May: regroup five-digit → four-digit, reverse digits, subtract 111, standard code (0452 → 2540 → 2429 文). Nothing on the Swatow telegram. |

The file therefore contains no Japanese solution of the Swatow telegram; the Swatow
consulate's reply to 機密送第一號 would be a separate item.

## Ciphertext (frame 680682)

Tomokiyo's transcription:

```
Twelve baxuxupeja qicijinati bemigasiqi jakebiqoye kufohemige tuxaboboba
gedoeijiga poyevayoxa leyoleveke biromapesa vorobenife xikebiqoye qekufiyaqa
tijaqixiqo xitohatula xopavajejo ropezpo ngobunibai tanaka
```

22 words = Rosamonde Tokio + Twelve + 16 ten-letter groups + ropezpo + ngobunibai + tanaka.
177 code letters; consonants exactly the 20 of Yamada's condensers (no w); vowels a e i o u.
Vowel counts i 22, e 21, a 20, o 19, **u 7**: the rarity of u pointed to a vowel-major table
with u = the 80s–90s block, which the codebook scarcely uses for page numbers.

Checking the JACAR image (cryptiana's crop, `img/sun_telegram.png`) against the
transcription: the form actually reads **gedocijiga** (not -eiji-) and **xitonatula**
(not -hat-); **kufohemige** is h/n-ambiguous and **baxuxupeja** may be baxuxepeja. All four
are exactly the emendations the decipherment requires (莫, 支, 光, 城).

## Method

1. `parse.py` — syllable statistics (above).
2. `family.py` — brute force of the systematic family: 40 consonant orders (20 rotations ×
   forward/reverse) × 120 vowel orders × {row-major, column-major} × {00-, 01-based} ×
   additive {0, ±111} = 57 600 keys. Each key decodes the clean syllable runs to 4-digit
   codes, scored by a traditional-Chinese character unigram model (jieba word list → OpenCC
   S→T; `build_lm.py`). Codebook = Unihan kTaiwanTelegraph / kMainlandTelegraph tables
   (`tw.csv`, `cn.csv`; Tomokiyo's decoded telegrams confirm the 1916 numbering is the same).
   Result: the winning key scores −360.6 against a population mean of −553.6 (sd 23.8) and
   is 49 points clear of the runner-up (`family_out.txt`, `show.py`).
3. `fix.py` / `lookup.py` — one-letter alternatives for the four doubtful codes, chosen by
   sense (光復, 支持, 莫, 潮城) and then confirmed against the handwriting.
4. `tail.py` — edit-distance search over the 13 letters after 返 (`zpongobunibai`); nothing
   within ≤3 plausible edits decodes to valid codes: at least one letter is lost in
   `ropezpo` (a 7-letter "word" is impossible in this system) and `ngobunibai` is not a CV
   string. Needs a high-resolution look at the second sheet of frame 680682.
5. `decode.py` — final annotated decoding → `decode_out.txt`.

## Confirmed cells of the table

Every syllable in a word that reads (潮, 由, 莫擎宇, 獨立, 我軍, 亦, 復, 汕頭, 後, 率大隊來,
令, 退出, 鎮守府, 力薄, 暫由, 持, 返) checks the systematic layout: 46 of the 50 distinct
syllables received are confirmed by sense; the four that are not (xu, he, ha, to) are the
four misread/uncertain ones. ku = 00 (亦 0076, 力 0500) fixes the u-column.

## Open points

* **9004 → 城 (1004)**: needs xu → xe. 潮城 is what Mo himself called the town; 潮州 (1558),
  潮梅 (2734), 潮汕 (3073) are all impossible from the letters.
* **翼□ (5065 5068)**: 5065 = 翼 is sent with two well-confirmed syllables; 5068 (xi to) is
  翿 in the modern table — 'to' could be a misread ('te' 5008 罹, 'ta' 5028 羣, 'yo' 5071 老 …).
  Probably a name or unit that "supported" the revolutionaries after Mo displaced them.
* **文慧 (2429 1979)**: read as sent; perhaps a person ("文慧 returns [to Tokyo?]"). 2429 is
  also Sun Wen's own signature character.
* **Tail** after 返: `zpo` = 港 (Morse slip, 30 Sept 2026, below); `ngobunibai` — ~2 codes, unrecoverable from this copy.
* The Huang Xing telegram (B03050731500) is kana-based; with its filed plaintext it should
  yield to the same known-plaintext approach, but JACAR must be read by hand.

## Sources

* JACAR B03050738800 (外務省記録, 各国内政関係雑纂／支那ノ部／革命党関係, 大正5年).
* S. Tomokiyo, "Chinese Cryptography: 1871–1945", cryptiana; blog 12 Dec 2021 (his attempts
  with the two Yamada tables, both negative).
* 黃浩瀚, 「百年前莫擎宇在汕宣布反袁獨立」, 汕頭特區晚報 (repr. 辛亥革命網, 6 Dec 2017) — the
  26–30 March 1916 chronology and Mo's telegram "率師占領潮城，宣布獨立".

## The tail, checked on the sheet (2026-09-15, second session)

The JACAR PDF was re-fetched (`jacar/sun.pdf`, 11 pages; raw path
`/content/item/aj12/C200139000900/raw/B03050738800.b10149.1-0959.00000288.pdf`) and frame 0296, the two sheets of the
received-message form (paper nos. 44 and 45), rendered at 600 dpi (`jacar/f0296_tail_rot.png`). The second sheet
carries two lines in a clear copperplate: **xopavajejo ropezpo / ngobunibai tanaka**. Every letter of the tail is as
Tomokiyo transcribed it; there is no h/n or e/c ambiguity to exploit here as there was in *kufonemige* and
*gedocijiga*. So the garble is the operator's, not the transcriber's: after **ro pe** (返) the thirteen letters
`zpo ngobunibai` cannot be parsed into consonant-vowel pairs at any edit distance of three or less (`tail.py`), and
the three lost characters stay lost. The "high-resolution look" this file asked for has been taken and closes
the point.

## The wider series (2026-09-18)

The Ministry of Communications' intercept files (JACAR B03050088300 … B03050090200) hold dozens more telegrams
in the same condenser family, each correspondent with its own key. See `y1916/NOTES.md` and `y1917/NOTES.md`. The Swatow
operator original is not in B03050088300 or B03050088400.

Credits (one-key review, 14 Oct 2026): `profile.json` is this telegram and its one key, so it credits only Tomokiyo's
transcription of frame 680682. Brice Dudout (the July–November 1916 systems and the corrections to our 1916
transcriptions) and wanglu2016 (issue #23, the 1917 telegrams) worked on other keys of the series; they are credited
in `y1916/NOTES.md`, `y1917/NOTES.md` and on `docs/sunintercepts.html`. The series page has no profile, so their
credits reach `contributors.html` only once the series gets one (one profile per key).

## Gaps revisited for Lasry's quotation (30 Sept 2026)

Lasry asked for fewer gaps in the quoted text (翼□, the tail). Findings:

* **Tail: `zpo` = 港 (M).** The sheet is clean copperplate (15 Sept), so the garble is in transmission, and a telegram
  garbles in Morse, not in cursive. `p` is `.--.`; `a` + `n` sent without their letter space is `.-` `-.` = `.--.`.
  So `ropezpo` = `ro pe za no` = 6604 3263 返港, "returns to Hong Kong". `morse_tail.py zpo 2` re-divides the Morse of
  `zpo` with up to two space changes: exactly four strings decode to valid codes, all at one change (港 3263,
  砉 4264, 彼 1764, 嫗 1277); only 港 makes sense after 返, and Hong Kong was the revolutionaries' base for the
  Swatow rising. Grade M. It also accounts for the seven-letter "word": `ropezano` was eight letters.
* **Tail: `ngobunibai` stays open.** The same re-division with up to four space changes gives no sensible
  decoding (`morse_tail_out.txt`); the earlier letter-edit search (`tail.py`, and a three-edit unrestricted search
  run today) gives none either. `ng` (`-. --.`) could be `y` (`-.--`) plus a dot, which would start `yo bu` = 電
  ("telegraph", as in 電示 "wire instructions", 電知), but no continuation within a few element errors reads; this is a
  possibility (I), not printed. About two characters are lost.
* **翼□ (5068) stays open.** All one-letter substitutions of `xi to` that give valid codes (翼耗, 翼群, 翼老, 翼考, 翼耀,
  翼翹, 翼江, 翼記, …) and all one-element Morse slips were listed: none is a word or a known name or unit in the
  1916 Swatow events, and no Morse re-division of `xiqoxito` other than the received one gives valid codes. The
  second character is left as □.

Files: `decode.py` (emended string ends `ropezano`, note 42), `decode_out.txt` regenerated (42 characters; the old
file's notes were one row off and are now on the right rows), `morse_tail.py` and `morse_tail_out.txt` added,
`docs/sunyatsen.html` and `docs/reveal/sunyatsen.json` updated.
