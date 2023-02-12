import json
import matplotlib.pyplot as plt
import sys
import timeit

sys.setrecursionlimit(20000)
def un_optimized_sort(arr, low, high):
    if low < high:
        pi = unoptimized_quicksort(arr, low, high)
        un_optimized_sort(arr, low, pi-1)
        un_optimized_sort(arr, pi + 1, high)

def unoptimized_quicksort(array, start, end):
    p = array[start] #p 10
    low = start + 1 # low = 1
    high = end      # high = 5
    while True:
        while low <= high and array[high] >= p:     # 5 >= 10
            high = high - 1
        while low <= high and array[low] <= p:      #  <= 10
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("q2.json", "r") as inF:
    arr = json.load(inF)

def unoptimized_call(i):
    unoptimized = un_optimized_sort(arr[i], 0, len(arr[i])-1)

unoptimized_array_y = []
array_x = []

for i in range(len(arr)):
    unoptimized_time = timeit.timeit(lambda: unoptimized_call(i), number=1)
    unoptimized_array_y.append(unoptimized_time)
    array_x.append(len(arr[i]))


# plotting the points 
plt.plot(array_x, unoptimized_array_y, label = "unoptimized_call")
  
# naming the x axis
plt.xlabel('Number of elements in array')
# naming the y axis
plt.ylabel('execution time (seconds)')
# adding a legend
plt.legend()
  
# function to show the plot
plt.show()

