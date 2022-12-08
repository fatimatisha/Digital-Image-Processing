import numpy as np
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt

x,y = np.meshgrid(range(256),range(256))
b = (x+y<329)&(x+y>182)&(x-y>-67)&(x-y<73)
plt.subplot(2,2,1)
plt.axis('off')
plt.title('Cameraman image')
plt.imshow(b, cmap='gray')

bf = np.fft.fft2(b)
bfs = np.fft.fftshift(bf)
bfsl = np.log(1+np.abs(bfs))




plt.subplot(2,2,2)
plt.axis('off')
plt.title('DFT of an created image')
plt.imshow(ex.rescale_intensity(bfsl,out_range=(0.0,1.0)),cmap='gray')


plt.show()

