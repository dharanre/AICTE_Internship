import pandas as pd

# ✅ Create a sample climate_change_download.xls similar to GitHub
# This is dummy data to simulate real climate change data
data = {
    'Country': ['USA', 'India', 'China'],
    'Year': [2020, 2020, 2020],
    'CO2_Emissions': [5000, 2500, 8000],
    'Methane_Emissions': [300, 500, 700]
}

# Create DataFrame
df = pd.DataFrame(data)

# Export to XLS
xls_file = 'climate_change_download.xls'
df.to_excel(xls_file, index=False)

print(f"✅ Sample file created: {xls_file}")
