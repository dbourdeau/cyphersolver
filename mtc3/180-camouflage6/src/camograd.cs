// Camouflage cipher: grow ONE piece letter by letter (English frequency order), scoring each partial group with a
// 5-gram model of English restricted to the letters chosen so far (other letters deleted). Beam search over stages.
// usage: CamoGrad cipher.bin corpus.txt beam kmax [truekey.bin] [exclude.txt] [out.txt]
using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

class CamoGrad {
    static string ORDER = Environment.GetEnvironmentVariable("ORDER") ?? "ETAOINSHRDLCUMWFGYPBVKJXQZ";
    static int[] C; static int N; static int[] syms; static int[] cnt = new int[256];
    static byte[] corpus; // letters 0..25
    static float[][] LM; static float[][] UNI; // per stage k: LM over k-letter alphabet (order 5), unigram
    static int[] Pow;

    static void BuildLM(int k) {
        // map letters: ORDER[i] -> i for i<k, else deleted
        var map = new int[26]; for (int i = 0; i < 26; i++) map[i] = -1; for (int i = 0; i < k; i++) map[ORDER[i] - 'A'] = i;
        var seq = new List<byte>(corpus.Length); foreach (byte b in corpus) { int m = map[b]; if (m >= 0) seq.Add((byte)m); }
        var s = seq.ToArray(); int n = s.Length;
        // counts for orders 1..5
        double[][] cntn = new double[6][];
        for (int o = 1; o <= 5; o++) {
            int size = 1; for (int q = 0; q < o; q++) size *= k; cntn[o] = new double[size];
            int h = 0, mod = size / k;
            for (int i = 0; i < n; i++) { h = (h % Math.Max(1, mod)) * k + s[i]; if (o == 1) h = s[i]; if (i >= o - 1) cntn[o][h]++; }
        }
        var uni = new float[k]; double tot = cntn[1].Sum(); for (int a = 0; a < k; a++) uni[a] = (float)Math.Log10((cntn[1][a] + 1) / (tot + k));
        UNI[k] = uni;
        // interpolated absolute discounting, recursively; P[o] over contexts of length o-1
        double[] prev = new double[k]; for (int a = 0; a < k; a++) prev[a] = (cntn[1][a] + 1) / (tot + k);
        double D = 0.75;
        for (int o = 2; o <= 5; o++) {
            int nctx = cntn[o].Length / k; var P = new double[cntn[o].Length]; int lowMod = nctx / k;
            for (int ctx = 0; ctx < nctx; ctx++) {
                double ch = 0; int tp = 0; for (int a = 0; a < k; a++) { double c = cntn[o][ctx * k + a]; ch += c; if (c > 0) tp++; }
                int low = lowMod > 0 ? ctx % lowMod : 0; // drop oldest letter
                for (int a = 0; a < k; a++) {
                    double lo = prev[low * k + a];
                    P[ctx * k + a] = ch < 5 ? lo : Math.Max(cntn[o][ctx * k + a] - D, 0) / ch + D * tp / ch * lo;
                }
            }
            prev = P;
        }
        LM[k] = prev.Select(x => (float)Math.Log10(x)).ToArray();
    }

    // score (LLR vs unigram) of subsequence of symbols with letter assignment lt (symbol -> letter index or -1)
    static double Score(int[] lt, int k) {
        var L = LM[k]; var U = UNI[k]; int mod = Pow[4] / 1; // context of 4 letters
        double sc = 0; int h = 0, hl = 0; int k4 = k * k * k * k;
        for (int i = 0; i < N; i++) {
            int a = lt[C[i]]; if (a < 0) continue;
            if (hl == 4) sc += L[h * k + a] - U[a];
            else { // short context: pad by using unigram only for first letters
                sc += 0;
            }
            if (hl < 4) { h = h * k + a; hl++; } else h = (h * k + a) % k4;
        }
        return sc;
    }

