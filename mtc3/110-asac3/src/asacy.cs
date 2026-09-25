// ASAC Part 3: find the PRNG (y-coordinate part: base sequence v[10] + odd column rotations px[1,3,5,7,9]) and the
// transposition width, using the known unseeded MSVC rand(): the Polybius cell of plaintext character i lies just after
// r_i = rand() % 100, so (stream digit at odd p) - r_i/10 - k[p % 100] follows the row-offset distribution P_dy.
// Fitness(k) = sum over cipher columns of the best (natural column c, start offset o) score.
// usage: AsacY cipher.txt Lmin Lmax restarts iters [out.txt]
class AsacY {
    public static int[] C; public static int N, NI; public static int[] EY, EX;
    public static double[] WY = new double[10], WX = new double[10];
    public static void InitRand(int n) {
        EY = new int[n]; EX = new int[n]; uint s = 1;
        for (int i = 0; i < n; i++) { s = s * 214013 + 2531011; int r = (int)((s >> 16) & 0x7FFF) % 100; EY[i] = r / 10; EX[i] = r % 10; }
        double[] py = { .18, .276, .208, .135, .071, .066, .034, .018, .005, .007 };
        double[] px = { .126, .121, .114, .078, .091, .094, .08, .107, .103, .087 };
        for (int d = 0; d < 10; d++) { WY[d] = Math.Log10(py[d] / 0.1); WX[d] = Math.Log10(px[d] / 0.1); }
    }
    public static int[] KeyOdd(int[] v, int[] px) { // keystream digits for all 100 classes (even classes = 0 placeholder)
        var k = new int[100];
        for (int x = 1; x < 10; x += 2) for (int y = 0; y < 10; y++) k[x + 10 * y] = (x + v[((y - px[x / 2]) % 10 + 10) % 10]) % 10;
        return k;
    }
    // per-L structures
    public class LS { public int L, H, Lg; public int[] oLo, oHi; }
    public static LS MakeL(int L) {
        var s = new LS { L = L, H = (N + L - 1) / L }; s.Lg = N - (s.H - 1) * L; s.oLo = new int[L]; s.oHi = new int[L];
        for (int A = 0; A < L; A++) { s.oLo[A] = (s.H - 1) * A + Math.Max(0, A - (L - s.Lg)); s.oHi[A] = (s.H - 1) * A + Math.Min(A, s.Lg); }
        return s;
    }
    public static double ColScore(LS s, int[] k, int A, int c, int o) {
        int len = c < s.Lg ? s.H : s.H - 1; if (o + len > N) return double.NegativeInfinity;
        double sc = 0;
        for (int r = 0; r < len; r++) { int p = c + r * s.L; if ((p & 1) == 0) continue; int i = p >> 1; if (i >= NI) continue; sc += WY[((C[o + r] - EY[i] - k[p % 100]) % 10 + 20) % 10]; }
        return sc;
    }
    public static double Fitness(LS s, int[] k) {
        double tot = 0;
        for (int A = 0; A < s.L; A++) {
            double best = double.NegativeInfinity;
            for (int c = 0; c < s.L; c++) {
                if ((s.L & 1) == 0 && (c & 1) == 0) continue; // even L: even columns hold x digits only
                for (int o = s.oLo[A]; o <= s.oHi[A]; o++) { double v = ColScore(s, k, A, c, o); if (v > best) best = v; }
            }
            if ((s.L & 1) == 0 && best == double.NegativeInfinity) best = 0;
            tot += Math.Max(best, -5); // x columns (even L) cannot score; clip
        }
        return tot;
    }
    static void Main(string[] a) {
        C = File.ReadAllText(a[0]).Where(char.IsDigit).Select(ch => ch - '0').ToArray(); N = C.Length; NI = N / 2; InitRand(NI);
        int Lmin = int.Parse(a[1]), Lmax = int.Parse(a[2]), R = int.Parse(a[3]); long iters = long.Parse(a[4]);
        string outp = a.Length > 5 ? a[5] : "asacy_out.txt";
        var results = new List<string>(); object lk = new object();
        var jobs = new List<Tuple<int, int>>(); for (int L = Lmin; L <= Lmax; L++) for (int r = 0; r < R; r++) jobs.Add(Tuple.Create(L, r));
        Parallel.ForEach(jobs, new ParallelOptions { MaxDegreeOfParallelism = 16 }, job => {
            int L = job.Item1; var s = MakeL(L); var rng = new Random(L * 977 + job.Item2 * 13 + 1);
            var v = new int[10]; var px = new int[5]; for (int i = 0; i < 10; i++) v[i] = rng.Next(10); for (int i = 0; i < 5; i++) px[i] = rng.Next(10);
            double cur = Fitness(s, KeyOdd(v, px)), best = cur; string bk = "";
            double T0 = 3.0;
            for (long it = 0; it < iters; it++) {
                double T = T0 * Math.Pow(0.02, (double)it / iters);
                int w = rng.Next(15); int old; if (w < 10) { old = v[w]; v[w] = (old + 1 + rng.Next(9)) % 10; } else { old = px[w - 10]; px[w - 10] = (old + 1 + rng.Next(9)) % 10; }
                double f = Fitness(s, KeyOdd(v, px));
                if (f >= cur || rng.NextDouble() < Math.Exp((f - cur) / T)) { cur = f; if (cur > best) { best = cur; bk = string.Join("", v) + " " + string.Join("", px); } }
                else { if (w < 10) v[w] = old; else px[w - 10] = old; }
            }
            lock (lk) { string line = string.Format("L={0} r={1} best {2:F1} v,px {3}", L, job.Item2, best, bk); results.Add(line); Console.WriteLine(line); }
        });
        File.WriteAllLines(outp, results);
    }
}
