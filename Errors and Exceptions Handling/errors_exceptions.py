try:
    result = 10 + 10
except:
    print("Hey it looks like you are not adding the code correctly")
else: # executes if no exception occured
    print("Addition went well")
    print(result)
finally: # executes irrespective of an error
    print("Finally block")