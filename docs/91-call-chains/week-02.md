# Week 02 — Call Chains

## rbac
Terminal
→ `azsec rbac --rg <rg> --out <dir>`
→ `src/azsec_kit/cli.py:main()`
→ `argparse` sets `args.cmd="rbac"`
→ `src/azsec_kit/commands/rbac.py:run()`
→ `src/azsec_kit/lib/azcli.py:run_az_tsv()` (subscription id, rg id)
→ `src/azsec_kit/lib/azcli.py:run_az_json()` (role assignments + role definitions)
→ `src/azsec_kit/lib/io.py:write_json()`
→ `src/azsec_kit/lib/manifest.py:write_manifest()` → `manifest.json`

## policy
Terminal
→ `azsec policy --rg <rg> --out <dir>`
→ `src/azsec_kit/cli.py:main()`
→ `argparse` sets `args.cmd="policy"`
→ `src/azsec_kit/commands/policy.py:run()`
→ `lib/azcli.py:run_az_tsv()` (rg id)
→ `lib/azcli.py:run_az_json()` (policy assignment list + state summarize)
→ `lib/io.py:write_json()`
→ `lib/manifest.py:write_manifest()` → `manifest.json`
