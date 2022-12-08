import numpy as np
import skimage.exposure as ex
import matplotlib.pyplot as plt
from skimage.color import convert_colorspace

img_01=plt.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.1.01.tiff')
img_hsv = convert_colorspace(img_01, 'RGB','HSV')
h=img_hsv[: , : , 0]
s=img_hsv[: , : , 1]
v=img_hsv[: , : , 2]

h_2=ex.equalize_hist(h)
s_2=ex.equalize_hist(s)
v_2=ex.equalize_hist(v)

recon_img=h_2+s_2+v_2

plt.subplot(4,4,1)
plt.axis('off')
plt.title('RGB image')
plt.imshow(img_01)

plt.subplot(4,4,2)
plt.axis('off')
plt.title('hsv image')
plt.imshow(img_hsv)

plt.subplot(4,4,3)
plt.axis('off')
plt.title('Hue channel image')
plt.imshow(h)

plt.subplot(4,4,4)
plt.axis('off')
plt.title('Saturation channel image')
plt.imshow(s)

plt.subplot(4,4,5)
plt.axis('off')
plt.title('Value channel image')
plt.imshow(v)

plt.subplot(4,4,6)
plt.axis('off')
plt.title('hue channel Equalize image')
plt.imshow(h_2)

plt.subplot(4,4,7)
plt.axis('off')
plt.title('saturation channel Equalize image')
plt.imshow(s_2)

plt.subplot(4,4,8)
plt.axis('off')
plt.title('Value channel Equalize image')
plt.imshow(v_2)

plt.subplot(4,4,9)
plt.axis('off')
plt.title('Reconstructed Equalized Image')
plt.imshow(recon_img)

plt.subplot(4,4,10)
plt.axis('off')
plt.title('HSV image histogram')
plt.hist(img_hsv.flatten(), bins=256)

plt.subplot(4,4,11)
plt.axis('off')
plt.title('Hue channel histogram equaliz image')
plt.hist(h_2.flatten(), bins=256)

plt.subplot(4,4,12)
plt.axis('off')
plt.title('saturation channel histogram equaliz image')
plt.hist(s_2.flatten(), bins=256)

plt.subplot(4,4,13)
plt.axis('off')
plt.title('value channel histogram equaliz image')
plt.hist(v_2.flatten(), bins=256)

plt.subplot(4,4,14)
plt.axis('off')
plt.title('histogram for reconstruct image')
plt.hist(recon_img.flatten(), bins=256)

plt.show()
