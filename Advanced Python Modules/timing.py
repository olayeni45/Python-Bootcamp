import time, timeit

# Method 1
# Grab the current time before
# Run the code
# Current time after running
# Elapsed time = Time after - time before

start_time = time.time()

def func_one(n):
    return [str(num) for num in range(n)]

result = func_one(1000000)

end_time = time.time()
elapsed_time = end_time - start_time

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=10))

print(f"Func One {elapsed_time}")

start_time = time.time()

def func_two(n):
    return list(map(str, range(n)))

result = func_two(1000000)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Func two {elapsed_time}")