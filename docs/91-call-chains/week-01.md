# Week 01 — Call Chain (azsec)

## Inventory command
Terminal
→ `azsec inventory --rg <rg> --out <dir>`
→ `src/azsec_kit/cli.py:main()`
→ `src/azsec_kit/cli.py:build_parser()`
→ `argparse` parses args into `args`
→ `src/azsec_kit/commands/inventory.py:run(rg, out_dir, debug)`
→ `src/azsec_kit/lib/azcli.py:run_az_json([...])`
→ `src/azsec_kit/lib/azcli.py:run_az([...])`
→ `subprocess.run(["az", ...])`
→ `src/azsec_kit/lib/io.py:write_json(...)` (writes evidence files)
→ `src/azsec_kit/lib/manifest.py:write_manifest(...)`
→ `src/azsec_kit/lib/manifest.py:sha256_file(...)`
→ `src/azsec_kit/lib/io.py:write_json(manifest.json)`

## Activitylog command
Terminal
→ `azsec activitylog --rg <rg> --out <dir>`
→ `src/azsec_kit/cli.py:main()`
→ `src/azsec_kit/commands/activitylog.py:run(...)`
→ `lib/azcli.py:run_az_json([...])` → `subprocess.run(...)`
→ `lib/io.py:write_json(activitylog...)`
→ `lib/manifest.py:write_manifest(...)` → `manifest.json`
