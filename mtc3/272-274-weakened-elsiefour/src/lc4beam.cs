// Beam-search state recovery for (weakened, nonce-free) LC4 with a partly known key.
// Unknown key cells are filled lazily while decrypting; an English char 5-gram LM (space = '_') ranks hypotheses.
// usage: Lc4Beam ciphertext keytemplate(36 chars, '?' unknown) B [topN] [markerRow markerCol]
using System;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;

class Lc4Beam {
    const string AL = "#_23456789abcdefghijklmnopqrstuvwxyz";
    static float[][] L = new float[6][]; const int K = 28;
    static int[] lmSym = new int[36];
    static int T; static int[] CT; static int B; static float OtherPen = float.Parse(Environment.GetEnvironmentVariable("OTHERPEN") ?? "2.0", System.Globalization.CultureInfo.InvariantCulture); static byte[][] trueStates;

    struct Hyp { public ulong placed; public byte mr, mc, hl; public int ctx; public float score; }
    static byte[] keys, nkeys; static byte[] pts, npts; static Hyp[] hy, nhy; static int nh;

    static float LP(int ctx, int hl, int s) { return L[hl + 1][ctx * K + s] - (s == 27 ? OtherPen : 0); }

    // enumerate children of hypothesis h for ciphertext char c; callback(score, choice)
    // choice packing: cpCell | (mchar+1)<<6 | (pchar+1)<<12  (0 means "no placement")
    static void Enum(int h, int c, Action<float, int> emit) {
        var H = hy[h]; int kb = h * 36; byte[] k = keys;
        int cpFixed = -1;
        if (((H.placed >> c) & 1) != 0) { for (int q = 0; q < 36; q++) if (k[kb + q] == c) { cpFixed = q; break; } }
        for (int cp = 0; cp < 36; cp++) {
            if (cpFixed >= 0) { if (cp != cpFixed) continue; } else if (k[kb + cp] != 255) continue;
            ulong pl1 = H.placed | (1UL << c);
            int m = H.mr * 6 + H.mc;
            int mv0 = m == cp ? c : k[kb + m];
            for (int mv = 0; mv < 36; mv++) {
                int mplace = 0;
                if (mv0 != 255) { if (mv != mv0) continue; } else { if (((pl1 >> mv) & 1) != 0) continue; mplace = mv + 1; }
                ulong pl2 = mplace > 0 ? pl1 | (1UL << mv) : pl1;
                int pr = ((cp / 6 - mv / 6) % 6 + 6) % 6, pc = ((cp % 6 - mv % 6) % 6 + 6) % 6; int pp = pr * 6 + pc;
                int pv0 = pp == cp ? c : (pp == m && mplace > 0 ? mv : k[kb + pp]);
                for (int pv = 0; pv < 36; pv++) {
                    int pplace = 0;
                    if (pv0 != 255) { if (pv != pv0) continue; } else { if (((pl2 >> pv) & 1) != 0) continue; pplace = pv + 1; }
                    float sc = H.score + LP(H.ctx, H.hl, lmSym[pv]);
                    emit(sc, cp | (mplace << 6) | (pplace << 12));
                }
            }
        }
    }

