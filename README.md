# 📁 Folder Inventory Generator

Python script that analyzes a folder structure and generates an Excel file containing information about the most recent file found in each directory.

## 🚀 Features

* Analyzes a base directory.
* Supports folder structures with up to **3 levels**.
* Detects the most recently modified file in each folder.
* Records the file name and modification date.
* Handles folders without subdirectories.
* Generates an Excel file automatically.
* Uses `pandas` for data processing and Excel generation.

## 🛠️ Technologies

* Python 3
* Pandas
* OS module
* Datetime

## 📂 How it works

The script starts from a base directory and analyzes its folder structure.

For each directory, it searches for the most recently modified file and stores the information in a dataset.

The resulting information includes:

* Level 1 folder
* Level 2 folder
* Level 3 folder
* Most recent file
* Modification date

The collected data is then converted into a Pandas DataFrame and exported to an Excel file.

## 📋 Example output

The generated Excel file contains columns similar to:

| Level 1      | Level 2   | Level 3 | Most Recent File | Modification Date |
| ------------ | --------- | ------- | ---------------- | ----------------- |
| Department A | Reports   | 2026    | report.xlsx      | 2026-09-15        |
| Department A | Documents |         | document.pdf     | 2026-09-12        |
| Department B |           |         | data.xlsx        | 2026-09-10        |

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/folder-inventory-generator.git
cd folder-inventory-generator
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
python -m pip install pandas openpyxl
```

## ▶️ Usage

1. Open `folder_inventory.py`.
2. Edit the `ruta_base` variable near the top of the file with the absolute path of the folder you want to analyze. On Windows, use a raw string (`r"..."`) so that backslashes are interpreted correctly:

```python
ruta_base = r"C:\Users\your-user\Documents\folder-to-analyze"
```

For example:

```python
ruta_base = r"C:\Users\erikc\Documents\GitHub"
```

The folder must exist and the user running the script must have permission to read it.

Run the script from the project directory:

```powershell
cd C:\path\to\Folder-Inventory-Generator
python folder_inventory.py
```

The script will generate:

```text
inventario_carpetas_rapido.xlsx
```

## ⚠️ Notes

The script is currently designed to analyze a fixed folder structure of up to three levels rather than recursively traversing all subdirectories.

This approach was chosen to avoid unnecessarily scanning deeper directory structures.

## 📌 Future improvements

* Allow the base directory to be provided as a command-line argument.
* Make the number of directory levels configurable.
* Improve error handling.
* Add configurable output file names.
* Add file type filtering.
* Add a graphical interface.
* Add more information about each file.

## 👨‍💻 Author

**Erik**

This project was created as a small Python automation tool for analyzing directory structures and exporting useful information to Excel.
