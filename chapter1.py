import time
from PIL import Image

# Generate the number (n)
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number (n): {generated_number}")

# Load the provided image
input_image_path = 'Chapter1.png'  # Replace with the correct path to your image
output_image_path = 'chapter1out.png'

# Open the image and process it
image = Image.open(input_image_path)
pixels = image.load()

width, height = image.size

# Modify pixels by adding the generated number to each color channel
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        pixels[x, y] = (min(r + generated_number, 255), 
                        min(g + generated_number, 255), 
                        min(b + generated_number, 255))

# Save the new image
image.save(output_image_path)

# Sum all the red (r) values in the new image
red_sum = 0
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        red_sum += r

print(f"Sum of red values: {red_sum}")
