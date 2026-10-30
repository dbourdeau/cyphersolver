"""Fetch full-size DECODE page images for a record into an output folder (never into the repo: BL/ASV copyright).
   python research/frame_check_2026-10/decode_fetch.py <record id> <out dir> [max pages]
Uses the cookie in C:/Users/dbour/cypher/targets/bordeaux/decode/cookie.txt (git-ignored; the user reuses it, never delete)."""
import pathlib, re, subprocess, sys
COOKIE = pathlib.Path(r'C:/Users/dbour/cypher/targets/bordeaux/decode/cookie.txt')
rec, out = sys.argv[1].lstrip('R'), pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 12
c = COOKIE.read_text().replace('\r', '').replace('\n', '').strip()
page = subprocess.run(['curl', '-s', '-H', f'Cookie: {c}', f'https://de-crypt.org/decrypt-web/RecordsView/{rec}'], capture_output=True).stdout.decode('utf8', 'replace')
(out / f'rec{rec}.htm').write_text(page, encoding='utf8')
names = sorted(set(re.findall(r'TH_(IMG_R%s_I\d+_P\d+\.jpg)' % rec, page)), key=lambda s: int(re.search(r'_P(\d+)', s).group(1)))
print(len(names), 'images on record', rec)
for n in names[:mx]:
    f = out / n
    subprocess.run(['curl', '-s', '-H', f'Cookie: {c}', f'https://de-crypt.org/decrypt-custom/filesrv/?file={n}', '-o', str(f)])
    print(n, f.stat().st_size, 'FORBIDDEN' if f.stat().st_size == 17947 else 'ok')
