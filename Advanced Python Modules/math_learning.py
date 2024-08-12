import math, random
print(math.pi)

# Sampling with and without replacement
my_list = list(range(0,20))
print(my_list)

# With replacement
print(random.choices(population=my_list, k=10))

# Without replacement
print(random.sample(population=my_list, k=10))