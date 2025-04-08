import pandas as pd
import os

INPUT_XLSX = "metadata.xlsx"  # Replace with your actual XLSX file name
OUTPUT_DIR = "raw_files"  # This should match the INPUT_DIR in your existing script

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define a dictionary where keys are sheet names and values are column indexes (starting from 0)
WANTED_FILES = [
    {"sheet_name": "VJDBCore", "cols": ["vjdbv0.3_field_id",	"vjdbv0.3_name",	"vjdbv0.3_description",	"vjdbv0.3_fields_type",	"vjdbv0.3_privacy"], "filename": "VJDBCore"},
    {"sheet_name": "VJDBCore", "cols": ["vjdbv0.3_field_id",	"vjdbv0.3_name",	"vjdbv0.3_tags"], "filename": "Tags"},
    {"sheet_name": "VJDBCore", "cols": ["vjdbv0.3_field_id",	"vjdbv0.3_name",	"vjdbv0.3_description", "vjdbv0.3_tags", "vjdbv0.3_privacy"], "filename": "Frontend"},
    {"sheet_name": "VJDBCore", "cols": ["vjdbv0.3_field_id",	"vjdbv0.3_name",	"vjdbv0.3_description", "vjdbv0.3_tags", "vjdbv0.3_privacy", "ena_submission_fieldtype", "ena_submission_requiredness"], "filename": "Submission"},
    {"sheet_name": "VJDBCore", "cols": ["vjdbv0.3_name","vjdbv0.3_tags","vjdbv0.3_description",], "filename": "Fellow"},
    ]


# Load the Excel file
xlsx = pd.ExcelFile(INPUT_XLSX)

# Convert each sheet to a TSV file with specified columns

for wanted_file in WANTED_FILES:
    print(wanted_file)
    if wanted_file["sheet_name"] in xlsx.sheet_names:
        df = pd.read_excel(xlsx, sheet_name=wanted_file["sheet_name"], usecols=lambda x: x in wanted_file["cols"], skiprows=3)
        tsv_path = os.path.join(OUTPUT_DIR, f"{wanted_file['filename']}.tsv")
        df.to_csv(tsv_path, sep="\t", index=False)
    else: 
        print("No such sheet: ", wanted_file.sheet_name)
        


print("TSV files have been generated!")
