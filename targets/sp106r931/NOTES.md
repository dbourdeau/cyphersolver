# An English royalist letter in a numerical code, September 1645 (TNA SP 106/10 f. 251, DECODE R931)

Status: attempted, not solved — no key found; Lasry's 1645-46 SP 106 keys, the R932 Goring key and the Charles I →
Culpeper 1645 key do not fit.

**Split on 14 Oct 2026** from `sp106box10` under the one-key rule (George Lasry, 14 Oct 2026). R931 came into that
entry with catalogue item 58, whose other three records (R656, R662, R722) belong to the 1623-25 codebreaker's file; R931
does not: it is twenty years later and in another code. The file's ciphers have their own entries
([`sp106box10`](../sp106box10/NOTES.md), [`sp106r725`](../sp106r725/NOTES.md), [`sp106r722`](../sp106r722/NOTES.md),
[`sp106r704`](../sp106r704/NOTES.md)); the Henrietta Maria letters of 1645-46 in the same box, read by Lasry, are
`hm1645`, `sp106r787`, `sp106r924`, `sp106r929`, and the Goring letter of the next record is `goring1645` (different
keys). The work below was done in the sp106box10 session of 21 Sept 2026 and is carried over from its NOTES.

Catalogue item 58 stays open for this record (attempted, open).

## The document

R931 (f. 251, 1 p.): a strip of numbers 10-260 with clear words: "(1) septembre 1645", "earnestly", "reasons",
"from", "(2)". DECODE transcription by FK (18 March 2020), checked against the image on 21 Sept 2026, copied here as
`R931_decode_transcription.txt` (from the main checkout's `sp106c58/decode/DOC_R931_D1901_1901.txt`; image
`IMG_R931_I4928_P1.png` there, git-ignored). Count of 21 Sept 2026: about 192 numbers, 104 distinct (not re-measured;
a quick tokenisation of the DECODE file on 14 Oct 2026 gives 176 numbers, 101 distinct, the difference being DECODE's
spacing and interlinear corrections such as the 114 and 60 written above line 6). With so many distinct numbers in
so short a text it is a nomenclator, not a letter cipher.

## What was tried (21 Sept 2026)

- All of George Lasry's 1645-46 SP 106 keys on DECODE (TNA SP 106, SP106-2, SP106-5, SP106-8) and the June 1645
  Goring key of the next record R932 (Lasry, SP106-3): coverage at most 0.45, gibberish.
- The Charles I → Culpeper 1645 key (BL Add MS 32256 ff. 6-7, DECODE R9117/R9118): letters 1-78, words 300-600,
  nothing in 100-260; does not fit. R9116 (1642) is a bare frequency tally and R9119 f. 8 blank.

## Remaining gaps
- R931, all cipher numbers - blocker: no-key-material; none of the known 1645 royalist keys fits; needs the matching key (Digby / Nicholas / Goring correspondence of autumn 1645, BL Add MS 32256 ff. 4-9 or Egerton 2550, DECODE R9115-R9119, R3053-R3105)

## Escalation
- [x] siblings: R930, R932 and the SP 106/10 neighbours opened; R932 is Goring's letter in another key
- [x] clear-pages: none
- [x] known-keys: Lasry's SP 106, SP106-2, -3, -5, -8 keys and the Culpeper key R9117/R9118 tried
- [ ] print: not done
- [n/a] key-rebuild: about 190 numbers, 104 values, a nomenclator: too short to rebuild without a key
- [n/a] retry: nothing to retry with
