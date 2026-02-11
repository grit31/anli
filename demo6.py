from PIL import Image

# Load the image
img_path = 'img.png'
img = Image.open(img_path)

# Remove background to create a transparent image
img = img.convert("RGBA")
datas = img.getdata()

new_data = []
for item in datas:
    # Change all white (also shades of whites)
    # to be transparent
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)

# Save the modified image
modified_img_path = 'img_transparent.png'
img.save(modified_img_path)

#modified_img_path
