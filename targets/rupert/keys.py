"""Key tables transcribed from the Add MS 72438 key sheets (DECODE images). Each key: letters {num: letter}, words {num: word}."""
def letters(spec):
    d = {}
    for let, nums in spec.items():
        for n in nums: d[n] = let
    return d
# Key 118 "Cypher for Ormond & Prince Rupert", Add MS 72438 ff. 59-60 (R8655), = Tomokiyo's Charles I-Rupert-Digby-Ormonde 1644-45.
K118_LET = letters({'a': [14, 15, 16, 17], 'b': [21, 22, 23], 'c': [11, 12, 13], 'd': [5, 6, 7], 'e': [1, 2, 3, 4], 'f': [8, 9, 10],
    'g': [18, 19, 20], 'h': [38, 39, 40], 'i': [30, 31, 32, 33], 'k': [41, 42, 43], 'l': [27, 28, 29], 'm': [24, 25, 26],
    'n': [48, 49, 50], 'o': [44, 45, 46, 47], 'p': [34, 35, 36, 37], 'q': [61, 62, 63], 'r': [64, 65, 66], 's': [57, 58, 59, 60],
    't': [78, 79, 80], 'v': [74, 75, 76, 77], 'w': [53, 54, 55, 56], 'x': [71, 72, 73], 'y': [67, 68, 69, 70], 'z': [51, 52]})
K118_NULLS = list(range(81, 91))
# words 91-434 alphabetical: A 91-107, B 109-122, C 123-141, D 142-158, E 159-175, F 176-192, G 193-205, H 209-224,
# I/J 225-239, K 241-249, L 257-272, M 273-288, N 289-303, O 304-316, P 317-333, Q 334-343, R 344-361, S 362-379,
# T 380-393, V 394-408, W 409-422, Y 423-430, Z 431-434.
