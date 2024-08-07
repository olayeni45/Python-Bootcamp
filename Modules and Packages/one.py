#one.py

def func():
    print("Func() in one.py")

print("Top level in one.py")

if __name__ == "__main__": #Python under the hood sets the __name__ variable to 'main' if the script is called directly on the terminal
    print("One.py is being run directly")
else:
    print("ONE.py has been imported")

# Execution Result
# Top level in one.py
# one.py is being run directly