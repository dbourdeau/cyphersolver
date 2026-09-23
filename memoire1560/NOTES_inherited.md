# Mémoire en chiffre du XIIe décembre 1560: BnF fr. 3157 no. 67

Status: in progress

Catalogue 276. BnF fr. 3157 ("Recueil de lettres et de pièces originales", Montmorency papers), item 67,
"Mémoire en chiffre du XIIe decembre 1560". Gallica btv1b90598645.

## Where it is

- The BnF notice (archivesetmanuscrits cc496207) puts each item's folio before its number, so item 67 is
  ff. 152r-156v, not f. 158 (f. 158 is item 68, Marillac's clear despatch from England).
- Gallica views: f.152r = view 153 (right page); 152v/153r = view 154; 153v/154r = 155; 154v/155r = 156;
  155v/156r = 157; 156v = view 158 (left page). f.157v (view 159, left) is the dorse: endorsement in a later hand
  "henry second" and a line in the same cipher script.
- Heading on f.152r in clear: "Du xiie decembre 1560". No address, no signature, no decipherment anywhere
  in the item or the neighbouring leaves. The Villars letters around it (items 65, 66, 69, 71, 72) are in clear.

## The cipher

A cursive pseudo-script with the words divided by "/". Homophonic substitution: most letters have two or
three signs, some signs are two-stroke units ("zo" = u, "pp" = m, "io" = u, "s3" hooked long s = r, ":." = o,
"nn" = s), and a few whole-word codes (Z = pour, 4 = roy, c+ / i+ / e+ = et, F and g = sieur).
Key: `key.txt`. Sign code: `SIGNS.md` plus the extra codes in the comment lines of each
`transcription/<fol>.txt`.

## How it was broken

1. Transcribed ff.152r-156v into ASCII sign codes (three transcription agents, `transcription/`).
2. Plain one-sign-per-letter annealing (`solve.py`, fr-1530-despatches 5-gram with word spaces): gibberish.
3. "z" is followed by "o" in 262 of 283 cases: "zo" taken as one unit. The most frequent 4-sign word "Tzox"
   (23x) fitted "que", "Wx"/"Wxm"/"hx" fitted le/les/de. With those seeded, the annealer produced
   "les derniers advertissemens", "les affaires de pardeça", "presches", "assemblées".
4. Alignment of decrypted words fixed more units: "xrQxrhio" = entendu (r = n, a separate sign from x;
   io = u), "Dio:is" = avoir, "3shDx+is3xppxrQ" = ordinairement (s3 = r).
5. Short standalone groups read from context as codes: "temps Z avoir secours" (Z = pour), "que le 4 et
   vostre grandeur" (4 = roy), "c+" where "et" is required.

## Content (first pass)

A report to "vostre grandeur" (the connétable de Montmorency) from someone living in the Agenais, a
neighbour of the sieur de Fumel ("monsieur de Fumel qui est mon prochain voisin"), on the Protestant
"rebelles" of the Agenais in the weeks after the death of François II: preaching and assemblies "plus
que jamais" in the towns, ladies of the nobility attending (madame de Castelpers, mademoiselle de ...);
two thousand rebels at Clairac; the seigneur de Caumont and his places; the présidial of Agen and the syndic
and tiers état of the Agenois sent to court to disguise the truth; the "chief" (their leader) and his
suite at Nérac; M. de Lioux, "frère du sieur de Montluc", going to court; M. de Termes's companies
countermanded; the rebels counting on a prince, on foreigners near Geneva and on the Swiss cantons.
The writer is not Blaise de Monluc himself (he names "le sieur de Montluc" in the third person).

## Remaining gaps

(to be filled after the reading)

## Escalation

(to be filled after the reading)
