// Final assembly for the camouflage cipher once pieces are separated: greedy/heat-bath over ALL symbols with the
// partition as a starting point (groups file: one line per group "sym:L,sym:L,..."; symbols not listed start unassigned
// and may join any group with any free letter). Score = sum over groups of full 5-gram LM (lmc/).
// usage: Assemble cipher.bin groups.txt sweeps out.txt
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;

class Assemble {
    static float[][] L = new float[6][]; const int P4 = 26 * 26 * 26 * 26;
    static int[] C; static int N, G;
    static int[] g = new int[256], l = new int[256];

    static double GroupScore(int k) {
        double sc = 0; int h = 0, hl = 0;
        for (int i = 0; i < N; i++) {
            int y = C[i]; if (g[y] != k) continue; int c = l[y];
            sc += L[hl + 1][h * 26 + c]; if (hl < 4) { h = h * 26 + c; hl++; } else h = (h * 26 + c) % P4;
        }
        return sc;
    }
    static double Total() { double t = 0; for (int k = 0; k < G; k++) t += GroupScore(k); return t; }

    static void Main(string[] a) {
        C = File.ReadAllBytes(a[0]).Select(x => (int)x).ToArray(); N = C.Length;
        var lines = File.ReadAllLines(a[1]).Where(x => x.Trim().Length > 0).ToArray(); G = lines.Length;
        int sweeps = int.Parse(a[2]);
        for (int n = 1; n <= 5; n++) { var qb = File.ReadAllBytes("lmc/lp" + n + ".bin"); L[n] = new float[qb.Length / 4]; Buffer.BlockCopy(qb, 0, L[n], 0, qb.Length); }
        for (int y = 0; y < 256; y++) { g[y] = -1; l[y] = -1; }
        for (int k = 0; k < G; k++) foreach (var it in lines[k].Split(',')) { var p = it.Split(':'); int y = int.Parse(p[0]); if (y < 0) continue; g[y] = k; l[y] = p[1][0] - 'A'; }
        var syms = C.Distinct().ToArray();
        Console.WriteLine("groups {0}, unassigned symbols {1} (occurrences {2})", G, syms.Count(y => g[y] < 0), C.Count(y => g[y] < 0));
        // unassigned symbols: letters positions are simply absent from groups (score ignores them) -> must be placed
        for (int sw = 0; sw < sweeps; sw++) {
            int changes = 0;
            foreach (int y in syms.OrderByDescending(y => C.Count(z => z == y))) {
                int og = g[y], ol = l[y];
                var baseG = new double[G]; for (int k = 0; k < G; k++) baseG[k] = GroupScore(k);
                double best = double.NegativeInfinity; int bg = og, bl = ol;
                // candidate slots: every (group, letter); swap with occupant
                var cands = new List<Tuple<int, int>>();
                for (int k = 0; k < G; k++) for (int c = 0; c < 26; c++) cands.Add(Tuple.Create(k, c));
                var res = new double[cands.Count];
                var gg = (int[])g.Clone(); var ll = (int[])l.Clone();
                Parallel.For(0, cands.Count, () => Tuple.Create((int[])g.Clone(), (int[])l.Clone()), (i, st, loc) => {
                    var G2 = loc.Item1; var L2 = loc.Item2; Array.Copy(g, G2, 256); Array.Copy(l, L2, 256);
                    int k = cands[i].Item1, c = cands[i].Item2;
                    int t = -1; for (int z = 0; z < 256; z++) if (G2[z] == k && L2[z] == c && z != y) { t = z; break; }
                    G2[y] = k; L2[y] = c; if (t >= 0) { G2[t] = og; L2[t] = ol; }
                    // score affected groups
                    double s = 0; var touched = new HashSet<int> { k }; if (og >= 0) touched.Add(og);
                    foreach (int kk in touched) s += ScoreWith(G2, L2, kk) - baseG[kk];
                    res[i] = s; return loc;
                }, loc => { });
                // current (no change) = 0 if assigned; if unassigned, staying unassigned is not allowed
                double stay = og >= 0 ? 0 : double.NegativeInfinity;
                int bi = -1; best = stay;
                for (int i = 0; i < res.Length; i++) if (res[i] > best + 1e-9) { best = res[i]; bi = i; }
                if (bi >= 0) {
                    int k = cands[bi].Item1, c = cands[bi].Item2;
                    int t = -1; foreach (int z in syms) if (g[z] == k && l[z] == c && z != y) { t = z; break; }
                    g[y] = k; l[y] = c; if (t >= 0) { g[t] = og; l[t] = ol; }
                    changes++;
                }
            }
            Console.WriteLine("sweep {0}: changes {1}, total {2:F1}, unassigned {3}", sw, changes, Total(), syms.Count(y => g[y] < 0));
            if (changes == 0) break;
        }
        using (var w = new StreamWriter(a[3])) {
            for (int k = 0; k < G; k++) {
                var sb = new System.Text.StringBuilder(); foreach (int y in C) if (g[y] == k) sb.Append((char)('A' + l[y]));
                w.WriteLine("GROUP {0} score {1:F1} key {2}", k, GroupScore(k), string.Join(",", syms.Where(y => g[y] == k).Select(y => y + ":" + (char)('A' + l[y]))));
                w.WriteLine(sb.ToString());
            }
        }
        Console.WriteLine("written " + a[3]);
    }
    static double ScoreWith(int[] G2, int[] L2, int k) {
        double sc = 0; int h = 0, hl = 0;
        for (int i = 0; i < N; i++) {
            int y = C[i]; if (G2[y] != k) continue; int c = L2[y];
            sc += L[hl + 1][h * 26 + c]; if (hl < 4) { h = h * 26 + c; hl++; } else h = (h * 26 + c) % P4;
        }
        return sc;
    }
}
