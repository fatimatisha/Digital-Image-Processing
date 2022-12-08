import skimage.io as io
import skimage.data as data
import skimage.transform as tr
import numpy as np
import math

c = data.camera()
head =c[33:200,90:353]

io.imshow(c)
io.show()
cr = tr.rescale(head,2,order=0)

io.imshow(cr, cmap='gray')
io.show()