    static void Apply(int h, int c, int choice, int dst, int step) {
        var H = hy[h]; int kb = h * 36, db = dst * 36;
        Array.Copy(keys, kb, nkeys, db, 36); Array.Copy(pts, h * T, npts, dst * T, T);
        byte[] k = nkeys; ulong placed = H.placed;
        int cp = choice & 63, mplace = (choice >> 6) & 63, pplace = (choice >> 12) & 63;
        if (k[db + cp] == 255) { k[db + cp] = (byte)c; placed |= 1UL << c; }
        int m = H.mr * 6 + H.mc;
        if (mplace > 0) { k[db + m] = (byte)(mplace - 1); placed |= 1UL << (mplace - 1); }
        int mv = k[db + m];
        int pr = ((cp / 6 - mv / 6) % 6 + 6) % 6, pc = ((cp % 6 - mv % 6) % 6 + 6) % 6; int pp = pr * 6 + pc;
        if (pplace > 0) { k[db + pp] = (byte)(pplace - 1); placed |= 1UL << (pplace - 1); }
        int p = k[db + pp];
        npts[dst * T + step] = (byte)p;
        int mr = H.mr, mc = H.mc;
        // rotate row pr right by 1
        byte last = k[db + pr * 6 + 5]; for (int q = 5; q > 0; q--) k[db + pr * 6 + q] = k[db + pr * 6 + q - 1]; k[db + pr * 6] = last;
        if (mr == pr) mc = (mc + 1) % 6;
        int ncp = -1; for (int q = 0; q < 36; q++) if (k[db + q] == c) { ncp = q; break; }
        int y = ncp % 6;
        last = k[db + 30 + y]; for (int q = 5; q > 0; q--) k[db + q * 6 + y] = k[db + (q - 1) * 6 + y]; k[db + y] = last;
        if (mc == y) mr = (mr + 1) % 6;
        mr = (mr + c / 6) % 6; mc = (mc + c % 6) % 6;
        int s = lmSym[p]; int ctx = H.ctx, hl = H.hl;
        if (hl < 4) { ctx = ctx * K + s; hl++; } else ctx = (ctx * K + s) % (K * K * K * K);
        nhy[dst] = new Hyp { placed = placed, mr = (byte)mr, mc = (byte)mc, hl = (byte)hl, ctx = ctx, score = H.score + LP(H.ctx, H.hl, s) };
    }

