from multiprocessing import Process
import os
import time

def square_numbers(n):
  for i in range(n):
    i * i
    time.sleep(0.1)
    

processes = []

num_processes = os.cpu_count()
print(num_processes)

# create a process
for i in range(num_processes):
  p = Process(target=square_numbers, args=(100,))
  processes.append(p)
  
for n in processes:
  n.start()
  
for p in processes:
  p.join()
  
print("end main")


from threading import Thread

threads = []
num_threads = 10

for i in range(num_threads):
  t = Thread(target=square_numbers, args=(100,))
  threads.append(t)

for n in threads:
  n.start()
  
for p in threads:
  p.join()
  
print("end main")