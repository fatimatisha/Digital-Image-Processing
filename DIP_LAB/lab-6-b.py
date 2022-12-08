import skimage.io as io
import skimage.filters as fl
import matplotlib.pyplot as plt
import skimage.exposure as ex
 
f = io.imread('D:\Fourth Year First Semester\DIP Lab\DIP_Python\Dataset\misc\\7.1.05.tiff')

edge_p=fl.sobel(f)

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(ex.rescale_intensity(f,out_range=(0.0,1.0)),cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Image filtered with Sobel operator')
plt.imshow(ex.rescale_intensity(edge_p,out_range=(0.0,1.0)),cmap='gray')

plt.show()




