# '''Numpy Arrays much faster than lists'''
#
# import numpy as np
# import time
#
# l=[]
# lsub=[]
# for i in range(100):
#     lsub=[]
#     for j in range(100):
#         lsub.append(0)
#     l.extend([lsub])
#
# a=np.zeros((100,100))
# tl1=time.time()
# for i in range(100):
#     for j in range(100):
#         l[i][j]=l[i][j]+5
#
# tl2= time.time()
# t1=tl2-tl1
# ta1=time.time()
# ArrayOp= "a=a+10"
# ta2=time.time()
# ta= ta2-ta1
# print(ta)
# print(t1)

# replace work
# st1= "Hey John. How are you, john e e e?".replace ("e", "E",3)
# print(st1)
# Output: "Hey John. How are you, john?"

# del and remove from list
# a= list("abcd")
# print(a[1:3])
# del a[1:3]
# print(a,type(a))
#
# b= list("wxyz")
# b.remove("x")
# print(b)

# append and expand
#
# lst =[1,2,3]
# lst.append([4,5,6])
# print(lst)
#
# lst.extend([7,8,9])
# print(lst)

# function
# def adddtolist(val, list=[]):
#     list.append(val)
#     return list
# l1 = adddtolist(1)
# l2 = adddtolist(123,[])
# l3 = adddtolist('a')
# print("l3 = %s%s"%l3)

# split use
# var = "r,g,b,y"
# lst= var.split(",")
# print(lst)


# item = [{"a": [1, 2, 3, 4, 5]}]
# print(type(item))
# item = item[0]
# print(len(item["a"]))
# print(item["a"][4])

# item = [1, 2, 3, 4, 5]  # print list with multiple of 2
# item = [1, 2, 3, 4, 5]
# item1=[]
# def mluti(num):
#     for i in item:
#         item1.append(i*num)
# mluti(2)
# print(item1)

"even no. print in "
item = [1, 2, 3, 4, 5]
even = [i for i in item if i % 2 == 0]
# even = []
# for i in item:
#     if i%2==0:
#         even.append(i)
print(even)

# arr = [i * 2 for i in item]
# print(arr)


# item = [{"a": [{"b": 1}, 2, 3, 4, 5]}]
# item = item[0]
# print(item)
# item = item["a"][0]
# print(item[0]["a"][0]["b"])
