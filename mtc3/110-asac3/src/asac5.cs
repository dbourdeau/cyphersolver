// ASAC Part 5: square + PRNG re-rotated every 100 digits, no transposition. With the unseeded MSVC rand() known, anneal
// the 20 PRNG shift digits on the row-offset score (odd stream digits), then the square on the German 5-gram, and check
// rand() consistency.  usage: Asac5 cipher.txt restarts iters
class Asac5 {
    static void Main(string[] a) {
        AsacCore.Load("../lmde");
        AsacY.C = File.ReadAllText(a[0]).Where(char.IsDigit).Select(ch => ch - '0').ToArray(); AsacY.N = AsacY.C.Length; AsacY.NI = AsacY.N / 2; AsacY.InitRand(AsacY.NI);
        var C = AsacY.C; int N = AsacY.N, NI = AsacY.NI; int R = int.Parse(a[1]); int iters = int.Parse(a[2]);
        int blocks = (N + 99) / 100;
        double decay = double.Parse(Environment.GetEnvironmentVariable("DECAY") ?? "3", System.Globalization.CultureInfo.InvariantCulture);
        var WB = Enumerable.Range(0, blocks).Select(b => 1.0 / (1 + b / decay)).ToArray();
        Func<int[], double> fit = pr => {
            var ks = AsacCore.Keystream(pr.Take(10).ToArray(), pr.Skip(10).ToArray(), blocks); double s = 0;
            for (int i = 0; i < NI; i++) { int p = 2 * i + 1; s += WB[p / 100] * AsacY.WY[((C[p] - AsacY.EY[i] - ks[p / 100][p % 100]) % 10 + 20) % 10]; }
            return s;
        };
        var res = new List<Tuple<double, int[]>>(); object lk = new object();
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 16 }, r => {
            var rng = new Random(r * 17 + 3); var pr = new int[20]; for (int i = 0; i < 20; i++) pr[i] = rng.Next(10);
            double cur = fit(pr), best = cur; var bp = (int[])pr.Clone(); double T0 = 5;
            for (int it = 0; it < iters; it++) {
                double T = T0 * Math.Pow(0.01, (double)it / iters);
                int i1 = rng.Next(20), o1 = pr[i1]; pr[i1] = (o1 + 1 + rng.Next(9)) % 10;
                int i2 = -1, o2 = 0; if (rng.Next(4) == 0) { i2 = rng.Next(20); if (i2 == i1) i2 = -1; else { o2 = pr[i2]; pr[i2] = (o2 + 1 + rng.Next(9)) % 10; } }
                double f = fit(pr);
                if (f >= cur || rng.NextDouble() < Math.Exp((f - cur) / T)) { cur = f; if (cur > best) { best = cur; bp = (int[])pr.Clone(); } } else { pr[i1] = o1; if (i2 >= 0) pr[i2] = o2; }
            }
            lock (lk) { res.Add(Tuple.Create(best, bp)); Console.WriteLine("restart {0}: {1:F1} pr {2}", r, best, string.Join("", bp)); }
        });
        var top = res.OrderByDescending(t => t.Item1).First(); var prb = top.Item2;
        var ksb = AsacCore.Keystream(prb.Take(10).ToArray(), prb.Skip(10).ToArray(), blocks);
        var cells = new int[NI]; for (int i = 0; i < NI; i++) { int p = 2 * i; cells[i] = ((C[p] - ksb[p / 100][p % 100]) % 10 + 10) % 10 + 10 * (((C[p + 1] - ksb[(p + 1) / 100][(p + 1) % 100]) % 10 + 10) % 10); }
        var sres = new List<Tuple<double, int[]>>();
        Parallel.For(0, 16, r => {
            var rng = new Random(r * 101 + 7); var buf = new int[NI]; var q2 = new int[20]; for (int i = 0; i < 20; i++) q2[i] = rng.Next(10);
            Func<int[], double> ev = q => { var sq = AsacCore.SquareSyms(q.Take(10).ToArray(), q.Skip(10).ToArray()); for (int i = 0; i < NI; i++) buf[i] = sq[cells[i]]; return AsacCore.ScoreSyms(buf, NI); };
            double c0 = ev(q2), best = c0; var bk = (int[])q2.Clone(); double T0 = NI * 0.002;
            for (int it = 0; it < 200000; it++) {
                double Tm = T0 * Math.Pow(0.005, it / 200000.0);
                int i1 = rng.Next(20), o1 = q2[i1]; q2[i1] = (o1 + 1 + rng.Next(9)) % 10; double f = ev(q2);
                if (f >= c0 || rng.NextDouble() < Math.Exp((f - c0) / Tm)) { c0 = f; if (c0 > best) { best = c0; bk = (int[])q2.Clone(); } } else q2[i1] = o1;
            }
            lock (lk) sres.Add(Tuple.Create(best, bk));
        });
        foreach (var b in sres.OrderByDescending(x => x.Item1).Take(2)) {
            var sqc = AsacCore.SquareChars(b.Item2.Take(10).ToArray(), b.Item2.Skip(10).ToArray());
            int ok = 0; for (int i = 0; i < NI; i++) { int r = AsacY.EY[i] * 10 + AsacY.EX[i]; char ch = sqc[cells[i]]; int m = 0; while (sqc[(r + m) % 100] != ch) m++; if ((r + m) % 100 == cells[i]) ok++; }
            Console.WriteLine("pr {0} square {1} LM {2:F1} ({3:F2}/char) rand-consistent {4}/{5}", string.Join("", prb), string.Join("", b.Item2), b.Item1, b.Item1 / NI, ok, NI);
            Console.WriteLine(new string(cells.Select(c => sqc[c]).ToArray()));
        }
    }
}
