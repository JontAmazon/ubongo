from PIL import Image
path = 'C:/Users/jonat/Desktop/Code/ubongo/img/flames/_4_original.jpg'
save_path = 'C:/Users/jonat/Desktop/Code/ubongo/img/flames/_4_black.jpg'
imgT = Image.open(path)
img = imgT.convert("RGB")
width, height = img.size[0], img.size[1] 
for i in range(0, width):
    for j in range(0, height):
        data = img.getpixel((i,j))
        if data[0] < 30 and data[1] < 30 and data[2] < 30:
            img.putpixel((i,j),(0, 0, 0))
# img.show()
img.save(save_path)