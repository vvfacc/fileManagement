import numpy as np
from numpy import dtype

# #Learning Numpy
# a = np.array([[1, 2, 3], [4, 6, 7]], dtype = 'int16')
# print(a[0][0])
# #Dimension
# print(a.ndim)

# #shape
# print(a.shape)

# #type
# print(a.dtype)

# #size
# print(a.itemsize, 'byte')

#zero matrix
b = np.zeros((3, 3))

#1s matrix
c = np.ones((3, 3))

#identity
d = np.identity(4)

print(d)