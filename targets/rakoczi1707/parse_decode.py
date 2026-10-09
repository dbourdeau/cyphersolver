"""Parse DECODE's R902 transcription into per-line groups with the hand's conventions
(1^. = raised 1, 3^ = 5, '.' separates groups) -> tr/R902_decode_parsed.txt."""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
src = (ROOT / "DOC_R902_D1951_1951.txt").read_text(encoding="utf-8", errors="replace")
out = []; page = None
for line in src.splitlines():
    if line.startswith("#IMAGE NAME"):
        page = line.split(":")[1].strip(); out.append(f"# image {page}"); continue
    if line.startswith("#") or not line.strip() or page is None:
        continue
    if "Ont fait" in line: line = line.split("�")[0]
    s = line.replace("1_^.", "1_").replace("1__^.", "1_").replace("1^.", "1").replace("1^", "1")
    s = s.replace("3^.", "5").replace("3^", "5").replace("7^.", "7").replace("8^.", "8").replace("0^.", "0")
    s = s.replace("leo", "100").replace("o", "0").replace("v", "0").replace("g", "9").replace("G/6", "6")
    s = s.replace("1/2", "1").replace("i", "1")
    s = s.replace("--", "")
    groups = []
    for chunk in s.split("."):
        u = "_" if "_" in chunk else ""
        d = re.sub(r"[^0-9 ]", "", chunk)
        # split on doubled spaces? keep digits only
        digs = d.replace(" ", "")
        if digs: groups.append(digs + u)
    out.append(" ".join(groups))
(ROOT / "tr" / "R902_decode_parsed.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
