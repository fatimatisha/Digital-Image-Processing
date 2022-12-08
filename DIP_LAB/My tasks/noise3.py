import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


img01= data.camera()

plt.subplot(2,2,1)
io.imshow(img01)


plt.subplot(2,2,2)
img02= noise.random_noise(img01,mode='speckle')
io.imshow(img02)

plt.subplot(2,2,3)
img05= ndi.median_filter(img02,3)
io.imshow(img05)

io.show()
