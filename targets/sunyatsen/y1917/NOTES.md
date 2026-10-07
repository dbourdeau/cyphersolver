# Sun Yat-sen ↔ Dai Jitao, Shanghai–Tokyo, March 1917 (JACAR B03050090200) — SOLVED

JACAR **B03050090200** = 各国内政関係雑纂／支那ノ部／革命党関係（亡命者ヲ含ム）／特定人ノ発受郵便物取調 第四巻,
item ５ (大正6年3月29日–9月21日), Gaimushō 1.6.1.4-2-1-2_004, reel 1-0583, frames 0503–0513 (11 images).
Raw PDF: `/content/item/aj12/C200138753500/raw/B03050090200.b10083.1-0583.00000503.pdf` under
www.jacar.archives.go.jp (the path is in the `/das/image/<refcode>` page). Saved as `../jacar/B03050090200.pdf`
(git-ignored); the three telegram crops are `../jacar/f0504_*.png`, `f0506_*.png`, `f0507_*.png`.

Each telegram comes with a covering note, 秘第…號, Director of the Communications Bureau (逓信省通信局長) → Director of
the Political Affairs Bureau, Foreign Ministry: 特定人發着郵便物等取調ノ件 別紙寫送付. There is no decode anywhere in the file.

| frame | telegram |
|---|---|
| 0504 | Shanghai → Tokyo, no. 0113, 31 words, 23/3/1917 18.19, recd 2.10 am. To **Toi c/o Kikuchi Rioichi, 275 Shiragawa? Sankōchō, Tokio**. 22 code words, signed **Sunwen** in clear |
| 0506 | Tokyo → Shanghai, 26/3/1917, 15 words. To **Sun yatsen Shanghai**. 12 code words, signed **Tenkiutai** (天仇 = Dai Jitao, Tai Tien-chou) |
| 0507 | Shanghai → Tokyo, 25/3/1917, 11 words. To Toi c/o Kikuchi. 7 code words, signed Sunwen |
| 0509 | Shanghai → Tokyo, 24/6/1917. To Taitenkiu c/o Toyama? — **different system**, not read (see below) |
| 0511 | Tokyo → Shanghai, 29/6/1917, two sheets, to Sunyatsen, signed Tai — **different system**, not read |
| 0508, 0513 | kana telegrams (Dai → Shanghai; 9 Sept 1917 Shanghai → Tokyo), in clear Japanese |

"Toi" is therefore Dai Jitao (戴季陶, 天仇), staying c/o Kikuchi Ryōichi (菊池良一) in Tokyo; the March telegrams are Sun
and Dai corresponding four months before the Constitutional Protection movement.

## Key

Same *family* as the Swatow telegram of April 1916 (`../NOTES.md`): 20 consonants (no w) × 5 vowels, numbered
vowel-major, 01…99, 00; each pair of syllables = one standard Chinese telegraph code; syllables run on across the
ten-letter words with no regard to word boundaries. **Different key**: consonants rotated to start at **k** (Swatow: l),
vowel columns **a e u o i** (Swatow: e a i o u). No additive.

```
     a   e   u   o   i
k    01 21 41 61 81
l    02 22 42 62 82
m    03 23 43 63 83
 …   (row n+1 = row n + 1)
j    20 40 60 80 00
```

`fam17.py` runs the whole 57 600-key family on the 23 March telegram. This key scores −321.6 against a population
mean −556.4, sd 25.8 (9 sd); the next unrelated key is 124 points behind. The 25 and 26 March telegrams, which played no
part in finding the key, read in it at once — the strongest confirmation. The Swatow key itself gives nonsense.

## Plaintexts

Conventions: □ = unread; *emendations* are single letters, all of kinds this copying clerk demonstrably makes
(g↔q, k↔h, e↔c, a dropped letter), each justified by sense *and* by a clean reading of a second occurrence.

### 23 March 1917, Sun → Dai (frame 0504)

