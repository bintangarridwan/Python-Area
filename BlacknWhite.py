from PIL import Image

img = Image.open("Assets/Luffy.jpg")
bnw = img.convert("L")
bnw.save('bnw_foto.jpg')
bnw.show