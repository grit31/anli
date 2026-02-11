# from PIL import Image
#
# # Load the images
# living_space_image = Image.open("1.jpg")
# medicine_image = Image.open("img.png")
#
# # Convert the medicine image to "RGBA" to handle transparency
# medicine_image = medicine_image.convert("RGBA")
#
# # Create a mask to extract the medicine bottle
# # Assuming the background is white, we can create a mask by comparing each pixel to white
# threshold = 200  # Threshold for determining 'white' might need adjusting
# mask = Image.eval(medicine_image, lambda px: 255 if px < threshold else 0)
#
# # Use the mask to extract the medicine bottle
# medicine_extracted = Image.composite(medicine_image, Image.new('RGBA', medicine_image.size, (0, 0, 0, 0)), mask)
#
# # Resize the extracted medicine image to a new size, for example 100x100 pixels
# new_size = (100, 100)
# medicine_extracted_resized = medicine_extracted.resize(new_size)
#
# # Rotate the resized extracted medicine image by 45 degrees
# medicine_extracted_rotated = medicine_extracted_resized.rotate(45, expand=True)
#
# # Determine the position to paste the extracted and rotated medicine image on the living space image
# position = (800, 950)
#
# # Paste the extracted and rotated medicine image onto the living space image, using the alpha channel as the mask
# living_space_image.paste(medicine_extracted_rotated, position, medicine_extracted_rotated)
#
# # Save the modified image
# living_space_image.save("merged_image_cutout_4.jpg")
#
# # Display the modified image
# living_space_image.show()


from PIL import Image, ImageChops

# Load the images
living_space_image = Image.open("1.jpg")
medicine_image = Image.open("img.png")

# Convert the medicine image to "RGBA" to handle transparency
medicine_image = medicine_image.convert("RGBA")

# Assuming the background is white, we can create a mask by subtracting the image from a white background
white_background = Image.new("RGBA", medicine_image.size, (255, 255, 255, 255))
mask = ImageChops.difference(medicine_image, white_background)
mask = mask.convert("L")  # Convert to grayscale
mask = Image.eval(mask, lambda x: 255 if x > 50 else 0)  # Create a binary 'mask' based on a threshold

# Use the mask to extract the medicine bottle
medicine_extracted = Image.composite(medicine_image, Image.new('RGBA', medicine_image.size, (0, 0, 0, 0)), mask)

# Resize and rotate the extracted medicine image as needed
new_size = (100, 100)
medicine_extracted_resized = medicine_extracted.resize(new_size)
medicine_extracted_rotated = medicine_extracted_resized.rotate(45, expand=True)

# Determine the position to paste the extracted and rotated medicine image on the living space image
position = (250, 300)

# Paste the extracted and rotated medicine image onto the living space image, using the alpha channel as the mask
living_space_image.paste(medicine_extracted_rotated, position, medicine_extracted_rotated)

# Save the modified image
#living_space_image.save("/mnt/data/merged_image_cutout_corrected.jpg")

# Display the modified image
living_space_image.show()
