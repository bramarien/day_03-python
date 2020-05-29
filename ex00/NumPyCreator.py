import numpy as np


class NumPyCreator():
    """lolilol"""
    def from_list(self, lst, dtype=None):
        return np.array(lst, dtype)

    def from_tuple(self, tpl, dtype=None):
        return np.array(tpl, dtype)

    def from_iterable(self, itr, dtype=None):
        return np.array(itr, dtype)

    def from_shape(self, shape, value=0, dtype=None):
        return np.full(shape, value, dtype)

    def random(self, shape):
        return np.random.random_sample(shape)

    def identity(self, n, dtype=None):
        return np.identity(n, dtype)


npc = NumPyCreator()
print(npc.from_shape((5, 2), 0))
