# a decorator is a function that takes another function as argument
# and extends the behavior of this function without explicitly
# modifying it

# It allow you to add new functionalities to a function

def start_end_decorator(func):
  
  def wrapper(*args, **kwargs):
    print("Before")
    result = func(*args, **kwargs)
    print("After")
    return result
    
  return wrapper

@start_end_decorator
def print_name():
  print("Riya")
  
print_name()


@start_end_decorator
def add_num(x):
  return x + 5

result = add_num(5)

print(result)

import functools

def repeat(num_times):
  def decorator_repeat(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
        
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=4)
def print_name(name):
  print(name)
  
print_name("Riya")


# class decorator

class CountCalls:
  
  def __init__(self, func):
    self.func = func
    self.num_calls = 0
    
  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f'This is executed {self.num_calls} times')
    return self.func(*args, **kwargs)
  

@CountCalls
def say_hello():
  print('Hello')
  

say_hello()
say_hello()

# Usage - to get the count of function executions, to debug the code, check if the arguments are fulfilling the requirements


