from PIL import Image
import os

def append_images_vertically(image_files, output_file):
    images = [Image.open(img) for img in image_files if img.endswith('.png')]

    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new('RGB', (max_width, total_height), color='white')

    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        y_offset += img.size[1]

    new_image.save(output_file)

if __name__ == "__main__":
    current_directory = os.getcwd()
    image_files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
    output_file = "appended_vertically.png"
    append_images_vertically(image_files, output_file)

