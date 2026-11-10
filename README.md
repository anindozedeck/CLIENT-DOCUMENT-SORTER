# Client Document Sorter

A small Python utility that organizes files in a target folder into:

- `Contracts/` — `.docx`, `.doc`
- `Evidence/` — `.jpg`, `.jpeg`, `.png`
- `Filings/` — `.pdf`
- `Correspondence/` — `.txt`, `.eml`
- `Other/` — all other file types

Each moved file is recorded in `sort_log.txt` with a timestamp and its
original and destination paths. Existing files are not overwritten; a numeric
suffix is added if a destination name already exists. The script processes
files in the selected folder, not files inside its subfolders.

## Run

Install Python 3 if it is not already available, then run from PowerShell:

```powershell
python .\Day21_Exercise.py "C:\path\to\client-documents"
```

Back up important documents before the first run. Sorting moves files out of
the target folder, so choose the folder carefully.

## Estimated weekly time saved

**Planning estimate: about 1 hour per week** for a folder of roughly 200 files.
This assumes staff currently spend an average of 20 seconds per file deciding
where it belongs and moving it (about 67 minutes), and spend around 5 minutes
reviewing or starting the automated sort. Actual savings will depend on the
firm's current filing process and how often files need manual review.

## Proposed client price

**One-time build and setup: KSh 25,000.** This proposed fee covers setting up
the script for one workstation and target folder, testing it with representative
sample files, and providing a short handover on how to run it. It does not
include ongoing support, broader document-management integration, or applicable
taxes and travel costs. Confirm the final scope and price with the client before
starting.
