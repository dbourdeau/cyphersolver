"""Download the AIS (HHStA) page images of catalogue 885 into img/, one request at a time.

AIS marks these records "Kein Zugang (Reservatbestand)", but the digital copy is served to any client that keeps the
session cookie from detail.aspx (tested 30 Oct 2026). The server labels the JPEG text/html; check with `file`.
Images are not committed (img/ is git-ignored).
"""
import pathlib, subprocess, time

RECORDS = {7040827: 5, 7040824: 6, 7040845: 11}      # AIS id -> number of images (7-4-4, 7-4-5, 7-4-9)
OUT = pathlib.Path(__file__).parent / 'img'
OUT.mkdir(exist_ok=True)
for veid, n in RECORDS.items():
    jar = OUT / f'cj{veid}'
    subprocess.run(['curl', '-s', '-L', '-c', str(jar), '-b', str(jar), '-o', str(OUT / f'd{veid}.html'),
                    f'https://www.archivinformationssystem.at/detail.aspx?ID={veid}'], check=True)
    for i in range(1, n + 1):
        url = f'https://www.archivinformationssystem.at/getimage.aspx?veid={veid}&deid=10&sqnznr={i}&width=2400&klid=9'
        subprocess.run(['curl', '-s', '-b', str(jar), '-o', str(OUT / f'{veid}_{i:02d}.jpg'), url], check=True)
        time.sleep(1)
