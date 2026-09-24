// Bigram substitution solver with incremental 5-gram scoring and letter-level moves.
// usage: Big2 ciphertext.txt restarts iters T0 T1 [seed] [fixed.txt]
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;

class Big2 {
    static float[][] L = new float[6][]; static string LMDIR = Environment.GetEnvironmentVariable("LMDIR") ?? "lmc/";
    static int[] C; static int N, M, NL; static string[] syms; static int[][] occ;

    class St {
        public int[] map, owner, pt; public float[] lp; public double score;
        public int[] mark; public int stamp; public List<int> idx = new List<int>();
    }
    static float LPat(int[] pt, int i) {
        int hl = Math.Min(i, 4); int h = 0; for (int q = i - hl; q < i; q++) h = h * 26 + pt[q];
        return L[hl + 1][h * 26 + pt[i]];
    }
    static void Init(St s) {
        s.pt = new int[NL]; s.lp = new float[NL]; s.mark = new int[NL];
        for (int i = 0; i < N; i++) { s.pt[2 * i] = s.map[C[i]] / 26; s.pt[2 * i + 1] = s.map[C[i]] % 26; }
        s.score = 0; for (int i = 0; i < NL; i++) { s.lp[i] = LPat(s.pt, i); s.score += s.lp[i]; }
    }
    // set symbol u to value v (updating pt), collect affected letter indices
    static void SetSym(St s, int u, int v) {
        s.map[u] = v;
        foreach (int p in occ[u]) {
            s.pt[2 * p] = v / 26; s.pt[2 * p + 1] = v % 26;
            for (int q = 2 * p; q <= 2 * p + 5 && q < NL; q++) if (s.mark[q] != s.stamp) { s.mark[q] = s.stamp; s.idx.Add(q); }
        }
    }
    static Tuple<double, int[]> Anneal(int[] fx, long iters, double T0, double T1, int seed, int[] init) {
        var r = new Random(seed); var s = new St();
        var free = Enumerable.Range(0, M).Where(u => fx[u] < 0).ToArray();
        s.map = new int[M]; s.owner = Enumerable.Repeat(-1, 676).ToArray();
        for (int u = 0; u < M; u++) if (fx[u] >= 0) { s.map[u] = fx[u]; s.owner[fx[u]] = u; }
        foreach (int u in free) {
            int v;
            if (init != null && s.owner[init[u]] < 0) v = init[u]; else do v = r.Next(676); while (s.owner[v] >= 0);
            s.map[u] = v; s.owner[v] = u;
        }
        Init(s); double best = s.score; int[] bm = (int[])s.map.Clone();
        var oldlp = new float[NL];
        for (long it = 0; it < iters; it++) {
            double T = T0 * Math.Pow(T1 / T0, (double)it / iters);
            int u = free[r.Next(free.Length)]; int ov = s.map[u]; int v; double mv = r.NextDouble();
            if (mv < 0.4) v = r.Next(26) * 26 + ov % 26; else if (mv < 0.8) v = (ov / 26) * 26 + r.Next(26); else if (mv < 0.9) v = r.Next(676);
            else { int u2 = free[r.Next(free.Length)]; v = s.map[u2]; }
            if (v == ov) continue;
            int w = s.owner[v]; if (w >= 0 && fx[w] >= 0) continue;
            s.stamp++; s.idx.Clear();
            SetSym(s, u, v); if (w >= 0) SetSym(s, w, ov);
            double d = 0; foreach (int q in s.idx) { oldlp[q] = s.lp[q]; float nl = LPat(s.pt, q); d += nl - s.lp[q]; s.lp[q] = nl; }
            if (d >= 0 || r.NextDouble() < Math.Exp(d / T)) {
                s.owner[v] = u; s.owner[ov] = w; s.score += d;
                if (s.score > best) { best = s.score; bm = (int[])s.map.Clone(); }
            } else {
                s.stamp++; s.idx.Clear();
                SetSym(s, u, ov); if (w >= 0) SetSym(s, w, v);
                foreach (int q in s.idx) s.lp[q] = LPat(s.pt, q);
            }
        }
        return Tuple.Create(best, bm);
    }
    static string Dec(int[] map) { var sb = new System.Text.StringBuilder(); foreach (int u in C) { sb.Append((char)('A' + map[u] / 26)); sb.Append((char)('A' + map[u] % 26)); } return sb.ToString(); }

