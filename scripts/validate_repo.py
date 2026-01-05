
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List


TALK_DIR_RE = re.compile(r"^\d{4}-[a-z0-9][a-z0-9-]*$")  # e.g. 2026-launch-molsyssuite


@dataclass
class Err:
    msg: str


def fail(errors: List[Err]) -> int:
    for e in errors:
        print(f"ERROR: {e.msg}")
    return 1


def warn(msg: str) -> None:
    print(f"WARNING: {msg}")


def check_file(p: Path, errors: List[Err]) -> None:
    if not p.exists():
        errors.append(Err(f"Missing required file: {p}"))


def check_dir(p: Path, errors: List[Err]) -> None:
    if not p.exists() or not p.is_dir():
        errors.append(Err(f"Missing required directory: {p}"))


def validate_talk_dir(tdir: Path, errors: List[Err], strict: bool) -> None:
    # Required
    for rel in ("README.md", "outline.md", "objectives.md"):
        if not (tdir / rel).exists():
            errors.append(Err(f"{tdir}: missing {rel}"))

    # Recommended dirs
    for d in ("notes", "media"):
        dd = tdir / d
        if strict and (not dd.exists() or not dd.is_dir()):
            warn(f"{tdir}: {d}/ recommended (strict mode expects it).")

    # If media exists, recommend README inside
    media_readme = tdir / "media" / "README.md"
    if (tdir / "media").exists() and strict and not media_readme.exists():
        warn(f"{tdir}: media/ exists but missing media/README.md (external links should be documented).")


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate molsyssuite-talks repository structure.")
    ap.add_argument("--repo-root", default=".", help="Repository root (default: .)")
    ap.add_argument("--strict", action="store_true", help="Stricter checks (recommended for CI).")
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    errors: List[Err] = []

    check_file(root / "README.md", errors)
    check_file(root / "CONTRIBUTING.md", errors)
    check_dir(root / "templates", errors)
    check_file(root / "templates" / "talk-README.md", errors)
    check_file(root / "templates" / "checklist.md", errors)

    check_dir(root / "talks", errors)

    talks_root = root / "talks"
    if talks_root.exists():
        for tdir in sorted(talks_root.iterdir()):
            if not tdir.is_dir() or tdir.name.startswith("."):
                continue

            if not TALK_DIR_RE.match(tdir.name):
                warn(f"{tdir}: directory name does not match 'YYYY-slug' (e.g. 2026-launch-molsyssuite).")
                if args.strict:
                    errors.append(Err(f"{tdir}: invalid talk directory name"))
                    continue

            validate_talk_dir(tdir, errors, args.strict)

    if errors:
        return fail(errors)

    print("OK: repository structure looks good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
