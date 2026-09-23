"""Fetch public primary-source metadata and the cipher image; no login needed."""
import json
from pathlib import Path
import requests
from PIL import Image

HERE = Path(__file__).resolve().parent
base = 'https://www.e-manuscripta.ch/i3f/v20/'
response = requests.get(base + '1033440/manifest', timeout=60)
response.raise_for_status()
(HERE / 'manifest.json').write_text(json.dumps(response.json(), indent=2), encoding='utf-8')
response = requests.get(base + '1033442/full/full/0/default.jpg', timeout=60)
response.raise_for_status()
(HERE / 'flyleaf-full.jpg').write_bytes(response.content)
image = Image.open(HERE / 'flyleaf-full.jpg')
assert image.size == (3409, 4031), 'Check source geometry before cropping.'
image.crop((140, 830, 2730, 1720)).save(HERE / 'cipher-full.png')
print('Saved manifest and full-resolution cipher surface.')
