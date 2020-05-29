import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter():
    """Change color of img"""

    def invert(self, array):
        invert = array[:, :, :3]
        invert[:] = 1 - invert[:]
        return array

    def to_blue(self, array):
        blue_array = np.zeros(array.shape)
        blue_array = array[:, :, :2]
        blue_array[:] = 0
        return array

    def to_green(self, array):
        tmp = array[:, :, 0:3:2]
        tmp *= 0.0
        return array

    def to_red(self, array):
        array[:, :, 1:3] = 0
        return array

    def celluloid(self, array):
        pass


i = ImageProcessor()
cfilter = ColorFilter()
array = i.load("elonmuskjoint.png")
array = cfilter.invert(array)
i.display(array)
