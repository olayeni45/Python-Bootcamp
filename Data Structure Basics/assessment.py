# Question 1
# Numbers: Whole numbers (30, 300, 20)
# Strings: Ordered sequence of characters ("Hello World")
# Lists: ordered sequence of elements [10,20,30]
# Tuples: ordered immutable sequence of objects (10, 20, 30)
# Dictionaries: Unordered Key Value Pairs {"age": 20, "name": "Yenssss"}
# Sets: Unordered collection of unique objects {"a", "b"}

# Question 2
question2 = ((5**2)*4) / 2 + 50.25 - 0
print(question2)

# Question 3
a = 4 * (6 + 5) #44
b = 4 * 6 + 5 #29
c = 4 + 6 * 5 #34
print(a)
print(b)
print(c)

# Question 4
d = 3 + 1.5 + 4 #float
print(type(d))

# Question 5
# squareroot (num**0.5)
# square (num**num)

# Question 6
s = "hello"
print(s[1])
print(s[::-1])
print(s[1:2])

# Question 7
list1 = [0,0,0]
list2 = list()
list2.append(0)
list2.append(0)
list2.append(0)
print(list1)
print(list2)

list3 = [1,2,[3,4,"hello"]]
list3[2][2] = "goodbye"
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

# Question 8
q = {'simple_key':'hello'}
print(q['simple_key'])

w = {'k1':{'k2':'hello'}}
print(w['k1']['k2'])

e = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(e['k1'][0]['nest_key'][1][0])

r = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(r['k1'][2]['k2'][1]['tough'][2][0])

# Dictionaries cannot be sorted because they are unordered

# Tuples
# The major difference between a tuple and a list is that a tuple is immutable
myTuple = (1,2,3)

# Set returns unique elements
print(set([1,2,2,33,4,4,11,22,3,3,2]))

# Booleans
print(2>3) #false
print(3<=2) #false
print(3 == 2.0) #false
print(3.0 == 3) #true
print(4**0.5 != 2) #false

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False? False
print(l_one[2][0] >= l_two[2]['k1'])