    static void Show(int[] h, byte[] tk) {
        var lt = new int[256]; for (int q = 0; q < 256; q++) lt[q] = -1; for (int q = 0; q < h.Length; q++) if (h[q] >= 0) lt[h[q]] = q;
        var sb = new System.Text.StringBuilder(); foreach (int y in C) if (lt[y] >= 0) sb.Append(ORDER[lt[y]]);
        Console.WriteLine("k={0} score {1:F1} {2} || {3}", h.Length, Score(lt, h.Length), string.Join(",", h.Select((y, q) => y + ":" + ORDER[q])), sb.ToString());
    }
    static double ScoreH(int[] h) {
        var lt = new int[256]; for (int q = 0; q < 256; q++) lt[q] = -1; for (int q = 0; q < h.Length; q++) if (h[q] >= 0) lt[h[q]] = q;
        return Score(lt, h.Length);
    }
    // hill-climb: for each letter slot try every unused symbol or null; accept improvements until none
    static int[] Refine(int[] h0, int k) {
        var h = (int[])h0.Clone(); double cur = ScoreH(h); bool improved = true;
        while (improved) {
            improved = false;
            for (int q = 0; q < k; q++) {
                var used = new HashSet<int>(h.Where(y => y >= 0));
                var opts = syms.Where(y => !used.Contains(y)).Concat(new[] { -1 }).ToArray();
                var res = new double[opts.Length];
                Parallel.For(0, opts.Length, i => { var hh = (int[])h.Clone(); hh[q] = opts[i]; res[i] = ScoreH(hh); });
                int bi = -1; double bv = cur + 1e-6; for (int i = 0; i < opts.Length; i++) if (res[i] > bv) { bv = res[i]; bi = i; }
                if (bi >= 0) { h[q] = opts[bi]; cur = bv; improved = true; }
            }
        }
        return h;
    }
    static void Main(string[] a) {
        C = File.ReadAllBytes(a[0]).Select(x => (int)x).ToArray();
        string corpusPath = a[1]; int B = int.Parse(a[2]); int kmax = int.Parse(a[3]);
        byte[] tk = a.Length > 4 && a[4] != "-" ? File.ReadAllBytes(a[4]) : null;
        var excl = new bool[256];
        if (a.Length > 5 && a[5] != "-") foreach (var w in File.ReadAllText(a[5]).Split(new[] { ',', ' ', '\n', '\r' }, StringSplitOptions.RemoveEmptyEntries)) excl[int.Parse(w)] = true;
        string outp = a.Length > 6 ? a[6] : "camograd_out.txt";
        C = C.Where(x => !excl[x]).ToArray(); N = C.Length;
        foreach (int y in C) cnt[y]++;
        syms = Enumerable.Range(0, 256).Where(y => cnt[y] > 0).ToArray();
        Console.WriteLine("N={0} symbols={1}", N, syms.Length);
        // corpus
        var txt = File.ReadAllText(corpusPath).ToUpperInvariant();
        corpus = txt.Where(ch => ch >= 'A' && ch <= 'Z').Select(ch => (byte)(ch - 'A')).ToArray();
        Console.WriteLine("corpus letters {0}", corpus.Length);
        LM = new float[27][]; UNI = new float[27][]; Pow = new int[6]; Pow[0] = 1; for (int q = 1; q < 6; q++) Pow[q] = Pow[q - 1] * 26;
        Parallel.For(2, kmax + 1, k => BuildLM(k));
        Console.WriteLine("LMs built");
        if (tk != null && Environment.GetEnvironmentVariable("TRUESCORE") != null) {
            for (int g = 0; g < 9; g++) {
                var line = new System.Text.StringBuilder("piece " + g + ":");
                for (int k = 2; k <= kmax; k++) {
                    var lt = new int[256]; for (int q = 0; q < 256; q++) lt[q] = -1; bool ok = true;
                    for (int q = 0; q < k; q++) { int y = Array.FindIndex(Enumerable.Range(0, 256).ToArray(), yy => cnt[yy] > 0 && tk[yy] == g * 26 + (ORDER[q] - 'A')); if (y < 0) { ok = false; break; } lt[y] = q; }
                    line.Append(ok ? string.Format(" {0:F1}", Score(lt, k)) : " -");
                }
                Console.WriteLine(line);
            }
            return;
        }
        string seed = Environment.GetEnvironmentVariable("SEED");
        if (seed != null) {
            var h = seed.Split(',').Select(t => int.Parse(t.Split(':')[0])).ToArray();
            int refK2 = int.Parse(Environment.GetEnvironmentVariable("REFINE_K") ?? "26");
            for (int k = 2; k <= refK2; k++) if (LM[k] == null) BuildLM(k);
            h = Refine(h, h.Length); Show(h, tk);
            for (int k = h.Length + 1; k <= refK2; k++) { var hx = new int[k]; Array.Copy(h, hx, h.Length); hx[k - 1] = -1; h = Refine(hx, k); Show(h, tk); }
            return;
        }
        // beam: each hypothesis = list of symbols (index = letter index in ORDER)
        var beam = new List<int[]> { new int[0] };
        for (int k = 1; k <= kmax; k++) {
            int kk = Math.Max(k, 2);
            var cand = new System.Collections.Concurrent.ConcurrentBag<Tuple<double, int[]>>();
            int minCnt = k <= 6 ? 4 : 1; // frequent letters need at least a few occurrences
            Parallel.ForEach(beam, h => {
                var lt = new int[256]; for (int q = 0; q < 256; q++) lt[q] = -1;
                for (int q = 0; q < h.Length; q++) if (h[q] >= 0) lt[h[q]] = q;
                var local = new List<Tuple<double, int[]>>();
                if (k >= 13) { var nh0 = new int[k]; Array.Copy(h, nh0, h.Length); nh0[k - 1] = -1; local.Add(Tuple.Create(Score(lt, k), nh0)); }
                foreach (int y in syms) {
                    if (lt[y] >= 0 || cnt[y] < minCnt) continue;
                    if (h.Length > 0 && ORDER.IndexOf(ORDER[k - 1]) >= 0 && k >= 2 && cnt[y] > cnt[h[0]] * 1.6 + 3) continue; // no letter far more frequent than E
                    lt[y] = k - 1;
                    double sc = k >= 2 ? Score(lt, k) : cnt[y];
                    lt[y] = -1;
                    var nh = new int[k]; Array.Copy(h, nh, h.Length); nh[k - 1] = y;
                    local.Add(Tuple.Create(sc, nh));
                }
                // keep only the local best few to limit memory
                foreach (var t in local.OrderByDescending(t => t.Item1).Take(Math.Max(50, B / 20))) cand.Add(t);
            });
            var all = cand.OrderByDescending(t => t.Item1).ToList();
            // dedupe: hypotheses with same symbol set in different letter order are different; keep as is
            beam = all.Take(B).Select(t => t.Item2).ToList();
            string trueInfo = "";
            if (tk != null) {
                int bestRank = -1; int piece = -1;
                for (int r = 0; r < all.Count && bestRank < 0; r++) {
                    var h = all[r].Item2; int g = tk[h[0]] / 26; bool ok = true;
                    for (int q = 0; q < h.Length && ok; q++) if (h[q] >= 0 && (tk[h[q]] / 26 != g || tk[h[q]] % 26 != ORDER[q] - 'A')) ok = false;
                    if (ok) { bestRank = r; piece = g; }
                }
                int pure = 0; foreach (var h in beam) { int g = tk[h[0]] / 26; if (h.All(y => y < 0 || tk[y] / 26 == g)) pure++; }
                trueInfo = string.Format(" | best true rank {0} (piece {1}) | pure-piece hyps in beam {2}/{3}", bestRank, piece, pure, beam.Count);
            }
            Console.WriteLine("stage {0} ({1}) cands {2} best {3:F1}{4}", k, ORDER.Substring(0, k), all.Count, all.Count > 0 ? all[0].Item1 : 0, trueInfo);
        }
        int refK = int.Parse(Environment.GetEnvironmentVariable("REFINE_K") ?? "0");
        if (refK > 0) {
            for (int k = kmax + 1; k <= refK; k++) if (LM[k] == null) BuildLM(k);
            var refined = new List<Tuple<double, int[]>>();
            foreach (var h0 in beam.Take(int.Parse(Environment.GetEnvironmentVariable("REFINE_N") ?? "5"))) {
                var h = Refine(h0, kmax);
                for (int k = kmax + 1; k <= refK; k++) { var hx = new int[k]; Array.Copy(h, hx, h.Length); hx[k - 1] = -1; h = Refine(hx, k); }
                refined.Add(Tuple.Create(ScoreH(h), h));
            }
            beam = refined.OrderByDescending(t => t.Item1).Select(t => t.Item2).ToList();
            if (tk != null) foreach (var h in beam) Console.WriteLine("refined: " + string.Join(" ", h.Select((y, q) => ORDER[q] + "->" + (y < 0 ? "-" : (tk[y] / 26) + "" + (char)('A' + tk[y] % 26)))));
        }
        using (var w = new StreamWriter(outp)) {
            foreach (var h in beam.Take(50)) {
                var lt = new int[256]; for (int q = 0; q < 256; q++) lt[q] = -1; for (int q = 0; q < h.Length; q++) if (h[q] >= 0) lt[h[q]] = q;
                var sb = new System.Text.StringBuilder(); foreach (int y in C) if (lt[y] >= 0) sb.Append(ORDER[lt[y]]);
                w.WriteLine("{0:F1} {1} | {2}", Score(lt, h.Length), string.Join(",", h.Select((y, q) => y + ":" + ORDER[q])), sb);
            }
        }
        Console.WriteLine(string.Join("\n", File.ReadAllLines(outp).Take(5).Select(l => l.Length > 300 ? l.Substring(0, 300) : l)));
    }
}
