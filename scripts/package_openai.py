#!/usr/bin/env python3
"""Build a reproducible OpenAI skills-only ZIP from the checked-out source."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="ZIP destination")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / ".codex-plugin/plugin.json").read_text())
    if any(key in manifest for key in ("mcpServers", "apps", "hooks")):
        parser.error("This packager only supports skills-only packages.")

    files = [root / name for name in (
        ".codex-plugin/plugin.json", "LICENSE", "README.md",
        "PRIVACY.md", "TERMS.md", "SUPPORT.md",
    )]
    for directory in ("skills", "assets"):
        files.extend(p for p in (root / directory).rglob("*") if p.is_file())
    if not list((root / "skills").glob("*/SKILL.md")):
        parser.error("At least one skill is required.")
    for field in ("composerIcon", "logo"):
        icon = root / manifest["interface"][field]
        if icon.resolve() not in {p.resolve() for p in files}:
            parser.error(f"Unpackaged icon: {field}")

    for path in files:
        if not path.is_file() or path.is_symlink():
            parser.error(f"Expected a regular file: {path}")
    output = args.output.resolve()
    if output == root or root in output.parents:
        parser.error("Choose an output path outside the repository.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(files):
            entry = ZipInfo(path.relative_to(root).as_posix(), (2026, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, path.read_bytes())
    print(f"Built {output} (version {manifest['version']}, {len(files)} files)")


if __name__ == "__main__":
    main()
