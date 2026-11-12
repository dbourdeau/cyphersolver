# b161 LOG
2026-11-12T13:37:17Z start; blind second transcriber
2026-11-12T13:37:31Z fetched 48574707 1ab03cee218b78eda527a7b52b91d270 901732
2026-11-12T13:37:32Z fetched 48574708 fdeb9f35c45e112725b06905628a589a 1008348
2026-11-12T13:37:33Z fetched 48574737 105d375a9e2621a796790904cb4ec0b8 936412
2026-11-12T13:37:34Z fetched 48574738 5c86572c656dde683a5b5167f714737a 945078
2026-11-12T13:39:16Z FROZE letter A tx/kl_A_205_blind2.txt
2026-11-12T13:41:39Z FROZE letter B
2026-11-12T13:42:15Z aligned with b152 (parser fixed to skip only line-1 header)
2026-11-12T13:43:20Z decoded A and B once with b152 dec_once.py
2026-11-12T13:45:00Z ledger + shuffles done
1ab03cee218b78eda527a7b52b91d270  dl/48574707.jpg
fdeb9f35c45e112725b06905628a589a  dl/48574708.jpg
105d375a9e2621a796790904cb4ec0b8  dl/48574737.jpg
5c86572c656dde683a5b5167f714737a  dl/48574738.jpg
ALIGNMENT vs b152 (difflib on tokens, ? stripped; first-line header only skipped):
 A: mine 130, b152 129; agree 122/130 = 93.85%. Diffs: 205R l1 E|C? ; l4 K|A ; l4 D?|Δ ; 206L l3 V|C? (decode-neutral, both f) ; l7 X|x ; l8 444|477 ; l9 K|A ; 811? (blot group) mine only.
 B: mine 304, b152 304; agree 287/304 = 94.41% (difflib). Reading diffs 12 (H|# x4, X|x x2, I?|L, I?|1, V|C? x4 decode-neutral); order diffs 5 tokens (74 before/after 'wo 61'; insert placement vs '474 K 507 y').
ADJUDICATION on crops (adj/): A l1 sign = [ shape, no middle bar -> b152 (C?/V, =f); my E wrong. A l4 and 206L l9 plain lambda = same shape as agreed carets (235R l2) -> A, b152 right; my K wrong. Triangle: name only, unresolved (no key sign; decode context wants n). 206L l7 straight saltire -> X (mine). 444|477 unresolved from image (open 4s vs 7s); decode favours 477 (=le, 'geleistet'), not used to rescore. 811? smeared group: real comma-delimited group, digits unreadable; decode context wants 'sa'. B H|#: all four single-bar on crops -> H (mine). X|x 235R l2,l12 straight saltire -> X (mine). 235R l4 thick flagged upright: unresolved (I or 1, not small L). l9 thin stroke -> numeral 1 likely (b152). '74' order: page reads 'gleich, / wo 61, [struck] daselbst 74' -> mine. Insert placement: unresolved, mine keeps 'unkosten' contiguous.
2026-11-12T13:45:11Z full images deleted; done
