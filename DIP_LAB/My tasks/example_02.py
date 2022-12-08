import skimage.io as io
import skimage.data as data
#img = data.astronaut()
img = data.coffee()
#img =io.imread("D://Fourth Year First Semester//DIP Lab//DIP_Python//Dataset//misc//4.2.07.tiff")
print(type(img))
io.imshow(img)
io.show()
