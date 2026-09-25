// Diagnose recovered camouflage groups: (1) per assigned symbol, the LLR of keeping it vs sending it to the pool,
// (2) per pool symbol, the best (group, free letter) placement by LLR. Full 26-letter 5-gram LM (lmc/).
// usage: Diag cipher.bin groups.txt [out.txt]
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;

class Diag {
    static float[][] L = new float[6][]; const int P4 = 26 * 26 * 26 * 26;
    static int[] C; static int N, G;
    static double Sc(int[] g, int[] l, int k) {
        double sc = 0; int h = 0, hl = 0;
        for (int i = 0; i < N; i++) {
            int y = C[i]; if (g[y] != k) continue; int c = l[y];
            sc += L[hl + 1][h * 26 + c]; if (hl < 4) { h = h * 26 + c; hl++; } else h = (h * 26 + c) % P4;
        }
        return sc;
    }
    static void Main(string[] a) {
        C = File.ReadAllBytes(a[0]).Select(x => (int)x).ToArray(); N = C.Length;
        var lines = File.ReadAllLines(a[1]).Where(x => x.Trim().Length > 0).ToArray(); G = lines.Length;
        for (int n = 1; n <= 5; n++) { var qb = File.ReadAllBytes("lmc/lp" + n + ".bin"); L[n] = new float[qb.Length / 4]; Buffer.BlockCopy(qb, 0, L[n], 0, qb.Length); }
        var g = new int[256]; var l = new int[256];
        for (int y = 0; y < 256; y++) { g[y] = -1; l[y] = -1; }
        for (int k = 0; k < G; k++) foreach (var it in lines[k].Split(',')) { var p = it.Split(':'); int y = int.Parse(p[0]); if (y < 0) continue; g[y] = k; l[y] = p[1][0] - 'A'; }
        var cnt = new int[256]; foreach (int y in C) cnt[y]++;
        var syms = Enumerable.Range(0, 256).Where(y => cnt[y] > 0).ToArray();
        var baseS = new double[G]; for (int k = 0; k < G; k++) baseS[k] = Sc(g, l, k);
        var w = new StreamWriter(a.Length > 2 ? a[2] : "diag_out.txt");
        w.WriteLine("# keep LLR of assigned symbols (low/negative = suspicious)");
        foreach (int y in syms.Where(y => g[y] >= 0)) {
            int k = g[y]; var g2 = (int[])g.Clone(); g2[y] = -1;
            double keep = baseS[k] - Sc(g2, l, k) - cnt[y] * L[1][l[y]];
            w.WriteLine("K g{0} {1}:{2} n={3} keep={4:F1} per={5:F2}", k + 1, y, (char)('A' + l[y]), cnt[y], keep, keep / cnt[y]);
        }
        w.WriteLine("# best placements of pool symbols (LLR vs unigram in an unknown piece)");
        var pool = syms.Where(y => g[y] < 0).ToArray();
        var res = new string[pool.Length]; var best = new double[pool.Length];
        Parallel.For(0, pool.Length, i => {
            int y = pool[i]; var g2 = (int[])g.Clone(); var l2 = (int[])l.Clone();
            var opts = new List<Tuple<double, int, int>>();
            for (int k = 0; k < G; k++) {
                var used = new bool[26]; foreach (int z in syms) if (g[z] == k) used[l[z]] = true;
                for (int c = 0; c < 26; c++) {
                    if (used[c]) continue;
                    g2[y] = k; l2[y] = c;
                    double gain = Sc(g2, l2, k) - baseS[k] - cnt[y] * L[1][c];
                    opts.Add(Tuple.Create(gain, k, c));
                }
                g2[y] = -1;
            }
            var top = opts.OrderByDescending(t => t.Item1).Take(3).ToArray();
            best[i] = top[0].Item1;
            res[i] = string.Format("P {0} n={1} ", y, cnt[y]) + string.Join("  ", top.Select(t => string.Format("g{0}:{1} {2:F1}", t.Item2 + 1, (char)('A' + t.Item3), t.Item1)));
        });
        foreach (int i in Enumerable.Range(0, pool.Length).OrderByDescending(i => best[i])) w.WriteLine(res[i]);
        w.Close(); Console.WriteLine("done");
    }
}
