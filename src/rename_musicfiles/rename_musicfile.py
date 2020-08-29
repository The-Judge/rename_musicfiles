#!/usr/bin/env python
from phrydy import MediaFile
from pathlib import Path
import sys

def main():
    for x in sys.argv[1:]:
        file = Path(x)
        try:
            f = MediaFile(file)
        except Exception as e:
            print(f"WARN: Skipping '{x}' because of: {str(e)}")
            continue
        new = Path(
            f"{f.artist}/(-{f.year}-) {f.album}/{f.track:02d} - {f.artist} - {f.title}.{file.name.rsplit('.', 1)[-1]}"
        )
        new.parent.mkdir(exist_ok=True, parents=True)
        file.rename(new)


if __name__ == "__main__":
    main()
