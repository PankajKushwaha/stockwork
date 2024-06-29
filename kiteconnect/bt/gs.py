import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('ind_niftytotalmarket_list.csv')

# Keep only the "Symbol" column and overwrite the DataFrame with this subset
df = df[['Symbol']]

# Write the DataFrame back to a CSV file without the other columns
df.to_csv('output_file.csv', index=False)

