"""Download DECODE thumbnails for the 1793 Fagel key bundle."""

from __future__ import annotations

from pathlib import Path
import re
import urllib.request


ROOT = Path(__file__).parent
COOKIE_PATH = ROOT.parent / "bordeaux" / "decode" / "cookie.txt"
cookie = re.sub(r"^cookie:\s*", "", COOKIE_PATH.read_text(encoding="utf-8").strip(), flags=re.I)


for record in range(2842, 2852):
    html_path = ROOT / ".." / "vanreede1787" / "decode" / f"record_{record}.html"
    text = html_path.read_text(encoding="utf-8", errors="replace")
    names = sorted(set(re.findall(r"filesrv/\?file=TH_((?:IMG)_[A-Za-z0-9_.]+)", text)))
    folder = ROOT / ".." / "vanreede1787" / "decode" / f"thumbs_R{record}"
    folder.mkdir(exist_ok=True)
    print(f"R{record}: {len(names)}", flush=True)
    for name in names:
        output = folder / name
        if output.exists():
            continue
        request = urllib.request.Request(
            f"https://de-crypt.org/decrypt-custom/filesrv/?file=TH_{name}",
            headers={"Cookie": cookie, "User-Agent": "Mozilla/5.0"},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            output.write_bytes(response.read())
