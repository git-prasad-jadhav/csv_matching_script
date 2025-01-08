# CSV Matching Script

This Python script automates the process of matching records between a master CSV file and multiple other CSV files (recursively scanned across folders). It outputs detailed results, making it a valuable tool for data reconciliation, quality assurance, and validation tasks.

---

## Features
- **Recursive Folder Scanning**: Automatically scans a folder and its subfolders for CSV files.
- **Flexible Matching**: Matches based on specified columns in the master file.
- **Detailed Output**: Includes the file name, matching column, and matched value in the output.
- **Multi-Delimiter Support**: Handles CSV files with delimiters like `,`, `;`, `\t`, and `|`.

---

## How It Works
1. **Input**: A folder containing:
   - A master CSV file (e.g., `Master.csv`).
   - Other CSV files to compare against the master file.

2. **Matching**:
   - Checks specified columns (`AppId`, `ID`) in the master file.
   - Finds matching values in all other CSV files across all columns.

3. **Output**: Generates a CSV file with:
   - All rows from the master file.
   - Additional columns for:
     - `SourceFile`: File where the match was found.
     - `MatchedColumn`: Column with the matching value.
     - `MatchedValue`: Exact value that matched.

---

## Prerequisites
- Python 3.x installed on your system.
- Required libraries: `pandas`.

Install dependencies using:
```bash
pip install pandas
