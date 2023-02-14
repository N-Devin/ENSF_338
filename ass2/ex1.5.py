import timeit
import matplotlib.pyplot as plt

def unoptimized_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        result =  unoptimized_fib(n-1) + unoptimized_fib(n-2)
        return result

def optimized_fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    elif n in memo:
        return memo[n]
    else:
        result =  optimized_fib(n-1, memo) + optimized_fib(n-2, memo)
        memo[n] = result
        return result

def unoptimized_fib_call(n):
    unoptimized_fib(n)

def optimized_fib_call(n):
    optimized_fib(n)

unoptimized_array_y = []
optimized_array_y = []
array_x = []

for i in range(35):
    unoptimized_time = timeit.timeit(lambda: unoptimized_fib_call(i), number=1)
    unoptimized_array_y.append(unoptimized_time)

    optimized_time = timeit.timeit(lambda: optimized_fib_call(i), number=1)
    optimized_array_y.append(optimized_time)
    
    array_x.append(i)

# plotting the points 
plt.plot(array_x, unoptimized_array_y, label = "unoptimized_fib_call")
plt.plot(array_x, optimized_array_y, label = "optimized_fib_call")
  
# naming the x axis
plt.xlabel(' execution time (seconds)')
# naming the y axis
plt.ylabel('nth input number')
# adding a legend
plt.legend()
  
# function to show the plot
plt.show()
