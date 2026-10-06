"""Measure the fresh image transcription of R902 (tr/R902_p277.txt, tr/R902_p278_l01-09.txt,
tr/R902_p278_l10-18.txt) against the R639 table, 5 Oct 2026.

Fillers (not counted): line-initial nulls/fillers (97-127 odd, 125, 127, 563, 566, 670, 689) and line-final
5xx/6xx groups other than 561/562. Every other group counts. A group is unread when listed in UNREAD;
CORR lists context-forced corrections (grade C), each a one-figure misreading or slip.
Usage: python measure_tr.py [--text]
"""
import re, sys, importlib.util as iu
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sp = iu.spec_from_file_location("d7", ROOT / "decode_tr.py"); m = iu.module_from_spec(sp); sp.loader.exec_module(m)
key = dict(m.key); key["89"] = "Et"   # C: 'les recrues et les munitions', 'Palatin de Russie et l'envoyé'
FILES = ["R902_p277.txt", "R902_p278_l01-09.txt", "R902_p278_l10-18.txt"]
LEAD = {"97", "99", "101", "103", "105", "107", "109", "111", "113", "115", "117", "119", "125", "127",
        "563", "566", "670", "689"}
# (file, line 1-based, token 0-based): corrected group
CORR = {
    ("R902_p277.txt", 2, 9): "118",   # dernieres: 'ii8' es, read 128 asses
    ("R902_p277.txt", 3, 9): "298",   # maniere: ni (248 il)
    ("R902_p277.txt", 3, 16): "104",  # denoüee: U (19 E)
    ("R902_p277.txt", 5, 10): "118",  # recrues: es (128)
    ("R902_p277.txt", 8, 19): "181",  # des articles (151 ci)
    ("R902_p277.txt", 15, 9): "371",  # vous rendre compte (391 sieur)
    ("R902_p277.txt", 24, 7): "348",  # qualitez (345 proposition)
    ("R902_p277.txt", 26, 11): "174", # soupçonné de V.A. (194 eux)
    ("R902_p278_l01-09.txt", 1, 6): "12",    # le bruit: B (112 Et)
    ("R902_p278_l01-09.txt", 1, 20): "352",  # qu'on (252 interets)
    ("R902_p278_l01-09.txt", 6, 22): "298",  # opinion: ni (248 il)
    ("R902_p278_l01-09.txt", 9, 18): "247",  # prejugez: ju (297 ne)
}
UNREAD = {
    ("R902_p277.txt", 1, 1),               # 589 before 'A Slupce'
    ("R902_p277.txt", 4, 4),               # 85 in 'il [85] sou T' (est tout?)
    ("R902_p277.txt", 7, 8),               # 8 in 's'arreste[8] point'
    ("R902_p277.txt", 9, 17),              # 120 after 'je persuade'
    *[("R902_p277.txt", 13, i) for i in range(17, 22)],  # 224 264 174 226 37
    *[("R902_p277.txt", 14, i) for i in range(1, 6)],    # 324 125 104 589 4
    ("R902_p277.txt", 16, 4),              # 297 'que [ne] lettres'
    ("R902_p277.txt", 17, 14),             # 363 'je [ri] S que'
    ("R902_p277.txt", 18, 1),              # 436 'en au [vous] dit'
    ("R902_p277.txt", 19, 21),             # 860
    ("R902_p277.txt", 20, 5),              # 95 'temps [es] beaucoup'
    ("R902_p277.txt", 20, 9),              # 92 'Da D [O] re S se'
    ("R902_p277.txt", 22, 10),             # 120 'si vous croi je [rt]'
    ("R902_p277.txt", 25, 12),              # 9 'manque [9] outre'
    ("R902_p277.txt", 30, 20),             # 194 'esté [eux] pable' (capable)
    ("R902_p277.txt", 18, 0),              # 129 'au' at line start (text or filler)
    ("R902_p278_l01-09.txt", 1, 0),        # 121 'ambassade' at line start
    ("R902_p278_l01-09.txt", 4, 0),        # 129 'au' at line start
    ("R902_p278_l01-09.txt", 4, 7),        # 264 'amenoit avec [les]' (luy?)
    ("R902_p278_l01-09.txt", 4, 8),        # 89 '[et] N député' (un?)
    ("R902_p278_l01-09.txt", 3, 18),       # 27 'Constantin [I] no P le'
}


def groups(f):
    n = 0
    for line in (ROOT / "tr" / f).read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        n += 1
        yield n, line.split()


def main():
    tot = rd = 0; per = {}
    text = []
    for f in FILES:
        t = r = 0
        for n, gs in groups(f):
            words = []
            for i, g in enumerate(gs):
                d = re.sub(r"\D", "", g)
                d = CORR.get((f, n, i), d)
                filler = (i == 0 and d in LEAD) or (i == len(gs) - 1 and len(d) == 3 and d[0] in "56" and d not in ("561", "562"))
                if filler:
                    words.append("·"); continue
                v = (m.TRUNC[d] + "_") if "_" in g and d in m.TRUNC else key.get(d)
                t += 1
                if v is None or (f, n, i) in UNREAD:
                    words.append(f"[{d}]")
                else:
                    r += 1; words.append(v or "·")
            text.append(f"{f[5:-4]}:{n} " + " ".join(words))
        per[f] = (r, t); tot += t; rd += r
    for f, (r, t) in per.items():
        print(f"{f}: {r}/{t} = {r/t:.3f}")
    print(f"R902 overall: {rd}/{tot} = {rd/tot:.3f}  (corrections C: {len(CORR)} + 89=Et)")
    if "--text" in sys.argv:
        print("\n".join(text))


if __name__ == "__main__":
    main()
