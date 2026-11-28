"""Check the transcription and conditional page-layout bounds for telegram 340."""

from collections import Counter, defaultdict
from itertools import product
from pathlib import Path


FIRST_PAGE = 10
BASE_BLOCKS = 75
ANCHOR = (259, 271)
VERBS = {"beibehalten": 13616, "gewonnen": 16016, "verlegt": 16716, "angeordnet": 4816}


def normalize(group):
    """Undo the one-step shift independently in each half of a page."""
    page, entry = divmod(group, 100)
    block, digit = divmod(entry, 10)
    half, offset = divmod(block, 5)
    return page, (5 * half + (offset - 1) % 5) * 10 + digit


def placements(source_to_base, block_start):
    """Generate the labelled runs consistent with the pins in one block."""
    first_label, first_base = source_to_base[0]
    for copies in product((1, 2), repeat=4):
        run = tuple(base for base, count in zip(range(block_start, block_start + 4), copies)
                    for _ in range(count))
        for offset, base in enumerate(run):
            if base != first_base:
                continue
            start = first_label - offset
            if start < FIRST_PAGE:
                continue
            if all(0 <= label - start < len(run) and run[label - start] == expected
                   for label, expected in source_to_base):
                yield start, start + len(run)


def minimum_last_label(pins):
    """Return the shortest full contiguous layout consistent with the pins."""
    source_map = dict(pins)
    if len(source_map) != len(pins):
        return None

    blocks = defaultdict(list)
    for label, base in sorted(pins):
        blocks[base - (base - FIRST_PAGE) % 4].append((label, base))

    states = {(FIRST_PAGE, 0)}
    # Nonoverlapping runs must follow the order of their first pinned labels.
    for block_start, required in blocks.items():
        next_states = set()
        for start, end in placements(required, block_start):
            for preceding_end, used in states:
                gap = start - preceding_end
                if gap < 0:
                    continue
                # Every unpinned block occupies between four and eight labels.
                fewest = (gap + 7) // 8
                most = min(gap // 4, BASE_BLOCKS - used - 1)
                for block_count in range(fewest, most + 1):
                    next_states.add((end, used + block_count + 1))
        states = next_states

    return min((end + 4 * (BASE_BLOCKS - used) - 1 for end, used in states), default=None)


def reading_pins(body, entries):
    pins = {ANCHOR}
    for position, code in entries:
        label, suffix = normalize(body[position - 1])
        base, base_suffix = divmod(code, 100)
        if suffix != base_suffix:
            raise ValueError(f"Group {position} has slot {suffix:02}; expected {base_suffix:02}")
        pins.add((label, base))
    return pins


def main():
    source = Path(__file__).with_name("ciphertext.txt").read_text(encoding="utf-8").splitlines()
    assert source[0].split() == ["047", "141", "135", "620", "27082"]
    original = [int(group) for line in source[1:] for group in line.split()]
    assert len(original) == 37 and original[0] == 29798
    assert [i for i, group in enumerate(original, 1) if group == 1235] == [15, 19]
    assert Counter(original).most_common(1) == [(1235, 2)]
    assert minimum_last_label({ANCHOR}) == 309

    for first_group in (29798, 29748):
        body = [first_group, *original[1:]]
        normalized = [normalize(group) for group in body]
        labels = Counter(page for page, _ in normalized)
        assert len(labels) == 33
        assert {page for page, count in labels.items() if count > 1} == {12, 58, 74, 78}
        assert not {42, 77}.intersection(slot for _, slot in normalized)
        print(f"First group {first_group}: {len(body)} groups, {len(labels)} distinct pages")
        print("verb          ending  wird/nicht (both)  weiterfuehr-/dass dieselben")
        for verb, code in VERBS.items():
            ending = ((34, 18654), (35, 4167), (36, code), (37, 11848))
            ending_bound = minimum_last_label(reading_pins(body, ending))
            negatives = [minimum_last_label(reading_pins(body, (*ending, (23, 12537), (33, neg))))
                         for neg in (11240, 24040)]
            preceding = (*ending, (20, 12190), (21, 8572))
            preceding_bound = minimum_last_label(reading_pins(body, preceding))
            assert ending_bound == 313
            assert negatives == [313 if verb == "verlegt" else 317] * 2
            assert preceding_bound == (317 if verb == "verlegt" else 313)
            print(f"{verb:<13} {ending_bound}     {negatives[0]}/{negatives[1]}            {preceding_bound}")


if __name__ == "__main__":
    main()
