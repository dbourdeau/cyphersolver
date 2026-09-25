// ASAC Part 3 (even L), stage 2: y columns placed with the odd-class PRNG; then brute force the 5 even-class PRNG digits
// (px[0,2,4,6,8]) with precomputed per-(column, position, offset, x-class, digit) tables and a greedy assignment of the
// x columns; rebuild the stream; solve the square with the German 5-gram; check rand() consistency.
// usage: Asac3d cipher.txt L v10 pxodd5
class Asac3d {
    static double[] PD = new double[100];
    static int[] Kfull(int[] v, int[] px) { var k = new int[100]; for (int x = 0; x < 10; x++) for (int y = 0; y < 10; y++) k[x + 10 * y] = (x + v[((y - px[x]) % 10 + 10) % 10]) % 10; return k; }
    static void Main(string[] a) {
        AsacCore.Load("../lmde");
        AsacY.C = File.ReadAllText(a[0]).Where(char.IsDigit).Select(ch => ch - '0').ToArray(); AsacY.N = AsacY.C.Length; AsacY.NI = AsacY.N / 2; AsacY.InitRand(AsacY.NI);
        var C = AsacY.C; int N = AsacY.N, NI = AsacY.NI; int L = int.Parse(a[1]);
        var v = a[2].Select(ch => ch - '0').ToArray(); var pxo = a[3].Select(ch => ch - '0').ToArray();
        var pdv = File.ReadAllText("pd.txt").Split(' ').Select(double.Parse).ToArray(); for (int i = 0; i < 100; i++) PD[i] = Math.Log10(pdv[i] / 0.01);
        var px = new int[10]; for (int i = 0; i < 5; i++) px[2 * i + 1] = pxo[i];
        var k = Kfull(v, px); var s = AsacY.MakeL(L);
        // stage A
        var cand = new List<Tuple<double, int, int, int>>();
        for (int A = 0; A < L; A++) for (int c = 1; c < L; c += 2) for (int o = s.oLo[A]; o <= s.oHi[A]; o++) { double sc = AsacY.ColScore(s, k, A, c, o); if (sc > -1e9) cand.Add(Tuple.Create(sc, A, c, o)); }
        var posOf = Enumerable.Repeat(-1, L).ToArray(); var offOf = new int[L]; var colAt = Enumerable.Repeat(-1, L).ToArray(); int need = L / 2;
        foreach (var t in cand.OrderByDescending(t => t.Item1)) { if (need == 0) break; if (posOf[t.Item2] >= 0 || colAt[t.Item3] >= 0) continue; posOf[t.Item2] = t.Item3; offOf[t.Item2] = t.Item4; colAt[t.Item3] = t.Item2; need--; }
        Console.WriteLine("y columns: " + string.Join(" ", Enumerable.Range(0, L).Where(A => posOf[A] >= 0).Select(A => A + "@" + posOf[A] + "/" + offOf[A])));
        var xcols = Enumerable.Range(0, L).Where(A => posOf[A] < 0).ToArray(); var xpos = Enumerable.Range(0, L / 2).Select(i => 2 * i).ToArray(); int M = xcols.Length;
        // tables T[ai][ci][oi][xclass 0..4][digit] for each offset
        var offs = xcols.Select(A => Enumerable.Range(s.oLo[A], s.oHi[A] - s.oLo[A] + 1).ToArray()).ToArray();
        var T = new double[M][][];
        Parallel.For(0, M, ai => {
            int A = xcols[ai]; T[ai] = new double[xpos.Length][];
            for (int ci = 0; ci < xpos.Length; ci++) {
                int c = xpos[ci]; int yc = colAt[c + 1], yo = offOf[yc]; int len = c < s.Lg ? s.H : s.H - 1;
                T[ai][ci] = new double[offs[ai].Length * 50];
                for (int oi = 0; oi < offs[ai].Length; oi++) {
                    int o = offs[ai][oi]; if (o + len > N) { for (int z = 0; z < 50; z++) T[ai][ci][oi * 50 + z] = -1e6; continue; }
                    for (int r = 0; r < len; r++) {
                        int p = c + r * L, i = p >> 1; if (i >= NI) continue;
                        int q = p % 100, xq = q % 10, yq = q / 10;
                        int y = ((C[yo + r] - k[(p + 1) % 100]) % 10 + 10) % 10; int ri = AsacY.EY[i] * 10 + AsacY.EX[i];
                        for (int d = 0; d < 10; d++) {
                            int kq = (xq + v[((yq - d) % 10 + 10) % 10]) % 10; int x = ((C[o + r] - kq) % 10 + 10) % 10;
                            T[ai][ci][oi * 50 + (xq / 2) * 10 + d] += PD[((x + 10 * y - ri) % 100 + 100) % 100];
                        }
                    }
                }
            }
        });
        // brute force px even
        var top = new List<Tuple<double, int>>(); object lk = new object();
        Parallel.For(0, 100000, new ParallelOptions { MaxDegreeOfParallelism = 16 }, combo => {
            int[] d = { combo % 10, combo / 10 % 10, combo / 100 % 10, combo / 1000 % 10, combo / 10000 % 10 };
            var best = new double[M * xpos.Length];
            for (int ai = 0; ai < M; ai++) for (int ci = 0; ci < xpos.Length; ci++) {
                double b = double.NegativeInfinity; var tt = T[ai][ci];
                for (int oi = 0; oi < offs[ai].Length; oi++) { double sum = tt[oi * 50 + d[0]] + tt[oi * 50 + 10 + d[1]] + tt[oi * 50 + 20 + d[2]] + tt[oi * 50 + 30 + d[3]] + tt[oi * 50 + 40 + d[4]]; if (sum > b) b = sum; }
                best[ai * xpos.Length + ci] = b;
            }
            // greedy assignment
            var idx = Enumerable.Range(0, best.Length).OrderByDescending(z => best[z]).ToArray();
            var ua = new bool[M]; var uc = new bool[xpos.Length]; double tot = 0; int n = 0;
            foreach (int z in idx) { int ai = z / xpos.Length, ci = z % xpos.Length; if (ua[ai] || uc[ci]) continue; ua[ai] = uc[ci] = true; tot += best[z]; if (++n == Math.Min(M, xpos.Length)) break; }
            lock (lk) { top.Add(Tuple.Create(tot, combo)); if (top.Count > 2000) { top = top.OrderByDescending(t => t.Item1).Take(50).ToList(); } }
        });
        top = top.OrderByDescending(t => t.Item1).Take(8).ToList();
        foreach (var t in top) Console.WriteLine("px even {0}{1}{2}{3}{4} total {5:F1}", t.Item2 % 10, t.Item2 / 10 % 10, t.Item2 / 100 % 10, t.Item2 / 1000 % 10, t.Item2 / 10000 % 10, t.Item1);
        // commit the best
        int bc = top[0].Item2; int[] dd = { bc % 10, bc / 10 % 10, bc / 100 % 10, bc / 1000 % 10, bc / 10000 % 10 };
        for (int i = 0; i < 5; i++) px[2 * i] = dd[i]; k = Kfull(v, px);
        var bl = new List<Tuple<double, int, int, int>>();
        for (int ai = 0; ai < M; ai++) for (int ci = 0; ci < xpos.Length; ci++) for (int oi = 0; oi < offs[ai].Length; oi++) {
            var tt = T[ai][ci]; double sum = 0; for (int xc = 0; xc < 5; xc++) sum += tt[oi * 50 + xc * 10 + dd[xc]]; bl.Add(Tuple.Create(sum, ai, ci, offs[ai][oi]));
        }
        foreach (var t in bl.OrderByDescending(t => t.Item1)) { int A = xcols[t.Item2], c = xpos[t.Item3]; if (posOf[A] >= 0 || colAt[c] >= 0) continue; posOf[A] = c; offOf[A] = t.Item4; colAt[c] = A; }
        Console.WriteLine("order " + string.Join(" ", posOf));
        var St = new int[N]; int off = 0; bool offOk = true;
        for (int A = 0; A < L; A++) { if (off != offOf[A]) offOk = false; for (int p = posOf[A]; p < N; p += L) St[p] = C[off++]; }
        Console.WriteLine("offsets consistent: {0}  px {1} v {2}", offOk, string.Join("", px), string.Join("", v));
        var cells = new int[NI]; for (int i = 0; i < NI; i++) { int p = 2 * i; cells[i] = ((St[p] - k[p % 100]) % 10 + 10) % 10 + 10 * (((St[p + 1] - k[(p + 1) % 100]) % 10 + 10) % 10); }
        File.WriteAllText("cells_" + Path.GetFileNameWithoutExtension(a[0]) + ".txt", string.Join(" ", cells));
        File.WriteAllText("order_" + Path.GetFileNameWithoutExtension(a[0]) + ".txt", string.Join(" ", posOf) + "\npx " + string.Join("", px) + " v " + string.Join("", v));
        // square
        var res = new List<Tuple<double, int[]>>();
        Parallel.For(0, 16, r => {
            var rng = new Random(r * 101 + 7); var buf = new int[NI];
            var q2 = new int[20]; for (int i = 0; i < 20; i++) q2[i] = rng.Next(10);
            Func<int[], double> ev = q => { var sq = AsacCore.SquareSyms(q.Take(10).ToArray(), q.Skip(10).ToArray()); for (int i = 0; i < NI; i++) buf[i] = sq[cells[i]]; return AsacCore.ScoreSyms(buf, NI); };
            double c0 = ev(q2), best = c0; var bk = (int[])q2.Clone(); double T0 = NI * 0.002;
            for (int it = 0; it < 200000; it++) {
                double Tm = T0 * Math.Pow(0.005, it / 200000.0);
                int i1 = rng.Next(20), o1 = q2[i1]; q2[i1] = (o1 + 1 + rng.Next(9)) % 10; double f = ev(q2);
                if (f >= c0 || rng.NextDouble() < Math.Exp((f - c0) / Tm)) { c0 = f; if (c0 > best) { best = c0; bk = (int[])q2.Clone(); } } else q2[i1] = o1;
            }
            lock (lk) res.Add(Tuple.Create(best, bk));
        });
        foreach (var b in res.OrderByDescending(x => x.Item1).Take(2)) {
            var sqc = AsacCore.SquareChars(b.Item2.Take(10).ToArray(), b.Item2.Skip(10).ToArray());
            int ok = 0; for (int i = 0; i < NI; i++) { int r = AsacY.EY[i] * 10 + AsacY.EX[i]; char ch = sqc[cells[i]]; int m = 0; while (sqc[(r + m) % 100] != ch) m++; if ((r + m) % 100 == cells[i]) ok++; }
            Console.WriteLine("square {0} LM {1:F1} ({2:F2}/char) rand-consistent {3}/{4}", string.Join("", b.Item2), b.Item1, b.Item1 / NI, ok, NI);
            Console.WriteLine(new string(cells.Select(c => sqc[c]).ToArray()));
        }
    }
}
