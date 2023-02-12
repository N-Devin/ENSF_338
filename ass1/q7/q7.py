import timeit

def fib(n): 
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_for_loop():
    for i in range(30):
        fib(i)
def list_comp():
    [fib(i) for i in range(30)]

for_loop_val = timeit.timeit(lambda: fib_for_loop(), number=100)
print("for loop Executed in ",for_loop_val)

list_comp_val = timeit.timeit(lambda: list_comp(), number=100)
print("list comprehension Executed in ",list_comp_val)
