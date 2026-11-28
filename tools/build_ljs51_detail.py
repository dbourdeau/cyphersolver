"""Register OPenn master photographs to the viewer UVs and export zoom textures."""
import argparse
from pathlib import Path

import cv2
import numpy as np

BOOK = Path(__file__).resolve().parents[1] / "docs/ljs51-book"


def export(master_dir):
    destination = BOOK / "detail"
    destination.mkdir(exist_ok=True)
    detector = cv2.SIFT_create(nfeatures=1400)
    matcher = cv2.BFMatcher()
    for number in range(6, 218):
        name = f"0084_{number:04d}"
        master = cv2.imread(str(master_dir / (name + ".tif")))
        page = cv2.imread(str(BOOK / "pages" / (name + ".jpg")), cv2.IMREAD_GRAYSCALE)
        small = cv2.resize(master, None, fx=.4, fy=.4, interpolation=cv2.INTER_AREA)
        kp, des = detector.detectAndCompute(cv2.cvtColor(small, cv2.COLOR_BGR2GRAY), None)
        ref, ref_des = detector.detectAndCompute(page, None)
        matches = [m for m, n in matcher.knnMatch(des, ref_des, k=2) if m.distance < .75*n.distance]
        src = np.float32([kp[m.queryIdx].pt for m in matches]) / .4
        dst = np.float32([ref[m.trainIdx].pt for m in matches])
        transform, mask = cv2.estimateAffine2D(src, dst, ransacReprojThreshold=1.5)
        if transform is None or mask.sum() < 40:
            raise ValueError(f"Insufficient alignment evidence for {name}")
        errors = np.linalg.norm(src @ transform[:, :2].T + transform[:, 2] - dst, axis=1)
        if np.median(errors[mask.ravel().astype(bool)]) > .8:
            raise ValueError(f"Registration residual too large for {name}")
        detail = cv2.warpAffine(master, transform * 2.5, (1800, 2600), flags=cv2.INTER_CUBIC,
                                borderMode=cv2.BORDER_REPLICATE)
        if not cv2.imwrite(str(destination / (name + ".jpg")), detail, [cv2.IMWRITE_JPEG_QUALITY, 90]):
            raise IOError(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("master_dir", type=Path)
    export(parser.parse_args().master_dir)
