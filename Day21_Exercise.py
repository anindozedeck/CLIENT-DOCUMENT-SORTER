"""Sort files in a folder into document-type subfolders."""

import argparse
import shutil
from datetime import datetime
from pathlib import Path


CATEGORIES = {
    ".docx": "Contracts",
    ".doc": "Contracts",
    ".jpg": "Evidence",
    ".jpeg": "Evidence",
    ".png": "Evidence",
    ".pdf": "Filings",
    ".txt": "Correspondence",
    ".eml": "Correspondence",
}
LOG_NAME = "sort_log.txt"


def _available_destination(destination: Path) -> Path:
    """Choose a non-existing path instead of overwriting an existing file."""
    if not destination.exists():
        return destination

    number = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem} ({number}){destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        number += 1


def sort_folder(folder: Path) -> int:
    """Move top-level files in *folder* into category folders and log each move."""
    folder = folder.expanduser().resolve()
    if not folder.is_dir():
        raise NotADirectoryError(f"Target folder does not exist: {folder}")

    log_path = folder / LOG_NAME
    moved_count = 0
    for source in sorted(folder.iterdir()):
        if not source.is_file() or source == log_path:
            continue

        category = CATEGORIES.get(source.suffix.lower(), "Other")
        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)
        destination = _available_destination(destination_folder / source.name)
        shutil.move(str(source), str(destination))

        timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
        with log_path.open("a", encoding="utf-8", newline="") as log_file:
            log_file.write(
                f"{timestamp}\t{source}\t{destination}\n"
            )
        moved_count += 1

    return moved_count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sort files into Contracts, Evidence, Filings, "
        "Correspondence, and Other folders."
    )
    parser.add_argument("folder", type=Path, help="Folder containing files to sort")
    args = parser.parse_args()
    moved_count = sort_folder(args.folder)
    print(f"Moved {moved_count} file(s). Log: {args.folder.resolve() / LOG_NAME}")


if __name__ == "__main__":
    main()