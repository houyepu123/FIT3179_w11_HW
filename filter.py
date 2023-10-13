import pandas as pd

df = pd.read_csv("co2-emissions-vs-gdp.csv")
# Replace empty strings with NaN
df.replace("", pd.NA, inplace=True)

# Drop rows where either 'Annual CO₂ emissions (per capita)' or 'GDP per capita' columns are NaN
filtered_df = df.dropna(subset=['Annual CO₂ emissions (per capita)', 'GDP per capita'])
filtered_df = df[df['Year'] == 2018]
filtered_df.to_csv("co2-emissions-vs-gdp_filter.csv", index=False)
