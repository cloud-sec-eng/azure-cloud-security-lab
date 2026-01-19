import argparse
# Module that builds a CLI interface
from pathlib import Path
# Handle filesystem paths

from azsec_kit.commands.activitylog import run as activitylog_run
from azsec_kit.commands.inventory import run as inventory_run


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="azsec",
        description="Azure Security Lab Toolkit (evidence-first automation)",
    )

    p.add_argument(
        "--debug",
        action="store_true",
        help="Print extra debug details (no secrets).",
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    inv = sub.add_parser(
        "inventory", help="Collect governance inventory evidence.")
    inv.add_argument("--rg", required=True, help="Target resource group name.")
    inv.add_argument("--out", default="reports/week01",
                     help="Output folder for evidence.")

    al = sub.add_parser("activitylog", help="Collect Activity Log evidence.")
    al.add_argument("--rg", required=True, help="Target resource group name.")
    al.add_argument("--out", default="reports/week01",
                    help="Output folder for evidence.")

    return p


def main() -> None:
    p = build_parser()
    args = p.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.cmd == "inventory":
        inventory_run(rg=args.rg, out_dir=out_dir, debug=args.debug)
    elif args.cmd == "activitylog":
        activitylog_run(rg=args.rg, out_dir=out_dir, debug=args.debug)
    else:
        raise ValueError(f"Unknown command: {args.cmd}")
