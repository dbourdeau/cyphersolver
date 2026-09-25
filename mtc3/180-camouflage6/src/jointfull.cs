// Full-alphabet joint polish of the leftover pool: G pieces x 26 letters; every pool symbol sits in a slot or is
// unassigned (cost NULLC per occurrence, log10). Score = sum of full 5-gram log10 prob (lmc/) of each piece + nulls.
// Starts from a groups file (lines "sym:L,..."; G = number of lines), anneals with move/swap.
// usage: JointFull cipher.bin exclude.txt groups.txt restarts iters T0 out.txt
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

class JointFull {
    static float[][] L = new float[6][]; const int P4 = 26 * 26 * 26 * 26;
    static int[] C; static int N, G; static double NULLC = double.Parse(Environment.GetEnvironmentVariable("NULLC") ?? "-2.0", System.Globalization.CultureInfo.InvariantCulture);
    static double PS(int[] slot, int g) {
        double sc = 0; int h = 0, hl = 0; int lo = g * 26, hi = lo + 26;
        for (int i = 0; i < N; i++) {
            int s = slot[C[i]]; if (s < lo || s >= hi) continue; int c = s - lo;
            sc += L[hl + 1][h * 26 + c]; if (hl < 4) { h = h * 26 + c; hl++; } else h = (h * 26 + c) % P4;
        }
        return sc;
    }
    static void Main(string[] a) {
        C = File.ReadAllBytes(a[0]).Select(x => (int)x).ToArray();
        var excl = new bool[256];
        if (a[1] != "-") foreach (var w in File.ReadAllText(a[1]).Split(new[] { ',', ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries)) excl[int.Parse(w)] = true;
        C = C.Where(x => !excl[x]).ToArray(); N = C.Length;
        var lines = File.ReadAllLines(a[2]).Where(x => x.Trim().Length > 0).ToArray(); G = lines.Length;
        int R = int.Parse(a[3]); long iters = long.Parse(a[4]); double T0 = double.Parse(a[5], System.Globalization.CultureInfo.InvariantCulture); string outp = a[6];
        for (int n = 1; n <= 5; n++) { var qb = File.ReadAllBytes("lmc/lp" + n + ".bin"); L[n] = new float[qb.Length / 4]; Buffer.BlockCopy(qb, 0, L[n], 0, qb.Length); }
        var cnt = new int[256]; foreach (int y in C) cnt[y]++;
        var syms = Enumerable.Range(0, 256).Where(y => cnt[y] > 0).ToArray();
        var init = new int[256]; for (int y = 0; y < 256; y++) init[y] = -1;
        for (int g = 0; g < G; g++) foreach (var it in lines[g].Trim().Split(',')) { var p = it.Split(':'); int y = int.Parse(p[0]); if (y < 0 || cnt[y] == 0) continue; init[y] = g * 26 + (p[1][0] - 'A'); }
        int S = G * 26;
        var results = new List<Tuple<double, int[]>>(); object lk = new object();
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 16 }, r => {
            var rng = new Random(77 + r);
            var slot = (int[])init.Clone();
            var occ = new int[S]; for (int s = 0; s < S; s++) occ[s] = -1; foreach (int y in syms) if (slot[y] >= 0) occ[slot[y]] = y;
            var ps = new double[G]; for (int g = 0; g < G; g++) ps[g] = PS(slot, g);
            int nullOcc = syms.Where(y => slot[y] < 0).Sum(y => cnt[y]);
            double cur = ps.Sum() + nullOcc * NULLC, best = cur; var bestSlot = (int[])slot.Clone();
            for (long it = 0; it < iters; it++) {
                double T = T0 * Math.Pow(0.01, (double)it / iters);
                int y = syms[rng.Next(syms.Length)]; int from = slot[y];
                int to = rng.Next(S + 3) >= S ? -1 : rng.Next(S);   // occasionally propose unassigning
                if (to == from) continue;
                if (to < 0 && from < 0) continue;
                int z = to >= 0 ? occ[to] : -1;   // occupant goes to 'from'
                // apply
                slot[y] = to; if (z >= 0) slot[z] = from;
                if (from >= 0) occ[from] = z; if (to >= 0) occ[to] = y;
                var touched = new HashSet<int>(); if (from >= 0) touched.Add(from / 26); if (to >= 0) touched.Add(to / 26);
                double d = 0; var nv = new Dictionary<int, double>();
                foreach (int g in touched) { double v = PS(slot, g); nv[g] = v; d += v - ps[g]; }
                int dn = 0; if (from < 0) dn -= cnt[y]; if (to < 0) dn += cnt[y]; if (z >= 0 && from < 0) dn += cnt[z];
                d += dn * NULLC;
                if (d >= 0 || rng.NextDouble() < Math.Exp(d / T)) {
                    foreach (var kv in nv) ps[kv.Key] = kv.Value; cur += d;
                    if (cur > best + 1e-9) { best = cur; bestSlot = (int[])slot.Clone(); }
                } else {
                    slot[y] = from; if (z >= 0) slot[z] = to;
                    if (from >= 0) occ[from] = y; if (to >= 0) occ[to] = z;
                }
            }
            lock (lk) {
                results.Add(Tuple.Create(best, bestSlot));
                Console.WriteLine("restart {0}: best {1:F1} pieces {2}", r, best, string.Join(" ", Enumerable.Range(0, G).Select(g => PS(bestSlot, g).ToString("F1"))));
            }
        });
        using (var w = new StreamWriter(outp)) {
            foreach (var t in results.OrderByDescending(t => t.Item1).Take(5)) {
                var slot = t.Item2;
                for (int g = 0; g < G; g++) {
                    var key = syms.Where(y => slot[y] >= g * 26 && slot[y] < g * 26 + 26).OrderBy(y => slot[y]).Select(y => y + ":" + (char)('A' + slot[y] - g * 26));
                    var sb = new System.Text.StringBuilder(); foreach (int y in C) if (slot[y] >= g * 26 && slot[y] < g * 26 + 26) sb.Append((char)('A' + slot[y] - g * 26));
                    w.WriteLine("{0:F1} g{1} {2:F1} n={3} {4} | {5}", t.Item1, g, PS(slot, g), sb.Length, string.Join(",", key), sb);
                }
                w.WriteLine("unassigned: " + string.Join(" ", syms.Where(y => slot[y] < 0).Select(y => y + "(" + cnt[y] + ")")));
                w.WriteLine();
            }
        }
    }
}
