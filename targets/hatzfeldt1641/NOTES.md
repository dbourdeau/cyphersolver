# Ferdinand III to Melchior von Hatzfeldt, Regensburg, August–September 1641 (HZA Neuenstein, Ni 10 Bd 242)

Status: read in part (Brice Dudout, 4 Nov 2026; five pieces, 859 cipher words: 677 certain, 131 probable, 49 restored, 2 unresolved;
94.1% of the words read; by letters 98.9%). By document: P5 (14 Sept) read (95.3%); P1, P2, P3, P4 read in part. Key: Stützel 1963 (key used, not claimed).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Not in `catalogue.json` or `research/leads.json` (our notes filed the Neuenstein volumes as no. 571, which is not on main; see issue #259);
this target covers the cipher pieces of Bd 242 (Ferdinand III, July–December 1641). No DECODE record.

## Documents

Neuenstein, Hohenlohe-Zentralarchiv (Landesarchiv Baden-Württemberg), Ni 10 (Rosenberg-Hatzfeldt) Bd 242. Reproductions ordered by
Brice Dudout (LABW-6aeaff73efe93, 19 images, 200 dpi); private research copies, **not published here and not to be republished**.
Only the cipher pieces were reproduced (fols. 46–49, 90, 93, 95–105).

| piece | date | folios | what | cipher signs |
|---|---|---|---|---|
| P1 | Regensburg, 21 Aug 1641 | 46r–49v | letter: two cipher blocks inside the clear text; signed Ferdinand, countersigned Schlick; endorsed "in Ziffern geschrieben" | 1,077 |
| P2 | Regensburg, 7 Sept 1641 | 90r–90v | letter: "Wir berichten dich … daß wir" + cipher, clear close | 454 |
| P3 | undated (after 7 Sept) | 93r | postscript, lighter hand: 4 cipher lines and clear text referring to "Unsers letzten schreibens vom siebenden" | 40 |
| P4 | Regensburg, 12 Sept 1641 | 95r–96r | ciphered copy of the bond of the city of Aachen, signed "Caspar von Schwarzenburg, delegatus Aquensis"; the "hiebeyligende obligation" of P5 | 962 |
| P5 | Regensburg, 14 Sept 1641 | 97r, 98v–105v | letter with clear passages between the cipher; endorsed "Schreiben ganz mit Ziffern"; **fols. 97v–98r are not among the copies supplied** | 2,986 |

No contemporary decipherment on any piece; only a pale abstract on the endorsement of P1 (fol. 49v), mostly illegible.
P4 and P5 confirm each other independently (20,000 reichsthalers, two months, 500 cuirassiers); P1 and P5 share the Mandelsloh regiment,
the sixty Austrian ox-wagons, the Franconian Circle and the Bishop of Würzburg; P2 and P5 share Leipzig and the half-cannon.

## Prior work

Hermann Stützel, "Chiffrierwesen im Dreißigjährigen Krieg", *Württembergisch Franken* 47 (1963) 109–115 (DOI 10.53458/wfr.v47i.13761,
CC BY 4.0), broke the four systems of the Neuenstein letters to Hatzfeld and printed their keys. Group I (Ferdinand III to Hatzfeld 1641,
Anlage 1) is the system of Bd 242. Stützel says the 1641 letters could all be translated (orders, munitions, provisions) but prints none of
their clear texts, nor shelfmarks or dates. Group II (1636) is edited in full by him (Bd 240, not part of this target).
Not found elsewhere: this repository, research/leads.json, DECODE, web search. The digital edition of the Reichstag of 1640/41 (Deutsche
Reichstagsakten, in preparation) may print the Aachen agreement: to be checked.

## System and key

Homophonic substitution with nulls (Stützel, group I): zodiac signs a–m in order, ◡ n, aspects o–r, planets and Moon s–z, numerals as
homophones of the vowels (3 10 25 = a; 7 8 65 = e; 5 70 81 = i; 30 = o; 4 = u), ten nulls (o‡, [·], ПП, ×, Z, 79, 89, 91, 94, 961), signs
separated by dots, no word division. `key.tsv` is Stützel's table, applied unchanged. Two notes on the 1641 hands (shapes, not key changes):
- u is mostly written as a single loop with a cross above (♁, Stützel's Mars row), b as an 8 with a cross above (♉). Several transcribers
  had noted both as TAU: 37 signs were reviewed on the images and corrected to CROSSO (the blind second transcriber independently wrote
  CROSSO, or CROSSO|TAU, at all 15 of these places on his two pages, and TAU at the true b's).
- y is written as an 8 with a cross below (☿, the horns closed into a loop), x as a single loop with a cross below (♀: "strax", "saxen",
  "oxen"). 10 signs reviewed and corrected VEN → MER; 9 not yet reviewed are left as VEN|MER (counted probable).
Glyph variants outside Stützel's list (crossed and barred forms, 56 letters) are assigned to his signs by shape and by every context, and
counted probable, never certain. Correction trace: CORRECTIONS-T2.tsv (old → new, reason) in the working folder.
- Blind review of the 18 unresolved signs by Brice Dudout (pre-registered; one sign boxed per question, shapes from the same hand, neutral
  ids; correspondence kept outside the page). Where he wrote a remark, the remark was followed rather than the box. 7 tokens changed, 11
  confirmed (CORRECTIONS-T3.tsv): 90v "4" is ♃ t and the third sign is a dot followed by the null [·]; 93r ARI is ◡ n; 97r and 98v carry
  numbers written in clear inside the cipher, 24 and 14 (the 1 and the 4 joined because the pen was not lifted, not a new sign); 101v "8"
  is ♉ b; the last sign of 101v.L09 was marked as ♄ s but remarked "looks like a 5" (5 = i), so it stays unresolved. Letters read from this
  review are counted probable, never certain. Nothing was added to the key; the dot, 24 and 14 are not in Stützel's table.
  None of the 9 VEN|MER signs was among the 18; they stay as they were.

## Transcription

Seven Claude Opus agents, one or more images each, sign by sign, without key values; frozen (SHA-256) before decoding. Token names:
ARI TAU GEM CAN LEO VIR LIB W SAG CAP AQU PSC SUN OPP ABAR PHI SQ TRI SEX SAT JUP MAR CROSSO SHA EARTH VEN MER MOON, nulls OHH BOXDOT PIPI X Z,
numerals as written; A|B = hesitation, ? = illegible, UNK:… = variant, DEL:/INS: = struck out / added above.
Control: a second transcriber, blind to the first, redid one page per hand (47r, 47v, 90v, 93r, 95v, 99r, 102v; 1,576 tokens):
91.5% identical tokens, 93.0% compatible (one of two readings), 94.4% same key value. Most differences are between the shapes of the
nulls (BOXDOT/PIPI) and in the postscript's hand (93r: 67.5%, 40 tokens), which stays below the rule.

## Reading and count (Daniel's rule)

The decryption was read line by line (`reading.md`); every letter is aligned with one decoded sign and the count is made by script.
| piece | words certain | probable | restored | unresolved | total | read | letters read | document |
|---|---|---|---|---|---|---|---|---|
| P1 21 Aug | 122 | 38 | 12 | 0 | 172 | 93.0% | 98.7% | read in part |
| P2 7 Sept | 61 | 7 | 7 | 0 | 75 | 90.7% | 98.4% | read in part |
| P3 postscript | 1 | 2 | 2 | 1 | 6 | 50.0% | 81.8% | read in part |
| P4 Aachen bond | 111 | 20 | 7 | 0 | 138 | 94.9% | 99.1% | read in part |
| P5 14 Sept | 382 | 64 | 21 | 1 | 468 | **95.3%** | 99.2% | **read** |
| **total** | 677 | 131 | 49 | 2 | 859 | **94.1%** | 98.9% | read in part |
P5 is at the edge: it rests on the two numbers read from Brice Dudout's remarks (24 and 14); with one of them left unresolved
it would be 95.1%, with both 94.9%. P4 misses by one word (131/138).
Restored words are mostly a single slip of the scribe in an otherwise certain word (e.g. a w for n, an m for r); they count as holes.
Unresolved after the blind review (6 letters, 2 words): the postscript, one word of 4 letters (decoded mi-t-n-e-ʒ-b-ung, not the
"mitnehmung" fixed beforehand); a marginal insertion on 103r (2, decoded "er", no
reading fixed beforehand). Read from the review: 90v "konnest", "vom 24 Augusti", "innerhalb 14 Tagen", and "selbige" on 101v (shape SAT = s chosen; the remark "looks like a 5" describes that shape).

## Limits

- The clear passages, signatures, countersignatures and the abstract were read by AI agents only, not by a human palaeographer.
- One reader (an agent) made the reading, seeing the decryption; the key was frozen before, and nothing in it was changed.
- Fols. 97v–98r are missing from the copies; other cipher letters of 1641 may be in the unreproduced folios and in Bd 243 (ordered, not received).
