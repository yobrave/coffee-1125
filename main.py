"""coffee-1125: ships the one-letter stance to the makefun output directory."""

import json
import pathlib
import shutil

PICK = "C"


def read_pick(root):
    data = (pathlib.Path(root) / "entry.txt").read_bytes()
    text = data.decode("utf-8").strip()
    if len(text) != 1 or not text.isalpha() or not text.isupper():
        raise SystemExit(f"gate wants exactly one capital letter, got {text!r}")
    return text


def write_pick(root, text):
    root = pathlib.Path(root)
    root.mkdir(parents=True, exist_ok=True)
    target = root / "entry.txt"
    src = pathlib.Path(__file__).resolve().parent / "entry.txt"
    if src.resolve() != target.resolve():
        shutil.copyfile(src, target)
    return target


if __name__ == "__main__":
    found = read_pick(pathlib.Path(__file__).resolve().parent)
    if found != PICK:
        raise SystemExit(f"entry drifted from the declared pick {PICK}")
    out = write_pick(__import__("os").environ.get("MAKEFUN_OUTPUT_DIR") or pathlib.Path(__file__).resolve().parent, found)
    print(json.dumps({"pick": found, "bytes": 1, "camp": "coffee", "target": str(out)}))
