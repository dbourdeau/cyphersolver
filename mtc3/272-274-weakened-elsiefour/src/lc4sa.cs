// Simulated annealing over the unknown cells of an LC4 key (nonce-free), scoring the decryption with a char 5-gram LM.
// usage: Lc4Sa ciphertext keytemplate restarts iters T0 T1 [seed]
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

class Lc4Sa {
    const string AL = "#_23456789abcdefghijklmnopqrstuvwxyz";
    static float[][] L = new float[6][]; const int K = 28; static int[] lmSym = new int[36];
    static int[] CT; static int T; static double OtherPen = double.Parse(Environment.GetEnvironmentVariable("OTHERPEN") ?? "2.0", System.Globalization.CultureInfo.InvariantCulture); static int[] unkCells; static int[] tmpl;

    static double Decrypt(int[] key, int[] pt) {
        var S = new int[36]; Array.Copy(key, S, 36); var pos = new int[36]; for (int q = 0; q < 36; q++) pos[S[q]] = q;
        int mr = 0, mc = 0; double sc = 0; int ctx = 0, hl = 0;
        for (int t = 0; t < T; t++) {
            int c = CT[t]; int cp = pos[c]; int mv = S[mr * 6 + mc];
            int pr = ((cp / 6 - mv / 6) + 6) % 6, pc = ((cp % 6 - mv % 6) + 6) % 6;
            int p = S[pr * 6 + pc]; if (pt != null) pt[t] = p;
            int s = lmSym[p]; sc += L[hl + 1][ctx * K + s] - (s == 27 ? OtherPen : 0); if (hl < 4) { ctx = ctx * K + s; hl++; } else ctx = (ctx * K + s) % (K * K * K * K);
            int last = S[pr * 6 + 5]; for (int q = 5; q > 0; q--) { S[pr * 6 + q] = S[pr * 6 + q - 1]; pos[S[pr * 6 + q]] = pr * 6 + q; } S[pr * 6] = last; pos[last] = pr * 6;
            if (mr == pr) mc = (mc + 1) % 6;
            int y = pos[c] % 6;
            last = S[30 + y]; for (int q = 5; q > 0; q--) { S[q * 6 + y] = S[(q - 1) * 6 + y]; pos[S[q * 6 + y]] = q * 6 + y; } S[y] = last; pos[last] = y;
            if (mc == y) mr = (mr + 1) % 6;
            mr = (mr + c / 6) % 6; mc = (mc + c % 6) % 6;
        }
        return sc;
    }

    static void Main(string[] a) {
        string ct = a[0], tp = a[1]; int R = int.Parse(a[2]); long iters = long.Parse(a[3]);
        var ci = System.Globalization.CultureInfo.InvariantCulture; double T0 = double.Parse(a[4], ci), T1 = double.Parse(a[5], ci); int seed0 = a.Length > 6 ? int.Parse(a[6]) : 1;
        for (int n = 1; n <= 5; n++) { var qb = File.ReadAllBytes("lmsp/lp" + n + ".bin"); L[n] = new float[qb.Length / 4]; Buffer.BlockCopy(qb, 0, L[n], 0, qb.Length); }
        for (int i = 0; i < 36; i++) { char ch = AL[i]; lmSym[i] = ch >= 'a' && ch <= 'z' ? ch - 'a' : (ch == '_' ? 26 : 27); }
        CT = ct.Select(ch => AL.IndexOf(ch)).ToArray(); T = CT.Length;
        tmpl = tp.Select(ch => ch == '?' ? -1 : AL.IndexOf(ch)).ToArray();
        unkCells = Enumerable.Range(0, 36).Where(q => tmpl[q] < 0).ToArray();
        var unkChars = Enumerable.Range(0, 36).Where(v => !tmpl.Contains(v)).ToArray();
        var res = new Tuple<double, int[]>[R];
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 22 }, ri => {
            var r = new Random(seed0 * 7919 + ri);
            var key = (int[])tmpl.Clone(); var sh = unkChars.OrderBy(x => r.Next()).ToArray();
            for (int q = 0; q < unkCells.Length; q++) key[unkCells[q]] = sh[q];
            double cur = Decrypt(key, null), best = cur; int[] bk = (int[])key.Clone();
            for (long it = 0; it < iters; it++) {
                double Tt = T0 * Math.Pow(T1 / T0, (double)it / iters);
                int u1 = unkCells[r.Next(unkCells.Length)], u2 = unkCells[r.Next(unkCells.Length)]; if (u1 == u2) continue;
                int x = key[u1]; key[u1] = key[u2]; key[u2] = x;
                double sc = Decrypt(key, null);
                if (sc >= cur || r.NextDouble() < Math.Exp((sc - cur) / Tt)) { cur = sc; if (cur > best) { best = cur; bk = (int[])key.Clone(); } }
                else { x = key[u1]; key[u1] = key[u2]; key[u2] = x; }
            }
            res[ri] = Tuple.Create(best, bk);
        });
        foreach (var t in res.OrderByDescending(x => x.Item1).Take(6)) {
            var pt = new int[T]; Decrypt(t.Item2, pt);
            Console.WriteLine("{0:F1} key={1} pt={2}", t.Item1, new string(t.Item2.Select(v => AL[v]).ToArray()), new string(pt.Select(v => AL[v]).ToArray()));
        }
        Console.WriteLine("all: " + string.Join(" ", res.Select(x => x.Item1.ToString("F0"))));
    }
}
