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

r,c=img.shape
x,y=np.mgrid[0:r,0:c].astype('float32')
p=np.sin(x/3+y/3)+1.0
gp=(2*skimage.util.img_as_float(img)+p/2)/3

plt.subplot(2,2,2)
io.imshow(gp)

z=np.sqrt((x-200)**2+(y-200)**2)
k=1
d=math.sqrt(610.0)

br = ((z<np.floor(d-k)) | (z>np.ceil(d+k)))
cfr=br*gp
plt.subplot(2,2,3)
io.imshow(cfr)

io.show()
