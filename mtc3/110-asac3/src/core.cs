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
