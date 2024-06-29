# Open the file in read mode
from myLib import *
with open("cross_200ma.txt", "r") as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Print the list of lines


line=[]

for text in lines:
    cleaned_text = text.replace(" ", "").replace("\n", "").replace("\t", "")
    line.append(cleaned_text)

print(line)

save_screenshot(line)
