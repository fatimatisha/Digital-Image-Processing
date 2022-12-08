#adaptive thresholding
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import skimage.exposure as ex
import skimage.filters as fl

p = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\All tasks\\rice.png').astype(float)

r,c=p.shape
x,y=np.mgrid[0:r,0:c].astype(float)
p2=255.0-p+y/2
plt.subplot(2,1,1)

plt.imshow(p, cmap='gray')

t=fl.threshold_otsu(p2)

plt.subplot(2,1,2)
plt.axis('off') 
plt.title('Adaptive thresholded image')
plt.imshow(p2>t,cmap='gray')

plt.show()




