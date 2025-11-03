# map, filter, reduce
from functools import reduce

a = [1, 2, 3, 4, 5]

b = map(lambda x: x*2, a)
print(list(b))
b = [x*2 for x in a]
print(b)

c = filter(lambda i: i % 2 == 0, a)
print(list(c))
c = [x for x in a if x % 2 == 0]
print(c)

d = reduce(lambda x, y: x*y, a)
print(d)
