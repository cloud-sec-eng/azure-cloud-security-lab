import json
from pathlib import Path
from typing import Any


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(
        # json.dumps = dump to string
        data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    # data = usually a Python dict or list
    # sort_key = true = sort dictionary keys alphabetically
    # encoding="uft-8" = Writes the string to the file at path using UTF-8 encoding
