import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.filters as fl

img_01 = plt.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img_01)

r = img_01[:,:,0]
g = img_01[:,:,1]
b = img_01[:,:,2]

z_r = np.zeros_like(r)
z_g = np.zeros_like(g)
z_b = np.zeros_like(b)

r_img = np.dstack((r,z_g,z_b))
g_img = np.dstack((z_r,g,z_b))
b_img = np.dstack((z_r,z_g,b))

plt.subplot(2,5,1)
plt.axis('off')
plt.title('RGB Color image')
plt.imshow(img_01)

plt.subplot(2,5,2)
plt.axis('off')
plt.title('RED channel image')
plt.imshow(r,cmap='gray')

plt.subplot(2,5,3)
plt.axis('off')
plt.title('GREEN channel image')
plt.imshow(g,cmap='gray')

plt.subplot(2,5,4)
plt.axis('off')
plt.title('BLUE channel image')
plt.imshow(b,cmap='gray')

re=fl.prewitt(r)
ge=fl.prewitt(g)
be=fl.prewitt(b)

plt.subplot(2,5,5)
plt.axis('off')
plt.title('red channel image')
plt.imshow(re,cmap='gray')

plt.subplot(2,5,6)
plt.axis('off')
plt.title('green channel image')
plt.imshow(ge,cmap='gray')

plt.subplot(2,5,7)
plt.axis('off')
plt.title('BLUE channel image')
plt.imshow(be,cmap='gray')

plt.show()

