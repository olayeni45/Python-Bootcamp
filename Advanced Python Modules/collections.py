from collections import Counter, defaultdict, namedtuple
my_list=[1,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5]

print(Counter(my_list))

sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['wrong key']) # returns 0 and not an exception

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=10, breed="Husky", name="Sam")
print(type(sammy))
print(sammy.age)