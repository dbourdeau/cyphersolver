"""Polite single fetch: 1 s pause, WAINUT-research UA, stop on 429/bot check."""
import sys, time, urllib.request, urllib.error
UA = "WAINUT-research"
def get(url):
    time.sleep(1.1)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            raw = r.read()
            try: b = raw.decode("utf-8")
            except UnicodeDecodeError: b = raw.decode("cp1252", "replace")
    except urllib.error.HTTPError as e:
        if e.code == 429: sys.exit("STOP 429")
        return f"HTTP {e.code}"
    low = b.lower()
    if (len(b) < 20000 and "captcha" in low) or "cf-chl" in low or "are you a robot" in low:
        sys.exit("STOP bot check")
    return b
if __name__ == "__main__":
    out = get(sys.argv[1])
    if len(sys.argv) > 2:
        open(sys.argv[2], "w", encoding="utf-8").write(out); print(len(out))
    else:
        sys.stdout.reconfigure(encoding="utf-8"); print(out)
