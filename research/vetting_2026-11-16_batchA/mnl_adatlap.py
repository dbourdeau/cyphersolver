"""Print the text of MNL AdatbazisokOnline G 15 datasheets. usage: mnl_adatlap.py id [id ...]"""
import sys, re, html, time, urllib.request
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0"
B = "https://adatbazisokonline.mnl.gov.hu/adatbazis/ii_-rakoczi-ferenc-fejedelem-leveltara_-emigracioba-vitt-resz/adatlap/"
for i in sys.argv[1:]:
    t = urllib.request.urlopen(urllib.request.Request(B + i, headers={"User-Agent": UA}), timeout=60).read().decode("utf8", "replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    a = t.find("fa-struktúrában!"); b = t.find("Tartalomgazda")
    print(i, "::", t[a + 16:b].strip()); time.sleep(1.2)
