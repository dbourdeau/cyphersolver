# 24874: reading (Italian) and translation

Image: Vlnas 2017, appendix zip P_lohy_A_a_B.zip (theses.cz/id/p3p2kb), frame 24874.jpg (original: SOA Zámrsk,
Rodinný archiv Piccolominiů, inv. 24874). The frame begins in mid-letter; 19 cipher lines,
then 4 clear lines. Key: `key_frozen.tsv` (Vlnas 2017, table 3). Status: **decoded, not read** (reading review, 6 Nov 2026: 2 of
6 cipher sentences read; the sentence check in Italian finds 1 of 8 cipher sentences clean).

Counts (`python scripts/check_marks.py`): 116 words; **76 decoded verbatim from the signs (65.5%; not a read share)**, of which 33 (28.4%)
need no s/i or g/q/u/v class choice and 29 (25.0%) contain no S, G or 5; 6 with a marked repair; 7 guessed from
context; 27 holes. Verbatim plus marked repairs: 82 (70.7%). 77 class signs are resolved by context in the read words.

## Marked reading (one unit per decrypted word; checked by `scripts/check_marks.py`)

Marks: `{a/b}` reads a where the signs give b; `{+a}` letter not given by any sign; `{-b}` sign value dropped;
`[...]` word not read; `[?word]` guess from context only. S (s or 5) and G (g, q or 9) are read as the sense needs;
that choice is counted separately and is not a repair. Words split over a line end are counted once per line.

<!-- marked -->
L01	Sono [...] [...] [...] Ecelenza havra recevuto la mia
L02	delli [?tredeci] et [...] havra [...] [...]
L03	Sua [...] [...] ha [...] [...]
L04	gran consolazione da{l/h}la di lei [?lettera]
L05	tanto piu per vedere [?la_prontezza] in [...]
L06	si esi{+b}isce di darli parte minutame
L07	nte come si [?ritrovano] la [...] [...]
L08	[...] modo et governo [...]
L09	[...] asi come dal governo poli{+t}ico
L10	desidera dunque una giusta et per
L11	[...] relatione mentre lei sa meglio
L12	queli avertimen{t/l}i [?che_siano] nece
L13	ssarii di quelo so tralascio per
L14	non tediarla [...] dunque [...] [...] le par
L15	ti{c/?}olarita che [...] [...]
L16	[...] per il governo [...] del arcid
L17	uca mio sig{-?}nore asicurandola che
L18	oltre [...] che ne cavara
L19	havra consolatione [...]
L20	[...]
<!-- /marked -->

Notes on the marks: L04 `da{l/h}la`: the sign is a looped ascender read as h, the sense needs l (dalla). L06
`esi{+b}isce`: a six stands where the sense needs b (esibisce); in this hand six and b are close and the six may be
meant as b. L09 `poli{+t}ico`: the same case; the sign is a six (both passes and the independent blind copy), the
sense needs t. L09 `dal`: the a rests on a doubtful sign (a short hooked minim without a clear dot, read r in pass 1);
it is counted as verbatim; if that sign is not 1, "dal" is a repair and the count is 75 of 116 (64.7%). L12
`avertimen{t/l}i`: the sign is a tall stroke without a cross-stroke, read l by both passes and the blind copy; this
hand's t and l differ only by the cross-stroke (as in 24876 `tu{t/l}ta`). L12 `[?che_siano]`: an ink blot covers one
sign. L15 `{c/?}`: an ink blot covers the sign. L17 `{-?}`: a stroke after g that is not a letter of the word.

## Text (Italian, spelling of the signs; accents added; holes kept)

[...] Sono [...] [...] [...] Ecelenza havrà recevuto la mia delli [?tredeci] et [...] havrà [...] [...]. Sua [...]
[...] ha [...] [...] gran consolazione dalla di lei [?lettera], tanto più per vedere [?la prontezza] in [...]. Si
esibisce di darli parte minutamente come si [?ritrovano] la [...] [...], [...] modo et governo [...] [...], a sì come
dal governo politico. Desidera dunque una giusta et per [...] relatione, mentre lei sa meglio queli avertimenti
[?che siano] necessarii. Di quelo so tralascio per non tediarla. [...] dunque [...] [...] le particolarità che [...]
[...] [...] per il governo [...] del arciduca mio signore, asicurandola che oltre [...] che ne cavarà, havrà
consolatione [...] [...].

Clear text that follows (read from the photograph, not part of the cipher count): "per le lettere che arrivano, si ha
aviso della venuta del S.r Don Michele di Salamanca, arrivando da [...] ... di [...] ... a V. E." (the last two clear
lines are faint and only partly legible on this photograph).

## English

[...] am [...] [...] [...] Your Excellency will have received my [letter] of the [?13th] and [...] will have [...]
[...]. His [...] [...] has [...] [...] great consolation from your [?letter], all the more to see [?the readiness] in
[...]. He offers to inform you in detail how the [...] stand [...], [...] manner and government [...] [...], and also
of the political government. He therefore wishes a just and [...] report, since you know better which advices are
needed. What I know I leave out so as not to weary you. [...] then [...] [...] the particulars that [...] [...] [...]
for the government [...] of the Archduke my lord, assuring you that besides [...] which he will gain from it, he
will have consolation [...] [...].

Clear text: "by the letters that arrive there is news of the coming of Señor Don Miguel de Salamanca, arriving from
[...] ..."
