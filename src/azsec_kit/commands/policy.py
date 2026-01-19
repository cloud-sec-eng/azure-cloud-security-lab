from pathlib import Path
from typing import List

from azsec_kit.lib.azcli import run_az_json, run_az_tsv
from azsec_kit.lib.io import write_json
from azsec_kit.lib.manifest import write_manifest


def run(rg: str, out_dir: Path, debug: bool = False) -> None:
    artifacts: List[Path] = []

    rg_id = run_az_tsv(["group", "show", "--name", rg,
                       "--query", "id"], debug=debug)

    assignments = run_az_json(
        ["policy", "assignment", "list", "--scope", rg_id], debug=debug)
    p1 = out_dir / f"policy.assignments.rg.{rg}.json"
    write_json(p1, assignments)
    artifacts.append(p1)

    summary = run_az_json(
        ["policy", "state", "summarize", "--resource-group", rg], debug=debug)
    p2 = out_dir / f"policy.state-summarize.rg.{rg}.json"
    write_json(p2, summary)
    artifacts.append(p2)

    write_manifest(out_dir, artifacts)
