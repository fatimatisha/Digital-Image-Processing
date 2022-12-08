import skimage.io as io
import skimage.data as data
import matplotlib.pyplot as plt
import numpy as np

#img1 = data.astronaut()
#img2 = data.coffee()
img1 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//4.1.04.tiff")

r = img1 [:,:, 0]
g = img1 [:, :, 1]
b = img1 [: ,:, 2]

output = [img1, r, g, b]
titles = ['Image', 'Red', 'Green', 'Blue']
for i in range (4) :
    plt.subplot(2, 2, i+1)
    plt.axis ('off')
    plt.title(titles[i] )
    if i == 0:
        plt.imshow(output[i] )
    else:
        plt.imshow(output[i], cmap='gray')
plt.show()

