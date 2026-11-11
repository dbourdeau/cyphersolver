# PREREG — Jablonski -> Ráday cipher, held-out test (frozen 2026-11-10, before any view of the portion)

Portion (held out): ALL numeric groups on SBB PPN1853544159 scans 91 and 92 (Nachl. Francke 11,2/16 : 44,
Jablonski -> Ráday, 14 Feb 1707), letter body + P.S. Expected >= 150 groups. Not viewed in this session
(scans 86 first strip only was viewed, which belongs to no. 42).

Blind transcription: the groups are transcribed ONLY from red-ink-only renderings of scans 91-92 (pixels
where R-G and R-B exceed a threshold kept in their colour, everything else white), so the Latin draft under
the groups is not seen until the decode is frozen. Line breaks kept; illegible groups marked '?'.

Key: rebuilt ONLY from figure/plaintext pairs on scans 23, 24, 37, 38, 39, 71, 72 of PPN1853543950
(11,2/15 nos. 8, 13, 33; 1705) and scans 86-87 of PPN1853544159 (11,2/16 no. 42, 7 Dec 1706). Frozen
before the portion is transcribed.

Decode: each group -> key value; nulls -> ''; unknown group -> '?' (one char). Concatenated letters only.

Reference: the Latin words written under the groups on scans 91-92, read AFTER the decode is frozen,
restricted to the stretches covered by groups (normalised: lower case, letters only, j->i, v->u, ae/oe kept
as written letters).

Measure (once): character accuracy = 1 - Levenshtein(decode, reference)/len(reference), per letter.
Control: 200 keys made by shuffling the key's values over its groups (seed 20261110); best control score.
Pass: accuracy >= 0.85 AND >= best control + 0.30.
Order of freezing (SHA-256 into gel/HASHES.txt): PREREG, portion (scan list + SHA of images), key,
transcription, decode, reference (clear). Portion is burnt once measured.
