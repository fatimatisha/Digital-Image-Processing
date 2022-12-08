import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


img01= data.camera()

plt.subplot(3,3,1)
io.imshow(img01)


plt.subplot(3,3,2)
img02= noise.random_noise(img01,mode='s&p',amount=0.1)
io.imshow(img02)


plt.subplot(3,3,3)
img03= noise.random_noise(img01,mode='s&p',amount=0.15)
io.imshow(img03)


plt.subplot(3,3,4)
img04= noise.random_noise(img01,mode='s&p',amount=0.2)
io.imshow(img04)


plt.subplot(3,3,5)
img05= ndi.median_filter(img02,3)
io.imshow(img05)

plt.subplot(3,3,6)
img06= ndi.median_filter(img03,3)
io.imshow(img06)

plt.subplot(3,3,7)
img07= ndi.median_filter(img04,3)
io.imshow(img07)

io.show()
