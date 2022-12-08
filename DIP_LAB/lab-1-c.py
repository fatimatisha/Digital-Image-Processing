import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import rgb2gray
#import skimage.color as co
img = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img)
#img_gray = co.rgb2gray(img)

viewer = IV(img_gray)

viewer.show()

