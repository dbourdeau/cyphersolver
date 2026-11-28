"""Extract stack samples at the front, middle and back of the OPenn master set."""
import argparse
from pathlib import Path

import cv2
import numpy as np

BOOK = Path(__file__).resolve().parents[1] / "docs/ljs51-book"


def strip(directory, number, outer, inner, tone, contrast):
    image = cv2.imread(str(directory / f"0084_{number:04d}.tif"))
    if number % 2:
        image = cv2.flip(image, 1)
    height = image.shape[0]
    rows = np.linspace(.085, .91, 1280)
    # Boundaries measured from the outside of each scan. Exclude the board,
    # blank flyleaves and the written face at each end of the colour sample.
    knots = [.085, .3, .5, .8, .91]
    a, b = np.interp(rows, knots, outer), np.interp(rows, knots, inner)
    x = (a[:,None] + (b-a)[:,None]*np.linspace(0,1,196)) * 400/190
    y = np.broadcast_to((rows*height)[:,None], x.shape)
    panel = cv2.remap(image, x.astype('float32'), y.astype('float32'), cv2.INTER_LINEAR).astype('float32')
    grain = panel - cv2.GaussianBlur(panel,(0,0),4.5)
    # Reduce long shadows from the scan lighting. Otherwise these stationary
    # bands read as deep grooves when the fore-edge is seen almost head-on.
    column_tone = np.median(panel, axis=0, keepdims=True)
    reference = np.median(column_tone, axis=1, keepdims=True)
    relief = panel - reference - .62*(column_tone-reference)
    detail = relief + .35*grain
    spread = np.maximum(np.percentile(detail, 90, axis=(0,1)) - np.percentile(detail, 10, axis=(0,1)), 1)
    corrected = tone + (detail - np.median(detail, axis=(0,1))) * contrast/spread
    return np.clip(corrected,0,255).astype('uint8')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("master_dir", type=Path)
    args = parser.parse_args()
    # Median BGR and 10th-to-90th percentile span inside the approved edge.
    tone = [136, 166, 187]
    contrast = [21, 19, 24]
    samples = [
        (6,[81,81,84,85,88],[134,131,131,125,124]),
        (86,[62,61,59,58,62],[131,128,128,123,116]),
        (85,[100,103,102,104,111],[145,147,150,148,146]),
        (217,[38,38,38,40,45],[130,131,132,130,118]),
    ]
    panels = [strip(args.master_dir, *sample, tone, contrast) for sample in samples]
    for side, order in [("left", panels), ("right", panels[::-1])]:
        image = np.hstack(order)
        if not cv2.imwrite(str(BOOK / f"stack-{side}.jpg"), image, [cv2.IMWRITE_JPEG_QUALITY, 96]):
            raise IOError(side)
