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

plt.subplot(2,3,1)
plt.axis('off')
plt.title('Color image')
plt.imshow(img_01)

plt.subplot(2,3,2)
plt.axis('off')
plt.title('RED channel image')
red=fl.prewitt(r)
plt.imshow(red,cmap='gray')

plt.subplot(2,3,3)
plt.axis('off')
plt.title('GREEN channel image')
ged=fl.prewitt(g)
plt.imshow(ged,cmap='gray')

plt.subplot(2,3,4)
plt.axis('off')
plt.title('BLUE channel image')
bed=fl.prewitt(b)
plt.imshow(bed,cmap='gray')


plt.subplot(2,3,5)
plt.axis('off')
plt.title('Grayscale image')
grayed=fl.prewitt(img_gray)
plt.imshow(grayed, cmap='gray')


plt.subplot(2,3,6)
plt.axis('off')
plt.title('BLUE only image')
bedd=fl.prewitt(b_img)
plt.imshow(bedd)



plt.show()

