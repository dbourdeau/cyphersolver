# b176 LOG
2026-11-12T16:28:24Z created work dir; blind second reader b176 start
2026-11-12T16:28:28Z fetched image 193 (id 48574401) by plain curl
2026-11-12T16:28:50Z fetched images 194 214-216 234-236 247-250 287-289 once each by plain curl; md5s in IMAGES.md5
2026-11-12T16:28:59Z EXPOSURE E1: opened permitted chart CHART_copybook_H_vs_hash.png; its row labels state key values 'H = g (copybook)' and '# = c (copybook)'. Seen before any transcription began; no tx exists yet so nothing to freeze. Impact: knowledge of two sign values; H/# reading still done by bar count only.
2026-11-12T16:29:24Z 193R checked at full res: right page is clear German; faint rows in its left half are show-through, not cipher. Cipher for letter 1 is on 194L (main column + left-margin block). Decision D1: long clear-German stretches summarised as {..clear..}; clear words inside/adjacent to cipher runs written in braces individually.
2026-11-12T16:30:45Z FROZE letter1 tx/kl_193_blind_tx.txt (112a8fac). New sign <I> logged. 3x crops checked: H (517 H), # (498 #), H (1 H E), # interlinear 3-bar mark treated as INS reference mark.
2026-11-12T16:33:40Z FROZE letter2 tx/kl_214_blind_tx.txt (5e47f80f). 3x H/# checks: 215L r3 H, r9 # #, r11 #, r17 #; 215R r1 #, r2 # (smudged), r4 #, r17 H, r20 #. New sign <t> logged.
2026-11-12T16:37:53Z FROZE letter3 tx/kl_234_blind_tx.txt (f416dbf8). New signs logged: second sign-set in 235L margin (<tri><psi><pi><m><theta><gamma>), <hashK> overwrite on 236L. 3x checks: 235L H (r3), #; C (bracket no bar) x3; 235R H x4, # x6; 236L # # H # C.
2026-11-12T16:40:24Z RESUMED after server stop; letters 1-3 frozen intact; letter4 partial notes saved to tx/WIP_248.txt (not frozen)
2026-11-12T16:40:50Z 249R 5x checks: r2 end H, r3 H, 498 H, all single bar; # at 481#, K#, 501#, 517# two bars; <invT> new sign (inverted T)
2026-11-12T16:41:49Z FROZE letter4 tx/kl_248_blind_tx.txt (a2efefae). 250 checks: C x2 (no middle bar), # x2, <invT>, digit 9.
2026-11-12T16:43:04Z FROZE letter5 tx/kl_247_blind_tx.txt (b931b5e5). 247 checks: H x4 single bar, # x2.
2026-11-12T16:44:06Z letter6 287R read; WIP saved tx/WIP_287.txt; margin A keyed by 3-bar mark (after 507 y), margin B keyed by crossed-loop mark under struck word after 477 y
2026-11-12T16:45:20Z 288L read, appended to WIP. checks: H x6 (incl 488 H), # x5, small L x2
2026-11-12T16:46:30Z 288R read, appended. checks: # x5, H x2, C x1, 112 (11+footed-2 shape, as letter1), small L
2026-11-12T16:47:42Z FROZE letter6 tx/kl_287_blind_tx.txt (74d69904). 289 checks: D (crossed), <d> plain, # x3, H x3, E (middle bar present). ALL SIX FROZEN.
2026-11-12T16:47:48Z copied decode scripts and key files (post-freeze)
2026-11-12T16:47:54Z md5 asserts PASS: words e9698159, table 38c7c1e5, kt2.py 4d38a72d
2026-11-12T16:48:12Z PATH-ONLY edits: dec_once.py and shuffle_de152.py sys.path -> b176 scripts; shuffle B -> b176 dir. kt2.py untouched (md5 4d38a72d).
2026-11-12T16:48:12Z decode inputs dec_in/*: mechanical label mapping only (strip INS[/]INS/MARG[/]MARG markers; <I>->I, <invT>->⊥ to match tool sign names); frozen tx untouched
2026-11-12T16:48:17Z all six frozen; now opening first-reader tx files (permitted)
2026-11-12T16:48:48Z align.py label normalisation: o/0->O, [->C, <I>->I, <invT>->⊥, <d>->d, strip ? and umlaut quote marks (label names only)
2026-11-12T16:49:54Z ADJUDICATION (post-freeze, tx unchanged) on 4-5x crops crops/ADJ_*.jpg:
  H vs #: 6 sampled sites (194 517H, 215L 450yH, 235R 451yH, 288L 488H, 236L H472, 288R F476H) all show ONE bar -> b176 (H) right; pattern of first-reader # for single-bar signs in b171 and b175 letters
  194 461 (b176) vs 460: clear 461 -> b176. 235R 178 vs 78: clear 178 -> b176. 287 margin 500 vs 400: clear 5 -> b176. 520 vs 510: unresolved. 235R 203 vs 200: unresolved.
  247 280 (first) vs 210 (b176): clear 280 -> first reader right. 250 507 (first) vs 501 (b176): clear 507 -> first right.
  FINDING: 247R left margin holds a cipher insert keyed by the 3-bar mark above 'y H 78': '[mark] 124? [blot] 172 E x / 233 [blot] E y K # 461 140'. b176 MISSED it (took the mark for the clear insert, which is keyed by its own #); first reader caught only 'x' and '140' as row starts. Both readings incomplete there.
2026-11-12T16:49:59Z decoded each dec_in file ONCE -> dec/
2026-11-12T16:52:49Z FIRST-PASS judging frozen: judge/judged_runs.tsv (9c14f72d); figure of record
2026-11-12T16:53:13Z shuffles 5000 x seeds 20261112 and 7 run once per letter -> shuf/
2026-11-12T16:53:20Z deleted full downloaded images (md5s kept in IMAGES.md5); crops kept
2026-11-12T16:53:50Z REPORT.md written
