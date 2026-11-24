# Vetting, 19 Nov 2026 (project): leads 1577 and 2744 corrected to "existing (Avenel 1858), verified with the key"

PR #813 (open, bdudout) shows the nine 1629 Richelieu letters of leads 1577 and 2744 are printed by Avenel (Lettres du
cardinal de Richelieu III, 1858) and checks his glosses with the key for fr. 3829 ff. 87, 89. `vetting.json` replaces
the two verdicts (`supersedes`) and corrects the lead text and the folio of CLVIII (fol. 59, not Avenel's printed
'fol. 69'). Avenel's heading of CLXVII also reads 'fol. 78' where the PR gives fol. 73: recorded, not settled without the
volume. Checked with `python research/vet.py --check`, written with `--apply`.
