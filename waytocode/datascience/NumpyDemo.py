import numpy as np

# single dimension
# num = [1, 2, 3, 4, 5]
# data = np.array(num)
# print(data)


# multi dimension

num = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
data = np.array(num)
print(data)


# initialization zeros

# num = np.zeros([4, 4])
# print(num)

# initialization with same number

# num = np.full((4, 4), 2)
# print(num)


# initialization with range

# num = np.arange(1, 11)
# print(num)

# num = np.arange(0, 101, 5)
# print(num)


# initialization with random number

# num = np.random.randint(10, 20, 5)
# print(num)


# Mean, Median and Standard Deviation

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data = np.array(num)
# dataMean = np.mean(data)
# print(dataMean)

# num = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# data = np.array(num)
# dataMed = np.median(data)
# print(dataMed)

# dataStd = np.std(data)
# print(dataStd)


# save and read(load)

# num = np.array([1, 2, 3, 4, 5])
# data = np.save("numpydocument", num)
# print(data)

# loadData = np.load('numpydocument.npy')
# print(loadData)

