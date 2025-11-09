import random

a = random.random() # give random float number

print(a)

a = random.uniform(1,10)

print(a)

a = random.randint(1,10)

print(a)

a = random.normalvariate(0,1)

print(a)

mylist = list("ABCHSGFIIEJ")

a = random.choice(mylist)

print(a)

a = random.sample(mylist, 4)

print(a)

random.shuffle(mylist)

print(mylist)



