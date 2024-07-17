def square(num):
    return num**2

mynums = [1,2,3,4,5,6,7,8]

for item in map(square, mynums):
    print(item)

def check_even(num):
    return num%2==0

print(list(filter(check_even, mynums)))

for n in filter(check_even, mynums):
    print(n)

# Lambda expression
square = lambda num: num **2
print(square(30))

list(map(lambda num: num**2, mynums))
list(filter(lambda num: num%2==0, mynums))