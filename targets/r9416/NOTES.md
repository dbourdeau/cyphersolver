# A Bavarian servant to his duke, and a report on the Pressburg talks, c. 1533–34 (BayHStA KAA 4591 ff.262–263, DECODE R9416)

Status: in progress — f.263 is a working decipherment beyond recto lines 11-16; the hand re-keying of the rest (the retry step) is still to do.

Split on 15 Oct 2026 from `targets/kaa4591/` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue entry 161
grouped fourteen ciphertexts of the Munich key volume KAA 4591 in at least six systems; R9416 is a record of two leaves
in two sign sets of their own. The other letters are different ciphers, each with its own page: System A′
([`targets/kaa4591/`](../kaa4591/NOTES.md)), Łaski's cipher ([`targets/kaa4591b/`](../kaa4591b/NOTES.md)), the Fulda note
([`targets/fulda1576/`](../fulda1576/NOTES.md)), R9367 ([`targets/r9367/`](../r9367/NOTES.md)), R9424
([`targets/r9424/`](../r9424/NOTES.md)) and R9319 ([`targets/r9319/`](../r9319/NOTES.md)). Work 21 and 30 Sept 2026 (Claude
Opus 5) as part of kaa4591; `r9416/` moved here unchanged; the solver `anneal.py` stays in `targets/kaa4591/` (also used
on R9424 and R9367). The `de-1500s` language model in `lang/` was built for this leaf.

The record keeps two parts in one entry (`outcome.parts`), because the two leaves are filed as one DECODE record and
the f.263 report reads as the enclosure of the f.262 letter; each part has its own method and README row:
1. **f.263 (pp.3–4)**, the report on the Pressburg talks: key recovered from ciphertext-only, partial (primary part).
2. **f.262 (pp.1–2)**, a servant's letter to his duke: read from the existing (contemporary interlinear) decipherment.

Images: DECODE, login; not public domain, kept untracked; the page shows none.

Outcome: **key recovered from ciphertext-only (f.263), read in part**; f.262 read at the time, its gloss transcribed in part.

## R9416 pp.1–2 (f.262) — read at the time

A Bavarian servant to his duke, "eritags nach Jacobi" (Tuesday after 25 July): troops in Austria and Styria, the
Italian and Spanish foot ("walischen und spanischen knechten") to move through Styria and by the Danube into Hungary;
he asks for seven years' pension and the Oberrichter post at Straubing. The leaf is glossed over every
line by a hand of the time; the gloss is faint and is transcribed in part (`r9416/gloss.txt`, photos rotated 180°;
"..." illegible, [?] uncertain). The cipher signs of f.262 were not transcribed: the gloss is the reading.

## R9416 pp.3–4 (f.263) — broken from ciphertext only

3,150 signs, 661 words, word-separated, ~23 frequent signs; 'io' always together (treated as one sign). The
constrained annealer (`targets/kaa4591/anneal.py`, homophone caps) with the new `de-1500s` model (Deutsches Textarchiv prints
1472–1609, added to `lang/` for this target) gave running German on the first run: "…uon beden kunigen zu entlicher
handlung gen Pressburg gesetzt… der tag zu Pressburg erfolgt ist… mit grossem pomp… dem turkischen kaiser… tribut…
zu geben…". The faint interlinear gloss on the first lines of f.263 ("nunmen bag uon beden kunigen zu entlicher /
handlung gen bresburg gesetzt") agrees with the solver's text word for word, which confirms the break independently.

