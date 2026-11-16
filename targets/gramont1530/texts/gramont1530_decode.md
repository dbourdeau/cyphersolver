# BnF fr. 3071 no. 7, f. 17r: mechanical decode of the transcription (14 Nov 2026)

Each line of `gramont1530_transcription.txt` decoded sign by sign with George Lasry's table "Gramont's cipher (1530)"
(`../img/BnF_fr3071_f17.png`, rendered in `key.md`). This is the check of the transcription, a single AI transcription not
checked by a person; no letter is supplied. Capitals = the table's value of the sign. Lower-case b, v, e = the sign `g`,
which the table gives for B and V and the leaf also uses for E: the letter is chosen by the word. `[...]` with a sign
name = a sign without a value. `?` = the sign is doubtful in the transcription. Word division is added.

Signs that are not letters in the table: `4t` reads ET at all four places (L01, L03, L06, L13; the table has this shape
under S); `COM` (B with bars) stands for *con-* and *com-* (L03, L05, L12), `CON` for *con-* (L01); `8Δ` = PAPE and the
key-ring sign = ROY as in `key.md`.

    L01 LE [ʃʃ] [Z̄] VOvLOIR eST TOVSIOvRS bON ET <CON>TINVe PLVS QvE IA-
    L02 MAIS [#] IE SVIS APRES POVR LE FAIRE MeCTRe A DEV[▣]e XE-
    L03 CVTION ET POVRCE QVe LES IMPERIAVLX POvRROIENT <COM>Ce-
    L04 PVOIR PLVS GRANT SVSPECON SI IE Y ALLOIS POvRCe
    L05 <COM>MANCEMENT [PAPE] TROvVE bON QvE LEDICT FRANCISQVe Y AILLE
    L06 SeVL POvR SCAvOIR QvEL IL Y FAICT ET ME SEMbLE QvIL
    L07 NI A QvE RIEN DAvLTANT QVESTANT YCI IE POvRRAY ObVIeR
    L08 A TOvT CE QvE LON LVY POvRROIT MECTRe AvANT POvR LE DIVeRT-
    L09 IR A QVOY? VOvS PVIS ASSEVReR QVE LON FAICT TOvTE LA
    L10 DILLIGeNCE POSSIbLe MONSIEvR LEVESQve DE FAYA?NCe
    L11 NEPVEv DV CONTE DE CARPI PARTIRA DEDANS TRO?IS Ov
    L12 QVATRe IOvRS POVR DE LA PART DV [PAPE] SE ALLeR <COM>GRATV-
    L13 LLER AvEC LE [ROY] DE LA VENVe DE LA ROYNe ET DE MESSeIGNeVRS

536 signs (552 tokens by `docs/_check_profile.py --measure --drop-first`, less the 16 separator marks `|` and `·`).
Without a value: `ʃʃ` and `Z̄` (L01, after LE and before VOVLOIR), `#` (L02, between MAIS and IE), and `▣` in L02
(the table gives X; the word wants DEVE, "à deue execution"; left open). Three signs doubtful (L09, L10, L11).

## What the decode changes in the reading of 18 Sept 2026 (`../fr3071_no7_gramont.md`)

- L02, gap before "[...]cution": *ie suis apres pour le faire mectre a dev[.]e execution*.
- L03-L04, "recepvoir": the signs are `COM ς g` + *pvoir* = *concepvoir*.
- L04-L05, "pource [...] commancement [le pape] a trouvé bon": no gap and no sign for *a*: *pource commancement [pape] trouve bon*.
- L06-L07, "y aille [...] qu'il n'y a que bien": *y aille seul pour scavoir quel il y faict, et me semble qu'il n'i a que rien*
  (the sign before IEN is the table's R, `E`; *bien* is not carried by the signs).
- L07, "d'aultant [..] estant ici": *d'aultant qu'estant yci*.
- L12-L13, "[s'en aller?] congratuler": *se aller congratuller*.
