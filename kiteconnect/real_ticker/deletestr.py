import csv

def delete_lines_starting_with(filename, starting_string):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        lines = [line for line in reader if not line[0].startswith(starting_string)]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

# Example usage:
filename = "tick.csv"
starting_string = "13:29:"  # Specify the string to match the lines you want to delete
delete_lines_starting_with(filename, starting_string)

