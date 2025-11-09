# Generators are functions that return object that can be iterated over and they generate the items inside the object lazily which
# means they genarate the items only one at a time and only when you ask for it because of this they much more memory efficient than other objects when you have deal with large datasets.


def mygenerator():
  yield 3
  yield 2
  yield 1
  
g = mygenerator()
# for i in g:
#   print(i)
  
# res = sum(g)
# print(res)

# sorted(g)

print(sorted(g))

def countdown(num):
  print("Starting")
  while num > 0:
    yield num
    num -= 1
    
cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))
print(next(cd))

def firstin_generator(n):
  num = 0
  while n > 0:
    yield num
    num += 1
    n -= 1
    
print(sum(firstin_generator(10)))

# fibonacci - > 0, 1, 1, 2, 3, 5, 8

def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a+b

fib = fibonacci(10)

for i in fib:
  print(i)

import sys

mygenerator = (i for i in range(1000000) if i%2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(1000000) if i%2 == 0]
print(sys.getsizeof(mylist))

 
