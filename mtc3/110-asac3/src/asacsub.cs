// ASAC substitution-stage solver: Polybius square shifts (20 digits) + PRNG square shifts (20 digits), annealed with a
// 28-symbol German 5-gram model (lmde/). Input: a digit stream as it was after step 2 (transposition already undone).
// usage: AsacSub digits.txt mode restarts iters [fixed key "sqX sqY prX prY" as 40 digits or -]
//   mode 1 = square only; 2 = square + periodic PRNG; 5 = square + PRNG re-rotated every 100 digits
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

public class AsacCore {
    public static float[][] L = new float[6][]; public const int K = 28; public static int K4 = K * K * K * K;
    public static char[] INIT = new char[100];
    public static void Load(string dir) {
        for (int n = 1; n <= 5; n++) { var b = File.ReadAllBytes(dir + "/lp" + n + ".bin"); L[n] = new float[b.Length / 4]; Buffer.BlockCopy(b, 0, L[n], 0, b.Length); }
        var d = new List<char>(); for (int i = 0; i < 10; i++) d.Add((char)('0' + i)); char e = '[';
        while (d.Count < 100) { int c = "AIOU".IndexOf(e) >= 0 ? 2 : (e == 'E' ? 4 : 1); for (int q = 0; q < c && d.Count < 100; q++) d.Add(e == '[' ? ' ' : e); e++; if (e == '\\') e = 'A'; }
        INIT = d.ToArray();
    }
    public static int Sym(char c) { return c == ' ' ? 26 : (c >= '0' && c <= '9' ? 27 : c - 'A'); }
    // generic transpose of a 100-cell array of ints
    public static int[] Transpose(int[] data, int[] sX, int[] sY) {
        var d = new int[100]; var t = new int[100];
        for (int y = 0; y < 10; y++) for (int x = 0; x < 10; x++) t[x + 10 * y] = data[((x - sY[y] + 10) % 10) + 10 * y];
        for (int x = 0; x < 10; x++) for (int y = 0; y < 10; y++) d[x + 10 * y] = t[x + 10 * ((y - sX[x] + 10) % 10)];
        return d;
    }
    public static int[] SquareSyms(int[] sX, int[] sY) { return Transpose(INIT.Select(Sym).ToArray(), sX, sY); }
    public static char[] SquareChars(int[] sX, int[] sY) { var idx = Transpose(Enumerable.Range(0, 100).ToArray(), sX, sY); return idx.Select(i => INIT[i]).ToArray(); }
    public static int[][] Keystream(int[] pX, int[] pY, int blocks) {
        var ks = new int[blocks][]; var cur = Enumerable.Range(0, 100).Select(n => n % 10).ToArray();
        for (int b = 0; b < blocks; b++) { cur = Transpose(cur, pX, pY); ks[b] = cur; }
        return ks;
    }
    public static double ScoreSyms(int[] s, int n) {
        double sc = 0; int h = 0, hl = 0;
        for (int i = 0; i < n; i++) { int c = s[i]; sc += L[hl + 1][h * K + c]; if (hl < 4) { h = h * K + c; hl++; } else h = (h * K + c) % K4; }
        return sc;
    }
}

class AsacSub {
    static int[] D; static int N, NP, MODE;
    static double Eval(int[] key, int[] buf) {
        var sq = AsacCore.SquareSyms(key.Take(10).ToArray(), key.Skip(10).Take(10).ToArray());
        int blocks = MODE == 5 ? (N + 99) / 100 : 1;
        int[][] ks = MODE == 1 ? null : AsacCore.Keystream(key.Skip(20).Take(10).ToArray(), key.Skip(30).Take(10).ToArray(), blocks);
        for (int i = 0; i < NP; i++) {
            int p = 2 * i; int x = D[p], y = D[p + 1];
            if (ks != null) { var k0 = ks[MODE == 5 ? p / 100 : 0]; x = (x - k0[p % 100] + 10) % 10; var k1 = ks[MODE == 5 ? (p + 1) / 100 : 0]; y = (y - k1[(p + 1) % 100] + 10) % 10; }
            buf[i] = sq[x + 10 * y];
        }
        return AsacCore.ScoreSyms(buf, NP);
    }
    public static string Decrypt(int[] key) {
        var sq = AsacCore.SquareChars(key.Take(10).ToArray(), key.Skip(10).Take(10).ToArray());
        int blocks = MODE == 5 ? (N + 99) / 100 : 1;
        int[][] ks = MODE == 1 ? null : AsacCore.Keystream(key.Skip(20).Take(10).ToArray(), key.Skip(30).Take(10).ToArray(), blocks);
        var sb = new System.Text.StringBuilder();
        for (int i = 0; i < NP; i++) {
            int p = 2 * i; int x = D[p], y = D[p + 1];
            if (ks != null) { x = (x - ks[MODE == 5 ? p / 100 : 0][p % 100] + 10) % 10; y = (y - ks[MODE == 5 ? (p + 1) / 100 : 0][(p + 1) % 100] + 10) % 10; }
            sb.Append(sq[x + 10 * y]);
        }
        return sb.ToString();
    }
    static void Main(string[] a) {
        AsacCore.Load("../lmde");
        D = File.ReadAllText(a[0]).Where(char.IsDigit).Select(c => c - '0').ToArray(); N = D.Length; NP = N / 2;
        MODE = int.Parse(a[1]); int R = int.Parse(a[2]); long iters = long.Parse(a[3]);
        int nk = MODE == 1 ? 20 : 40;
        if (a.Length > 4 && a[4] != "-") { var k = a[4].Select(c => c - '0').ToArray(); Console.WriteLine("score {0:F1}", Eval(k, new int[NP])); Console.WriteLine(Decrypt(k)); return; }
        var res = new List<Tuple<double, int[]>>(); object lk = new object();
        Parallel.For(0, R, new ParallelOptions { MaxDegreeOfParallelism = 16 }, r => {
            var rng = new Random(r * 7919 + 1); var buf = new int[NP];
            var key = new int[40]; for (int i = 0; i < nk; i++) key[i] = rng.Next(10);
            double cur = Eval(key, buf), best = cur; var bk = (int[])key.Clone();
            double T0 = 0.02 * NP / 10;  // temperature scale in log10 units
            for (long it = 0; it < iters; it++) {
                double T = T0 * Math.Pow(0.005, (double)it / iters);
                int i1 = rng.Next(nk), o1 = key[i1]; key[i1] = (o1 + 1 + rng.Next(9)) % 10;
                int i2 = -1, o2 = 0; if (rng.Next(3) == 0) { i2 = rng.Next(nk); if (i2 != i1) { o2 = key[i2]; key[i2] = (o2 + 1 + rng.Next(9)) % 10; } else i2 = -1; }
                double v = Eval(key, buf);
                if (v >= cur || rng.NextDouble() < Math.Exp((v - cur) / T)) { cur = v; if (cur > best) { best = cur; bk = (int[])key.Clone(); } }
                else { key[i1] = o1; if (i2 >= 0) key[i2] = o2; }
            }
            lock (lk) { res.Add(Tuple.Create(best, bk)); Console.WriteLine("restart {0}: {1:F1} {2}", r, best, string.Join("", bk.Take(nk))); }
        });
        var top = res.OrderByDescending(t => t.Item1).First();
        Console.WriteLine("BEST {0:F1} key {1}", top.Item1, string.Join("", top.Item2.Take(nk)));
        Console.WriteLine(Decrypt(top.Item2));
    }
}
