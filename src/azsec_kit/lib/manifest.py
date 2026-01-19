import hashlib
# Provides hash algorithms like SHA-256
from pathlib import Path
from typing import Any, Dict, List

from azsec_kit.lib.io import write_json


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    # Create a SHA-256 "hash object"
    with path.open("rb") as f:
        # rb = read binary = for hashing it is better to hsh the binary not the text because it might cause encoding issues
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            # Read the file in chunks (1MB at a time)
            # Why in chunks? if the files is huge, reading it all at once can blow up memory
            # Keep calling the function until you it returns the sentinel value (b""[Empty bytes])
            h.update(chunk)
            # Adds this chunk to the hash calculation
    return h.hexdigest()
    # returns the digest as a human-friendly hex string


def write_manifest(out_dir: Path, artifacts: List[Path]) -> Path:
    entries: List[Dict[str, Any]] = []
    # Create a list to hold manifest entries
    # List[Dict[str, Any]] is just type hint
    for p in artifacts:
        # p is a Path to one evidence file
        entries.append(
            {"path": str(p), "sha256": sha256_file(p), "bytes": p.stat().st_size})
        # path = converts Path to a string so it. is JSON serializable
        # sha256 = computes the SHA-256 string for that file
        # bytes = p.stat() asks the OS for fiule metadata, .st_size is the file size in bytes
    mf = out_dir / "manifest.json"
    # Choose the manifest filename
    # Path operator / joins paths safely
    # out_dir = Path("reports/week01")
    # mf = Path("reports/week01/manifest.json")
    write_json(mf, {"artifacts": entries})
    return mf
