import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# prompt for scripts/pass_c.py (half-line images)
LEG = open(os.path.join(ROOT, 'validation', 'legend.md'), encoding='utf8').read()
P = """The image shows ONE HALF of one line of a 1546 cipher of invented signs (signs cut at the left or right edge: skip them).
Copy ONLY the cipher signs, left to right, using exactly these sign names (separate every sign by one space):
{leg}
Rules:
- copy every component as its own name (o + is two signs, not one);
- a digit or letter written small ABOVE a sign: write it right after that sign as ^digit (e.g. e^6); if only part of it is visible at the top edge write ^?;
- a bar/tilde over a sign: write ~ after it (h~); a struck-through group: write it inside ( ) ;
- commas or dots on the line: , or .
- a gap between word groups: write | ;
- ordinary cursive Italian words on the line: write [TXT] once for each run of them; ignore writing cut off at the top or bottom edge;
- a sign you cannot match: ? .
This is a shape copy only; do not guess meaning. Output the sign sequence on ONE line and nothing else."""
