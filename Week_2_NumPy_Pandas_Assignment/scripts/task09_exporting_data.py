import pandas as pd
from pathlib import Path

df = pd.read_csv("../outputs/task07_cleaned_missing_values.csv")
output_file = Path("../outputs/final_processed_data.csv")

df.to_csv(output_file, index=False)

print("Exported file:", output_file.resolve())
print("\nVerification - exported data:\n", pd.read_csv(output_file))
