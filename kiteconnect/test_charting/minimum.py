my_dict = {'a': 10, 'b': 5, 'c': 3, 'd': 7, 'e': 8, 'f': 1, 'g': 9, 'h': 4, 'i': 2, 'j': 6}

# Sort the dictionary items by their values
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])

# Get the ten minimum values
ten_min_values = sorted_items[:10]

print(ten_min_values)

