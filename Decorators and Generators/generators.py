def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

def create_cubes_generator(n):
    for x in range(n):
        yield x**3

def gen_fibonacci_generator(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

# A generator returns an iterable object so we have to loop through it
for num in gen_fibonacci_generator(10):
    print(num)

def fibonacci(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b, a+b
    
    return output

word = "hello"
word_iterator = iter(word)