Working decrypt (solver key, before the look-alike split; `r9416/decrypt_f263.txt`; corrected transcription
`r9416/p34_v2.txt`): the report of a Bavarian agent on the Pressburg negotiations between "beden kunigen" (Ferdinand
and John Zápolya) and their commissaries; a Turkish embassy; "der Emrich beeche" (Imre Czibak) offering the Sultan
tribute and "tausent tucaten"; "den hern Griti abgefertigt" (Alvise Gritti, killed Sept 1534) — so c.1533–34. The
cipher (sign codes f/z/j, H/K split in v2) is a homophonic simple substitution; codes "der d", "der g", "der h" are
persons (probably Ferdinand, Gritti's party, the Hungarian king). State: read in part — running German with local
errors; a clean reading needs the v2 transcription re-keyed and the 'y' sign split.

**30 Sept 2026 — recto lines 11-16 read clean** (to fill the gaps in the quotation for Lasry's list;
`r9416/reading_p3_11-16.txt`, word by word with grades). The v2 transcription was re-keyed by hand and every word
checked on the image; lines 11-12 agree with the faint contemporary gloss, which runs further down the page than
"its first lines" (g11: "das aus den tag zu bresburg erfolgt ist dahin auch"; g12: "des Ferd tail ... mit grossem
bumbb kummen sint auch"). The split the notes asked for, on these lines: v2 `z` is two shapes, the one-bar zig-zag
(e) and a two-bar dagger (s: "daraus", "Bresburg", "ist", "grossem", "sich", "das", "Fasnacht"); `b` covers d and l.
Normalised: "... daraus der Tag zu Pressburg erfolgt ist, dahin auch des [Ferd.] Tail mit grossem Pomp kummen
sint, auch volmechtigen Gwalt anzaigt, und sich zu beden Tailn entliche Vertrage versehen. Es hat sich aber
zutragen, das am Ertag in der Fasnacht von dem turkischen Kaiser ain treffliche Botschaft ankummen ..." [Ferd.] is
the code sign g read from the gloss (faint; "Fed" possible). Three signs after "Tail" (circle with dot, I, closing
curve) are passed over by the gloss and are not rendered. Lines 17-19 read in outline "... welcher dem [T] ain
Brief vom Kaiser bracht hat, welcher in Latein transferirt ist, desselben Copei ich E. F. G. hiemit schick";
"mit vy fngioDDio" on line 17 (perhaps "mit ir Scheffe[n]") is not settled. The rest of f. 263 is not re-keyed.

Measured: `signstream.py` → `r9416/signs_f263.txt`, 3,313 transcription codes on f.263 (v2, look-alike splits and
doubtful signs included; the 3,150 above is the count before the v2 split). `mk_validation.py` aligns the hand-keyed
lines 11-16 sign by sign (225 signs, 199 read; 6.0% of f.263 read clean, a lower bound) and writes `validation.tsv`.

## Remaining gaps

- f.263 clean reading beyond recto lines 11-16 - blocker: open-codes; paused 21 Sept 2026 (workable): v2 re-keyed (Pressburg talks read throughout); one sign serves ch but the annealer gives it s ("auss"=auch) — needs a digraph value set by hand. 30 Sept 2026: recto lines 11-16 read clean by hand (`r9416/reading_p3_11-16.txt`; z split into e and a two-bar s, b into d and l); the rest still to do the same way.
- f.263 person codes "der d", "der g", "der h" - blocker: open-codes; probably Ferdinand, Gritti's party, the Hungarian king; [Ferd.] read from the gloss once
- f.262 gloss lines A09-A11 and the faint words - blocker: illegible; the contemporary gloss is faint and the signs are not transcribed

## Escalation

- [x] siblings: the volume's other ciphertexts and keys (R9423 register, System A′, System B, R9324) checked; none is the f.263 or f.262 sign set
- [x] clear-pages: the gloss on f.262 transcribed; the faint gloss over f.263's first lines agrees with the solver's text
- [x] known-keys: the volume's keys do not fit either leaf
- [x] print: web search for KAA 4591 / the Pressburg talks report found no edition
- [x] key-rebuild: constrained annealing with de-1500s (first run); v2 look-alike split; lines 11-16 re-keyed by hand
- [ ] retry: the rest of f.263 still to re-key by hand as lines 11-16 were (workable)

## Assumptions for George's review

- f.262 and f.263 are kept as two parts of one entry (one DECODE record, the report as the letter's enclosure), not
  as two entries; they are different sign sets.
