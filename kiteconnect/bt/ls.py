# Open the file and read its contents as a list of strings
with open('output_file.csv', 'r') as file:
    file_as_list = file.readlines()

# Strip newline characters from each line
file_as_list = ["NSE:"+line.strip() for line in file_as_list]

# Now, file_as_list contains the file content as a list of strings
print(file_as_list)

