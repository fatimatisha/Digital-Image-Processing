import skimage.data as data
import matplotlib.pyplot as plt

img_01 = data.astronaut()
img_02 = data.brick()
img_03 = data.coins()

plt.subplot(2,2,1)
plt.axis('off')
plt.title('Color image')
plt.imshow(img_01)

plt.subplot(2,2,2)
plt.axis('off')
plt.title('Gray Scale image')
plt.imshow(img_02,cmap='gray')

plt.subplot(2,2,3)
plt.axis('off')
plt.title('Indexed Image')
plt.imshow(img_03)

plt.show()
