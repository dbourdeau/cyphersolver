// Known-plaintext key recovery for nonce-free LC4: DFS over partial initial keys, with constraint propagation.
// usage: Lc4Kpa plaintext ciphertext [keytemplate] [maxSolutions]
using System;
using System.Linq;
using System.Collections.Generic;

class Lc4Kpa {
    const string AL = "#_23456789abcdefghijklmnopqrstuvwxyz";
    static int[] P, C; static int T; static long nodes = 0; static List<int[]> sols = new List<int[]>(); static int maxSol;

    // state: key0[36] initial-cell -> char (-1), cur[36] current cell -> initial cell id, where[36] char -> initial cell id (-1)
    static void Dfs(int t, int[] key0, int[] cur, int[] where, int mr, int mc) {
        nodes++;
        if (sols.Count >= maxSol) return;
        if (t == T) { sols.Add((int[])key0.Clone()); return; }
        int c = C[t], p = P[t];
        int mcell = mr * 6 + mc; int mid = cur[mcell];
        // candidate marker values
        IEnumerable<int> mvals = key0[mid] >= 0 ? new[] { key0[mid] } : Enumerable.Range(0, 36).Where(v => where[v] < 0);
        foreach (int mv in mvals.ToArray()) {
            var k1 = (int[])key0.Clone(); var w1 = (int[])where.Clone();
            if (k1[mid] < 0) { k1[mid] = mv; w1[mv] = mid; }
            // current positions of c and p (if placed)
            int cpc = -1, ppc = -1;
            if (w1[c] >= 0) cpc = Array.IndexOf(cur, w1[c]);
            if (w1[p] >= 0) ppc = Array.IndexOf(cur, w1[p]);
            int dr = mv / 6, dc = mv % 6;
            var cands = new List<int>();
            if (cpc >= 0) cands.Add(cpc);
            else if (ppc >= 0) cands.Add(((ppc / 6 + dr) % 6) * 6 + (ppc % 6 + dc) % 6);
            else for (int x = 0; x < 36; x++) if (k1[cur[x]] < 0) cands.Add(x);
            foreach (int cp in cands) {
                int pp = ((cp / 6 - dr + 6) % 6) * 6 + (cp % 6 - dc + 6) % 6;
                var k2 = (int[])k1.Clone(); var w2 = (int[])w1.Clone();
                // place / check c at cp
                int idc = cur[cp];
                if (k2[idc] >= 0 && k2[idc] != c) continue;
                if (k2[idc] < 0) { if (w2[c] >= 0) continue; k2[idc] = c; w2[c] = idc; }
                int idp = cur[pp];
                if (k2[idp] >= 0 && k2[idp] != p) continue;
                if (k2[idp] < 0) { if (w2[p] >= 0) continue; k2[idp] = p; w2[p] = idp; }
                // apply rotations on cur
                var cu = (int[])cur.Clone(); int nmr = mr, nmc = mc;
                int pr = pp / 6;
                int last = cu[pr * 6 + 5]; for (int q = 5; q > 0; q--) cu[pr * 6 + q] = cu[pr * 6 + q - 1]; cu[pr * 6] = last;
                if (nmr == pr) nmc = (nmc + 1) % 6;
                int y = Array.IndexOf(cu, w2[c]) % 6;
                last = cu[30 + y]; for (int q = 5; q > 0; q--) cu[q * 6 + y] = cu[(q - 1) * 6 + y]; cu[y] = last;
                if (nmc == y) nmr = (nmr + 1) % 6;
                nmr = (nmr + c / 6) % 6; nmc = (nmc + c % 6) % 6;
                Dfs(t + 1, k2, cu, w2, nmr, nmc);
                if (sols.Count >= maxSol) return;
            }
        }
    }

    static void Main(string[] a) {
        P = a[0].Select(ch => AL.IndexOf(ch)).ToArray(); C = a[1].Select(ch => AL.IndexOf(ch)).ToArray(); T = Math.Min(P.Length, C.Length);
        var key0 = Enumerable.Repeat(-1, 36).ToArray(); var where = Enumerable.Repeat(-1, 36).ToArray();
        if (a.Length > 2 && a[2] != "-") for (int i = 0; i < 36; i++) if (a[2][i] != '?') { key0[i] = AL.IndexOf(a[2][i]); where[key0[i]] = i; }
        maxSol = a.Length > 3 ? int.Parse(a[3]) : 20;
        var cur = Enumerable.Range(0, 36).ToArray();
        var sw = System.Diagnostics.Stopwatch.StartNew();
        Dfs(0, key0, cur, where, 0, 0);
        Console.WriteLine("nodes {0} solutions {1} time {2:F1}s", nodes, sols.Count, sw.Elapsed.TotalSeconds);
        foreach (var s in sols.Take(20)) Console.WriteLine(new string(s.Select(v => v < 0 ? '?' : AL[v]).ToArray()));
    }
}
