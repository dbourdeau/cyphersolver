// Joint core solve for the leftover pool of a camouflage cipher: G pieces x K letters (ORDER[0..K-1]) = slots; the
// top M symbols by count (M >= G*K; the extra ones may stay unassigned) are annealed onto the slots by swaps.
// Score = sum over pieces of the K-letter restricted 5-gram LLR (letters outside the core deleted).
// usage: JointCore cipher.bin corpus.txt exclude.txt G K M restarts iters out.txt [truekey.bin]
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

class JointCore {
    static string ORDER = Environment.GetEnvironmentVariable("ORDER") ?? "THEANDOISRLCUMWFGYPBVKJXQZ";
    static int[] C; static int N; static float[] LMk; static float[] UNk; static int K, G;

    static void BuildLM(byte[] corpus, int k) {
        var map = new int[26]; for (int i = 0; i < 26; i++) map[i] = -1; for (int i = 0; i < k; i++) map[ORDER[i] - 'A'] = i;
        var seq = new List<byte>(corpus.Length); foreach (byte b in corpus) { int m = map[b]; if (m >= 0) seq.Add((byte)m); }
        var s = seq.ToArray(); int n = s.Length;
        double[][] cntn = new double[6][];
        for (int o = 1; o <= 5; o++) {
            int size = 1; for (int q = 0; q < o; q++) size *= k; cntn[o] = new double[size];
            int h = 0, mod = size / k;
            for (int i = 0; i < n; i++) { h = (h % Math.Max(1, mod)) * k + s[i]; if (o == 1) h = s[i]; if (i >= o - 1) cntn[o][h]++; }
        }
        double tot = cntn[1].Sum(); UNk = new float[k]; for (int a = 0; a < k; a++) UNk[a] = (float)Math.Log10((cntn[1][a] + 1) / (tot + k));
        double[] prev = new double[k]; for (int a = 0; a < k; a++) prev[a] = (cntn[1][a] + 1) / (tot + k);
        double D = 0.75;
        for (int o = 2; o <= 5; o++) {
            int nctx = cntn[o].Length / k; var P = new double[cntn[o].Length]; int lowMod = nctx / k;
            for (int ctx = 0; ctx < nctx; ctx++) {
                double ch = 0; int tp = 0; for (int a = 0; a < k; a++) { double c = cntn[o][ctx * k + a]; ch += c; if (c > 0) tp++; }
                int low = lowMod > 0 ? ctx % lowMod : 0;
                for (int a = 0; a < k; a++) { double lo = prev[low * k + a]; P[ctx * k + a] = ch < 5 ? lo : Math.Max(cntn[o][ctx * k + a] - D, 0) / ch + D * tp / ch * lo; }
            }
            prev = P;
        }
        LMk = prev.Select(x => (float)Math.Log10(x)).ToArray();
    }
    // slot of symbol: piece*K+letter, or -1
    static double PieceScore(int[] slot, int g) {
        double sc = 0; int h = 0, hl = 0; int k4 = K * K * K * K; int lo = g * K, hi = lo + K;
        for (int i = 0; i < N; i++) {
            int s = slot[C[i]]; if (s < lo || s >= hi) continue; int a = s - lo;
            if (hl == 4) sc += LMk[h * K + a] - UNk[a];
            if (hl < 4) { h = h * K + a; hl++; } else h = (h * K + a) % k4;
        }
        return sc;
    }
    static void Main(string[] a) {
        C = File.ReadAllBytes(a[0]).Select(x => (int)x).ToArray();
        var corpus = File.ReadAllText(a[1]).ToUpperInvariant().Where(ch => ch >= 'A' && ch <= 'Z').Select(ch => (byte)(ch - 'A')).ToArray();
        var excl = new bool[256];
        if (a[2] != "-") foreach (var w in File.ReadAllText(a[2]).Split(new[] { ',', ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries)) excl[int.Parse(w)] = true;
        G = int.Parse(a[3]); K = int.Parse(a[4]); int M = int.Parse(a[5]); int R = int.Parse(a[6]); long iters = long.Parse(a[7]); string outp = a[8];
        byte[] tk = a.Length > 9 ? File.ReadAllBytes(a[9]) : null;
        C = C.Where(x => !excl[x]).ToArray(); N = C.Length;
        var cnt = new int[256]; foreach (int y in C) cnt[y]++;
        var top = Enumerable.Range(0, 256).Where(y => cnt[y] > 0).OrderByDescending(y => cnt[y]).Take(M).ToArray();
        Console.WriteLine("N={0} pool symbols {1}, core symbols {2} (min count {3}), slots {4}", N, cnt.Count(c => c > 0), top.Length, cnt[top[top.Length - 1]], G * K);
        BuildLM(corpus, K);
        int S = G * K; // slot ids 0..S-1; positions S..M-1 = unassigned
        var results = new List<Tuple<double, int[]>>(); object lk = new object();
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = int.Parse(Environment.GetEnvironmentVariable("THREADS") ?? "16") }, r => {
            var rng = new Random(1000 + r);
            var perm = top.OrderBy(x => rng.Next()).ToArray(); // perm[p] = symbol at position p
            var slot = new int[256]; for (int y = 0; y < 256; y++) slot[y] = -1;
            for (int p = 0; p < M; p++) slot[perm[p]] = p < S ? p : -1;
            var ps = new double[G]; for (int g = 0; g < G; g++) ps[g] = PieceScore(slot, g);
            double cur = ps.Sum(), best = cur; int[] bestSlot = (int[])slot.Clone();
            double T0 = 3.0, T1 = 0.05;
            for (long it = 0; it < iters; it++) {
                double T = T0 * Math.Pow(T1 / T0, (double)it / iters);
                int p1 = rng.Next(M), p2 = rng.Next(M); if (p1 == p2 || (p1 >= S && p2 >= S)) continue;
                if (p1 < S && p2 < S && p1 / K == p2 / K && rng.Next(4) != 0) { } // same-piece letter swaps allowed
                int y1 = perm[p1], y2 = perm[p2];
                perm[p1] = y2; perm[p2] = y1; slot[y2] = p1 < S ? p1 : -1; slot[y1] = p2 < S ? p2 : -1;
                int g1 = p1 < S ? p1 / K : -1, g2 = p2 < S ? p2 / K : -1;
                double n1 = g1 >= 0 ? PieceScore(slot, g1) : 0, n2 = (g2 >= 0 && g2 != g1) ? PieceScore(slot, g2) : 0;
                double delta = (g1 >= 0 ? n1 - ps[g1] : 0) + ((g2 >= 0 && g2 != g1) ? n2 - ps[g2] : 0);
                if (delta >= 0 || rng.NextDouble() < Math.Exp(delta / T)) {
                    if (g1 >= 0) ps[g1] = n1; if (g2 >= 0 && g2 != g1) ps[g2] = n2; cur += delta;
                    if (cur > best) { best = cur; bestSlot = (int[])slot.Clone(); }
                } else { perm[p1] = y1; perm[p2] = y2; slot[y1] = p1 < S ? p1 : -1; slot[y2] = p2 < S ? p2 : -1; }
            }
            lock (lk) {
                results.Add(Tuple.Create(best, bestSlot));
                var bps = Enumerable.Range(0, G).Select(g => PieceScore(bestSlot, g)).OrderByDescending(x => x).ToArray();
                Console.WriteLine("restart {0}: best {1:F1} pieces {2}", r, best, string.Join(" ", bps.Select(x => x.ToString("F1"))));
            }
        });
        using (var w = new StreamWriter(outp)) {
            foreach (var t in results.OrderByDescending(t => t.Item1)) {
                var slot = t.Item2;
                for (int g = 0; g < G; g++) {
                    var key = new List<string>(); for (int q = 0; q < K; q++) { int y = Array.IndexOf(slot, g * K + q); key.Add(y + ":" + ORDER[q]); }
                    var sb = new System.Text.StringBuilder(); foreach (int y in C) { int s = slot[y]; if (s >= g * K && s < g * K + K) sb.Append(ORDER[s - g * K]); }
                    w.WriteLine("{0:F1} g{1} {2:F1} {3} | {4}", t.Item1, g, PieceScore(slot, g), string.Join(",", key), sb);
                }
                w.WriteLine();
            }
        }
    }
}
