import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"


def load(name):
    return json.loads((OUT / name).read_text())

