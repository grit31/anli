from PIL import Image

# Load the images
living_space_image = Image.open("1.jpg")
medicine_image = Image.open("img.png")

# Convert the medicine image to "RGBA" if it's not already to handle transparency correctly
medicine_image = medicine_image.convert("RGBA")
medicine_image = medicine_image.resize((100, 100))

# Determine the position to paste the medicine image on the living space image
# Top left corner of the medicine image will be at (250, 300) in the living space image
position = (300, 300)

# Paste the medicine image onto the living space image, using alpha channel as mask
living_space_image.paste(medicine_image, position, medicine_image.split()[3])

# Save the modified image
living_space_image.save("merged_image_correct_2.jpg")

# Display the modified image
living_space_image.show()
