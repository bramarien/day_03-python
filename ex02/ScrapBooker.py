import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker():
    """Slicing"""

    def crop(self, array, dimensions, position=(0, 0)):
        if dimensions[1] <= array.shape[0] and dimensions[0] <= array.shape[1]:
            return array[position[1]:dimensions[1] + position[1],
                         position[0]:dimensions[0] + position[0]]

    def thin(self, array, n, axis):
        return np.delete(array, [range(n-1, array.shape[axis], n)], axis)

    def juxtapose(self, array, n, axis):
        return np.concatenate([array for i in range(n)], axis)

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)


img = ImageProcessor()
scrap = ScrapBooker()
m = np.array(range(20)).reshape(4, 5)
print(m)
# print(np.tile(m, [2,2]).shape)
print(scrap.thin(m, 2, 1))
# print(scrap.mosaic(m, [5,5]))
