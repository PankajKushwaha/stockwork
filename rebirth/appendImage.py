from PIL import Image
import os

# Get a list of all PNG files in the current directory
png_files = [file for file in os.listdir() if file.endswith('.png')]

if len(png_files) == 0:
    print("No PNG files found in the current directory.")
else:
    # Open the first image to get dimensions
    first_image = Image.open(png_files[0])
    width, height = first_image.size

    # Create a blank canvas to append images vertically
    result = Image.new('RGB', (width, height * len(png_files)))

    # Loop through each PNG file and append it vertically
    for idx, png_file in enumerate(png_files):
        image = Image.open(png_file)
        result.paste(image, (0, idx * height))

    # Save the resulting image
    result.save('vertical_appended.png')

    print(f"Vertical appended image saved as 'vertical_appended.png'.")

