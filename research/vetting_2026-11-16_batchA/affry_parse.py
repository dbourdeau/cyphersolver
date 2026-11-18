"""Parse saved friXplore pages (raw/frix/*.html) into raw/affry_rows.json: one row per Affry piece."""
import re, html, json, glob
ROW = re.compile(r"CH AEF Affry \(de Boccard\) (\d+)\.(\d+[a-z]?) ((?:(?!CH AEF|\.\.\.).)*?) \((Pièce|Dossier|Sous-dossier)\)")
rows = {}
for f in sorted(glob.glob('raw/frix/*.html')):
    t = open(f, encoding='utf8').read()
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    for ser, num, title, lvl in ROW.findall(t):
        m = re.match(r"(.*?),\s*((?:\d{4}|s\.\s?d\.)[^,]*)$", title)
        ti, date = (m.group(1), m.group(2)) if m else (title, '')
        rows.setdefault(f"{ser}.{num}", {"series": int(ser), "num": num, "title": ti.strip(), "date": date.strip(), "level": lvl})
json.dump(rows, open('raw/affry_rows.json', 'w', encoding='utf8'), ensure_ascii=False, indent=0)
import collections
print(len(rows), sorted(collections.Counter(r['series'] for r in rows.values()).items())[:12])
