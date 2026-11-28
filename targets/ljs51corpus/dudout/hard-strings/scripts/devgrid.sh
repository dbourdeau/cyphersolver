#!/bin/bash
# Grille de developpement sur les 16 chaines deja mesurees avec separateurs (grillees). usage: devgrid.sh mode rho lam
cd "/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/ljs51-22r1-61r3"
LM=../ljs51-aveugle/modele/lm4_sp.bin
for c in 22r.1 61r.3 19r.7 105v.6 18r.11 23r.9 30r.4 42r.2 39v.12 41r.3 31r.11 35v.8 46r.11 82r.9 56v.8 20r.8+47r.1; do
  echo "$c"; done | xargs -P 8 -I{} python3 -I scripts/dev.py {} $LM modele/lex.bin $2 $3 20 500000 2811 $1 | cut -f1-16 | sort
