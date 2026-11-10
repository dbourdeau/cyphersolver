# taulet1866: reading of the cipher runs of N.94 (Spanish), 10 Nov 2026

Letters and telegrams received by colonel Bernardo Taulet, January 1866. AHN, DIVERSOS-COLECCIONES, 193, N.94 (PARES
5855640), views 43, 87, 78 and 26: the held-out portion H of the re-test (325 numbers, 17 runs R01-R17; see
validation.txt and retest/). Decoded with the frozen key (frozen/KEY.tsv), unchanged.

Marks: clear words of the documents are given only as context in ⟨ ⟩ (not counted). In the cipher: {x} = probable (a
number corrected by sense, or a number not in the frozen key read by sense; the justification follows each passage);
[x] = restored; ‹…› = unresolved. There are no restored and no unresolved words here.

Classes (Daniel's rule). **Certain** = every letter given by the frozen key, applied without change. **Probable** =
one or more numbers corrected by sense inside the word, or a number absent from the frozen key (12, 78) read by sense.

## Counts (cipher words)

| passage | words | certain | probable | restored | unresolved |
|---|---|---|---|---|---|
| letter from Albarca, 28 Jan 1866 (view 43, R01-R09) | 22 | 20 | 2 | 0 | 0 |
| telegram of the Minister of War (view 87, R10-R13) | 33 | 27 | 6 | 0 | 0 |
| acknowledgement (view 78, R14-R15) | 6 | 2 | 4 | 0 | 0 |
| troop figures (view 26, R16-R17) | 7 | 5 | 2 | 0 | 0 |
| **total** | **68** | **54** | **14** | **0** | **0** |

Read share: certain only 54/68 = **0.794**; certain + probable 68/68 = 1.000. N.94 stays "read in part" with the
whole target because the key fell short of our validation rule again (margin 0.261 < 0.30).

The fourteen probable words: orde{n}, con{o}cimiento (view 43); {y}, {q}ue, j{u}zgue, le{y}es, igualmen{t}e, {y}
(view 87); reci{b}ido, {v}einte, o{c}ho, cu{m}plimentará (view 78); {y}, {y} (view 26).

Two counting slips of retest/clair.txt are corrected here (the totals 54/14 were right): orde{n} is probable but was
not braced there, and the number 12 occurs 5 times, not 4.

## Letter from Albarca (view 43, 28 Jan 1866): R01-R09

⟨…⟩ enterado i se ⟨cumplimentará⟩ su superior orde{n}, ⟨quedando en⟩ dar a ⟨V.S.⟩ con{o}cimiento del ⟨inmediato⟩
resultado. Es cuanto ⟨debo decir a V.S.⟩ en contestación a su oficio ⟨de este día⟩ recibido ⟨a las 9⟩ de la noche.

- "enterado i se": the cipher has 92 (= i) for the conjunction y, a common spelling of the time; counted certain.
- orde{n} (R02): the last number is 27 (= r), "order", where 29 (= n) is required.
- con{o}cimiento (R04): 61 (= d), "condcimiento", where 64 (= o) is required.
- The signer is read as Rafael Ramis (uncertain); not used for the key or the measurement.

## Telegram of the Minister of War, forwarded by the Captain General (view 87): R10-R13

⟨…⟩ no se haga ninguna concesión a Escoda {y} {q}ue se j{u}zgue con arreglo a las le{y}es si fuera aprendido.
⟨Los prisioneros⟩ serán igualmen{t}e ⟨juzgados⟩. Procure ⟨V.E. … que a toda costa⟩ sean aprendidos no solo Escoda {y}
Sagueta sino los demás dispersos.

- {y}, le{y}es (R10), {y} (R13): number 12, absent from the frozen key; y by sense (see key_derived_n94.tsv).
- {q}ue (R10): 19 (= g), "gue"; the frozen key has no q, and "Escoda y que se juzgue" is imposed by the sense.
- j{u}zgue (R10): number 78, absent from the frozen key, u by sense; the z is written with 10 (= s), kept as written.
- igualmen{t}e (R11): 38 (= m), "igualmenme", where 88 (= t) is required.
- "aprendido(s)" = aprehendido(s), arrested: spelling of the original, counted certain.
- The clear words between R12 and R13 are partly doubtful in the image ("V. E. ? que a toda costa"); see validation.txt.
- Escoda and Sagueta (the "Saguete/Sagueta" of the N.99 reports) are rebels of the January 1866 rising; not identified
  further here.

## Acknowledgement (view 78): R14-R15

⟨…⟩ reci{b}ido el {v}einte ⟨y⟩ o{c}ho, se cu{m}plimentará ⟨…⟩

- reci{b}ido (R14): 61 (= d), "recidido", where 14 (= b) is required.
- {v}einte (R14): 55 (= u), "ueinte", for v (u/v).
- o{c}ho (R15): "oho", the c is missing.
- cu{m}plimentará (R15): "cunplimenstara", 29 (= n) for m and an extra s; that s is our doubtful reading 10? of a
  mark at the start of a line of the image (see validation.txt).

## Troop figures (view 26): R16-R17

⟨y siendo esta la de⟩ doscientos cuarenta {y} dos ⟨incluzos los Tambores, solo podrá componerse cada una de estas
tres columnas de⟩ ochenta {y} uno.

- {y} (R16, R17): number 12, y by sense.
- The figures agree with each other: 242 men, including the drummers, make three columns of about 81 (3 x 81 = 243).
  Internal consistency only, not a validation.
