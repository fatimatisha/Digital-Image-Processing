import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import rgb2lab

img = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\house.tiff')

img_lab = rgb2lab(img)

viewer = IV(img_lab)

viewer.show()

