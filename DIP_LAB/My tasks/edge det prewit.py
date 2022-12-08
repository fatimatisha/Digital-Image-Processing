import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.filters as fl




img_01 = plt.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.2.07.tiff')
plt.title('RGB Color image')
plt.imshow(img_01)

vg = rgb2gray(img_01)
vel=fl.prewitt(vg)
plt.imshow(vel)
plt.show()
