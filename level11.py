from PIL import Image

file = r'C:\Users\sven-\Desktop\cave.jpg'

# ever odd and even pixel gets seperated and only the black picture 

img = Image.open(file)
new_img1 = []
new_img2 = []

with Image.open(file) as image:
    x_width, y_width = image.size

for x in range(x_width):
    if x % 2:
        offset = 0
    else:
        offset = 1
    for y in range(y_width):
        rgb_pixel = img.getpixel((x, y))
        if (y+offset) % 2:
            new_img1.append(rgb_pixel)
        else:
            new_img2.append(rgb_pixel)

img = Image.new('RGB', (int(x_width), int(y_width/2)), color='black')

z = -1
for x in range(int(x_width)):
    z += 1
    for y in range(int(y_width/2-1)):
        pixel_position = (x, y)
        img.putpixel(pixel_position, new_img1[z])
        z += 1

img.show()