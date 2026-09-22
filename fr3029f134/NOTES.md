# BnF fr. 3029 ff. 134-135 (no. 59), cipher letter "Au Roy" (DECODE R3670) — NOTES

Status: no write-up (unpublished 22 Sept 2026 at George Lasry's request: he and a historian have deciphered and analysed these letters for their own publication; do not publish or send to DECODE without his word). Read 22 Sept 2026. Key: Lasry 2023, applied unchanged. Name signs open.

## What it is

- BnF, Français 3029, ff. 134r-135v, no. 59: f.134r 26 cipher lines, f.135r 4 lines, f.135v address in clear
  "Au Roy / Mon souverain seigneur". Gallica btv1b90598719, views 210 (f.134r), 211 (f.135r), 213 (address);
  views 208 and 212 are blank versos. The canvases carry no folio labels (view 182 = f.118, 206 = f.132).
- DECODE R3670: "Unknown sender to Francis I, 11 Jan 1530", Non-decrypted, 3 pp. The date's source is not given;
  the other fr. 3029 cipher records (R3666-R3687) are dated "1530-1540" in the listing.
- Sender: unknown. Not signed; the letter begins mid-sentence, so a first leaf may be missing.

## Key

The cipher is the one Tomokiyo calls "De la Tremoille's(?) Cipher" (cryptiana GL.htm, local copy
`gramont1529/GL.htm`), broken by George Lasry in 2023 and independently by Norbert Biermann. Lasry's table
(05/11/2023) is `key_f67.png`: one sign per letter (O has two forms, U/V and I/J shared), six null signs,
Nom 1-4 and Place 1. Tomokiyo lists f.134 no.59 among the letters in this cipher but prints readable text only for
f.67 and f.186 (and fr. 3092 f.100). The earlier repo target `fr3029/` (catalogue 174) closed the volume as "already
broken" without reading any leaf; this folder reads f.134.

The key applies **unchanged**: no sign needed a new value.

## Reading

`reading.md` (text, translation, doubtful points); `transcription.txt` (per line, sign aliases = key letters);
`signs.txt` (one character per sign: 926 letters, 49 nulls, 9 name/place signs = 984).

Content: someone ("le dit sieur") means to recover by arms costs he could not have by agreement, and will press on
against the lands of the Church unless ‹N1› or ‹P1› promise to reimburse ‹N3›; by their obligations to ‹N3›, ‹P1› and
‹N1› must assist him, this being tacitly within the defensive league. The Venetian ambassador says the Cardinal
persuaded him, so that the Signoria would not be against ‹N4›. News "de bon lieu": the archbishopric of Toledo given
to the bishop of Palencia, charged with pensions (cardinal de' Medici 20,000 ducats "de L.lis", "cardinal d'Iort"
20,000, protonotary Carafa "newly created cardinal" 10,000); the bishop of Badajoz, who had been promised it, has
left discontented. f.135r: someone mutinied from the court of ‹N2›; a rumour that ‹N2› was nearly poisoned in a
piece of beef and the cooks arrested.

Read bar: 975 of 984 signs have a value (0.991); all read as sense apart from the name "L.lis" (4 letters). Class
**read**; only the nine name/place-sign tokens are open.

## Dating (open)

DECODE's 11 Jan 1530 is unsourced. Toledo was vacant from Croÿ's death (Worms, 11 Jan 1521) until Fonseca's
appointment (1523/24), and again after Fonseca's death (Feb 1534). The bishop of Palencia in 1520-22 was Pedro Ruiz
de la Mota, Charles V's favourite, which, with a "cardinal de Medicis" and a Church war to recover lands, points to
1521 and supports Tomokiyo's tentative 1520-21 for this cipher. Against that: no cardinal Carafa was created in 1521
(Gian Vincenzo Carafa 1527, Gian Pietro Carafa 1536). Not resolved; the page says so. That the DECODE date is 11 Jan,
the day Croÿ died, may be a coincidence.


Update 22 Sept 2026: the sister memoirs in BnF fr. 3092 ff. 101-107 (`fr3092/`), read with the same key, identify
<N3> as the word "roy" (either king) and <N2> as the Emperor (Charles V), grade C from context; <N1> is probably the
King of England (M); <N4> and <P1> stay open. Here that gives "promectre au roy", "la court de l'Empereur".

## Remaining gaps

- name signs N1-N4 and place sign P1, 9 tokens - blocker: open-codes; unidentified in Lasry's table too; only a
  reading of the sibling letters (fr. 3029 ff. 67-202, fr. 3092 ff. 101-107) could fix them
- "L.lis" (134r20), a proper name - blocker: too-short; one occurrence, letters certain, referent unknown

## Escalation

- [x] siblings: fr3029/ NOTES list the 20 sibling records; Tomokiyo's printed f.67/f.186 texts leave the name signs blank too
- [x] clear-pages: none on the leaves; f.135v is the address only
- [x] known-keys: Lasry's table reads every letter sign; no other key needed
- [x] print: GL.htm, francis.htm: no text of f.134; fr3029/ notes found none elsewhere
- [n/a] key-rebuild: the letter key is complete; name signs occur 1-2 times each, too few to rebuild from this letter
- [x] retry: doubtful spots re-cropped at full resolution (blot at 134r22 = C; "?icy"; "l.lis"; "diort")
