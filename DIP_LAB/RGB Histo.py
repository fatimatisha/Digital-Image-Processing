import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import skimage.exposure as ex


img_01 = plt.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img_01)

r = img_01[:,:,0]
g = img_01[:,:,1]
b = img_01[:,:,2]


plt.subplot(4,5,1)
plt.axis('off')
plt.title('Color image')
plt.imshow(img_01)

plt.subplot(4,5,2)
plt.axis('off')
plt.title('RED channel image')
plt.imshow(r,cmap='gray')

plt.subplot(4,5,3)
plt.axis('off')
plt.title('RED image Histogram')
plt.hist(r.flatten(), bins=256)


plt.subplot(4,5,4)
plt.axis('off')
plt.title('Equalized Histogram')
r_eq= ex.equalize_hist(r)
plt.hist(r_eq.flatten(), bins=256)


plt.subplot(4,5,5)
plt.axis('off')
plt.title('GREEN channel image')
plt.imshow(g,cmap='gray')

plt.subplot(4,5,6)
plt.axis('off')
plt.title('GREEN image Histogram')
plt.hist(g.flatten(), bins=256)

plt.subplot(4,5,7)
plt.axis('off')
plt.title('Equalized Histogram')
g_eq= ex.equalize_hist(r)
plt.hist(g_eq.flatten(), bins=256)


plt.subplot(4,5,8)
plt.axis('off')
plt.title('BLUE channel image')
plt.imshow(b,cmap='gray')

plt.subplot(4,5,9)
plt.axis('off')
plt.title('BLUE image Histogram')
plt.hist(b.flatten(), bins=256)

plt.subplot(4,5,10)
plt.axis('off')
plt.title('Equalized Histogram')
b_eq= ex.equalize_hist(r)
plt.hist(b_eq.flatten(), bins=256)

rcon_img = np.dstack((r,g,b))

plt.subplot(4,5,11)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img)

plt.subplot(4,5,12)
plt.axis('off')
plt.title('Reconstruced image Histogram')
plt.hist(rcon_img.flatten(), bins=256)


plt.subplot(4,5,13)
plt.axis('off')
plt.title('Equalized Histogram')
rcon_eq= ex.equalize_hist(r)
plt.hist(rcon_eq.flatten(), bins=256)

plt.subplot(4,5,14)
plt.axis('off')
plt.title('Grayscale image')
plt.imshow(img_gray, cmap='gray')

plt.subplot(4,5,15)
plt.axis('off')
plt.title('Grayscale image Histogram')
plt.hist(img_gray.flatten(), bins=256)


plt.subplot(4,5,16)
plt.axis('off')
plt.title('Equalized Histogram')
gray_eq= ex.equalize_hist(r)
plt.hist(gray_eq.flatten(), bins=256)


plt.show()

