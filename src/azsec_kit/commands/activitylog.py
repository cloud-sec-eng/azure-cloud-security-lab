from pathlib import Path
from typing import List

from azsec_kit.lib.azcli import run_az_json
from azsec_kit.lib.io import write_json
from azsec_kit.lib.manifest import write_manifest


def run(rg: str, out_dir: Path, debug: bool = False) -> None:
    artifacts: List[Path] = []

    events = run_az_json(
        ["monitor", "activity-log", "list",
            "--resource-group", rg, "--max-events", "50"],
        debug=debug,
        # Pull activity log events via Azure CLI
    )
    p = out_dir / f"activitylog.{rg}.json"
    write_json(p, events)
    artifacts.append(p)

    write_manifest(out_dir, artifacts)
