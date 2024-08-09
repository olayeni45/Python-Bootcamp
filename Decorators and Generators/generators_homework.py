import random

print("--Q1--")
def gensquares(n):
    for x in range(n):
        yield x**2

for x in gensquares(10):
    print(x)

print("--Q2--")
def rand_num(low, high, n):
    for x in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

print("--Q3--")
s = "hello"
s_iter = iter(s)
for x in s_iter:
    print(x)

print("--Q4--")
'''
Use Case: Printing the square of numbers between 1 and 10,000
A generator is best suited for this action because it does not store the values in memory,
instead, it returns the next value of the iteration based on the formula provided, hence
more memory efficient

If the output has the potential of taking up a large amount of memory and you only intend to iterate
through it, you would want to use a generator here
'''

print("--Q5--")
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)