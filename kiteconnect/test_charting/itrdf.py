import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3, 4, 5, 6, 2, 8, 9, 10],
        'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'i']}
df = pd.DataFrame(data)

# Iterate over rows
for index, row in df[4:].iterrows():
    #print(index,row['A'], row['B'])
    sample = list(df[0:index+1]['A'])

    if sample[-1] >=sample[-2] >= sample[-3]:
        print("working")
    else:
        print("still working")
    
    print(list(df[0:index+1]['A']))
    print(row['A'])
