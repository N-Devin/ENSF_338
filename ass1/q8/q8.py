from time import perf_counter
t1_start = perf_counter()
with open('q8.txt', 'r') as inp:
    y = inp.read().upper()
with open('q8_out.txt', 'a') as out:
    out.write(y)
t1_stop = perf_counter()
print("Elapsed time:", t1_stop-t1_start)
