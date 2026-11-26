# Codebook — page (2), "bar and tick" script (blind transcription)

Each image shows ONE line of the cipher (LINE nn), cut in two parts: part 1 = left half, part 2 = right half. Part 2 starts with about one sign that may already be at the end of part 1: do NOT write that overlapping sign twice (look at the end of part 1 and the start of part 2 and decide).
Parts of the lines above/below may show at the top/bottom edge: ignore them, transcribe only the central line.

Every sign is a short HORIZONTAL BAR with small VERTICAL TICKS attached to it. A tick can point UP (u), DOWN (d), or cross the bar both ways (x). Signs are separated by small gaps.

Write each sign as the sequence, left to right, of bar pieces and ticks:
- a tick going up = u ; going down = d ; crossing the bar (up and down) = x
- a piece of bar = -  (one '-' between two ticks, one '-' at the left end if the bar extends to the left of the first tick, one '-' at the right end if the bar extends to the right of the last tick; never two '-' in a row)
Examples: ⌐ (tick down at the left end) = d- ; ¬ (tick down at the right end) = -d ; ⊔ (ticks up at both ends) = u-u ; ⊔ with a third tick up in the middle = u-u-u ; + = -x- ; ⊥ = -u- ; T = -d- ; a bar with a tick down at the left end and a tick up at the right end = d-u ; a bar alone = -
- A tick bent into a small hook or curl (like the top of a 2 or a z) still counts as u or d according to the direction it leaves the bar; add * after it if it is curled (e.g. u*-d).
- Uncertain element: add ? after it (e.g. -d?-u). Unreadable sign: ?
- A dot next to a sign: write . after the sign code as a separate token "dot".

Output format: one line per LINE: `nn<TAB>code code code ...` (sign codes separated by single spaces, in reading order left to right, part 1 then part 2).
Do not guess letters or meanings. Do not use any other transcription.
