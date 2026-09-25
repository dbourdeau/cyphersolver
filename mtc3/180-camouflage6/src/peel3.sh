#!/bin/bash
S="C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-mysterytwisterc3-solution-812495/c54e3226-8150-41ac-99d9-ab3c0b9157a6/scratchpad"
cd "$S"
EX=peel3_exclude.txt; LOG=peel3_log.txt
for r in $(seq $1 $2); do
  OUT="peel3_r${r}.txt"
  ORDER=THEANDOISRLCUMWFGYPBVKJXQZ ./run.sh camograd.cs CamoGrad "ct.bin C:/Users/dbour/cypher/lang/corpora/en-gutenberg.txt 150000 20 - $EX $OUT" > "peel3_r${r}.stdout" 2>&1
  TOP=$(head -1 "$OUT"); SC=$(echo "$TOP" | cut -d' ' -f1)
  echo "ROUND $r score $SC" >> "$LOG"
  if python -c "import sys; sys.exit(0 if float('$SC')>=40 else 1)"; then
    echo "$TOP" | cut -d' ' -f2 | tr ',' '\n' | cut -d: -f1 | grep -v '^-1$' | tr '\n' ' ' >> "$EX"; echo >> "$EX"
  else
    echo "LOWSCORE stop at round $r" >> "$LOG"; break
  fi
done
echo DONE >> "$LOG"
