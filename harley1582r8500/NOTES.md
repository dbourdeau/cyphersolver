# Sir Edward Stafford (Paris) to [Walsingham], 20 August 1586 (BL Harley MS 1582 ff. 65-66; DECODE R8500)

DECODE refill catalogue entry 119 "... to unknown recipient", 20 Aug 1586 (rule-scored class C). Worked 22 Sept 2026.

Outcome: **read.** All five cipher runs read with the letter key of Stafford's Walsingham cipher, rebuilt here from
sibling letters in the same volume (glossed runs on f. 73r, R8502; the contemporary decipherment on f. 72r of the
f. 71 runs, R8501). No decipherment of this letter is on the page or in print.

## What the record is

DECODE R8500 (4 images) is a holograph despatch in clear English, f. 65r-65v, signed "E. Stafford", dated
"Paris this xxth of August 1586"; endorsed on f. 66v "20 August 1586. From Sr Edw. Stafford". So the sender is
Stafford (DECODE "..."), the place is Paris (London is only where the manuscript is held), and the recipient is
almost certainly Walsingham (same series as R8503, addressed to him). Contents: Captain Blaize (Blaise), the
Neapolitan in Cesar's company, and his dealings; Locatello; Cambrai; a book printed at Rome by Dr Sanders. The
margin of f. 65v carries a note on a request by "one that was Mr Dennys man".

The cipher is five short runs in the postscript on f. 65v, without glosses.

## Key

Stafford's cipher is a letter substitution with homophones plus codes (B alone = Villeroy, O+ alone = Duke/Duchess
of Nemours, numbers 120 = French ambassador, 47 = King of Navarre, 22, 20, 54). Letter values, from the f. 72r crib
aligned with the f. 71 runs and the f. 73r glosses (Junius, Cambray, Balagny, Germany, 10000 crownes):
w=a (and a d-form), 24=b, d=l/c, D=u/v, D d=w, 6=e, psi=f, B=g, λ=h, x=i/y, M=k, a=l, oo=m, h=n, n=o, E=p,
Δ=q, O+=r, II/#/I=s, u=t, A=t, H=y, rho=u. Files: `sib_runs.txt` (sibling runs), `f72r_clear.txt`, `alignment.txt`,
`key.tsv`. Earlier assumption "6 = null" (from R8503) was wrong: 6 is e.

## Reading (f. 65v postscript)

| run | ciphertext | reading | in context |
|---|---|---|---|
| 1 | x D h x D II · II n n h 6 | Junius sonne | "yesterday came hither **Junius' son**" |
| 2 | f O+ n oo · d x oo 24 O+ w 7 H 6 | from Cambraye | "**from Cambray**, and brought me letters from his father and the other that is with him" |
| 3 | d O+ 6 w x A · D d x u λ · 24 w a w h H x | credit with Balagny | "other papers that he hath sent me to keep of his **credit with Balagny**" |
| 4 | 24 w a w h H x | Balagny | "but I am afraid **Balagny** dare them some mischief after so long dealing with them" |
| 5 | oo w H x h u w σ H δ h 6 | mayntayne | "[I] **maintain** he is in another than he hath heard often from your honour of long time" |

Junius = presumably the Dutch agent Junius (his son brought letters from Cambrai); Balagny = Jean de Monluc,
seigneur de Balagny, governor of Cambrai.

Measured: 61 tokens, 20 distinct (`python docs/_check_profile.py --measure ciphertext.txt`). Four signs take their
value from context only: run 3 A (t) and the 'a'-shaped fourth sign (d); run 5 σ and δ (read a, y/e variants).
All 61 tokens read as sense (100%); 57 confirmed by the sibling key, 4 by context.

## Prior art and print

CSP Foreign XXI pt 1, August 1586 (BHO pp. 64-80) calendars a different Stafford letter of 20 August (SP 78, on
Navarre and Guise); this Harley letter is not calendared and none of the cipher names appear. No decipherment found.

## Remaining gaps

None in sense. Four sign values rest on context (see above), not on a second occurrence in the siblings.

## Escalation

- [x] siblings: R8501 (f. 71-72, with f. 72r decipherment), R8502 (f. 73, glossed), R8503, R8504 viewed
- [x] clear-pages: f. 72r decipherment used as crib
- [x] known-keys: no printed Stafford-Walsingham key; key rebuilt here
- [x] print: CSP Foreign XXI pt 1 (August 1586) checked; not calendared
- [x] key-rebuild: letter key rebuilt from the crib and glosses (`key.tsv`)
- [x] retry: runs re-cropped at native resolution and re-read after the 6 = e correction

Images are BL material behind the DECODE login: kept git-ignored in `img/` and `sib/`.
