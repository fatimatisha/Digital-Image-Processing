import numpy as np
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt
import math 

a=np.array([[4,5,-9,-5],[3,-7,1,2],[6,-1,-6,1],[3,-1,7,-5]])

al=np.fft.fft(a)
print(al)
