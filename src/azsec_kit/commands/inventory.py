from pathlib import Path
from typing import List

from azsec_kit.lib.azcli import run_az_json
from azsec_kit.lib.io import write_json
from azsec_kit.lib.manifest import write_manifest


def run(rg: str, out_dir: Path, debug: bool = False) -> None:
    artifacts: List[Path] = []

    account = run_az_json(["account", "show"], debug=debug)
    p1 = out_dir / "account.show.json"
    # p1 is the file path you will write
    write_json(p1, account)
    # writes the JSON to disk
    artifacts.append(p1)
    # records that file for the manifest

    groups = run_az_json(["group", "list"], debug=debug)
    p2 = out_dir / "group.list.json"
    write_json(p2, groups)
    artifacts.append(p2)

    rg_obj = run_az_json(["group", "show", "--name", rg], debug=debug)
    p3 = out_dir / f"group.show.{rg}.json"
    write_json(p3, rg_obj)
    artifacts.append(p3)

    write_manifest(out_dir, artifacts)
