import numpy as np
# 2D array
# my_array_2D = np.array([12,25,10,5])

# 3D array
my_array = np.array([[12,25,10,5]],np.int64)

# np.int 8/32/64 for memory mangement
# my_array = np.array([12,2556,10,5],np.int32)

# .shape to know size
# print(my_array.shape)

# return memory type np.int64/32 etc
# print(my_array.dtype)

# Element change
my_array[0,2]=200
print(my_array)