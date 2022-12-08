import skimage.io as io
import matplotlib.pyplot as plt

img_01 = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.1.01.tiff')
img_02 = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\5.1.12.tiff')


plt.subplot(5,5,1)
plt.axis('off')
#plt.title('Color image ... .')
plt.imshow(img_01)

plt.subplot(5,5,2)
plt.axis('off')
#plt.title('Grayscale image.')
plt.imshow(img_02,cmap='gray')

plt.show()

