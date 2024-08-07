class Dog():
    species = "mammal"

    def __init__(self, breed, name, spots): #constructor
        self.breed = breed
        self.name = name
        self.spots = spots
    
    def bark(self):
        print(f"{self.name} Woof!")


my_dog = Dog(breed="Lasa", name="Angela", spots=False)

print(my_dog.breed)

class Animal():
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")

    def who_am_i(self):
        print("I am a dog")

# Polymorphism
print("--Polymorphism--")
class Lizard():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Lizard speaking")

class Gecko():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Gecko speaking")

niko = Lizard("Niko")
felix = Gecko("Felix")

for pet in [niko, felix]:
    print(type(pet))
    print(pet.speak())

# Abstraction
class Book():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Wattpad(Book):
    def speak(self):
        return self.name + " is in the library"

# Magic / Dunder Methods
print('---Magic / Dunder methods')
class Book2():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str: #Overriding in-built functions, that's why we have double underscore
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return int(self.pages)
    
b2 = Book2("Python programming", "Jose Portilla", 10)
print(b2)
print(len(b2))
str(b2)