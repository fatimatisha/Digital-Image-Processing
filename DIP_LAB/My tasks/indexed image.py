import skimage.io as io
import matplotlib.pyplot as plt
#from skimage.color import rgb2ind



#plt.title('Color image of the astronaut Eileen Collins.')

#[y,map] = rgb2ind
img1 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//indexed-image2.jpg")


plt.imshow(img1)
plt.show()
