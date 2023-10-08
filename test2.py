from PIL import Image
from numpy import asarray

img = Image.open("lgbt.png")
numpydata = asarray(img)

print(numpydata)