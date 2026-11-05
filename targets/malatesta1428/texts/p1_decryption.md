# Pandolfo Malatesta to Gianfrancesco Gonzaga, Rome, 22 April 1428 (ASMn, Archivio Gonzaga; DECODE R1854 image 1): decipherment

Transcription of the cipher: Satoshi Tomokiyo (DECODE1854_transcription.txt), corrected on the image by Mark Vladimir
Prizmic. Key and reading: Prizmic, with Claude, preprint doi 10.5281/zenodo.23969170 (5 Nov 2026), CC BY 4.0. Checked here
(5 Nov 2026): `key.json` applied to `transcription_tomokiyo_corrected.txt` by `dec.py` gives exactly the cipher text below.
The clear Latin around the runs is from `../p1_clear.md` (this project's transcription of the clear parts, with its
own expansions and doubts). Cipher in **bold**; spelling follows the cipher (north-Italian x, single l, i for j);
parentheses mark letters the scribe left out; `[·]` is the one unread sign (23), before "delliberet".

## The letter with the three runs in place

Magnifice et potens domine et honorandissime frater carissime. Huc nuperrime novum delatum est, pacem inter illustre
ducale dominium et dominum ducem assi(?)... esse conclusam, licet nondum publicatam. Ex quo iam nonnulla pro nobis
concepi et excogitavi valde utilia, quibus poterit amplitudo Vestra statum et nostrum suum non modicum pangere(?). Qua de
re ipsam premissa rogare ac simul decrevi ne **de suis gentibus armigeris cas(s)andis vel quid aliud peragendum [·]
delliberet** donec sciam; alioquin non possim, quod deo auspice infra viginti dies futurum spero si novum ipsum pacis
sensu(?) verificari. Nam sibi tue prepositum(?) me sciat quo modo valeat **absque dis(c)rimine et multo dispendio
provincie Moree, patrie siquidem fertilis et amene, rex efici**; precor itaque prefatam amplitudinem Vestram, cum se
fratrem(?) paratam quoque reperiat posse sibi et natis amplitudinem tantam vendicare, nolit rem ipsam negligere. **De eo
autem regno magnificum c(o)mitem Riciardum bene informatum puto, quoniam ad illud cum serenissima sorore nostra domina
vaxilissa tetendit, et iterum deinde etiam sui ocaxione redivit.** Recommendo me prefate amplitudini Vestre, quam cum
magnifica consorte sua honoranda sorore atque natis (?)dissere(?) valere ex (?)animo(?).

Pandulfus de Malatestis Archiepiscopus Patracensis etc. Rome xxii Aprilis 1428.

## The cipher text only, decoded sign by sign (output of `dec.py`, u and v both v)

```
RUN 1  66 signs
desvisgentibvsarmigeriscasandisvelqvidalivdperagendvm?delliberet
RUN 2  82 signs
absqvedisrimineetmvltodispendioprovinciemoreepatriesiqvidemfertilisetamenerexefici
RUN 3  160 signs
deeoavtemregnomagnificvmcmitemriciardvmbeneinformatvmpvtoqvoniamadillvdcvmserenissimasororenostradominavaxilissatetenditetitervmdeindeetiamsviocaxioneredivit
308 signs, 33 distinct, 5 nulls, 1 unread
```

Word division, with the readings read for sense (c(o)mitem: the scribe wrote an abbreviated c, and "disrimine" omits
the c of "discrimine"):

- Run 1: de suis gentibus armigeris cassandis vel quid aliud peragendum [·] delliberet
- Run 2: absque discrimine et multo dispendio provincie Moree, patrie siquidem fertilis et amene, rex effici
- Run 3: de eo autem regno magnificum comitem Riciardum bene informatum puto, quoniam ad illud cum serenissima sorore nostra
  domina vaxilissa tetendit, et iterum deinde etiam sui ocaxione redivit

Sign values (Tomokiyo's labels): a 12 44 22 · b x · c 48 · d cc · e 9 ss 42 · f 30 · g 20 · i 26 b3 46 · l 8 · m ss2 ·
n 40 · o V 45 50 · p 52 · q 28 · r H 21 · s 32 · t I · u/v 10 24 33 · x 49 · nulls v, g · unread 23. The full table
is `../key.json`.
