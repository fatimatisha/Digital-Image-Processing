import numpy as np
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = np.zeros((256,256))
c[77:177,77:177]=1
cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Cameraman image')
plt.imshow(c, cmap='gray')

plt.subplot(2,2,2)
plt.axis('off')
plt.title('DFT of an created image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)),cmap='gray')


plt.show()

