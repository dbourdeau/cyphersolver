#!/bin/sh
# Headless CTTS solver. usage: run.sh tokens.txt LANG ngrams maxHomophones seconds out.txt
# Needs (git-ignored, see README.md): ctts/jre or jdk folder, ctts/src (clone of CrypToolProject/CTTS), ctts/classes.
cd "$(dirname "$0")" || exit 1
JAVA=$(ls -d jre/*/bin/java.exe jdk/*/bin/java.exe 2>/dev/null | head -1)
exec "$JAVA" -cp classes org.cryptool.ctts.cryptanalysis.HeadlessSolve "$@"
