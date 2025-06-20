import pandas as pd

# ✅ Load the sample XLS just created
xls_file = 'climate_change_download.xls'
df = pd.read_excel(xls_file)

# ✅ Clean it (same steps)
df.dropna(how='all', inplace=True)
df.dropna(axis=1, how='all', inplace=True)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.convert_dtypes()

# ✅ Save to CSV
cleaned_csv = 'data_cleaned.csv'
df.to_csv(cleaned_csv, index=False)

print(f"✅ Cleaned CSV created: {cleaned_csv}")
