import skimage.io as io
import matplotlib.pyplot as plt
import skimage.filters as fl
from skimage.color import rgb2gray

#from skimage.color import rgb2ind



#plt.title('Color image of the astronaut Eileen Collins.')

#[y,map] = rgb2ind
img1 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//indexed-image2.jpg")
img_gray = rgb2gray(img1)
img2=fl.sobel(img_gray)
plt.imshow(img2)
plt.show()
