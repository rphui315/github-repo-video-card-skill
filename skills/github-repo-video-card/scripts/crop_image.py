#!/usr/bin/env python3
"""Crop an image by x/y/w/h for repo video screenshot preparation."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--x", type=int, required=True)
    parser.add_argument("--y", type=int, required=True)
    parser.add_argument("--w", type=int, required=True)
    parser.add_argument("--h", type=int, required=True)
    args = parser.parse_args()

    image = Image.open(args.input)
    box = (args.x, args.y, args.x + args.w, args.y + args.h)
    crop = image.crop(box)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    crop.save(args.output)
    print(f"{args.output} {crop.size[0]}x{crop.size[1]}")


if __name__ == "__main__":
    main()
