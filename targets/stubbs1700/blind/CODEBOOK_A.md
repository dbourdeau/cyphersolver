# Codebook — page (1), box script (blind transcription)

Each cell of a contact sheet shows ONE drawn box (a small rectangle), labelled with an id (e.g. L07.12). Inside the box there are 0, 1, 2 (rarely 3) small dark marks, each a small triangle / wedge attached to the inside of the frame. Record WHERE each mark sits, using these 8 position codes, as seen in the image (top of image = top):

- TL = mark filling/cutting the top-left corner (a diagonal across the corner, or a small triangle in the corner — size does not matter, a long diagonal running from the top-left area is still TL if the filled triangle sits in the top-left corner)
- TR = top-right corner
- BR = bottom-right corner
- BL = bottom-left corner
- T  = a V-shaped notch hanging from the middle of the top edge
- B  = a Λ-shaped notch rising from the middle of the bottom edge
- L  = a >-shaped notch pointing right from the middle of the left edge
- R  = a <-shaped notch pointing left from the middle of the right edge

Rules
- Write the positions joined by '+' in this fixed order: TL, T, TR, R, BR, B, BL, L. Example: "TL+BR", "T+BR", "R".
- Empty box (no mark): write 0
- Uncertain mark: add '?' to that code (e.g. "TR+B?"). Unreadable box: write ?
- Cell shows no box at all (blank paper, a stray stroke, a dash): write NOBOX
- Cell shows only part of a box (box broken in two, the other part in a neighbouring cell): write FRAG:<what you see>, e.g. FRAG:TL
- Two boxes visible in one cell: describe only the central one.
- Do NOT guess letters or meanings; only shapes. Do not look for or use any other transcription.
- Ids starting with M are boxes written sideways in the margin: still describe positions as seen in the image, without rotating.

Output: a plain text file, one line per id, in sheet order: `<id>\t<code>`
