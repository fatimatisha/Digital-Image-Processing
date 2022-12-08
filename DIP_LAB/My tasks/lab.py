
import skimage.io as io
import skimage.data as data
import matplotlib.pyplot as plt
import numpy as np

#img1 = data.astronaut()
#img2 = data.coffee()
img1 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//4.1.06.tiff")
img2 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//5.3.01.tiff")

#print(type(img))

plt.subplot(1,2,1)
io.imshow(img1)
print(img1.min())
print(img1.max())
print(img1.mean())
print(np.median(img1))
print(np.average(img1))
print(np.mean(img1))
print(np.std(img1))
print(np.var(img1))
plt.subplot(1,2,2)
io.imshow(img2)
io.show()
