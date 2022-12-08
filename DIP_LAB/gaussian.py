import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi

img01= io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.1.04.tiff')

io.imshow(img01)
io.show()

img02= ndi.gaussian_filter(img01,5,truncate=3)

io.imshow(img02)
io.show()
