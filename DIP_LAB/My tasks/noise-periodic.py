import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util
import scipy.ndimage as ndi
import matplotlib.pyplot as plt


img= data.camera()

plt.subplot(2,2,1)
io.imshow(img)

r,c=img.shape
x,y=np.mgrid[0:r,0:c].astype('float32')
p=np.sin(x/3+y/3)+1.0
gp=(2*skimage.util.img_as_float(img)+p/2)/3

plt.subplot(2,2,2)
io.imshow(gp)

io.show()
