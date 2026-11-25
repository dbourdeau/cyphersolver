"""Test the five GEMF 8 verso masks against selected edited recto recitations.

One period counts one illegible or estimated missing position. Under-dotted
readings are held fixed for the exact test. These are normalized editorial
strings, including supplements, not independent readings from ink.
"""

PASSAGES = [
    "ειειειειειειειειχοιθσαφουθχενθονευαφουθανουαωθειειειπεοοειακωβμαννοχαραννουθχαλωαφκουλιξνοη",
    "βορναθλουβεινεαρουηρουειρειτινλοτολ",
    "ιωθηπνουνγμοηρμενδουμβαομεγαλωνυμοσιακωφθοηριθερμοηρφθαωομεγαλωνυμοσιωθηφνουθουηρβωβελιξομεγαλωνυμοσιακω",
    "ουσιρφνουχμελλανχιωκερδωμελιβευ",
    "νεβενθηριχ",
    "ωθραωσαυτραιστραεβασυμ",
]

MASKS = ["ε.", "γ.......φι", "εωτ.....χ", "λ....τα", "..τω....ξ"]

for line, mask in enumerate(MASKS, 1):
    hits = []
    for passage in PASSAGES:
        for start in range(len(passage) - len(mask) + 1):
            window = passage[start : start + len(mask)]
            if all(m == "." or m == c for m, c in zip(mask, window)):
                hits.append(window)
    print(line, len(hits), sorted(set(hits)))

# Compare every window with the same right-aligned seven-letter span,
# allowing any one of the three proposed readings to disagree.
suffix = MASKS[-1][2:]
windows = [
    passage[i : i + len(suffix)]
    for passage in PASSAGES
    for i in range(len(passage) - len(suffix) + 1)
]
near = [word for word in windows if sum(a == b for a, b in zip(word, suffix)) >= 2]
print("Line 5, seven slots:", len(windows), "windows, two or more agreements:", near)
print("All windows ending in xi:", [word for word in windows if word.endswith("ξ")])
