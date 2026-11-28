#!/bin/bash
# usage: rr.sh step tool settings seeds inputs outputs result   (utc taken here, in the same command as the call)
F=/home/claude/keyless/round40c/basel_anv9/keyleaf/RUN_RECORD.tsv
printf '%s\t%s\tclaude-subagent\tclaude-opus-5-5\tnot exposed\thttps://claude.ai/code/session_01P5UF3myhVjFtgU9vTMj1qn\t-\t%s\t%s\t%s\t%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$1" "$2" "$3" "$4" "$5" "$6" "$7" >> $F
tail -1 $F
