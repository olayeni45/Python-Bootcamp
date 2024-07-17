def name_of_function(name):
    '''
    Print Hello
    '''
    print(f"Hello {name}")

name_of_function("Jose")

def add_function(num1, num2):
    return float(num1) + float(num2)

result = add_function(1, '2')
print(result)

work_hours = [("Anna", 500), ("Billy", 300), ("Sandra", 900)]

def employee_check(work_hours = [()]):
    maxHour = 0
    employee = ""

    for name, hour in work_hours:
        if hour > maxHour:
            maxHour = hour
            employee = name
        else:
            pass
    
    return (employee, maxHour)

name, hour = employee_check(work_hours)
print(name)
print(hour)

# *Args (Arguments) and **Kwargs (Key Word Arguments)
# *Args returns a tuple while **kwargs returns a dictionary
def myfunc(*args):
    print(args)

myfunc(1,2,3,4,5,6)

def myfunc2(**kwargs):
    print(kwargs)

myfunc2(fruit="Guava", veggie="Lettuce")

def myfunc3(word):
    result = ""

    for index, letter in enumerate(word):
        if index % 2 == 0:
            result += str(letter).upper()
        else:
            result += str(letter).lower()
    
    return result

print(myfunc3("Hellord"))