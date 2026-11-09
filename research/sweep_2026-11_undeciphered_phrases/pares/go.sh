cd "$(dirname "$0")"
while IFS= read -r t; do
 PYTHONUTF8=1 MAXPAGES=15 MAXREQ=60 python run.py "" "$t"
done < terms.txt
