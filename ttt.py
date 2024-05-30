import imghdr
from PIL import Image


a = imghdr.what('R-C.jpg')
print(a)
img = Image.open('R-C.jpg')
img.save('real.jpg')
b = imghdr.what('real.jpg')
print(b)