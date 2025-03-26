import pandas as pd
import os

INPUT_XLSX = "metadata.xlsx"  # Replace with your actual XLSX file name
OUTPUT_DIR = "raw_files"  # This should match the INPUT_DIR in your existing script

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define a dictionary where keys are sheet names and values are column indexes (starting from 0)
SHEET_COLUMNS = {
    "Sheet1": [0, 2, 4],  # Keep only columns at index 0, 2, and 4 for Sheet1
    "Sheet2": [1, 3],  # Keep columns at index 1 and 3 for Sheet2
    # Add more sheets as needed
}

# Load the Excel file
xlsx = pd.ExcelFile(INPUT_XLSX)

# Convert each sheet to a TSV file with specified columns
for sheet_name in xlsx.sheet_names:
    if sheet_name in SHEET_COLUMNS:
        df = pd.read_excel(xlsx, sheet_name=sheet_name, usecols=lambda x: x in SHEET_COLUMNS[sheet_name])
    else:
        df = pd.read_excel(xlsx, sheet_name=sheet_name)  # Default: Use all columns
    
    tsv_path = os.path.join(OUTPUT_DIR, f"{sheet_name}.tsv")
    df.to_csv(tsv_path, sep="\t", index=False)

print("TSV files have been generated!")
