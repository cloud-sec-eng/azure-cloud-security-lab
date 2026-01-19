import json
# Parse JSON strings into Python objects
import subprocess
# Run external commands
from typing import Any, List


class AzCliError(RuntimeError):
    pass
# class that inherit from RuntimeError
# pass means "no extra behavior," just a clearer category so you can except AzClitError: upstream


def run_az(args: List[str], debug: bool = False) -> str:
    # List[str] and bool are Type Hint
    # Debug: bool = False means we are expecting boolean and the default value of debug is False.
    # You can write debug without type hint. debug = False.
    cmd = ["az", *args]

    if debug:
        print(f"[debug] running: {cmd}")

    p = subprocess.run(
        # subprocess module : create new processes, connect to their input/output/error and get return codes.
        cmd,
        check=False,
        # To raise my own exception type with a message that cooses stderr ot stdout
        # If it is true, then python raises an exception automatically when the command fails.
        capture_output=True,
        # Python collect what the program writes to stdout/stderr
        text=True,
        # Give the output as normal string
    )
    # Runs the command and returns a CompletedProcess object p

    if p.returncode != 0:
        # returncode 0 means success, non-zero means failure
        msg = p.stderr.strip() or p.stdout.strip()
        raise AzCliError(f"az command failed (code={p.returncode}): {msg}")

    return p.stdout


def run_az_json(args: List[str], debug: bool = False) -> Any:
    out = run_az([*args, "-o", "json"], debug=debug)
    return json.loads(out)


def run_az_tsv(args: List[str], debug: bool = False) -> str:
    out = run_az([*args, "-o", "tsv"], debug=debug)
    return out.strip()
