import numpy as np
import skimage.io as io

import matplotlib.pyplot as plt
import pywt

c = io.imread('D:\\Fourth Year First Semester\\DIP Lab\\DIP_Python\\Dataset\\misc\\4.1.01.tiff')

plt.imshow(c, cmap='gray')
plt.show()
coeffs2 = pywt.dwt2(c,'db2')

cA,(cH,cV,cD)= coeffs2

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Approximate image LL')
plt.imshow(cA, cmap='gray')

plt.subplot(2,2,2)
plt.axis('off')
plt.title('Horizontal detail image LH')
plt.imshow(cH, cmap='gray')

 
plt.subplot(2,2,3)
plt.axis('off')
plt.title('Vertical detail image HL')
plt.imshow(cV, cmap='gray')

plt.subplot(2,2,4)
plt.axis('off')
plt.title('Diagonal detail image HH')
plt.imshow(cD, cmap='gray')

plt.show()  

