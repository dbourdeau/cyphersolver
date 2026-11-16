# Heespen, Bremen 17 April 1676, image 537 left: re-reading of 14 Nov 2026 (partial, context-assisted, NON-BLIND)

By Claude (session of 14 Nov 2026): an AI reading, not checked by a person. It does not replace the figure of record (9 of 60 word units with the frozen key v1, `readings/heespen_1676-04-17_537L.md`) and is not a count. State of the document after it: still **decoded, not read** (see "Why it stays decoded, not read").

## What was tried

1. **The held-out glossed pages as key material.** `heldout/413_transcription_glosses.tsv` and `heldout/342R_glosses.tsv` were made to test the keys and are not in them. Used now (so they are no longer held out for anything decoded here), they give: T = s ("das gantze" 400 T ...), 597 = nach ("nachsehen"), 9 = u ("unter" 9 # 690 ‡), 402 = di ("allergnädigst"), α = i ("übrigen" 711 α 477 6).
2. **The image** (Rigsarkivet API, image id 49059236, plain GET, 14 Nov 2026). The writer divides the block himself: a point between sign groups inside a word, a comma after each word. The frozen transcription has the tokens right but no word division. `transcriptions/heespen_1676-04-17_537L_worddiv.txt` adds the commas (tokens asserted equal to the frozen file). The image also shows that the small `#` before 265 on line 5 and the `#` at the head of the marginal line are one insertion mark, not the sign for n: the marginal word belongs after "402 θ".
3. **The clear text around the block** (same image; one AI reading of the German hand, doubtful words marked): before it, "... bleiben annoch bey dem vorgeschlagenen [?..], die beyde Hertzogthümer zu partiren, wie in meiner allerunderthänigsten relation vom 16ten verwichenen Monats Marty gehorsambst berichtet, und suchen vor sich die negst an Ew. Königl. Mayt. destinirten anpart gelegene und folgends an die [?..] Lüneburgische portion stoßende Stück an sich zu bringen,"; after it, "Ob und wie weit nun solches mit Ew. Königl. Mayt. allergnädigsten absehen und interesse übereinkompt ...". So the subject of the block is the party that wants the pieces next to the King's intended share and to the Lüneburg portion; the word "anpart" stands in the clear text too.
4. **Values from the context of this page**, with the writer's word division: `gloss/context_values_537L_2026-11-14.tsv` (22 values; each with the words it rests on). A value was taken only when it gives a German word inside the writer's own word boundaries, and it is used at every occurrence in the block. Seven rest also on a held-out gloss or on the key's row rule (consonant + a, e, i, o, u on consecutive numbers: 500 ho beside 497 ha, 654 ra beside 655 re, 689 ta, 624 pa, 348 bi, 593 ni). **Three contradict the gloss key**: ϙ = f (key: t), λ = e (key: r), 19 = o (key: s). Each holds at three or four words here (Hoffnung, Grafschafft, Stift; sie, die, einen, [504]en; permutation, oder, also), and each contradiction may be a difference of sign labels between the contributor's gloss pages and this page rather than a different value. That was not checked on the gloss pages' images.
5. Decode with key v2 plus these values: `decryptions/heespen_1676-04-17_537L_v2_context_NONBLIND.txt` (context values in capitals).

Not tried: reading further glossed pages of unit 262098 for the numbers still open (37, 411, 265, 504, 116, 529, 22, ‖). That is the workable next step and the blocker named below.

## Partial reading

Conventions: plain = spelled by gloss-key values and by context values that hold at every occurrence in the block; `[?word]` = rests on a value met once, or on a repair; `[529]` = a code with no value; `[unn]` = decoded, not read.

[?In] der Intention unt Hoffnung, wie [529] davor halte, das sie nachgehends von [37] [411] permutation [?die] Gravschafft [265] [unn] von den [504]en [116] die Grafschafft [?Ho[22]l] oder Diepholtz, [?oder] einen Theil davon [?erhandlen] und also [?ihren] Anpart mit dem Stift Münster [?immediate] [?combiniren] [?können].

Notes on single words.
- "[?In]": the writer has `α , # ,` (two signs, each followed by a comma), read i + n.
- "[?die]": di-a as decoded (402 θ), one word running over the line end.
- "Gravschafft" is the marginal word (g-ra-u-s-ck-ha-f-t), inserted after "die" by the mark; "Grafschafft" on line 6 is spelled g-ra-f-s-ck-ha-f-t. The key's `+` = ck is read ch, as on the held-out page 342R.
- "permutation": pe-r-mü-ta-ti-o-n (578 = mü in the key).
- "[?Ho[22]l]": ho + 22 + l as one word; Hoya would fit a county named beside Diepholz, but 22 has no value and the last sign is l in the key. Not read.
- "[?oder]": `‖` + de-r; ‖ has no value.
- "[?erhandlen]": a-r-ha-n-t-le-n as decoded (θ = a; the gloss "allergnädigst" writes ä with it).
- "[?ihren]": i-b-re-n as decoded (7 = b in the key, one gloss).
- "[?immediate]": i-m-me-di-a-te, with L = m met once.
- "[?combiniren]": co-i-bi-ni-re-n as decoded (□ = i in the key, one gloss).
- "[?können]": 543 + n-ne-n, with 543 = kö met once.
- "[529]": "wie ich davor halte" is the usual phrase; 529 = ich is a guess and is not printed.
- "[504]en [116]": 506 is glossed "Herrn" in the key's source pages; 504 is not glossed.

## English (same holes)

[?In] the intention and hope, as [529] take it, that they will afterwards [?obtain by negotiation] from [37] [411], by exchange, the county of [265] [unn], from the [504] [116] the county of [?Ho[22]l] or Diepholz, [?or] a part of it, and so [?be able] [?to join] [?their] share [?directly] with the bishopric of Münster.

The German has one verb for both objects ("erhandlen", at the end); the English moves it forward.

## Why it stays decoded, not read

The passage is one sentence. Of its 45 words, 32 are printed plain and 13 are holes or marked words: about one in four, against the bar of at most one hole in ten words, and the open codes are the nouns that carry the news (who is to give up what: 37, 411, 265, 504, 116, 22). Many of the plain words rest on context values, three of which contradict the gloss key. So this is a partial reading with a clear frame (an exchange of counties, Diepholz named, to join a share with the bishopric of Münster), not a reading.

Blockers, all workable: (1) the numbers 37, 411, 265, 504, 116, 529, 22 and the sign ‖ have no value: the glossed pages of unit 262098 not yet transcribed (336, 340, 342, 389, 391, 401, 411, 455, 481, 526 and others) are where to look; (2) the three contradictions (ϙ, λ, 19) need the sign forms compared on the images of the gloss pages 117, 118, 240, 241; (3) no second reader.
