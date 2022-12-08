import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import math

img= data.camera()

plt.subplot(2,2,1)
io.imshow(img)

m=np.ones((1,7))/7
cm=ndi.correlate(img,m)


plt.subplot(2,2,3)
io.imshow(cm)

io.show()
