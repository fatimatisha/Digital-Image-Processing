import skimage.io as io
import skimage.data as data
import skimage.transform as tr
import numpy as np
import math

c = data.camera()
r = range(-256,256)
[x,y] = np.meshgrid(r,r)
#z = math.sqrt(x**2 + y**2)
#t = 1-((z>254.5) & (z<256))*1
io.imshow(c)

cr = tr.rescale(c,0.25,order=3)

io.imshow(cr, cmap='gray')
io.show()



