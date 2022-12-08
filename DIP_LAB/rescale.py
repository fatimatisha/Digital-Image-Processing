import skimage.io as io
import skimage.data as data
import skimage.transform as tr

c = data.camera()
head=c[32:296,189:253]
io.imshow(head,cmap='gray')
io.show()
head4n = tr.rescale(head,2,order=0) #order (default is 1) is the polynomial order of the interpolation.
head4n = tr.rescale(head,2,order=1)

io.imshow(head4n,cmap='gray')
io.show()



