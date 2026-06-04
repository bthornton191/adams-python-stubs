"""
docs_setup.py — Build Adams Python API docs from .pyi stubs.

Griffe (the static analysis backend used by mkdocstrings) only looks for
modules as `module.py` or `module/__init__.py(i)`.  It does NOT discover
bare `.pyi` stub files on their own.  To work around this, we temporarily
create an empty `.py` shim alongside each `.pyi` so that griffe finds the
module and then automatically picks up the `.pyi` as its companion stubs
file.  The shims are deleted after the build completes.

Usage
-----
    # Build docs (creates shims, runs mkdocs build, deletes shims):
    python scripts/docs_setup.py

    # Pass extra args directly to mkdocs (e.g. mkdocs serve):
    python scripts/docs_setup.py -- serve

    # Only create shims (e.g. to run mkdocs manually afterwards):
    python scripts/docs_setup.py --shims-only

    # Only delete any leftover shims:
    python scripts/docs_setup.py --clean
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SHIM_COMMENT = "# Documentation shim — see {pyi} for type stub content\n"


def create_shims() -> list[Path]:
    created = []
    for pyi in sorted(REPO_ROOT.glob("*.pyi")):
        py = pyi.with_suffix(".py")
        if not py.exists():
            py.write_text(SHIM_COMMENT.format(pyi=pyi.name), encoding="utf-8")
            created.append(py)
    if created:
        print(f"[docs_setup] Created {len(created)} shim(s).")
    return created


def clean_shims() -> None:
    removed = []
    for pyi in sorted(REPO_ROOT.glob("*.pyi")):
        py = pyi.with_suffix(".py")
        if py.exists():
            content = py.read_text(encoding="utf-8").strip()
            # Only delete files that are pure shims (single comment line).
            # Guards against accidentally removing real .py files.
            if content.startswith("# Documentation shim"):
                py.unlink()
                removed.append(py.name)
    if removed:
        print(f"[docs_setup] Removed {len(removed)} shim(s).")
    else:
        print("[docs_setup] No shims to remove.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--shims-only",
        action="store_true",
        help="Create shims but do not run mkdocs.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove leftover shims and exit.",
    )
    parser.add_argument(
        "mkdocs_args",
        nargs="*",
        metavar="ARG",
        help="Arguments forwarded to mkdocs (default: build).",
    )
    args = parser.parse_args()

    if args.clean:
        clean_shims()
        return

    create_shims()

    if args.shims_only:
        return

    mkdocs_cmd = ["mkdocs"] + (args.mkdocs_args or ["build"])
    try:
        result = subprocess.run(mkdocs_cmd, cwd=REPO_ROOT)
    finally:
        # Always clean up shims, even if mkdocs fails.
        clean_shims()

    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
