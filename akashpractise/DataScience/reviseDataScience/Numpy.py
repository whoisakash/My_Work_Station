import numpy as np
# print(np.__version__)

# 2. Numpy Array
# a = np.array([[1,2,3,4,5,6],[2,5,7,8,9,10]])
# a = np.array([1,2,3,4,5,6])
#
# print(type(a),a)
# print(a.shape,"Shape of array")
# print(a.dtype,"type of elements")
# print(a.ndim,"Number of dimention")
# print(a.size,"Total number of element")
# print(a.itemsize,"the size in bytes of each element")


# Essential mwthods:
a = np.array([1,3,6])

# access and change element
print(a[0])
a[0]= 5
print(a)

# Elementvice maths operation
b = a * np.array([2,2,5])
print(b)

# 3. Numpy Array vs List:
l = [1,2,3]
a= np.array([1,2,3])

# multiplication for eac element
l2 = l*2
print("\n",l2)

a2 = 2*a
print(a2)

# Note: Fuction applied to array usually operates element wise!

#4. Dot product

a= np.array([1,2])
b= np.array([3,4])

dot= 0
for i in range(len(a)):
    dot += a[i] * b[i]
print("dot is",dot)

# easy with numpy:)
dot = np.dot(a,b)
print(dot,"dot with numpy")

# most  of these function are instance methods
dot = a.dot(b)
print(dot," dot wit instance")

# in newer version
dot = a @ b
print(dot,"newer version with @")

# 5. Speed test Array vs list
from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)
A = list(a)
B = list(b)
T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
        return dot
def dot2():
    return np.dot(a, b)

start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end-start

# print('Time with lists:', t1) # -> 0.19371
# print('Time with array:', t2) # -> 0.00112
# print('Ratio', t1/t2) # -> 172.332 times faster

# 6. Multidimensional (nd) Arrays
# (matrix class exists but not recommended to use)
a = np.array([[1,2], [3,4]])
print(a)
# [[1 2]
# [3 4]]
print(a.shape) # (2, 2)
# Access elements
# row first, then columns
print(a[0]) # [1 2]
print(a[0][0]) # 1
# or
print(a[0,0]) # 1
# slicing
print(a[:,0]) # all rows in col 0: [1 3]
print(a[0,:]) # all columns in row 0: [1 2]
# transpose
a.T
# matrix multiplication
b = np.array([[3, 4], [5,6]])
c = a.dot(b)
d = a * b # elementwise multiplication
# inner dimensions must match!
b = np.array([[1,2,3], [4,5,6]])
c = a.dot(b.T)
# determinant
c = np.linalg.det(a)
# inverse
c = np.linalg.inv(a)
# diag
c = np.diag(a)
print(c) # [1 4]
# diag on a vector returns diagonal matrix (overloaded function)
c = np.diag([1,4])
print(c)
# [[1 0]
# [0 4]]


