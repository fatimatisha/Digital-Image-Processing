import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import rgb2gray
import skimage.filters as fl
import matplotlib.pyplot as plt
import numpy as np

img = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.2.07.tiff')

vg = rgb2gray(img)

vel=fl.sobel(vg)>0.11

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Image filtered with Roberts operator')
plt.imshow(vel)

v2=np.zeros_like(img)
for i in range(3):
    v2[:,:,i] = fl.sobel(img[:,:,2])>0.11

ve2=(v2[:,:,0]+v2[:,:,1]+v2[:,:,2])>0.11

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Image filtered with Roberts operator')
plt.imshow(ve2)
plt.show()


