from random import shuffle, randint

isHungry = True

if isHungry:
    print("Feed my dog")
else:
    print("Dog has been fed")

count = 10
if count > 5:
    print("Greater than 5")
elif count > 10:
    print("Greater than 10")
else:
    print("Default else")

#Loops
my_iterable = [1,2,3,4]

for item in my_iterable:
    print(item)

for letter in 'Hello World':
    print(letter)

# Tuple Unpacking - Duplicate the structure of the item in a list
my_list = [(1,2), (3,4), (5,6), (7,8), (9,10)]

for a,b in my_list:
    print(a)
    print(b)

# Dictionary
dict = {"k1": 1, "k2": 2, "k3": 3}

for (key, value) in dict.items():
    print(value)

# While Loops
x = 0

while x < 5:
    print(f" The current value of x is {x}")
    x+=1
else:
    print(f"X is not less than 5: {x}")

# Break, Continue, Pass
# We can use break, continue, and pass statements in our loops to add additional functionality for various cases. 
# The three statements are defined by:
# •	Break: Breaks out of the current closest enclosing loop
# •	Continue: Goes to the top of the closest enclosing loop
# •	Pass: Does nothing at all

x = [1,2,3]

for item in x:
    pass

mystring = 'Sammy'

for letter in mystring:
    if letter == "a":
        continue
    print(letter) #s m m y

x = 0

while x < 5:
    if x == 2:
        break
    print(f" The current value of x is {x}")
    x+=1

# Useful Operators
for num in range(0,11,2):
    print(num) #Prints out even numbers from 0 to 10

index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

# Enumerate works like a for i=0; loop
# It returns the (index, value) as a tuple
for index, letter in enumerate(word):
    print(f"Index: {index}, Letter: {letter}")

# The zip function pairs up elements from lists and returns the result as a tuple
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1, mylist2): 
    print(item)

print(list(zip(mylist1, mylist2)))

# In operator
print(2 in [1,2,3])
print('x' in ['x', 'y', 'z'])

my_list = [1,2,3,4,5,6,7]
shuffle(my_list)
print(my_list)

# Input
userInput = input("Enter a number here: ")
print(userInput)

mystring = "hello"
my_list = [letter for letter in mystring]
print(my_list)

celcius = [0,10,20,34.5]
fahrenheit = [( ((9/5) * temp) + 32) for temp in celcius ]
print(fahrenheit)