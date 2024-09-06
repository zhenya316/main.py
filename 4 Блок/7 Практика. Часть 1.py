from sortfunc123 import *
import time

nums = [1, 6, 6, 3, 1, 9]

start = time.perf_counter()
finish = time.perf_counter()
time_1 = finish - start
print(start)
print(finish)
print(start, bubble_sort(nums), finish)     # время выполнения кода