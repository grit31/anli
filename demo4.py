from PIL import Image

# Load the images
living_space_image = Image.open("1.jpg")
medicine_image = Image.open("img.png")

# Convert the medicine image to "RGBA" to handle transparency
medicine_image = medicine_image.convert("RGBA")

# Resize the medicine image to a new size, for example 100x100 pixels
new_size = (100, 100)
medicine_image_resized = medicine_image.resize(new_size)

# Rotate the resized medicine image by 45 degrees without any black filling
medicine_image_rotated = medicine_image_resized.rotate(0, expand=True)

# Determine the position to paste the rotated medicine image on the living space image
# The position can be modified as needed
position = (800, 950)

# Paste the rotated medicine image onto the living space image, using the alpha channel as the mask
living_space_image.paste(medicine_image_rotated, position, medicine_image_rotated)

# Save the modified image
living_space_image.save("merged_image_adjustable_3.jpg")

# Display the modified image
living_space_image.show()
