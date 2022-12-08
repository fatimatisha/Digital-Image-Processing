import skimage.color as co
import skimage.io as io

em = io.imread('D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\4.1.04.tiff')
e = co.rgb2gray(em)
#f=co.rgb2ind(em)
io.imshow(em)
io.show()
