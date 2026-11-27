# Catalogue review of 22 Nov 2026, put back through the lead queue (PR #910)

Pull request #910 first added these 44 rows to `catalogue.json` by hand, as ids 3644 to 3697, each with a `vetting`
block written by the review of 22 Nov 2026 (Codex): Scandinavian cipher runes (Nordby 2018, Runor, RuneS),
alchemical manuscripts with cipher (Wellcome, Ferguson, Weimar, Wolfenbüttel, the 2024 HistoCrypt survey), Rákóczi-era
number ciphers (MNL), Hilandar Slavic cryptograms (Ohio State catalogue), and Russian items from Butskikh's register of
undeciphered cryptography. The house rule is that a new find enters the catalogue only through the lead queue and
`docs/_check_catalogue.py --promote`, so on 26 Nov 2026 the rows were taken out of `catalogue.json` and put here,
with the PR's text and vetting unchanged except as listed below, then merged by `merge.py --write` (ids 3890 to 3933).

## What changed from the PR's rows

- `id`, `counted`, `scored`, `ark` and `repository` dropped (the merge and the gate set them).
- Vocabulary fixed for `merge.py`: region "Norway" to "Scandinavia"; period "1601-1700" and "1501-1600" to the
  project's buckets by year; 18 rows had `year: null` and now carry a sorting year taken from their `date` field, with a
  `year_note` saying so.
- Eight rows carry a `vetting_note` and stay leads (below).

## Outcome

- **36 promoted** by the gate (`--promote`), keeping their lead ids.
- **8 left as leads**:
  - 3920, 3927, 3929, 3930, 3931 (Butskikh X.23, X.24, XVII.26, XIX.17, XIII.17): the PR's `prior_art.literature`
    records no literature search (it repeats the dating or shelfmark remarks). Kept as `literature_note`; the field is
    now missing, so `--lead` reports it.
  - 3894 (Columbia MS Or 34 coded year), 3914 (Hilandar 112 cover, six signs), 3933 (Hilandar 786, five letters): too
    short to count as a target on their own, the same call the 25 Nov vetting pass made for lead 2903.

## PR #910 id to lead id

| PR | Lead | | PR | Lead | | PR | Lead |
|---|---|---|---|---|---|---|---|
| 3644 | 3890 | | 3665 | 3902 | | 3681 | 3917 |
| 3647 | 3891 | | 3666 | 3903 | | 3682 | 3918 |
| 3648 | 3892 | | 3667 | 3904 | | 3683 | 3919 |
| 3649 | 3893 | | 3668 | 3905 | | 3684 | 3920 (lead) |
| 3650 | 3894 (lead) | | 3669 | 3906 | | 3685 | 3921 |
| 3651 | 3895 | | 3671 | 3907 | | 3686 | 3922 |
| 3655 | 3896 | | 3672 | 3908 | | 3687 | 3923 |
| 3656 | 3897 | | 3673 | 3909 | | 3688 | 3924 |
| 3657 | 3898 | | 3674 | 3910 | | 3689 | 3925 |
| 3662 | 3899 | | 3675 | 3911 | | 3690 | 3926 |
| 3663 | 3900 | | 3676 | 3912 | | 3691 | 3927 (lead) |
| 3664 | 3901 | | 3677 | 3913 | | 3692 | 3928 |
| | | | 3678 | 3914 (lead) | | 3693 | 3929 (lead) |
| | | | 3679 | 3915 | | 3694 | 3930 (lead) |
| | | | 3680 | 3916 | | 3695 | 3931 (lead) |
| | | | | | | 3696 | 3932 |
| | | | | | | 3697 | 3933 (lead) |

The other six rows of PR #910 were already leads: 2109, 2896, 2897 and 2942 got the PR's vetting blocks in
`research/leads.json` and were promoted under their own ids; 2901 and 2903 were dropped from the promotion (the
25 Nov vetting pass marked them not ready).
