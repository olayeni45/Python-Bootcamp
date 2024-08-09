def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet():
        return "\t This is the greet() function inside hello"
    
    def welcome():
        return "\t This is welcome() inside hello"
    
    print("I am going to return a function")

    if name == "Jose":
        return greet
    else:
        return welcome
    

def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function!")

    return wrap_func