Read from the sheet (the JACAR metadata transcription has ~15 letters wrong):

```
Naroxoziji Kojipanejo facorabixa pixaqaqe eianakerele befacoyohi tebovocega Kalamanaro rugoqasuxe
bixaziqaso yusoxozipa bujihoceno poqiqaforu qocaxoqasu xebiqabiqo mujuvamako qabokezaka cagexuxala
banegerapo qixapfete  Sunwen
```

> 前電云三日後商妥□□□□□後音。此間必俟前約取消，始可致電北京照辦。各約已取消否？速覆。公司抄件瑞士尚未辦妥。文

"My previous telegram said that after three days [the matter] would be settled by agreement … [further] word. Here we
must wait until the former contract is cancelled before we can wire Peking to act accordingly. Have the contracts all
been cancelled? Reply at once. The company copy … [瑞士?] not yet settled. — Wen."

* 約 (twice): the first is written *rugo* (4778 紞), the second *ruqo* (4766 約); g/q.
* 尚**未**: *gera* 現 → *qera* 未; g/q.
* 瑞士: *gexu* 瑣 → *gemu* 瑞 (3843); an x/m misreading. "Switzerland" makes little obvious sense here, so this pair is
  the least certain of the emendations (the unemended 瑣士 means nothing either).
* 辦妥。文: the last word, *qixapfete*, has nine letters and must have ten; *qixa pi ne te* gives 辦妥 + **文** (2429),
  Sun's own signature character, which also closes the 25 March telegram (*juvanete*).
* **Lacuna**: words 4–5 as copied, *pixaqaqe eianakerele*, have 8 + 11 = 19 letters where 20 are required (the clerk
  misplaced the word division and lost or misread at least two letters: *ei* is not a CV pair). *pi* completes 妥; the
  following five codes are not recoverable with confidence. `mid.py`/`mid2.py` search one insertion plus up to two
  plausible substitutions; nothing clean emerges (best: 壺杭城抬接, i.e. "…Hangzhou city…", three edits — not adopted).
  The last of them, *lebe* = 接, reads as written, so "…接後音" ("received further word") is likely.

### 25 March 1917, Sun → Dai (frame 0507)

```
Nasegapiru qoqasuxebi facohekicu nokaverabo zuboqabiqa suxebiqaza juvanete  Sunwen
```

> 函悉。約取消後，當□□□能否。取消卽覆。文

"Letter received. After the contract is cancelled, [whether] … is possible. Reply as soon as it is cancelled. — Wen."

* 能: *zubo* 茆 → *xubo* 能 (one letter; 能否 is the set phrase).
* *kicu noka verabo* (三 codes 當□□□) do not read; `variants.py` finds no one-letter solution that makes sense.

### 26 March 1917, Dai → Sun (frame 0506)

```
getazazuji yineyomoni cemixetibi javesokaxo jikofanopu mizoyamaku xakizazuru qajipanejo
tayelaxama kozabojifu xayokatuxo zimucuzaku  Tenkiutai
```

> 本定今日赴熱海。□□來云：彼等須先□定，約三日回。□公司事如何？電示。宥

"I was to have gone to Atami today. □□ came and said that they must first settle □; [I shall be] back in about three
days. How stands the company matter? Wire me. — the 26th."

* 本: *geta* → *qeta*; 今: *jiyi* (仇) → *jizi*; 日: *neyo* → *nejo* (日 is read cleanly elsewhere in the same key).
* 公**司**: *zabo* → *qabo* (司 read cleanly as *qabo* in the 23 March telegram); 約 (about): *ruqa* → *ruqo*.
* **宥**: the last code, *zaku* (宅), is *zahu* = 1359 宥, the rhyme-code (韻目代日) for the **26th** — the telegram's date.
* □□ before 來云: *bija veso* (□江). 小池 (Koike Chōzō, who had left the Foreign Ministry's Political Bureau for Kuhara
  in 1916) is two edits away (*baja veto*) and is only a guess.

