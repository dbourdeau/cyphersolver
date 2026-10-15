"""Extract R2851 nomenclator cells addressed by R1893 code groups."""

from __future__ import annotations

import re
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageEnhance
from scipy.signal import find_peaks


ROOT = Path(__file__).parent
SCANS = ROOT / ".." / "vanreede1787" / "decode"
PAGE_ORDER = [4, 6, 5, 7, 9, 8]
# Global starts for each photographed page. A series contains codes 1..999.
# R2851 begins at overbar (=) 100, then continues with unmarked, diagonal
# (transcribed v), and dotted (transcribed diaeresis) series.
PAGE_STARTS = [100, 869, 1639, 2408, 3176, 3944]
SERIES_BASE = {"=": 0, "": 999, "v": 1998, "¨": 2997}


def red_mask(image: Image.Image) -> np.ndarray:
    rgb = np.asarray(image.convert("RGB")).astype(np.int16)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    return (r - g > 15) & (r - b > 12) & (r > 70) & (g < 210)


def row_grid(mask: np.ndarray) -> np.ndarray:
    projection = mask[:, 400:6400].sum(axis=1)
    peaks, _ = find_peaks(projection, distance=48, prominence=250)
    candidates = np.array([int(y) for y in peaks if 350 < y < 5150 and projection[y] > 1300])
    top = float(candidates[0] - 64)
    predicted = top + np.arange(72) * 62.0
    for _ in range(5):
        assignments: dict[int, int] = {}
        for y in candidates:
            index = int(np.argmin(np.abs(predicted - y)))
            if abs(predicted[index] - y) > 27:
                continue
            old = assignments.get(index)
            if old is None or projection[y] > projection[old]:
                assignments[index] = int(y)
        indexes = np.array(sorted(assignments))
        observed = np.array([assignments[i] for i in indexes])
        coefficients = np.polyfit(indexes, observed, 2)
        predicted = np.polyval(coefficients, np.arange(72))
    return predicted


def column_lines(mask: np.ndarray) -> list[int]:
    band = mask[450:4900]
    projection = band.sum(axis=0)
    peaks, _ = find_peaks(projection, distance=38, prominence=80)
    strong = [int(x) for x in peaks if 350 < x < 6500 and projection[x] > 1200]

    # The gutter sometimes creates two extra full-height strokes. Select a
    # 21-line subsequence whose gaps alternate wide word cells and narrow
    # number cells, allowing those gutter candidates to be skipped.
    states: dict[tuple[int, int], tuple[float, list[int]]] = {}
    for i, x in enumerate(strong):
        if x < 750:
            states[(i, 1)] = ((x - 540) ** 2 / 2500, [x])
    for length in range(1, 21):
        additions: dict[tuple[int, int], tuple[float, list[int]]] = {}
        expected = 440 if (length - 1) % 2 == 0 else 130
        low, high = ((340, 610) if expected == 440 else (75, 190))
        for (last_i, old_length), (cost, run) in list(states.items()):
            if old_length != length:
                continue
            for new_i in range(last_i + 1, len(strong)):
                gap = strong[new_i] - strong[last_i]
                if gap > high:
                    break
                if gap < low:
                    continue
                new_cost = cost + ((gap - expected) / (75 if expected == 440 else 30)) ** 2
                key = (new_i, length + 1)
                if key not in additions or new_cost < additions[key][0]:
                    additions[key] = (new_cost, run + [strong[new_i]])
        states.update(additions)
    finals = [value for (index, length), value in states.items() if length == 21]
    if not finals:
        raise RuntimeError(f"vertical grid not found: {strong}")
    return min(finals, key=lambda item: item[0])[1]


def canonical(token: str) -> tuple[int, str]:
    digits = re.findall(r"\d", token)
    marks = re.findall(r"\^([~v=¨+])", token)
    if not digits:
        raise ValueError(token)
    marker = marks[0] if marks else ""
    if any(mark != marker for mark in marks):
        raise ValueError(f"mixed marks: {token}")
    return int("".join(digits)), marker


def locate(token: str) -> tuple[int, int, int]:
    number, marker = canonical(token)
    if marker not in SERIES_BASE:
        raise ValueError(f"special series: {token}")
    global_number = SERIES_BASE[marker] + number
    page_index = max(i for i, start in enumerate(PAGE_STARTS) if start <= global_number)
    offset = global_number - PAGE_STARTS[page_index]
    macro, local = divmod(offset, 77)
    if macro >= 10:
        raise ValueError(f"outside page map: {token}")
    return PAGE_ORDER[page_index], macro, local


def extract(token: str) -> Image.Image:
    page, macro, local = locate(token)
    source = Image.open(SCANS / f"IMG_R2851_I19192_P{page}.jpg").convert("RGB")
    mask = red_mask(source)
    rows = row_grid(mask)
    lines = column_lines(mask)
    outer, divider, right = lines[macro * 2:macro * 2 + 3]
    row_height = float(np.median(np.diff(rows)))
    if local < 65:
        row = local
        x0, x1 = outer, divider
    else:
        half = (local - 65) // 6
        row = 65 + (local - 65) % 6
        midpoint = (outer + right) / 2
        half_left, half_right = (outer, midpoint) if half == 0 else (midpoint, right)
        # Keep the compact word and its printed code together.
        x0, x1 = half_left, half_right
    y0, y1 = rows[row], rows[row + 1]
    crop = source.crop((
        max(0, int(x0 - 8)), max(0, int(y0 - row_height * .12)),
        min(source.width, int(x1 + 8)), min(source.height, int(y1 + row_height * .12)),
    ))
    crop = ImageEnhance.Contrast(crop).enhance(1.25)
    crop = ImageEnhance.Sharpness(crop).enhance(1.4)
    crop.thumbnail((520, 115))
    return crop


def first_cipher_line() -> list[str]:
    source = (SCANS / "DOC_R1893_D3608_3608.txt").read_text(encoding="utf-8", errors="replace")
    for line in source.splitlines():
        if line.startswith("4 8 3."):
            normalized = re.sub(r"(\d)\s+\^", r"\1^", line)
            return [part.strip() for part in re.split(r"\.\s*", normalized) if part.strip()]
    raise RuntimeError("first ciphertext line not found")


def main() -> None:
    tokens = first_cipher_line()
    tile_w, tile_h = 560, 155
    tiles: list[Image.Image] = []
    for token in tokens:
        tile = Image.new("RGB", (tile_w, tile_h), "white")
        draw = ImageDraw.Draw(tile)
        try:
            page, macro, local = locate(token)
            draw.text((8, 5), f"{token}  P{page} col {macro + 1} local {local}", fill="black")
            tile.paste(extract(token), (8, 32))
        except Exception as exc:
            draw.text((8, 38), str(exc), fill="red")
        tiles.append(tile)
    cols = 3
    sheet = Image.new("RGB", (cols * tile_w, ((len(tiles) + cols - 1) // cols) * tile_h), "white")
    for index, tile in enumerate(tiles):
        sheet.paste(tile, ((index % cols) * tile_w, (index // cols) * tile_h))
    destination = SCANS / "R1893_first_line_R2851.jpg"
    sheet.save(destination, quality=96)
    print(destination)


if __name__ == "__main__":
    main()
