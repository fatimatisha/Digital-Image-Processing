import skimage.io as io
import skimage.data as data
import matplotlib.pyplot as plt
import numpy as np

#img1 = data.astronaut()
#img2 = data.coffee()
img1 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//4.1.06.tiff")
#img2 =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//5.3.01.tiff")

#print(type(img))

nrows, ncols, channels = img1.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows/2, ncols/2
outer_disk_mask = ((row - cnt_row) ** 2 + (col - cnt_col) ** 2 > (nrows/2) ** 2)
img1.setflags(write=1)
img1[outer_disk_mask]=0
plt .imshow (img1)
plt.axis ('off' )
plt.title('Masked Image')
plt .show()
