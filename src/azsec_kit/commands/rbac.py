from pathlib import Path
from typing import List

from azsec_kit.lib.azcli import run_az_json, run_az_tsv
from azsec_kit.lib.io import write_json
from azsec_kit.lib.manifest import write_manifest


def run(rg: str, out_dir: Path, debug: bool = False) -> None:
    artifacts: List[Path] = []

    sub_id = run_az_tsv(["account", "show", "--query", "id"], debug=debug)
    rg_id = run_az_tsv(["group", "show", "--name", rg,
                       "--query", "id"], debug=debug)

    sub_assignments = run_az_json(
        ["role", "assignment", "list", "--scope", f"/subscriptions/{sub_id}"], debug=debug)
    p1 = out_dir / f"rbac.role-assignments.subscription.{sub_id}.json"
    write_json(p1, sub_assignments)
    artifacts.append(p1)

    rg_assignments = run_az_json(
        ["role", "assignment", "list", "--scope", rg_id], debug=debug)
    p2 = out_dir / f"rbac.role-assignments.rg.{rg}.json"
    write_json(p2, rg_assignments)
    artifacts.append(p2)

    for role_name in ["Reader", "Contributor", "Owner"]:
        role_def = run_az_json(
            ["role", "definition", "list", "--name", role_name], debug=debug)
        p = out_dir / f"rbac.role-definition.{role_name}.json"
        write_json(p, role_def)
        artifacts.append(p)

    write_manifest(out_dir, artifacts)
