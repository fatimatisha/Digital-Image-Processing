import skimage.io as io
import skimage.data as data
import matplotlib.pyplot as plt
import numpy as np

#img1 = data.astronaut()
#img2 = data.coffee()
img1 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//4.1.01.tiff")

r = img1 [:,: , 0]
g = img1 [:, :, 1]
b = img1 [:, :, 2]

plt.subplots_adjust(hspace= 0.5, wspace= 0.5)

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow (img1)

hist, bins = np.histogram(r.ravel(), bins=256,range=(0, 256))

plt.subplot(2, 2, 2)
plt.title('Red Histogram')
plt.bar(bins[:-1] , hist)


hist, bins = np.histogram(g.ravel(), bins=256,range=(0, 256))
plt.subplot(2, 2, 3)
plt.title('Green Histogram')
plt.bar(bins[:-1] , hist)
hist, bins = np.histogram(b.ravel(), bins=256,range=(0, 256))
plt.subplot(2, 2, 4)
plt.title('Blue Histogram')
plt.bar(bins[:-1] , hist)
plt.show ()

