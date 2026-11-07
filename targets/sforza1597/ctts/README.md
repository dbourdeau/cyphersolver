# Headless CTTS solver (George Lasry's homophonic solver, Apache 2.0)

CTTS (CrypTool Transcriber and Solver, https://www.cryptool.org/en/ctts/, source https://github.com/CrypToolProject/CTTS) does
symbol segmentation and classification by hand in a GUI; only its cryptanalysis half is scriptable. `HeadlessSolve.java` calls
`Cryptanalysis.solve` directly (no JavaFX), with the Italian, Latin, French, Spanish, English, German and Dutch corpora that ship
in the repo.

Set-up (6 Nov 2026; nothing here is committed except this folder's small files):
1. `git clone --depth 1 https://github.com/CrypToolProject/CTTS.git src`
2. A JDK 21 (Temurin) unzipped to `jdk/` and a JRE to `jre/` (the jar needs no install).
3. Compile from source, not the signed jar (package-private access fails against a signed jar):
   `javac -encoding UTF-8 -d classes src/src/main/java/org/cryptool/ctts/{cryptanalysis/{Cryptanalysis,CryptanalysisParameters,SimulatedAnnealing}.java,grams/*.java,util/Token.java} HeadlessSolve.java`
   then `cp src/src/main/resources/*.txt classes/`.
4. `sh run.sh tokens.txt ITALIAN 5 4 60 out.txt` (tokens file: one ciphertext line per line, symbols space-separated).

Control (`control_tokens.txt`, 450 Italian letters under a random key with up to 3 homophones, 33 symbols): 60 s, 449 of 450 letters recovered (`control_plain.txt` is the truth). The solver covers letter homophones only: word signs and nulls have to be given as
symbols the solver may leave unmatched, so a nomenclator cipher reads in part.
