# 443 c. 315r-v: Marcello Griffoli to Cosimo I, Siena, 1 February 1555 [1556?]

Bare cipher letter (no decipherment on or near it). Read with the key rebuilt from c. 316v / c. 317 (`key.tsv`).
Marks: `{x/y}` mechanical value x read as y; `{+a}` added letter; `[?word]` guess; `[nn]` unit not in the key;
`[?ddd]` digit group of odd length (stray digit, misread or unknown sign); `«...»` decoded from the signs but sense not
established. Everything else is the mechanical decryption, re-spaced. `scripts/check_marks.py` enforces this.
How words are counted (`scripts/reading.py`): a word whose letters come from a hole filled from context
(`{[nn]/x}`, `{[?ddd]/x}`) is a **context fill**, counted with the guesses, not as read from the signs; a marked change
of a key value (`{o/t}`) or a dropped stray group (`{[?ddd]/}`) is a **marked repair**; a word with a hole left inside
it (`sta[?3]`) is counted apart. Only unmarked words are **verbatim**.

## Marked reading (line by line, original spelling)

```marked
r01 | Del due de l'istante per comisione
r02 | di [86] scrisi al V. Ecc. che quanto più {[?34774]/pr}esto co-
r03 | metete se al Pogio Imperiale fusero
r04 | date le scale et le {o/t}rombe di fuoco et per
r05 | questa il [?858] mi comete «gle nererlichi»
r06 | «per e[71] come nestar par[?2387645]» in Montalcino non ci si sennte
r07 | novità, sì che la mia polizi{[?222]/a} al medico an-
r08 | dò bene et ne stiamo di buona vogla.
r09 | Quanto al negozio «del orladino si sofe[?74533]i»
r10 | li homini et al Milandrone è stato
r11 | promeso venia et tratenimento da
r12 | Franzesi; ha acetato et sì per que{[78]/s}to non in-
r13 | pedisca l'altro. Si è ordenato faci
r14 | prima di ritrare da loro i confiden-
r15 | ti hano in Siena, mostrado loro di po-
r16 | tere fa{[?74843]/re} tratato in Siena {[?1182543]/et si è} orde-
r17 | nato venga con testimoni loro a
r18 | riconoscere una parte di mura, che
r19 | non si raguardata, et q{[36]/u}esto causarà che
r20 | si saprà i loro in «chi[?65345][?47222]no» et si tratera
v01 | di modo che non «riesen[?477]o la» del medico.
v02 | Subito si fugì{[?72423]/} in Montalcino per paura de-
v03 | tratato. Si sc{[?722]/o}prì [?74222] in Siena, et
v04 | racolti li dieci ho{[83]/m}ini che sta[?3]
v05 | la per noi in Montalcino s{[88]/u}bito si farà
```

## Running text (Italian)

Del due de l'istante per comisione di [86] scrisi a V. Ecc. che quanto più presto commettete se al Poggio Imperiale
fusero date le scale et le trombe di fuoco; et per questa il [?858] mi commette «gle nererlichi» «per e[71] come nestar
par[...]» in Montalcino non ci si sente novità, sì che la mia polizza al medico andò bene et ne stiamo di buona voglia.
Quanto al negozio «del orladino si sofe[...]i» li homini, et al Milandrone è stato promesso venia et trattenimento da
Franzesi; ha accettato, et sì per questo non impedisca l'altro. Si è ordinato facci prima di ritrarre da loro i
confidenti [che] hanno in Siena, mostrando loro di potere fare trattato in Siena, et si è ordinato venga con testimoni
loro a riconoscere una parte di mura che non si [è] riguardata, et questo causerà che si saprà i loro in «chi[...]no»
et si tratterà di modo che non «riesen[...]o la» del medico. Subito si fuggì in Montalcino per paura del trattato. Si
scoprì [...] in Siena, et raccolti li dieci huomini che sta[nno] là per noi in Montalcino subito si farà
(the cipher ends here; the clear close follows on c. 315v: "che per questa non havendo altro ...").

## English

In `translation_c315.md`.

Notes on the reading: "Poggio Imperiale" is the Medici fortress at Poggibonsi; "le scale" and "le trombe di fuoco"
(scaling ladders, incendiary fire-trumpets) are the same items the 2 Feb letter (c. 316v/317) asks for. "Milandrone"
is read letter by letter from the signs (33 45 32 22 39 47 74 72 39 43); not identified. "il medico" recurs in the
2 Feb letter's context and in 451 c. 25r ("il ritorno del medico di Montalcino"). The «...» stretches decode to
letters but do not yet parse; they are counted as not read.