    static void Main(string[] a) {
        string ct = new string(File.ReadAllText(a[0]).Where(char.IsLetter).ToArray()).ToUpper();
        int R = int.Parse(a[1]); long iters = long.Parse(a[2]); var ci = System.Globalization.CultureInfo.InvariantCulture;
        double T0 = double.Parse(a[3], ci), T1 = double.Parse(a[4], ci); int seed0 = a.Length > 5 ? int.Parse(a[5]) : 1;
        for (int n = 1; n <= 5; n++) { var qb = File.ReadAllBytes(LMDIR + "lp" + n + ".bin"); L[n] = new float[qb.Length / 4]; Buffer.BlockCopy(qb, 0, L[n], 0, qb.Length); }
        var bg = Enumerable.Range(0, ct.Length / 2).Select(i => ct.Substring(2 * i, 2)).ToArray();
        syms = bg.Distinct().ToArray(); M = syms.Length; N = bg.Length; NL = 2 * N;
        C = bg.Select(s => Array.IndexOf(syms, s)).ToArray();
        occ = Enumerable.Range(0, M).Select(u => Enumerable.Range(0, N).Where(i => C[i] == u).ToArray()).ToArray();
        var fx = Enumerable.Repeat(-1, M).ToArray();
        if (a.Length > 6 && a[6] != "-") foreach (var line in File.ReadAllLines(a[6])) {
            var p = line.Split(' '); if (p.Length < 2) continue; int u = Array.IndexOf(syms, p[0]); if (u < 0) continue;
            fx[u] = (p[1][0] - 'A') * 26 + (p[1][1] - 'A');
        }
        Console.WriteLine("N={0} symbols={1} fixed={2}", N, M, fx.Count(x => x >= 0));
        string crib = Environment.GetEnvironmentVariable("CRIB");
        if (crib != null) {
            var results = new System.Collections.Concurrent.ConcurrentBag<Tuple<double, int, int[]>>();
            Parallel.For(0, NL - crib.Length + 1, new ParallelOptions { MaxDegreeOfParallelism = 20 }, pos => {
                var f2 = (int[])fx.Clone(); var used = new int[676]; for (int q = 0; q < 676; q++) used[q] = -1;
                for (int u = 0; u < M; u++) if (f2[u] >= 0) used[f2[u]] = u;
                bool ok = true; int s0 = pos % 2 == 0 ? pos : pos + 1; int e0 = pos + crib.Length;
                for (int q = s0; q + 1 < e0 && ok; q += 2) {
                    int u = C[q / 2]; int pb = (crib[q - pos] - 'A') * 26 + (crib[q + 1 - pos] - 'A');
                    if (f2[u] >= 0 && f2[u] != pb) ok = false; else if (used[pb] >= 0 && used[pb] != u) ok = false; else { f2[u] = pb; used[pb] = u; }
                }
                if (!ok) return;
                var t = Anneal(f2, iters, T0, T1, pos, null);
                results.Add(Tuple.Create(t.Item1, pos, t.Item2));
            });
            foreach (var t in results.OrderByDescending(x => x.Item1).Take(12)) { var d = Dec(t.Item3); Console.WriteLine("{0:F1} pos {1} {2}", t.Item1, t.Item2, d.Substring(Math.Max(0, t.Item2 - 50), 170)); }
            return;
        }
        int[] init = null;
        if (a.Length > 7) { init = new int[M]; foreach (var line in File.ReadAllLines(a[7])) { var p = line.Split(' '); int u = Array.IndexOf(syms, p[0]); if (u >= 0) init[u] = (p[1][0] - 'A') * 26 + (p[1][1] - 'A'); } }
        var res = new Tuple<double, int[]>[R];
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 20 }, ri => { res[ri] = Anneal(fx, iters, T0, T1, seed0 * 1000 + ri, init); });
        var bestT = res.OrderByDescending(x => x.Item1).First();
        Console.WriteLine("score {0:F1}\n{1}", bestT.Item1, Dec(bestT.Item2));
        File.WriteAllLines("big2_best.txt", Enumerable.Range(0, M).Select(u => syms[u] + " " + (char)('A' + bestT.Item2[u] / 26) + (char)('A' + bestT.Item2[u] % 26)));
        Console.WriteLine("all: " + string.Join(" ", res.Select(x => x.Item1.ToString("F0"))));
    }
}
