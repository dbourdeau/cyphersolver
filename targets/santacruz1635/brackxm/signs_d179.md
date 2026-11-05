# D.179: transcription signs and their values (28 Oct 2026)

The transcription of D.179 (`d179_cipher.md`) was made in passes. Page 1 is pass 3 and writes the nasal as `L`
and the e-like sign as `o`. Pages 2-7 are pass 2 and use the conventions below, which the prose of `key_1635.md`
only partly states. Every value here is in the table `K` of `dec1635.py`. The same table is used for all seven
pages, and there are no per-page tables. The decode is not corrected by hand: `d179_reading.md` normalises its
output into words and marks every choice with (?), [?] or `[group]`.

| written | value | note |
|---|---|---|
| `1` | r, often the nasal n | the hundreds-digit-like stroke; in this hand it and `L` are hard to tell apart, so the decoder gives *r* and the reading picks *n* where the word needs it (*co r* = *con*, *español r le s* = *españoles*) |
| `L`, `l` | n (nasal, also m) | as in the key |
| `Z` alone | n | as in D.194 (`g Z` *en*, `43 Z no` *mando*); `Z` + vowel is *v/b* + vowel |
| `n` alone | h | *n p* = *ha*; `n` + vowel is *d* + vowel |
| `ff` | m | *i ff po r ta* = *importa*, *cu ff p li do* = *cumplido* |
| `1u` | pu | *1u di d se* = *pudiese*, *1u d s to s* = *puestos* |
| `1c`, `Lc` | no | n + o, written as one group: *y si 1c fu d se* = *y si no fuese* |
| `ch`, `Ch` | os | *e si ch ma n do* = *assí os mando* |
| `o` | e | the e-like sign (page 1, pass 3) |
| `c` | o | |
| `Le` | me | |
| `7L` | de | read as one group (page 1) |
| `Lo` | ne | |
| `19` | u | *14 L 19 55 C* = *inútil* |
| `26` | o | *26 206* = *obliga* |
| `9` | a | |
| `22` | xe | |
| `&`, `I`, `T`, `S` | null / marks | `T` and `I` are written above a group; `&` is a flourish |

Measured with `dec1635.py` on `d179_cipher.md`, the share of groups that get a value is: page 1 94%, page 3 98%,
page 4 98%, page 5 97%, page 6 97%, page 7 91%. (Page 2 sits in the same section as page 1.)
