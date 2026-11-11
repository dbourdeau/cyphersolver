#!/usr/bin/env python3
"""Fetch DECODE record views (metadata only, no images) and print id | holder | start date | end date | author | origin city | status.
usage: decode_views.py CACHEDIR id [id ...]"""
import sys, re, html, time, os, urllib.request
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
d = sys.argv[1]; os.makedirs(d, exist_ok=True)
def field(t, a, b):
    m = re.search(re.escape(a) + r"\|(.*?)\| " + re.escape(b), t); return m.group(1).strip() if m else ""
for i in sys.argv[2:]:
    p = os.path.join(d, i + ".html")
    if not os.path.exists(p):
        s = urllib.request.urlopen(urllib.request.Request("https://de-crypt.org/decrypt-web/RecordsView/" + i, headers={"User-Agent": UA}), timeout=90).read().decode("utf8", "replace")
        open(p, "w", encoding="utf8").write(s); time.sleep(2.5)
    s = open(p, encoding="utf8").read()
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)))
    t = re.sub(r"(\|\s*)+", "| ", re.sub(r"<[^>]+>", "|", t))
    print(" | ".join([i, field(t, "Holder", "Author"), "-".join(field(t, x, y) for x, y in (("Start Year", "Start Month"), ("Start Month", "Start Day"), ("Start Day", "End Year"))),
        field(t, "| Author", "Sender"), field(t, "Receiver", "Region"), field(t, "Origin City", "Start Year"), field(t, "| Status", "Symbol Set"), "inline plaintext " + field(t, "Inline Plaintext", "Cleartext")]), flush=True)
