import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 7, 5, 5, 6, 7, 8, 9, 10]}

df = pd.DataFrame(data)

# Define the range (e.g., first 5 rows)
start_range = 0
end_range = 5

# Select the range of values in column 'A'
values_in_range = df['A'][start_range:end_range]

# Check if the values in the range are in increasing order or remain the same
increasing_order = all(x <= y for x, y in zip(values_in_range, values_in_range[1:]))

if increasing_order:
    print("Values in the range of column 'A' are in increasing order or remain the same.")
else:
    print("Values in the range of column 'A' are not in increasing order or remain the same.")