### Taken together

In the last week of March 1917 Sun, in Shanghai, is waiting on the cancellation of "the former contract" / "the
contracts" before he can wire Peking; he presses Dai in Tokyo for word, and Dai reports that "they" must first settle
something, and asks after "the company matter". The texts do not name the contracts or the company. Identifying them
needs the Chinese-side record (孫中山全集 / 年譜長編 for March 1917) — not found online in this session.

### Wang Lu's proposals (issue 23, 5 Oct 2026), checked here 7 Oct

Wang Lu (wanglu2016) proposed the following. The code arithmetic below was re-run here with `show17.T` + `family.code2ch`; every value matches.

* **公司 / 前約 / 各約 = the Shanghai exchange project** (hypothesis, not proved). Dai signed an agreement on 5 Dec 1916 with
  中島行一 for 三上豊夷: Japanese half-capital, 80% of profits, Japanese advisers. The Jan 1917 petition to Peking omitted the
  Japanese side, and Chinese exchange law barred foreign shareholders and staff (Yang Tianshi; Bryna Goodman, "Questions of
  Colonialism, Nationalism, and the Early Shanghai Stockmarket", *Provincial China* 1.1, 2009, doi:10.5130/pc.v1i1.986).
  That would explain "the former contract must first be cancelled before we can wire Peking". No record of the cancellation in
  late March 1917 has been found. Lead: Aichi University, Tōa Dōbun Shoin Memorial Center, Sun Wen–Yamada Junzaburō papers,
  item 「上海交易所案」（秘）(catalogue entry not seen).
* *bija* = 9420, not in either telegraph-code field. *baja* = 1420 小 is one of 32 valid one-letter variants, so it is
  contextual, not mechanical. *veso* = 3068 江 reads cleanly, so **小江** costs one edit; 小池 (*veto* 3069) costs two.
  **中島** would be *jile bafi* (0022 1497), which differs in 7 of 8 letters: ruled out.
* *xaki* = 1181 妙. One-letter candidates are *xapi* 1185 **妥** (妥定; 妥 occurs cleanly in the 23 March telegram) and
  *qaki* 0681 同.
* What would settle it: the frame 0506 letterforms (*i/a* in *bija*, *s/t* in *veso*, *k/p* in *xaki*), and any Gaimushō
  surveillance report on Dai's movements on 26 March 1917.

## June 1917 telegrams: a different system

Frames 0509 (24 June, Sunwen → "Taitenkiu", 8 words) and 0511 (29 June, Tai → Sun, two sheets, ~30 words) use *y* as
a sixth vowel (*lidajysamy*, *cymefymeca*) and contain non-CV clusters (*myzoasdoke*, *jomoaxfojy*, *liriopen*). They
do not read in the March key, and are not strictly consonant–vowel. Transcriptions (my reading) are kept here for a
later attempt:

```
0509: Lidajysamy vemucayri mevecafema(u) pokelutazi riyecafafi cymefymeca madamymiri pujihokehe  Sunwen
0511: Mukoacyobe myzoasdoke catejidoke yokigeleyi liriopen duricidule kohokycuee kuxomifumu hutadyny(y)go
      capakazuye mycykafevu damoumhosy cydicapayo benyzoac hinucuge rifyjabo(?) mahykagica fegajiriby
      jomoaxfojy micycoteco fuhodijige cafemigymu pokycekige rudubyrijo jorinimafy fojylisiby mikypomice
      miyaminoma fykazokipa  Tai
```

## Files

* `fam17.py` — family brute force on the 23 March telegram (prints the Swatow-key failure first).
* `show17.py` — the key (`T`, `INV`) and a syllable-level decoder.
* `body.py` — decode a letter string at both syllable alignments.
* `variants.py` — one-letter variants of any code group, ranked by bigram fit with its neighbours.
* `mid.py`, `mid2.py` — searches over the damaged span of 23 March.
