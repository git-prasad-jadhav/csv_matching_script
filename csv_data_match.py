import os
import pandas as pd

# Define the folder path, master file name, and output file path
folder_path = # folder path
master_file_name = # Master file name
output_file_path = # output file name with path

# Specify the columns in the master file for matching
match_columns_master = ['AppId', 'Id']

master_file_path = os.path.join(folder_path, master_file_name)

# Read the master file
try:
    master_df = pd.read_csv(master_file_path)
    print("Master file read successfully.")
except Exception as e:
    print(f"Error while reading master file '{master_file_name}': {e}")
    master_df = None  # Set master_df to None if reading fails

# Ensure master_df is valid before proceeding
if master_df is not None:
    for col in match_columns_master:
        if col not in master_df.columns:
            print(f"Error: Column '{col}' not found in the master file.")
else:
    print("Exiting script as the master file could not be loaded.")
    exit()

result_df = master_df.copy()
result_df['SourseFile'] = ''
result_df['MatchedColumn'] = ''
result_df['MatchedValue'] = ''
print(result_df.columns)

master_values_dict = {}
for col in match_columns_master:
    try:
        master_values_dict[col] = master_df[col].dropna().unique()
        # print(f"Distinct master values items", master_values_dict.items())
    except Exception as e:
        print(f"Error processing column '{col}': {e}")

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.csv') and file_name != master_file_name:
                file_path = os.path.join(root, file_name)
                # print(file_path)

                # Try different delimiters to read the CSV file
                df = None
                for delimiter in [',', ';', '\t', '|']:
                    try:
                        df = pd.read_csv(file_path, delimiter=delimiter)
                        # print(df)
                        break
                    except Exception:
                        continue

                # If the file could not be read, skip to the next file
                if df is None:
                    print(f"Skipping file '{file_name}': Unable to read with any delimiter.")
                    continue

                # Check for matches in each column
                for col_master, master_values in master_values_dict.items():
                    for col_other in df.columns:
                        matching_rows = df[df[col_other].isin(master_values)]
                        if not matching_rows.empty:
                            # Update the master DataFrame with matching details
                            matched_values = matching_rows[col_other].unique()
                            mask = result_df[col_master].isin(matched_values)
                            result_df.loc[mask, 'SourceFile'] = file_path
                            result_df.loc[mask, 'MatchedColumn'] = col_other
                            result_df.loc[mask, 'MatchedValue'] = result_df.loc[mask, col_master]

# Save the result DataFrame to the output file
# result_df.to_csv(output_file_path, index=False)
print(f"Matching records have been saved to '{output_file_path}'.")