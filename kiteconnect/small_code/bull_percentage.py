import sys

# Check if there are exactly two command-line arguments
if len(sys.argv) != 3:
    print("Usage: python calculate_percentage.py <total> <part>")
    sys.exit(1)

# Parse the command-line arguments as floats
try:
    total = float(sys.argv[1])
    part = float(sys.argv[2])
except ValueError:
    print("Both arguments must be numeric")
    sys.exit(1)

# Calculate the percentage
percentage = ((part / total) * 100) - 100

# Print the result
print(f"{part} is {percentage:.2f}% of {total}")

