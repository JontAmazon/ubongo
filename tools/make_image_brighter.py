from PIL import Image

path = 'C:/Users/jonat/Desktop/Code/ubongo/img/board_square/2_square.jfif'
save_path = 'C:/Users/jonat/Desktop/Code/ubongo/img/board_square/2_square_brighter.jfif'

img = Image.open(path)
img = img.convert("RGB")
datas = img.getdata()

new_image_data = []
for item in datas:
    # change all background to white and keep all white

    r = min(int(1.20 * item[0]), 255)
    b = min(int(1.20 * item[1]), 255)
    g = min(int(1.20 * item[2]), 255)
    new_image_data.append((r, b, g))

img.putdata(new_image_data)
img.save(save_path)
img.show()