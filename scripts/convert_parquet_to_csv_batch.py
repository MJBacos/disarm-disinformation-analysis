import os
import pandas as pd

# === Configuration ===
# Automatically use the script's current folder
script_dir = os.path.dirname(os.path.abspath(__file__))
input_parquet_dir = script_dir
output_csv_dir = os.path.join(script_dir, "csv_output")

# Create output folder if it doesn't exist
os.makedirs(output_csv_dir, exist_ok=True)

# Initialize result list
converted_files = []

# Loop through all .parquet files in the input directory
for filename in os.listdir(input_parquet_dir):
    if filename.endswith(".parquet"):
        input_path = os.path.join(input_parquet_dir, filename)
        output_filename = filename.replace(".parquet", ".csv")
        output_path = os.path.join(output_csv_dir, output_filename)

        try:
            df = pd.read_parquet(input_path)
            df.to_csv(output_path, index=False)
            converted_files.append(f"✅ Converted: {filename} → {output_filename}")
        except Exception as e:
            converted_files.append(f"❌ Failed: {filename} - Error: {e}")

# Print conversion summary
print("\nBatch Conversion Summary:")
for entry in converted_files:
    print(entry)

print("\n✅ All conversions completed!")
