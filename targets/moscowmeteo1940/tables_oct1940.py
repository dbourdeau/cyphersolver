"""The two new key grids of the Moscow weather broadcast, in force from 12 October 1940 16:00, as reconstructed by the
Japanese Army Meteorological Department (report of 16 October 1940, JACAR Ref. C01004818600, image 2; not reproduced).
Rows = bb (00..99), columns = aaa in the order of the printed heading. One figure per cell (condensed form: read row
after row it gives the 109-figure cycle). Cursive glyphs: "/"=1, "Z"=2, "ц"=4, "√"=5 (confirmed by the row labels
44 "цц" and 55 "√√"). "X" = struck-out cell (the one duplicate key of 110 keys for 109 positions).
Caveat: in the odd-day grid 2 and 5 occur 13 times and 4 only 11 times: one figure is probably misread (a 5 or a 2 for
a 4); Brice Dudout re-read eight of the "5" cells on the image (all confirmed 5), so the faulty cell is not located.
The even-day cells (00,111)=5 and (00,888)=8, marked doubtful in the first transcription, were confirmed by him."""
ODD_HDR = ["XXX","444","777","555","000","333","999","888","666","111","222"]
EVEN_HDR = ["000","111","222","333","444","555","666","777","888","999","XXX"]
ODD = """
00 1 3 9 5 7 2 2 8 6 5 X
11 9 8 5 2 3 7 9 4 8 1 6
22 9 1 4 8 3 5 4 7 5 2 6
33 3 2 8 5 6 1 3 7 2 4 9
44 8 7 4 1 2 6 8 3 7 9 5
55 5 3 1 7 8 3 4 9 4 6 2
66 2 1 7 4 5 9 2 6 1 3 8
77 3 9 5 9 4 8 1 1 6 2 7
88 6 5 2 8 9 4 6 1 5 7 3
99 7 6 3 9 1 5 7 2 6 8 4
"""
EVEN = """
00 7 5 1 2 3 6 3 9 8 4 X
11 3 1 6 7 8 2 8 5 4 9 9
22 3 2 6 5 1 8 5 4 7 4 9
33 6 3 9 1 2 5 2 8 7 3 3
44 2 9 5 6 7 1 7 4 3 8 8
55 8 6 2 3 4 7 4 1 9 4 5
66 5 3 8 9 1 4 1 7 6 2 2
77 4 2 7 8 9 9 6 5 1 1 3
88 9 7 3 4 5 8 5 2 1 6 6
99 1 8 4 5 6 9 6 3 2 7 7
"""
def parse(s):
    return [(l.split()[0], l.split()[1:]) for l in s.strip().splitlines()]
