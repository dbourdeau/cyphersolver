package org.cryptool.ctts.cryptanalysis;

import org.cryptool.ctts.grams.Language;
import org.cryptool.ctts.util.Token;

import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.*;

/** Headless wrapper around CTTS's homophonic solver (Apache 2.0, George Lasry & CrypTool 2 Team).
 *  usage: HeadlessSolve tokens.txt LANG ngrams maxHomophones seconds out.txt
 *  tokens.txt: one line of text per ciphertext line, symbols separated by spaces. */
public class HeadlessSolve {
    public static void main(String[] a) throws Exception {
        List<String> lines = Files.readAllLines(Paths.get(a[0]), StandardCharsets.UTF_8);
        Language lang = Language.valueOf(a[1].toUpperCase());
        int ngrams = Integer.parseInt(a[2]);
        int maxHom = Integer.parseInt(a[3]);
        int seconds = Integer.parseInt(a[4]);
        ArrayList<Token> toks = new ArrayList<>();
        for (String line : lines) {
            if (line.trim().isEmpty()) continue;
            for (String s : line.trim().split("\s+")) toks.add(new Token(Token.Type.HOMOPHONE, s));
            toks.add(new Token(Token.Type.NEW_LINE));
        }
        CryptanalysisParameters p = new CryptanalysisParameters(lang);
        p.ngrams = ngrams;
        p.maxHomophones = maxHom;
        if (a.length > 6) {
            for (String row : Files.readAllLines(Paths.get(a[6]), StandardCharsets.UTF_8)) {
                String[] kv = row.trim().split("=");
                if (kv.length == 2) p.lockedHomophones.put(kv[0].trim(), kv[1].trim());
            }
            p.ignoreCurrentKey = false;
        }
        p.readTokens();
        p.referenceSequences();
        Cryptanalysis.solve(toks, p, 8);
        long end = System.currentTimeMillis() + seconds * 1000L;
        while (System.currentTimeMillis() < end) Thread.sleep(500);
        String key;
        synchronized (Cryptanalysis.keySb) { key = Cryptanalysis.keySb.toString(); }
        Cryptanalysis.stop();
        // decrypt with the key text
        Map<String, String> map = new HashMap<>();
        for (String row : key.split("\n")) {
            int i = row.lastIndexOf(" - ");
            if (i < 0) continue;
            String pl = row.substring(i + 3).trim();
            for (String c : row.substring(0, i).split("[|]")) map.put(c, pl);
        }
        StringBuilder out = new StringBuilder(key).append("\n--- decryption (? = unassigned/other)\n");
        for (String line : lines) {
            if (line.trim().isEmpty()) continue;
            for (String s : line.trim().split("\s+")) out.append(map.getOrDefault(s, "?"));
            out.append("\n");
        }
        Files.write(Paths.get(a[5]), out.toString().getBytes(StandardCharsets.UTF_8));
        System.out.println(out);
        System.exit(0);
    }
}