    static void Main(string[] a) {
        string ct = a[0]; string tmpl = a[1]; B = int.Parse(a[2]); int topN = a.Length > 3 ? int.Parse(a[3]) : 10;
        int mr0 = a.Length > 5 ? int.Parse(a[4]) : 0, mc0 = a.Length > 5 ? int.Parse(a[5]) : 0;
        for (int n = 1; n <= 5; n++) { var qb = File.ReadAllBytes("lmsp/lp" + n + ".bin"); L[n] = new float[qb.Length / 4]; Buffer.BlockCopy(qb, 0, L[n], 0, qb.Length); }
        for (int i = 0; i < 36; i++) { char ch = AL[i]; lmSym[i] = ch >= 'a' && ch <= 'z' ? ch - 'a' : (ch == '_' ? 26 : 27); }
        CT = ct.Select(ch => AL.IndexOf(ch)).ToArray(); T = CT.Length;
        keys = new byte[(long)B * 36]; nkeys = new byte[(long)B * 36]; pts = new byte[(long)B * T]; npts = new byte[(long)B * T];
        hy = new Hyp[B]; nhy = new Hyp[B];
        ulong pl = 0; for (int i = 0; i < 36; i++) { if (tmpl[i] == '?') keys[i] = 255; else { keys[i] = (byte)AL.IndexOf(tmpl[i]); pl |= 1UL << keys[i]; } }
        hy[0] = new Hyp { placed = pl, mr = (byte)mr0, mc = (byte)mc0 }; nh = 1;
        string tk = Environment.GetEnvironmentVariable("TRUEKEY");
        if (tk != null) {
            trueStates = new byte[T + 1][]; var S = tk.Select(ch => (byte)AL.IndexOf(ch)).ToArray(); int mr = mr0, mc = mc0; trueStates[0] = (byte[])S.Clone();
            for (int t = 0; t < T; t++) {
                int c = CT[t]; int cp = Array.IndexOf(S, (byte)c); int mv = S[mr * 6 + mc];
                int pr = ((cp / 6 - mv / 6) + 6) % 6, pc = ((cp % 6 - mv % 6) + 6) % 6;
                byte last = S[pr * 6 + 5]; for (int q = 5; q > 0; q--) S[pr * 6 + q] = S[pr * 6 + q - 1]; S[pr * 6] = last; if (mr == pr) mc = (mc + 1) % 6;
                int y = Array.IndexOf(S, (byte)c) % 6; last = S[30 + y]; for (int q = 5; q > 0; q--) S[q * 6 + y] = S[(q - 1) * 6 + y]; S[y] = last; if (mc == y) mr = (mr + 1) % 6;
                mr = (mr + c / 6) % 6; mc = (mc + c % 6) % 6; trueStates[t + 1] = (byte[])S.Clone();
            }
        }
        for (int step = 0; step < T; step++) {
            int c = CT[step];
            // pass 1: max & histogram
            float mx = float.NegativeInfinity; object lk = new object(); long total = 0;
            Parallel.For(0, nh, () => new float[] { float.NegativeInfinity, 0 }, (h, st, loc) => { Enum(h, c, (sc, ch) => { if (sc > loc[0]) loc[0] = sc; loc[1]++; }); return loc; },
                loc => { lock (lk) { if (loc[0] > mx) mx = loc[0]; total += (long)loc[1]; } });
            const int NB = 4000; const float span = 40f; var hist = new long[NB + 1];
            Parallel.For(0, nh, () => new long[NB + 1], (h, st, loc) => { Enum(h, c, (sc, ch) => { int bi = (int)((mx - sc) / span * NB); if (bi > NB) bi = NB; loc[bi]++; }); return loc; },
                loc => { lock (lk) { for (int q = 0; q <= NB; q++) hist[q] += loc[q]; } });
            long acc = 0; int cut = NB; for (int q = 0; q <= NB; q++) { acc += hist[q]; if (acc >= B) { cut = q; break; } }
            float thr = acc >= B ? mx - (cut + 1) * span / NB : float.NegativeInfinity;
            var bag = new System.Collections.Concurrent.ConcurrentBag<List<Tuple<float, int, int>>>();
            Parallel.For(0, nh, () => new List<Tuple<float, int, int>>(), (h, st, loc) => { Enum(h, c, (sc, ch) => { if (sc >= thr) loc.Add(Tuple.Create(sc, h, ch)); }); return loc; }, loc => bag.Add(loc));
            var all = bag.SelectMany(x => x).ToList();
            if (all.Count > B) all = all.OrderByDescending(x => x.Item1).Take(B).ToList();
            for (int q = 0; q < all.Count; q++) Apply(all[q].Item2, c, all[q].Item3, q, step);
            nh = all.Count;
            var t1 = keys; keys = nkeys; nkeys = t1; var t2 = pts; pts = npts; npts = t2; var t3 = hy; hy = nhy; nhy = t3;
            if (step % 2 == 0 || step == T - 1) {
                int best = 0; for (int h = 1; h < nh; h++) if (hy[h].score > hy[best].score) best = h;
                string tr = "";
                if (trueStates != null) {
                    var ts = trueStates[step + 1]; int th = -1;
                    for (int h = 0; h < nh && th < 0; h++) { bool ok = true; for (int q = 0; q < 36 && ok; q++) { byte v = keys[h * 36 + q]; if (v != 255 && v != ts[q]) ok = false; } if (ok) th = h; }
                    if (th >= 0) { int rank = 0; for (int h = 0; h < nh; h++) if (hy[h].score > hy[th].score) rank++; tr = string.Format(" TRUE rank {0} score {1:F1}", rank, hy[th].score); } else tr = " TRUE lost";
                }
                Console.WriteLine("step {0} children {1} beam {2} best {3:F1}{5} {4}", step, total, nh, hy[best].score, new string(Enumerable.Range(0, step + 1).Select(q => AL[pts[best * T + q]]).ToArray()), tr);
            }
        }
        var ord = Enumerable.Range(0, nh).OrderByDescending(h => hy[h].score).Take(topN);
        foreach (int h in ord) {
            string pt = new string(Enumerable.Range(0, T).Select(q => AL[pts[h * T + q]]).ToArray());
            // key at END state is not the initial key; print plaintext and score
            Console.WriteLine("{0:F1} {1}", hy[h].score, pt);
        }
    }
}
