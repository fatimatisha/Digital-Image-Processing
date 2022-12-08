import cv2
import numpy as np
import pywt

image=cv2.imread('1.tif')
image=cv2.resize(image,(256,256))
[b,g,r]=cv2.split(image)
x=b
coffes=pywt.dwt2(x,'haar')
ca,(ch,cv,cd)=coffes
ca2=np.uint8(ca)
ch2=np.uint8(ch)
cv2=np.uint8(cv)
cd2=np.uint8(cd)
coffes=ca2,(ch2,cv2,cd2)
origin=pywt.idwt2(coffes,'haar')
cv2.imshow('image',origin)
cv2.waitKey(0)
cv2.destroyAllWindows()
