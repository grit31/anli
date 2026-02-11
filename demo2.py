from PIL import Image

# Load the images
living_space_image = Image.open("1.jpg")
medicine_image = Image.open("img.png")

# Resize the medicine image
medicine_image_resized = medicine_image.resize((100, 100))  # Resize to 100x100 pixels

# Rotate the medicine image by 45 degrees
medicine_image_rotated = medicine_image_resized.rotate(45, expand=True)

# Convert the rotated medicine image to "RGBA" to handle transparency correctly
medicine_image_rotated = medicine_image_rotated.convert("RGBA")

# Determine the position to paste the medicine image on the living space image
# Top left corner of the medicine image will be at (250, 300) in the living space image
position = (250, 300)

# Paste the medicine image onto the living space image, using alpha channel as mask
living_space_image.paste(medicine_image_rotated, position, medicine_image_rotated)

# Save the modified image
living_space_image.save("merged_image.jpg")

# Display the modified image
living_space_image.show()
