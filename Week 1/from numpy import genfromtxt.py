from numpy import genfromtxt
from matplotlib import pyplot as plt
from matplotlib.image import imread
my_data = genfromtxt('greyscaleMatrix.csv', delimiter=',')
plt.imsave('greyscaleImage.png', my_data, cmap='gray')
image_1 = imread('greyscaleImage.png')
# plot raw pixel data
plt.imshow(image_1)
# show the figure
plt.show()