#two.py
import one

print("Top level in two.py")

one.func()

if __name__ == "__main__":
    print("Two.py is being run directly")
else:
    print("Two.py has been imported")

# Execution Result
# Top level in one.py
# one.py has been imported
# top level in two.py
# func() in one.py
# two.py is being run directly