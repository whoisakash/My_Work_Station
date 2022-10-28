# myList = []
#
# myList.append("a")
# myList.append("b")
# myList.append("c")
# myList.append("d")
# myList.append("e")
#
# print(myList)
#
# print(myList.pop(0))
# print(myList.pop(0))
# print(myList.pop(0))
#
# print(myList)


'''try enqueue and dequeue'''

# .pop() = FIFO(First in first out)
# .pop(0) = LIFO(Last in first out)

# stock_price = []
# stock_price.insert(0,132.21)
# stock_price.insert(0,133.50)
# stock_price.insert(0,135.30)
# print(stock_price)
# stock_price.pop()
# stock_price.pop()
# stock_price.pop()
# stock_price.pop()
# print(stock_price)

# deque()
from collections import deque
d=deque()
d.appendleft(5)
d.append(6)
d.appendleft(10)
d.appendleft(15)
d.appendleft(20)
d.appendleft(25)
print(d)
# d.pop()
# print(d)

"""enqueue= example...placing people in queue for buying ticket
   dequeue= example...you bought ticket now out of the queue """
# class Queue:

