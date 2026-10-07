#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export TMPDIR="$PWD"
export PYTHONDONTWRITEBYTECODE=1
python3 prepare_search.py > preparation.log
clang++ -std=c++17 -O3 -pthread search_transforms.cpp -o search_transforms
./search_transforms WE028 8 > run_WE028.log 2>&1
./search_transforms Armstrong972 8 > run_Armstrong972.log 2>&1
python3 summarize_results.py > summary_console.txt
