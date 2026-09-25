// ASAC two-phase substitution solver.
// Phase 1: PRNG shifts (20 digits) by annealing the coincidence count of the aligned cells (square-independent).
// Phase 2: square shifts (20 digits) by annealing the German 5-gram score with the PRNG fixed.
// usage: Asac2 digits.txt mode(2|5) restarts iters1 iters2
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

class Asac2 {
    static int[] D; static int N, NP, MODE, BLOCKS;
    static int[][] KS(int[] pr) { return AsacCore.Keystream(pr.Take(10).ToArray(), pr.Skip(10).Take(10).ToArray(), MODE == 5 ? BLOCKS : 1); }
    static int Kd(int[][] ks, int p) { return MODE == 5 ? ks[p / 100][p % 100] : ks[0][p % 100]; }
    public static double IC(int[] pr, int[] cnt) {
        var ks = KS(pr); Array.Clear(cnt, 0, 100);
        for (int i = 0; i < NP; i++) { int p = 2 * i; int x = (D[p] - Kd(ks, p) + 10) % 10, y = (D[p + 1] - Kd(ks, p + 1) + 10) % 10; cnt[x + 10 * y]++; }
        double s = 0; for (int c = 0; c < 100; c++) s += cnt[c] * (cnt[c] - 1); return s;
    }
    static int[] Cells(int[] pr) {
        var ks = KS(pr); var cells = new int[NP];
        for (int i = 0; i < NP; i++) { int p = 2 * i; cells[i] = (D[p] - Kd(ks, p) + 10) % 10 + 10 * ((D[p + 1] - Kd(ks, p + 1) + 10) % 10); }
        return cells;
    }
    static double LMScore(int[] sq, int[] cells, int[] buf) { for (int i = 0; i < NP; i++) buf[i] = sq[cells[i]]; return AsacCore.ScoreSyms(buf, NP); }
    static void Main(string[] a) {
        AsacCore.Load("../lmde");
        D = File.ReadAllText(a[0]).Where(char.IsDigit).Select(c => c - '0').ToArray(); N = D.Length; NP = N / 2; BLOCKS = (N + 99) / 100;
        MODE = int.Parse(a[1]); int R = int.Parse(a[2]); long it1 = long.Parse(a[3]), it2 = long.Parse(a[4]);
        // phase 1
        var p1 = new List<Tuple<double, int[]>>(); object lk = new object();
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 16 }, r => {
            var rng = new Random(r * 31 + 5); var cnt = new int[100];
            var pr = new int[20]; for (int i = 0; i < 20; i++) pr[i] = rng.Next(10);
            double cur = IC(pr, cnt), best = cur; var bk = (int[])pr.Clone(); double T0 = NP * 0.5;
            for (long it = 0; it < it1; it++) {
                double T = T0 * Math.Pow(0.002, (double)it / it1);
                int i1 = rng.Next(20), o1 = pr[i1]; pr[i1] = (o1 + 1 + rng.Next(9)) % 10;
                double v = IC(pr, cnt);
                if (v >= cur || rng.NextDouble() < Math.Exp((v - cur) / T)) { cur = v; if (cur > best) { best = cur; bk = (int[])pr.Clone(); } } else pr[i1] = o1;
            }
            lock (lk) p1.Add(Tuple.Create(best, bk));
        });
        double rnd = (double)NP * (NP - 1) / 100;
        foreach (var t in p1.OrderByDescending(t => t.Item1).Take(5)) Console.WriteLine("phase1 IC {0:F0} (random {1:F0}) pr {2}", t.Item1, rnd, string.Join("", t.Item2));
        // phase 2 on the top distinct phase-1 results
        foreach (var t in p1.OrderByDescending(t => t.Item1).Take(2)) {
            var cells = Cells(t.Item2);
            var p2 = new List<Tuple<double, int[]>>();
            Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 16 }, r => {
                var rng = new Random(r * 101 + 7); var buf = new int[NP];
                var k = new int[20]; for (int i = 0; i < 20; i++) k[i] = rng.Next(10);
                Func<int[], double> ev = kk => LMScore(AsacCore.SquareSyms(kk.Take(10).ToArray(), kk.Skip(10).ToArray()), cells, buf);
                double cur = ev(k), best = cur; var bk = (int[])k.Clone(); double T0 = NP * 0.002;
                for (long it = 0; it < it2; it++) {
                    double T = T0 * Math.Pow(0.005, (double)it / it2);
                    int i1 = rng.Next(20), o1 = k[i1]; k[i1] = (o1 + 1 + rng.Next(9)) % 10;
                    double v = ev(k);
                    if (v >= cur || rng.NextDouble() < Math.Exp((v - cur) / T)) { cur = v; if (cur > best) { best = cur; bk = (int[])k.Clone(); } } else k[i1] = o1;
                }
                lock (lk) p2.Add(Tuple.Create(best, bk));
            });
            var b = p2.OrderByDescending(x => x.Item1).First();
            var sq = AsacCore.SquareChars(b.Item2.Take(10).ToArray(), b.Item2.Skip(10).ToArray());
            var txt = new string(cells.Select(c => sq[c]).ToArray());
            Console.WriteLine("phase2 {0:F1} ({1:F2}/char) key sq {2} pr {3}", b.Item1, b.Item1 / NP, string.Join("", b.Item2), string.Join("", t.Item2));
            Console.WriteLine(txt.Length > 600 ? txt.Substring(0, 600) : txt);
        }
    }
}
