"""Print the aligned sign transcription and its literal substitution."""

# Mnemonics approximate shapes, not numerical values. See NOTES for variants.
KEY = {
    "9": "a", "2": "c", "3": "d", "4": "e", "5": "h", "T": "i",
    "6": "l", "7": "m", "L": "n", "V": "o", "8": "p", "B": "r",
    "y": "s", "D": "t", "K": "u", "O": "w",
}

# Proposed spellings. The notes give the evidence for each assignment.
PROPOSED = {"F": "g", "E": "k", "J": "s", "j": "s"}

PASSAGES = {
    "103v.1": "7T25 3KL2D 96yV",
    "103v.2": "39J 3Ty4y 34B B425D4",
    "103v.3": "O42FE TyD 34B 85T6V",
    "103v.4": "jV854T",
    "103v below, first two groups": "924DV 3TyDT6",
    "103v below, at the fold": "4yyT?",
    "104v, first label": "y8TBDKy",
    "104v, second label after the large C": "VB8Ky",
    "104v, third label": "9LT79",
    "105r, opening, first group": "74B2KBT27",
    "105r, opening, second group": "yK685KB47",
    "105r, between Et and in aquam": "y9647",
    "105r, after apparent initial f": "T?D",
    "105r, group after the colon": "yV6K7",
    "105r, group after sepe": "9ByV",
    "105r, before the longer group": "F?",
    "105r, end of the sepe line": "y?6KT?D",
    "105r, after fiat in the lower line": "yK68KB",
    "00030, opening words": "3T4 O4Tyy4 3T4 T25",
    "00036, after capital O": "64K7",
    "00036, after mercury sign": "4yD",
    "00036, after capital F": "4B74LDK7",
    "00074, final group": "KTDBTV6K7",
    "00155, dotted circle before 'orden'": "OVB34L",
    "00155, short group by the weights": "OV6",
    "00155, coin, after p and apparent f": "4LLTF2E",
}


def decode(groups, key=KEY):
    return " ".join("".join(key.get(sign, "?") for sign in group)
                    for group in groups.split())


if __name__ == "__main__":
    working_key = KEY | PROPOSED
    for location, groups in PASSAGES.items():
        literal = decode(groups)
        proposed = decode(groups, working_key)
        alternative = f"  [proposed: {proposed}]" if literal != proposed else ""
        print(f"{location:36} {groups:26} {literal}{alternative}")
