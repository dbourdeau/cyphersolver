"""Fetch selected original key pages from authenticated DECODE records."""

import re
from pathlib import Path
import sys
import urllib.request


root = Path(__file__).parent
record = int(sys.argv[1])
wanted = {int(value) for value in sys.argv[2].split(",")}
cookie = re.sub(r"^cookie:\s*", "", (root.parent / "bordeaux" / "decode" / "cookie.txt").read_text(encoding="utf-8").strip(), flags=re.I)
html = (root / ".." / "vanreede1787" / "decode" / f"record_{record}.html").read_text(encoding="utf-8", errors="replace")
names = sorted(set(re.findall(r"filesrv/\?file=TH_((?:IMG)_[A-Za-z0-9_.]+)", html)))
for name in names:
    match = re.search(r"_P(\d+)\.", name)
    if not match or int(match.group(1)) not in wanted:
        continue
    destination = root / ".." / "vanreede1787" / "decode" / name
    if destination.exists() and destination.stat().st_size > 100_000:
        print(f"exists {name}")
        continue
    request = urllib.request.Request(
        f"https://de-crypt.org/decrypt-custom/filesrv/?file={name}",
        headers={"Cookie": cookie, "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        data = response.read()
    destination.write_bytes(data)
    print(f"{name}: {len(data)} bytes", flush=True)
