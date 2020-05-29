import numpy as np
import matplotlib.pyplot as plt


class ImageProcessor():
    """class for load and print a png in array"""

    def load(self, path):
        arrayimg = plt.imread(path)
        return arrayimg

    def display(self, array):
        img = plt.imshow(array)
        plt.show()


i = ImageProcessor()
array = i.load("rick.png")
i.display(array)
