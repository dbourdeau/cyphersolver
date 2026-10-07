# February 20, 1808 transformation search

**Verdict: no convincing signal in the tested transformations.**

| Code | Best transformation (small/large shifts) | Score | Shuffled best mean +/- SD | z | p | Coverage |
|---|---|---:|---:|---:|---:|---:|
| WE028 | Split modular, +1374 / +1511 | -2.53225 | -2.54719 +/- 0.00819 | 1.83 | 0.055 | 100.0% |
| Armstrong972 | Split modular, +278 / +831 | -7.03619 | -7.04861 +/- 0.00697 | 1.78 | 0.045 | 63.7% |

Here small means x<100; y=1+((x-1+k) mod N), with N=1600 for WE028 and assumed N=1700 for the incomplete Armstrong key. Scores are mean natural-log character likelihood, higher better.

Tested 19,648,254 parameter settings across direct/modular shifts, reversal, all 24 padded digit permutations, all 10,000 decimal-position offsets, exhaustive separate small/large shifts, and all invertible affine maps. A smoothed character bigram model used 125,680 letters of Austen (1813); syllables were concatenated.

Every search was repeated on 200 shuffled ciphertexts. Across all 16 code/family comparisons, empirical max-z p=0.403. Thus the approximately 1.8-sigma best scores do not establish a decoding signal.

Top three distinct candidates (all WE028 split-modular; vertical bars show code-group boundaries):

1. +1374/+1511; score -2.53225, search-control z=1.83: `november | more | angue | there | idge | ledge | quire | mos | go | more`.
2. +1374/+154; score -2.55246, search-control z=-0.64: `mag | super | orn | disaffect | idge | die | faction | sur | rich | super`.
3. +1372/+1511; score -2.55867, search-control z=-1.40: `november | more | angue | there | id | ledge | quire | mos | go | more`.

No tested transformation maps all five groups (17,18,38,1,14) simultaneously into {the,of,and,to,a}; the maximum is two for either key. Individual matches can always be forced by a shift and are not evidence.

Limitations: Armstrong has only 760 known entries. Additional Cryptiana tables could not be fetched (curl DNS failure; web HTTP 503); this is not an exclusion of other Weber codes or untested compound transformations. Independent rescoring verified all 3,216 family/control winners within 1e-13.
