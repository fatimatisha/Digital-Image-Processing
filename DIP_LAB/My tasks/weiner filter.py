import numpy as np
import skimage.io as io
import skimage.data as data
import skimage.util.noise as noise
import scipy.ndimage as ndi
from scipy.signal import wiener


img01= data.camera()

io.imshow(img01)
io.show()

img02= noise.random_noise(img01,mode='s&p',amount=0.05)
io.imshow(img02)
io.show()

img03= wiener(img02,[3,3])
io.imshow(img03)
io.show()
